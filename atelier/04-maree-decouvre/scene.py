"""Pièce 04 « Ce que la marée découvre » — scène Blender.
Lancer : blender -b -P scene.py -- params.json outdir
params.json : {"res": [480, 270], "samples": 8, "frames": [1, 250],
               "cam": {"loc": [x,y,z], "rot_deg": [rx,ry,rz], "lens": 35},
               "water": [[frame, z], ...]}   # courbe de hauteur d'eau (interpolation Bézier)
Plateau : estran de sable ondulé, une chaise de bistrot debout, une chaîne vers un anneau, ciel couvert gris.
"""
import bpy, json, math, sys, os
argv = sys.argv[sys.argv.index("--") + 1:]
P = json.load(open(argv[0])); out = argv[1]; os.makedirs(out, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"
sc.cycles.samples = P.get("samples", 8); sc.cycles.use_denoising = True
sc.cycles.max_bounces = 4; sc.cycles.transmission_bounces = 4
sc.render.resolution_x, sc.render.resolution_y = P.get("res", [480, 270])
sc.render.fps = 25; sc.frame_start, sc.frame_end = P.get("frames", [1, 250])
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = P.get("look", "AgX - Base Contrast")
sc.render.image_settings.file_format = "PNG"
sc.render.filepath = os.path.join(out, "####")

# Ciel couvert : fond gris-bleu uniforme, c'est la seule lumière (pas de soleil : pas de « chaleur méritée »)
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (*P.get("sky", [0.42, 0.47, 0.52]), 1)
w.node_tree.nodes["Background"].inputs[1].default_value = P.get("sky_strength", 1.0)

def mat(name, col, rough=0.5, metal=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*col, 1); b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    return m

def put(o, m): o.data.materials.append(m); return o

# Sable mouillé : plan subdivisé + déplacement par texture d'ondes (rides de sable)
bpy.ops.mesh.primitive_plane_add(size=P.get("sand_size", 200)); sable = bpy.context.object
mod = sable.modifiers.new("sub", "SUBSURF"); mod.subdivision_type = "SIMPLE"; mod.levels = mod.render_levels = P.get("sand_levels", 8)
tex = bpy.data.textures.new("rides", "WOOD"); tex.wood_type = "BANDNOISE"; tex.noise_scale = 0.35; tex.turbulence = 3
d = sable.modifiers.new("disp", "DISPLACE"); d.texture = tex; d.strength = 0.04
put(sable, mat("sable", (0.20, 0.18, 0.15), 0.35))
# pente douce vers le large (y positif = large) : l'eau découvre d'abord le premier plan
sable.rotation_euler = (math.radians(-1.2), 0, 0)

rouille = mat("rouille", (0.11, 0.05, 0.03), 0.8, 0.3)
bois = mat("bois", (0.05, 0.03, 0.02), 0.7)

# Chaise de bistrot (en mètres) posée en (0, 6, 0)
CX, CY = P.get("chair", [0.0, 6.0])
def boite(loc, dim, m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.object
    o.scale = (dim[0] / 2, dim[1] / 2, dim[2] / 2); return put(o, m)
for dx in (-0.2, 0.2):
    for dy in (-0.2, 0.2):
        bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=0.46, location=(CX + dx, CY + dy, 0.23)); put(bpy.context.object, rouille)
boite((CX, CY, 0.47), (0.44, 0.44, 0.03), bois)
for dx in (-0.2, 0.2):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.016, depth=0.42, location=(CX + dx, CY + 0.21, 0.69)); put(bpy.context.object, rouille)
boite((CX, CY + 0.21, 0.82), (0.42, 0.025, 0.12), bois)
# Tout ce qui est posé suit la pente du sable
PENTE = math.radians(1.2)
def sol(y): return -math.tan(PENTE) * y
for o in bpy.data.objects:
    if o is not sable: o.location.z += sol(CY)

