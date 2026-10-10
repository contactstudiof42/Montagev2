"""Pièce 22 « Cent dix-sept milliards » (à la manière d'EGO) — scène Blender.
blender -b -P scene.py -- OUTDIR N [--figure] [--final] [--noir]
Rend N images d'un recul continu (paramètre u de 0 à 1) : une chaise seule → sa colonne (les mères) → un champ
de chaises qui se perd dans le blanc. --final : plan fixe latéral bas, une silhouette assise sur la première chaise.
Tout est géométrie primitive (aucun média externe). Cycles CPU, 480×270."""
import bpy, math, sys
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:]
OUT, N = argv[0], int(argv[1])
FINAL, FIG, NOIR = "--final" in argv, "--figure" in argv or "--final" in argv, "--noir" in argv
V3 = "--v3" in argv
if V3: argv.append("--v2")   # v3 hérite de la trajectoire v2
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.samples = 8; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 480, 270
sc.view_settings.view_transform = "AgX"; sc.view_settings.exposure = 0.0 if NOIR else (1.0 if "--v2" in argv else 0.6); sc.view_settings.look = "AgX - Base Contrast" if not NOIR else "AgX - High Contrast"
COLS, ROWS, DX, DY = 241, 260, 1.0, 1.25


def mat(name, rgb, rough=0.6, emit=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1); b.inputs["Roughness"].default_value = rough
    return m


def box(name, loc, dims, m):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object
    o.scale = dims; o.name = name; o.data.materials.append(m); return o


# --- une chaise (assise, dossier, 4 pieds), orientée vers +Y (vers le vide) ---
mc = mat("chaise", (0.45, 0.45, 0.47) if not NOIR else (0.05, 0.05, 0.06), 0.45)
parts = [box("assise", (0, 0, 0.45), (0.44, 0.42, 0.04), mc), box("dossier", (0, -0.2, 0.72), (0.44, 0.03, 0.5), mc)]
for sx in (-1, 1):
    for sy in (-1, 1):
        parts.append(box("pied", (0.19 * sx, 0.18 * sy, 0.22), (0.03, 0.03, 0.44), mc))
for p in parts: p.select_set(True)
bpy.context.view_layer.objects.active = parts[0]; bpy.ops.object.transform_apply(scale=True); bpy.ops.object.join()
chaise = bpy.context.object; chaise.name = "chaise_1"
# le champ : une copie décalée, multipliée par deux modificateurs Array (instances bon marché pour Cycles)
champ = chaise.copy(); champ.data = chaise.data; bpy.context.collection.objects.link(champ)
champ.location = (-(COLS // 2) * DX, -DY, 0)
a = champ.modifiers.new("x", "ARRAY"); a.count = COLS; a.relative_offset_displace = (0, 0, 0); a.use_relative_offset = False
a.use_constant_offset = True; a.constant_offset_displace = (DX, 0, 0)
b = champ.modifiers.new("y", "ARRAY"); b.count = ROWS; b.use_relative_offset = False
b.use_constant_offset = True; b.constant_offset_displace = (0, -DY, 0)
# v2 : la chaise 1 est SEULE devant le champ (la première rangée est vide) : « tout au bout »
for side in ((-1, 1) if "--rangee" in argv else ()):
    r = chaise.copy(); r.data = chaise.data; bpy.context.collection.objects.link(r)
    r.location = (side * DX, 0, 0)
    m = r.modifiers.new("x", "ARRAY"); m.count = COLS // 2; m.use_relative_offset = False
    m.use_constant_offset = True; m.constant_offset_displace = (side * DX, 0, 0)

# sol, monde blanc clinique (ou noir + une lumière froide en --noir)
bpy.ops.mesh.primitive_plane_add(size=2000); sol = bpy.context.object
sol.data.materials.append(mat("sol", ((0.9, 0.9, 0.91) if V3 else (0.8, 0.8, 0.82)) if not NOIR else (0.02, 0.02, 0.025), 0.35))
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1) if not NOIR else (0, 0, 0, 1)
w.node_tree.nodes["Background"].inputs[1].default_value = 0.55 if not NOIR else 0.0
bpy.ops.object.light_add(type="SUN", location=(0, 0, 10)); sun = bpy.context.object
sun.data.energy = 4.0 if not NOIR else 3.0; sun.data.angle = math.radians(12)
sun.rotation_euler = (math.radians(50), 0, math.radians(200))
if NOIR: sun.data.color = (0.6, 0.75, 1.0)

if FIG:  # silhouette assise, noire, sur la chaise 1 (tête, buste, cuisses, tibias)
    mf = mat("figure", (0.85, 0.88, 0.95) if (NOIR and "--v3b" in argv) else (0.01, 0.01, 0.012), 0.8)  # v3b noir : la silhouette devient la lumière
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, location=(0, -0.08, 1.32)); bpy.context.object.data.materials.append(mf)
    box("buste", (0, -0.1, 0.85), (0.34, 0.2, 0.62), mf); box("cuisses", (0, 0.1, 0.53), (0.3, 0.42, 0.14), mf)
    box("tibias", (0, 0.32, 0.25), (0.28, 0.1, 0.5), mf)

