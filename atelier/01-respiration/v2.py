# Pièce 01 v2 — inspiration 3 s / rétention 3 s / expiration 2 s. blender -b -P v2.py -- <sortie>
import bpy, sys
out = sys.argv[sys.argv.index("--")+1] if "--" in sys.argv else "/tmp/r01/"
sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
sc.render.engine = 'CYCLES'; sc.cycles.samples = 4; sc.cycles.device = 'CPU'
sc.render.resolution_x, sc.render.resolution_y = 640, 360
sc.render.fps = 25; sc.frame_start, sc.frame_end = 1, 200
sc.render.image_settings.file_format = 'PNG'; sc.render.filepath = out + "f_"
sc.view_settings.view_transform = 'Standard'
w = bpy.data.worlds.new("W"); sc.world = w; w.use_nodes = True
bg = w.node_tree.nodes["Background"].inputs[0]
# fond : descend (s'assombrit) pendant la rétention, remonte à l'expiration
for f, c in [(1, (0.010, 0.026, 0.055)), (75, (0.010, 0.026, 0.055)), (150, (0.002, 0.006, 0.016)), (200, (0.008, 0.020, 0.045))]:
    bg.default_value = (*c, 1); bg.keyframe_insert("default_value", frame=f)
bpy.ops.object.text_add(location=(0, -0.35, 0)); t = bpy.context.object
t.data.body = "souffle"; t.data.align_x = 'CENTER'; t.data.align_y = 'CENTER'
t.data.font = bpy.data.fonts.load("/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf")
t.data.size = 0.8
m = bpy.data.materials.new("M"); m.use_nodes = True
nt = m.node_tree; n = nt.nodes; n.clear()
em = n.new("ShaderNodeEmission"); em.inputs[0].default_value = (0.90, 0.88, 0.83, 1)
tr = n.new("ShaderNodeBsdfTransparent"); mix = n.new("ShaderNodeMixShader")
o_ = n.new("ShaderNodeOutputMaterial")
nt.links.new(tr.outputs[0], mix.inputs[1]); nt.links.new(em.outputs[0], mix.inputs[2]); nt.links.new(mix.outputs[0], o_.inputs[0])
t.data.materials.append(m)
fac = mix.inputs[0]
for f, v in [(1, 0.0), (60, 1.0), (150, 1.0), (200, 0.0)]:
    fac.default_value = v; fac.keyframe_insert("default_value", frame=f)
bpy.ops.object.camera_add(location=(0, 0, 6)); sc.camera = bpy.context.object
# échelle : 0.97 -> 1.03 (inspiration), immobile (rétention), relâchement plus rapide
for f, s in [(1, 0.97), (75, 1.03), (150, 1.03), (200, 0.98)]:
    t.scale = (s, s, s); t.keyframe_insert("scale", frame=f)
# léger affaissement vertical à l'expiration (on « lâche »)
for f, y in [(1, -0.35), (150, -0.35), (200, -0.45)]:
    t.location.y = y; t.keyframe_insert("location", index=1, frame=f)
bpy.ops.render.render(animation=True)
