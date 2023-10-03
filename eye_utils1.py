from maya import cmds, openMaya
import maya.cmds as cmds


center = "center"
vtx = cmds.ls(sl = 1, fl =1)

for v in vtx :
    cmds.select(cl =1)
    jnt = cmds.joint()
    pos = cmds.xform(v, q=1, ws=1, t= 1)
    cmds.xform(jnt, ws =1, t = pos)
    posC = cmds.xform(center, q=1, ws=1, t=1)
    cmds.select(cl =1)
    jntC = cmds.joint()
    cmds.xform(jntC, ws =1, t=posC)
    cmds.parent(jnt, jntC)
    
    cmds.joint(jntC, e =1, oj ="xyz", secondaryAxisOrient= "yup")
    
    
    
    sel = cmds.ls(sl=1)
    
    for s in sel :
        loc = cmds.spaceLocator()[0]
        pos = cmds.xform(s, q = 1, ws = 1, t = 1)
        cmds.xform(loc, ws = 1, t =pos)
        par = cmds.listRelatives(s, p = 1)[0]
        
        cmds.aimConstraint(loc,par, mo = 1, weight = 1, aimVector = (1, 0, 0), upVector = (0, 1, 0), worldUpType = "object", worldupObjec)
    
    
    
from maya import cmds, openMaya

sel = cmds.ls(sl=1)
crv = "curveShape1"
for s in sel :
    pos = cmds.xform(s, q = 1, ws =1, t =1)
    u = getUParam(pos, crv)
    name = s.replace("_LOC", "_PCI")
    pci = cmds.createNode("pointOnCurveInfo", n = name)
    cmds.connectAttr(crv + '.worldSpace', pci + '.infputCurve')
    cmds.setAttr(pci + '.parameter', u)
    cmds.connectAttr(pci + '.position', s + '.t')




    
    
import maya.cmds as mc

sel = mc.ls(sl=1)
crv = 'lid_L_topHigh_crv00Shape'
for loc in sel:

npc = mc.createNode('nearestPointOnCurve',n=loc.replace('loc','npc'))
mc.connectAttr(crv+'.worldSpace',npc+'.inputCurve')
mc.connectAttr(loc+'.t',npc+'.inPosition')
u = mc.getAttr(npc+'.parameter')
mc.delete(npc)
pci = mc.createNode('pointOnCurveInfo',n=loc.replace('loc','pci'))
mc.connectAttr(crv+'.worldSpace',pci+'.inputCurve')
mc.connectAttr(pci+'.position',loc+'.t')
mc.setAttr(pci+'.parameter',u)