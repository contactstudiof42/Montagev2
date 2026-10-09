# Pièce 01 v6 = v5 sans bruit (16 éch. + OIDN). interlettrage mini 0.93 (EB Garamond plus étroite), inspiration plus lumineuse. Police : EB Garamond Italic (OFL) via https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/ebgaramond/EBGaramond-Italic%5Bwght%5D.ttf — 10 s : inspiration 3 s / rétention 4,5 s (le mot se resserre) / relâchement 2,5 s.
# blender -b -P v3.py -- <sortie>
import bpy, sys
out = sys.argv[sys.argv.index("--")+1] if "--" in sys.argv else "/tmp/r01/"
sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o)
sc.render.engine = 'CYCLES'; sc.cycles.samples = 16; sc.cycles.use_denoising = True; sc.cycles.denoiser = 'OPENIMAGEDENOISE'; sc.cycles.device = 'CPU'
sc.render.resolution_x, sc.render.resolution_y = 640, 360
sc.render.fps = 25; sc.frame_start, sc.frame_end = 1, 250
sc.render.image_settings.file_format = 'PNG'; sc.render.filepath = out + "f_"
sc.view_settings.view_transform = 'Standard'
I, H, E = 75, 188, 250   # fin inspiration, fin rétention, fin
def mat_emission(name):
    m = bpy.data.materials.new(name); m.use_nodes = True; m.node_tree.nodes.clear(); return m
# --- fond : plan en dégradé vertical (lumière de surface en haut), intensité = profondeur
bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 0, -1)); p = bpy.context.object
m = mat_emission("Fond"); nt = m.node_tree; n = nt.nodes
tc = n.new("ShaderNodeTexCoord"); sep = n.new("ShaderNodeSeparateXYZ"); cr = n.new("ShaderNodeValToRGB")
em = n.new("ShaderNodeEmission"); out_ = n.new("ShaderNodeOutputMaterial")
cr.color_ramp.elements[0].position = 0.30; cr.color_ramp.elements[0].color = (0.002, 0.007, 0.012, 1)
cr.color_ramp.elements[1].position = 0.75; cr.color_ramp.elements[1].color = (0.018, 0.075, 0.095, 1)
nt.links.new(tc.outputs["Generated"], sep.inputs[0]); nt.links.new(sep.outputs["Y"], cr.inputs[0])
nt.links.new(cr.outputs[0], em.inputs[0]); nt.links.new(em.outputs[0], out_.inputs[0]); p.data.materials.append(m)
st = em.inputs[1]
for f, v in [(1, 0.8), (I, 1.6), (H, 0.30), (E, 0.85)]:
    st.default_value = v; st.keyframe_insert("default_value", frame=f)
# --- texte
bpy.ops.object.text_add(location=(0, -0.35, 0)); t = bpy.context.object
t.data.body = "souffle"; t.data.align_x = 'CENTER'; t.data.align_y = 'CENTER'
t.data.font = bpy.data.fonts.load("/tmp/claude-0/-home-user-Montagev2/3c7db77e-e7d8-5080-a9a8-f5509d8270f4/scratchpad/fonts/EBGaramond-Italic.ttf")
t.data.size = 0.9
m2 = mat_emission("Texte"); nt = m2.node_tree; n = nt.nodes
e2 = n.new("ShaderNodeEmission"); e2.inputs[0].default_value = (0.90, 0.88, 0.83, 1)
tr = n.new("ShaderNodeBsdfTransparent"); mix = n.new("ShaderNodeMixShader"); o2 = n.new("ShaderNodeOutputMaterial")
nt.links.new(tr.outputs[0], mix.inputs[1]); nt.links.new(e2.outputs[0], mix.inputs[2]); nt.links.new(mix.outputs[0], o2.inputs[0])
t.data.materials.append(m2)
for f, v in [(1, 0.0), (55, 1.0), (H, 1.0), (E, 0.55)]:
    mix.inputs[0].default_value = v; mix.inputs[0].keyframe_insert("default_value", frame=f)
# interlettrage : normal -> resserré pendant la rétention -> relâché
for f, v in [(1, 1.0), (I, 1.0), (H, 0.93), (E, 1.07)]:
    t.data.space_character = v; t.data.keyframe_insert("space_character", frame=f)
for f, s in [(1, 0.98), (I, 1.02), (H, 1.02), (E, 1.0)]:
    t.scale = (s, s, s); t.keyframe_insert("scale", frame=f)
for f, y in [(1, -0.35), (H, -0.35), (E, -0.47)]:
    t.location.y = y; t.keyframe_insert("location", index=1, frame=f)
bpy.ops.object.camera_add(location=(0, 0, 6)); sc.camera = bpy.context.object
bpy.ops.render.render(animation=True)
