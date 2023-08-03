import maya.cmds as cmds
import maya.cmds as mc
import pymel.core as pm

cmds.window( widthHeight=(420, 300), t= "Jimmy_Vehicle_Setup_ver5.0", s=0)
form = cmds.formLayout()
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

child1 = cmds.rowColumnLayout(numberOfColumns=3)





def importCOGs(*argn):
    #import maya.mel as mel
    #mel.eval('file -import -type "mayaAscii" -mergeNamespacesOnClash false -rpr "Vehicle_COGs" -options "v=0;" "C:/Users/jyang/Documents/Jimmy_Folder/Vehicle_COGs.ma"')
    import maya.cmds as cmds
    import maya.mel as mel
    
    import os
        
    rePath = os.environ["HOME"] +'/maya/scripts/wheelSpinScript'
    rePathCOG = rePath + '/Vehicle_COGs.ma'
    
    cmds.file( '%s' % rePathCOG, i=True, defaultNamespace = True )   
    
def addallExtras(*argn):
    import pymel.core as pm

    # Clear the selection
    pm.select(cl=True)
    
    # Select the group named "CTRL_ALL_EXTRAS"
    pm.select("CTRL_ALL_EXTRAS", add=True)
    
    # Add the "WHEELS_STREET" attribute as an enum with a single option
    pm.addAttr(ln="WHEELS_STREET", at="enum", en="----------:")
    pm.setAttr("CTRL_ALL_EXTRAS.WHEELS_STREET", e=True, channelBox=True)
    
    # Add the "autoWheels" attribute as a long (integer) with range 0 to 1 and default value 0
    pm.addAttr(ln="autoWheels", at="long", min=0, max=1, dv=0)
    pm.setAttr("CTRL_ALL_EXTRAS.autoWheels", e=True, keyable=True)
    
    # Add the "wheelFactor" attribute as a double with default value 1
    pm.addAttr(ln="wheelFactor", at="double", dv=1)
    pm.setAttr("CTRL_ALL_EXTRAS.wheelFactor", e=True, keyable=True)
    
    # Add the "manualWheels" attribute as a double with default value 1
    pm.addAttr(ln="manualWheels", at="double", dv=1)
    pm.setAttr("CTRL_ALL_EXTRAS.manualWheels", e=True, keyable=True)

def tweakCOGs1(*argn):
    print "bb"

def tweakCOGs2(*argn):
    print "cc"

def tweakCOGs3(*argn):
    print "dd"

#import COGs 
cmds.button(l="Import COGs", c=importCOGs)
cmds.button(l="AddAllEXTRAS", c=addallExtras)
cmds.text(l="")

cmds.button(l="Tweak COGs", c=tweakCOGs1)
cmds.button(l="Tweak COGs", c=tweakCOGs2)
cmds.button(l="Tweak COGs", c=tweakCOGs3)
cmds.setParent( '..' )

child2 = cmds.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=410)


#import Wheelspin CVs


def importWheelSP0(*argn):
    #import maya.mel as mel
    #mel.eval('file -import -type "mayaAscii" -mergeNamespacesOnClash false -rpr "Vehicle_Wheelspin_CV_PC" -options "v=0;" "C:/Users/jyang/Documents/Jimmy_Folder/Vehicle_Wheelspin_CV_PC.ma"')

    import maya.cmds as cmds
    import maya.mel as mel

    import os


    rePath = os.environ["HOME"] +'/maya/scripts/wheelSpinScript'
    rePathCV = rePath + '/Vehicle_Wheelspin_CV_PC.ma'


    cmds.file( '%s' % rePathCV, i=True, defaultNamespace = True )



def importWheelSP1(*argn):
    import maya.mel as mel
    import os
    
    rePath = os.environ["HOME"] +'/maya/scripts/wheelSpinScript'
    rePathSY = rePath + '/ApplySymmetry.mel'
    mel.eval('source "%s"' % rePathSY)
    mel.eval('symmeTRI')

def importWheelSP2(*argn):
    import maya.mel as mel
    import os
    
    rePath = os.environ["HOME"] +'/maya/scripts/wheelSpinScript'
    rePathACW = rePath + '/ApplyCtrlWheels.mel'
    mel.eval('source "%s"' % rePathACW)
    mel.eval('ctrlWheels')
    
def importWheelSP3(*argn):
    import pymel.core as pm
    pm.select(cl=1)
    pm.select('CTRL_COG_MAIN_A',r=1)
    pm.select('CTRL_COG_MAIN_B',add=1)
    pm.select('CTRL_WHEELSPIN_FR',add=1)
    pm.select('CTRL_WHEELSPIN_BR',add=1)
    pm.select('CTRL_WHEELSPIN_FL',add=1)
    pm.select('CTRL_WHEELSPIN_BL',add=1)
    pm.select('CTRL_WHEEL_FR',add=1)
    pm.select('CTRL_WHEEL_BR',add=1)
    pm.select('CTRL_WHEEL_FL',add=1)
    pm.select('CTRL_WHEEL_BL',add=1)
    pm.select('CTRL_WHEELS',add=1)
    
   


