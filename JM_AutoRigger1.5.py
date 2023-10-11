import maya.cmds as mc
import maya.cmds as cmds
import pymel.core as pm

# 각 로케이터를 저장할 리스트 초기화
brow_locator_list = []
eyelow_locator_list = []
cheek_locator_list = []
nasoFolds_locator_list = []

def queryTextFld1(*args):
    loc_name = mc.textField("nameOfTexFld1", q=True, tx=True)
    return loc_name

def queryTextFld2(*args):
    loc_name = mc.textField("nameOfTexFld2", q=True, tx=True)
    return loc_name

def queryTextFld3(*args):
    loc_name = mc.textField("nameOfTexFld3", q=True, tx=True)
    return loc_name
    
def queryTextFld4(*args):
    loc_name = mc.textField("nameOfTexFld4", q=True, tx=True)
    return loc_name
    
def checkScene():
    typeRight = ["R_eyebrow_crv", "R_eyelow_crv", "R_nasoFolds_crv", "R_cheek_crv"]
    typeLeft = ["L_eyebrow_crv", "L_eyelow_crv", "L_nasoFolds_crv", "L_cheek_crv"]

    found_right = [False] * len(typeRight)
    found_left = [False] * len(typeLeft)

    all_objects = cmds.ls(dag=True, long=True, tr=True)

    matching_objects = set()

    for obj in all_objects:
        for i, name in enumerate(typeRight):
            if name in obj:
                found_right[i] = True
                matching_objects.add(obj)

    for obj in all_objects:
        for i, name in enumerate(typeLeft):
            if name in obj:
                found_left[i] = True
                matching_objects.add(obj)

    # typeRight 또는 typeLeft 리스트의 어떤 구성 요소 하나라도 발견되면 경고 메시지를 표시하지 않습니다.
    if not (all(found_right) or all(found_left)):
        warning_message = "R_ 혹은 L_ 'eyebrow_crv', 'eyelow_crv', 'cheek_crv', 'nasoFolds_crv' 조합을 갖추어야 합니다.."
        # 경고 창을 띄웁니다.
        cmds.warning(warning_message)
        return

    # typeRight 리스트의 모든 구성 요소가 발견되었는지 확인
    if all(found_right):
        print("모든 typeRight 요소가 씬에 존재합니다.")
        for obj in matching_objects:
            print("오브젝트 '{}'은(는) 씬에 존재합니다.".format(obj))
            
        result = cmds.confirmDialog(title='Confirm', message='apply symmetrizing?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No')

        if result == 'Yes':
            print("Yes 버튼을 클릭했습니다. 여기서 원하는 작업을 수행하세요.")
            cmds.createNode('transform', n='R_facial_cvs_temppp')
            cmds.select(cl=True)
            cmds.select(typeRight)
            cmds.select("R_facial_cvs_temppp", add = True)
            cmds.parent()
            cmds.duplicate("R_facial_cvs_temppp", renameChildren=True)
            cmds.select(cl=True)
            cmds.rename("R_facial_cvs_temppp1", "L_facial_cvs_temppp")
            cmds.rename("R_eyebrow_crv1", "L_eyebrow_crv")
            cmds.rename("R_eyelow_crv1", "L_eyelow_crv")
            cmds.rename("R_nasoFolds_crv1", "L_nasoFolds_crv")
            cmds.rename("R_cheek_crv1", "L_cheek_crv")
            duplicated_node = "L_facial_cvs_temppp"
            cmds.scale(-1, 1, 1, duplicated_node, r=True)
            cmds.select(cl=True)
            cmds.select(duplicated_node)
            cmds.makeIdentity(apply=True, t=0, r=0, s=1, n=0, pn=1)
            cmds.select(cl=True)
            cmds.select(typeRight)
            cmds.select(typeLeft, add =True)
            cmds.parent(w = True)
            cmds.select(cl=True)
            cmds.delete("R_facial_cvs_temppp")
            cmds.delete("L_facial_cvs_temppp")
            
            

            
            

    # typeLeft 리스트의 모든 구성 요소가 발견되었는지 확인
    if all(found_left):
        print("모든 typeLeft 요소가 씬에 존재합니다.")
        for obj in matching_objects:
            print("오브젝트 '{}'은(는) 씬에 존재합니다.".format(obj))
            
        result = cmds.confirmDialog(title='Confirm', message='apply symmetrizing?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No')

        if result == 'Yes':
            print("Yes 버튼을 클릭했습니다. 여기서 원하는 작업을 수행하세요.")
            cmds.createNode('transform', n='L_facial_cvs_temppp')
            cmds.select(cl=True)
            cmds.select(typeLeft)
            cmds.select("L_facial_cvs_temppp", add = True)
            cmds.parent()
            cmds.duplicate("L_facial_cvs_temppp", renameChildren=True)
            cmds.select(cl=True)
            cmds.rename("L_facial_cvs_temppp1", "R_facial_cvs_temppp")
            cmds.rename("L_eyebrow_crv1", "R_eyebrow_crv")
            cmds.rename("L_eyelow_crv1", "R_eyelow_crv")
            cmds.rename("L_nasoFolds_crv1", "R_nasoFolds_crv")
            cmds.rename("L_cheek_crv1", "R_cheek_crv")
            duplicated_node = "R_facial_cvs_temppp"
            cmds.scale(-1, 1, 1, duplicated_node, r=True)
            cmds.select(cl=True)
            cmds.select(duplicated_node)
            cmds.makeIdentity(apply=True, t=0, r=0, s=1, n=0, pn=1)
            cmds.select(cl=True)
            cmds.select(typeRight)
            cmds.select(typeLeft, add =True)
            cmds.parent(w = True)
            cmds.select(cl=True)
            cmds.delete("R_facial_cvs_temppp")
            cmds.delete("L_facial_cvs_temppp")



