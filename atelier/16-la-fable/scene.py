"""Pièce 16 : blender -b -P scene.py -- R|F sortie.png [lampe_chaude 0|1]"""
import bpy, sys, math, mathutils
a = sys.argv[sys.argv.index("--") + 1:]; mode, out = a[0], a[1]; chaude = len(a) > 2 and a[2] == "1"
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 24; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 480, 270; sc.view_settings.view_transform = "AgX"; sc.render.filepath = out
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; bg = w.node_tree.nodes["Background"]
def mat(n, c, r=0.6, e=0):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*c, 1); b.inputs["Roughness"].default_value = r
    if e: b.inputs["Emission Color"].default_value = (*c, 1); b.inputs["Emission Strength"].default_value = e
    return m
def boite(loc, dim, m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object; o.scale = [d / 2 for d in dim]; o.data.materials.append(m); return o
bois = mat("bois", (0.2, 0.12, 0.06)); tissu = mat("tissu", (0.25, 0.22, 0.3), 0.8)
def mobilier(z0):
    boite((0, 0, z0 + 0.72), (0.9, 0.6, 0.04), bois)
    for dx in (-0.4, 0.4):
        for dy in (-0.25, 0.25): boite((dx, dy, z0 + 0.36), (0.04, 0.04, 0.72), bois)
    for sx in (-0.75, 0.75):   # deux chaises
        boite((sx, 0, z0 + 0.45), (0.4, 0.4, 0.04), bois); boite((sx + 0.19 * (1 if sx > 0 else -1), 0, z0 + 0.75), (0.03, 0.4, 0.6), bois)
        for dx in (-0.17, 0.17):
            for dy in (-0.17, 0.17): boite((sx + dx, dy, z0 + 0.22), (0.03, 0.03, 0.44), bois)
    # silhouette assise sur la chaise de gauche, tournée vers la chaise vide
    bpy.ops.mesh.primitive_cylinder_add(radius=0.16, depth=0.55, location=(-0.72, 0, z0 + 0.75)); bpy.context.object.data.materials.append(tissu)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, location=(-0.68, 0, z0 + 1.13)); bpy.context.object.data.materials.append(mat("peau", (0.6, 0.45, 0.38)))
    # lampe sur la table
    boite((0.15, 0.1, z0 + 0.9), (0.02, 0.02, 0.3), bois)
    bpy.ops.mesh.primitive_cone_add(radius1=0.12, radius2=0.05, depth=0.12, location=(0.15, 0.1, z0 + 1.07)); bpy.context.object.data.materials.append(mat("abat", (1, 0.75, 0.45), 0.5, 3 if chaude else 0.5))
    bpy.ops.object.light_add(type="POINT", location=(0.15, 0.1, z0 + 1.0)); l = bpy.context.object; l.data.energy = 25 if chaude else 4; l.data.color = (1, 0.7, 0.4); l.data.shadow_soft_size = 0.05
if mode == "R":
    bg.inputs[0].default_value = (0.4, 0.45, 0.5, 1); bg.inputs[1].default_value = 0.3
    mobilier(0); boite((0, 0, -0.01), (6, 6, 0.02), mat("sol", (0.2, 0.2, 0.2))); boite((0, 1.0, 1.5), (6, 0.02, 3), mat("mur", (0.42, 0.42, 0.4), 0.9))
    bpy.ops.object.light_add(type="AREA", location=(-2, -0.5, 1.6)); l = bpy.context.object; l.data.energy = 120; l.data.size = 1.5
    l.data.color = (0.8, 0.88, 1); l.rotation_euler = (0, math.radians(-75), 0)
    cam_loc, cible, lens = (1.6, -2.6, 1.5), (0, 0, 0.8), 35
else:
    bg.inputs[0].default_value = (0.002, 0.002, 0.006, 1); bg.inputs[1].default_value = 1
    R = 2.2; bpy.ops.mesh.primitive_uv_sphere_add(radius=R, location=(0, 0, -R), segments=64, ring_count=32)
    bpy.context.object.data.materials.append(mat("roche", (0.35, 0.33, 0.3), 0.95)); bpy.ops.object.shade_smooth()
    mobilier(0)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(6, 14, 3.5)); bpy.context.object.data.materials.append(mat("terre", (0.1, 0.25, 0.6), 0.5, 1.2))
    bpy.ops.object.light_add(type="SUN"); s = bpy.context.object; s.data.energy = 1.2; s.data.color = (0.7, 0.8, 1); s.rotation_euler = (math.radians(60), 0, math.radians(30))
    cam_loc, cible, lens = (2.6, -5.5, 1.6), (0.6, 2, 0.9), 35
    if len(a) > 3 and a[3] == "fil":   # v2 : un téléphone sur la table, son fil descend jusqu'à la Terre
        boite((-0.25, -0.1, 0.77), (0.14, 0.11, 0.06), mat("tel", (0.8, 0.74, 0.6) if len(a) > 4 else (0.03, 0.03, 0.03), 0.3))
        cd = bpy.data.curves.new("fil", "CURVE"); cd.dimensions = "3D"; cd.bevel_depth = 0.008
        sp = cd.splines.new("POLY"); pts = 40; sp.points.add(pts - 1)
        p0 = mathutils.Vector((-0.25, -0.1, 0.74)); p1 = mathutils.Vector((5.75, 13.6, 3.3))
        for k, pt in enumerate(sp.points):
            u = k / (pts - 1); p = p0.lerp(p1, u); p.z -= 2.2 * 4 * u * (1 - u)
            if u < 0.06: p = p0 + (mathutils.Vector((-0.3, -0.3, -0.7)) * (u / 0.06))
            pt.co = (p.x, p.y, p.z, 1)
        o = bpy.data.objects.new("fil", cd); sc.collection.objects.link(o); cd.materials.append(mat("film", (0.6, 0.75, 1.0), 0.4, 0.8) if len(a) > 4 else mat("film", (0.05, 0.05, 0.05), 0.4))
        if len(a) > 4: cd.bevel_depth = 0.012
bpy.ops.object.camera_add(location=cam_loc); c = bpy.context.object; c.data.lens = lens
c.rotation_euler = (mathutils.Vector(cible) - mathutils.Vector(cam_loc)).to_track_quat("-Z", "Y").to_euler(); sc.camera = c
bpy.ops.render.render(write_still=True)
