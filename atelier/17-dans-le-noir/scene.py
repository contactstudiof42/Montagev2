"""Pièce 17 : blender -b -P scene.py -- sortie_dossier/ temp(froid|chaud) pos(bas|cote) [cam(face|cote)]"""
import bpy, sys, math, mathutils, os
a = sys.argv[sys.argv.index("--") + 1:]; out, temp, pos = a[0], a[1], a[2]; camv = a[3] if len(a) > 3 else "face"
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 12; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 384, 216; sc.view_settings.view_transform = "AgX"; sc.render.fps = 12
sc.frame_start, sc.frame_end = 1, 120; sc.render.filepath = out + "f_"; sc.render.image_settings.file_format = "PNG"
sc.frame_step = int(__import__("os").environ.get("STEP", "1")); sc.render.use_overwrite = False   # STEP=2 : une image sur deux (aperçu)
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes["Background"].inputs[1].default_value = 0   # aucune autre lumière
def mat(n, c, r=0.7):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*c, 1); b.inputs["Roughness"].default_value = r; return m
def boite(loc, dim, m, parent=None):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.scale = [d / 2 for d in dim]; o.data.materials.append(m)
    if parent: o.parent = parent
    return o
tissu = mat("fauteuil", (0.25, 0.2, 0.18), 0.9); peau = mat("peau", (0.55, 0.4, 0.33), 0.6); pyj = mat("pyjama", (0.3, 0.32, 0.38), 0.9)
creme = mat("couverture", (0.85, 0.8, 0.7), 0.95)
boite((0, 0, -0.01), (8, 8, 0.02), mat("sol", (0.15, 0.13, 0.12)))
boite((0, 1.2, 1.5), (8, 0.02, 3), mat("mur", (0.4, 0.38, 0.36), 0.9))
# fauteuil
boite((0, 0.3, 0.25), (0.9, 0.8, 0.5), tissu); boite((0, 0.65, 0.75), (0.9, 0.15, 1.0), tissu)
for sx in (-0.5, 0.5): boite((sx, 0.3, 0.6), (0.15, 0.8, 0.3), tissu)
# parent + bébé dans un groupe qui se berce (pivot au bassin)
bpy.ops.object.empty_add(location=(0, 0.3, 0.5)); g = bpy.context.object
def enfant(o): o.parent = g; o.matrix_parent_inverse = g.matrix_world.inverted()
bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=0.6, location=(0, 0.35, 0.82)); enfant(bpy.context.object); bpy.context.object.data.materials.append(pyj)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(0, 0.3, 1.25)); h = bpy.context.object; enfant(h); h.data.materials.append(peau)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.16, location=(0.05, 0.05, 0.85)); b = bpy.context.object; b.scale = (1.4, 0.8, 0.8); enfant(b); b.data.materials.append(creme)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.075, location=(0.2, -0.02, 0.92)); enfant(bpy.context.object); bpy.context.object.data.materials.append(peau)  # tête du bébé
# bras qui portent le bébé (v3) : de l'épaule au-dessous de la couverture, puis l'avant-bras qui l'enveloppe
def membre(p0, p1, r=0.045):
    p0, p1 = mathutils.Vector(p0), mathutils.Vector(p1); v = p1 - p0
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=v.length, location=(p0 + p1) / 2); o = bpy.context.object
    o.rotation_euler = v.to_track_quat("Z", "Y").to_euler(); o.data.materials.append(pyj); enfant(o)
membre((-0.2, 0.32, 1.05), (-0.22, 0.05, 0.8)); membre((-0.22, 0.05, 0.8), (0.22, -0.08, 0.78))     # bras gauche sous le bébé
membre((0.2, 0.32, 1.05), (0.24, 0.0, 0.9)); membre((0.24, 0.0, 0.9), (-0.05, -0.12, 0.95))        # bras droit qui l'entoure
# le téléphone
if pos == "bas":   # tenu sous le visage, écran vers le haut-visage
    ploc, prot = (0.05, 0.0, 1.0), (math.radians(-60), 0, 0)