import maya.cmds as mc

def create_locators(selected_option, locator_name, locator_list, scale_factor=0.04):
    if locator_name:
        for i in range(1, selected_option + 1):
            loc_name_with_index = "L_" + locator_name + "_" + str(i)
            mc.spaceLocator(n=loc_name_with_index)
            
            # 생성한 로케이터에 스케일 적용
            mc.setAttr(loc_name_with_index + ".localScaleX", scale_factor)
            mc.setAttr(loc_name_with_index + ".localScaleY", scale_factor)
            mc.setAttr(loc_name_with_index + ".localScaleZ", scale_factor)
            
            locator_list.append(loc_name_with_index)
            print("Locator '{}' created.".format(loc_name_with_index))
            
            # 오른쪽 버전도 생성
            loc_name_with_index_r = "R_" + locator_name + "_" + str(i)
            mc.spaceLocator(n=loc_name_with_index_r)
            
            # 생성한 로케이터에 스케일 적용
            mc.setAttr(loc_name_with_index_r + ".localScaleX", scale_factor)
            mc.setAttr(loc_name_with_index_r + ".localScaleY", scale_factor)
            mc.setAttr(loc_name_with_index_r + ".localScaleZ", scale_factor)
            
            locator_list.append(loc_name_with_index_r)
            print("Locator '{}' created.".format(loc_name_with_index_r))
    else:
        print("Text field is empty. Please enter a name.")


