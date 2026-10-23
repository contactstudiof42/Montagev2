# build_previz.py : construit la previz de « L'Air » (pièce, accessoires, personnages articulés, 13 caméras, animation minutée).
# blender -b -P build_previz.py -- SORTIE.blend
# Unités : mètres. Origine : centre du sol de la pièce. Fond de la pièce (fenêtre, croix) en +Y, porte sur le mur gauche (-X).
# Lui est assis côté -X, face à +X ; elle côté +X, face à -X. Temps du film en secondes, 24 i/s.
import bpy, sys, math
from mathutils import Vector, Euler

OUT = sys.argv[sys.argv.index("--") + 1]
FPS = 24
def F(t): return int(round(t * FPS)) + 1          # seconde du film -> image (l'image 1 = 0:00)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.fps = FPS; sc.frame_start = 1; sc.frame_end = F(47)
sc.render.engine = "BLENDER_EEVEE"
sc.render.resolution_x, sc.render.resolution_y = 1280, 720
sc.view_settings.view_transform = "AgX"
col = {}
def coll(name):
    c = bpy.data.collections.new(name); sc.collection.children.link(c); col[name] = c; return c
for n in ("DECOR", "ACCESSOIRES", "LUI", "ELLE", "CAMERAS", "LUMIERES"): coll(n)

# ---------- matériaux ----------
def mat(name, rgb, rough=0.7, emit=None, strength=0.0, metal=0.0, alpha=1.0, transm=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1); b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if emit: b.inputs["Emission Color"].default_value = (*emit, 1); b.inputs["Emission Strength"].default_value = strength
    if transm: b.inputs["Transmission Weight"].default_value = transm
    if alpha < 1: b.inputs["Alpha"].default_value = alpha
    return m
def mat_parpaing(name, axe):
    m = bpy.data.materials.new(name); m.use_nodes = True; nt = m.node_tree
    b = nt.nodes["Principled BSDF"]; br = nt.nodes.new("ShaderNodeTexBrick")
    br.inputs["Color1"].default_value = (0.62, 0.55, 0.43, 1); br.inputs["Color2"].default_value = (0.56, 0.49, 0.38, 1)
    br.inputs["Mortar"].default_value = (0.47, 0.42, 0.33, 1); br.inputs["Scale"].default_value = 1.25
    br.inputs["Mortar Size"].default_value = 0.012; br.offset = 0.5
    tc = nt.nodes.new("ShaderNodeTexCoord"); sep = nt.nodes.new("ShaderNodeSeparateXYZ"); cmb = nt.nodes.new("ShaderNodeCombineXYZ")
    nt.links.new(tc.outputs["Object"], sep.inputs["Vector"])
    nt.links.new(sep.outputs[axe], cmb.inputs["X"]); nt.links.new(sep.outputs["Z"], cmb.inputs["Y"])
    nt.links.new(cmb.outputs["Vector"], br.inputs["Vector"])
    nt.links.new(br.outputs["Color"], b.inputs["Base Color"]); b.inputs["Roughness"].default_value = 0.9
    return m
M = {
 "parpaing": mat_parpaing("M_parpaing_beige_XZ", "X"), "parpaing_y": mat_parpaing("M_parpaing_beige_YZ", "Y"), "sol": mat("M_sol_beton", (0.30, 0.29, 0.27), 0.8), "plafond": mat("M_plafond", (0.55, 0.52, 0.47), 0.9),
 "bois": mat("M_bois_table", (0.30, 0.18, 0.09), 0.55), "bois_croix": mat("M_bois_croix", (0.36, 0.22, 0.11), 0.6),
 "chaise": mat("M_bois_chaise", (0.26, 0.16, 0.08), 0.6), "verre": mat("M_verre", (0.9, 0.9, 0.9), 0.05, alpha=0.3, transm=1.0),
 "cire": mat("M_cire", (0.92, 0.88, 0.78), 0.4), "flamme": mat("M_flamme", (1, 0.6, 0.2), 0.5, emit=(1.0, 0.62, 0.26), strength=25),
 "plateau": mat("M_plateau", (0.42, 0.44, 0.45), 0.5), "assiette": mat("M_assiette", (0.85, 0.84, 0.80), 0.3),
 "nourriture": mat("M_nourriture", (0.55, 0.36, 0.18), 0.7), "legume": mat("M_legume", (0.25, 0.40, 0.12), 0.7),
 "pain": mat("M_pain", (0.72, 0.52, 0.28), 0.8), "metal_couverts": mat("M_couverts", (0.8, 0.8, 0.8), 0.25, metal=1.0),
 "gobelet": mat("M_gobelet", (0.75, 0.76, 0.78), 0.4), "serviette": mat("M_serviette", (0.88, 0.88, 0.85), 0.9),
 "verre_depoli": mat("M_verre_depoli", (0.95, 0.8, 0.9), 0.6, emit=(0.76, 0.09, 0.36), strength=6),
 "cadre_fenetre": mat("M_cadre_fenetre", (0.35, 0.34, 0.32), 0.6, metal=0.5),
 "porte": mat("M_porte", (0.55, 0.50, 0.40), 0.6), "serrure": mat("M_serrure", (0.25, 0.25, 0.26), 0.4, metal=0.8),
 "couloir": mat("M_couloir", (0.8, 0.95, 1.0), 0.5, emit=(0.72, 0.95, 1.0), strength=3),
 "dome": mat("M_dome", (0.1, 0.1, 0.1), 0.2), "linge": mat("M_linge", (0.93, 0.93, 0.90), 0.9),
 "led": mat("M_led_rouge", (1, 0.1, 0.1), 0.3, emit=(1.0, 0.16, 0.16), strength=0.0),
 "grille": mat("M_grille", (0.4, 0.4, 0.38), 0.5, metal=0.6),
 "peau_lui": mat("M_peau_lui", (0.62, 0.44, 0.34), 0.5), "peau_elle": mat("M_peau_elle", (0.70, 0.55, 0.47), 0.6),
 "chemise": mat("M_chemise_blanche", (0.92, 0.92, 0.90), 0.7), "pantalon": mat("M_pantalon_sombre", (0.08, 0.08, 0.10), 0.7),
 "chaussures": mat("M_chaussures", (0.04, 0.04, 0.04), 0.4), "cheveux": mat("M_cheveux_courts", (0.07, 0.05, 0.04), 0.6),
 "acier": mat("M_entraves_acier", (0.6, 0.6, 0.62), 0.3, metal=1.0),
 "habit": mat("M_habit", (0.05, 0.05, 0.07), 0.8), "voile": mat("M_voile", (0.04, 0.04, 0.05), 0.8),
 "guimpe": mat("M_guimpe_blanche", (0.9, 0.9, 0.88), 0.8), "chapelet": mat("M_chapelet_bois", (0.32, 0.20, 0.10), 0.5),
 "montre": mat("M_montre", (0.7, 0.62, 0.4), 0.3, metal=1.0), "cadran": mat("M_cadran", (0.95, 0.94, 0.9), 0.3),
}

