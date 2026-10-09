"""Pièce 02 « Étincelle » — scène Blender (lancer : blender -b -P scene.py -- jobs.json outdir)
jobs.json : liste de [camera, frame_start, frame_end] à rendre (images PNG cam_FFFF.png).
Plateau : sol sombre, lumière cyan-vert froide ; pendule (tic toutes les 15 images), cube qui tombe,
sphères qui roulent, allumette qui s'allume à l'image 200 (seule source chaude)."""
import bpy, json, math, sys, os
argv = sys.argv[sys.argv.index("--") + 1:]
jobs = json.load(open(argv[0])); out = argv[1]; os.makedirs(out, exist_ok=True)
RES = (270, 480) if len(argv) < 3 else tuple(map(int, argv[2].split("x")))
IGN = 200  # image d'allumage

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.samples = 12; sc.cycles.use_denoising = True
sc.cycles.device = "CPU"; sc.render.resolution_x, sc.render.resolution_y = RES
sc.render.fps = 30; sc.render.use_motion_blur = True; sc.render.motion_blur_shutter = 0.5
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Punchy"
sc.render.image_settings.file_format = "PNG"
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.0008, 0.0025, 0.0025, 1)

def mat(name, col, metal=0.0, rough=0.4, emit=None):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*col, 1); b.inputs["Metallic"].default_value = metal
    b.inputs["Roughness"].default_value = rough
    return m

def obj(o, m): o.data.materials.append(m); return o

sol = mat("sol", (0.015, 0.018, 0.018), 0.3, 0.35)
chrome = mat("chrome", (0.7, 0.75, 0.75), 1.0, 0.12)
noir = mat("noir_mat", (0.02, 0.02, 0.02), 0.0, 0.5)
bois = mat("bois", (0.12, 0.09, 0.06), 0.0, 0.7)
tete = mat("tete", (0.10, 0.025, 0.02), 0.0, 0.6)

bpy.ops.mesh.primitive_plane_add(size=60); obj(bpy.context.object, sol)

# Lumière froide : grande area cyan-vert rasante + un liseré
def area(name, loc, rot, col, power, size):
    bpy.ops.object.light_add(type="AREA", location=loc, rotation=rot)
    l = bpy.context.object; l.data.color = col; l.data.energy = power; l.data.size = size; return l
area("cle", (-4, -3, 5), (math.radians(50), 0, math.radians(-50)), (0.35, 0.9, 0.8), 2500, 3)
# Bandes lumineuses (hors champ) : donnent des reflets lisibles au chrome, sinon il reflète du noir
for x, y in [(-6, 2), (2, 5), (6, -2)]:
    bpy.ops.mesh.primitive_plane_add(size=1, location=(x, y, 2.5)); bd = bpy.context.object
    bd.scale = (0.25, 4, 1); bd.rotation_euler = (0, math.radians(90), math.atan2(-y, -x))
    em = mat("bande", (0, 0, 0)); eb = em.node_tree.nodes["Principled BSDF"]
    eb.inputs["Emission Color"].default_value = (0.4, 1.0, 0.9, 1); eb.inputs["Emission Strength"].default_value = 6
    bd.data.materials.append(em); bd.visible_camera = False
area("rim", (4, 6, 2.5), (math.radians(-70), 0, math.radians(150)), (0.5, 0.85, 1.0), 400, 1.5)

# Pendule (pivot en (0,0,3)) : tic à chaque passage au point bas, toutes les 15 images
bpy.ops.object.empty_add(location=(0, 0, 3)); piv = bpy.context.object
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=2.4, location=(0, 0, 1.8)); tige = obj(bpy.context.object, chrome)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.22, location=(0, 0, 0.55)); bpy.ops.object.shade_smooth(); bob = obj(bpy.context.object, chrome)
for o in (tige, bob): o.parent = piv; o.matrix_parent_inverse = piv.matrix_world.inverted()
for f in range(0, 320):
    piv.rotation_euler = (0, math.radians(32) * math.sin(2 * math.pi * f / 30), 0)
    piv.keyframe_insert("rotation_euler", frame=f)

