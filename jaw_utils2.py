import maya.cmds as mc

# object constants
GROUP = 'GRP'
JOINT = 'JNT'
GUIDE = 'guide'
JAW ='jaw'

# side constants
LEFT = 'L'
RIGHT = 'R'
CENTER = 'C'

def addOffset(dst, suffix='OFF'):
    """
    return:
    """
    
    grp_offset = mc.createNode('transform', name='{}_{}'.format(dst, suffix))
    dst_mat = mc.xform(dst, q=True, m=True, ws=True)
    mc.xform(grp_offset, m=dst_mat, ws=True)

    dst_parent = mc.listRelatives(dst, parent=True)
    if dst_parent:
        mc.parent(grp_offset, dst_parent)
    mc.parent(dst, grp_offset)
    
    return grp_offset
    
def createGuides(number=8):
    """
    :param number:
    :return:
    
    """
    
    jaw_guide_grp = mc.createNode('transform', name='{}_{}_{}_{}'.format(CENTER, JAW, GUIDE, GROUP))
    locs_grp = mc.createNode('transform', name='{}_{}_lip_{}_{}'.format(CENTER, JAW, GUIDE, GROUP),
                             parent=jaw_guide_grp)
    lip_locs_grp = mc.createNode('transform', name='{}_lipMinor_{}_{}'.format(CENTER, GUIDE, GROUP), 
                                 parent=locs_grp)
    
    
    # create locators
    for part in ['Upper', 'Lower']:
        
        part_mult = 1 if part =='Upper' else -1
        mid_data = (0, part_mult, 0)
        
        mid_loc = mc.spaceLocator(name='{}_{}{}_lip_{}'.format(CENTER, JAW, part, GUIDE))[0]
        mc.parent(mid_loc, lip_locs_grp)
        
        for side in [LEFT, RIGHT]:
            for x in range(number):
                multiplier = x + 1 if side == LEFT else -(x+1)
                loc_data = (multiplier, part_mult, 0) #xyz
                loc = mc.spaceLocator(name='{}_{}{}_lip_{:02d}_{}'.format(side, JAW, part, x+1, GUIDE))[0]
                mc.parent(loc, lip_locs_grp)
            
                #set data
                mc.setAttr('{}.t'.format(loc), *loc_data)
            
            
        # set center data
        mc.setAttr('{}.t'.format(mid_loc), *mid_data)
        
    # create corners
    left_corner_loc = mc.spaceLocator(name='{}_{}Corner_lip_{}'.format(LEFT, JAW, GUIDE))[0]
    right_corner_loc = mc.spaceLocator(name='{}_{}Corner_lip_{}'.format(RIGHT, JAW, GUIDE))[0]
    
    mc.parent(left_corner_loc, lip_locs_grp)
    mc.parent(right_corner_loc, lip_locs_grp)
    
    mc.setAttr('{}.t'.format(left_corner_loc), *(number+ 1, 0, 0))
    mc.setAttr('{}.t'.format(right_corner_loc), *(-(number+ 1), 0, 0))
    
    mc.select(cl=True)
    
    # create jaw base
    
    jaw_base_guide_grp = mc.createNode('transform', name='{}_{}_base_{}_{}'.format(CENTER, JAW, GUIDE, GROUP), 
                                       parent=jaw_guide_grp)
    jaw_guide = mc.spaceLocator(name='{}_{}_{}'.format(CENTER, JAW, GUIDE))[0]
    jaw_inverse_guide = mc.spaceLocator(name='{}_{}_inverse_{}'.format(CENTER, JAW, GUIDE))[0]
    
    mc.setAttr('{}.t'.format(jaw_guide), *(0, -1, -number))
    mc.setAttr('{}.t'.format(jaw_inverse_guide), *(0, 1, -number))
    
    mc.parent(jaw_guide, jaw_base_guide_grp)
    mc.parent(jaw_inverse_guide, jaw_base_guide_grp)
    
    mc.select(cl=True)
    
def lip_guides():
    """
    :return:
    """
    
    grp = '{}_lipMinor_{}_{}'.format(CENTER, GUIDE, GROUP)
    return [loc for loc in mc.listRelatives(grp) if mc.objExists(grp)]
    
