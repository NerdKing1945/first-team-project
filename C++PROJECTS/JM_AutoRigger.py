import maya.cmds as mc
import pymel.core as pm

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

def create_locators(selected_option, locator_name):
    if locator_name:
        for i in range(1, selected_option + 1):  # 1부터 selected_option까지 반복
            loc_name_with_index = locator_name + "_" + str(i)  # 로케이터 이름에 인덱스 추가
            mc.spaceLocator(n=loc_name_with_index)  # 로케이터 생성
            print("Locator '" + loc_name_with_index + "' created.")
    else:
        print("Text field is empty. Please enter a name.")

def makePri(*args):
    selected_option1 = int(pm.radioButtonGrp('RBGrp1', q=1, select=1)) + 2
    locator_name1 = queryTextFld1()
    create_locators(selected_option1, locator_name1)
    
    selected_option2 = int(pm.radioButtonGrp('RBGrp2', q=1, select=1)) + 2
    locator_name2 = queryTextFld2()
    create_locators(selected_option2, locator_name2)
    
    selected_option3 = int(pm.radioButtonGrp('RBGrp3', q=1, select=1)) + 2
    locator_name3 = queryTextFld3()
    create_locators(selected_option3, locator_name3)
    
    selected_option4 = int(pm.radioButtonGrp('RBGrp4', q=1, select=1)) + 2
    locator_name4 = queryTextFld4()
    create_locators(selected_option4, locator_name4)





# Create the main window
if cmds.window("myWindow", exists=True):
    cmds.deleteUI("myWindow", window=True)

my_window = cmds.window("myWindow", title="Tabbed UI Example")

# Set the width and height of the window
window_width = 500
window_height = 300
cmds.window(my_window, edit=True, widthHeight=(window_width, window_height))

# Create the tab layout
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

# First tab
cmds.setParent(tabs)
tab1 = cmds.columnLayout(adjustableColumn=True)
pm.text(label="Temporary Content for Tab 1")

# Second tab
cmds.setParent(tabs)
tab2 = cmds.columnLayout(adjustableColumn=True)
pm.text(label="Temporary Content for Tab 2")

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

# Add the tabs to the tab layout
cmds.tabLayout(tabs, edit=True, tabLabel=((tab1, 'Eyes'), (tab2, 'LipSeal'), (tab3, 'Facial')))

# Show the window
cmds.showWindow(my_window)
