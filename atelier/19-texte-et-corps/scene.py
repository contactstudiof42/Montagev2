"""Pièce 19 : blender -b -P scene.py -- PLAN DOSSIER
PLAN ∈ large, mains, gestes (v4), face, vitrine, porte, escalier, rue-vide. 21 images à 12 i/s (1,75 s = un vers), 480×270, Cycles."""
import bpy, sys, math, os
from mathutils import Vector
a = sys.argv[sys.argv.index("--") + 1:]; plan, out = a[0], a[1]
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = int(os.environ.get("SPP", "16")); sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = 480, 270; sc.view_settings.view_transform = "AgX"; sc.render.fps = 12
sc.frame_start, sc.frame_end = 1, 21; sc.render.filepath = out + "/"; sc.render.image_settings.file_format = "PNG"
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.02, 0.025, 0.04, 1); w.node_tree.nodes["Background"].inputs[1].default_value = 0.2
def mat(n, c, r=0.8, em=None, es=0, metal=0):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*c, 1); b.inputs["Roughness"].default_value = r; b.inputs["Metallic"].default_value = metal
    if em: b.inputs["Emission Color"].default_value = (*em, 1); b.inputs["Emission Strength"].default_value = es
    return m
def boite(loc, dim, m, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(location=loc, rotation=rot); o = bpy.context.object; o.scale = [d / 2 for d in dim]; o.data.materials.append(m); return o
SODIUM, LED = (1.0, 0.55, 0.22), (0.75, 0.85, 1.0)
boite((0, 40, -0.05), (8, 100, 0.1), mat("bitume", (0.08, 0.08, 0.09), 0.35))
for sx in (-5.5, 5.5): boite((sx, 40, 0.05), (3, 100, 0.1), mat("trottoir", (0.22, 0.21, 0.2), 0.9))
facade = mat("facade", (0.18, 0.17, 0.17), 0.95)
for sx in (-8.5, 8.5): boite((sx, 40, 6), (3, 100, 12), facade)
for i in range(6):   # lampadaires sodium alternés, la palette « Joker » en fond
    y = 6 + 12 * i; x = 4.6 if i % 2 else -4.6; s = -1 if x > 0 else 1
    boite((x, y, 3), (0.12, 0.12, 6), mat(f"m{i}", (0.1, 0.1, 0.1)))
    boite((x + s * 1.0, y, 5.92), (0.5, 0.25, 0.08), mat(f"t{i}", (0.05, 0.05, 0.05), 0.4, SODIUM, 30))
    bpy.ops.object.light_add(type="SPOT", location=(x + s * 1.0, y, 5.85)); L = bpy.context.object
    L.data.energy = 1500; L.data.color = SODIUM; L.data.spot_size = math.radians(120); L.data.spot_blend = 0.6
veste = mat("veste", (0.1, 0.1, 0.12), 0.9); peau = mat("peau", (0.45, 0.32, 0.26), 0.6)
def cyl(r, d, loc, rot=(0, 0, 0), m=None):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=d, location=loc, rotation=rot); o = bpy.context.object; o.data.materials.append(m or veste); return o
def sphere(r, loc, m, sc_=(1, 1, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc); o = bpy.context.object; o.scale = sc_; o.data.materials.append(m); bpy.ops.object.shade_smooth(); return o
def personnage(x, y, yaw=0.0, yeux=False):
    """Silhouette ; yaw = rotation autour de Z (0 = regarde vers -Y, la caméra par défaut). Rend un parent vide."""
    bpy.ops.object.empty_add(location=(x, y, 0)); p = bpy.context.object
    parts = [cyl(0.075, 0.85, (dx, 0, 0.43)) for dx in (-0.09, 0.09)]
    parts += [cyl(0.19, 0.62, (0, 0, 1.17)), cyl(0.06, 0.5, (0, 0, 1.45), (0, math.radians(90), 0))]
    parts += [cyl(0.05, 0.55, (s * 0.24, 0, 1.12)) for s in (-1, 1)]
    parts.append(sphere(0.12, (0, 0, 1.66), peau, (0.9, 1, 1.15)))
    if yeux: parts += [sphere(0.018, (s * 0.04, -0.105, 1.69), mat("oeil", (0.01, 0.01, 0.01), 0.2)) for s in (-1, 1)]
    for o in parts: o.parent = p
    p.rotation_euler = (0, 0, yaw); return p
def camera(loc, cible, lens=35, fin=None, ouverture=None, mise_au_point=None):
    bpy.ops.object.camera_add(location=loc); c = bpy.context.object; c.data.lens = lens; sc.camera = c
    def vise(l): c.location = l; c.rotation_euler = (Vector(cible) - Vector(l)).to_track_quat("-Z", "Y").to_euler()
    vise(loc); c.keyframe_insert("location", frame=1); c.keyframe_insert("rotation_euler", frame=1)
    if fin: vise(fin); c.keyframe_insert("location", frame=21); c.keyframe_insert("rotation_euler", frame=21)
    if ouverture: c.data.dof.use_dof = True; c.data.dof.aperture_fstop = ouverture; c.data.dof.focus_distance = mise_au_point
    return c
def lumiere(loc, energie, couleur, taille=0.3):
    bpy.ops.object.light_add(type="POINT", location=loc); L = bpy.context.object; L.data.energy = energie; L.data.color = couleur; L.data.shadow_soft_size = taille
if plan in ("large", "rue-vide"):
    if plan == "large":   # il marche au milieu de la chaussée, vers nous
        p = personnage(0, 9); p.keyframe_insert("location", frame=1); p.location.y = 7.6   # v2 : plus près (v1 : 2 % du cadre); p.keyframe_insert("location", frame=21)
    camera((0.3, -2, 2.0), (0, 20, 1.3), 40, fin=(0.3, -1.6, 2.0))
elif plan == "mains":    # v2 : de profil, la main descend dans la poche de la cuisse et s'y ferme ; contre-jour sodium
    p = personnage(0, 10)
    main = sphere(0.05, (0.25, 9.98, 0.86), peau, (0.6, 1.0, 1.4)); main.keyframe_insert("location", frame=1); main.keyframe_insert("scale", frame=1)
    main.location = (0.2, 9.93, 0.66); main.keyframe_insert("location", frame=12)
    main.scale = (0.9, 0.9, 0.9); main.keyframe_insert("scale", frame=12); main.keyframe_insert("scale", frame=21)
    boite((0.17, 9.92, 0.62), (0.12, 0.03, 0.14), mat("poche", (0.03, 0.03, 0.04), 0.9))
    lumiere((0.6, 11.2, 1.2), 60, SODIUM, 0.2); lumiere((1.0, 9.0, 0.9), 4, LED)
    camera((1.1, 9.55, 0.78), (0.2, 9.95, 0.72), 70, ouverture=2.0, mise_au_point=0.98)
elif plan == "gestes":   # v4 : silhouette en contre-jour, de profil, les bras qui parlent (le vers 3 avant que le vers 4 les ferme)
    p = personnage(0, 12, math.radians(90))
    bras = [o for o in p.children if abs(o.location.x) > 0.2 and o.location.z > 1.0]
    for f, (ag, ad) in zip((1, 6, 11, 16, 21), ((-20, 10), (-70, 30), (-35, 75), (-80, 20), (-25, 60))):
        for o, ang in zip(bras, (ag, ad)):
            o.rotation_euler = (math.radians(ang), 0, 0); o.keyframe_insert("rotation_euler", frame=f)
    bpy.ops.object.light_add(type="AREA", location=(0, 16, 2.0)); L = bpy.context.object; L.data.energy = 600; L.data.size = 1.5; L.data.color = SODIUM
    L.rotation_euler = (math.radians(90), 0, math.radians(180))
    camera((0.4, 8.0, 1.3), (0, 12, 1.25), 45)   # v4b : dans l axe de la source, contre-jour (v4a de côté : éclairé, pas de silhouette)
elif plan == "face":     # plan poitrine, regard caméra, léger travelling avant
    personnage(0, 10, 0, yeux=True); lumiere((0.9, 9.0, 2.2), 40, SODIUM); lumiere((-1.2, 9.6, 1.6), 6, LED)
    camera((0, 7.6, 1.62), (0, 10, 1.55), 50, fin=(0, 7.9, 1.62), ouverture=2.0, mise_au_point=2.3)
elif plan == "vitrine":  # son reflet dans une vitrine noire ; lui au bord du cadre, flou
    boite((-6.95, 12, 1.6), (0.05, 3.0, 2.2), mat("vitre", (0.35, 0.35, 0.38), 0.03, metal=1.0))   # v2 : miroir (v1 : reflet invisible)
    boite((-6.9, 12, 2.9), (0.08, 3.2, 0.25), mat("enseigne", (0.05, 0.05, 0.05), 0.5, (0.9, 0.2, 0.15), 6))
    personnage(-5.2, 12, math.radians(-90)); lumiere((-3.5, 11, 3), 120, SODIUM, 0.5)
    camera((-4.4, 9.6, 1.6), (-6.95, 12.6, 1.4), 40)
elif plan == "porte":    # de dos devant l'entrée ; une applique froide au-dessus de la porte
    boite((-6.95, 20, 1.1), (0.08, 1.2, 2.2), mat("porte", (0.06, 0.05, 0.05), 0.7))
    boite((-6.85, 20, 2.45), (0.1, 0.3, 0.12), mat("applique", (0.1, 0.1, 0.1), 0.4, LED, 15)); lumiere((-6.6, 20, 2.3), 25, LED, 0.1)
    personnage(-6.1, 20, math.radians(-90)); camera((-3.4, 20.6, 1.7), (-6.95, 20, 1.4), 40, fin=(-3.6, 20.5, 1.7))
elif plan == "escalier":  # façade : la colonne de la cage d'escalier ; une fenêtre s'allume à l'image 10
    for k, z in enumerate((2.5, 5.5, 8.5)):
        f = boite((-6.95, 20.0, z), (0.05, 0.9, 1.3), mat(f"esc{k}", (0, 0, 0), 0.5, (1.0, 0.8, 0.55), 0))
        if k == 0:
            n = f.data.materials[0].node_tree.nodes["Principled BSDF"].inputs["Emission Strength"]
            n.default_value = 0; n.keyframe_insert("default_value", frame=9); n.default_value = 8; n.keyframe_insert("default_value", frame=10)
    camera((2.5, 14, 1.4), (-6.95, 20.5, 4.5), 28)
sc.frame_set(1); bpy.ops.render.render(animation=True)
