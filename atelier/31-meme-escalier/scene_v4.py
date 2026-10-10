"""Pièce 31 v4 (figure articulée ; azimut caméra : arg « az=DEG » autour de la figure). blender -b -P scene.py -- SORTIE.png lumiere(froid|chaud) camera(haute|basse) corps(voute|ouvert)"""
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
# figure articulée (v4) : chaîne de capsules par cinématique directe ; poses « voute » (aller) et « ouvert » (retour)
import mathutils
y0, z0 = 7 * 0.35, 7 * 0.18 + 0.18
peau = (0.6, 0.45, 0.38); veste = (0.45, 0.12, 0.08) if CORPS == 'ouvert' else (0.25, 0.22, 0.2)
def M(c):
    m = bpy.data.materials.new('m'); m.use_nodes = True; m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (*c, 1); return m
mv, mp, mj = M(veste), M(peau), M((0.08, 0.08, 0.1))
def os_(p, q, r, m):                                  # capsule de p à q
    p, q = mathutils.Vector(p), mathutils.Vector(q); d = q - p
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=d.length, location=(p + q) / 2); o = bpy.context.object
    o.rotation_euler = d.to_track_quat('Z', 'Y').to_euler(); o.data.materials.append(m)
    for e in (p, q): bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=e); bpy.context.object.data.materials.append(m)
def pt(o, ang, L):                                   # ang : inclinaison dans le plan sagittal (0 = vertical haut, + = vers l'avant -Y... ici vers +Y, sens de la montée)
    return (o[0], o[1] + L * math.sin(ang), o[2] + L * math.cos(ang))
R = math.radians
if CORPS == 'voute':   P = dict(dos=R(38), cou=R(70), bras=R(170), avbras=R(160), cuisseA=R(150), tibiaA=R(180), cuisseB=R(185), tibiaB=R(185), ecart=0.16)
else:                  P = dict(dos=R(-12), cou=R(-25), bras=R(-35), avbras=R(-20), cuisseA=R(140), tibiaA=R(200), cuisseB=R(178), tibiaB=R(182), ecart=0.55)
bassin = (0.1, y0, z0 + 0.92)
for s, (c, t) in ((-1, ('cuisseA', 'tibiaA')), (1, ('cuisseB', 'tibiaB'))):
    h = (bassin[0] + s * 0.11, bassin[1], bassin[2]); g = pt(h, P[c], 0.46); pied = pt(g, P[t], 0.46)
    os_(h, g, 0.075, mj); os_(g, pied, 0.065, mj)
epaule = pt(bassin, P['dos'], 0.58); os_(bassin, epaule, 0.17, mv)
tete = pt(epaule, P['cou'], 0.22); os_(epaule, tete, 0.05, mp)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=pt(epaule, P['cou'], 0.32)); bpy.context.object.data.materials.append(mp)
for s in (-1, 1):
    e = (epaule[0] + s * 0.21, epaule[1], epaule[2] - 0.03)
    if CORPS == 'voute':
        c = pt(e, P['bras'], 0.32); m_ = pt(c, P['avbras'], 0.3)
    else:                                            # bras ouverts sur le côté et vers le haut (danse)
        c = (e[0] + s * 0.28, e[1] - 0.05, e[2] + 0.12); m_ = (c[0] + s * 0.22, c[1] - 0.05, c[2] + 0.22)
    os_(e, c, 0.055, mv); os_(c, m_, 0.05, mv)
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
AZ = [float(x[3:]) for x in a if x.startswith('az=')]
if 'murfou' in a:                                    # « mur volant » de studio : le mur droit reste dans la lumière et les reflets, invisible pour la caméra
    o = bpy.data.objects['mur_d']; o.visible_camera = False
    for k in range(5): bpy.data.objects[f'fen{k}'].visible_camera = False
if AZ:                                               # v4 : même distance, caméra tournée autour de la figure (0 = face, 90 = profil)
    r = 3.0; th = math.radians(AZ[0]); cam.location = (0.1 + r * math.sin(th), y0 - r * math.cos(th), z0 + (2.2 if CAM == 'haute' else 0.5)); cible = (0.1, y0, z0 + 1.0)
d = mathutils.Vector(cible) - cam.location; cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
if 'grue' in a:                                     # v3 : retour en grue montante (0,9 m → 2,8 m), 75 images, cadre qui suit la silhouette
    sc.render.resolution_x, sc.render.resolution_y = 320, 180; sc.cycles.samples = 12
    sc.frame_start, sc.frame_end = 1, 75; sc.render.fps = 25
    vise = bpy.data.objects.new('vise', None); sc.collection.objects.link(vise); vise.location = cible
    tr = cam.constraints.new('TRACK_TO'); tr.target = vise; tr.track_axis = 'TRACK_NEGATIVE_Z'; tr.up_axis = 'UP_Y'
    for f, loc in ((1, (0.6, -2.4, 0.9)), (75, (0.2, -0.6, 2.8))):
        cam.location = loc; cam.keyframe_insert('location', frame=f)
    for fc in cam.animation_data.action.fcurves:
        for k in fc.keyframe_points: k.interpolation = 'SINE'; k.easing = 'EASE_IN_OUT'
    sc.render.filepath = OUT; bpy.ops.render.render(animation=True)
else:
    sc.render.filepath = OUT; bpy.ops.render.render(write_still=True)