def makePri(*args):
    selected_option1 = int(pm.radioButtonGrp('RBGrp1', q=1, select=1)) + 2
    locator_name1 = queryTextFld1() + "_loc"
    create_locators(selected_option1, locator_name1, brow_locator_list)
    
    selected_option2 = int(pm.radioButtonGrp('RBGrp2', q=1, select=1)) + 2
    locator_name2 = queryTextFld2() + "_loc"
    create_locators(selected_option2, locator_name2, eyelow_locator_list)
    
    selected_option3 = int(pm.radioButtonGrp('RBGrp3', q=1, select=1)) + 2
    locator_name3 = queryTextFld3() + "_loc"
    create_locators(selected_option3, locator_name3, cheek_locator_list)
    
    selected_option4 = int(pm.radioButtonGrp('RBGrp4', q=1, select=1)) + 2
    locator_name4 = queryTextFld4() + "_loc"
    create_locators(selected_option4, locator_name4, nasoFolds_locator_list)
    
    
    print "brow_locator_list"
    print brow_locator_list
    print "eyelow_locator_list"
    print eyelow_locator_list
    print "cheek_locator_list"
    print cheek_locator_list
    print "nasoFolds_locator_list"
    print nasoFolds_locator_list
    
    checkScene()
    
     #정수리의 중앙에 위치해야 할 로케이터를 생성        
    cmds.spaceLocator(n="centre_Ultimate_Loc")
    cmds.setAttr('centre_Ultimate_Loc.translateX', 0)
    cmds.setAttr('centre_Ultimate_Loc.translateY', 2)
    cmds.setAttr('centre_Ultimate_Loc.translateZ', 0)

