import maya.cmds as cmds

def place_selected_on_curve():
    ''' Algorithm / Pseudocode / Steps in plain English
    For each object:
    Select object
    Select curve
    Apply motion path (with default settings)
    Break animation connection from U value of motionPath
    Set U value
    
    '''
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
        #total_length_of_curve = 1
        
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

# Call the function to distribute objects on the curve
place_selected_on_curve()