cmds.button(l="Import Wheelspin_CV", c=importWheelSP0)

cmds.text(l="place and resize the wheelspin curves",h=40,w= 200,rs=1)
cmds.text(l="Outline needs to be cleared except 4 CTRLs",h=40,w= 200,rs=1)

cmds.button(l="Symmetri Wheelspin_CV", c=importWheelSP1)

cmds.button(l="Set CTRL_WHEELS",c=importWheelSP2)

cmds.button(l="Select All WheelSpin Vehicle_CTRLs", c=importWheelSP3)
cmds.setParent( '..' )



child3 = pm.frameLayout(label="First Step")


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

name1 = cmds.textField("nameOfTexFld0", tx="vehicle_ctrl")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name1))
cmds.text(label='------------------')

name2 = cmds.textField("nameOfTexFld00", tx="vehicle_ctrl_parent")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name2))
cmds.text(label='------------------')

name3 = cmds.textField("nameOfTexFld1", tx="groupName_wheelPosition_parentConstraint1")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name3))
cmds.text(label='.target[0].targetOffsetRotateX')

name4 = cmds.textField("nameOfTexFld2", tx="groupname_wheelPosition_parentConstraint1")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name4))
cmds.text(label='.target[0].targetOffsetRotateX')

name5 = cmds.textField("nameOfTexFld3", tx="groupname_wheelPosition_parentConstraint1")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name5))
cmds.text(label='.target[0].targetOffsetRotateX')

name6 = cmds.textField("nameOfTexFld4", tx="groupname_wheelPosition_parentConstraint1")
cmds.button(l="CV", c=lambda x: copy_selected_object_to_text_field(name6))
cmds.text(label='.target[0].targetOffsetRotateX')



pm.setParent('..')
pm.frameLayout(label="Second Step")
pm.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 450)] )








#defines Himanish Wheelspin script