# Chaîne : maillons toriques le long d'une courbe au sol, de la chaise vers un anneau au premier plan
def maillon(x, y, z, ang, k):
    bpy.ops.mesh.primitive_torus_add(major_radius=0.05, minor_radius=0.012, location=(x, y, z),
                                     rotation=(math.radians(90) if k % 2 else 0, 0, ang))
    o = bpy.context.object; o.scale = (1.0, 0.6, 1.0); put(o, rouille)
AX, AY = P.get("ring", [-1.2, 2.5])
n = 60
for k in range(n):
    t = k / (n - 1)
    x = CX - 0.2 + (AX - CX + 0.2) * t + 0.35 * math.sin(t * math.pi)
    y = CY - 0.2 + (AY - CY + 0.2) * t
    z = 0.06 * (1 - t) ** 3 + 0.012  # remonte vers le pied de la chaise
    ang = math.atan2(AY - CY, AX - CX)
    maillon(x, y, z + sol(y), ang, k)
bpy.ops.mesh.primitive_torus_add(major_radius=0.12, minor_radius=0.02, location=(AX, AY, 0.02 + sol(AY))); put(bpy.context.object, rouille)

# Eau : plan à hauteur animée, verre d'eau sombre, rides par bump d'ondes
bpy.ops.mesh.primitive_plane_add(size=300); eau = bpy.context.object
me = bpy.data.materials.new("eau"); me.use_nodes = True; nt = me.node_tree
b = nt.nodes["Principled BSDF"]
b.inputs["Base Color"].default_value = (*P.get("water_col", [0.06, 0.09, 0.10]), 1)
b.inputs["Roughness"].default_value = 0.06; b.inputs["IOR"].default_value = 1.33
b.inputs["Transmission Weight"].default_value = P.get("transmission", 0.5)
wave = nt.nodes.new("ShaderNodeTexWave"); wave.inputs["Scale"].default_value = 1.2
wave.inputs["Distortion"].default_value = 6
bump = nt.nodes.new("ShaderNodeBump"); bump.inputs["Strength"].default_value = 0.08
nt.links.new(wave.outputs["Fac"], bump.inputs["Height"]); nt.links.new(bump.outputs["Normal"], b.inputs["Normal"])
# les rides avancent : la phase de l'onde est animée
for f, ph in ((sc.frame_start, 0.0), (sc.frame_end, P.get("wave_phase", 6.0))):
    wave.inputs["Phase Offset"].default_value = ph; wave.inputs["Phase Offset"].keyframe_insert("default_value", frame=f)
eau.data.materials.append(me)
for f, z in P["water"]:
    eau.location.z = z; eau.keyframe_insert("location", index=2, frame=f)
for fc in (eau.animation_data.action.fcurves if eau.animation_data else []):
    for kp in fc.keyframe_points:
        kp.interpolation = P.get("interp", "BEZIER")

# v5 : volume sous-marin (absorption + diffusion vert-gris) qui suit la surface : turbidité crédible vue de dessous
if P.get("underwater_volume"):
    bpy.ops.mesh.primitive_cube_add(size=1); vol = bpy.context.object
    vol.scale = (40, 40, 1.5); vol.parent = eau; vol.location = (0, 0, -0.75 - 0.002)  # cube de 1 m mis à l échelle 1,5 : demi-hauteur 0,75
    mv = bpy.data.materials.new("eau_volume"); mv.use_nodes = True; nv = mv.node_tree
    nv.nodes.remove(nv.nodes["Principled BSDF"]); pv = nv.nodes.new("ShaderNodeVolumePrincipled")
    pv.inputs["Color"].default_value = (0.35, 0.45, 0.40, 1); pv.inputs["Density"].default_value = P["underwater_volume"]
    pv.inputs["Absorption Color"].default_value = (0.6, 0.75, 0.7, 1)
    nv.links.new(pv.outputs["Volume"], nv.nodes["Material Output"].inputs["Volume"]); vol.data.materials.append(mv)
    sc.cycles.volume_step_rate = 4

# Caméra
C = P["cam"]
bpy.ops.object.camera_add(location=C["loc"], rotation=[math.radians(a) for a in C["rot_deg"]])
cam = bpy.context.object; cam.data.lens = C.get("lens", 35); sc.camera = cam

bpy.ops.render.render(animation=True)