def jaw_guides():
    """
    return:
    """
    
    grp ='{}_{}_base_{}_{}'.format(CENTER, JAW, GUIDE, GROUP)
    return [loc for loc in mc.listRelatives(grp) if mc.objExists(grp)]

def build():
    """
    return:
    """
    
    
    createHierarchy()
    createMinorJoints()
    createBroadJoints()
    createJawBase()
    constraintBroadJoints()
    createSeal('upper')
    createSeal('lower')
    
    
def createHierarchy():
    """
    :return:
    
    """
    main_grp = mc.createNode('transform', name='{}_{}_rig_{}'.format(CENTER, JAW, GROUP))
    lip_grp = mc.createNode('transform', name= '{}_{}Lip_{}'.format(CENTER, JAW, GROUP), parent=main_grp)
    base_grp = mc.createNode('transform', name= '{}_{}Base_{}'.format(CENTER, JAW, GROUP), parent=main_grp)
    
    lip_minor_grp = mc.createNode('transform', name='{}_{}Lip_minor_{}'.format(CENTER, JAW, GROUP), parent=lip_grp)
    lip_broad_grp = mc.createNode('transform', name='{}_{}Lip_broad_{}'.format(CENTER, JAW, GROUP), parent=lip_grp)
    
    mc.select(cl=True)
    
    



def createMinorJoints():
    """
    :return:
    """
    
    minor_joints = list()
    
    for guide in lip_guides():
        mat = mc.xform(guide, q=True, m=True, ws=True)
        jnt = mc.joint(name=guide.replace(GUIDE, JOINT))
        mc.setAttr('{}.radius'.format(jnt), 0.5)
        mc.xform(jnt, m=mat, ws=True)
        
        # parent joint
        mc.parent(jnt, '{}_{}Lip_minor_{}'.format(CENTER, JAW, GROUP))
        
        minor_joints.append(jnt)
        
        
    return minor_joints
    
def createBroadJoints():
    """
    
    :return:
    """
    upper_joint =mc.joint(name='{}_{}_broadUpper_{}'.format(CENTER, JAW, JOINT))
    mc.select(cl=True)
    lower_joint = mc.joint(name='{}_{}_broadLower_{}'.format(CENTER, JAW, JOINT))    
    mc.select(cl=True)
    left_joint = mc.joint(name='{}_{}_broadCorner_{}'.format(LEFT, JAW, JOINT))    
    mc.select(cl=True)
    right_joint = mc.joint(name='{}_{}_broadCorner_{}'.format(RIGHT, JAW, JOINT))    
    mc.select(cl=True)

    #parent joints under broad group
    mc.parent([upper_joint, lower_joint, left_joint, right_joint], '{}_{}Lip_broad_{}'.format(CENTER, JAW, GROUP))
        
    # get guides positions
    upper_pos = mc.xform('{}_{}Upper_lip_{}'.format(CENTER, JAW, GUIDE), q=True, m=True, ws=True)
    lower_pos = mc.xform('{}_{}Lower_lip_{}'.format(CENTER, JAW, GUIDE), q=True, m=True, ws=True)
    left_pos = mc.xform('{}_{}Corner_lip_{}'.format(LEFT, JAW, GUIDE), q=True, m=True, ws=True)
    right_pos =mc.xform('{}_{}Corner_lip_{}'.format(RIGHT, JAW, GUIDE), q=True, m=True, ws=True)
    
    #set guides positions
    mc.xform(upper_joint, m=upper_pos)
    mc.xform(lower_joint, m=lower_pos)
    mc.xform(left_joint, m=left_pos)       
    mc.xform(right_joint, m=right_pos)
    
    mc.select(cl=True)
    
