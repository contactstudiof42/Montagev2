"""Pièce 18 : blender -b -P scene.py -- sortie.png ALLUMES(ex. 1111111) [fenetres 0-4] [ordre]
ALLUMES : un caractère par lampadaire, du plus proche (gauche) au plus lointain. Plan fixe : une image."""
import bpy, sys, math, mathutils, os
a = sys.argv[sys.argv.index("--") + 1:]; out, etat = a[0], a[1]; nfen = int(a[2]) if len(a) > 2 else 4
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = int(os.environ.get("SPP", "48")); sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 640, 360; sc.view_settings.view_transform = "AgX"; sc.view_settings.exposure = float(os.environ.get("EXPO", "0"))
sc.render.filepath = out; sc.render.image_settings.file_format = "PNG"
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.02, 0.025, 0.04, 1); w.node_tree.nodes["Background"].inputs[1].default_value = float(os.environ.get("CIEL", "0.15"))
def mat(n, c, r=0.8, em=None, es=0):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*c, 1); b.inputs["Roughness"].default_value = r
    if em: b.inputs["Emission Color"].default_value = (*em, 1); b.inputs["Emission Strength"].default_value = es
    return m
def boite(loc, dim, m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.scale = [d / 2 for d in dim]; o.data.materials.append(m); return o
bitume = mat("bitume", (0.08, 0.08, 0.09), 0.6); trottoir = mat("trottoir", (0.22, 0.21, 0.2), 0.9); facade = mat("facade", (0.18, 0.17, 0.17), 0.95)
boite((0, 40, -0.05), (8, 100, 0.1), bitume)
for sx in (-5.5, 5.5): boite((sx, 40, 0.05), (3, 100, 0.1), trottoir)
for sx in (-8.5, 8.5): boite((sx, 40, 6), (3, 100, 12), facade)
LED = (0.75, 0.85, 1.0)
# lampadaires côté droit, tous les 9 m, du plus proche au plus lointain
for i, on in enumerate(etat):
    y = 6 + 9 * i; x = 4.6
    boite((x, y, 3), (0.12, 0.12, 6), mat(f"mat{i}", (0.1, 0.1, 0.1)))
    boite((x - 0.6, y, 6), (1.3, 0.1, 0.1), mat(f"bras{i}", (0.1, 0.1, 0.1)))
    tete = boite((x - 1.2, y, 5.92), (0.5, 0.25, 0.08), mat(f"tete{i}", (0.05, 0.05, 0.05), 0.4, LED, 40 if on == "1" else 0))
    if on == "1":
        bpy.ops.object.light_add(type="SPOT", location=(x - 1.2, y, 5.85)); L = bpy.context.object
        L.data.energy = 1800; L.data.color = LED; L.data.spot_size = math.radians(120); L.data.spot_blend = 0.6; L.data.shadow_soft_size = 0.2
# fenêtres allumées (façade gauche), chaudes et faibles
fen = [(-6.95, 14, 4), (-6.95, 23, 7), (-6.95, 31, 4), (-6.95, 48, 7)]
for k, (x, y, z) in enumerate(fen[:nfen]):
    boite((x, y, z), (0.05, 1.2, 1.4), mat(f"fen{k}", (0, 0, 0), 0.5, (1.0, 0.75, 0.45), 3))
# le personnage : silhouette sur le trottoir gauche, source ambre basse tenue à sa droite (vers la rue)
peau = mat("veste", (0.12, 0.12, 0.13), 0.9)
# silhouette (v3) : jambes, torse étroit, épaules, tête, un bras qui tient la source vers la rue
def cyl(r, d, loc, rot=(0, 0, 0), m=None):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=d, location=loc, rotation=rot); bpy.context.object.data.materials.append(m or peau)
for dx in (-0.09, 0.09): cyl(0.075, 0.85, (-3.2 + dx, 16, 0.43))
cyl(0.19, 0.62, (-3.2, 16, 1.17)); cyl(0.06, 0.5, (-3.2, 16, 1.45), (0, math.radians(90), 0))   # torse, épaules
cyl(0.05, 0.55, (-3.05, 15.9, 1.08), (0, math.radians(-25), 0))                                   # bras vers la rue
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(-3.2, 16, 1.66)); bpy.context.object.data.materials.append(mat("tete", (0.4, 0.3, 0.25), 0.6))
bpy.ops.object.light_add(type="POINT", location=(-2.85, 15.8, 0.85)); A = bpy.context.object
A.data.energy = float(os.environ.get("AMBRE", "25")); A.data.color = (1.0, 0.6, 0.3); A.data.shadow_soft_size = 0.1
# caméra : depuis une passerelle, en hauteur, regard dans l'axe de la rue
cam = (0.5, -6, 7.5) if not os.environ.get("SERRE") else (-0.5, 4, 4.0)   # v3 : plus bas et plus près, le personnage au tiers
bpy.ops.object.camera_add(location=cam); c = bpy.context.object; c.data.lens = float(os.environ.get("LENS", "32"))
c.rotation_euler = (mathutils.Vector((0, 30, 0.5) if not os.environ.get("SERRE") else (-0.8, 24, 1.2)) - c.location).to_track_quat("-Z", "Y").to_euler(); sc.camera = c
bpy.ops.render.render(write_still=True)
