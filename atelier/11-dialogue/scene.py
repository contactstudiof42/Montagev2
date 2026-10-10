"""Pièce 11 « Dialogue » : deux personnages abstraits, plans fixes rendus en une image chacun + un travelling qui traverse l'axe.
blender -b -P scene.py -- sortie_dir
Mesure pour chaque plan le sens du regard à l'écran de chaque personnage (signe de x_nez - x_tête), cf. labo/grammaire."""
import bpy, json, math, os, sys
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
out = sys.argv[sys.argv.index("--") + 1]; os.makedirs(out, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.samples = 8; sc.cycles.use_denoising = True; sc.cycles.seed = 3
sc.render.resolution_x, sc.render.resolution_y = 480, 270; sc.render.fps = 25
sc.view_settings.view_transform = "AgX"
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (.05, .055, .065, 1)


def mat(c, r=.5):
    m = bpy.data.materials.new("m"); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*c, 1); b.inputs["Roughness"].default_value = r; return m


bpy.ops.mesh.primitive_plane_add(size=14); bpy.context.object.data.materials.append(mat((.12, .11, .1), .8))
bpy.ops.mesh.primitive_plane_add(size=14, location=(0, 3.5, 0), rotation=(math.radians(90), 0, 0))
bpy.context.object.data.materials.append(mat((.25, .24, .22), .9))  # un mur d'un côté seulement : le fond change quand on franchit
bpy.ops.object.light_add(type="AREA", location=(-2.5, -1.5, 3)); L = bpy.context.object
L.data.energy = 300; L.data.size = 2; L.rotation_euler = (Vector((0, 0, 1)) - L.location).to_track_quat("-Z", "Y").to_euler()

P = {}
def perso(nom, x, haut, col):
    """corps (cylindre) + tête + nez ; haut = hauteur des yeux"""
    objs = []
    bpy.ops.mesh.primitive_cylinder_add(radius=.2, depth=haut - .15, location=(x, 0, (haut - .15) / 2)); objs.append(bpy.context.object)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=.16, location=(x, 0, haut)); objs.append(bpy.context.object)
    for o in objs: o.data.materials.append(mat(col))
    bpy.ops.mesh.primitive_cone_add(radius1=.055, depth=.2, location=(x, 0, haut)); nez = bpy.context.object
    nez.data.materials.append(mat((1, 1, 1))); objs.append(nez)
    P[nom] = dict(objs=objs, nez=nez, x=x, haut=haut)


def etat(hA, hB):
    """place les personnages (hauteurs des yeux) et oriente chaque nez vers la tête de l'autre"""
    for nom, h in (("A", hA), ("B", hB)):
        p = P[nom]; c, t, n = p["objs"]; s = h / p["haut"]
        c.scale.z = (h - .15) / (p["haut"] - .15); c.location.z = (h - .15) / 2; t.location.z = h
    for nom, autre in (("A", "B"), ("B", "A")):
        p, q = P[nom], P[autre]; tete = Vector((p["x"], 0, p["objs"][1].location.z)); cible = Vector((q["x"], 0, q["objs"][1].location.z))
        d = (cible - tete).normalized(); p["nez"].location = tete + d * .2
        p["nez"].rotation_euler = d.to_track_quat("-Z", "Y").to_euler(); p["nez"].rotation_euler.rotate_axis("X", math.radians(180))
    bpy.context.view_layer.update()


perso("A", -.6, 1.65, (.9, .35, .05)); perso("B", .6, 1.65, (.1, .3, .9))
ETATS = {"avant": (1.65, 1.05), "apres": (1.65, 1.95)}  # B assis puis debout, plus grand que A


def camera(pos, cible, lens):
    bpy.ops.object.camera_add(location=pos); cam = bpy.context.object
    cam.rotation_euler = (Vector(cible) - Vector(pos)).to_track_quat("-Z", "Y").to_euler(); cam.data.lens = lens; sc.camera = cam
    bpy.context.view_layer.update(); return cam


def mesure(cam):
    r = {}
    for q in ("A", "B"):
        t = world_to_camera_view(sc, cam, P[q]["objs"][1].location); n = world_to_camera_view(sc, cam, P[q]["nez"].location)
        r[q] = dict(x=round(t.x, 2), regard="droite" if n.x > t.x else "gauche", visible=bool(0 <= t.x <= 1 and t.z > 0))
    return r


res = {}
for e, (hA, hB) in ETATS.items():
    etat(hA, hB)
    tA, tB = (-.6, 0, hA - .05), (.6, 0, hB - .05)
    # côté -Y = côté « bon » (établi) ; côté +Y = axe franchi. Champ sur A : plongée si A domine (caméra à hauteur de B).
    plans = {"E": ((0, -4.6, 1.5), (0, 0, 1.25), 32), "E2": ((0, 3.3, 1.5), (0, 0, 1.25), 24),
             "A1": ((1.0, -1.5, hB), tA, 50), "B1": ((-1.0, -1.5, hA), tB, 50),
             "A2": ((1.0, 1.5, hB), tA, 50), "B2": ((-1.0, 1.5, hA), tB, 50)}
    for nom, (pos, cible, lens) in plans.items():
        cam = camera(pos, cible, lens); k = f"{nom}_{e}"; res[k] = mesure(cam)
        sc.render.filepath = os.path.join(out, f"{k}.png"); bpy.ops.render.render(write_still=True)
# v3 : travelling circulaire qui traverse l'axe pendant que B se lève (50 images = 2 s), autour du centre, rayon 2,6
etat(*ETATS["avant"]); os.makedirs(os.path.join(out, "trav"), exist_ok=True); trav = []
for i in range(50):
    u = i / 49; s = u * u * (3 - 2 * u)  # lissé
    etat(1.65, 1.05 + .9 * s)
    a = math.radians(-20 + 220 * s)  # de -Y (côté établi) à +Y (axe franchi), en passant derrière B (x > 0)
    pos = (2.6 * math.sin(a), -2.6 * math.cos(a), 1.5)
    cam = camera(pos, (0, 0, 1.3), 32); trav.append(dict(i=i, cam=[round(c, 2) for c in pos], **mesure(cam)))
    sc.render.filepath = os.path.join(out, "trav", f"{i:03d}.png"); bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(cam)
res["trav"] = [trav[0], trav[24], trav[49]]
json.dump(res, open(os.path.join(out, "mesures.json"), "w"), indent=1, ensure_ascii=False)
for k, v in res.items():
    print("MESURE", k, v)