elif pos == "main":   # v3 : tenu bas, devant les genoux, écran incliné vers la couverture et le visage (lumière basse de côté)
    ploc, prot = (0.3, -0.22, 0.72), (math.radians(-40), 0, math.radians(25))
else:              # posé sur l'accoudoir, écran vers la couverture
    ploc, prot = (0.5, 0.05, 0.77), (math.radians(-20), 0, math.radians(50))
bpy.ops.object.empty_add(location=ploc); rig = bpy.context.object; rig.rotation_euler = prot   # repère du téléphone (non mis à l'échelle)
def au_rig(o, loc): o.parent = rig; o.matrix_parent_inverse.identity(); o.location = loc
ph = boite((0, 0, 0), (0.07, 0.14, 0.008), mat("coque", (0.02, 0.02, 0.02), 0.3)); au_rig(ph, (0, 0, 0))
col = (0.55, 0.7, 1.0) if temp == "froid" else (1.0, 0.72, 0.45)
em = bpy.data.materials.new("ecran"); em.use_nodes = True; nt = em.node_tree; bs = nt.nodes["Principled BSDF"]
bs.inputs["Base Color"].default_value = (0, 0, 0, 1); bs.inputs["Emission Color"].default_value = (*col, 1)
scr = boite((0, 0, 0), (0.062, 0.13, 0.002), em); au_rig(scr, (0, 0, 0.005))
bpy.ops.object.light_add(type="AREA"); L = bpy.context.object; au_rig(L, (0, 0, 0.02)); L.data.size = 0.13; L.data.color = col
L.rotation_euler = (math.radians(180), 0, 0)   # la zone éclaire du côté de l'écran (+Z local)
sc.view_settings.exposure = float(__import__("os").environ.get("EXPO", "1.5"))
# animation : noir 0-3 s, l'écran s'allume en 0,5 s, bercement qui ralentit après
for f in range(1, 121):
    t = (f - 1) / 12
    on = 0 if t < 3 else min(1, (t - 3) / 0.5)
    bs.inputs["Emission Strength"].default_value = 0.02 + 6 * on; bs.inputs["Emission Strength"].keyframe_insert("default_value", frame=f)
    L.data.energy = 0.1 + float(os.environ.get("ENER", "15")) * on; L.data.keyframe_insert("energy", frame=f)
    k = min(1, max(0, (t - 3.5) / 4)); amp = 5.0 - 3.8 * k
    if os.environ.get("NAIF"):   # v1-v2 : sin(2πt/P(t)) — faux : le bercement se fige vers 4-6 s puis repart (labo/ae-expressions/bercement)
        ph = t / (1.6 + 1.6 * k)
    else:                        # v3+ : phase intégrée ∫dt/P, P de 1,6 à 3,2 s en 4 s après l'allumage
        aa = 1.6 / 4; ph = (t / 1.6) if t <= 3.5 else 3.5 / 1.6 + math.log((1.6 + aa * min(t - 3.5, 4)) / 1.6) / aa + max(0, t - 7.5) / 3.2
    g.rotation_euler = (0, math.radians(amp * math.sin(2 * math.pi * ph)), 0); g.keyframe_insert("rotation_euler", frame=f)
    h.rotation_euler = (0, 0, math.radians(25 * on) if pos != "bas" else 0); h.keyframe_insert("rotation_euler", frame=f)   # la tête se tourne vers l'écran
cam_loc, cible = ((0.0, -2.8, 1.15), (0, 0.3, 0.9)) if camv == "face" else ((1.9, -2.0, 1.1), (0.1, 0.3, 0.85))
bpy.ops.object.camera_add(location=cam_loc); c = bpy.context.object; c.data.lens = 40
c.rotation_euler = (mathutils.Vector(cible) - mathutils.Vector(cam_loc)).to_track_quat("-Z", "Y").to_euler(); sc.camera = c
import os
if os.environ.get("UNE"): sc.frame_set(int(os.environ["UNE"])); sc.render.filepath = out + "une.png"; bpy.ops.render.render(write_still=True)
else: bpy.ops.render.render(animation=True)