def createJawBase():
    """
    return:
    
    """
    
    jaw_jnt = mc.joint(name='{}_{}_{}'.format(CENTER, JAW, JOINT))
    jaw_inverse_jnt = mc.joint(name='{}_inverse_{}_{}'.format(CENTER, JAW, JOINT))
    
    jaw_mat = mc.xform(jaw_guides()[0], q=True, m=True, ws=True)
    jaw_inverse_mat = mc.xform(jaw_guides()[1], q=True, m=True, ws=True)
    
    mc.xform(jaw_jnt, m=jaw_mat, ws=True)
    mc.xform(jaw_inverse_jnt, m=jaw_inverse_mat, ws=True)
    
    mc.parent(jaw_jnt, '{}_{}Base_{}'.format(CENTER, JAW, GROUP))
    mc.parent(jaw_inverse_jnt, '{}_{}Base_{}'.format(CENTER, JAW, GROUP))
    
    mc.select(cl=True)
    
    
    # add offsets

    addOffset(jaw_jnt, suffix='OFF')
    addOffset(jaw_inverse_jnt, suffix='OFF')

    mc.select(cl=True)
    
def constraintBroadJoints():
    """
    return:
    
    """
    
    
    jaw_joint = '{}_{}_{}'.format(CENTER, JAW, JOINT)
    inverse_jaw_joint = '{}_inverse_{}_{}'.format(CENTER, JAW, JOINT)
    
    broad_upper = '{}_{}_broadUpper_{}'.format(CENTER, JAW, JOINT)
    broad_lower = '{}_{}_broadLower_{}'.format(CENTER, JAW, JOINT)
    broad_left = '{}_{}_broadCorner_{}'.format(LEFT, JAW, JOINT)
    broad_right = '{}_{}_broadCorner_{}'.format(RIGHT, JAW, JOINT)
    
    
    #add offsets to broad joints
    
    upper_off = addOffset(broad_upper)
    lower_off = addOffset(broad_lower)
    left_off = addOffset(broad_left)
    right_off = addOffset(broad_right)
    
    # create constraint to upper and lower
    mc.parentConstraint(jaw_joint, lower_off, mo=True)
    mc.parentConstraint(inverse_jaw_joint, upper_off, mo=True)
    
    
    # create constraint to corners
    mc.parentConstraint(upper_off, lower_off, left_off, mo=True)
    mc.parentConstraint(upper_off, lower_off, right_off, mo=True)
    
    mc.select(cl=True)
    
    
def getLipParts():
    """
    return:
    """
    
    upper_token = 'jawUpper'
    lower_token = 'jawLower'
    corner_token ='jawCorner'
    
    C_upper = '{}_{}_broadUpper_{}'.format(CENTER, JAW, JOINT)
    C_lower = '{}_{}_broadLower_{}'.format(CENTER, JAW, JOINT)
    L_corner = '{}_{}_broadCorner_{}'.format(LEFT, JAW, JOINT)
    R_corner = '{}_{}_broadCorner_{}'.format(RIGHT, JAW, JOINT)
    
    lip_joints = mc.listRelatives('{}_{}Lip_{}'.format(CENTER, JAW, GROUP), allDescendents=True)

    
    lookup = {'C_upper':{}, 'C_lower':{}, 
              'L_upper':{}, 'L_lower':{},
              'R_upper':{}, 'R_lower':{},
              'L_corner':{}, 'R_corner':{}}

    for joint in lip_joints:
        
        if mc.objectType(joint) != 'joint':
            continue
        
        if joint.startswith('C') and upper_token in joint:
            lookup['C_upper'][joint] = [C_upper]
            
        if joint.startswith('C') and lower_token in joint:
            lookup['C_lower'][joint] = [C_lower]
            
        if joint.startswith('L') and upper_token in joint:
            lookup['L_upper'][joint] = [C_upper, L_corner]
            
        if joint.startswith('L') and lower_token in joint:
            lookup['L_lower'][joint] = [C_lower, L_corner]
            
        if joint.startswith('R') and upper_token in joint:
            lookup['R_upper'][joint] = [C_upper, R_corner]
            
        if joint.startswith('R') and lower_token in joint:
            lookup['R_lower'][joint] = [C_lower, R_corner]
            
        if joint.startswith('L') and corner_token in joint:
            lookup['L_corner'][joint] = [L_corner]
            
        if joint.startswith('R') and corner_token in joint:
            lookup['R_corner'][joint] = [R_corner]
        
    return lookup
    