def makePri2(*args):
    
    # 선택된 객체를 가져옵니다.
    selected_objects = cmds.ls(selection=True)
    
    # 일치하는 횟수를 저장하는 변수를 초기화합니다.
    match_count = 0
    
    # 'eyebrow_crv', 'eyelow_crv', 'cheek_crv', 'nasoFolds_crv'와 이름이 일치하는지 확인합니다.
    for obj in selected_objects:
        if obj == 'L_eyebrow_crv':
            match_count += 1
    
        if obj == 'L_eyelow_crv':
            match_count += 1
    
        if obj == 'L_cheek_crv':
            match_count += 1
    
        if obj == 'L_nasoFolds_crv':
            match_count += 1
            
        if obj == 'R_eyebrow_crv':
            match_count += 1
    
        if obj == 'R_eyelow_crv':
            match_count += 1
    
        if obj == 'R_cheek_crv':
            match_count += 1
    
        if obj == 'R_nasoFolds_crv':
            match_count += 1
    
    # 모든 이름이 일치하는 경우에만 스크립트가 작동합니다.
    if match_count == 8:
        print("선택된 객체들은 'L_eyebrow_crv', 'L_eyelow_crv', 'L_cheek_crv', 'L_nasoFolds_crv'와 이름이 모두 일치합니다.")
        print("선택된 객체들은 'R_eyebrow_crv', 'R_eyelow_crv', 'R_cheek_crv', 'R_nasoFolds_crv'와 이름이 모두 일치합니다.")
        
        
        
        
        
        
        
        mc.select(cl=True)
        # brow_locator_list에 저장된 오브젝트 중 이름이 "R_"로 시작하는 오브젝트 선택 -1
        selected_objects = [obj for obj in brow_locator_list if obj.startswith("R_")]
        
        # 선택한 오브젝트들을 Maya에서 선택
        mc.select(selected_objects)
        mc.select("R_eyebrow_crv", add=True)
        place_selected_on_curve()
        
        mc.select(cl=True)
        # brow_locator_list에 저장된 오브젝트 중 이름이 "L_"로 시작하는 오브젝트 선택 -2
        selected_objects = [obj for obj in brow_locator_list if obj.startswith("L_")]
        
        # 선택한 오브젝트들을 Maya에서 선택
        mc.select(selected_objects)
        mc.select("L_eyebrow_crv", add=True)
        place_selected_on_curve()
        
        
        mc.select(cl=True)
        # eyelow_locator_list에 저장된 오브젝트 중 이름이 "R_"로 시작하는 오브젝트 선택 -3
        selected_objects = [obj for obj in eyelow_locator_list if obj.startswith("R_")]
        
        # 선택한 오브젝트들을 Maya에서 선택
        mc.select(selected_objects)
        mc.select("R_eyelow_crv", add=True)
        place_selected_on_curve()
        
        
        mc.select(cl=True)
        # eyelow_locator_list에 저장된 오브젝트 중 이름이 "L_"로 시작하는 오브젝트 선택 -4
        selected_objects = [obj for obj in eyelow_locator_list if obj.startswith("L_")]
        
        # 선택한 오브젝트들을 Maya에서 선택
        mc.select(selected_objects)
        mc.select("L_eyelow_crv", add=True)
        place_selected_on_curve()
        
        
        mc.select(cl=True)
        # cheek_locator_list에 저장된 오브젝트 중 이름이 "R_"로 시작하는 오브젝트 선택 -5
        selected_objects = [obj for obj in cheek_locator_list if obj.startswith("R_")]
        
        # 선택한 오브젝트들을 Maya에서 선택
        mc.select(selected_objects)
        mc.select("R_cheek_crv", add=True)
        place_selected_on_curve()
        
        
        mc.select(cl=True)
        # cheek_locator_list에 저장된 오브젝트 중 이름이 "L_"로 시작하는 오브젝트 선택 -6
        selected_objects = [obj for obj in cheek_locator_list if obj.startswith("L_")]
        
        # 선택한 오브젝트들을 Maya에서 선택
        mc.select(selected_objects)
        mc.select("L_cheek_crv", add=True)
        place_selected_on_curve()
                
        mc.select(cl=True)
        # nasoFolds_locator_list에 저장된 오브젝트 중 이름이 "R_"로 시작하는 오브젝트 선택 -7
        selected_objects = [obj for obj in nasoFolds_locator_list if obj.startswith("R_")]
        
        # 선택한 오브젝트들을 Maya에서 선택
        mc.select(selected_objects)
        mc.select("R_nasoFolds_crv", add=True)
        place_selected_on_curve()
        
        
        mc.select(cl=True)
        # nasoFolds_locator_list에 저장된 오브젝트 중 이름이 "L_"로 시작하는 오브젝트 선택 -8
        selected_objects = [obj for obj in nasoFolds_locator_list if obj.startswith("L_")]
        
        # 선택한 오브젝트들을 Maya에서 선택
        mc.select(selected_objects)
        mc.select("L_nasoFolds_crv", add=True)
        place_selected_on_curve()
        
        cmds.select(cl=True)
        buildFacialJoints()
    
    
    
    else:
        print("선택된 객체들 중에서 'L_eyebrow_crv', 'L_eyelow_crv', 'L_cheek_crv', 'L_nasoFolds_crv'와 이름이 모두 일치하지 않습니다.")
        print("선택된 객체들 중에서 'R_eyebrow_crv', 'R_eyelow_crv', 'R_cheek_crv', 'R_nasoFolds_crv'와 이름이 모두 일치하지 않습니다.")
        # 경고 메시지를 지정합니다.
        warning_message = "'eyebrow_crv', 'eyelow_crv', 'cheek_crv', 'nasoFolds_crv'를 셀렉트해야 합니다."

        # 경고 창을 띄웁니다.
        cmds.warning(warning_message)
    
    
    
    
   
    


