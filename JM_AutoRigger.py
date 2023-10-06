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



def create_locators(selected_option, locator_name, locator_list):
    if locator_name:
        for i in range(1, selected_option + 1):
            loc_name_with_index = "L_" + locator_name + "_" + str(i)
            mc.spaceLocator(n=loc_name_with_index)
            locator_list.append(loc_name_with_index)
            print("Locator '{}' created.".format(loc_name_with_index))
            
            # 오른쪽 버전도 생성
            loc_name_with_index_r = "R_" + locator_name + "_" + str(i)
            mc.spaceLocator(n=loc_name_with_index_r)
            locator_list.append(loc_name_with_index_r)
            print("Locator '{}' created.".format(loc_name_with_index_r))
    else:
        print("Text field is empty. Please enter a name.")

def makePri(*args):
    selected_option1 = int(pm.radioButtonGrp('RBGrp1', q=1, select=1)) + 2
    locator_name1 = queryTextFld1()
    create_locators(selected_option1, locator_name1, brow_locator_list)
    
    selected_option2 = int(pm.radioButtonGrp('RBGrp2', q=1, select=1)) + 2
    locator_name2 = queryTextFld2()
    create_locators(selected_option2, locator_name2, eyelow_locator_list)
    
    selected_option3 = int(pm.radioButtonGrp('RBGrp3', q=1, select=1)) + 2
    locator_name3 = queryTextFld3()
    create_locators(selected_option3, locator_name3, cheek_locator_list)
    
    selected_option4 = int(pm.radioButtonGrp('RBGrp4', q=1, select=1)) + 2
    locator_name4 = queryTextFld4()
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

    



# Create the main window
if cmds.window("myWindow", exists=True):
    cmds.deleteUI("myWindow", window=True)

my_window = cmds.window("myWindow", title="JM_Facial_AutoRigger1.0")

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

name1 = cmds.textField("nameOfTexFld1", tx="brow_loc")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name1))
cmds.text(label='eyebrow_crv')

name2 = cmds.textField("nameOfTexFld2", tx="eyelow_loc")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name2))
cmds.text(label='eyelow_crv')

name3 = cmds.textField("nameOfTexFld3", tx="cheek_loc")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name3))
cmds.text(label='cheek_crv')

name4 = cmds.textField("nameOfTexFld4", tx="nasolabi_loc")
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