# Cube qui tombe (pose au sol à l'image 10, petit rebond)
acier = mat("acier", (0.35, 0.4, 0.4), 1.0, 0.38)
bpy.ops.mesh.primitive_cube_add(size=0.6, location=(3, 0, 0.3)); cube = obj(bpy.context.object, acier)
cube.modifiers.new("b", "BEVEL").width = 0.03
for f, z, r in [(0, 3.5, 0), (10, 0.3, 25), (13, 0.55, 28), (16, 0.3, 30), (40, 0.3, 30)]:
    cube.location.z = z; cube.rotation_euler.z = math.radians(r)
    cube.keyframe_insert("location", frame=f); cube.keyframe_insert("rotation_euler", frame=f)
for fc in cube.animation_data.action.fcurves:
    for k in fc.keyframe_points: k.interpolation = "QUAD"; k.easing = "EASE_IN"

# Trois sphères qui roulent vite (images 40 à 64)
for i in range(3):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.18, location=(-8, 0, 0.18)); bpy.ops.object.shade_smooth()
    s = obj(bpy.context.object, chrome); s.location.y = -3 + i * 0.5
    s.location.x = -6; s.keyframe_insert("location", frame=40 + i * 4)
    s.location.x = 4; s.keyframe_insert("location", frame=60 + i * 4)
    for fc in s.animation_data.action.fcurves:
        for k in fc.keyframe_points: k.interpolation = "LINEAR"

# Allumette (en (-3, 0.0)) : tête sombre, puis feu à IGN
bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=0.9, location=(-3, 0.5, 0.45)); obj(bpy.context.object, bois)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.05, location=(-3, 0.5, 0.92)); bpy.ops.object.shade_smooth()
th = obj(bpy.context.object, tete)
b = th.data.materials[0].node_tree.nodes["Principled BSDF"]
b.inputs["Emission Color"].default_value = (1.0, 0.35, 0.06, 1)
s_em = b.inputs["Emission Strength"]
for f, v in [(IGN - 1, 0), (IGN, 8), (IGN + 3, 2.5), (IGN + 6, 3.5), (IGN + 30, 3)]:
    s_em.default_value = v; s_em.keyframe_insert("default_value", frame=f)
bpy.ops.object.light_add(type="POINT", location=(-3, 0.5, 1.02)); feu = bpy.context.object
feu.data.color = (1.0, 0.45, 0.12); feu.data.shadow_soft_size = 0.04
import random; random.seed(3)
for f in range(IGN - 1, 320):
    v = 0 if f < IGN else (400 if f == IGN else 120 + random.uniform(-25, 25))
    feu.data.energy = v; feu.data.keyframe_insert("energy", frame=f)
# Flamme : petit cône émissif
bpy.ops.mesh.primitive_cone_add(radius1=0.03, depth=0.14, location=(-3, 0.5, 1.02)); fl = bpy.context.object
fm = mat("flamme", (0, 0, 0)); fb = fm.node_tree.nodes["Principled BSDF"]
fb.inputs["Emission Color"].default_value = (1.0, 0.55, 0.15, 1)
fl.data.materials.append(fm)
for f, sc_ in [(IGN - 1, 0.0), (IGN, 1.6), (IGN + 4, 1.0)]:
    fl.scale = (sc_, sc_, sc_); fl.keyframe_insert("scale", frame=f)
fb.inputs["Emission Strength"].default_value = 12

def cam(name, loc, target, lens):
    bpy.ops.object.camera_add(location=loc); c = bpy.context.object; c.name = name; c.data.lens = lens
    d = c.constraints.new("TRACK_TO"); bpy.ops.object.empty_add(location=target); d.target = bpy.context.object
    return c
CAMS = {
    "pendule": cam("pendule", (0.6, -2.4, 0.35), (0, 0, 0.8), 45),
    "cube": cam("cube", (3.7, -2.0, 0.2), (3, 0, 0.45), 35),
    "spheres": cam("spheres", (0.4, -4.0, 0.12), (-0.5, -2.5, 0.2), 24),
    "allumette": cam("allumette", (-3.25, -0.6, 0.95), (-3, 0.5, 0.85), 85),
    "large": cam("large", (-2.2, -3.6, 1.1), (-2.6, 0.4, 0.55), 30),
}
for c, a, b_ in jobs:
    sc.camera = CAMS[c]; sc.frame_start, sc.frame_end = a, b_
    sc.render.filepath = os.path.join(out, f"{c}_####")
    bpy.ops.render.render(animation=True)
