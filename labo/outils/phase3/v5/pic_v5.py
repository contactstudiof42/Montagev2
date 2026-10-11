"""Dernier pic V5 Sony (831-948, 117 images à 25 i/s), demandé par Diego le 2026-10-11 (« un dernier moment de 4 à 5 s, très
accéléré, avec de gros effets tirés d'eyecannndy, selon la matière et la DA »). Référence : foebusdelapaz (analyses/reseaux/) ;
principes repris dans notre palette (da.md : noir et blanc, négatif, seuil, rouge réel, jamais d'aplat de couleur).
Version b (session du 2026-10-11 au soir) : parties recalées sur les attaques de la musique (129 BPM ; fortes à 837, 878, 901,
907, 931, 948), photosensibilité tenue (≤ 3 flashs par seconde), doublons retirés (C6578 8,4 s et C6664 1,5 s étaient déjà
dans la timeline), comptoir KORE exposé −0,13 en log (le mur était brûlé), P3 et P4 refaits :
  P1 831-849  révélation par seuil (la sangle KORE sort du noir par paliers), la couleur arrive sur l'attaque de 837.
  P2 849-878  rafale récapitulative : 14 plans de 2 images (le premier de 3), chacun dans un état (naturel, n&b, négatif, seuil).
  P3 878-901  respiration sur l'attaque de 878 : un héros de dos qui tire les sangles, en noir et blanc (variante « net » :
              plan tenu, poussée lente ; variante « echo » : traînée continue du geste par flux optique).
  P4 901-931  stroboscope d'états sur la salle rouge (naturel / n&b une image chacun), punch-in sur les temps, UN négatif sur
              l'accent de 907, UN seuil sur le temps de 919 : la vitesse sans rafale de flashs.
  P5 931-948  crash zoom du comptoir vers le mot KORE (rappel voulu de l'ouverture), le mot change d'état, un négatif sur 942,
              balayage monochrome ; le blanc de 948 est sur V3.
Chaque source (rush, temps) est listée dans pic_v5_sources.json pour le contrôle des doublons.
Usage : python pic_v5.py SORTIE_DIR [--partie P1,P3] [--p3 net|echo] [--nom NOM] ; sortie : NOM.mov (ProRes 4444) + aperçus.
"""
import sys, os, json
import numpy as np, cv2
sys.path.insert(0, os.path.dirname(__file__))
from collage_v5 import nb, ecrit, lisse, W, H, bandes, decale_lignes, CUBES, LUT
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../couleur"))
from banc_look import extrait
from look_sony import lit_cube, applique_cube

SRC = []
P3_MODE = sys.argv[sys.argv.index("--p3") + 1] if "--p3" in sys.argv else "net"


def grade(rush, t, larg=1080, lut="salle", off=0.0):
    """image étalonnée : correction d'exposition en log (S-Log3, avant la LUT), puis LUT de look V5."""
    if lut not in CUBES: CUBES[lut] = lit_cube(LUT.format(lut))
    return applique_cube(np.clip(extrait(rush, t, larg) - off, 0, 1), *CUBES[lut]).astype(np.float32)


def plan(rush, t0, n, lut, pas=0.04, larg=1080, off=0.0):
    """n images à 25 i/s depuis t0 (vitesse 100 % : une image sur deux du rush 50p)."""
    SRC.append(dict(rush=rush, debut=round(t0, 3), fin=round(t0 + pas * n, 3)))
    return [grade(rush, t0 + pas * i, larg, lut, off) for i in range(n)]


def seuil(img, p):
    y = nb(img, 1.0)[..., 0]
    return np.repeat((y > np.percentile(y, p)).astype(np.float32)[..., None], 3, 2)


def etat(img, e):
    if e == "seuil": return seuil(img, 72)
    if e == "nbl": return nb(img, 1.0, 1.0)   # noir et blanc à luminance conservée : sur une image claire, pas de flash
    return {"nat": img, "nb": nb(img, 0.95), "neg": 1 - img}[e]


def zoom(img, s, centre=None):
    c = centre or (W / 2, H / 2)
    M = cv2.getRotationMatrix2D(c, 0, s)
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


def P1():
    src = plan("C6632", 2.0, 18, "salle")
    out = []
    for k, im in enumerate(src):
        if k < 6:   # paliers de seuil : du très haut (presque noir) au plein ; la couleur tombe sur l'attaque de 837
            out.append(seuil(im, [99.5, 98, 95, 90, 82, 70][k]))
        else:
            out.append(zoom(im, 1.0 + 0.06 * lisse((k - 6) / 11)))
    return out


