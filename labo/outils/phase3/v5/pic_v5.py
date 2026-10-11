"""Dernier pic V5 Sony (831-948, 117 images à 25 i/s), demandé par Diego le 2026-10-11 (« un dernier moment de 4 à 5 s, très
accéléré, avec de gros effets tirés d'eyecannndy, selon la matière et la DA »). Référence : foebusdelapaz (analyses/reseaux/) ;
principes repris dans notre palette (da.md : noir et blanc, négatif, seuil, rouge réel, jamais d'aplat de couleur) :
  P1 831-850  révélation par seuil (la sangle KORE sort du noir par paliers), puis couleur et poussée.
  P2 850-878  rafale récapitulative : 14 plans de 2 images, chacun dans un état (naturel, noir et blanc, négatif, seuil).
  P3 878-898  respiration : traînées du geste en noir et blanc (bras levés de toute la salle).
  P4 898-925  stroboscope d'états sur une seule action (la salle rouge), une image chacun, 3 négatifs au plus.
  P5 925-948  flash cut aligné sur le mot KORE (hall, façade, sangles), puis balayage monochrome ; le blanc de 948 est sur V3.
Chaque source (rush, temps) est listée dans pic_sources.json pour le contrôle des doublons.
Usage : python pic_v5.py SORTIE_DIR [--partie P1..P5] ; sortie : pic_v5.mov (ProRes 4444) + aperçus.
"""
import sys, os, json
import numpy as np, cv2
sys.path.insert(0, os.path.dirname(__file__))
from collage_v5 import grade, nb, ecrit, ease, lisse, W, H, bandes, decale_lignes

SRC = []


def plan(rush, t0, n, lut, pas=0.04, larg=1080):
    """n images à 25 i/s depuis t0 (vitesse 100 % : une image sur deux du rush 50p)."""
    SRC.append(dict(rush=rush, debut=round(t0, 3), fin=round(t0 + pas * n, 3)))
    return [grade(rush, t0 + pas * i, larg, lut) for i in range(n)]


def seuil(img, p):
    y = nb(img, 1.0)[..., 0]
    return np.repeat((y > np.percentile(y, p)).astype(np.float32)[..., None], 3, 2)


def etat(img, e):
    return {"nat": img, "nb": nb(img, 0.95), "neg": 1 - img, "seuil": None}[e] if e != "seuil" else seuil(img, 72)


def P1():
    src = plan("C6632", 2.0, 19, "salle")
    out = []
    for k, im in enumerate(src):
        if k < 6:   # paliers de seuil : du très haut (presque noir) au plein
            out.append(seuil(im, [99.5, 98, 95, 90, 82, 70][k]))
        else:
            s = 1.0 + 0.06 * lisse((k - 6) / 12)
            M = cv2.getRotationMatrix2D((W / 2, H / 2), 0, s)
            out.append(cv2.warpAffine(im, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE))
    return out


def P2():
    plans = [("C6573", 5.0, "salle"), ("C6583", 6.0, "salle"), ("C6588", 2.5, "salle"), ("C6578", 8.4, "salle"), ("C6587", 15.0, "salle"),
             ("C6626", 8.0, "salle"), ("C6636", 5.0, "salle"), ("C6640", 4.0, "salle"), ("C6658", 3.0, "rouge"), ("C6659", 3.0, "rouge"),
             ("C6661", 2.0, "rouge"), ("C6662", 2.8, "rouge"), ("C6664", 1.5, "rouge"), ("C6665", 10.6, "rouge")]
    etats = ["nat", "nb", "nat", "neg", "nat", "nb", "seuil", "nat", "nb", "nat", "neg", "nat", "nb", "nat"]
    out = []
    for (r, t, l), e in zip(plans, etats):
        for im in plan(r, t, 2, l):
            out.append(etat(im, e))
    return out


def P3():
    src = plan("C6637", 3.0, 20, "salle")
    out, trace = [], None
    for im in src:
        y = nb(im, 1.0)
        trace = y if trace is None else np.maximum(y, trace * 0.82)     # traînée : le maximum qui s'éteint lentement
        out.append(np.clip(trace * 0.9 + y * 0.1, 0, 1))
    return out


def P4():
    src = plan("C6662", 3.0, 27, "rouge")
    seq = ["nat", "nat", "nb", "nb", "nat", "seuil", "nat", "nb", "neg", "nat", "nat", "nb", "seuil", "nat", "nb", "nb", "nat",
           "neg", "nat", "nb", "seuil", "nat", "nb", "nat", "neg", "nb", "nat"]
    return [etat(im, e) for im, e in zip(src, seq)]


# mot KORE : (rush, temps, lut, zone de recherche en pixels d'une image 2160 de large, texte clair ou sombre)
H6495, FAC = (300, 1900, 1800, 2450), (700, 250, 2100, 1100)
KORE = [("C6495", 1.5, "jour", H6495, "clair", 4), ("C6682", 0.5, "jour", FAC, "sombre", 4),
        ("C6495", 1.8, "jour", H6495, "clair", 3), ("C6682", 30.0, "jour", FAC, "sombre", 3),
        ("C6495", 2.05, "jour", H6495, "clair", 2), ("C6682", 8.0, "jour", FAC, "sombre", 2),
        ("C6495", 2.3, "jour", H6495, "clair", 1), ("C6682", 14.0, "jour", FAC, "sombre", 1)]
# (les sangles C6632 / C6627 ont été essayées : orientation du mot mal estimée, mot trop petit et penché -> écartées)
CIBLE = (540, 960, 980)     # centre x, y et largeur du mot dans l'image 1080x1920


