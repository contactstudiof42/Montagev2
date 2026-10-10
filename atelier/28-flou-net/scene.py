"""Pièce 28 « Flou → net » (Y31, examen n°12) : fenêtre de train au premier plan (0,4 m), champ et 3 chevaux stylisés à 30-60 m,
reflets de soleil (points brillants) pour voir le bokeh. Rend des images fixes à plusieurs distances de mise au point.
usage : blender -b -P scene.py -- OUTDIR f1,f2,... [--f 1.4] [--sharp]   (--sharp = sans profondeur de champ = plaque nette)"""
import bpy, sys, math
a = sys.argv[sys.argv.index('--')+1:]; out = a[0]; focs = [float(x) for x in a[1].split(',')]
REFLET = '--reflet' in a; ks = [float(x) for x in a[a.index('--reflet')+1].split(',')] if REFLET else [1]
fst = float(a[a.index('--f')+1]) if '--f' in a else 1.4; sharp = '--sharp' in a
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = 'CYCLES'; sc.cycles.samples = 24; sc.cycles.device = 'CPU'
sc.render.resolution_x, sc.render.resolution_y = 640, 360; sc.view_settings.view_transform = 'AgX'
w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True; w.node_tree.nodes['Background'].inputs[0].default_value = (0.75, 0.8, 0.9, 1); w.node_tree.nodes['Background'].inputs[1].default_value = 1.2
def mat(n, c, e=0):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*c, 1)
    if e: b.inputs['Emission Color'].default_value = (*c, 1); b.inputs['Emission Strength'].default_value = e
    return m
def boite(loc, dim, m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.scale = [d/2 for d in dim]; o.data.materials.append(m); return o
herbe, brun, cadre = mat('herbe', (0.18, 0.32, 0.08)), mat('brun', (0.25, 0.12, 0.05)), mat('cadre', (0.05, 0.05, 0.06))
boite((0, 60, -1.5), (400, 200, 0.2), herbe)                                  # sol (Y = profondeur)
for i, (x, y) in enumerate([(-6, 32), (1, 45), (9, 60)]):                     # chevaux : corps + 4 pattes + cou
    boite((x, y, 0.3), (2.2, 0.7, 0.9), brun)
    for dx in (-0.8, 0.8):
        for dy in (-0.2, 0.2): boite((x+dx, y+dy, -0.6), (0.18, 0.18, 1.2), brun)
    boite((x+1.2, y, 0.95), (0.5, 0.4, 1.0), brun)
for i in range(12):                                                           # reflets (eau, clôture) : petits points émissifs
    boite((-14+i*2.6, 38+(i % 3)*4, -1.0), (0.12, 0.12, 0.12), mat(f'r{i}', (1, 0.9, 0.7), 60))
boite((-0.125, 0.4, 0), (0.03, 0.02, 1), cadre); boite((0.15, 0.4, 0), (0.03, 0.02, 1), cadre)   # montants de fenêtre à 0,4 m
boite((0, 0.4, -0.06), (1, 0.02, 0.012), cadre)
bpy.ops.object.light_add(type='SUN', rotation=(math.radians(50), 0, math.radians(30))); bpy.context.object.data.energy = 3
bpy.ops.object.camera_add(location=(0, 0, 0), rotation=(math.radians(90), 0, 0)); cam = bpy.context.object; sc.camera = cam
cam.data.lens = 50; cam.data.dof.use_dof = not sharp; cam.data.dof.aperture_fstop = fst
if REFLET:   # v3 : vitre réelle, visage éclairé à côté de la caméra ; on assombrit l'extérieur (pont, forêt)
    bpy.ops.mesh.primitive_plane_add(size=2, location=(0, 0.4, 0), rotation=(math.radians(90), 0, 0)); g = bpy.context.object
    gm = bpy.data.materials.new('verre'); gm.use_nodes = True; gb = gm.node_tree.nodes['Principled BSDF']
    gb.inputs['Transmission Weight'].default_value = 1; gb.inputs['Roughness'].default_value = 0; gb.inputs['IOR'].default_value = 1.5; g.data.materials.append(gm)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.07, location=(0.11, 0.0, 0.0)); bpy.context.object.data.materials.append(mat('peau', (0.8, 0.55, 0.42)))
    bpy.ops.object.light_add(type='POINT', location=(0.02, 0.2, 0.1)); bpy.context.object.data.energy = 3   # le visage est éclairé côté vitre (lumière du compartiment)
    sun = [o for o in bpy.data.objects if o.type == 'LIGHT' and o.data.type == 'SUN'][0]
    cam.data.dof.use_dof = False
    for k in ks:
        w.node_tree.nodes['Background'].inputs[1].default_value = 1.2*k; sun.data.energy = 3*k
        sc.render.filepath = f"{out}/reflet_{k:g}.png"; bpy.ops.render.render(write_still=True)
    focs = []
for f in focs:
    cam.data.dof.focus_distance = f
    sc.render.filepath = f"{out}/{'net' if sharp else f'foc_{f:g}'}.png"; bpy.ops.render.render(write_still=True)
    if sharp: break
