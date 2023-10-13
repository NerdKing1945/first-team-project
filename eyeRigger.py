# -*- coding: utf-8 -*-
import maya.cmds as cmds




#선택된 버텍스들과 센터 로케이터를 기준으로 조인트를 생성하는 함수
#
#
def create_base_joints_with_selected_vertices(centerLoc):
    center = centerLoc
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
    
    
#로케이터 생성및 에임 콘스트레인트 생성
#
#
def create_locator_with_aim_constraint(joint, world_up_object):
    # 로케이터 이름 생성
    loc_name = "{0}_Loc".format(joint)
    
    # 로케이터 생성
    loc = cmds.spaceLocator(name=loc_name)[0]
    
    # 조인트의 월드 포지션을 로케이터로 복사
    joint_position = cmds.xform(joint, query=True, translation=True, worldSpace=True)
    cmds.xform(loc, translation=joint_position, worldSpace=True)
    
    # 부모를 찾아서 par 변수에 저장
    par = cmds.listRelatives(joint, parent=True)[0]
    
    # 로케이터의 스케일 조정
    scale_value = 0.02
    cmds.setAttr("{0}.localScaleX".format(loc), scale_value)
    cmds.setAttr("{0}.localScaleY".format(loc), scale_value)
    cmds.setAttr("{0}.localScaleZ".format(loc), scale_value)
    
    # aimConstraint 설정
    cmds.aimConstraint(loc, par, mo=1, weight=1, aimVector=(1, 0, 0), upVector=(0, 1, 0), worldUpType="object", worldUpObject=world_up_object)
    
    

#자식조인트를 선택하는 함수
#
#
def select_children_jnt(selected_joints1):
    child_joints = []
    for joint in selected_joints1:
        child_joints.extend(cmds.listRelatives(joint, type='joint', children=True))
    
    # 선택된 모든 자식 조인트를 선택
    if child_joints:
        cmds.select(child_joints)


#특정 그룹안에 있는 조인트의 이름을 바꾸는 함수
#
#
def rename_joints_in_group(group_name, new_name):
    # 그룹 노드에 있는 모든 조인트 목록을 가져옵니다.
    joint_list = cmds.listRelatives(group_name, type='joint', allDescendents=False)

    if joint_list:
        for joint in joint_list:
            cmds.rename(joint, new_name)
            print("조인트 {0}의 이름을 {1}로 변경했습니다.".format(joint, new_name))
    else:
        print("그룹 노드 {0} 안에 조인트가 없거나 찾을 수 없습니다.".format(group_name))
        
        

#특정 그룹안에 있는 조인트의 자식의 이름을 바꾸는 함수
#
#
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
            
            



#특정조건을 만족하는 로케이터들을 잡아서 리스트로 만들고 그룹화하는 함수
#
#        
def list_locators_for_group(startsWith, endsWith, locGrp):
    # 초기 빈 리스트 생성
    locator_list = []
    
    # 씬에서 모든 로케이터 찾기
    all_locators = cmds.ls(type='transform')
    
    
    # 원하는 이름 패턴에 맞는 로케이터를 찾아서 리스트에 추가
    for locator in all_locators:
        if locator.startswith(startsWith) and locator.endswith(endsWith):
            locator_list.append(locator)
            
    print locator_list
    cmds.parent(locator_list, locGrp)
        
def eyeRigInitialSetup(*args):            
    #필요한 그룹노드 생성        
    cmds.group(em=True, name="L_upEyeLidJnt_GRP")
    cmds.group(em=True, name="L_lowEyeLidJnt_GRP")
    cmds.group(em=True, name="R_upEyeLidJnt_GRP")
    cmds.group(em=True, name="R_lowEyeLidJnt_GRP")
    
    
    #필요한 눈관련 로케이터 생성
    cmds.spaceLocator(n = "L_center", p = (0, 0, 0))
    cmds.spaceLocator(n = "L_eyeUpVec_loc", p = (0, 2, 0))
    
    cmds.pointConstraint("L_center", "L_eyeUpVec_loc", mo=True)
    cmds.setAttr("L_center.tx", 1)
    
    
    cmds.spaceLocator(n = "R_center", p = (0, 0, 0))
    cmds.spaceLocator(n = "R_eyeUpVec_loc", p = (0, 2, 0))
    
    cmds.pointConstraint("R_center", "R_eyeUpVec_loc", mo=True)
    cmds.setAttr("R_center.tx", -1)




def leyeJointSetup(*args):
    centerLoc="L_center"
    create_base_joints_with_selected_vertices(centerLoc)


def reyeJointSetup(*args):
    centerLoc="R_center"
    create_base_joints_with_selected_vertices(centerLoc)




# 함수 호출 (그룹 노드 이름과 새로운 이름을 인수로 지정)
#조인트 그룹의 조인트를 리네임

