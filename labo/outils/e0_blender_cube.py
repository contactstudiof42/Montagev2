# E0 : un cube, une caméra, une lumière, rendu PNG en Cycles sur le GPU du Mac.
# Usage : Blender -b --factory-startup -P e0_blender_cube.py -- <sortie.png> [<fichier.blend>]
# Dans le Blender ouvert (MCP) : exec() avec OUT et BLEND définis avant.
import sys, time, bpy

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = globals().get("OUT") or argv[0]
BLEND = globals().get("BLEND") or (argv[1] if len(argv) > 1 else None)

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0), rotation=(0, 0, 0.6))
cube = bpy.context.active_object
cube.name = "E0_Cube"
mat = bpy.data.materials.new("E0_Gris")
mat.use_nodes = True
mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.5, 0.5, 0.5, 1)
cube.data.materials.append(mat)

bpy.ops.object.camera_add(location=(6, -6, 4.5))
cam = bpy.context.active_object
cam.name = "E0_Camera"
track = cam.constraints.new("TRACK_TO")
track.target = cube
scene.camera = cam

bpy.ops.object.light_add(type="AREA", location=(3, -2, 5))
light = bpy.context.active_object
light.name = "E0_Softbox"
light.data.energy = 800
light.data.size = 3

scene.world = bpy.data.worlds.new("E0_Monde")
scene.world.use_nodes = True
scene.world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.02, 0.02, 0.02, 1)

scene.render.engine = "CYCLES"
prefs = bpy.context.preferences.addons["cycles"].preferences
prefs.compute_device_type = "METAL"
prefs.refresh_devices()
for d in prefs.devices:
    d.use = True
scene.cycles.device = "GPU"
scene.cycles.samples = 64
scene.render.resolution_x, scene.render.resolution_y = 960, 540
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.filepath = OUT

t0 = time.time()
bpy.ops.render.render(write_still=True)
duree = time.time() - t0
if BLEND:
    bpy.ops.wm.save_as_mainfile(filepath=BLEND)

result = {
    "version": bpy.app.version_string,
    "engine": scene.render.engine,
    "device": scene.cycles.device,
    "metal": [(d.name, d.type, d.use) for d in prefs.devices],
    "render_s": round(duree, 2),
    "out": OUT,
}
print("E0_RESULT", result)
