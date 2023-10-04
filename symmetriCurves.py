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