def place_selected_on_curve():
    my_selections = cmds.ls(sl=True)
    
    selected_items = my_selections[0:-1]
    target_curve = my_selections[len(my_selections) - 1]
    
    object_index = 0
    for selected_object in selected_items:
        cmds.select(clear=True)
        cmds.select(selected_object, add=True)
        cmds.select(target_curve, add=True)
    
        motion_path = cmds.pathAnimation(fractionMode=True,
        follow=False,
        followAxis="x",
        upAxis="y",
        worldUpType="vector",
        worldUpVector=[0, 1, 0],
        inverseUp=False,
        inverseFront=False,
        bank=False,
        startTimeU=0,  # Start U value from 0
        endTimeU=1)    # End U value at 1
        
        key = cmds.listConnections('%s.uValue' % motion_path)
        cmds.delete(key)
        
        num_objects = len(selected_items) - 1  # Corrected num_objects calculation
        total_length_of_curve = 1
        
        increment = 1.0 / num_objects if num_objects > 0 else 0.0  # Corrected increment calculation
        
        new_u_value = object_index * increment
        
        cmds.setAttr('%s.uValue' % motion_path, new_u_value)
        
        object_index = object_index + 1
        
        rx_connections = cmds.listConnections('%s.rx' % selected_object, plugs=True, source=True, destination=False)
        if rx_connections:
            for rx_connection in rx_connections:
                cmds.disconnectAttr(rx_connection, '%s.rx' % selected_object)
        
        ry_connections = cmds.listConnections('%s.ry' % selected_object, plugs=True, source=True, destination=False)
        if ry_connections:
            for ry_connection in ry_connections:
                cmds.disconnectAttr(ry_connection, '%s.ry' % selected_object)
        
        rz_connections = cmds.listConnections('%s.rz' % selected_object, plugs=True, source=True, destination=False)
        if rz_connections:
            for rz_connection in rz_connections:
                cmds.disconnectAttr(rz_connection, '%s.rz' % selected_object)
        
        cmds.xform(selected_object, rotation=[0, 0, 0])



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
        
        

#넙스를 생성해서 개별 컨트롤러를 만들어줌. 
#셰이더도 생성해서 연결

def select_joints_with_string(joint_chain_name, search_string):
    # 주어진 조인트 체인에서 모든 조인트를 가져옵니다.
    all_joints = cmds.listRelatives(joint_chain_name, allDescendents=True, type="joint", fullPath=True)

    if not all_joints:
        print("조인트가 없거나 조인트 체인이 유효하지 않습니다.")
        return

    # "offset_jnt" 문자열을 포함하는 조인트를 찾습니다.
    joints_with_string = [joint for joint in all_joints if search_string in joint]

    if not joints_with_string:
        print('"{0}"을 포함하는 조인트를 찾을 수 없습니다.'.format(search_string))
        return

    # 찾은 조인트를 선택합니다.
    cmds.select(joints_with_string)




def create_spheres_for_selected_joints():
    # 현재 선택된 모든 조인트를 가져옵니다.
    selected_joints = cmds.ls(selection=True, type='joint')
    
    if not selected_joints:
        print("선택된 조인트가 없습니다.")
        return
    
    # 각 선택된 조인트에 대해 NURBS 스피어를 생성합니다.
    for joint in selected_joints:
        # NURBS 스피어 생성
        sphere = cmds.sphere(name="sphere_for_" + joint, radius=0.02)
        
        # 스피어의 위치를 선택된 조인트와 일치시킵니다.
        joint_position = cmds.xform(joint, query=True, translation=True, worldSpace=True)
        cmds.xform(sphere, translation=joint_position, worldSpace=True)




def parent_shape_nodes_to_selected_joints():
    # 현재 선택된 모든 조인트를 가져옵니다.
    selected_joints = cmds.ls(selection=True, type='joint')
    
    if not selected_joints:
        print("선택된 조인트가 없습니다.")
        return

    for joint in selected_joints:
        # NURBS 스피어의 이름을 조인트 이름으로 만듭니다.
        sphere_name = "sphere_for_" + joint
        
        # NURBS 스피어의 쉐이프 노드를 선택합니다.
        sphere_shape = cmds.listRelatives(sphere_name, shapes=True, type="nurbsSurface")
        
        
        if sphere_shape:
            # 쉐이프 노드를 선택한 후 부모 관계를 설정합니다.
            cmds.parent(sphere_shape, joint, shape=True, relative=True)
        else:
            print('NURBS 스피어 쉐이프 노드를 찾을 수 없습니다.')
                  

