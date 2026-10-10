"""Pièce 10 « Chaleur partout » (copie de la scène 08 + "monde", "lampe", "ecran").
Pièce 08 « Souvenir » — reprend le plateau de la pièce 06 (table, tasse, fenêtre).
Ajouts : "sans_tasse" (la tasse absente), "fen_col" (couleur de la fenêtre), "main" (caméra portée :
micro-dérive + zoom lent, amplitude en degrés), "zoom" [lens0, lens1].
(Origine : pièce 06 « Versions » — une tasse tombe d'une table, trois variantes.)
Lancer : blender -b -P scene.py -- params.json outdir
params.json : {"variante": "seule" | "tremble" | "ombre", "camera": "large" | "insert",
               "res": [480, 270], "samples": 16, "frames": [1, 75],
               "chute": 50,            # image où la tasse commence à basculer
               "tremble": [36, 44],    # secousse de la table (variante tremble)
               "ombre": [18, 44]}      # passage de l'ombre (variante ombre)
Tout est identique entre variantes sauf le détail changé (même cadre, même chute à l'image près).
"""
import bpy, json, math, sys, os
argv = sys.argv[sys.argv.index("--") + 1:]
P = json.load(open(argv[0])); out = argv[1]; os.makedirs(out, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"
sc.cycles.samples = P.get("samples", 16); sc.cycles.use_denoising = True
sc.cycles.seed = 7  # bruit identique d'une variante à l'autre
sc.render.resolution_x, sc.render.resolution_y = P.get("res", [480, 270])
sc.render.fps = 25; sc.frame_start, sc.frame_end = P.get("frames", [1, 75])
sc.view_settings.view_transform = P.get("vue", "AgX")  # v4 : "Standard" pour tester la compression AgX
if sc.view_settings.view_transform == "AgX": sc.view_settings.look = "AgX - Medium High Contrast"
sc.render.image_settings.file_format = "PNG"
sc.render.filepath = os.path.join(out, "####")

w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.02, 0.025, 0.03, 1)
w.node_tree.nodes["Background"].inputs[1].default_value = 0.3


def mat(name, col, rough=0.5):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*col, 1); b.inputs["Roughness"].default_value = rough
    return m


def boite(nom, loc, dim, m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.name = nom
    o.scale = (dim[0] / 2, dim[1] / 2, dim[2] / 2); o.data.materials.append(m); return o


mur_m = mat("mur", (0.42, 0.40, 0.36), 0.9)
boite("sol", (0, 0, -0.01), (8, 8, 0.02), mat("sol", (0.12, 0.09, 0.07), 0.6))
boite("mur", (0, 1.2, 1.5), (8, 0.02, 3), mur_m)

# Table (plateau + 4 pieds), parentée à un vide pour la secousse
bpy.ops.object.empty_add(location=(0, 0, 0)); table = bpy.context.object; table.name = "table"
bois = mat("bois", (0.16, 0.09, 0.05), 0.45)
parts = [boite("plateau", (0, 0.3, 0.74), (1.2, 0.7, 0.04), bois)]
for dx in (-0.55, 0.55):
    for dy in (0.0, 0.6):
        parts.append(boite("pied", (dx, dy, 0.36), (0.04, 0.04, 0.72), bois))
for o in parts:
    o.parent = table

# Tasse : cylindre creux simplifié (cylindre + anse en tore), posée au bord avant de la table
bpy.ops.object.empty_add(location=(0.35, -0.03, 0.76)); pivot = bpy.context.object; pivot.name = "pivot"
pivot.parent = table
faience = mat("faience", (0.85, 0.83, 0.78), 0.15)
bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.09, location=(0, 0.035, 0.045)); tasse = bpy.context.object
bpy.ops.mesh.primitive_torus_add(major_radius=0.025, minor_radius=0.006, location=(0.045, 0.035, 0.05),
                                 rotation=(math.radians(90), 0, 0)); anse = bpy.context.object
if P.get("cuillere"):  # v4 : un indice d'usage (quelqu'un buvait ce café)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.003, depth=0.10, location=(-0.018, 0.03, 0.095),
                                        rotation=(math.radians(-30), math.radians(-35), 0))
    cu = bpy.context.object; cu.data.materials.append(mat("inox", (0.8, 0.8, 0.82), 0.2))
    cu.material_slots[0].material.node_tree.nodes["Principled BSDF"].inputs["Metallic"].default_value = 1
    cu.parent = pivot; cu.hide_render = bool(P.get("sans_tasse"))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.036, depth=0.002, location=(0, 0.035, 0.0915))  # café resté dans la tasse
    cafe = bpy.context.object; cafe.data.materials.append(mat("cafe", (0.03, 0.015, 0.006), 0.35))
    cafe.parent = pivot; cafe.hide_render = bool(P.get("sans_tasse"))
