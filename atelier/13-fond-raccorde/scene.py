"""Pièce 13 : une tête abstraite (A ou B) devant un mur de couleur réglable, lumière clé réglable. Une image par plan.
blender -b -P scene.py -- params.json sortie.png
params : {"perso": "A"|"B", "mur": [r,g,b] (linéaire), "cle": [r,g,b], "res": [480,270]}"""
import bpy, json, math, sys
from mathutils import Vector
argv = sys.argv[sys.argv.index("--") + 1:]; P = json.load(open(argv[0])); out = argv[1]
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.samples = 16; sc.cycles.use_denoising = True; sc.cycles.seed = 3
sc.render.resolution_x, sc.render.resolution_y = P.get("res", [480, 270])
sc.view_settings.view_transform = "AgX"; sc.render.filepath = out
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (.03, .03, .03, 1)
def mat(c, r=.5, sss=0.0):
    m = bpy.data.materials.new("m"); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*c, 1); b.inputs["Roughness"].default_value = r; return m
A = P.get("perso", "A") == "A"; s = 1 if A else -1   # A regarde vers +x (droite de l'écran), B vers -x
peau = mat((0.62, 0.40, 0.30) if A else (0.55, 0.36, 0.28), 0.55)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, location=(0, 0, 1.6)); bpy.ops.object.shade_smooth()
bpy.context.object.scale = (0.9, 0.95, 1.15); bpy.context.object.data.materials.append(peau)
bpy.ops.mesh.primitive_cone_add(radius1=0.025, depth=0.06, location=(s * 0.105, -0.03, 1.6), rotation=(0, s * math.radians(90), 0))
bpy.context.object.data.materials.append(peau)
bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.2, location=(0, 0, 1.45)); bpy.context.object.data.materials.append(peau)
bpy.ops.mesh.primitive_cylinder_add(radius=0.18, depth=0.6, location=(0, 0, 1.08)); bpy.ops.object.shade_smooth()
bpy.context.object.data.materials.append(mat((0.08, 0.08, 0.09) if A else (0.2, 0.18, 0.15), .7))
bpy.ops.mesh.primitive_plane_add(size=6, location=(-s * 0.6, 1.6, 1.5), rotation=(math.radians(90), 0, 0))
bpy.context.object.data.materials.append(mat(tuple(P.get("mur", [0.3, 0.3, 0.3])), .95))
# clé : 3/4 face côté regard ; contre faible
bpy.ops.object.light_add(type="AREA", location=(s * 1.0, -1.2, 2.0)); L = bpy.context.object
L.data.energy = P.get("cle_w", 45); L.data.size = 1.0; L.data.color = tuple(P.get("cle", [1, 1, 1]))
L.rotation_euler = (Vector((0, 0, 1.6)) - L.location).to_track_quat("-Z", "Y").to_euler()
bpy.ops.object.light_add(type="AREA", location=(0, 1.0, 1.4)); M = bpy.context.object
M.data.energy = 30; M.data.size = 3; M.rotation_euler = (Vector((0, 1.6, 1.5)) - M.location).to_track_quat("-Z", "Y").to_euler()
# caméra : légèrement du côté opposé au regard (champ/contrechamp), visage décentré vers le regard
cam = Vector((-s * 0.35, -1.3, 1.62)); bpy.ops.object.camera_add(location=cam); c = bpy.context.object
c.data.lens = 55; c.rotation_euler = (Vector((s * 0.12, 0, 1.55)) - cam).to_track_quat("-Z", "Y").to_euler()
sc.camera = c
if P.get("masque"):  # masque du visage : tout noir sauf la peau en émission blanche
    sc.view_settings.view_transform = "Standard"; sc.cycles.use_denoising = False; sc.cycles.samples = 4
    w.node_tree.nodes["Background"].inputs[1].default_value = 0
    for m in bpy.data.materials:
        b = m.node_tree.nodes["Principled BSDF"]; b.inputs["Base Color"].default_value = (0, 0, 0, 1)
        b.inputs["Roughness"].default_value = 1; b.inputs["Specular IOR Level"].default_value = 0
    b = peau.node_tree.nodes["Principled BSDF"]; b.inputs["Emission Color"].default_value = (1, 1, 1, 1); b.inputs["Emission Strength"].default_value = 5
    for o in bpy.data.objects:
        if o.type == "LIGHT": o.data.energy = 0
bpy.ops.render.render(write_still=True)
