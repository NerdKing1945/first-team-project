import maya.cmds as cmds
import pymel.core as pm

def makePri(*args):
    selected = int(pm.radioButtonGrp('RBGrp1', q=1, select=1))
    if selected == 1:
        queryTextFld1()
    if selected == 2:
        queryTextFld2()
    if selected == 3:
        queryTextFld3()

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
cmds.tabLayout(tabs, edit=True, tabLabel=((tab1, 'Eyes'), (tab2, 'LipSeal 2'), (tab3, 'Facial')))

# Show the window
cmds.showWindow(my_window)
