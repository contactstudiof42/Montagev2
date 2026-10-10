"""Pièce 23 — chambre de nuit filmée à l'infrarouge (maquette). blender -b -P scene.py -- OUT.png axe|decale"""
import bpy, math, sys
from mathutils import Vector
argv = sys.argv[sys.argv.index("--") + 1:]; OUT, MODE = argv[0], argv[1]
bpy.ops.wm.read_factory_settings(use_empty=True); sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.samples = 32; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 480, 270
sc.view_settings.view_transform = "Standard"   # le capteur IR « voit » linéaire ; le look se fait au grade


def mat(rgb, rough=0.8):
    m = bpy.data.materials.new("m"); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1); b.inputs["Roughness"].default_value = rough; return m


def box(loc, dims, m, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.scale = dims; o.data.materials.append(m)
    if bevel:
        bpy.ops.object.transform_apply(scale=True); mo = o.modifiers.new("b", "BEVEL"); mo.width = bevel; mo.segments = 4
    return o


tissu, bois, mur = mat((0.7, 0.7, 0.7)), mat((0.35, 0.35, 0.35), 0.5), mat((0.5, 0.5, 0.5))
box((0, 0, -0.05), (8, 8, 0.1), mat((0.25, 0.25, 0.25)))               # sol
box((0, -2.0, 1.5), (8, 0.1, 3), mur); box((-2.5, 0, 1.5), (0.1, 8, 3), mur)   # murs
box((0, 0, 0.25), (1.6, 2.1, 0.5), bois, 0.03)                          # sommier
box((0, 0, 0.6), (1.5, 2.0, 0.2), tissu, 0.06)                          # matelas
box((0, -0.85, 0.78), (0.6, 0.35, 0.14), tissu, 0.06)                   # oreiller
# le dormeur sous le drap : une forme couchée sur le côté (bosse épaule-hanche-genoux), drap = subdivision lissée
for loc, dims in (((0.15, -0.45, 0.82), (0.45, 0.5, 0.28)), ((0.2, 0.15, 0.8), (0.5, 0.6, 0.26)), ((0.1, 0.7, 0.75), (0.4, 0.5, 0.18))):
    o = box(loc, dims, tissu, 0.12)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(-0.05, -0.82, 0.93)); bpy.context.object.data.materials.append(mat((0.55, 0.55, 0.55), 0.6))  # tête
box((1.2, -1.5, 0.3), (0.45, 0.45, 0.6), bois, 0.02)                    # table de nuit
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes["Background"].inputs[1].default_value = 0.0
bpy.ops.object.camera_add(); cam = bpy.context.object; sc.camera = cam
cam.location = (2.6, 2.6, 2.1); cam.rotation_euler = (Vector((0, -0.4, 0.6)) - cam.location).to_track_quat("-Z", "Y").to_euler(); cam.data.lens = 26
if MODE == "axe":   # illuminateur intégré à la caméra : projecteur au-dessus de l'objectif
    bpy.ops.object.light_add(type="SPOT", location=cam.location + Vector((0, 0, 0.08))); L = bpy.context.object
    L.rotation_euler = cam.rotation_euler; L.data.energy = 220; L.data.spot_size = math.radians(70); L.data.shadow_soft_size = 0.02
else:               # projecteur IR décalé, haut et latéral, motivé comme une fenêtre ; + un débouchage très faible
    bpy.ops.object.light_add(type="AREA", location=(-2.2, 1.8, 2.4)); L = bpy.context.object
    L.rotation_euler = (Vector((0.1, -0.3, 0.6)) - L.location).to_track_quat("-Z", "Y").to_euler()
    L.data.energy = 260; L.data.size = 0.8
    if MODE == "nuit":  # v2 : la nuit doit rester majoritaire — une bande de « fenêtre » étroite et faible, rasante sur le lit
        L.data.energy = 45; L.data.shape = "RECTANGLE"; L.data.size, L.data.size_y = 0.25, 1.2; L.location = (-2.3, 0.4, 1.3)
        L.rotation_euler = (Vector((0.2, -0.2, 0.7)) - L.location).to_track_quat("-Z", "Y").to_euler()
    if MODE == "nuit3":  # v3 : la fenêtre au pied du lit, côté caméra-gauche, visée sur l'oreiller : le visage reçoit la lumière
        L.data.energy = 40; L.data.shape = "RECTANGLE"; L.data.size, L.data.size_y = 0.25, 1.0; L.location = (-1.2, 2.4, 1.5)
        L.rotation_euler = (Vector((0.0, -0.8, 0.85)) - L.location).to_track_quat("-Z", "Y").to_euler()
    bpy.ops.object.light_add(type="POINT", location=(2.5, 2.0, 1.5)); bpy.context.object.data.energy = 6 if MODE not in ("nuit", "nuit3") else 0.8
sc.render.filepath = OUT; bpy.ops.render.render(write_still=True)
