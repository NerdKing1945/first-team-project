# 로케이터 리스트를 반복하여 조인트 생성 및 Y값 적용
#같은 변수를 사용하고 싶어서 스크립트를 합치는걸 꺼렸는데.. 변수 이름만 바꾸니 생각보다 굉장히 쉽게 기능을 구현했다. 

import maya.cmds as cmds

def createJoints():
    for locator_list in [brow_locator_list, eyelow_locator_list, cheek_locator_list, nasoFolds_locator_list]:
        for locator_name in locator_list:
            # 로케이터의 Y값 가져오기
            locator_y_position = cmds.getAttr(locator_name + ".translateY")
            locator_x_position = cmds.getAttr("centre_Ultimate_Loc.translateX")
            locator_z_position = cmds.getAttr("centre_Ultimate_Loc.translateZ")
            
            # 조인트 이름 설정
            joint_name = "__centre_" + locator_name.replace("_loc", "_jnt")  # 로케이터 이름을 조인트 이름에 추가
            
            # 센터 조인트 생성
            cmds.select(clear=True)  # 선택 해제
            cmds.joint(name=joint_name, position=( locator_x_position, locator_y_position, locator_z_position))
            
            
            locator_x_position2 = cmds.getAttr(locator_name + ".translateX")
            locator_y_position2 = cmds.getAttr(locator_name + ".translateY")
            locator_z_position2 = cmds.getAttr(locator_name + ".translateZ")
            
            joint_name2 = locator_name.replace("_loc", "_jnt")  # 로케이터 이름을 조인트 이름에 추가
            
            # 얼굴 조인트 생성
            cmds.select(clear=True)  # 선택 해제
            cmds.joint(name=joint_name2, position=(locator_x_position2, locator_y_position2, locator_z_position2))
            
            # 오프셋 조인트 생성
            offset_joint_name = joint_name2.replace("_jnt", "_offset_jnt")
            cmds.joint(name=offset_joint_name, position=(locator_x_position2, locator_y_position2, locator_z_position2))  # 원하는 위치에 따라 조절 가능
            
           
            
            
            try:
            # 오프셋 조인트를 원래 조인트의 자식으로 설정
                cmds.parent(offset_joint_name, joint_name2)
            except RuntimeError as e:
                # 이미 부모로 설정되어 있던 경우 예외 처리
                print("Joint already has a parent:", e)
                
            try:
            # 센터 조인트를 로케이터 조인트의 부모로 설정
                cmds.parent(joint_name2, joint_name)
            except RuntimeError as e:
                # 이미 부모로 설정되어 있던 경우 예외 처리
                print("Joint already has a parent:", e)
                
                

def toggle_local_rotation_axes():
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("Please select one or more objects.")
        return

    for obj in selected_objects:
        # 현재 오브젝트의 로컬 회전 축 표시 상태 확인
        display_local_axis = cmds.getAttr(obj + ".displayLocalAxis")

        # 로컬 회전 축 표시 상태 토글
        cmds.setAttr(obj + ".displayLocalAxis", not display_local_axis)







createJoints()

#센터 조인트의 오리엔테이션 설정

cmds.select(cl=True)
joint_list = cmds.ls('__centre_*', type='joint')
alljnt = cmds.listRelatives(joint_list, parent=True, type='joint')
cmds.select(joint_list)
toggle_local_rotation_axes()
cmds.select(cl=True)


for joint_name in joint_list:
    cmds.joint(joint_name, e=True, oj="xyz", sao="yup", ch=True, zso=True)
    
    



import maya.cmds as cmds

# 모든 조인트를 가져오기
all_joints = cmds.ls(type='joint')

# 부모-자식 관계를 저장할 딕셔너리 생성
parent_child_map = {}

# 부모-자식 관계 매핑 생성
for joint in all_joints:
    parent = cmds.listRelatives(joint, parent=True, type='joint')
    if parent:
        parent = parent[0]  # 리스트에서 첫 번째 요소만 사용
        if parent in parent_child_map:
            parent_child_map[parent].append(joint)
        else:
            parent_child_map[parent] = [joint]