if P.get("trace") and P.get("sans_tasse"):  # le présent : la trace sèche d'un fond de tasse, là où elle était
    bpy.ops.mesh.primitive_torus_add(major_radius=0.038, minor_radius=0.0025, location=(0.35, 0.005, 0.7605))
    tr = bpy.context.object; tr.scale = (1, 1, 0.15); tr.data.materials.append(mat("trace", (0.07, 0.035, 0.015), 0.6))
    tr.parent = table
for o in (tasse, anse):
    o.data.materials.append(faience); o.parent = pivot
    o.hide_render = bool(P.get("sans_tasse"))

# Lumière : fenêtre à gauche (grande source douce, légèrement chaude) + débouchage froid faible
bpy.ops.object.light_add(type="AREA", location=(-2.4, 0.3, 1.3)); fen = bpy.context.object
fen.data.shape = "RECTANGLE"; fen.data.size, fen.data.size_y = 0.9, 1.4; fen.data.energy = P.get("fenetre", 450)
fen.data.color = tuple(P.get("fen_col", [1.0, 0.92, 0.82]))
fen.rotation_euler = (0, math.radians(-80), 0)
if P.get("monde"):  # ambiance générale (couleur, intensité)
    *c, k = P["monde"]; w.node_tree.nodes["Background"].inputs[0].default_value = (*c, 1)
    w.node_tree.nodes["Background"].inputs[1].default_value = k
if P.get("lampe"):  # lampe de bureau chaude sur la table (source motivée de la chaleur générale)
    bpy.ops.object.light_add(type="POINT", location=(-0.35, 0.45, 1.15)); la = bpy.context.object
    la.data.energy = P["lampe"]; la.data.color = (1.0, 0.62, 0.32); la.data.shadow_soft_size = 0.08
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.05, location=(-0.35, 0.45, 1.15)); ab = bpy.context.object
    em = bpy.data.materials.new("abat"); em.use_nodes = True; nb = em.node_tree.nodes["Principled BSDF"]
    nb.inputs["Emission Color"].default_value = (1, .6, .3, 1); nb.inputs["Emission Strength"].default_value = 8
    ab.data.materials.append(em); ab.visible_shadow = False
    ab.visible_camera = not P.get("lampe_hors_champ", False)  # v2 : la source hors champ, seule sa lumière est dans l'image
if P.get("ecran"):  # l'événement froid : un téléphone posé face en l'air qui s'allume
    if P.get("feuille"):  # v3 : une surface neutre pour recevoir le froid
        bpy.ops.mesh.primitive_plane_add(size=1, location=(0.05, 0.2, 0.7615)); fe = bpy.context.object
        fe.scale = (0.21, 0.297, 1); fe.rotation_euler = (0, 0, math.radians(12))
        fe.data.materials.append(mat("papier", (0.8, 0.8, 0.78), 0.8))
    if P.get("main_ecran"):  # v5 : une main (forme simple couleur peau) au-dessus du téléphone, à P["main"] m, qui reçoit la lumière de l'écran
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.05, location=(0.05, 0.17, 0.767 + P["main_ecran"])); mn = bpy.context.object
        mn.scale = (0.9, 1.6, 0.35); mn.data.materials.append(mat("peau", (0.62, 0.45, 0.36), 0.55))
    bpy.ops.mesh.primitive_cube_add(location=(0.05, 0.2, 0.767)); ph = bpy.context.object; ph.scale = (0.04, 0.075, 0.004)
    pm = bpy.data.materials.new("ecran"); pm.use_nodes = True; nb = pm.node_tree.nodes["Principled BSDF"]
    nb.inputs["Base Color"].default_value = (0.01, 0.01, 0.01, 1)
    nb.inputs["Emission Color"].default_value = (*P.get("ecran_col", [0.55, 0.75, 1]), 1); nb.inputs["Emission Strength"].default_value = P["ecran"]
    ph.data.materials.append(pm)
    bpy.ops.object.light_add(type="AREA", location=(0.05, 0.2, 0.80)); el = bpy.context.object
    el.data.energy = P.get("ecran_eclaire", P["ecran"] * 0.6); el.data.color = tuple(P.get("ecran_col", [0.55, 0.75, 1.0])); el.data.size = 0.12  # v4 : couleur saturée = gélatine CTB
bpy.ops.object.light_add(type="AREA", location=(1.5, -2.5, 1.5)); deb = bpy.context.object
deb.data.energy = 40; deb.data.color = (0.8, 0.88, 1.0); deb.data.size = 2
deb.rotation_euler = (math.radians(60), 0, math.radians(30))

# Chute : bascule autour du bord (6 images) puis chute libre jusqu'au sol (g = 9,81)
F0 = P.get("chute", 50)
def cle(f, loc, rot):
    pivot.location = loc; pivot.rotation_euler = rot
    pivot.keyframe_insert("location", frame=f); pivot.keyframe_insert("rotation_euler", frame=f)
