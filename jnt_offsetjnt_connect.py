#넙스컨트롤을 스킨이 잡힌 조인트와 연결 컨트롤러가 기능하게 함.

import maya.cmds as cmds
import pymel.core as pm



# 텍스트 필드에서 이름 가져오기
get_name = cmds.textField("nameOfTexFld1", query=True, text=True)
get_number = int(pm.radioButtonGrp('RBGrp1', q=1, select=1)) + 2

for number in range(1, get_number + 1):
    offsetjnt_name = 'R_' + get_name + '_offset_jnt_' + str(number)
    jnt_name = 'R_' + get_name + '_jnt_' + str(number)
    
    try:
        # 여기서 object_name을 사용하여 해당 오브젝트에 대한 작업 수행
        print offsetjnt_name, jnt_name
        
        if cmds.objExists(jnt_name):
            source_attr = offsetjnt_name + '.translate'
            target_attr = jnt_name + '.translate'
            
            # 소스와 대상 속성 연결
            cmds.connectAttr(source_attr, target_attr, force=True)
    except Exception as e:
        print("예외 발생: %s" % str(e))
        
for number in range(1, get_number + 1):
    offsetjnt_name = 'L_' + get_name + '_offset_jnt_' + str(number)
    jnt_name = 'L_' + get_name + '_jnt_' + str(number)
    
    try:
        # 여기서 object_name을 사용하여 해당 오브젝트에 대한 작업 수행
        print offsetjnt_name, jnt_name
        
        if cmds.objExists(jnt_name):
            source_attr = offsetjnt_name + '.translate'
            target_attr = jnt_name + '.translate'
            
            # 소스와 대상 속성 연결
            cmds.connectAttr(source_attr, target_attr, force=True)
    except Exception as e:
        print("예외 발생: %s" % str(e))
        
get_name = cmds.textField("nameOfTexFld2", query=True, text=True)
get_number = int(pm.radioButtonGrp('RBGrp2', q=1, select=1)) + 2

for number in range(1, get_number + 1):
    offsetjnt_name = 'R_' + get_name + '_offset_jnt_' + str(number)
    jnt_name = 'R_' + get_name + '_jnt_' + str(number)
    
    try:
        # 여기서 object_name을 사용하여 해당 오브젝트에 대한 작업 수행
        print offsetjnt_name, jnt_name
        
        if cmds.objExists(jnt_name):
            source_attr = offsetjnt_name + '.translate'
            target_attr = jnt_name + '.translate'
            
            # 소스와 대상 속성 연결
            cmds.connectAttr(source_attr, target_attr, force=True)
    except Exception as e:
        print("예외 발생: %s" % str(e))
        
for number in range(1, get_number + 1):
    offsetjnt_name = 'L_' + get_name + '_offset_jnt_' + str(number)
    jnt_name = 'L_' + get_name + '_jnt_' + str(number)
    
    try:
        # 여기서 object_name을 사용하여 해당 오브젝트에 대한 작업 수행
        print offsetjnt_name, jnt_name
        
        if cmds.objExists(jnt_name):
            source_attr = offsetjnt_name + '.translate'
            target_attr = jnt_name + '.translate'
            
            # 소스와 대상 속성 연결
            cmds.connectAttr(source_attr, target_attr, force=True)
    except Exception as e:
        print("예외 발생: %s" % str(e))
        
        
get_name = cmds.textField("nameOfTexFld3", query=True, text=True)
get_number = int(pm.radioButtonGrp('RBGrp3', q=1, select=1)) + 2

for number in range(1, get_number + 1):
    offsetjnt_name = 'R_' + get_name + '_offset_jnt_' + str(number)
    jnt_name = 'R_' + get_name + '_jnt_' + str(number)
    
    try:
        # 여기서 object_name을 사용하여 해당 오브젝트에 대한 작업 수행
        print offsetjnt_name, jnt_name
        
        if cmds.objExists(jnt_name):
            source_attr = offsetjnt_name + '.translate'
            target_attr = jnt_name + '.translate'
            
            # 소스와 대상 속성 연결
            cmds.connectAttr(source_attr, target_attr, force=True)
    except Exception as e:
        print("예외 발생: %s" % str(e))
        