def aimConstraintLocatorSetup():

    group_name_to_rename = "L_lowEyeLidJnt_GRP"  # 그룹 노드의 이름
    new_joint_name = "L_lowEyeLidJnt"  # 새로운 조인트의 이름
    rename_joints_in_group(group_name_to_rename, new_joint_name)
    
    group_name_to_rename = "L_upEyeLidJnt_GRP"  # 그룹 노드의 이름
    new_joint_name = "L_upEyeLidJnt"  # 새로운 조인트의 이름
    rename_joints_in_group(group_name_to_rename, new_joint_name)
    
    group_name_to_rename = "R_lowEyeLidJnt_GRP"  # 그룹 노드의 이름
    new_joint_name = "R_lowEyeLidJnt"  # 새로운 조인트의 이름
    rename_joints_in_group(group_name_to_rename, new_joint_name)
    
    group_name_to_rename = "R_upEyeLidJnt_GRP"  # 그룹 노드의 이름
    new_joint_name = "R_upEyeLidJnt"  # 새로운 조인트의 이름
    rename_joints_in_group(group_name_to_rename, new_joint_name)
    
    
    
    
    
    
    
    
    # 함수 호출 자식 조인트를 리네임
    
    cmds.select(cl=True)
    joint_list1 = cmds.listRelatives("L_upEyeLidJnt_GRP", type='joint', allDescendents=False)
    cmds.select(joint_list1)
    rename_child_joints_with_suffix()
    
    cmds.select(cl=True)
    joint_list1 = cmds.listRelatives("L_lowEyeLidJnt_GRP", type='joint', allDescendents=False)
    cmds.select(joint_list1)
    rename_child_joints_with_suffix()
    cmds.select(cl=True)
    
    cmds.select(cl=True)
    joint_list1 = cmds.listRelatives("R_upEyeLidJnt_GRP", type='joint', allDescendents=False)
    cmds.select(joint_list1)
    rename_child_joints_with_suffix()
    
    cmds.select(cl=True)
    joint_list1 = cmds.listRelatives("R_lowEyeLidJnt_GRP", type='joint', allDescendents=False)
    cmds.select(joint_list1)
    rename_child_joints_with_suffix()
    cmds.select(cl=True)
    
    
    
    
    
    # 선택된 조인트들의 자식 조인트들을 잡아서 에임콘스트레인트를 생성하고 로케이터 부착
    #
    #
    cmds.select(cl=True)
    selected_joints1 = cmds.listRelatives("L_upEyeLidJnt_GRP", type='joint', children=True)
    cmds.select(selected_joints1)
    select_children_jnt(selected_joints1)
    
    selected_joints = cmds.ls(selection=True, type='joint')
    
    # 각 조인트에 대해 함수 호출
    for joint in selected_joints:
        create_locator_with_aim_constraint(joint, "L_eyeUpVec_loc")
    
    
    
    cmds.select(cl=True)
    selected_joints1 = cmds.listRelatives("L_lowEyeLidJnt_GRP", type='joint', children=True)
    cmds.select(selected_joints1)
    select_children_jnt(selected_joints1)
    
    selected_joints = cmds.ls(selection=True, type='joint')
    
    # 각 조인트에 대해 함수 호출
    for joint in selected_joints:
        create_locator_with_aim_constraint(joint, "L_eyeUpVec_loc")
    
    
    
    cmds.select(cl=True)
    selected_joints1 = cmds.listRelatives("R_upEyeLidJnt_GRP", type='joint', children=True)
    cmds.select(selected_joints1)
    select_children_jnt(selected_joints1)
    
    selected_joints = cmds.ls(selection=True, type='joint')
    
    # 각 조인트에 대해 함수 호출
    for joint in selected_joints:
        create_locator_with_aim_constraint(joint, "L_eyeUpVec_loc")
    
    
    
    cmds.select(cl=True)
    selected_joints1 = cmds.listRelatives("R_lowEyeLidJnt_GRP", type='joint', children=True)
    cmds.select(selected_joints1)
    select_children_jnt(selected_joints1)
    
    selected_joints = cmds.ls(selection=True, type='joint')
    
    # 각 조인트에 대해 함수 호출
    for joint in selected_joints:
        create_locator_with_aim_constraint(joint, "L_eyeUpVec_loc")
    
    
    
    
    
    #로케이터를 위한 그룹을 생성
    cmds.group(em=True, name="L_upEyeLidLoc_GRP")
    cmds.group(em=True, name="L_lowEyeLidLoc_GRP")
    cmds.group(em=True, name="R_upEyeLidLoc_GRP")
    cmds.group(em=True, name="R_lowEyeLidLoc_GRP")
    
    
    
    
    
        
    #조건을 만족하는 로케이터들을 위에서 생성된 그룹에 패런트
    startsWith = "L_upEyeLid"
    endsWith = "_Loc"
    locGrp = "L_upEyeLidLoc_GRP"
    list_locators_for_group(startsWith, endsWith, locGrp)
    
    
    startsWith = "L_lowEyeLid"
    endsWith = "_Loc"
    locGrp = "L_lowEyeLidLoc_GRP"
    list_locators_for_group(startsWith, endsWith, locGrp)
    
    
    startsWith = "R_upEyeLid"
    endsWith = "_Loc"
    locGrp = "R_upEyeLidLoc_GRP"
    list_locators_for_group(startsWith, endsWith, locGrp)
    
    
    startsWith = "R_lowEyeLid"
    endsWith = "_Loc"
    locGrp = "R_lowEyeLidLoc_GRP"
    list_locators_for_group(startsWith, endsWith, locGrp)