def localise(img, zone, mode):
    x0, y0, x1, y1 = zone
    g = cv2.cvtColor((np.clip(img[y0:y1, x0:x1], 0, 1) * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
    if mode == "sangle":   # lettres sombres sur une sangle claire, fond sombre autour : la sangle d'abord, les lettres dedans
        t, clair = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        nn, ll, ss, _ = cv2.connectedComponentsWithStats(clair)
        k = 1 + int(np.argmax(ss[1:, cv2.CC_STAT_AREA]))
        hull = cv2.convexHull(np.column_stack(np.where(ll == k))[:, ::-1].astype(np.int32))
        zone_m = np.zeros_like(g); cv2.fillConvexPoly(zone_m, hull, 255)
        zone_m = cv2.erode(zone_m, np.ones((15, 15), np.uint8))
        b = ((g < t * 0.75) & (zone_m > 0)).astype(np.uint8) * 255
    else:
        _, b = cv2.threshold(g, 0, 255, (cv2.THRESH_BINARY if mode == "clair" else cv2.THRESH_BINARY_INV) + cv2.THRESH_OTSU)
    n, lab, st, cen = cv2.connectedComponentsWithStats(b)
    # lettres : composantes de taille moyenne ; on garde les 4 plus grandes compatibles
    cand = [i for i in range(1, n) if 150 < st[i, cv2.CC_STAT_AREA] < 0.2 * b.size]
    cand = sorted(cand, key=lambda i: -st[i, cv2.CC_STAT_AREA])[:4]
    pts = np.column_stack(np.where(np.isin(lab, cand)))[:, ::-1].astype(np.float32)
    (cx, cy), (w, h), ang = cv2.minAreaRect(pts)
    if w < h: w, h = h, w; ang += 90
    if ang > 90: ang -= 180
    if ang < -90: ang += 180
    return cx + x0, cy + y0, w, ang


def P5():
    """crash zoom du hall vers le mot KORE (flou radial), puis le mot tenu qui change d'état en accélérant, puis balayage.
    (Essais écartés : flash cut aligné hall / façade / sangles : sur la façade l'enseigne est en haut de l'image et le visage de
    l'animatrice reste dans le cadre ; sur les sangles le mot est petit et penché.)"""
    full0 = grade("C6495", 1.3, 2160, "jour")
    cx, cy, w, ang = localise(full0, H6495, "clair")
    sF = CIBLE[2] / w                                # échelle finale : le mot fait CIBLE[2] px de large
    s0 = W / 2160                                    # départ : le plan entier
    out = []
    n_zoom, etats = 6, ["nat"] * 3 + ["nb"] * 3 + ["seuil"] * 2 + ["nat"] * 2 + ["neg", "nb", "seuil", "nat"]
    SRC.append(dict(rush="C6495", debut=1.3, fin=round(1.3 + 0.04 * (n_zoom + len(etats)), 3)))
    for k in range(n_zoom + len(etats)):
        im = grade("C6495", 1.3 + 0.04 * k, 2160, "jour")
        if k < n_zoom:   # crash zoom exponentiel, accéléré, avec flou radial (moyenne de sous-images)
            acc = np.zeros((H, W, 3), np.float32)
            for sub in range(6):
                u = min(1.0, (k + sub / 6) / n_zoom) ** 2
                sc = np.exp(np.log(s0) * (1 - u) + np.log(sF) * u)
                px = W / 2 * (1 - u) + CIBLE[0] * u; py = H / 2 * (1 - u) + CIBLE[1] * u
                M = cv2.getRotationMatrix2D((cx, cy), 0, sc); M[0, 2] += px - cx; M[1, 2] += py - cy
                acc += cv2.warpAffine(im, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
            out.append(acc / 6)
        else:
            M = cv2.getRotationMatrix2D((cx, cy), ang, sF); M[0, 2] += CIBLE[0] - cx; M[1, 2] += CIBLE[1] - cy
            f = cv2.warpAffine(im, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
            out.append(etat(f, etats[k - n_zoom]))
    last = out[-1]
    for k in range(3):   # balayage monochrome
        a = np.ones((H, W), np.float32)
        c, a2 = decale_lignes(nb(last, 1.1), a, 40 + 50 * k, 70 + k)
        a2 = a2 * bandes(k, 0.3 + 0.3 * k, 80 + k)[:, None]
        out.append(c * a2[..., None])
    return out


if __name__ == "__main__":
    SORTIE = sys.argv[1]; os.makedirs(SORTIE, exist_ok=True)
    parts = sys.argv[sys.argv.index("--partie") + 1].split(",") if "--partie" in sys.argv else ["P1", "P2", "P3", "P4", "P5"]
    frames = []
    for p in parts:
        f = globals()[p](); print(p, len(f), flush=True); frames += f
    nom = "pic_v5" if len(parts) == 5 else "pic_" + "_".join(parts)
    ecrit(frames, os.path.join(SORTIE, nom + ".mov"))
    json.dump(SRC, open(os.path.join(SORTIE, nom + "_sources.json"), "w"), indent=1)
    # planche de toutes les images
    th = [cv2.resize(f, (135, 240)) for f in frames]
    cols = 20; rows = (len(th) + cols - 1) // cols
    sh = np.zeros((rows * 240, cols * 135, 3), np.float32)
    for i, t in enumerate(th): sh[(i // cols) * 240:(i // cols + 1) * 240, (i % cols) * 135:(i % cols + 1) * 135] = t
    cv2.imwrite(os.path.join(SORTIE, nom + "_planche.jpg"), (np.clip(sh[..., ::-1], 0, 1) * 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 85])
    print("écrit", nom, len(frames))