for number in range(1, get_number + 1):
    offsetjnt_name = 'L_' + get_name + '_offset_jnt_' + str(number)
    jnt_name = 'L_' + get_name + '_jnt_' + str(number)
    
    try:
        # 여기서 object_name을 사용하여 해당 오브젝트에 대한 작업 수행
        print offsetjnt_name, jnt_name
        
        if cmds.objExists(jnt_name):
            source_attr = offsetjnt_name + '.translate'
            target_attr = jnt_name + '.translate'
            
            # 소스와 대상 속성 연결
            cmds.connectAttr(source_attr, target_attr, force=True)
    except Exception as e:
        print("예외 발생: %s" % str(e))
        
        
get_name = cmds.textField("nameOfTexFld4", query=True, text=True)
get_number = int(pm.radioButtonGrp('RBGrp4', q=1, select=1)) + 2

for number in range(1, get_number + 1):
    offsetjnt_name = 'R_' + get_name + '_offset_jnt_' + str(number)
    jnt_name = 'R_' + get_name + '_jnt_' + str(number)
    
    try:
        # 여기서 object_name을 사용하여 해당 오브젝트에 대한 작업 수행
        print offsetjnt_name, jnt_name
        
        if cmds.objExists(jnt_name):
            source_attr = offsetjnt_name + '.translate'
            target_attr = jnt_name + '.translate'
            
            # 소스와 대상 속성 연결
            cmds.connectAttr(source_attr, target_attr, force=True)
    except Exception as e:
        print("예외 발생: %s" % str(e))
        
for number in range(1, get_number + 1):
    offsetjnt_name = 'L_' + get_name + '_offset_jnt_' + str(number)
    jnt_name = 'L_' + get_name + '_jnt_' + str(number)
    
    try:
        # 여기서 object_name을 사용하여 해당 오브젝트에 대한 작업 수행
        print offsetjnt_name, jnt_name
        
        if cmds.objExists(jnt_name):
            source_attr = offsetjnt_name + '.translate'
            target_attr = jnt_name + '.translate'
            
            # 소스와 대상 속성 연결
            cmds.connectAttr(source_attr, target_attr, force=True)
    except Exception as e:
        print("예외 발생: %s" % str(e))









import maya.cmds as cmds
import pymel.core as pm



# 텍스트 필드에서 이름 가져오기
get_name = cmds.textField("nameOfTexFld1", query=True, text=True)
get_number = int(pm.radioButtonGrp('RBGrp1', q=1, select=1)) + 2

for number in range(1, get_number + 1):
    offsetjnt_name = 'R_' + get_name + '_offset_jnt_' + str(number)
    loc_name = 'R_' + get_name + '_loc_' + str(number)
    
    
    print offsetjnt_name, loc_name
    
    cmds.select(offsetjnt_name, r= True)
    cmds.select(loc_name, add= True)
    
    try:
        cmds.parent(offsetjnt_name, loc_name)
        cmds.parent(cl= True)
    except Exception as e:
        # 이미 부모-자식 관계가 설정되어 있을 때 에러를 무시하거나 처리
        pass



for number in range(1, get_number + 1):
    offsetjnt_name = 'L_' + get_name + '_offset_jnt_' + str(number)
    loc_name = 'L_' + get_name + '_loc_' + str(number)
    
    
    print offsetjnt_name, loc_name
    
    cmds.select(offsetjnt_name, r= True)
    cmds.select(loc_name, add= True)
    
    try:
        cmds.parent(offsetjnt_name, loc_name)
        cmds.parent(cl= True)
    except Exception as e:
        # 이미 부모-자식 관계가 설정되어 있을 때 에러를 무시하거나 처리
        pass
    


# 텍스트 필드에서 이름 가져오기
get_name = cmds.textField("nameOfTexFld2", query=True, text=True)
get_number = int(pm.radioButtonGrp('RBGrp2', q=1, select=1)) + 2

