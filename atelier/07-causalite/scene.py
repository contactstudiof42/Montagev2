"""Pièce 07 « Causalité » — chaîne causale simulée (corps rigides) sur la table de la pièce 06.
Lancer : blender -b -P scene.py -- params.json outdir
params.json : {"mode": "sim" | "render", "camera": "large"|"livre"|"dominos"|"tasse",
               "res": [480, 270], "engine": "EEVEE"|"CYCLES", "samples": 16, "frames": [1, 200]}
mode "sim" : simule et écrit outdir/sim.json (positions + contacts par image), sans rendu.
"""
import bpy, json, math, sys, os
argv = sys.argv[sys.argv.index("--") + 1:]
P = json.load(open(argv[0])); out = argv[1]; os.makedirs(out, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
F1, F2 = P.get("frames", [1, 200])
sc.render.fps = 25; sc.frame_start, sc.frame_end = F1, F2
eng = P.get("engine", "EEVEE")
sc.render.engine = "BLENDER_EEVEE_NEXT" if eng == "EEVEE" else "CYCLES"
if eng == "CYCLES":
    sc.cycles.device = "CPU"; sc.cycles.samples = P.get("samples", 16); sc.cycles.use_denoising = True; sc.cycles.seed = 7
else:
    sc.eevee.taa_render_samples = P.get("samples", 16)
sc.render.resolution_x, sc.render.resolution_y = P.get("res", [480, 270])
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
sc.render.image_settings.file_format = "PNG"; sc.render.filepath = os.path.join(out, "####")

w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.02, 0.025, 0.03, 1)
w.node_tree.nodes["Background"].inputs[1].default_value = 0.3

def mat(name, col, rough=0.5):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*col, 1); b.inputs["Roughness"].default_value = rough
    return m

def boite(nom, loc, dim, m, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(location=loc, rotation=rot); o = bpy.context.object; o.name = nom
    o.scale = (dim[0] / 2, dim[1] / 2, dim[2] / 2); bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)  # appliquer aussi la position décentre la forme de collision (piège vu en s6)
    o.data.materials.append(m); return o

def rigide(o, kind="ACTIVE", shape="CONVEX_HULL", masse=0.1, frot=0.5, rebond=0.1):
    bpy.context.view_layer.objects.active = o; o.select_set(True)
    bpy.ops.rigidbody.object_add(); rb = o.rigid_body
    rb.type = kind; rb.collision_shape = shape; rb.mass = masse; rb.friction = frot; rb.restitution = rebond
    rb.collision_margin = 0.001; o.select_set(False)

bpy.ops.rigidbody.world_add(); rw = sc.rigidbody_world
rw.substeps_per_frame = 40; rw.solver_iterations = 30
rw.point_cache.frame_start, rw.point_cache.frame_end = F1, F2

TOP = 0.76
sol = boite("sol", (0, 0, -0.01), (8, 8, 0.02), mat("sol", (0.12, 0.09, 0.07), 0.6)); rigide(sol, "PASSIVE", "BOX", frot=0.8)
boite("mur", (0, 1.2, 1.5), (8, 0.02, 3), mat("mur", (0.42, 0.40, 0.36), 0.9))
bois = mat("bois", (0.16, 0.09, 0.05), 0.45)
plateau = boite("plateau", (0, 0.3, TOP - 0.02), (1.7, 0.7, 0.04), bois); rigide(plateau, "PASSIVE", "BOX", frot=0.8)
for dx in (-0.8, 0.8):
    for dy in (0.0, 0.6):
        boite("pied", (dx, dy, 0.36), (0.04, 0.04, 0.72), bois)

# Livre incliné (rampe) à gauche, bille en haut
ang = math.radians(P.get("pente", 14))
L = 0.30
livre = boite("livre", (-0.62, 0.2, TOP + math.sin(ang) * L / 2 + 0.01), (L, 0.2, 0.02),
              mat("couverture", (0.35, 0.06, 0.05), 0.7), rot=(0, ang, 0))
