"""Collages V5 Sony (2026-10-11), d'après `projets-phase-3/sony-linkbuds/da.md` : le sujet net, en couleur, devant SA PROPRE
image transformée (noir et blanc, négatif, écho) ; jamais de fond ajouté, de cadre, d'ombre ni de cerne. Détourage BiRefNet
portrait (deux passes), contrôlé au bord à 200 % (`labo/outils/controle_detourage.py`).
Piste de Diego pour le collage A : « elle détourée, le plan suivant vient se glisser derrière elle, puis elle disparaît
(par un glitch, par exemple) ».

Usage : python collage_v5.py VARIANTE SORTIE_DIR   (VARIANTE : A1 A2 A3 B1 B3 C1 C2)
Sorties : <variante>.mov (ProRes 4444, 1080x1920, 25 i/s, à poser sans LUT), <variante>_apercu.jpg (images clés).
"""
import sys, os, subprocess, json
import numpy as np, cv2
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../couleur"))
from banc_look import extrait
from look_sony import lit_cube, applique_cube
LUT = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/P3/P3_sony_look_V5_{}.cube"
W, H = 1080, 1920
ease = lambda u: 1 - (1 - min(max(u, 0.0), 1.0)) ** 3
lisse = lambda u: (lambda x: x * x * (3 - 2 * x))(min(max(u, 0.0), 1.0))
CUBES = {}


def grade(rush, t, larg, lut="salle"):
    if lut not in CUBES: CUBES[lut] = lit_cube(LUT.format(lut))
    return applique_cube(extrait(rush, t, larg), *CUBES[lut]).astype(np.float32)


def masque(img_full, cache):
    if os.path.exists(cache):
        return cv2.imread(cache, cv2.IMREAD_GRAYSCALE).astype(np.float32) / 255
    from rembg import new_session, remove
    from PIL import Image
    s = new_session("birefnet-portrait")
    im = Image.fromarray((np.clip(img_full, 0, 1) * 255).astype(np.uint8))
    m1 = np.asarray(remove(im, session=s, only_mask=True, post_process_mask=False).convert("L"), np.float32) / 255
    ys, xs = np.where(m1 > 0.5); Hh, Ww = m1.shape
    mx, my = int((xs.max() - xs.min()) * 0.08) + 40, int((ys.max() - ys.min()) * 0.08) + 40
    x0, x1, y0, y1 = max(0, xs.min() - mx), min(Ww, xs.max() + mx), max(0, ys.min() - my), min(Hh, ys.max() + my)
    m2 = np.asarray(remove(im.crop((x0, y0, x1, y1)), session=s, only_mask=True, post_process_mask=False).convert("L"), np.float32) / 255
    m = np.zeros_like(m1); m[y0:y1, x0:x1] = m2
    cv2.imwrite(cache, (m * 255).astype(np.uint8))
    return m


def nb(img, gain=0.85, gamma=1.15):
    y = img @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    y = np.clip(y * gain, 0, 1) ** gamma
    return np.repeat(y[..., None], 3, 2)


def place(img, a, s=1.0, dx=0.0, dy=0.0, centre=None):
    c = centre or (W / 2, H / 2)
    M = cv2.getRotationMatrix2D(c, 0, s); M[0, 2] += dx; M[1, 2] += dy
    return (cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE),
            cv2.warpAffine(a, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT))


def sur(fond, c, a): return fond * (1 - a[..., None]) + c * a[..., None]