def select_top_level_sphere_groups():
    # 모든 노드를 가져옵니다.
    all_nodes = cmds.ls(dag=True, long=True)

    top_level_sphere_groups = []

    for node in all_nodes:
        if node.startswith("|sphere_for_"):
            # 현재 노드의 모든 부모를 가져옵니다.
            parents = cmds.listRelatives(node, parent=True, fullPath=True)
            if not parents:
                # 부모가 없으면 이 노드는 가장 상위 레벨 노드입니다.
                top_level_sphere_groups.append(node)
    
    if top_level_sphere_groups:
        cmds.select(top_level_sphere_groups, replace=True)
    else:
        print("씬에서 'sphere_for'로 시작하는 가장 상위 레벨의 그룹 노드를 찾을 수 없습니다.")




#얼굴의 조인트를 생성밑 관절의 오리엔테이션 재설정에 관련한 시퀀스

def buildFacialJoints():

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
        
    
    
    
    #Loc_Group 아래에 있는 조인트들을 선택
    select_joints_with_string("Loc_Group", "offset_jnt")
    
    
    #조인트로부터 넙스 스피어를 생성하고 좌표를 맞춤
    create_spheres_for_selected_joints()
    cmds.select(cl=True)
    select_joints_with_string("Loc_Group", "offset_jnt")
    
    cmds.select(cl=True)
    select_joints_with_string("Loc_Group", "offset_jnt")
    
    
    # 생성된 조인트 차일드에 넙스 스피어 셰이프를 패런트
    parent_shape_nodes_to_selected_joints()
    
    
    
    
    
    
    cmds.select(cl=True)
    # Loc_Group 내의 모든 nurbsSurface 셰이프를 선택합니다.
    nurbs_surface_shapes = cmds.listRelatives("Loc_Group", allDescendents=True, type="nurbsSurface")
    
    if nurbs_surface_shapes:
        cmds.select(nurbs_surface_shapes)
    else:
        print("Loc_Group 내에 nurbsSurface 셰이프가 없습니다.")
    
    # 선택된 모든 오브젝트를 가져옵니다.
    selected_objects = cmds.ls(selection=True)
    # 적용할 램버트 셰이더 이름
    shader_name = 'lambert5'
    # 램버트 셰이더가 이미 존재하는지 확인하고 없으면 생성합니다.
    if not cmds.objExists(shader_name):
        lambert_shader = cmds.shadingNode('lambert', asShader=True, name=shader_name)
        # 램버트 셰이더의 초기값 설정 (RGB 0, 1, 0)
        cmds.setAttr(lambert_shader + ".color", 0, 1, 0, type="double3")
    else:
        lambert_shader = shader_name
    
    # 선택된 모든 오브젝트에 램버트 셰이더를 할당합니다.
    for obj in selected_objects:
        cmds.select(obj)
        cmds.hyperShade(assign=lambert_shader)
        cmds.select(clear=True)
    
    
    
    # 함수 호출
    select_top_level_sphere_groups()
    cmds.delete()





    



# Create the main window
if cmds.window("myWindow", exists=True):
    cmds.deleteUI("myWindow", window=True)

my_window = cmds.window("myWindow", title="JM_Facial_AutoRigger1.5")

# Set the width and height of the window
window_width = 500
window_height = 320
cmds.window(my_window, edit=True, widthHeight=(window_width, window_height))

# Create the tab layout
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

# First tab
cmds.setParent(tabs)
tab1 = cmds.columnLayout(adjustableColumn=True)
pm.text(label="Temporary Content for Tab 1")
pm.button(l= "itwillcomeSoon")

# Second tab
cmds.setParent(tabs)
tab2 = cmds.columnLayout(adjustableColumn=True)
pm.text(label="Temporary Content for Tab 2")

import maya.cmds as cmds
import sys

# Define the path to the module
path = r'D:\jaw_utils'

# Remove the module from sys.modules if it's already imported
if 'jaw_utils3' in sys.modules:
    del sys.modules['jaw_utils3']

