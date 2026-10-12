"""Looks V4 du mariage-jo : vraie conversion S-Log3 / S-Gamut3.Cine -> Rec.709 (gamma 2.4), sans LUT de carte ni tirage Cineon.

Chaîne (une LUT .cube, un nœud ; l'exposition et la balance de chaque plan se font AVANT, en CDL sur le log) :
  1. S-Log3 -> linéaire scène (formule Sony, jusqu'à la saturation du capteur), S-Gamut3.Cine -> Rec.709 (Bradford),
     compression douce du hors-gamut.
  2. Rapprochement des primaires (« inset », comme AgX) puis courbe de tonalité par canal, définie en diaphs autour du
     gris 18 % : pied dense, tons moyens, et **une épaule longue** (les hautes lumières descendent doucement vers le blanc
     sans jamais l'atteindre : +6 diaphs au-dessus du gris = 0,94). Les blancs saturés se désaturent naturellement.
  3. Look en OkLCh : chroma réduite, ombres neutres puis légèrement olive, hautes lumières chaudes, peau protégée
     (teinte ~55°, chroma plafonnée).
  NB : luminance d'un mélange de canaux (peau éclaircie, pierre orange en gris clair), même courbe avec un pied plus
     profond, aucune teinte.
Usage : look_mariage_v4.py couleur|nb SORTIE.cube [JSON]  ·  look_mariage_v4.py test SRC_rgb48.png SORTIE.jpg couleur|nb EXPO [JSON]
"""
import sys, json, subprocess, numpy as np
from scipy.interpolate import PchipInterpolator
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from look_sony import slog3_vers_lin, M, compresse_gamut
from oklab import vers_lch, depuis_lch

W = np.array([0.2126, 0.7152, 0.0722])
# (diaphs autour de 0,18 ; valeur affichée Rec.709 gamma 2.4)
COURBE = [(-9, 0.0), (-6.5, 0.012), (-5, 0.035), (-3.5, 0.10), (-2, 0.215), (0, 0.42), (1, 0.53), (2, 0.635),
          (3, 0.73), (4, 0.81), (5, 0.875), (6, 0.925), (7.5, 0.965), (10, 0.99)]
COURBE_NB = [(-9, 0.0), (-6, 0.006), (-4.5, 0.03), (-3, 0.10), (-1.5, 0.24), (0, 0.42), (1, 0.545), (2, 0.66),
             (3, 0.755), (4, 0.83), (5, 0.88), (6, 0.915), (8, 0.95), (10, 0.97)]
COUL = dict(inset=0.12, chroma=0.82, olive=0.010, olive_h=108.0, chaud=0.010, chaud_h=75.0, peau_c=0.085, peau_h=55.0,
            ombres_neutres=0.55, courbe=COURBE)
NB = dict(mix=[0.42, 0.48, 0.10], courbe=COURBE_NB)

def fabrique_courbe(pts):
    s, v = np.array(pts, float).T
    f = PchipInterpolator(s, v, extrapolate=True)
    return lambda lin: np.clip(f(np.clip(np.log2(np.maximum(lin, 1e-7) / 0.18), s[0], s[-1])), 0, 1)

lisse = lambda a, b, v: np.clip((v - a) / (b - a), 0, 1) ** 2 * (3 - 2 * np.clip((v - a) / (b - a), 0, 1))
def bande(h, c, d):
    x = np.clip(1 - np.abs((h - c + 180) % 360 - 180) / d, 0, 1); return x * x * (3 - 2 * x)

def scene(x, expo=0.0):
    return compresse_gamut(slog3_vers_lin(x) @ M.T) * (2 ** expo)

def couleur_lin(lin, p=COUL):
    y = (lin @ W)[..., None]
    lin = lin * (1 - p["inset"]) + y * p["inset"]                     # inset : la courbe par canal ne vire pas les teintes
    out = fabrique_courbe(p["courbe"])(lin)
    L, C, h = vers_lch(out)
    C = C / (1 - p["inset"]) * p["chroma"]                           # outset + chroma du look
    wp = bande(h, 52, 26) * lisse(0.25, 0.5, L)                       # peau : teinte ramenée, chroma plafonnée en douceur
    plaf = p["peau_c"] * (1 + 0.5 * np.log1p(np.maximum(C / p["peau_c"] - 1, 0)))
    C = np.where(C > p["peau_c"], C + wp * (plaf - C), C); h = h + wp * 0.4 * ((p["peau_h"] - h + 180) % 360 - 180)
    C = C * (1 - p["ombres_neutres"] * (1 - lisse(0.06, 0.30, L)))    # ombres neutres
    a, b = C * np.cos(np.radians(h)), C * np.sin(np.radians(h))
    wo = lisse(0.10, 0.35, L) * (1 - lisse(0.55, 0.80, L)) * (1 - 0.7 * bande(h, 52, 26))   # olive dans les tons moyens
    wc = lisse(0.65, 0.90, L)                                                                # chaleur dans les hautes lumières
    a = a + wo * p["olive"] * np.cos(np.radians(p["olive_h"])) + wc * p["chaud"] * np.cos(np.radians(p["chaud_h"]))
    b = b + wo * p["olive"] * np.sin(np.radians(p["olive_h"])) + wc * p["chaud"] * np.sin(np.radians(p["chaud_h"]))
    return np.clip(depuis_lch(L, np.hypot(a, b), np.degrees(np.arctan2(b, a)) % 360), 0, 1)

def nb_lin(lin, p=NB):
    g = np.maximum(lin @ np.array(p["mix"]), 0)
    y = fabrique_courbe(p["courbe"])(g)
    return np.stack([y, y, y], -1)

def couleur(x, p=COUL): return couleur_lin(scene(x), p)
def nb(x, p=NB): return nb_lin(scene(x), p)

def ecrit_cube(f, fn, p, n=65, titre=""):
    gg = np.linspace(0, 1, n); b, g, r = np.meshgrid(gg, gg, gg, indexing="ij")
    out = fn(np.stack([r, g, b], -1).reshape(-1, 3), p)
    with open(f, "w") as h:
        h.write(f'TITLE "{titre}"\nLUT_3D_SIZE {n}\n')
        np.savetxt(h, out, fmt="%.6f")

def lit_rgb48(f):
    w, h = map(int, subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height",
                                    "-of", "csv=p=0:s=x", f], capture_output=True, text=True).stdout.strip().split("x")[:2])
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint16).reshape(h, w, 3) / 65535.0

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "test":
        src, sortie, quel, expo = sys.argv[2], sys.argv[3], sys.argv[4], float(sys.argv[5])
        p = dict(COUL if quel == "couleur" else NB); p.update(json.loads(sys.argv[6]) if len(sys.argv) > 6 else {})
        x = lit_rgb48(src)
        lin = scene(x, expo)
        out = couleur_lin(lin, p) if quel == "couleur" else nb_lin(lin, p)
        from PIL import Image
        Image.fromarray((out * 255 + 0.5).astype(np.uint8)).save(sortie, quality=92)
        m = (out @ W) * 255
        print(sortie, "p2 %.0f p50 %.0f p98 %.0f p99.9 %.0f" % tuple(np.percentile(m, [2, 50, 98, 99.9])))
    else:
        p = dict(COUL if mode == "couleur" else NB); p.update(json.loads(sys.argv[3]) if len(sys.argv) > 3 else {})
        ecrit_cube(sys.argv[2], couleur if mode == "couleur" else nb, p, titre=f"P3 mariage-jo V4 {mode}")
        print("écrit", sys.argv[2])