# 특정 부모 조인트의 자식 조인트 얻기
parent_joint_names = cmds.ls('__centre_*', type='joint')  # 부모 조인트의 이름을 지정
child_joints = []

for parent_joint_name in parent_joint_names:
    child_joints.extend(parent_child_map.get(parent_joint_name, []))
    
print(child_joints)
cmds.select(child_joints)
toggle_local_rotation_axes()
cmds.select(cl=True)

# 자식 조인트의 자식 조인트 찾기
grandchild_joints = []

for child_joint_name in child_joints:
    grandchildren = parent_child_map.get(child_joint_name, [])
    grandchild_joints.extend(grandchildren)

# 손자 조인트 리스트 출력
print(grandchild_joints)
cmds.select(grandchild_joints)
toggle_local_rotation_axes()
cmds.select(cl=True)


#손자 조인트의 월드 오리엔테이션 설정

for joint in grandchild_joints:
    cmds.setAttr(joint + '.jointOrientX', 0)
    cmds.setAttr(joint + '.jointOrientY', 0)
    cmds.setAttr(joint + '.jointOrientZ', 0)
    
    
    
    


print(child_joints)
cmds.select(cl=True)
cmds.select(child_joints)
cmds.parent(w=True)



cmds.select(joint_list)
cmds.delete()
cmds.select(cl=True)




#만들어둔 변수를 활용해야 한다.
#brow_locator_list
#eyelow_locator_list
#cheek_locator_list
#nasoFolds_locator_list

    
    
    
import maya.cmds as cmds

# 함수 정의: 로케이터와 조인트 쌍을 받아 패런트 설정
def parent_locator_joint_pairs(locator_list, joint_prefix):
    num_pairs = len(locator_list) // 2  # 각 로케이터 리스트의 쌍의 수

    for i in range(num_pairs):
        joint_name = "{}_jnt_{}".format(joint_prefix, i + 1)
        locator_name = "{}_loc_{}".format(joint_prefix, i + 1)

        # 조인트와 로케이터를 선택
        cmds.select(joint_name, locator_name)

        # 로케이터를 조인트의 자식으로 설정 (패런트 시키기)
        cmds.parent(a=True)

        # 선택 해제
        cmds.select(clear=True)



# 각 로케이터 리스트에 대해 패런트 설정 호출
jnt_name1 = mc.textField("nameOfTexFld1", q=True, tx=True)
parent_locator_joint_pairs(brow_locator_list, "L_" + jnt_name1)
parent_locator_joint_pairs(brow_locator_list, "R_" + jnt_name1)

jnt_name2 = mc.textField("nameOfTexFld2", q=True, tx=True)
parent_locator_joint_pairs(eyelow_locator_list, "L_" + jnt_name2)
parent_locator_joint_pairs(eyelow_locator_list, "R_" + jnt_name2)

jnt_name3 = mc.textField("nameOfTexFld3", q=True, tx=True)
parent_locator_joint_pairs(cheek_locator_list, "L_" + jnt_name3)
parent_locator_joint_pairs(cheek_locator_list, "R_" + jnt_name3)


jnt_name4 = mc.textField("nameOfTexFld4", q=True, tx=True)
parent_locator_joint_pairs(nasoFolds_locator_list, "L_" + jnt_name4)
parent_locator_joint_pairs(nasoFolds_locator_list, "R_" + jnt_name4)





group_name = cmds.group(em=True, name="Loc_Group")   
cmds.select(cl=True)
cmds.select(brow_locator_list, add=True) 
cmds.select(eyelow_locator_list, add=True)
cmds.select(cheek_locator_list, add=True)
cmds.select(nasoFolds_locator_list, add=True) 
cmds.select(group_name, add=True)

cmds.parent()





#radius 값 조절.. 

# 변경할 radius 값
new_radius = 0.2  # 이 값을 원하는 크기로 변경하세요

# 검색할 그룹의 이름
group_name = "Loc_Group"  # 원하는 그룹의 이름으로 변경하세요

# 그룹 내의 모든 조인트를 검색
joint_list = cmds.listRelatives(group_name, allDescendents=True, type="joint")

# 조인트의 radius 값을 변경
for joint in joint_list:
    cmds.setAttr(joint + ".radius", new_radius)
    
