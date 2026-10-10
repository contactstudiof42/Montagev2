"""Labo whip pan : blender -b -P scene.py -- sortie_dossier/ lieu(0|1) sens(+1|-1) phase(sortie|entree)
Un décor de colonnes colorées autour de la caméra ; la caméra pivote (lacet).
sortie : accélère jusqu à VMAX °/image (30 par défaut) à la fin (fin du plan A) ; entree : part de VMAX °/image et décélère (début du plan B)."""
import bpy, sys, math, random
a = sys.argv[sys.argv.index("--") + 1:]; out, lieu, sens, phase = a[0], int(a[1]), int(a[2]), a[3]
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.samples = 16; sc.cycles.use_denoising = False
sc.render.resolution_x, sc.render.resolution_y = 192, 108; sc.render.fps = 25; sc.frame_start, sc.frame_end = 1, 12
sc.render.use_motion_blur = True; sc.render.motion_blur_shutter = 0.5; sc.render.filepath = out + "f_"
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes["Background"].inputs[1].default_value = 1.0
w.node_tree.nodes["Background"].inputs[0].default_value = (0.5, 0.6, 0.8, 1) if lieu == 0 else (0.9, 0.6, 0.4, 1)
random.seed(lieu)
for k in range(48):   # colonnes autour de la caméra
    ang = 2 * math.pi * k / 48; r = random.uniform(5, 9)
    bpy.ops.mesh.primitive_cube_add(location=(r * math.cos(ang), r * math.sin(ang), 0)); o = bpy.context.object; o.scale = (0.3, 0.3, random.uniform(0.5, 3))
    m = bpy.data.materials.new("m%d" % k); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (random.random(), random.random(), random.random(), 1); o.data.materials.append(m)
bpy.ops.object.light_add(type="SUN"); bpy.context.object.data.energy = 3
bpy.ops.object.camera_add(location=(0, 0, 0.5)); c = bpy.context.object; c.data.lens = 24; sc.camera = c
yaw = 0.0
PROLONGE = __import__("os").environ.get("PROLONGE", "1") == "1"   # clés une image avant et après le plan : flou complet aux bords
for f in (range(0, 14) if PROLONGE else range(1, 13)):
    u = (f - 1) / 11
    VM = float(__import__("os").environ.get("VMAX", "30"))
    v = (2 + (VM - 2) * u ** 2) if phase == "sortie" else (VM - (VM - 2) * (1 - (1 - u) ** 2))   # °/image
    if f != (0 if PROLONGE else 1): yaw += sens * v
    c.rotation_euler = (math.radians(90), 0, math.radians(yaw)); c.keyframe_insert("rotation_euler", frame=f)
for fc in c.animation_data.action.fcurves:
    for kp in fc.keyframe_points: kp.interpolation = "LINEAR"
bpy.ops.render.render(animation=True)
