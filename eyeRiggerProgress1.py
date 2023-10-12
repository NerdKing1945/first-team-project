import maya.cmds as cmds


center = "center1"
vtx = cmds.ls(sl = 1, fl =1)

for v in vtx :
    cmds.select(cl =1)
    jnt = cmds.joint(radius=0.03)
    pos = cmds.xform(v, q=1, ws=1, t= 1)
    cmds.xform(jnt, ws =1, t = pos)
    posC = cmds.xform(center, q=1, ws=1, t=1)
    cmds.select(cl =1)
    jntC = cmds.joint(radius=0.01)
    cmds.xform(jntC, ws =1, t=posC)
    cmds.parent(jnt, jntC)
    
    cmds.joint(jntC, e =1, oj ="xyz", secondaryAxisOrient= "yup", ch=1, zso=1)
    
    
    
    sel = cmds.ls(sl=1)
    
    for s in sel :
        loc = cmds.spaceLocator()[0]
        pos = cmds.xform(s, q = 1, ws = 1, t = 1)
        cmds.xform(loc, ws = 1, t =pos)
        par = cmds.listRelatives(s, p = 1)[0]
        
        cmds.aimConstraint(loc,par, mo = 1, weight = 1, aimVector = (1, 0, 0), upVector = (0, 1, 0), worldUpType = "object", worldupObject)
        
        
        
        
        
        
cmds.group(em=True, name="upEyeLidJnt_GRP")
cmds.group(em=True, name="lowEyeLidJnt_GRP")













import maya.cmds as cmds

def rename_joints_in_group(group_name, new_name):
    # 그룹 노드에 있는 모든 조인트 목록을 가져옵니다.
    joint_list = cmds.listRelatives(group_name, type='joint', allDescendents=False)

    if joint_list:
        for joint in joint_list:
            cmds.rename(joint, new_name)
            print("조인트 {0}의 이름을 {1}로 변경했습니다.".format(joint, new_name))
    else:
        print("그룹 노드 {0} 안에 조인트가 없거나 찾을 수 없습니다.".format(group_name))



# 함수 호출 (그룹 노드 이름과 새로운 이름을 인수로 지정)
group_name_to_rename = "lowEyeLidJnt_GRP"  # 그룹 노드의 이름
new_joint_name = "lowEyeLidJnt"  # 새로운 조인트의 이름
rename_joints_in_group(group_name_to_rename, new_joint_name)





group_name_to_rename = "upEyeLidJnt_GRP"  # 그룹 노드의 이름
new_joint_name = "upEyeLidJnt"  # 새로운 조인트의 이름
rename_joints_in_group(group_name_to_rename, new_joint_name)



import maya.cmds as cmds

def rename_child_joints_with_suffix():
    # 현재 선택된 조인트 목록을 가져옵니다.
    selected_joints = cmds.ls(selection=True, type='joint')

    if not selected_joints:
        print("선택된 조인트가 없습니다.")
        return

    for joint in selected_joints:
        # 선택된 조인트의 자식 조인트 목록을 가져옵니다.
        child_joints = cmds.listRelatives(joint, type='joint', children=True)

        if child_joints:
            for child_joint in child_joints:
                # 선택된 조인트와 같은 이름으로 자식 조인트의 이름을 변경하고 "_offset" suffix를 추가합니다.
                new_name = joint + "_offset"
                cmds.rename(child_joint, new_name)
                print("조인트 {0}의 이름을 {1}로 변경했습니다.".format(child_joint, new_name))
        else:
            print("선택한 조인트 {0}에 자식 조인트가 없습니다.".format(joint))

# 함수 호출

cmds.select(cl=True)
joint_list1 = cmds.listRelatives("upEyeLidJnt_GRP", type='joint', allDescendents=False)
cmds.select(joint_list1)
rename_child_joints_with_suffix()

cmds.select(cl=True)
joint_list1 = cmds.listRelatives("lowEyeLidJnt_GRP", type='joint', allDescendents=False)
cmds.select(joint_list1)
rename_child_joints_with_suffix()
cmds.select(cl=True)

