# mist → mélange vers la couleur du monde : le champ « se perd » au lieu de s'arrêter
sc.view_layers[0].use_pass_mist = True
w.mist_settings.start, w.mist_settings.depth, w.mist_settings.falloff = 18, 260, "QUADRATIC"
sc.use_nodes = True; nt = sc.node_tree; nt.nodes.clear()
rl = nt.nodes.new("CompositorNodeRLayers"); mix = nt.nodes.new("CompositorNodeMixRGB"); comp = nt.nodes.new("CompositorNodeComposite")
mix.inputs[2].default_value = ((1.0, 1.0, 1.0, 1) if "--v3b" in argv else (0.93, 0.93, 0.94, 1)) if not NOIR else (0, 0, 0, 1)
nt.links.new(rl.outputs["Mist"], mix.inputs[0]); nt.links.new(rl.outputs["Image"], mix.inputs[1]); nt.links.new(mix.outputs[0], comp.inputs[0])

bpy.ops.object.camera_add(); cam = bpy.context.object; sc.camera = cam
cam.data.lens = 50; cam.data.clip_end = 2000


def look(pos, tgt):
    cam.location = pos; cam.rotation_euler = (Vector(tgt) - Vector(pos)).to_track_quat("-Z", "Y").to_euler()


def recul(u):
    """u 0→1 : distance exponentielle 2,4 m → 90 m ; la visée glisse de la chaise vers le fond du champ."""
    dist = 2.0 * (90 / 2.0) ** u
    if "--v2" in argv:  # v2 : la chaise 1 reste dans le bas du cadre tout le recul ; départ moins plongeant (assise lisible)
        dist = 2.6 * (90 / 2.6) ** u
    pitch = math.radians(62 - 34 * u)                       # plongée qui se relève vers l'horizon
    tgt = Vector((0, -0.35 - 28 * u ** 2, 0.5 * (1 - u)))
    if "--v2" in argv:
        pitch = math.radians(38 - 12 * u); tgt = Vector((0, -0.6 - (2 + 0.25 * dist) * u, 0.45 * (1 - u)))
    pos = tgt + Vector((0.25 * (1 - u), math.cos(pitch) * dist, math.sin(pitch) * dist))
    look(pos, tgt)
    cam.data.lens = 50 - 15 * u


if FINAL:
    look((7.5, 6.0, 1.1), (-3.0, -6.0, 0.6)); cam.data.lens = 40
    if "--v2" in argv: look((5.5, 9.0, 1.0), (-4.5, -4.0, 0.9)); cam.data.lens = 40   # silhouette au tiers droit, vide devant elle
    if V3:  # v3 : caméra plus haute, horizon au tiers supérieur ; la silhouette au tiers inférieur gauche, le blanc devant elle
        cx = [float(v) for v in argv[argv.index("--cam") + 1].split(",")] if "--cam" in argv else (14.0, 2.5, 2.4, 0.0, -1.2, 1.3)
        look(cx[:3], cx[3:]); cam.data.lens = 40
    sc.render.filepath = f"{OUT}/final.png"; bpy.ops.render.render(write_still=True)
else:
    for i in range(N):
        recul(i / (N - 1))
        sc.render.filepath = f"{OUT}/r{i:03d}.png"; bpy.ops.render.render(write_still=True)
