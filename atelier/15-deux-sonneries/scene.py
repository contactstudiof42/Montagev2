"""Pièce 15 : téléphone fixe, main qui décroche. blender -b -P scene.py -- sortie_dossier fps
Rend la phase de décroché (1,6 s) à la cadence demandée, 320x180, Cycles 8 éch. Images : f0000.png..."""
import bpy, sys, math, os, mathutils
argv = sys.argv[sys.argv.index("--") + 1:]; out = argv[0]; fps = int(argv[1]); os.makedirs(out, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 8
sc.cycles.use_denoising = True; sc.cycles.seed = 7
sc.render.resolution_x, sc.render.resolution_y = 320, 180
sc.view_settings.view_transform = "Standard"; sc.render.image_settings.file_format = "PNG"
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.05, 0.06, 1)
def mat(n, c, r=0.5):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*c, 1); b.inputs["Roughness"].default_value = r; return m
def boite(loc, dim, m, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(location=loc, rotation=rot); o = bpy.context.object
    o.scale = [d / 2 for d in dim]; o.data.materials.append(m); return o
boite((0, 0, -0.02), (3, 3, 0.04), mat("table", (0.25, 0.14, 0.07), 0.4))
boite((0, 0.6, 0.5), (3, 0.02, 1.2), mat("mur", (0.5, 0.42, 0.33), 0.9))
noir = mat("bakelite", (0.03, 0.03, 0.03), 0.25); creme = mat("cadran", (0.8, 0.75, 0.62), 0.4)
peau = mat("peau", (0.62, 0.42, 0.33), 0.55)
base = boite((0, 0.1, 0.04), (0.22, 0.18, 0.08), noir)
bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.01, location=(0, 0.05, 0.085)); bpy.context.object.data.materials.append(creme)
# combiné = parent vide + barre + deux écouteurs
bpy.ops.object.empty_add(location=(0, 0.13, 0.11)); comb = bpy.context.object
for x in (-0.09, 0.0, 0.09):
    o = boite((x, 0.13, 0.11 if x == 0 else 0.1), (0.07 if x else 0.16, 0.05, 0.035 if x == 0 else 0.05), noir)
    o.parent = comb; o.matrix_parent_inverse = comb.matrix_world.inverted()
main = boite((0.6, 0.1, 0.16), (0.2, 0.09, 0.07), peau)        # la main (bloc) hors champ à droite
pouce = boite((0.55, 0.05, 0.13), (0.05, 0.03, 0.03), peau); pouce.parent = main; pouce.matrix_parent_inverse = main.matrix_world.inverted()
# cordon : courbe fine reconstruite à chaque image
cd = bpy.data.curves.new("cordon", "CURVE"); cd.dimensions = "3D"; cd.bevel_depth = 0.004
sp = cd.splines.new("POLY"); sp.points.add(7); cordon = bpy.data.objects.new("cordon", cd)
sc.collection.objects.link(cordon); cd.materials.append(noir)
bpy.ops.object.light_add(type="AREA", location=(-0.6, -0.5, 0.9)); l = bpy.context.object; l.data.energy = 22; l.data.size = 0.5
l.data.color = (1.0, 0.85, 0.65); l.rotation_euler = mathutils.Vector((0.6, 0.6, -0.9)).to_track_quat("-Z", "Y").to_euler()
bpy.ops.object.camera_add(location=(0.15, -0.75, 0.42)); c = bpy.context.object; c.data.lens = 40
c.rotation_euler = mathutils.Vector((-0.05 - 0.15, 0.1 + 0.75, 0.1 - 0.42)).to_track_quat("-Z", "Y").to_euler(); sc.camera = c
def ease(t): t = min(max(t, 0), 1); return t * t * (3 - 2 * t)
D = 1.6; n = round(D * fps)
for i in range(n):
    t = i / fps
    a = ease(t / 0.5)                    # 0-0,5 s : la main arrive sur le combiné
    b = ease((t - 0.6) / 0.8)            # 0,6-1,4 s : levée
    main.location = (0.6 - 0.46 * a, 0.13, 0.15 + 0.3 * b)
    main.rotation_euler = (0, -0.3 * b, 0)
    comb.location = (0.0, 0.13, 0.11 + 0.3 * b); comb.rotation_euler = (0, -0.3 * b, 0)
    bpy.context.view_layer.update()
    p0 = mathutils.Vector((0.11, 0.12, 0.05)); p3 = comb.matrix_world @ mathutils.Vector((0.09, 0.13, 0.08))
    for k, pt in enumerate(sp.points):      # chaînette approchée : interpolation + affaissement
        u = k / 7; p = p0.lerp(p3, u); p.z -= 0.06 * 4 * u * (1 - u) * (1 - 0.6 * b); p.x += 0.05 * 4 * u * (1 - u)
        pt.co = (p.x, p.y, max(p.z, 0.005), 1)
    sc.render.filepath = os.path.join(out, f"f{i:04d}.png"); bpy.ops.render.render(write_still=True)
