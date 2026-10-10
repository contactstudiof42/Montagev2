"""Pièce 34. blender -b -P scene.py -- SORTIE.png vue(ext|int) [lampe] [phares]"""
import bpy, sys, math
a = sys.argv[sys.argv.index('--') + 1:]; OUT, VUE = a[:2]; LAMPE = 'lampe' in a; PHARES = 'phares' in a; BUEE = 'buee' in a
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = 'CYCLES'; sc.cycles.samples = 48; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = (1280, 540) if 'hd' in a else (640, 270); sc.view_settings.view_transform = 'AgX'
w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True; w.node_tree.nodes['Background'].inputs[0].default_value = (0.004, 0.005, 0.008, 1)
def mat(nom, col, rough=0.8, em=None, ems=0):
    m = bpy.data.materials.new(nom); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*col, 1); b.inputs['Roughness'].default_value = rough
    if em: b.inputs['Emission Color'].default_value = (*em, 1); b.inputs['Emission Strength'].default_value = ems
    return m
def boite(nom, loc, dim, m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.name = nom; o.scale = [d / 2 for d in dim]; o.data.materials.append(m); return o
boite('sol', (0, 0, -0.05), (80, 80, 0.1), mat('sol', (0.08, 0.08, 0.085), 0.6))
for i in range(-3, 4):                                         # lignes de places
    boite(f'ligne{i}', (i * 2.6 + 1.3, 1.0, 0.002), (0.08, 5.0, 0.004), mat('l', (0.5, 0.5, 0.5)))
# hôpital au fond : façade et fenêtres éclairées
boite('hopital', (0, 60, 8), (60, 2, 16), mat('h', (0.15, 0.15, 0.16)))
fen = mat('fen', (0.9, 0.95, 1.0), 0.3, (0.75, 0.85, 1.0), 0.6)
for r in range(5):
    for c in range(-11, 12):
        if (r * 13 + c * 7 + r * c) % 4 == 1:                                # quelques fenêtres éteintes
            boite(f'f{r}_{c}', (c * 2.6, 58.95, 2 + r * 2.8), (1.1, 0.05, 1.2), fen)
# voiture (berline simplifiée) garée face au fond, vue de 3/4 arrière depuis la caméra extérieure
carro = mat('carro', (0.05, 0.06, 0.07), 0.25); vitre = mat('vitre', (0.6, 0.65, 0.7), 0.05); vitre.node_tree.nodes['Principled BSDF'].inputs['Transmission Weight'].default_value = 0.85
if BUEE:                                                        # vitres embuées : diffusion, on ne voit plus que des taches
    bv = vitre.node_tree.nodes['Principled BSDF']; bv.inputs['Roughness'].default_value = 0.55; bv.inputs['Base Color'].default_value = (0.75, 0.78, 0.8, 1)
boite('caisse', (0, 0, 0.65), (1.8, 4.5, 0.75), carro)
boite('habitacle', (0, -0.2, 1.3), (1.62, 2.4, 0.56), vitre)
boite('toit', (0, -0.2, 1.62), (1.5, 2.0, 0.06), carro)
for x in (-0.9, 0.9):
    for y in (-1.4, 1.4):
        bpy.ops.mesh.primitive_cylinder_add(radius=0.33, depth=0.25, location=(x, y, 0.33), rotation=(0, math.pi / 2, 0)); bpy.context.object.data.materials.append(mat('roue', (0.02, 0.02, 0.02)))
boite('feuG', (-0.7, -2.26, 0.85), (0.3, 0.03, 0.1), mat('feu', (0.3, 0.02, 0.02), 0.3)); boite('feuD', (0.7, -2.26, 0.85), (0.3, 0.03, 0.1), mat('feu2', (0.3, 0.02, 0.02), 0.3))
# deux têtes dans l'habitacle (Nadia conductrice à gauche, Karim passager à droite)
peau = mat('peau', (0.45, 0.32, 0.26), 0.6); cheveux = mat('ch', (0.03, 0.025, 0.02), 0.7)
for nom, x, z in (('nadia', -0.4, 1.32), ('karim', 0.4, 1.28)):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(x, 0.0, z)); t = bpy.context.object; t.name = nom; t.scale = (0.85, 1, 1.15); t.data.materials.append(peau)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=0.5, location=(x, 0.05, z - 0.4)); bpy.context.object.data.materials.append(mat('veste' + nom, (0.1, 0.1, 0.12) if nom == 'karim' else (0.25, 0.08, 0.06)))
boite('tableau', (0, 0.75, 1.0), (1.6, 0.4, 0.2), mat('tb', (0.03, 0.03, 0.03)))
boite('ticket', (0.32, 0.25, 1.05), (0.06, 0.09, 0.005), mat('tk', (0.85, 0.83, 0.7), 0.5))   # dans la main de Karim
# lampadaire LED blanc à droite, devant
boite('mat', (3.2, 1.5, 3.0), (0.12, 0.12, 6.0), mat('m', (0.1, 0.1, 0.1)))
boite('bras', (2.6, 1.5, 6.0), (1.3, 0.12, 0.1), mat('m2', (0.1, 0.1, 0.1)))
boite('led', (2.1, 1.5, 5.93), (0.5, 0.25, 0.03), mat('led', (1, 1, 1), 0.2, (0.9, 0.95, 1.0), 60))
bpy.ops.object.light_add(type='SPOT', location=(2.1, 1.5, 5.9)); s = bpy.context.object; s.data.energy = 2600; s.data.color = (0.85, 0.92, 1.0)
s.data.spot_size = 1.9; s.data.spot_blend = 0.6; s.data.shadow_soft_size = 0.2
if LAMPE:                                                       # liseuse : chaude, petite, dans l'habitacle
    bpy.ops.object.light_add(type='POINT', location=(0.2, 0.1, 1.55)); l = bpy.context.object; l.data.energy = 12; l.data.color = (1.0, 0.7, 0.4); l.data.shadow_soft_size = 0.05
if PHARES:                                                      # une voiture qui passe derrière la caméra : nappe qui balaie
    bpy.ops.object.light_add(type='SPOT', location=(-6, -9, 0.8)); p = bpy.context.object; p.data.energy = 2500; p.data.color = (1.0, 0.95, 0.85)
    p.data.spot_size = 0.35; p.data.spot_blend = 0.5; p.rotation_euler = (math.radians(88), 0, math.radians(-30))
if VUE == 'ext':
    bpy.ops.object.camera_add(location=(-7.0, -16.0, 1.7)); cam = bpy.context.object; cam.data.lens = 45
    cam.rotation_euler = (math.radians(94), 0, math.radians(-20))
else:                                                           # dedans : Karim de 3/4 face depuis le pare-brise côté conducteur
    bpy.ops.object.camera_add(location=(0.12, 0.9, 1.34)); cam = bpy.context.object; cam.data.lens = 32
    cam.rotation_euler = (math.radians(88), 0, math.radians(196))
    bpy.ops.object.light_add(type='AREA', location=(1.6, 0.3, 1.8)); f = bpy.context.object; f.data.energy = 20; f.data.size = 0.5; f.data.color = (0.8, 0.9, 1.0)
    f.rotation_euler = (0, math.radians(-70), 0)
sc.camera = cam; sc.render.filepath = OUT; bpy.ops.render.render(write_still=True)
