# verif_previz.py : contrôles automatiques de la previz de « L'Air », sur le début, le milieu et la fin de chaque plan.
# blender -b FICHIER.blend -P verif_previz.py -- RAPPORT.json
# 1. Axe des 180° : la caméra reste du même côté de la ligne entre les deux têtes que le plan 1 ; à l'écran, il regarde
#    vers la droite et elle vers la gauche (tant qu'ils se font face, plans 1 à 7a).
# 2. Avant le plan 7b : aucun pixel du cadre livré (2,39:1) ne voit le sol ni ses jambes, ses pieds, ses entraves ou la chaîne.
# 3. Plans 1, 6, 8b, et la fin du 7b : le dôme couvert est visible (non caché) dans le cadre livré.
import bpy, sys, json
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
OUT = sys.argv[sys.argv.index("--") + 1]
FPS = 24
def F(t): return int(round(t * FPS)) + 1
PLANS = [("01", "CAM_01_large", 0, 5), ("02a", "CAM_ELLE", 5, 8), ("02b", "CAM_LUI", 8, 11), ("03", "CAM_LUI", 11, 16),
         ("04a", "CAM_ELLE", 16, 19), ("04b", "CAM_LUI", 19, 22), ("05a", "CAM_ELLE", 22, 25), ("05b", "CAM_LUI", 25, 28),
         ("06", "CAM_06_deux", 28, 31), ("07a", "CAM_07a_taille", 31, 34), ("07b", "CAM_07b_en_pied", 34, 39),
         ("08a", "CAM_08a_mains", 39, 41), ("08b", "CAM_08b_profil", 41, 46)]
AVANT_7B = {"01", "02a", "02b", "03", "04a", "04b", "05a", "05b", "06", "07a"}
DOME = {"01", "06", "07b", "08b"}
INTERDIT = ("SOL", "COULOIR_sol", "LUI_cuisse", "LUI_tibia", "LUI_pied", "LUI_entrave", "LUI_chaine")
sc = bpy.context.scene; sc.render.resolution_x, sc.render.resolution_y = 1280, 720
V0, V1 = 0.5 - 0.5 * (16 / 9) / 2.39, 0.5 + 0.5 * (16 / 9) / 2.39     # bande livrée en 2,39:1 dans l'image 16:9
O = bpy.data.objects
def cote(cam):   # signe du côté de la ligne d'action (vue de dessus) où se trouve la caméra
    a = O["LUI_tete"].matrix_world.translation; b = O["ELLE_tete"].matrix_world.translation; c = cam.matrix_world.translation
    return 1 if ((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)) > 0 else -1
def regard(cam, P):   # direction du regard à l'écran : +1 vers la droite, -1 vers la gauche ; et position x à l'écran
    t = world_to_camera_view(sc, cam, O[P + "_tete"].matrix_world.translation)
    n = world_to_camera_view(sc, cam, O[P + "_nez"].matrix_world.translation)
    return (1 if n.x > t.x else -1), round(t.x, 2), t.z > 0
def rayons(cam, nu=48, nv=20, v0=V0, v1=V1):
    dg = bpy.context.evaluated_depsgraph_get(); fr = cam.data.view_frame(scene=sc)   # haut-droit, bas-droit, bas-gauche, haut-gauche
    tr, brr, bl, tl = [cam.matrix_world @ p for p in fr]; o = cam.matrix_world.translation; hits = {}
    for i in range(nu):
        for j in range(nv):
            u = (i + 0.5) / nu; v = v0 + (v1 - v0) * (j + 0.5) / nv
            p = bl + (brr - bl) * u + (tl - bl) * v
            ok, loc, nor, idx, ob, mtx = sc.ray_cast(dg, o, (p - o).normalized())
            if ok: hits[ob.name] = hits.get(ob.name, 0) + 1
    return hits
def dome_visible(cam):
    dg = bpy.context.evaluated_depsgraph_get(); tgt = O["DOME_linge"].matrix_world.translation
    v = world_to_camera_view(sc, cam, tgt)
    if not (0 <= v.x <= 1 and V0 <= v.y <= V1 and v.z > 0): return False, "hors du cadre livré", round(v.x, 2), round(v.y, 2)
    o = cam.matrix_world.translation; ok, loc, nor, idx, ob, mtx = sc.ray_cast(dg, o, (tgt - o).normalized())
    return (ok and ob.name.startswith("DOME")), (ob.name if ok else "rien"), round(v.x, 2), round(v.y, 2)
sc.frame_set(F(2.5)); ref = cote(O["CAM_01_large"])
rapport = []; erreurs = 0
for nom, cn, t0, t1 in PLANS:
    cam = O[cn]
    for t in (t0 + 0.05, (t0 + t1) / 2, t1 - 0.05):
        sc.frame_set(F(t)); sc.camera = cam; r = {"plan": nom, "t": round(t, 2), "camera": cn}
        if nom in AVANT_7B:
            r["cote_axe"] = "bon" if cote(cam) == ref else "AXE FRANCHI"
            for P, attendu in (("LUI", 1), ("ELLE", -1)):
                d, x, devant = regard(cam, P)
                if devant and -0.1 <= x <= 1.1: r[f"regard_{P}"] = ("droite" if d > 0 else "gauche") + ("" if d == attendu else " (FAUX)")
            h = rayons(cam); bad = {k: v for k, v in h.items() if k.startswith(INTERDIT)}
            r["sol_ou_jambes_dans_le_cadre_livre"] = bad or "aucun"
            hf = rayons(cam, v0=0.0, v1=1.0); badf = {k: v for k, v in hf.items() if k.startswith(INTERDIT)}
            r["sol_ou_jambes_dans_le_16_9_complet"] = badf or "aucun"
            if r["cote_axe"] != "bon" or bad or any("FAUX" in str(v) for k, v in r.items() if k.startswith("regard")): erreurs += 1; r["ERREUR"] = True
        if nom in DOME and not (nom == "07b" and t < t1 - 0.5):   # 7b : sa tête cache le dôme au début ; il doit être visible quand la porte se referme
            ok, ob, x, y = dome_visible(cam); r["dome"] = "visible" if ok else f"NON ({ob})"; r["dome_xy"] = (x, y)
            if not ok: erreurs += 1; r["ERREUR"] = True
        rapport.append(r)
json.dump(rapport, open(OUT, "w"), ensure_ascii=False, indent=1)
for r in rapport:
    print(r["plan"], r["t"], "|", " ; ".join(f"{k}={v}" for k, v in r.items() if k not in ("plan", "t", "camera")))
print("ERREURS", erreurs)
