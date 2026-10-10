"""Pièce 14 « Balancier » (dérivée de la scène de la pièce 12) : la nuit, une lampe suspendue qui se balance et s'amortit.
Paramètres en plus : "frames": [1, 375], "camera": "large"|"serre", "amp0" (rad), "tau" (s, amortissement), "sortie" = dossier.
(Ancien en-tête :) Pièce 12 « Inquiétude calme » — une pièce, une table, une ou deux tasses, une chaise, une fenêtre.
Lancer : blender -b -P scene.py -- params.json sortie.png
params.json : {"camera": "large"|"fenetre", "tasses": 1|2, "res": [480,270], "samples": 24,
               "cam_loc": [...], "cam_rot": [...], "lens": 35, "tache": 0.0 (flaque de lumière sur la table)}
Plans fixes : une seule image rendue par plan (le grain est ajouté au montage).
"""
import bpy, json, math, sys, os
argv = sys.argv[sys.argv.index("--") + 1:]
P = json.load(open(argv[0])); out = argv[1]

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"
sc.cycles.samples = P.get("samples", 24); sc.cycles.use_denoising = True; sc.cycles.seed = 3
sc.render.resolution_x, sc.render.resolution_y = P.get("res", [480, 270])
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Base Contrast"
sc.render.image_settings.file_format = "PNG"; os.makedirs(out, exist_ok=True); sc.render.filepath = os.path.join(out, "####")
sc.render.fps = 25; sc.frame_start, sc.frame_end = P.get("frames", [1, 375])
sc.view_settings.exposure = P.get("expo", 0.0)
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = tuple(P.get("ciel", [0.5, 0.62, 0.85])) + (1,)
w.node_tree.nodes["Background"].inputs[1].default_value = P.get("ciel_f", 0.35)

def mat(n, c, r=0.5):
    m = bpy.data.materials.new(n); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*c, 1); b.inputs["Roughness"].default_value = r
    return m

def boite(n, loc, dim, m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.name = n
    o.scale = (dim[0] / 2, dim[1] / 2, dim[2] / 2); o.data.materials.append(m); return o

mur = mat("mur", (0.45, 0.43, 0.38), 0.9)
boite("sol", (0, 0, -0.01), (8, 8, 0.02), mat("sol", (0.13, 0.1, 0.08), 0.6))
boite("mur_fond", (0, 1.6, 1.5), (8, 0.02, 3), mur)
# mur gauche percé d'une fenêtre (deux montants + allège + linteau)
for loc, dim in (((-2.0, -2.3, 1.5), (0.02, 3.0, 3)), ((-2.0, 1.15, 1.5), (0.02, 0.9, 3)),
                 ((-2.0, -0.05, 0.45), (0.02, 1.5, 0.9)), ((-2.0, -0.05, 2.6), (0.02, 1.5, 0.8))):
    boite("mur_g", loc, dim, mur)
bois = mat("bois", (0.17, 0.10, 0.05), 0.45)
boite("plateau", (0, 0.4, 0.74), (1.2, 0.7, 0.04), bois)
for dx in (-0.55, 0.55):
    for dy in (0.1, 0.7):
        boite("pied", (dx, dy, 0.36), (0.04, 0.04, 0.72), bois)
# chaise rangée
# chaise de l'autre côté de la table, face caméra (une place vide)
boite("assise", (0.0, 0.95, 0.45), (0.42, 0.4, 0.04), bois)
boite("dossier", (0.0, 1.14, 0.75), (0.42, 0.03, 0.6), bois)
for dx in (-0.19, 0.19):
    for dy in (0.77, 1.13):
        boite("pied_ch", (dx, dy, 0.22), (0.03, 0.03, 0.44), bois)

faience = mat("faience", (0.86, 0.84, 0.8), 0.15)
def tasse(x, y, rz=0):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.09, location=(x, y, 0.805))
    bpy.context.object.data.materials.append(faience)
    bpy.ops.mesh.primitive_torus_add(major_radius=0.025, minor_radius=0.006,
        location=(x + 0.045 * math.cos(rz), y + 0.045 * math.sin(rz), 0.81), rotation=(math.radians(90), 0, rz))
    bpy.context.object.data.materials.append(faience)