rigide(livre, "PASSIVE", "BOX", frot=0.4)
cale = boite("cale", (-0.62 - L / 2 + 0.03, 0.2, TOP + math.sin(ang) * L / 2), (0.06, 0.2, math.sin(ang) * L), bois)
rigide(cale, "PASSIVE", "BOX")
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.022, location=(-0.62 - L / 2 + 0.05, 0.2, TOP + math.sin(ang) * L + 0.045))
bille = bpy.context.object; bille.name = "bille"; bpy.ops.object.shade_smooth()
bille.data.materials.append(mat("acier", (0.8, 0.8, 0.82), 0.12))
bille.data.materials[0].node_tree.nodes["Principled BSDF"].inputs["Metallic"].default_value = 1
rigide(bille, shape="SPHERE", masse=0.06, frot=0.3, rebond=0.2)

# Dominos (ivoire), le long de x
n = P.get("n_dominos", 6); x_d0 = P.get("x_d0", -0.36); pas = P.get("pas", 0.07)
dominos = []
ivoire = mat("ivoire", (0.8, 0.76, 0.66), 0.35)
for i in range(n):
    d = boite(f"domino{i}", (x_d0 + i * pas, 0.2, TOP + 0.045), (0.012, 0.045, 0.09), ivoire)
    rigide(d, shape="BOX", masse=P.get("masse_domino", 0.05), frot=0.7, rebond=0.02); dominos.append(d)

# Tasse au bord droit (bord du plateau à x = 0.85)
xt = P.get("x_tasse", 0.80)
bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.09, location=(xt, 0.2, TOP + 0.046)); tasse = bpy.context.object
tasse.name = "tasse"; tasse.data.materials.append(mat("faience", (0.85, 0.83, 0.78), 0.15))
bpy.ops.object.shade_smooth()
rigide(tasse, shape="CYLINDER", masse=P.get("masse_tasse", 0.05), frot=0.4, rebond=0.15)

# Lumières (comme la pièce 06)
bpy.ops.object.light_add(type="AREA", location=(-2.4, 0.3, 1.3)); fen = bpy.context.object
fen.data.shape = "RECTANGLE"; fen.data.size, fen.data.size_y = 0.9, 1.4; fen.data.energy = 450
fen.data.color = (1.0, 0.92, 0.82); fen.rotation_euler = (0, math.radians(-80), 0)
bpy.ops.object.light_add(type="AREA", location=(1.5, -2.5, 1.5)); deb = bpy.context.object
deb.data.energy = 40; deb.data.color = (0.8, 0.88, 1.0); deb.data.size = 2
deb.rotation_euler = (math.radians(60), 0, math.radians(30))

CAMS = {  # loc, rot (deg), focale
    "large":   ((0.05, -1.45, 0.95), (76, 0, 0), 30),
    "livre":   ((-0.45, -0.45, 0.88), (80, 0, 0), 35),
    "dominos": ((0.41, -0.35, 0.86), (84, 0, 0), 32),
    "tasse":   ((0.95, -1.0, 0.42), (90, 0, 0), 26),
}
c = P.get("camera", "large"); loc, rot, lens = CAMS[c]
bpy.ops.object.camera_add(location=loc, rotation=tuple(math.radians(a) for a in rot))
bpy.context.object.data.lens = lens; sc.camera = bpy.context.object

if P.get("debug"): exec(open(P["debug"]).read())
if P.get("mode") == "sim":
    objs = {"bille": bille, "tasse": tasse, **{d.name: d for d in dominos}}
    rec = []
    for f in range(F1, F2 + 1):
        sc.frame_set(f)
        rec.append({k: [list(o.matrix_world.translation), list(o.matrix_world.to_euler())] for k, o in objs.items()})
    json.dump({"frames": [F1, F2], "rec": rec}, open(os.path.join(out, "sim.json"), "w"))
    print("SIM OK")
else:
    bpy.ops.ptcache.bake_all(bake=True)
    if P.get("still"):  # une image de contrôle seulement
        sc.frame_set(P["still"]); sc.render.filepath = os.path.join(out, "%s_%04d.png" % (c, P["still"]))
        bpy.ops.render.render(write_still=True)
    else:
        bpy.ops.render.render(animation=True)