x0, y0, z0 = 0.35, -0.03, 0.76
cle(1, (x0, y0, z0), (0, 0, 0)); cle(F0, (x0, y0, z0), (0, 0, 0))
for i in range(1, 7):  # bascule vers l'avant (y négatif)
    a = math.radians(90) * (i / 6) ** 2
    cle(F0 + i, (x0, y0 - 0.02 * i, z0), (-a, 0, 0))
t, f, z, y = 0.0, F0 + 6, z0, y0 - 0.12
while z > 0.045:
    f += 1; t += 1 / 25; z = max(0.04, z0 - 0.5 * 9.81 * t * t); y -= 0.02
    cle(f, (x0, y, z), (math.radians(-90 - 400 * t), 0, 0))
# v1 : la tasse finissait à moitié dans le sol (rotation -180°, z 0,04). "repos_sol" la couche sur le flanc.
if P.get("repos_sol"):
    cle(f + 1, (x0, y - 0.01, 0.085), (math.radians(-90), 0, 0))
else:
    cle(f + 1, (x0, y - 0.01, 0.04), (math.radians(-180), 0, 0))
sc["impact"] = f
for fc in pivot.animation_data.action.fcurves:
    for kp in fc.keyframe_points:
        kp.interpolation = "LINEAR"

V = P.get("variante", "seule")
if P.get("indice_lumiere"):  # v3 : baisse brève de la fenêtre (un indice qu'on peut relire, ou pas)
    f0, f1, k = P["indice_lumiere"]; e = fen.data.energy
    for f, val in ((f0 - 1, e), (f0, e * k), (f1, e * k), (f1 + 1, e)):
        fen.data.energy = val; fen.data.keyframe_insert("energy", frame=f)
    fen.data.energy = e
if V == "tremble":  # secousse : quelques millimètres, amortie
    a, b = P.get("tremble", [36, 44])
    for k, f in enumerate(range(a, b + 1)):
        amp = P.get("tremble_amp", 0.006) * (1 - k / (b - a + 1))
        table.location = ((-1) ** k * amp, 0, 0); table.keyframe_insert("location", frame=f)
    table.location = (0, 0, 0); table.keyframe_insert("location", frame=b + 1)
    table.keyframe_insert("location", frame=1)
if V == "ombre":  # silhouette invisible à la caméra qui passe devant la fenêtre
    a, b = P.get("ombre", [18, 44])
    sil = boite("silhouette", (-1.6, -1.5, 0.9), (0.45, 0.3, 1.75), mat("noir", (0, 0, 0)))
    sil.visible_camera = False; sil.visible_glossy = False
    zs = sil.location.z
    sil.location = (-1.6, -1.3, zs); sil.keyframe_insert("location", frame=a)
    sil.location = (-1.6, 1.5, zs); sil.keyframe_insert("location", frame=b)

# Caméras : large (même cadre pour les trois versions) et insert (la tasse au bord)
if P.get("camera", "large") == "large":
    rx, ry, rz = P.get("cam_rot", [82, 0, 32])
    bpy.ops.object.camera_add(location=tuple(P.get("cam_loc", [1.25, -2.1, 1.0])),
                              rotation=(math.radians(rx), math.radians(ry), math.radians(rz)))
    bpy.context.object.data.lens = P.get("cam_lens", 38)
else:
    il = P.get("insert_loc", [0.62, -0.42, 0.86]); ir = P.get("insert_rot", [80, 0, 35])
    bpy.ops.object.camera_add(location=tuple(il), rotation=tuple(math.radians(a) for a in ir))
    if P.get("insert_cible"):  # viser un point (le haut de la tasse) plutôt que régler des angles à l'aveugle
        from mathutils import Vector
        cobj = bpy.context.object; d = Vector(P["insert_cible"]) - cobj.location
        cobj.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    bpy.context.object.data.lens = 85; bpy.context.object.data.dof.use_dof = True
    bpy.context.object.data.dof.focus_object = tasse; bpy.context.object.data.dof.aperture_fstop = 2.8
sc.camera = bpy.context.object
cam = sc.camera
if P.get("main"):  # caméra portée : somme de sinus lents, pas de bruit blanc (un bras, pas un séisme)
    amp = math.radians(P["main"]); r0 = tuple(cam.rotation_euler)
    for f in range(sc.frame_start, sc.frame_end + 1, 2):
        t = f / 25
        cam.rotation_euler = (r0[0] + amp * (math.sin(1.3 * t) + 0.5 * math.sin(3.1 * t + 1)),
                              r0[1] + amp * 0.4 * math.sin(2.2 * t + 2),
                              r0[2] + amp * (math.sin(0.9 * t + 0.5) + 0.4 * math.sin(2.7 * t)))
        cam.keyframe_insert("rotation_euler", frame=f)
if P.get("zoom"):
    l0, l1 = P["zoom"]
    cam.data.lens = l0; cam.data.keyframe_insert("lens", frame=sc.frame_start)
    cam.data.lens = l1; cam.data.keyframe_insert("lens", frame=sc.frame_end)
print("IMPACT", sc["impact"])
bpy.ops.render.render(animation=True)
