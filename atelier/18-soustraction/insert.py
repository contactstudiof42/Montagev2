"""Pièce 18 v6 : insert de l'interrupteur (la cause). blender -b -P insert.py -- <dossier> <sens>
sens = "presse" : un index entre dans le cadre, appuie, la bascule passe de haut (allumé) à bas à l'image 14 ;
sens = "lache"  : la bascule est déjà en bas, l'index posé dessus se retire (on découvre le geste après coup).
Plaque d'interrupteur sur un mur sombre, éclairée par l'ambre basse du personnage (même source que la rue) ;
16 images, Cycles, 640×360, PNG vue AgX."""
import bpy, sys, math, os
a = sys.argv[sys.argv.index("--") + 1:]; out, sens = a[0], a[1]
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = int(os.environ.get("SPP", "24")); sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 640, 360; sc.view_settings.view_transform = "AgX"
sc.frame_start, sc.frame_end = 1, 16; sc.render.fps = 25
sc.render.filepath = f"{out}/{sens}{'_nuit' if os.environ.get('NUIT') else ''}_"; sc.render.image_settings.file_format = "PNG"
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.02, 0.025, 0.04, 1); w.node_tree.nodes["Background"].inputs[1].default_value = 0.05
def mat(n, c, r=0.6):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*c, 1); b.inputs["Roughness"].default_value = r; return m
def boite(loc, dim, m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.scale = [d / 2 for d in dim]; o.data.materials.append(m); return o
# mur (plan x-z, face vers -y), plaque, bascule (pivote autour de l'axe x)
boite((0, 0.05, 0), (2, 0.1, 1.2), mat("mur", (0.16, 0.15, 0.14), 0.95))
boite((0, -0.006, 0), (0.086, 0.012, 0.086), mat("plaque", (0.75, 0.73, 0.7), 0.35))
bpy.ops.object.empty_add(location=(0, -0.013, 0)); piv = bpy.context.object
bas = boite((0, -0.016, 0), (0.05, 0.012, 0.05), mat("bascule", (0.8, 0.78, 0.75), 0.3)); bas.parent = piv
HAUT, BAS = math.radians(14), math.radians(-14)   # haut enfoncé = allumé ; bas enfoncé = éteint
# index : trois phalanges (cylindres) dans un même parent, peau sombre et chaude ; le reste de la main hors champ
peau = mat("peau", (0.45, 0.3, 0.24), 0.5)
bpy.ops.object.empty_add(location=(0.0, -0.03, -0.012)); doigt = bpy.context.object
for k, (z, r) in enumerate([(-0.03, 0.0095), (-0.075, 0.0105), (-0.13, 0.012)]):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=0.05, location=(0, -0.03, -0.012 + z))
    o = bpy.context.object; o.data.materials.append(peau); o.parent = doigt; o.matrix_parent_inverse = doigt.matrix_world.inverted()
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0095, location=(0, -0.03, -0.007)); o = bpy.context.object; o.data.materials.append(peau); o.parent = doigt; o.matrix_parent_inverse = doigt.matrix_world.inverted()
bpy.ops.mesh.primitive_cube_add(location=(0, -0.05, -0.23)); o = bpy.context.object; o.scale = (0.045, 0.025, 0.07); o.data.materials.append(mat("manche", (0.1, 0.1, 0.11), 0.9)); o.parent = doigt; o.matrix_parent_inverse = doigt.matrix_world.inverted()
# le doigt monte d'en bas pour appuyer sur la moitié basse de la bascule
LOIN, CONTACT, ENFONCE = (0.02, -0.09, -0.2), (0.0, -0.01, 0.0), (0.0, 0.0, 0.0)
def cle(o, f, loc=None, rot=None):
    if loc is not None: o.location = loc; o.keyframe_insert("location", frame=f)
    if rot is not None: o.rotation_euler = (rot, 0, 0); o.keyframe_insert("rotation_euler", frame=f)
if sens == "presse":
    cle(doigt, 1, LOIN); cle(doigt, 10, CONTACT); cle(doigt, 13, CONTACT); cle(doigt, 14, ENFONCE); cle(doigt, 16, ENFONCE)
    cle(piv, 13, rot=HAUT); cle(piv, 14, rot=BAS)
else:
    cle(doigt, 1, ENFONCE); cle(doigt, 5, ENFONCE); cle(doigt, 16, LOIN); cle(piv, 1, rot=BAS)
for fc in (doigt.animation_data.action.fcurves if doigt.animation_data else []):
    for kp in fc.keyframe_points: kp.interpolation = "BEZIER"
if piv.animation_data:
    for fc in piv.animation_data.action.fcurves:
        for kp in fc.keyframe_points: kp.interpolation = "CONSTANT"   # contacteur : la bascule claque, pas d'interpolation
# lumière : l'ambre basse (sa lanterne, sous le cadre à droite) et un reste de bleu de rue, faible
bpy.ops.object.light_add(type="POINT", location=(0.25, -0.35, -0.3)); L = bpy.context.object; L.data.energy = 6; L.data.color = (1.0, 0.6, 0.3); L.data.shadow_soft_size = 0.05
bpy.ops.object.light_add(type="AREA", location=(-0.6, -0.8, 0.6)); B = bpy.context.object; B.data.energy = 3; B.data.color = (0.75, 0.85, 1.0); B.data.size = 0.5
B.rotation_euler = (math.radians(-55), math.radians(-30), 0)
# v6 ter (NUIT=1) : la rue est éteinte, il ne reste que sa lanterne, basse et proche : une flaque sur le noir
if os.environ.get("NUIT"):
    B.data.energy = 0; w.node_tree.nodes["Background"].inputs[1].default_value = 0.0
    L.location = (0.06, -0.12, -0.12); L.data.energy = 0.6
import mathutils
bpy.ops.object.camera_add(location=(-0.2, -0.5, 0.1)); c = bpy.context.object; c.data.lens = 50; sc.camera = c
c.rotation_euler = (mathutils.Vector((0.01, 0, -0.03)) - c.location).to_track_quat("-Z", "Y").to_euler()
bpy.ops.render.render(animation=True)
