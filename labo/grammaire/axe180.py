"""Labo grammaire : la règle des 180°, mesurée.
blender -b -P axe180.py -- sortie_dir
Deux « personnages » (cylindres avec un nez qui indique le regard) se font face sur l'axe X : A (orange) à
gauche, B (bleu) à droite. Ligne d'action = l'axe X. Quatre caméras :
  E   plan d'ensemble, côté -Y ;
  A1  champ sur A, côté -Y (bon côté) ;   B1 contrechamp sur B, côté -Y (bon côté) ;
  A2  champ sur A, côté +Y (axe franchi).
Pour chaque caméra : direction du regard À L'ÉCRAN (signe de x_nez - x_tête dans le cadre) et position
horizontale du personnage. Règle : dans un champ / contrechamp, les regards doivent être opposés à l'écran.
"""
import bpy, json, math, os, sys
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
out = sys.argv[sys.argv.index("--") + 1]; os.makedirs(out, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.samples = 8; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 320, 180
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (.35, .37, .4, 1)


def mat(c):
    m = bpy.data.materials.new("m"); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*c, 1); return m


bpy.ops.mesh.primitive_plane_add(size=12); bpy.context.object.data.materials.append(mat((.2, .2, .2)))
perso = {}
for nom, x, sens, col in (("A", -.6, 1, (.9, .35, .05)), ("B", .6, -1, (.1, .3, .9))):
    bpy.ops.mesh.primitive_cylinder_add(radius=.18, depth=1.5, location=(x, 0, .75))
    bpy.context.object.data.materials.append(mat(col))
    bpy.ops.mesh.primitive_uv_sphere_add(radius=.16, location=(x, 0, 1.65))
    bpy.context.object.data.materials.append(mat(col))
    bpy.ops.mesh.primitive_cone_add(radius1=.06, depth=.22, location=(x + sens * .2, 0, 1.65),
                                    rotation=(0, math.radians(90 * sens), 0))
    bpy.context.object.data.materials.append(mat((1, 1, 1)))
    perso[nom] = dict(tete=Vector((x, 0, 1.65)), nez=Vector((x + sens * .31, 0, 1.65)))
bpy.ops.object.light_add(type="SUN", rotation=(math.radians(40), 0, math.radians(30)))
bpy.context.object.data.energy = 3

CAMS = {  # nom : (position, cible, personnage cadré)
    "E": ((0, -4.2, 1.5), (0, 0, 1.2), None),
    "A1": ((1.1, -1.3, 1.6), (-.6, 0, 1.5), "A"),
    "B1": ((-1.1, -1.3, 1.6), (.6, 0, 1.5), "B"),
    "A2": ((1.1, 1.3, 1.6), (-.6, 0, 1.5), "A"),
    # amorces (par-dessus l'épaule) : on voit l'épaule de l'autre au bord du cadre
    "A1amorce": ((1.25, -.55, 1.75), (-.6, 0, 1.55), "A"),
    "B1amorce": ((-1.25, -.55, 1.75), (.6, 0, 1.55), "B"),
    "A2amorce": ((1.25, .55, 1.75), (-.6, 0, 1.55), "A"),
}
res = {}
for nom, (pos, cible, p) in CAMS.items():
    bpy.ops.object.camera_add(location=pos); cam = bpy.context.object
    d = Vector(cible) - Vector(pos); cam.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    cam.data.lens = 35 if nom == "E" else 50
    sc.camera = cam; bpy.context.view_layer.update()
    r = {}
    for q in ("A", "B"):
        t = world_to_camera_view(sc, cam, perso[q]["tete"]); n = world_to_camera_view(sc, cam, perso[q]["nez"])
        r[q] = dict(x_ecran=round(t.x, 3), regard="droite" if n.x > t.x else "gauche", visible=0 <= t.x <= 1 and t.z > 0)
    res[nom] = dict(cadre=p, **r)
    sc.render.filepath = os.path.join(out, f"{nom}.png"); bpy.ops.render.render(write_still=True)
json.dump(res, open(os.path.join(out, "mesures.json"), "w"), indent=1, ensure_ascii=False)
for k, v in res.items():
    print("MESURE", k, v)