# Add the path to sys.path if it's not already there
if path not in sys.path:
    sys.path.append(path)
    
import jaw_utils3



# 텍스트 필드에서 값을 가져와서 createGuides 함수에 전달하는 함수
def get_number_and_create_guides(*args):
    text = cmds.textField("myTextField", q=True, text=True)
    
    try:
        number = int(text)
        if 1 <= number <= 15:  # 1에서 15 사이의 양의 정수 확인
            jaw_utils3.createGuides(number)  # createGuides 함수 호출 및 텍스트 필드의 값을 전달
        else:
            print('Invalid input. Please enter a positive integer between 1 and 15.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')

def placeJoints(*args):
    jaw_utils3.build()
    
def temp(*args):
    jaw_utils3.createJawPin()
    


cmds.text(label="Enter a span number(1-15):")
textfield = cmds.textField("myTextField")
cmds.button(label="Create Locator Guides", command=get_number_and_create_guides)
cmds.button(label="build joints", command=placeJoints)
cmds.button(label="Create JawPin", command=temp)








# Third tab
cmds.setParent(tabs)
tab3 = cmds.columnLayout(adjustableColumn=True)
pm.text(label="This is the content of Tab 3")

import pymel.core as pm

def copy_selected_object_to_text_field(text_field):
    # Get the selected object's name
    selected_object = pm.ls(selection=True)
    if selected_object:
        object_name = selected_object[0].name()
        # Set the text field's value to the selected object's name
        pm.textField(text_field, edit=True, text=object_name)

# Create the UI
pm.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 220), (2, 20), (3, 180)])

cmds.text(l="Fill these fields before APPLY SCRIPT")
cmds.text(l="")
cmds.text(l="")

name1 = cmds.textField("nameOfTexFld1", tx="brow")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name1))
cmds.text(label='eyebrow_crv')

name2 = cmds.textField("nameOfTexFld2", tx="eyelow")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name2))
cmds.text(label='eyelow_crv')

name3 = cmds.textField("nameOfTexFld3", tx="cheek")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name3))
cmds.text(label='cheek_crv')

name4 = cmds.textField("nameOfTexFld4", tx="nasolabi")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name4))
cmds.text(label='nasoFolds_crv')

# 첫 번째 행의 라디오 버튼 그룹 생성
cmds.setParent(tab3)
pm.text(label="eyebrow_crv")
rb_grp1 = pm.radioButtonGrp('RBGrp1', numberOfRadioButtons=3,
                            labelArray3=("3", "4", "5"), select=1, label="numberOfLoc")

# 두 번째 행의 라디오 버튼 그룹 생성
pm.text(label="eyelow_crv")
rb_grp2 = pm.radioButtonGrp('RBGrp2', numberOfRadioButtons=3,
                            labelArray3=("3", "4", "5"), select=1, label="numberOfLoc")

# 세 번째 행의 라디오 버튼 그룹 생성
pm.text(label="cheek_crv")
rb_grp3 = pm.radioButtonGrp('RBGrp3', numberOfRadioButtons=3,
                            labelArray3=("3", "4", "5"), select=1, label="numberOfLoc")

# 네 번째 행의 라디오 버튼 그룹 생성
pm.text(label="nasoFolds_crv")
rb_grp4 = pm.radioButtonGrp('RBGrp4', numberOfRadioButtons=3,
                            labelArray3=("3", "4", "5"), select=1, label="numberOfLoc")

# 생성 버튼 추가
create_button = pm.button(label="로케이터 생성", command=makePri)
create_button = pm.button(label="모션패스 연결", command=makePri2)

# Add the tabs to the tab layout
cmds.tabLayout(tabs, edit=True, tabLabel=((tab1, 'Eyes'), (tab2, 'LipSeal'), (tab3, 'Facial')))

# Show the window
cmds.showWindow(my_window)



