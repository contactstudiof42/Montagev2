# Pièce 01 v1 — Blender 4.2, rendu : blender -b -P v1.py -- <dossier_sortie>
import bpy, sys, math
out = sys.argv[sys.argv.index("--")+1] if "--" in sys.argv else "/tmp/r01/"
sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
sc.render.engine = 'CYCLES'; sc.cycles.samples = 16; sc.cycles.device = 'CPU'
sc.render.resolution_x, sc.render.resolution_y = 640, 360
sc.render.fps = 25; sc.frame_start, sc.frame_end = 1, 200
sc.render.image_settings.file_format = 'PNG'; sc.render.filepath = out + "f_"
sc.view_settings.view_transform = 'Standard'
w = bpy.data.worlds.new("W"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.008, 0.018, 0.04, 1)
bpy.ops.object.text_add(location=(0, 0, 0)); t = bpy.context.object
t.data.body = "souffle"; t.data.align_x = 'CENTER'; t.data.align_y = 'CENTER'
t.data.font = bpy.data.fonts.load("/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf")
m = bpy.data.materials.new("M"); m.use_nodes = True
n = m.node_tree.nodes; n.clear()
em = n.new("ShaderNodeEmission"); em.inputs[0].default_value = (0.92, 0.9, 0.85, 1)
o_ = n.new("ShaderNodeOutputMaterial"); m.node_tree.links.new(em.outputs[0], o_.inputs[0])
t.data.materials.append(m)
bpy.ops.object.camera_add(location=(0, 0, 6)); sc.camera = bpy.context.object
# respiration : échelle 0.9 -> 1.1 -> 0.9, apparition en fondu sur 1 s
for f, s in [(1, 0.9), (100, 1.1), (200, 0.9)]:
    t.scale = (s, s, s); t.keyframe_insert("scale", frame=f)
em.inputs[1].default_value = 0.0; em.inputs[1].keyframe_insert("default_value", frame=1)
em.inputs[1].default_value = 1.0; em.inputs[1].keyframe_insert("default_value", frame=25)
bpy.ops.render.render(animation=True)