for t in P.get("tasses_pos", [[0.35, 0.3, 0.0], [-0.05, 0.6, 2.6]])[:P.get("tasses", 1)]:
    tasse(*t)

# soleil par la fenêtre (rasant, chaud) + ciel froid de débouchage
bpy.ops.object.light_add(type="SUN", location=(-4, 0, 3)); s = bpy.context.object
s.data.energy = P.get("soleil", 9.0); s.data.color = (1.0, 0.86, 0.68); s.data.angle = math.radians(1.5)
s.rotation_euler = (0, math.radians(-62), math.radians(P.get("soleil_z", 8)))
bpy.ops.object.light_add(type="AREA", location=(-2.3, -0.05, 1.5)); a = bpy.context.object
a.data.shape = "RECTANGLE"; a.data.size, a.data.size_y = 1.4, 1.3; a.data.energy = P.get("ciel_area", 80)
a.data.color = (0.75, 0.85, 1.0); a.rotation_euler = (0, math.radians(-90), 0)

cam = P.get("camera", "large")
loc = P.get("cam_loc", {"large": [1.15, -1.35, 1.55], "serre": [0.75, -0.25, 1.05]}.get(cam, [0.3, -1.6, 1.3]))
bpy.ops.object.camera_add(location=tuple(loc)); c = bpy.context.object
c.data.lens = P.get("lens", {"large": 26, "serre": 50}.get(cam, 24))
cible = P.get("cible", {"large": [0.0, 0.42, 1.1], "serre": [0.3, 0.3, 0.76]}.get(cam, [-1.0, 0.0, 0.5]))
d = [cible[i] - loc[i] for i in range(3)]
import mathutils
c.rotation_euler = mathutils.Vector(d).to_track_quat("-Z", "Y").to_euler()
sc.camera = c
# lampe suspendue : pivot au plafond (z = 2,4) au-dessus de la table, câble 1 m, abat-jour + ampoule
import math as m
bpy.ops.object.empty_add(location=(0.0, 0.42, 2.4)); piv = bpy.context.object
bpy.ops.mesh.primitive_cylinder_add(radius=0.004, depth=1.0, location=(0, 0.42, 1.9)); cable = bpy.context.object
cable.data.materials.append(mat("cable", (0.02, 0.02, 0.02)))
bpy.ops.mesh.primitive_cone_add(radius1=0.13, radius2=0.03, depth=0.12, location=(0, 0.42, 1.4)); abat = bpy.context.object
abat.data.materials.append(mat("abat", (0.05, 0.05, 0.05), 0.4))
bpy.ops.object.light_add(type="POINT", location=(0, 0.42, 1.36)); amp = bpy.context.object
amp.data.energy = P.get("lampe", 150); amp.data.color = (1.0, 0.78, 0.5); amp.data.shadow_soft_size = 0.03
for o in (cable, abat, amp):
    o.parent = piv; o.matrix_parent_inverse = piv.matrix_world.inverted()
T0 = 2 * m.pi * (1.0 / 9.81) ** 0.5; tau = P.get("tau", 6.0); A0 = P.get("amp0", 0.35)
morts = []
for f in range(sc.frame_start, sc.frame_end + 1):
    t = (f - 1) / 25
    piv.rotation_euler = (0, A0 * m.exp(-t / tau) * m.cos(2 * m.pi * t / T0), 0); piv.keyframe_insert("rotation_euler", frame=f)
    if f > 1 and abs(m.sin(2 * m.pi * t / T0)) < abs(m.sin(2 * m.pi * (t - 0.04) / T0)) and abs(m.sin(2 * m.pi * t / T0)) < abs(m.sin(2 * m.pi * (t + 0.04) / T0)):
        morts.append(f)
json.dump({"periode_s": round(T0, 3), "points_morts": morts}, open(os.path.join(out, "balancier.json"), "w"))
if P.get("render", True):
    bpy.ops.render.render(animation=True)