#radio buttonX
def queryTextFldX(*args):
    print mc.textField("nameOfTexFld0", q=True, tx=1)
    vehicle_ctrl = mc.textField("nameOfTexFld0", q=True, tx=1)
    print mc.textField("nameOfTexFld00", q=True, tx=1)
    vehicle_ctrl_parent = mc.textField("nameOfTexFld00", q=True, tx=1)
    
    
    print mc.textField("nameOfTexFld1", q=True, tx=1) + ".target[0].targetOffsetRotateX"
    rePlace1 = mc.textField("nameOfTexFld1", q=True, tx=1) + ".target[0].targetOffsetRotateX"
    print mc.textField("nameOfTexFld2", q=True, tx=1) + ".target[0].targetOffsetRotateX"
    rePlace2 = mc.textField("nameOfTexFld2", q=True, tx=1) + ".target[0].targetOffsetRotateX"
    print mc.textField("nameOfTexFld3", q=True, tx=1) + ".target[0].targetOffsetRotateX"
    rePlace3 = mc.textField("nameOfTexFld3", q=True, tx=1) + ".target[0].targetOffsetRotateX"
    print mc.textField("nameOfTexFld4", q=True, tx=1) + ".target[0].targetOffsetRotateX"
    rePlace4 = mc.textField("nameOfTexFld4", q=True, tx=1) + ".target[0].targetOffsetRotateX"
    
    
    autoWheelWeightAttr = 'CTRL_ALL_EXTRAS.autoWheels'  # weight attribute for auto wheel rotations
    wheelDiameterFactorAttr = 'CTRL_ALL_EXTRAS.wheelFactor'
    
    
    
 
    #3rd replacement
    wheel_rotate_transform_attrs = (rePlace1,
                                rePlace2,
                                rePlace3,
                                rePlace4
                                                              
                                )
    
    # local orientation axes with respect to world axes directions
    local_aim_axis = 'Z'
    local_up_axis = 'Y'
    local_cross_axis = 'X'
    
    ###########################################################################################################
    # clean-up
    for node in ('default_base_pos', 'default_base_aim_pos', 'default_base_cross_pos', 'default_base_up_pos',
                 'vehicle_default_aim_vector', 'vehicle_default_cross_vector', 'vehicle_default_up_vector',
                 'vehicle_move_base_pos', 'vehicle_move_aim_pos', 'vehicle_move_cross_pos', 'vehicle_move_up_pos',
                 'vehicle_move_aim_vector', 'vehicle_move_cross_vector', 'vehicle_move_up_vector',
                 'vehicleAim_to_defaultAim_dot', 'vehicleAim_to_defaultCross_dot', 'vehicleAim_to_defaultUp_dot',
                 'vehicle_auto_wheel_factor', 'vehicle_auto_wheel_rot_exp'):
                 if mc.objExists(node):
                    mc.delete(node)
                  
    # world pos loc on the parent transform for the vehicle move control
    default_base_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_pos')
    mc.setAttr(default_base_pos+'.visibility', 0)
    
    # world aim loc on the parent transform for the vehicle move control
    default_base_aim_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_aim_pos')
    mc.setAttr(default_base_aim_pos+'.localPosition%s'%local_aim_axis, 5)
    mc.setAttr(default_base_aim_pos+'.visibility', 0)
    
    # world cross loc on the parent transform for the vehicle move control
    default_base_cross_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_cross_pos')
    mc.setAttr(default_base_cross_pos+'.localPosition%s'%local_cross_axis, 5)
    mc.setAttr(default_base_cross_pos+'.visibility', 0)
    
    # world up loc on the parent transform for the vehicle move control
    default_base_up_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_up_pos')
    mc.setAttr(default_base_up_pos+'.localPosition%s'%local_up_axis, 5)
    mc.setAttr(default_base_up_pos+'.visibility', 0)
    
    # Default vectors #
    
    # Default aim vector
    default_aim_vector = mc.createNode('plusMinusAverage', name='vehicle_default_aim_vector')
    mc.setAttr(default_aim_vector+'.operation', 2)
    mc.connectAttr(default_base_aim_pos+'.worldPosition[0]', default_aim_vector+'.input3D[0]', force=True)
    mc.connectAttr(default_base_pos+'.worldPosition[0]', default_aim_vector+'.input3D[1]', force=True)
    
    # Default cross vector
    default_cross_vector = mc.createNode('plusMinusAverage', name='vehicle_default_cross_vector')
    mc.setAttr(default_cross_vector+'.operation', 2)
    mc.connectAttr(default_base_cross_pos+'.worldPosition[0]', default_cross_vector+'.input3D[0]', force=True)
    mc.connectAttr(default_base_pos+'.worldPosition[0]', default_cross_vector+'.input3D[1]', force=True)
    
    # Default up vector
    default_up_vector = mc.createNode('plusMinusAverage', name='vehicle_default_up_vector')
    mc.setAttr(default_up_vector+'.operation', 2)
    mc.connectAttr(default_base_up_pos+'.worldPosition[0]', default_up_vector+'.input3D[0]', force=True)
    mc.connectAttr(default_base_pos+'.worldPosition[0]', default_up_vector+'.input3D[1]', force=True)
    
    # -----------------------------------------------------------------------------------------------------------
    
    # world pos loc for the vehicle move control
    vehicle_move_base_pos = mc.createNode('locator', parent=vehicle_ctrl, name='vehicle_move_base_pos')
    mc.setAttr(vehicle_move_base_pos+'.visibility', 0)
    
    # world aim loc for the vehicle move control
    vehicle_move_aim_pos = mc.createNode('locator', parent=vehicle_ctrl, name='vehicle_move_aim_pos')
    mc.setAttr(vehicle_move_aim_pos+'.localPosition%s'%local_aim_axis, 5)
    mc.setAttr(vehicle_move_aim_pos+'.visibility', 0)
    
    # Move vectors #
    
    # Move aim vector
    # For the vehicle, we only want to compare the aim vector with default aim, cross and up.
    move_aim_vector = mc.createNode('plusMinusAverage', name='vehicle_move_aim_vector')
    mc.setAttr(move_aim_vector+'.operation', 2)
    mc.connectAttr(vehicle_move_aim_pos+'.worldPosition[0]', move_aim_vector+'.input3D[0]', force=True)
    mc.connectAttr(vehicle_move_base_pos+'.worldPosition[0]', move_aim_vector+'.input3D[1]', force=True)
    
    
    # -----------------------------------------------------------------------------------------------------------
    
    # Default / Move Dot products
    
    # Move aim dot
    vehicle_to_default_aim_dot = mc.createNode('vectorProduct', name='vehicleAim_to_defaultAim_dot')
    mc.setAttr(vehicle_to_default_aim_dot+'.operation', 1)
    mc.setAttr(vehicle_to_default_aim_dot+'.normalizeOutput', 1)
    mc.connectAttr(default_aim_vector+'.output3D', vehicle_to_default_aim_dot+'.input1', force=True)
    mc.connectAttr(move_aim_vector+'.output3D', vehicle_to_default_aim_dot+'.input2', force=True)
    
    # Move cross dot
    vehicle_to_default_cross_dot = mc.createNode('vectorProduct', name='vehicleAim_to_defaultCross_dot')
    mc.setAttr(vehicle_to_default_cross_dot+'.operation', 1)
    mc.setAttr(vehicle_to_default_cross_dot+'.normalizeOutput', 1)
    mc.connectAttr(default_cross_vector+'.output3D', vehicle_to_default_cross_dot+'.input1', force=True)
    mc.connectAttr(move_aim_vector+'.output3D', vehicle_to_default_cross_dot+'.input2', force=True)
    
    # Move up dot
    vehicle_to_default_up_dot = mc.createNode('vectorProduct', name='vehicleAim_to_defaultUp_dot')
    mc.setAttr(vehicle_to_default_up_dot+'.operation', 1)
    mc.setAttr(vehicle_to_default_up_dot+'.normalizeOutput', 1)
    mc.connectAttr(default_up_vector+'.output3D', vehicle_to_default_up_dot+'.input1', force=True)
    mc.connectAttr(move_aim_vector+'.output3D', vehicle_to_default_up_dot+'.input2', force=True)
    
    # -----------------------------------------------------------------------------------------------------------
    # Wheel multipliers
    
    # Auto wheel axes dot multiplier
    auto_wheel_factor = mc.createNode('multiplyDivide', name='vehicle_auto_wheel_factor')
    
    mc.connectAttr(vehicle_to_default_aim_dot+'.outputX', auto_wheel_factor+'.input1X', force=True)
    mc.connectAttr(vehicle_to_default_cross_dot+'.outputX', auto_wheel_factor+'.input1Y', force=True)
    mc.connectAttr(vehicle_to_default_up_dot+'.outputX', auto_wheel_factor+'.input1Z', force=True)
    
    mc.connectAttr(vehicle_ctrl+'.translate%s'%local_aim_axis, auto_wheel_factor+'.input2X', force=True)
    mc.connectAttr(vehicle_ctrl+'.translate%s'%local_cross_axis, auto_wheel_factor+'.input2Y', force=True)
    mc.connectAttr(vehicle_ctrl+'.translate%s'%local_up_axis, auto_wheel_factor+'.input2Z', force=True)
    
    # Auto wheel axes weight multiplier expression
    auto_wheel_rot_exp = '$weight = %s;' % autoWheelWeightAttr
    auto_wheel_rot_exp += '\n$factor = %s;' % wheelDiameterFactorAttr
    for transform_attr in wheel_rotate_transform_attrs:
        auto_wheel_rot_exp += '\n{0} = ({1}.outputX + {1}.outputY + {1}.outputZ) * $factor * $weight;' \
                                    .format(transform_attr, auto_wheel_factor)
    
    mc.expression(string=auto_wheel_rot_exp, alwaysEvaluate=0, name='vehicle_auto_wheel_rot_exp')  
    

