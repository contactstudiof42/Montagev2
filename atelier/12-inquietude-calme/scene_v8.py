"""Pièce 12 v8 (lieu encombré) — copie de scene.py + "encombre": true (objets du quotidien) et "soleil_z" libre.
Pièce 12 « Inquiétude calme » — une pièce, une table, une ou deux tasses, une chaise, une fenêtre.
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
sc.render.image_settings.file_format = "PNG"; sc.render.filepath = out
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


# v8 : lieu encombré (objets du quotidien, couleurs ternes ; un pot à sucre blanc = leurre proche de la tasse)
if P.get("encombre"):
    def cyl(n, loc, r, h, m, verts=32):
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=loc)
        o = bpy.context.object; o.name = n; o.data.materials.append(m); return o
    papier = mat("papier", (0.62, 0.6, 0.55), 0.8); rouge = mat("rouge", (0.35, 0.08, 0.06), 0.6)
    vert = mat("vert", (0.12, 0.2, 0.1), 0.7); verre = mat("verre", tuple(P.get("verre_c", [0.5, 0.55, 0.55])), 0.05)
    fruit = mat("fruit", (0.55, 0.3, 0.06), 0.5); metal = mat("metal", (0.3, 0.3, 0.32), 0.3)
    boite("journal", (-0.3, 0.28, 0.765), (0.32, 0.24, 0.006), papier)
    cyl("coupe", (-0.42, 0.58, 0.79), 0.11, 0.06, faience if P.get("coupe_blanche") else rouge)
    for i, (x, y) in enumerate(((-0.45, 0.55), (-0.39, 0.61), (-0.43, 0.63))):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.035, location=(x, y, 0.84)); bpy.context.object.data.materials.append(fruit)
    for i, (dz, c) in enumerate(((0.0, rouge), (0.03, vert), (0.06, papier))):
        boite("livre", (0.45, 0.6, 0.775 + dz), (0.22, 0.16, 0.03), c)
    cyl("sucre", (0.18, 0.55, 0.81), 0.038, 0.1, faience)          # leurre blanc
    boite("couvercle", (0.18, 0.55, 0.865), (0.06, 0.06, 0.01), metal)
    cyl("verre", (0.22, 0.2, 0.81), 0.03, 0.1, verre)
    boite("cles", (0.05, 0.18, 0.763), (0.06, 0.02, 0.004), metal)
    # étagère au mur du fond : bocaux, boîtes
    ez = P.get("etagere_z", 1.45); ex = P.get("etagere_x", 0.0)
    boite("etagere", (0.3 + ex, 1.5, ez), (1.4, 0.18, 0.03), bois)
    for i, x in enumerate((-0.25, -0.05, 0.15, 0.4, 0.62, 0.85)):
        cyl("bocal", (x + ex, 1.5, ez + 0.08), 0.05, 0.13 + 0.03 * (i % 2), (verre, papier, rouge, vert, papier, metal)[i])
    boite("calendrier", tuple(P.get("cal_loc", [-0.6, 1.585, 1.25])), (0.3, 0.005, 0.42), papier)
    if P.get("radio"):
        boite("radio", (0.62, 0.3, 0.83), (0.2, 0.08, 0.12), mat("radio", tuple(P.get("radio_c", [0.3, 0.3, 0.32])), 0.5))
    boite("cabas", (0.75, 0.9, 0.2), (0.3, 0.18, 0.4), vert)
    boite("gilet", (0.0, P.get("gilet_y", 1.17), 0.85), (0.38, 0.04, 0.35), rouge)   # gilet sur le dossier de la chaise vide

# soleil par la fenêtre (rasant, chaud) + ciel froid de débouchage
bpy.ops.object.light_add(type="SUN", location=(-4, 0, 3)); s = bpy.context.object
s.data.energy = P.get("soleil", 9.0); s.data.color = (1.0, 0.86, 0.68); s.data.angle = math.radians(1.5)
s.rotation_euler = (0, math.radians(-62), math.radians(P.get("soleil_z", 8)))
bpy.ops.object.light_add(type="AREA", location=(-2.3, -0.05, 1.5)); a = bpy.context.object
a.data.shape = "RECTANGLE"; a.data.size, a.data.size_y = 1.4, 1.3; a.data.energy = P.get("ciel_area", 80)
a.data.color = (0.75, 0.85, 1.0); a.rotation_euler = (0, math.radians(-90), 0)

cam = P.get("camera", "large")
loc = P.get("cam_loc", [1.5, -1.9, 1.45] if cam == "large" else [0.3, -1.6, 1.3])
bpy.ops.object.camera_add(location=tuple(loc)); c = bpy.context.object
c.data.lens = P.get("lens", 32 if cam == "large" else 24)
cible = P.get("cible", [0.0, 0.45, 0.78] if cam == "large" else [-1.0, 0.0, 0.5])
d = [cible[i] - loc[i] for i in range(3)]
import mathutils
c.rotation_euler = mathutils.Vector(d).to_track_quat("-Z", "Y").to_euler()
sc.camera = c
bpy.ops.render.render(write_still=True)