def bandes(k_rng, prop, seed, h=10):
    """masque de lignes horizontales : une proportion `prop` des bandes de `h` px est retirée (ordre aléatoire fixe)."""
    r = np.random.default_rng(seed).permutation(H // h + 1)
    keep = np.ones(H, np.float32)
    n = int(prop * len(r))
    for b in r[:n]: keep[b * h:(b + 1) * h] = 0
    return keep


def decale_lignes(img, a, force, seed, h=10):
    """décale des bandes horizontales de quelques dizaines de pixels (glitch monochrome du sujet qui part)."""
    rng = np.random.default_rng(seed); out, ao = img.copy(), a.copy()
    for y0 in range(0, H, h):
        if rng.random() < 0.45:
            d = int(rng.normal(0, 1) * force)
            out[y0:y0 + h] = np.roll(img[y0:y0 + h], d, axis=1); ao[y0:y0 + h] = np.roll(a[y0:y0 + h], d, axis=1)
    return out, ao


def flou_mouvement(frames_fn, n=4):
    return sum(frames_fn(i / n) for i in range(n)) / n


def ecrit(frames, out):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb48le", "-s", f"{W}x{H}", "-r", "25", "-i", "-",
                          "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuv444p12le",
                          "-vf", "scale=out_color_matrix=bt709:out_range=tv", "-colorspace", "bt709", "-color_primaries", "bt709",
                          "-color_trc", "bt709", "-color_range", "tv", out], stdin=subprocess.PIPE)
    for f in frames: p.stdin.write((np.clip(f, 0, 1) * 65535 + 0.5).astype(np.uint16).tobytes())
    p.stdin.close(); p.wait()
    idx = [0, len(frames) // 3, 2 * len(frames) // 3, len(frames) - 2, len(frames) - 1]
    ap = np.concatenate([cv2.resize(frames[i], (270, 480)) for i in idx], 1)
    cv2.imwrite(out.rsplit(".", 1)[0] + "_apercu.jpg", (np.clip(ap[..., ::-1], 0, 1) * 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 88])


def collage_A(var, sortie):
    # gel C6594 à 0,84 s (fin de 275-281) ; plan suivant C6580 (fente) à partir de 0,30 s, 100 % : src 15 + 2k
    full = grade("C6594", 0.84, 2160)
    a = cv2.resize(masque(full, os.path.join(sortie, "m_A.png")), (W, H), interpolation=cv2.INTER_AREA)
    img = cv2.resize(full, (W, H), interpolation=cv2.INTER_AREA)
    suiv = [grade("C6580", 0.30 + 0.04 * (k - 3), 1080) for k in range(3, 12)]
    frames = []
    for k in range(12):
        if var == "A1":   fond0 = nb(img, 0.75)
        elif var == "A2": fond0 = (1 - img) * 0.62
        else:             fond0 = nb(img, 0.55)
        if var == "A3":   # échos du sujet, en noir et blanc, qui grandissent derrière lui
            for e, (s_, al) in enumerate([(1.06, .35), (1.13, .22), (1.21, .12)]):
                ce, me = place(nb(img, 1.0), a, s_ + 0.01 * k, 0, 0)
                fond0 = sur(fond0, ce, cv2.GaussianBlur(me, (0, 0), 6) * al)
        fond = fond0
        if k >= 3:        # le plan suivant arrive derrière le sujet
            u = (k - 3) / 5
            nx = suiv[min(k - 3, len(suiv) - 1)]
            if var == "A1":   # glisse depuis le bas, flou de mouvement
                def f(sub):
                    off = H * (1 - ease(u + sub / 5)) if u < 1 else 0
                    c, m = place(nx, np.ones((H, W), np.float32), 1.0, 0, off)
                    return sur(fond0, c, m)
                fond = flou_mouvement(f) if u < 1 else nx
            elif var == "A2": # révélé par lignes (balayage)
                keep = bandes(k, 1 - lisse(u), 11)
                fond = fond0 * keep[:, None, None] + nx * (1 - keep[:, None, None])
            else:             # entre par la droite, filé
                def f(sub):
                    off = W * (1 - ease(u + sub / 5)) if u < 1 else 0
                    c, m = place(nx, np.ones((H, W), np.float32), 1.0, off, 0)
                    return sur(fond0, c, m)
                fond = flou_mouvement(f, 6) if u < 1 else nx
        s = 1.0 + 0.03 * ease(k / 3)
        cs, ms = place(img, a, s)
        if k >= 9:        # le sujet disparaît
            v = (k - 8) / 3
            if var in ("A1", "A2"):
                cs, ms = decale_lignes(nb(cs, 1.05) * 0.5 + cs * 0.5, ms, 18 + 50 * v, 30 + k)
                ms = ms * bandes(k, min(1, 0.35 + 0.65 * v) if k < 11 else 1.0, 40 + k)[:, None]
            else:
                ms = ms * (1 - lisse(v)); cs = nb(cs, 1.0) * v + cs * (1 - v)
        frames.append(sur(fond, cs, ms))
    ecrit(frames, os.path.join(sortie, var + ".mov"))


def collage_B(var, sortie):
    # gel C6566 à 2,40 s (fin de 497-503) ; reprise du mouvement à 515 (même image)
    full = grade("C6566", 2.40, 2160)
    a = cv2.resize(masque(full, os.path.join(sortie, "m_B.png")), (W, H), interpolation=cv2.INTER_AREA)
    img = cv2.resize(full, (W, H), interpolation=cv2.INTER_AREA)
    frames = []
    for k in range(12):
        if var == "B4":   # écho : copies floues et agrandies du sujet, en noir et blanc, derrière lui (Nike PM24)
            fond = img * 0.55
            for s_, al, fl in [(1.10, .30, 10), (1.22, .18, 18), (1.36, .10, 28)]:
                ce, me = place(nb(img, 1.1), a, s_ + 0.012 * k, 0, 0, centre=(W * 0.55, H * 0.45))
                fond = sur(fond, cv2.GaussianBlur(ce, (0, 0), fl / 3), cv2.GaussianBlur(me, (0, 0), fl) * al)
        else:
            fond = nb(img, 0.62) if var == "B1" else (1 - img) * 0.5
        if k >= 10:   # la couleur revient sur deux images avant la reprise
            v = (k - 9) / 3; fond = fond * (1 - v) + img * v
        s = 1.0 + 0.04 * lisse(k / 11)
        cs, ms = place(img, a, s, 0, 0, centre=(W * 0.55, H * 0.45))
        frames.append(sur(fond, cs, ms))
    ecrit(frames, os.path.join(sortie, var + ".mov"))


def collage_C(var, sortie):
    # gel C6657 à 2,20 s (fin de 672-678), lumière rouge
    full = grade("C6657", 2.20, 2160, "rouge")
    a = cv2.resize(masque(full, os.path.join(sortie, "m_C.png")), (W, H), interpolation=cv2.INTER_AREA)
    img = cv2.resize(full, (W, H), interpolation=cv2.INTER_AREA)
    frames = []
    for k in range(8):
        if var == "C3":   # tête positive, réduite, entourée de sa propre image en négatif (sans cadre)
            fond = (1 - img) * 0.80
            cs, ms = place(img, a, 0.80 + 0.06 * ease(k / 3), 0, 0, centre=(W * 0.42, H * 0.40))
            frames.append(sur(fond, cs, ms)); continue
        if var == "C1":   # tête positive sur sa propre image en négatif
            fond = (1 - img) * 0.85
            cs, ms = place(img, a, 1.0 + 0.04 * ease(k / 3))
            frames.append(sur(fond, cs, ms))
        else:             # strobe d'états sur l'image figée (foebusdelapaz), 2 négatifs seulement (photosensibilité)
            etat = ["nat", "neg", "nb", "nat", "seuil", "neg", "nb", "nat"][k]
            f = {"nat": img, "neg": 1 - img, "nb": nb(img, 1.0)}.get(etat)
            if etat == "seuil":
                y = nb(img, 1.0)[..., 0]; f = np.repeat((y > np.percentile(y, 70)).astype(np.float32)[..., None], 3, 2)
            frames.append(f)
    ecrit(frames, os.path.join(sortie, var + ".mov"))


if __name__ == "__main__":
    var, sortie = sys.argv[1], sys.argv[2]
    os.makedirs(sortie, exist_ok=True)
    {"A": collage_A, "B": collage_B, "C": collage_C}[var[0]](var, sortie)
    print("écrit", var)