#radio buttonY
def queryTextFldY(*args):
    print mc.textField("nameOfTexFld0", q=True, tx=1)
    vehicle_ctrl = mc.textField("nameOfTexFld0", q=True, tx=1)
    print mc.textField("nameOfTexFld00", q=True, tx=1)
    vehicle_ctrl_parent = mc.textField("nameOfTexFld00", q=True, tx=1)
    
    
    print mc.textField("nameOfTexFld1", q=True, tx=1) + ".target[0].targetOffsetRotateY"
    rePlace1 = mc.textField("nameOfTexFld1", q=True, tx=1) + ".target[0].targetOffsetRotateY"
    print mc.textField("nameOfTexFld2", q=True, tx=1) + ".target[0].targetOffsetRotateY"
    rePlace2 = mc.textField("nameOfTexFld2", q=True, tx=1) + ".target[0].targetOffsetRotateY"
    print mc.textField("nameOfTexFld3", q=True, tx=1) + ".target[0].targetOffsetRotateY"
    rePlace3 = mc.textField("nameOfTexFld3", q=True, tx=1) + ".target[0].targetOffsetRotateY"
    print mc.textField("nameOfTexFld4", q=True, tx=1) + ".target[0].targetOffsetRotateY"
    rePlace4 = mc.textField("nameOfTexFld4", q=True, tx=1) + ".target[0].targetOffsetRotateY"
    
    
    autoWheelWeightAttr = 'CTRL_ALL_EXTRAS.autoWheels'  # weight attribute for auto wheel rotations
    wheelDiameterFactorAttr = 'CTRL_ALL_EXTRAS.wheelFactor'
    
    
    
 
    #3rd replacement
    wheel_rotate_transform_attrs = (rePlace1,
                                rePlace2,
                                rePlace3,
                                rePlace4
                                                              
                                )
    
    # local orientation axes with respect to world axes directions
    local_aim_axis = 'Z'
    local_up_axis = 'Y'
    local_cross_axis = 'X'
    
    ###########################################################################################################
    # clean-up
    for node in ('default_base_pos', 'default_base_aim_pos', 'default_base_cross_pos', 'default_base_up_pos',
                 'vehicle_default_aim_vector', 'vehicle_default_cross_vector', 'vehicle_default_up_vector',
                 'vehicle_move_base_pos', 'vehicle_move_aim_pos', 'vehicle_move_cross_pos', 'vehicle_move_up_pos',
                 'vehicle_move_aim_vector', 'vehicle_move_cross_vector', 'vehicle_move_up_vector',
                 'vehicleAim_to_defaultAim_dot', 'vehicleAim_to_defaultCross_dot', 'vehicleAim_to_defaultUp_dot',
                 'vehicle_auto_wheel_factor', 'vehicle_auto_wheel_rot_exp'):
                 if mc.objExists(node):
                    mc.delete(node)
                  
    # world pos loc on the parent transform for the vehicle move control
    default_base_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_pos')
    mc.setAttr(default_base_pos+'.visibility', 0)
    
    # world aim loc on the parent transform for the vehicle move control
    default_base_aim_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_aim_pos')
    mc.setAttr(default_base_aim_pos+'.localPosition%s'%local_aim_axis, 5)
    mc.setAttr(default_base_aim_pos+'.visibility', 0)
    
    # world cross loc on the parent transform for the vehicle move control
    default_base_cross_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_cross_pos')
    mc.setAttr(default_base_cross_pos+'.localPosition%s'%local_cross_axis, 5)
    mc.setAttr(default_base_cross_pos+'.visibility', 0)
    
    # world up loc on the parent transform for the vehicle move control
    default_base_up_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_up_pos')
    mc.setAttr(default_base_up_pos+'.localPosition%s'%local_up_axis, 5)
    mc.setAttr(default_base_up_pos+'.visibility', 0)
    
    # Default vectors #
    
    # Default aim vector
    default_aim_vector = mc.createNode('plusMinusAverage', name='vehicle_default_aim_vector')
    mc.setAttr(default_aim_vector+'.operation', 2)
    mc.connectAttr(default_base_aim_pos+'.worldPosition[0]', default_aim_vector+'.input3D[0]', force=True)
    mc.connectAttr(default_base_pos+'.worldPosition[0]', default_aim_vector+'.input3D[1]', force=True)
    
    # Default cross vector
    default_cross_vector = mc.createNode('plusMinusAverage', name='vehicle_default_cross_vector')
    mc.setAttr(default_cross_vector+'.operation', 2)
    mc.connectAttr(default_base_cross_pos+'.worldPosition[0]', default_cross_vector+'.input3D[0]', force=True)
    mc.connectAttr(default_base_pos+'.worldPosition[0]', default_cross_vector+'.input3D[1]', force=True)
    
    # Default up vector
    default_up_vector = mc.createNode('plusMinusAverage', name='vehicle_default_up_vector')
    mc.setAttr(default_up_vector+'.operation', 2)
    mc.connectAttr(default_base_up_pos+'.worldPosition[0]', default_up_vector+'.input3D[0]', force=True)
    mc.connectAttr(default_base_pos+'.worldPosition[0]', default_up_vector+'.input3D[1]', force=True)
    
    # -----------------------------------------------------------------------------------------------------------
    
    # world pos loc for the vehicle move control
    vehicle_move_base_pos = mc.createNode('locator', parent=vehicle_ctrl, name='vehicle_move_base_pos')
    mc.setAttr(vehicle_move_base_pos+'.visibility', 0)
    
    # world aim loc for the vehicle move control
    vehicle_move_aim_pos = mc.createNode('locator', parent=vehicle_ctrl, name='vehicle_move_aim_pos')
    mc.setAttr(vehicle_move_aim_pos+'.localPosition%s'%local_aim_axis, 5)
    mc.setAttr(vehicle_move_aim_pos+'.visibility', 0)
    
    # Move vectors #
    
    # Move aim vector
    # For the vehicle, we only want to compare the aim vector with default aim, cross and up.
    move_aim_vector = mc.createNode('plusMinusAverage', name='vehicle_move_aim_vector')
    mc.setAttr(move_aim_vector+'.operation', 2)
    mc.connectAttr(vehicle_move_aim_pos+'.worldPosition[0]', move_aim_vector+'.input3D[0]', force=True)
    mc.connectAttr(vehicle_move_base_pos+'.worldPosition[0]', move_aim_vector+'.input3D[1]', force=True)
    
    
    # -----------------------------------------------------------------------------------------------------------
    
    # Default / Move Dot products
    
    # Move aim dot
    vehicle_to_default_aim_dot = mc.createNode('vectorProduct', name='vehicleAim_to_defaultAim_dot')
    mc.setAttr(vehicle_to_default_aim_dot+'.operation', 1)
    mc.setAttr(vehicle_to_default_aim_dot+'.normalizeOutput', 1)
    mc.connectAttr(default_aim_vector+'.output3D', vehicle_to_default_aim_dot+'.input1', force=True)
    mc.connectAttr(move_aim_vector+'.output3D', vehicle_to_default_aim_dot+'.input2', force=True)
    
    # Move cross dot
    vehicle_to_default_cross_dot = mc.createNode('vectorProduct', name='vehicleAim_to_defaultCross_dot')
    mc.setAttr(vehicle_to_default_cross_dot+'.operation', 1)
    mc.setAttr(vehicle_to_default_cross_dot+'.normalizeOutput', 1)
    mc.connectAttr(default_cross_vector+'.output3D', vehicle_to_default_cross_dot+'.input1', force=True)
    mc.connectAttr(move_aim_vector+'.output3D', vehicle_to_default_cross_dot+'.input2', force=True)
    
    # Move up dot
    vehicle_to_default_up_dot = mc.createNode('vectorProduct', name='vehicleAim_to_defaultUp_dot')
    mc.setAttr(vehicle_to_default_up_dot+'.operation', 1)
    mc.setAttr(vehicle_to_default_up_dot+'.normalizeOutput', 1)
    mc.connectAttr(default_up_vector+'.output3D', vehicle_to_default_up_dot+'.input1', force=True)
    mc.connectAttr(move_aim_vector+'.output3D', vehicle_to_default_up_dot+'.input2', force=True)
    
    # -----------------------------------------------------------------------------------------------------------
    # Wheel multipliers
    
    # Auto wheel axes dot multiplier
    auto_wheel_factor = mc.createNode('multiplyDivide', name='vehicle_auto_wheel_factor')
    
    mc.connectAttr(vehicle_to_default_aim_dot+'.outputX', auto_wheel_factor+'.input1X', force=True)
    mc.connectAttr(vehicle_to_default_cross_dot+'.outputX', auto_wheel_factor+'.input1Y', force=True)
    mc.connectAttr(vehicle_to_default_up_dot+'.outputX', auto_wheel_factor+'.input1Z', force=True)
    
    mc.connectAttr(vehicle_ctrl+'.translate%s'%local_aim_axis, auto_wheel_factor+'.input2X', force=True)
    mc.connectAttr(vehicle_ctrl+'.translate%s'%local_cross_axis, auto_wheel_factor+'.input2Y', force=True)
    mc.connectAttr(vehicle_ctrl+'.translate%s'%local_up_axis, auto_wheel_factor+'.input2Z', force=True)
    
    # Auto wheel axes weight multiplier expression
    auto_wheel_rot_exp = '$weight = %s;' % autoWheelWeightAttr
    auto_wheel_rot_exp += '\n$factor = %s;' % wheelDiameterFactorAttr
    for transform_attr in wheel_rotate_transform_attrs:
        auto_wheel_rot_exp += '\n{0} = ({1}.outputX + {1}.outputY + {1}.outputZ) * $factor * $weight;' \
                                    .format(transform_attr, auto_wheel_factor)
    
    mc.expression(string=auto_wheel_rot_exp, alwaysEvaluate=0, name='vehicle_auto_wheel_rot_exp')  


