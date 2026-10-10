"""Labo keying : sujet (sphère grise + fines tiges = « cheveux ») devant un fond vert, à distance D du fond.
blender -b -P scene_vert.py -- <D> <sortie_png> <avec_fond 0|1>
Avec fond 0 : rendu transparent = alpha de vérité terrain."""
import bpy, sys, math
D, out, fond = float(sys.argv[-3]), sys.argv[-2], sys.argv[-1] == "1"
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.samples = 16; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 480, 270; sc.render.film_transparent = not fond
sc.view_settings.view_transform = "Standard"; sc.render.image_settings.color_mode = "RGBA"
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes["Background"].inputs[0].default_value = (0.02, 0.02, 0.02, 1)
def mat(col, em=0):
    m = bpy.data.materials.new("m"); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*col, 1); b.inputs["Roughness"].default_value = 0.6
    if em: b.inputs["Emission Color"].default_value = (*col, 1); b.inputs["Emission Strength"].default_value = em
    return m
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, 0)); bpy.ops.object.shade_smooth()
bpy.context.object.data.materials.append(mat((0.5, 0.45, 0.42)))
for i in range(9):  # fines tiges
    bpy.ops.mesh.primitive_cylinder_add(radius=0.004, depth=0.6, location=(0.45 + 0.03 * i, 0, 0.35), rotation=(0, math.radians(20 + 5 * i), 0))
    bpy.context.object.data.materials.append(mat((0.35, 0.3, 0.25)))
if fond:  # fond vert diffus éclairé (réfléchit sa couleur sur le sujet = débordement)
    bpy.ops.mesh.primitive_plane_add(size=12, location=(0, D + 0.5, 0), rotation=(math.radians(90), 0, 0))
    bpy.context.object.data.materials.append(mat((0.05, 0.6, 0.1), em=1.2))
bpy.ops.object.light_add(type="AREA", location=(-2, -2, 2)); l = bpy.context.object; l.data.energy = 300; l.data.size = 2
l.rotation_euler = (math.radians(55), 0, math.radians(-45))
bpy.ops.object.camera_add(location=(0, -3.2, 0.1), rotation=(math.radians(90), 0, 0)); sc.camera = bpy.context.object
sc.camera.data.lens = 40
sc.render.filepath = out; bpy.ops.render.render(write_still=True)