def put(o, c):
    for u in list(o.users_collection): u.objects.unlink(o)
    col[c].objects.link(o); return o
def box(name, size, loc, m, c="DECOR", rot=(0, 0, 0), bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot); o = bpy.context.object; o.name = name
    o.scale = size; bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel:
        md = o.modifiers.new("biseau", "BEVEL"); md.width = bevel; md.segments = 2
    o.data.materials.append(m); return put(o, c)
def cyl(name, r, h, loc, m, c="ACCESSOIRES", rot=(0, 0, 0), v=24, r2=None):
    if r2 is None: bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=h, location=loc, rotation=rot, vertices=v)
    else: bpy.ops.mesh.primitive_cone_add(radius1=r, radius2=r2, depth=h, location=loc, rotation=rot, vertices=v)
    o = bpy.context.object; o.name = name; o.data.materials.append(m); return put(o, c)
def sph(name, r, loc, m, c="ACCESSOIRES", scale=(1, 1, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc, segments=24, ring_count=12); o = bpy.context.object
    o.name = name; o.scale = scale; o.data.materials.append(m); return put(o, c)
def torus(name, R, r, loc, m, c="ACCESSOIRES", rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_torus_add(major_radius=R, minor_radius=r, location=loc, rotation=rot, major_segments=24, minor_segments=8)
    o = bpy.context.object; o.name = name; o.data.materials.append(m); return put(o, c)
def empty(name, loc=(0, 0, 0), parent=None, c="DECOR"):
    o = bpy.data.objects.new(name, None); o.empty_display_size = 0.05; o.location = loc
    if parent: o.parent = parent
    col[c].objects.link(o); return o
def parent_keep(child, parent):
    mw = child.matrix_world.copy(); child.parent = parent; child.matrix_parent_inverse = parent.matrix_world.inverted(); child.matrix_world = mw

# ---------- la pièce : 4,0 x 3,6 x 2,7 m ----------
W, D, H = 4.0, 3.6, 2.7
box("SOL", (W, D, 0.02), (0, 0, -0.01), M["sol"])
box("PLAFOND", (W, D, 0.02), (0, 0, H + 0.01), M["plafond"])
# mur du fond (fenêtre) en morceaux autour de l'ouverture de la fenêtre : 0,35 x 0,9 m, bas à 1,72 m, centrée en x = +0,55
wx, ww, wz0, wh = 0.55, 0.35, 1.72, 0.90
box("MUR_FOND_gauche", (wx - ww / 2 + W / 2, 0.2, H), ((-W / 2 + wx - ww / 2) / 2, D / 2 + 0.1, H / 2), M["parpaing"])
box("MUR_FOND_droite", (W / 2 - (wx + ww / 2), 0.2, H), ((W / 2 + wx + ww / 2) / 2, D / 2 + 0.1, H / 2), M["parpaing"])
box("MUR_FOND_sous_fenetre", (ww, 0.2, wz0), (wx, D / 2 + 0.1, wz0 / 2), M["parpaing"])
box("MUR_FOND_sur_fenetre", (ww, 0.2, H - wz0 - wh), (wx, D / 2 + 0.1, (H + wz0 + wh) / 2), M["parpaing"])
box("MUR_DROIT", (0.2, D, H), (W / 2 + 0.1, 0, H / 2), M["parpaing_y"])
box("MUR_AVANT", (W, 0.2, H), (0, -D / 2 - 0.1, H / 2), M["parpaing"])
# mur gauche avec la porte : 0,90 x 2,05 m, centrée en y = +0,55
dy, dw, dh = 0.55, 0.90, 2.05
box("MUR_GAUCHE_avant", (0.2, dy - dw / 2 + D / 2, H), (-W / 2 - 0.1, (-D / 2 + dy - dw / 2) / 2, H / 2), M["parpaing_y"])
box("MUR_GAUCHE_arriere", (0.2, D / 2 - (dy + dw / 2), H), (-W / 2 - 0.1, (D / 2 + dy + dw / 2) / 2, H / 2), M["parpaing_y"])
box("MUR_GAUCHE_linteau", (0.2, dw, H - dh), (-W / 2 - 0.1, dy, (H + dh) / 2), M["parpaing_y"])
# plinthe et une trace d'usure au sol devant la porte
box("PLINTHE_fond", (W, 0.015, 0.08), (0, D / 2 - 0.008, 0.04), M["sol"])
# la fenêtre : cadre métal, verre dépoli éclairé en magenta par le néon de la ville (immobile)
box("FENETRE_verre_depoli", (ww - 0.04, 0.02, wh - 0.04), (wx, D / 2 + 0.12, wz0 + wh / 2), M["verre_depoli"])
for n, s, l in (("haut", (ww, 0.06, 0.03), (wx, D / 2 + 0.02, wz0 + wh - 0.015)), ("bas", (ww, 0.08, 0.03), (wx, D / 2 + 0.03, wz0 + 0.015)),
                ("g", (0.03, 0.06, wh), (wx - ww / 2 + 0.015, D / 2 + 0.02, wz0 + wh / 2)), ("d", (0.03, 0.06, wh), (wx + ww / 2 - 0.015, D / 2 + 0.02, wz0 + wh / 2)),
                ("traverse", (ww, 0.04, 0.02), (wx, D / 2 + 0.03, wz0 + wh / 2))):
    box("FENETRE_cadre_" + n, s, l, M["cadre_fenetre"])
box("NEON_VILLE_derriere", (0.9, 0.05, 1.4), (wx, D / 2 + 0.6, wz0 + wh / 2), mat("M_neon_ville", (1, 0.2, 0.5), 0.5, emit=(0.76, 0.09, 0.36), strength=12))
# la croix de bois : sur le mur du fond, x = -0,55, à 1,55-2,05 m
box("CROIX_montant", (0.05, 0.03, 0.50), (-0.55, D / 2 - 0.015, 1.80), M["bois_croix"], bevel=0.005)
box("CROIX_traverse", (0.30, 0.03, 0.05), (-0.55, D / 2 - 0.015, 1.92), M["bois_croix"], bevel=0.005)
# grille de ventilation (le son de la ventilation lointaine), haut du mur droit
box("VENTILATION_grille", (0.02, 0.30, 0.18), (W / 2 - 0.01, -0.9, 2.35), M["grille"])
for i in range(6): box(f"VENTILATION_lame_{i}", (0.03, 0.28, 0.008), (W / 2 - 0.02, -0.9, 2.28 + i * 0.026), M["grille"])
# le dôme de caméra, angle du fond à gauche (côté porte, pour être dans le cadre du plan 7b), couvert d'un linge blanc plié ; la diode rouge dessous
dome_loc = (-W / 2 + 0.16, D / 2 - 0.16, H - 0.05)
box("DOME_embase", (0.14, 0.14, 0.02), (dome_loc[0], dome_loc[1], H - 0.01), M["dome"])
sph("DOME_camera", 0.06, dome_loc, M["dome"], c="DECOR", scale=(1, 1, 0.8))
lg = sph("DOME_linge", 0.10, (dome_loc[0], dome_loc[1], H - 0.07), M["linge"], c="DECOR", scale=(1.15, 1.0, 0.75))
d = lg.modifiers.new("plis", "DISPLACE"); t = bpy.data.textures.new("T_plis", "CLOUDS"); t.noise_scale = 0.05; d.texture = t; d.strength = 0.015
box("DOME_linge_pan_retombant", (0.16, 0.005, 0.10), (dome_loc[0] + 0.02, dome_loc[1] - 0.09, H - 0.15), M["linge"], rot=(0.2, 0, -0.1))
led = sph("DOME_diode_rouge", 0.012, (dome_loc[0], dome_loc[1] - 0.05, H - 0.10), M["led"], c="DECOR")
# la porte : battant pivotant sur charnière (côté fond), plaque de serrure électrique côté couloir ; le couloir derrière
hinge = empty("PORTE_charniere", (-W / 2 - 0.02, dy + dw / 2 - 0.02, 0))
pb = box("PORTE_battant", (0.05, dw - 0.04, dh - 0.02), (-W / 2 - 0.02, dy, dh / 2), M["porte"]); parent_keep(pb, hinge)
pq = box("PORTE_poignee", (0.06, 0.12, 0.03), (-W / 2 + 0.04, dy - dw / 2 + 0.12, 1.02), M["serrure"]); parent_keep(pq, hinge)
box("PORTE_gache_electrique", (0.03, 0.05, 0.18), (-W / 2 + 0.005, dy - dw / 2 - 0.03, 1.05), M["serrure"])
box("PORTE_chambranle_haut", (0.08, dw + 0.1, 0.06), (-W / 2 + 0.02, dy, dh + 0.03), M["porte"])
box("COULOIR_sol", (3.0, 1.6, 0.02), (-W / 2 - 1.6, dy, -0.01), M["sol"])
box("COULOIR_mur_fond", (0.1, 4.0, H), (-W / 2 - 1.7, dy, H / 2), M["couloir"])
box("COULOIR_plafond_lumineux", (3.0, 1.6, 0.02), (-W / 2 - 1.6, dy, H - 0.1), M["couloir"])

# ---------- la table, les chaises, les accessoires ----------
TZ = 0.76
box("TABLE_plateau", (1.10, 0.75, 0.04), (0, 0, TZ - 0.02), M["bois"], bevel=0.004)
for sx in (-1, 1):
    for sy in (-1, 1): box(f"TABLE_pied_{sx}{sy}", (0.05, 0.05, TZ - 0.04), (sx * 0.50, sy * 0.32, (TZ - 0.04) / 2), M["bois"])
box("TABLE_ceinture_avant", (1.0, 0.02, 0.08), (0, -0.33, TZ - 0.08), M["bois"]); box("TABLE_ceinture_arriere", (1.0, 0.02, 0.08), (0, 0.33, TZ - 0.08), M["bois"])
def chaise(name, x, face):            # face : +1 = la personne regarde +X
    e = empty(name, (x, 0, 0))
    parts = [box(name + "_assise", (0.44, 0.42, 0.04), (x, 0, 0.45), M["chaise"]),
             box(name + "_dossier", (0.03, 0.40, 0.42), (x - face * 0.21, 0, 0.70), M["chaise"])]
    for sx in (-1, 1):
        for sy in (-1, 1): parts.append(box(f"{name}_pied_{sx}{sy}", (0.035, 0.035, 0.45), (x + sx * 0.19, sy * 0.18, 0.225), M["chaise"]))
    for p in parts: parent_keep(p, e)
    return e
ch_lui = chaise("CHAISE_LUI", -0.82, +1); ch_elle = chaise("CHAISE_ELLE", 0.82, -1)
# la bougie dans un verre, au centre
cyl("BOUGIE_verre", 0.045, 0.10, (0, 0.02, TZ + 0.05), M["verre"]); cyl("BOUGIE_cire", 0.030, 0.06, (0, 0.02, TZ + 0.03), M["cire"])
cyl("BOUGIE_meche", 0.002, 0.012, (0, 0.02, TZ + 0.066), M["chaussures"])
flame_piv = empty("FLAMME_pivot", (0, 0.02, TZ + 0.07), c="ACCESSOIRES")
fl = sph("FLAMME", 0.010, (0, 0.02, TZ + 0.085), M["flamme"], scale=(0.7, 0.7, 1.8)); parent_keep(fl, flame_piv)
# le plateau-repas intact, au bord de la table, côté caméra et vers lui
TX, TY = -0.18, -0.20
box("PLATEAU_repas", (0.42, 0.30, 0.015), (TX, TY, TZ + 0.008), M["plateau"], bevel=0.005)
cyl("PLATEAU_assiette", 0.11, 0.015, (TX - 0.05, TY, TZ + 0.022), M["assiette"])
sph("PLATEAU_viande", 0.045, (TX - 0.07, TY + 0.01, TZ + 0.035), M["nourriture"], scale=(1.4, 1, 0.45))
for i, (ox, oy) in enumerate(((-0.01, -0.04), (0.02, -0.03), (0.0, 0.05), (0.03, 0.04))): sph(f"PLATEAU_legume_{i}", 0.016, (TX - 0.05 + ox, TY + oy, TZ + 0.035), M["legume"])
sph("PLATEAU_pain", 0.035, (TX + 0.12, TY + 0.07, TZ + 0.04), M["pain"], scale=(1.4, 1, 0.8))
cyl("PLATEAU_gobelet", 0.035, 0.10, (TX + 0.13, TY - 0.06, TZ + 0.065), M["gobelet"], r2=0.03)
box("PLATEAU_serviette", (0.05, 0.16, 0.008), (TX + 0.10, TY, TZ + 0.02), M["serviette"])
box("PLATEAU_fourchette", (0.012, 0.17, 0.004), (TX + 0.10, TY + 0.005, TZ + 0.027), M["metal_couverts"])
box("PLATEAU_couteau", (0.012, 0.18, 0.004), (TX + 0.12, TY - 0.005, TZ + 0.027), M["metal_couverts"])

# ---------- les personnages : mannequins articulés ----------
# repère local : la personne regarde +Y ; le pivot racine est au bassin (articulation des hanches).
def membre(name, length, wid, dep, piv, mat_, c, down=True, offset=(0, 0, 0)):
    z = -length / 2 if down else length / 2
    o = box(name, (wid, dep, length), (0, 0, 0), mat_, c=c, bevel=min(wid, dep) * 0.3)
    o.parent = piv; o.location = (offset[0], offset[1], z + offset[2]); return o
def personne(P, Hh, c, mats, broad, hunch=0.0):
    root = empty(P + "_bassin", c=c)
    s = {k: v * Hh for k, v in dict(thigh=0.245, shin=0.285, torso=0.29, upper=0.19, fore=0.15, hand=0.10, neck=0.05, head=0.13).items()}
    s["shoulder"] = broad; s["hipw"] = broad * 0.62
    spine = empty(P + "_colonne", parent=root, c=c); spine.rotation_euler.x = hunch
    membre(P + "_torse", s["torso"], s["shoulder"] * 0.9, 0.24 * Hh / 1.8, spine, mats["torse"], c, down=False)
    neck = empty(P + "_cou", (0, 0, s["torso"]), parent=spine, c=c)
    membre(P + "_cou_m", s["neck"], 0.11, 0.11, neck, mats["peau"], c, down=False)
    head = empty(P + "_tete", (0, 0, s["neck"]), parent=neck, c=c)
    hd = sph(P + "_tete_m", s["head"] / 2, (0, 0, 0), mats["peau"], c=c, scale=(0.78, 0.92, 1.0)); hd.parent = head; hd.location = (0, 0.01, s["head"] / 2)
    sph(P + "_nez", 0.018, (0, 0, 0), mats["peau"], c=c).parent = head; bpy.data.objects[P + "_nez"].location = (0, s["head"] * 0.45, s["head"] * 0.45)
    j = {"root": root, "spine": spine, "neck": neck, "head": head, "s": s}
    for side, sx in (("g", -1), ("d", 1)):
        sh = empty(f"{P}_epaule_{side}", (sx * s["shoulder"] / 2, 0, s["torso"] * 0.93), parent=spine, c=c)
        membre(f"{P}_bras_{side}", s["upper"], 0.10 * Hh / 1.8, 0.10 * Hh / 1.8, sh, mats["manche"], c)
        el = empty(f"{P}_coude_{side}", (0, 0, -s["upper"]), parent=sh, c=c)
        membre(f"{P}_avantbras_{side}", s["fore"], 0.085 * Hh / 1.8, 0.085 * Hh / 1.8, el, mats["manche"], c)
        wr = empty(f"{P}_poignet_{side}", (0, 0, -s["fore"]), parent=el, c=c)
        membre(f"{P}_main_{side}", s["hand"], mats.get("main_w", 0.09) * Hh / 1.8, 0.035, wr, mats["peau"], c)
        hp = empty(f"{P}_hanche_{side}", (sx * s["hipw"] / 2, 0, 0), parent=root, c=c)
        membre(f"{P}_cuisse_{side}", s["thigh"], 0.15 * Hh / 1.8, 0.16 * Hh / 1.8, hp, mats["jambe"], c)
        kn = empty(f"{P}_genou_{side}", (0, 0, -s["thigh"]), parent=hp, c=c)
        membre(f"{P}_tibia_{side}", s["shin"], 0.11 * Hh / 1.8, 0.12 * Hh / 1.8, kn, mats["jambe"], c)
        an = empty(f"{P}_cheville_{side}", (0, 0, -s["shin"]), parent=kn, c=c)
        ft = box(f"{P}_pied_{side}", (0.10, 0.27 * Hh / 1.8, 0.08), (0, 0, 0), mats["pied"], c=c, bevel=0.02); ft.parent = an; ft.location = (0, 0.07, -0.04)
        j.update({f"sh_{side}": sh, f"el_{side}": el, f"wr_{side}": wr, f"hp_{side}": hp, f"kn_{side}": kn, f"an_{side}": an})
    return j

lui = personne("LUI", 1.95, "LUI", {"torse": M["chemise"], "manche": M["chemise"], "peau": M["peau_lui"], "jambe": M["pantalon"], "pied": M["chaussures"], "main_w": 0.11}, broad=0.54)
elle = personne("ELLE", 1.50, "ELLE", {"torse": M["habit"], "manche": M["habit"], "peau": M["peau_elle"], "jambe": M["habit"], "pied": M["chaussures"], "main_w": 0.075}, broad=0.36, hunch=math.radians(10))
# détails de lui : cheveux courts, col boutonné, boutons ; les entraves d'acier et la chaîne (toujours là, cachées avant 7b)
s = lui["s"]
cv = sph("LUI_cheveux", s["head"] / 2 * 1.03, (0, 0, 0), M["cheveux"], c="LUI", scale=(0.80, 0.94, 0.55)); cv.parent = lui["head"]; cv.location = (0, -0.005, s["head"] * 0.72)
col_ = box("LUI_col_chemise", (0.15, 0.14, 0.04), (0, 0, 0), M["chemise"], c="LUI"); col_.parent = lui["neck"]; col_.location = (0, 0, 0.01)
for i in range(5):
    b = sph(f"LUI_bouton_{i}", 0.006, (0, 0, 0), M["guimpe"], c="LUI"); b.parent = lui["spine"]; b.location = (0, 0.125, s["torso"] * (0.92 - i * 0.17))
for side in ("g", "d"):
    t = torus(f"LUI_entrave_{side}", 0.06, 0.012, (0, 0, 0), M["acier"], c="LUI"); t.parent = lui[f"an_{side}"]; t.location = (0, 0, 0.03)
# chaîne courte entre les chevilles : 8 maillons accrochés au bassin du mannequin (suivi approximatif)
chain_root = empty("LUI_chaine", parent=lui["root"], c="LUI")
for i in range(8):
    t = torus(f"LUI_chaine_maillon_{i}", 0.018, 0.005, (0, 0, 0), M["acier"], c="LUI", rot=(0, math.pi / 2 * (i % 2), 0)); t.parent = chain_root
    t.location = (-0.14 + i * 0.04, 0.0, 0.0)
# détails d'elle : voile, guimpe blanche autour du visage, chapelet à la ceinture, petite montre au poignet gauche, jupe de l'habit
s2 = elle["s"]
vl = box("ELLE_voile", (0.24, 0.20, 0.30), (0, 0, 0), M["voile"], c="ELLE", bevel=0.05); vl.parent = elle["head"]; vl.location = (0, -0.07, s2["head"] * 0.62)
vd = box("ELLE_voile_dos", (0.26, 0.04, 0.32), (0, 0, 0), M["voile"], c="ELLE", bevel=0.01); vd.parent = elle["head"]; vd.location = (0, -0.12, -0.02)
gp = box("ELLE_guimpe", (0.17, 0.05, 0.035), (0, 0, 0), M["guimpe"], c="ELLE"); gp.parent = elle["head"]; gp.location = (0, 0.06, s2["head"] * 0.98)
gc = box("ELLE_col_blanc", (0.16, 0.10, 0.05), (0, 0, 0), M["guimpe"], c="ELLE"); gc.parent = elle["neck"]; gc.location = (0, 0.01, 0.0)
jupe = cyl("ELLE_jupe", 0.16, 0.62, (0, 0, 0), M["habit"], c="ELLE", r2=0.13); jupe.parent = elle["root"]
chap = empty("ELLE_chapelet", parent=elle["root"], c="ELLE"); chap.location = (0.12, 0.08, -0.02)
for i in range(14):
    b = sph(f"ELLE_chapelet_grain_{i}", 0.008, (0, 0, 0), M["chapelet"], c="ELLE"); b.parent = chap
    a = i / 13 * math.pi; b.location = (0.0, 0.04 * math.sin(a), -0.20 * (i / 13))
cr = box("ELLE_chapelet_croix", (0.03, 0.006, 0.045), (0, 0, 0), M["chapelet"], c="ELLE"); cr.parent = chap; cr.location = (0, 0.0, -0.23)
mo = cyl("ELLE_montre", 0.013, 0.006, (0, 0, 0), M["montre"], c="ELLE", rot=(math.pi / 2, 0, 0)); mo.parent = elle["wr_g"]; mo.location = (0, 0.02, 0.02)
cd = cyl("ELLE_montre_cadran", 0.010, 0.002, (0, 0, 0), M["cadran"], c="ELLE", rot=(math.pi / 2, 0, 0)); cd.parent = elle["wr_g"]; cd.location = (0, 0.024, 0.02)
br = torus("ELLE_montre_bracelet", 0.025, 0.004, (0, 0, 0), M["chaussures"], c="ELLE"); br.parent = elle["wr_g"]; br.location = (0, 0, 0.02)

# ---------- poses ----------
R = math.radians
ARTIC = ("_colonne", "_hanche_", "_genou_", "_epaule_", "_coude_", "_poignet_")
def k(obj, attr, frame, value):
    # Les angles des articulations sont écrits « négatif = vers l'avant » (cuisse, bras) et « positif = dos penché en avant » ;
    # dans Blender c'est l'inverse pour une personne qui regarde +Y : on inverse donc X pour ces articulations.
    if attr == "rotation_euler" and any(n in obj.name for n in ARTIC): value = Euler((-value.x, value.y, value.z))
    setattr(obj, attr, value); obj.keyframe_insert(attr, frame=frame)
def pose_assis(j, frame, x, face, seat=0.45, lean=0.0, hands="table"):
    s = j["s"]; zr = -math.pi / 2 if face > 0 else math.pi / 2
    k(j["root"], "location", frame, Vector((x, 0, seat + 0.06))); k(j["root"], "rotation_euler", frame, Euler((0, 0, zr)))
    k(j["spine"], "rotation_euler", frame, Euler((R(8) + lean, 0, 0)) if j is lui else Euler((R(10) + lean, 0, 0)))
    for side in ("g", "d"):
        k(j[f"hp_{side}"], "rotation_euler", frame, Euler((R(-82), 0, 0)))          # cuisse vers l'avant
        k(j[f"kn_{side}"], "rotation_euler", frame, Euler((R(82), 0, 0)))           # tibia vertical
        k(j[f"an_{side}"], "rotation_euler", frame, Euler((0, 0, 0)))
        if hands == "table":   # avant-bras posés à plat vers la table
            k(j[f"sh_{side}"], "rotation_euler", frame, Euler((R(-35), 0, R(4) if side == "g" else R(-4))))
            k(j[f"el_{side}"], "rotation_euler", frame, Euler((R(-50), 0, 0)))
            k(j[f"wr_{side}"], "rotation_euler", frame, Euler((R(-5), 0, 0)))
        else:                  # mains sur les genoux
            k(j[f"sh_{side}"], "rotation_euler", frame, Euler((R(-20), 0, 0)))
            k(j[f"el_{side}"], "rotation_euler", frame, Euler((R(-80), 0, R(-15) if side == "g" else R(15))))
            k(j[f"wr_{side}"], "rotation_euler", frame, Euler((R(-10), 0, 0)))
def pose_debout(j, frame, x, face, y=0.0, zr=None):
    zr = (-math.pi / 2 if face > 0 else math.pi / 2) if zr is None else zr
    k(j["root"], "location", frame, Vector((x, y, j["s"]["thigh"] + j["s"]["shin"] + 0.08))); k(j["root"], "rotation_euler", frame, Euler((0, 0, zr)))
    k(j["spine"], "rotation_euler", frame, Euler((R(2) if j is lui else R(10), 0, 0)))
    for side in ("g", "d"):
        k(j[f"hp_{side}"], "rotation_euler", frame, Euler((0, 0, 0))); k(j[f"kn_{side}"], "rotation_euler", frame, Euler((0, 0, 0)))
        k(j[f"sh_{side}"], "rotation_euler", frame, Euler((R(-5), 0, R(6) if side == "g" else R(-6))))
        k(j[f"el_{side}"], "rotation_euler", frame, Euler((R(-10), 0, 0))); k(j[f"wr_{side}"], "rotation_euler", frame, Euler((0, 0, 0)))
def tete(j, frame, yaw=0.0, pitch=0.0):
    k(j["head"], "rotation_euler", frame, Euler((R(pitch), 0, R(yaw))))

XL, XE = -0.82, 0.82
# 0:00 à 0:28 : assis ; lui siffle, penché vers elle
for t in (0, 5, 8, 11, 16, 19, 22, 25, 28.4):
    pose_assis(lui, F(t), XL, +1); pose_assis(elle, F(t), XE, -1)
tete(lui, F(0), 0, -5); tete(lui, F(4.5), 0, -8); tete(elle, F(0), 0, -3)
# 2a : elle se penche et souffle (5,5-7,0) ; la flamme se couche
pose_assis(elle, F(5.6), XE, -1, lean=R(10)); pose_assis(elle, F(7.2), XE, -1, lean=R(4))
k(flame_piv, "rotation_euler", F(5.9), Euler((0, 0, 0))); k(flame_piv, "rotation_euler", F(6.3), Euler((0, R(70), 0)))
k(flame_piv, "rotation_euler", F(7.4), Euler((0, R(10), 0))); k(flame_piv, "rotation_euler", F(8.2), Euler((0, 0, 0)))
# 2b-3 : il se penche pour montrer la bouche ronde (10-12,5), tapote (13,5-15,5) avec les doigts de la main droite
pose_assis(lui, F(10.2), XL, +1, lean=R(12)); pose_assis(lui, F(12.6), XL, +1, lean=R(4))
for i, t in enumerate([13.5 + 0.25 * n for n in range(9)]):
    k(lui["wr_d"], "rotation_euler", F(t), Euler((R(-5 if i % 2 else 12), 0, 0)))
# 4a : elle réessaie (16,4-18) ; 4b : il regarde la croix (19,4-20,6), puis elle
pose_assis(elle, F(16.4), XE, -1, lean=R(8)); pose_assis(elle, F(18.2), XE, -1)
tete(lui, F(19.2), 0, -8); tete(lui, F(19.6), 35, 8); tete(lui, F(20.6), 35, 8); tete(lui, F(21.0), 0, -6)
# 5a : elle regarde sa montre (22,4-23,6) en levant le poignet gauche, puis se tourne vers lui
tete(elle, F(22.2), 0, -3); tete(elle, F(22.6), -10, -35); tete(elle, F(23.6), -10, -35); tete(elle, F(24.1), 0, -2)
k(elle["el_g"], "rotation_euler", F(22.3), Euler((R(-50), 0, 0))); k(elle["el_g"], "rotation_euler", F(22.7), Euler((R(-95), 0, R(-25))))
k(elle["el_g"], "rotation_euler", F(23.6), Euler((R(-95), 0, R(-25)))); k(elle["el_g"], "rotation_euler", F(24.0), Euler((R(-50), 0, 0)))
# 5b : sa main glisse vers la sienne, sans la toucher (25,4-26,6)
k(lui["sh_d"], "rotation_euler", F(25.4), Euler((R(-35), 0, R(-4)))); k(lui["sh_d"], "rotation_euler", F(26.6), Euler((R(-62), 0, R(-14))))
k(lui["el_d"], "rotation_euler", F(25.4), Euler((R(-50), 0, 0))); k(lui["el_d"], "rotation_euler", F(26.6), Euler((R(-25), 0, 0)))
k(lui["sh_d"], "rotation_euler", F(30.8), Euler((R(-62), 0, R(-14)))); k(lui["el_d"], "rotation_euler", F(30.8), Euler((R(-25), 0, 0)))
# 6 : elle tourne la tête vers la porte (28,3) ; lui la regarde ; la diode rouge s'allume au pêne (28,4)
tete(elle, F(28.2), 0, -2); tete(elle, F(28.7), -14, 4); tete(elle, F(31.0), -14, 4)   # vers la porte, derrière lui
led_m = M["led"].node_tree.nodes["Principled BSDF"].inputs["Emission Strength"]
for t, v in ((0, 0), (28.35, 0), (28.45, 30), (38.9, 30), (39.0, 0)): led_m.default_value = v; led_m.keyframe_insert("default_value", frame=F(t))
# 7a : il se lève (31,2-32,4), elle se lève (32,6-33,6) ; elle lui arrive à la poitrine
pose_assis(lui, F(31.2), XL, +1); pose_debout(lui, F(32.4), XL + 0.10, +1)
pose_assis(elle, F(32.6), XE, -1); pose_debout(elle, F(33.6), XE - 0.10, -1)
tete(lui, F(32.4), 0, -25); tete(elle, F(33.6), 0, 28)
k(ch_lui, "location", F(31.2), Vector((XL, 0, 0))); k(ch_lui, "location", F(32.0), Vector((XL - 0.18, 0, 0)))
# 7b : la porte s'ouvre (35,0-36,0) ; il se tourne (36,0-36,6) et sort à petits pas (36,6-38,8) par la porte
hinge.rotation_euler = (0, 0, 0); hinge.keyframe_insert("rotation_euler", frame=F(35.0))
hinge.rotation_euler = (0, 0, R(-100)); hinge.keyframe_insert("rotation_euler", frame=F(36.0))
hinge.keyframe_insert("rotation_euler", frame=F(39.0)); hinge.rotation_euler = (0, 0, 0); hinge.keyframe_insert("rotation_euler", frame=F(39.6))
pose_debout(lui, F(35.8), XL + 0.10, +1); pose_debout(lui, F(36.4), XL + 0.10, +1, zr=R(150))
path = [(36.4, XL + 0.10, 0.0), (37.0, -1.10, 0.18), (37.6, -1.45, 0.42), (38.1, -1.95, 0.55), (38.6, -2.6, 0.55)]
for i, (t, x, y) in enumerate(path):
    pose_debout(lui, F(t), x, +1, y=y, zr=R(150))
    if i < len(path) - 1:     # petits pas : chaque demi-pas lève un pied de quelques centimètres seulement (chaîne courte)
        tm = (t + path[i + 1][0]) / 2; side = "g" if i % 2 else "d"
        k(lui[f"hp_{side}"], "rotation_euler", F(tm), Euler((R(-12), 0, 0))); k(lui[f"kn_{side}"], "rotation_euler", F(tm), Euler((R(18), 0, 0)))
# elle reste debout, puis se rassoit pendant qu'il sort (38,8-39,6) ; mains sur les genoux pour 8a
pose_debout(elle, F(37.8), XE - 0.10, -1); pose_assis(elle, F(38.6), XE + 0.22, -1, hands="genoux")
k(ch_elle, "location", F(37.8), Vector((XE, 0, 0))); k(ch_elle, "location", F(38.4), Vector((XE + 0.22, 0, 0)))
# 8a : ses mains cherchent le chapelet, commencent à se joindre (40,0-40,6), s'arrêtent (40,8)
k(elle["el_g"], "rotation_euler", F(39.8), Euler((R(-80), 0, R(-15)))); k(elle["el_d"], "rotation_euler", F(39.8), Euler((R(-80), 0, R(15))))
k(elle["el_g"], "rotation_euler", F(40.6), Euler((R(-88), 0, R(-38)))); k(elle["el_d"], "rotation_euler", F(40.6), Euler((R(-88), 0, R(38))))
k(elle["el_g"], "rotation_euler", F(46), Euler((R(-88), 0, R(-38)))); k(elle["el_d"], "rotation_euler", F(46), Euler((R(-88), 0, R(38))))
# 8b : elle lève les yeux vers la fenêtre (41,5) et siffle
tete(elle, F(41.2), 0, -10); tete(elle, F(41.9), -25, 18); tete(elle, F(46), -25, 18)
# la jupe suit la position assise ou debout
def jupe_assise(f): k(jupe, "rotation_euler", f, Euler((R(-82), 0, 0))); k(jupe, "location", f, Vector((0, 0.24, -0.04)))
def jupe_debout(f): k(jupe, "rotation_euler", f, Euler((0, 0, 0))); k(jupe, "location", f, Vector((0, 0, -0.30)))
jupe_assise(F(0)); jupe_assise(F(32.6)); jupe_debout(F(33.6)); jupe_debout(F(37.8)); jupe_assise(F(38.6))
# la chaîne reste entre les chevilles : basse quand il est assis comme debout
k(chain_root, "location", F(0), Vector((0, 0.45, -0.55))); k(chain_root, "location", F(31.2), Vector((0, 0.45, -0.55)))
k(chain_root, "location", F(32.4), Vector((0, 0.05, -0.97)))
for o in bpy.data.objects:
    if o.animation_data and o.animation_data.action:
        for fc in o.animation_data.action.fcurves if hasattr(o.animation_data.action, "fcurves") else []:
            for kp in fc.keyframe_points: kp.interpolation = "BEZIER"

# ---------- lumières (aperçu d'ambiance seulement ; les prompts ignorent la lumière de la previz) ----------
def light(name, kind, loc, energy, rgb, size=0.5, rot=(0, 0, 0)):
    ld = bpy.data.lights.new(name, kind); ld.energy = energy; ld.color = rgb
    if kind == "AREA": ld.size = size
    o = bpy.data.objects.new(name, ld); o.location = loc; o.rotation_euler = rot; col["LUMIERES"].objects.link(o); return o
light("L_neon_fenetre", "AREA", (wx, D / 2 - 0.05, wz0 + wh / 2), 260, (0.95, 0.25, 0.55), size=0.6, rot=(R(90), 0, R(180)))
light("L_bougie", "POINT", (0, 0.02, TZ + 0.12), 12, (1.0, 0.62, 0.3))
cl = light("L_couloir", "AREA", (-W / 2 - 0.6, dy, 1.6), 0, (0.72, 0.95, 1.0), size=1.5, rot=(0, R(-90), 0))
cl.data.energy = 0; cl.data.keyframe_insert("energy", frame=F(35.0)); cl.data.energy = 900; cl.data.keyframe_insert("energy", frame=F(36.0))
cl.data.keyframe_insert("energy", frame=F(39.0)); cl.data.energy = 0; cl.data.keyframe_insert("energy", frame=F(39.6))
w = bpy.data.worlds.new("W"); w.use_nodes = True; w.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.02; sc.world = w

# ---------- caméras (capteur plein format 36 mm ; image générée en 16:9, livrée en 2,39:1 au centre) ----------
def cam(name, loc, target, lens, shift_y=0.0, shift_x=0.0):
    cd = bpy.data.cameras.new(name); cd.lens = lens; cd.sensor_width = 36; cd.sensor_fit = "HORIZONTAL"; cd.shift_y = shift_y; cd.shift_x = shift_x
    cd.clip_start = 0.05
    o = bpy.data.objects.new(name, cd); o.location = loc; col["CAMERAS"].objects.link(o)
    d = Vector(target) - Vector(loc); o.rotation_euler = d.to_track_quat("-Z", "Y").to_euler(); return o
cam("CAM_01_large", (0.0, -1.72, 0.95), (0.0, 0.8, 0.95), 24, shift_y=0.14)
cam("CAM_ELLE", (-0.50, -0.45, 1.18), (0.80, 0.02, 1.16), 50)
cam("CAM_LUI", (1.70, -0.48, 1.22), (-0.82, 0.02, 1.12), 40)   # par-dessus son épaule droite à elle, côté caméra (axe des 180° : y < 0)
cam("CAM_06_deux", (1.25, -1.62, 0.92), (-0.6, 1.4, 1.15), 26, shift_y=0.10)
cam("CAM_07a_taille", (0.0, -1.75, 1.70), (0.0, 0.0, 1.70), 24)
cam("CAM_07b_en_pied", (0.45, -1.62, 1.00), (-1.45, 0.40, 1.0), 18, shift_y=0.07)
cam("CAM_08a_mains", (0.42, -0.70, 0.98), (0.72, 0.0, 0.63), 55)
cam("CAM_08b_profil", (0.20, -1.72, 1.05), (0.0, 1.6, 1.30), 20, shift_y=0.05)
sc.camera = bpy.data.objects["CAM_01_large"]
bpy.ops.wm.save_as_mainfile(filepath=OUT)
print("PREVIZ_OK", OUT, len(bpy.data.objects), "objets")
