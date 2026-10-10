"""Pièce 31. blender -b -P scene.py -- SORTIE.png lumiere(froid|chaud) camera(haute|basse) corps(voute|ouvert)"""
import bpy, sys, math
a = sys.argv[sys.argv.index('--') + 1:]; OUT, LUM, CAM, CORPS = a[:4]; V2 = 'v2' in a   # v2 : soleil rasant de côté, caméra basse à 0,9 m
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = 'CYCLES'; sc.cycles.samples = 32; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 480, 270; sc.view_settings.view_transform = 'AgX'
def boite(nom, loc, dim, col, rough=0.8):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.name = nom; o.scale = [d / 2 for d in dim]
    m = bpy.data.materials.new(nom); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*col, 1); b.inputs['Roughness'].default_value = rough; o.data.materials.append(m); return o
# escalier : 14 marches montant vers +Y
for i in range(14):
    boite(f'marche{i}', (0, i * 0.35, i * 0.18 + 0.09), (3.0, 0.35, 0.18 + i * 0.36 * 0), (0.42, 0.40, 0.38))
    boite(f'contre{i}', (0, i * 0.35 + 0.175, i * 0.09), (3.0, 0.02, i * 0.18 + 0.18), (0.42, 0.40, 0.38))
boite('palier_bas', (0, -2.5, -0.05), (8, 5, 0.1), (0.35, 0.34, 0.33))
boite('palier_haut', (0, 4.9 + 2.5, 2.52 - 0.05), (8, 5, 0.1), (0.35, 0.34, 0.33))
boite('mur_g', (-1.8, 2.5, 2.5), (0.6, 14, 5), (0.55, 0.45, 0.38)); boite('mur_d', (1.8, 2.5, 2.5), (0.6, 14, 5), (0.50, 0.44, 0.40))
for k in range(5):                                   # fenêtres du mur droit (repères pour reconnaître le lieu)
    boite(f'fen{k}', (1.49, -1 + k * 1.8, 2.6 + (k % 2) * 0.8), (0.02, 0.6, 0.9), (0.08, 0.09, 0.1), 0.2)
boite('rampe', (-1.2, 2.4, 1.3), (0.06, 6.0, 0.06), (0.1, 0.1, 0.1), 0.4).rotation_euler[0] = math.atan2(0.18, 0.35)
# réverbère
boite('mat', (1.2, 0.6, 2.0), (0.08, 0.08, 4.0), (0.05, 0.05, 0.05)); boite('tete', (1.0, 0.6, 3.95), (0.5, 0.18, 0.12), (0.05, 0.05, 0.05))
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.09, location=(0.85, 0.6, 3.85)); ampoule = bpy.context.object
me = bpy.data.materials.new('ampoule'); me.use_nodes = True; em = me.node_tree.nodes['Principled BSDF']
em.inputs['Emission Color'].default_value = (1.0, 0.55, 0.18, 1); em.inputs['Emission Strength'].default_value = 40; ampoule.data.materials.append(me)
# silhouette (mi-escalier, marche 7)
y0, z0 = 7 * 0.35, 7 * 0.18 + 0.18
peau = (0.6, 0.45, 0.38); veste = (0.45, 0.12, 0.08) if CORPS == 'ouvert' else (0.25, 0.22, 0.2)
penche = 0.45 if CORPS == 'voute' else -0.08
bpy.ops.mesh.primitive_cylinder_add(radius=0.07, depth=0.85, location=(0.1, y0, z0 + 0.42)); jambes = bpy.context.object
bpy.ops.mesh.primitive_cylinder_add(radius=0.19, depth=0.7, location=(0.1, y0 + 0.3 * math.sin(penche) * 0, z0 + 1.15)); buste = bpy.context.object
buste.rotation_euler[0] = -penche
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.13, location=(0.1, y0 - 0.33 * math.sin(penche) * -1, z0 + 1.5 + 0.06 * math.cos(penche) - 0.15 * (penche > 0.2)))
tete = bpy.context.object
for o, c in ((jambes, (0.08, 0.08, 0.1)), (buste, veste), (tete, peau)):
    m = bpy.data.materials.new(o.name); m.use_nodes = True; m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (*c, 1); o.data.materials.append(m)
for s in (-1, 1):                                    # bras
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.62); br = bpy.context.object
    if CORPS == 'ouvert':
        br.location = (0.1 + s * 0.42, y0, z0 + 1.42); br.rotation_euler = (0, s * 1.1, 0)
    else:
        br.location = (0.1 + s * 0.22, y0 - 0.12, z0 + 0.98); br.rotation_euler = (-0.35, 0, 0)
    br.data.materials.append(buste.data.materials[0])
# monde et lumières
w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True; bg = w.node_tree.nodes['Background']
if LUM == 'froid':
    bg.inputs['Color'].default_value = (0.10, 0.16, 0.30, 1); bg.inputs['Strength'].default_value = 1.2
    bpy.ops.object.light_add(type='AREA', location=(0, -6, 4)); l = bpy.context.object; l.data.energy = 300; l.data.size = 4
    l.data.color = (0.6, 0.75, 1.0); l.rotation_euler = (math.radians(62), 0, 0)
    em.inputs['Emission Strength'].default_value = 8
else:
    bg.inputs['Color'].default_value = (0.25, 0.14, 0.07, 1); bg.inputs['Strength'].default_value = 0.6
    bpy.ops.object.light_add(type='SUN', location=(0, 10, 4)); l = bpy.context.object; l.data.energy = 6; l.data.angle = math.radians(2)
    l.data.color = (1.0, 0.55, 0.22); l.rotation_euler = (math.radians(-80), 0, 0)   # soleil bas derrière le haut des marches
    if V2:                                           # rasant et de biais : chaque nez de marche accroche un trait de lumière
        l.rotation_euler = (math.radians(-76), 0, math.radians(28)); l.data.energy = 9; bg.inputs['Strength'].default_value = 1.0
    em.inputs['Emission Strength'].default_value = 0
# caméra
bpy.ops.object.camera_add(); cam = bpy.context.object; sc.camera = cam; cam.data.lens = 28
if CAM == 'haute':
    cam.location = (0.4, -3.2, 5.2); cible = (0.1, y0, z0 + 0.6)
else:
    cam.location = (0.3, -1.6, 0.35); cible = (0.1, y0 + 1.2, z0 + 1.5)
    if V2:
        cam.location = (0.6, -2.4, 0.9); cible = (0.1, y0 + 0.6, z0 + 1.1)
import mathutils
d = mathutils.Vector(cible) - cam.location; cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
sc.render.filepath = OUT; bpy.ops.render.render(write_still=True)