#radio buttonZ
def queryTextFldZ(*args):
    print mc.textField("nameOfTexFld0", q=True, tx=1)
    vehicle_ctrl = mc.textField("nameOfTexFld0", q=True, tx=1)
    print mc.textField("nameOfTexFld00", q=True, tx=1)
    vehicle_ctrl_parent = mc.textField("nameOfTexFld00", q=True, tx=1)
    
    
    print mc.textField("nameOfTexFld1", q=True, tx=1) + ".target[0].targetOffsetRotateZ"
    rePlace1 = mc.textField("nameOfTexFld1", q=True, tx=1) + ".target[0].targetOffsetRotateZ"
    print mc.textField("nameOfTexFld2", q=True, tx=1) + ".target[0].targetOffsetRotateZ"
    rePlace2 = mc.textField("nameOfTexFld2", q=True, tx=1) + ".target[0].targetOffsetRotateZ"
    print mc.textField("nameOfTexFld3", q=True, tx=1) + ".target[0].targetOffsetRotateZ"
    rePlace3 = mc.textField("nameOfTexFld3", q=True, tx=1) + ".target[0].targetOffsetRotateZ"
    print mc.textField("nameOfTexFld4", q=True, tx=1) + ".target[0].targetOffsetRotateZ"
    rePlace4 = mc.textField("nameOfTexFld4", q=True, tx=1) + ".target[0].targetOffsetRotateZ"
    
    
    autoWheelWeightAttr = 'CTRL_ALL_EXTRAS.autoWheels'  # weight attribute for auto wheel rotations
    wheelDiameterFactorAttr = 'CTRL_ALL_EXTRAS.wheelFactor'
    
    
    
 
    #3rd replacement
    wheel_rotate_transform_attrs = (rePlace1,
                                rePlace2,
                                rePlace3,
                                rePlace4
                                                              
                                )
    
    # local orientation axes with respect to world axes directions
    local_aim_axis = 'Z'
    local_up_axis = 'Y'
    local_cross_axis = 'X'
    
    ###########################################################################################################
    # clean-up
    for node in ('default_base_pos', 'default_base_aim_pos', 'default_base_cross_pos', 'default_base_up_pos',
                 'vehicle_default_aim_vector', 'vehicle_default_cross_vector', 'vehicle_default_up_vector',
                 'vehicle_move_base_pos', 'vehicle_move_aim_pos', 'vehicle_move_cross_pos', 'vehicle_move_up_pos',
                 'vehicle_move_aim_vector', 'vehicle_move_cross_vector', 'vehicle_move_up_vector',
                 'vehicleAim_to_defaultAim_dot', 'vehicleAim_to_defaultCross_dot', 'vehicleAim_to_defaultUp_dot',
                 'vehicle_auto_wheel_factor', 'vehicle_auto_wheel_rot_exp'):
                 if mc.objExists(node):
                    mc.delete(node)
                  
    # world pos loc on the parent transform for the vehicle move control
    default_base_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_pos')
    mc.setAttr(default_base_pos+'.visibility', 0)
    
    # world aim loc on the parent transform for the vehicle move control
    default_base_aim_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_aim_pos')
    mc.setAttr(default_base_aim_pos+'.localPosition%s'%local_aim_axis, 5)
    mc.setAttr(default_base_aim_pos+'.visibility', 0)
    
    # world cross loc on the parent transform for the vehicle move control
    default_base_cross_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_cross_pos')
    mc.setAttr(default_base_cross_pos+'.localPosition%s'%local_cross_axis, 5)
    mc.setAttr(default_base_cross_pos+'.visibility', 0)
    
    # world up loc on the parent transform for the vehicle move control
    default_base_up_pos = mc.createNode('locator', parent=vehicle_ctrl_parent, name='default_base_up_pos')
    mc.setAttr(default_base_up_pos+'.localPosition%s'%local_up_axis, 5)
    mc.setAttr(default_base_up_pos+'.visibility', 0)
    
    # Default vectors #
    
    # Default aim vector
    default_aim_vector = mc.createNode('plusMinusAverage', name='vehicle_default_aim_vector')
    mc.setAttr(default_aim_vector+'.operation', 2)
    mc.connectAttr(default_base_aim_pos+'.worldPosition[0]', default_aim_vector+'.input3D[0]', force=True)
    mc.connectAttr(default_base_pos+'.worldPosition[0]', default_aim_vector+'.input3D[1]', force=True)
    
    # Default cross vector
    default_cross_vector = mc.createNode('plusMinusAverage', name='vehicle_default_cross_vector')
    mc.setAttr(default_cross_vector+'.operation', 2)
    mc.connectAttr(default_base_cross_pos+'.worldPosition[0]', default_cross_vector+'.input3D[0]', force=True)
    mc.connectAttr(default_base_pos+'.worldPosition[0]', default_cross_vector+'.input3D[1]', force=True)
    
    # Default up vector
    default_up_vector = mc.createNode('plusMinusAverage', name='vehicle_default_up_vector')
    mc.setAttr(default_up_vector+'.operation', 2)
    mc.connectAttr(default_base_up_pos+'.worldPosition[0]', default_up_vector+'.input3D[0]', force=True)
    mc.connectAttr(default_base_pos+'.worldPosition[0]', default_up_vector+'.input3D[1]', force=True)
    
    # -----------------------------------------------------------------------------------------------------------
    
    # world pos loc for the vehicle move control
    vehicle_move_base_pos = mc.createNode('locator', parent=vehicle_ctrl, name='vehicle_move_base_pos')
    mc.setAttr(vehicle_move_base_pos+'.visibility', 0)
    
    # world aim loc for the vehicle move control
    vehicle_move_aim_pos = mc.createNode('locator', parent=vehicle_ctrl, name='vehicle_move_aim_pos')
    mc.setAttr(vehicle_move_aim_pos+'.localPosition%s'%local_aim_axis, 5)
    mc.setAttr(vehicle_move_aim_pos+'.visibility', 0)
    
    # Move vectors #
    
    # Move aim vector
    # For the vehicle, we only want to compare the aim vector with default aim, cross and up.
    move_aim_vector = mc.createNode('plusMinusAverage', name='vehicle_move_aim_vector')
    mc.setAttr(move_aim_vector+'.operation', 2)
    mc.connectAttr(vehicle_move_aim_pos+'.worldPosition[0]', move_aim_vector+'.input3D[0]', force=True)
    mc.connectAttr(vehicle_move_base_pos+'.worldPosition[0]', move_aim_vector+'.input3D[1]', force=True)
    
    
    # -----------------------------------------------------------------------------------------------------------
    
    # Default / Move Dot products
    
    # Move aim dot
    vehicle_to_default_aim_dot = mc.createNode('vectorProduct', name='vehicleAim_to_defaultAim_dot')
    mc.setAttr(vehicle_to_default_aim_dot+'.operation', 1)
    mc.setAttr(vehicle_to_default_aim_dot+'.normalizeOutput', 1)
    mc.connectAttr(default_aim_vector+'.output3D', vehicle_to_default_aim_dot+'.input1', force=True)
    mc.connectAttr(move_aim_vector+'.output3D', vehicle_to_default_aim_dot+'.input2', force=True)
    
    # Move cross dot
    vehicle_to_default_cross_dot = mc.createNode('vectorProduct', name='vehicleAim_to_defaultCross_dot')
    mc.setAttr(vehicle_to_default_cross_dot+'.operation', 1)
    mc.setAttr(vehicle_to_default_cross_dot+'.normalizeOutput', 1)
    mc.connectAttr(default_cross_vector+'.output3D', vehicle_to_default_cross_dot+'.input1', force=True)
    mc.connectAttr(move_aim_vector+'.output3D', vehicle_to_default_cross_dot+'.input2', force=True)
    
    # Move up dot
    vehicle_to_default_up_dot = mc.createNode('vectorProduct', name='vehicleAim_to_defaultUp_dot')
    mc.setAttr(vehicle_to_default_up_dot+'.operation', 1)
    mc.setAttr(vehicle_to_default_up_dot+'.normalizeOutput', 1)
    mc.connectAttr(default_up_vector+'.output3D', vehicle_to_default_up_dot+'.input1', force=True)
    mc.connectAttr(move_aim_vector+'.output3D', vehicle_to_default_up_dot+'.input2', force=True)
    
    # -----------------------------------------------------------------------------------------------------------
    # Wheel multipliers
    
    # Auto wheel axes dot multiplier
    auto_wheel_factor = mc.createNode('multiplyDivide', name='vehicle_auto_wheel_factor')
    
    mc.connectAttr(vehicle_to_default_aim_dot+'.outputX', auto_wheel_factor+'.input1X', force=True)
    mc.connectAttr(vehicle_to_default_cross_dot+'.outputX', auto_wheel_factor+'.input1Y', force=True)
    mc.connectAttr(vehicle_to_default_up_dot+'.outputX', auto_wheel_factor+'.input1Z', force=True)
    
    mc.connectAttr(vehicle_ctrl+'.translate%s'%local_aim_axis, auto_wheel_factor+'.input2X', force=True)
    mc.connectAttr(vehicle_ctrl+'.translate%s'%local_cross_axis, auto_wheel_factor+'.input2Y', force=True)
    mc.connectAttr(vehicle_ctrl+'.translate%s'%local_up_axis, auto_wheel_factor+'.input2Z', force=True)
    
    # Auto wheel axes weight multiplier expression
    auto_wheel_rot_exp = '$weight = %s;' % autoWheelWeightAttr
    auto_wheel_rot_exp += '\n$factor = %s;' % wheelDiameterFactorAttr
    for transform_attr in wheel_rotate_transform_attrs:
        auto_wheel_rot_exp += '\n{0} = ({1}.outputX + {1}.outputY + {1}.outputZ) * $factor * $weight;' \
                                    .format(transform_attr, auto_wheel_factor)
    
    mc.expression(string=auto_wheel_rot_exp, alwaysEvaluate=0, name='vehicle_auto_wheel_rot_exp')  



import pymel.core as pm
def makePri(*argn):
	selected=0
	selected=int(pm.radioButtonGrp('RBGrp1',q=1,select=1))
	if selected == 1:
		queryTextFldX()
		
	if selected == 2:
		queryTextFldY()
		
	if selected == 3:
		queryTextFldZ()
		
	


pm.formLayout('myForm',numberOfDivisions=100)
pm.text(label="")
pm.radioButtonGrp('RBGrp1',numberOfRadioButtons=3,
	labelArray3=("rotateX", "rotateY", "rotateZ"),select=1,label="OffsetType")


pm.button('myBtn1',command=makePri,label="Run Script!!")
pm.formLayout('myForm',edit=1,attachForm=[('RBGrp1', "top", 10), ('RBGrp1', "left", -50), ('myBtn1', "bottom", 10), ('myBtn1', "left", 30)])


cmds.setParent( '..' )



cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'One'), (child2, 'Two'), (child3, 'Three')) )

cmds.showWindow()







		
		