def P2():
    plans = [("C6573", 5.0, "salle"), ("C6583", 6.0, "salle"), ("C6588", 2.5, "salle"), ("C6578", 5.0, "salle"), ("C6587", 15.0, "salle"),
             ("C6626", 8.0, "salle"), ("C6636", 5.0, "salle"), ("C6640", 4.0, "salle"), ("C6658", 3.0, "rouge"), ("C6659", 3.0, "rouge"),
             ("C6661", 2.0, "rouge"), ("C6662", 2.8, "rouge"), ("C6664", 4.3, "rouge"), ("C6665", 10.6, "rouge")]
    etats = ["nat", "nb", "nat", "neg", "nat", "nb", "seuil", "nat", "nb", "nat", "neg", "nat", "nb", "nat"]
    out = []
    for i, ((r, t, l), e) in enumerate(zip(plans, etats)):
        for im in plan(r, t, 3 if i == 0 else 2, l):
            out.append(etat(im, e))
    return out


def flux_interp(a, b, n):
    """n images intermédiaires entre a et b (flux optique DIS calculé à mi-résolution) : la traînée devient continue."""
    ga = cv2.cvtColor((cv2.resize(a, (W // 2, H // 2)) * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
    gb = cv2.cvtColor((cv2.resize(b, (W // 2, H // 2)) * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
    f = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM).calc(ga, gb, None)
    f = cv2.resize(f, (W, H)) * 2
    gx, gy = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
    return [cv2.remap(a, gx - f[..., 0] * (k / n), gy - f[..., 1] * (k / n), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
            for k in range(n)]


def P3():
    n = 23
    if P3_MODE == "net":   # plan tenu, noir et blanc dense, poussée lente freinée
        src = plan("C6637", 4.0, n, "salle")
        return [zoom(nb(im, 0.95), 1.0 + 0.05 * lisse(k / (n - 1))) for k, im in enumerate(src)]
    # écho : toutes les images 50p, 4 sous-images interpolées par intervalle ; le sujet net devant sa traînée
    SRC.append(dict(rush="C6637", debut=4.0, fin=round(4.0 + 0.04 * n, 3)))
    f50 = [nb(grade("C6637", 4.0 + 0.02 * j, 1080, "salle"), 0.95) for j in range(2 * n + 1)]
    out, trace = [], None
    dec = 0.80 ** (1 / 8)           # même décroissance par image 25p que la V5 a, répartie sur 8 sous-images
    for k in range(n):
        subs = flux_interp(f50[2 * k], f50[2 * k + 1], 4) + flux_interp(f50[2 * k + 1], f50[2 * k + 2], 4)
        for s in subs:
            trace = s if trace is None else np.maximum(s, trace * dec)
        cur = f50[2 * k]
        out.append(zoom(np.maximum(cur, trace * 0.7), 1.0 + 0.05 * lisse(k / (n - 1))))
    return out


def P4():
    """30 images C6662 (salle rouge) ; temps à 0 (901), 6 (907, accent), 18 (919), 23 (924)."""
    src = plan("C6662", 3.0, 30, "rouge")
    seq = ["nat", "nat", "nb", "nat", "nb", "nat", "neg", "nat", "nat", "nb", "nat", "nb", "nat", "nb", "nat", "nb", "nat", "nb",
           "seuil", "nat", "nat", "nb", "nat", "nb", "nat", "nat", "nat", "nat", "nat", "nat"]
    punch = {7: 1.14, 8: 1.14, 13: 1.08, 19: 1.14, 20: 1.14, 24: 1.22}
    out = []
    for k, (im, e) in enumerate(zip(src, seq)):
        s = punch.get(k, 1.0)
        if k >= 25: s = 1.22 + 0.10 * lisse((k - 25) / 4)     # poussée finale qui entre dans le crash zoom de P5
        out.append(etat(zoom(im, s), e))
    return out


H6495 = (300, 1900, 1800, 2450)   # zone de recherche du mot dans l'image 2160 de large
CIBLE = (540, 960, 980)           # centre x, y et largeur du mot dans l'image 1080x1920
OFF_KORE = 0.13                   # exposition du comptoir en log : à 0 le mur et le haut sont brûlés (mesuré : mur 0,79 → 0,47)


def localise(img, zone):
    x0, y0, x1, y1 = zone
    g = cv2.cvtColor((np.clip(img[y0:y1, x0:x1], 0, 1) * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
    _, b = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    n, lab, st, cen = cv2.connectedComponentsWithStats(b)
    cand = [i for i in range(1, n) if 150 < st[i, cv2.CC_STAT_AREA] < 0.2 * b.size]
    cand = sorted(cand, key=lambda i: -st[i, cv2.CC_STAT_AREA])[:4]   # les 4 lettres
    pts = np.column_stack(np.where(np.isin(lab, cand)))[:, ::-1].astype(np.float32)
    (cx, cy), (w, h), ang = cv2.minAreaRect(pts)
    if w < h: w, h = h, w; ang += 90
    if ang > 90: ang -= 180
    if ang < -90: ang += 180
    return cx + x0, cy + y0, w, ang


def P5():
    """crash zoom du comptoir vers le mot KORE (flou radial), le mot tenu change d'état, un négatif sur 942, balayage."""
    full0 = grade("C6495", 1.3, 2160, "jour", OFF_KORE)
    cx, cy, w, ang = localise(full0, H6495)
    sF, s0 = CIBLE[2] / w, W / 2160
    n_zoom, etats = 5, ["nat", "nat", "nbl", "nat", "nbl", "nat", "neg", "nat", "nbl"]
    SRC.append(dict(rush="C6495", debut=1.3, fin=round(1.3 + 0.04 * (n_zoom + len(etats)), 3)))
    out = []
    for k in range(n_zoom + len(etats)):
        im = grade("C6495", 1.3 + 0.04 * k, 2160, "jour", OFF_KORE)
        if k < n_zoom:   # crash zoom exponentiel accéléré, flou radial (moyenne de sous-images)
            acc = np.zeros((H, W, 3), np.float32)
            for sub in range(6):
                u = min(1.0, (k + sub / 6) / n_zoom) ** 2
                sc = np.exp(np.log(s0) * (1 - u) + np.log(sF) * u)
                px = W / 2 * (1 - u) + CIBLE[0] * u; py = H / 2 * (1 - u) + CIBLE[1] * u
                M = cv2.getRotationMatrix2D((cx, cy), ang * u, sc); M[0, 2] += px - cx; M[1, 2] += py - cy
                acc += cv2.warpAffine(im, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
            out.append(acc / 6)
        else:
            j = k - n_zoom
            s = sF * (1.06 if j == 6 else 1.0)              # léger punch sur le négatif
            M = cv2.getRotationMatrix2D((cx, cy), ang, s); M[0, 2] += CIBLE[0] - cx; M[1, 2] += CIBLE[1] - cy
            f = cv2.warpAffine(im, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
            out.append(etat(f, etats[j]))
    last = nb(out[-1], 1.0, 1.0)
    for k in range(3):   # balayage monochrome
        a = np.ones((H, W), np.float32)
        c, a2 = decale_lignes(last, a, 40 + 50 * k, 70 + k)
        a2 = a2 * bandes(k, 0.3 + 0.3 * k, 80 + k)[:, None]
        out.append(c * a2[..., None])
    return out


if __name__ == "__main__":
    SORTIE = sys.argv[1]; os.makedirs(SORTIE, exist_ok=True)
    parts = sys.argv[sys.argv.index("--partie") + 1].split(",") if "--partie" in sys.argv else ["P1", "P2", "P3", "P4", "P5"]
    frames = []
    for p in parts:
        f = globals()[p](); print(p, len(f), flush=True); frames += f
    nom = sys.argv[sys.argv.index("--nom") + 1] if "--nom" in sys.argv else ("pic_v5" if len(parts) == 5 else "pic_" + "_".join(parts))
    ecrit(frames, os.path.join(SORTIE, nom + ".mov"))
    json.dump(SRC, open(os.path.join(SORTIE, nom + "_sources.json"), "w"), indent=1)
    th = [cv2.resize(f, (135, 240)) for f in frames]
    cols = 20; rows = (len(th) + cols - 1) // cols
    sh = np.zeros((rows * 240, cols * 135, 3), np.float32)
    for i, t in enumerate(th): sh[(i // cols) * 240:(i // cols + 1) * 240, (i % cols) * 135:(i % cols + 1) * 135] = t
    cv2.imwrite(os.path.join(SORTIE, nom + "_planche.jpg"), (np.clip(sh[..., ::-1], 0, 1) * 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 85])
    print("écrit", nom, len(frames))