for number in range(1, get_number + 1):
    offsetjnt_name = 'R_' + get_name + '_offset_jnt_' + str(number)
    loc_name = 'R_' + get_name + '_loc_' + str(number)
    
    
    print offsetjnt_name, loc_name
    
    cmds.select(offsetjnt_name, r= True)
    cmds.select(loc_name, add= True)
    
    try:
        cmds.parent(offsetjnt_name, loc_name)
        cmds.parent(cl= True)
    except Exception as e:
        # 이미 부모-자식 관계가 설정되어 있을 때 에러를 무시하거나 처리
        pass



for number in range(1, get_number + 1):
    offsetjnt_name = 'L_' + get_name + '_offset_jnt_' + str(number)
    loc_name = 'L_' + get_name + '_loc_' + str(number)
    
    
    print offsetjnt_name, loc_name
    
    cmds.select(offsetjnt_name, r= True)
    cmds.select(loc_name, add= True)
    
    try:
        cmds.parent(offsetjnt_name, loc_name)
        cmds.parent(cl= True)
    except Exception as e:
        # 이미 부모-자식 관계가 설정되어 있을 때 에러를 무시하거나 처리
        pass


# 텍스트 필드에서 이름 가져오기
get_name = cmds.textField("nameOfTexFld3", query=True, text=True)
get_number = int(pm.radioButtonGrp('RBGrp3', q=1, select=1)) + 2

for number in range(1, get_number + 1):
    offsetjnt_name = 'R_' + get_name + '_offset_jnt_' + str(number)
    loc_name = 'R_' + get_name + '_loc_' + str(number)
    
    
    print offsetjnt_name, loc_name
    
    cmds.select(offsetjnt_name, r= True)
    cmds.select(loc_name, add= True)
    
    try:
        cmds.parent(offsetjnt_name, loc_name)
        cmds.parent(cl= True)
    except Exception as e:
        # 이미 부모-자식 관계가 설정되어 있을 때 에러를 무시하거나 처리
        pass



for number in range(1, get_number + 1):
    offsetjnt_name = 'L_' + get_name + '_offset_jnt_' + str(number)
    loc_name = 'L_' + get_name + '_loc_' + str(number)
    
    
    print offsetjnt_name, loc_name
    
    cmds.select(offsetjnt_name, r= True)
    cmds.select(loc_name, add= True)
    
    try:
        cmds.parent(offsetjnt_name, loc_name)
        cmds.parent(cl= True)
    except Exception as e:
        # 이미 부모-자식 관계가 설정되어 있을 때 에러를 무시하거나 처리
        pass


# 텍스트 필드에서 이름 가져오기
get_name = cmds.textField("nameOfTexFld4", query=True, text=True)
get_number = int(pm.radioButtonGrp('RBGrp4', q=1, select=1)) + 2

for number in range(1, get_number + 1):
    offsetjnt_name = 'R_' + get_name + '_offset_jnt_' + str(number)
    loc_name = 'R_' + get_name + '_loc_' + str(number)
    
    
    print offsetjnt_name, loc_name
    
    cmds.select(offsetjnt_name, r= True)
    cmds.select(loc_name, add= True)
    
    try:
        cmds.parent(offsetjnt_name, loc_name)
        cmds.parent(cl= True)
    except Exception as e:
        # 이미 부모-자식 관계가 설정되어 있을 때 에러를 무시하거나 처리
        pass



for number in range(1, get_number + 1):
    offsetjnt_name = 'L_' + get_name + '_offset_jnt_' + str(number)
    loc_name = 'L_' + get_name + '_loc_' + str(number)
    
    
    print offsetjnt_name, loc_name
    
    cmds.select(offsetjnt_name, r= True)
    cmds.select(loc_name, add= True)
    
    try:
        cmds.parent(offsetjnt_name, loc_name)
        cmds.parent(cl= True)
    except Exception as e:
        # 이미 부모-자식 관계가 설정되어 있을 때 에러를 무시하거나 처리
        pass
    