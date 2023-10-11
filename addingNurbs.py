#넙스를 생성해서 개별 컨트롤러를 만들어줌. 
#셰이더도 생성해서 연결


    
import maya.cmds as cmds

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