def lipPart(part):
    
    """
    param part:
    return:
    """    
    
    lip_parts =[reversed(sorted(getLipParts()['L_{}'.format(part)].keys())), getLipParts()['C_{}'.format(part)].keys(),
                sorted(getLipParts()['R_{}'.format(part)].keys())]
    
    return [joint for joint in lip_parts for joint in joint]


def createSeal(part):
    """
    param part:
    return:

  
    """
    
    seal_name = '{}_seal_{}'.format(CENTER, GROUP)
    seal_parent = seal_name if mc.objExists(seal_name) else \
        mc.createNode('transform', name=seal_name, parent='{}_{}_rig_{}'.format(CENTER, JAW, GROUP))
    
    part_grp = mc.createNode('transform', name=seal_name.replace('seal', 'seal_{}'.format(part)), parent=seal_parent)
    
    
    l_corner = '{}_{}_broadCorner_{}'.format(LEFT, JAW, JOINT)
    r_corner = '{}_{}_broadCorner_{}'.format(RIGHT, JAW, JOINT)
    
    value = len(lipPart(part))
    
    for index, joint in enumerate(lipPart(part)):
        node = mc.createNode('transform', name =joint.replace('JNT', '{}_SEAL'.format(part)), parent=part_grp)
        mat = mc.xform(joint, q=True, m=True, ws=True)
        mc.xform(node, m=mat, ws=True)
        
        constraint = mc.parentConstraint(l_corner, r_corner, node, mo=True)[0]
        mc.setAttr('{}.interpType'.format(constraint), 2)
        
        r_corner_value = float(index) / float(value - 1)
        l_corner_value = 1 - r_corner_value
        
        l_corner_attr = '{}.{}W0'.format(constraint, l_corner)
        r_corner_attr = '{}.{}W1'.format(constraint, r_corner)
        
        mc.setAttr(l_corner_attr, l_corner_value)
        mc.setAttr(r_corner_attr, r_corner_value)
        
    mc.select(cl=True)
    
    
def createJawAttrs():
    """
    return:
    
    """
    
    node = mc.createNode('transform', name='jaw_attributes', parent='{}_{}_rig_{}'.format(CENTER, JAW, GROUP))
    mc.addAttr(node, ln=sorted(getLipParts()['C_upper'].keys())[0], min=0, max=1, dv=0)
    mc.setAttr('{}.{}'.format(node, sorted(getLipParts()['C_upper'].keys())[0]), lock=1)
        
    for upper in sorted(getLipParts()['L_upper'].keys()):
        mc.addAttr(node, ln=upper, min=0, max=1, dv=0)
        
    mc.addAttr(node, ln=sorted(getLipParts()['L_corner'].keys())[0], min=0, max=1, dv=1)
    mc.setAttr('{}.{}'.format(node, sorted(getLipParts()['L_corner'].keys())[0]), lock=1)
    
    for lower in sorted(getLipParts()['L_lower'].keys())[::-1]:
        mc.addAttr(node, ln=lower, min=0, max=1, dv=0)
        
    mc.addAttr(node, ln=sorted(getLipParts()['C_lower'].keys())[0], min=0, max=1, dv=0)
    mc.setAttr('{}.{}'.format(node, sorted(getLipParts()['C_lower'].keys())[0]), lock=1)
    
    
def createConstraints():
    """
    return:
    
    """
    
    for value in getLipParts().values():
        for lip_jnt, broad_jnt in value.items():
            
            seal_token = 'upper_SEAL' if 'Upper' in lip_jnt else 'lower_SEAL'
            lip_seal = lip_jnt.replace(JOINT, seal_token)
            
            if mc.objExists(lip_seal):
                const = mc.parentConstraint(broad_jnt, lip_seal, lip_jnt, mo=True)[0]
                mc.setAttr('{}.interpType'.format(const), 2)
                
            else:
                const = mc.parentConstraint(broad_jnt, lip_jnt, mo=True)[0]
                mc.setAttr('{}.interpType'.format(const), 2)
                
                
    
    
    
    