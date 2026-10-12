"""Looks du projet mariage-jo (S-Log3 / S-Gamut3.Cine -> Rec.709), cuits en LUT .cube (un nœud dans Resolve).
COULEUR : tirage 2383 (look_sony.look), puis en OkLCh : chroma réduite (film peu saturé), dominante olive douce dans les tons
moyens, peau protégée (teinte ~55°, chroma plafonnée), hautes lumières tenues (épaule douce sur la luminance), noirs neutres.
NB : luminance d'un mélange de canaux (rouge renforcé : peau lumineuse, pierre orange éclaircie), tirage 2383 appliqué au gris
(courbe de film), épaule douce, noirs profonds, aucune teinte.
Usage : look_mariage.py couleur|nb SORTIE.cube [JSON des réglages]   ou   look_mariage.py test IMAGE.png SORTIE.png couleur|nb [JSON]
"""
import sys, json, numpy as np
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from look_sony import look, slog3_vers_lin, M, compresse_gamut, lin_vers_cineon, applique_cube, FILMC
from oklab import vers_lch, depuis_lch

COUL = dict(expo=0.0, force=0.85, gains=[1.0, 1.0, 1.0], pied=0.05, chroma=0.80, olive=0.012, olive_h=105.0,
            peau_c=0.075, peau_h=55.0, epaule=0.85, ombres_neutres=0.6)
NB = dict(expo=0.15, mix=[0.42, 0.48, 0.10], force=0.9, pied=0.04, epaule=0.88, gamma=1.0)

lisse = lambda a, b, v: np.clip((v - a) / (b - a), 0, 1) ** 2 * (3 - 2 * np.clip((v - a) / (b - a), 0, 1))
def bande(h, c, d):
    x = np.clip(1 - np.abs((h - c + 180) % 360 - 180) / d, 0, 1); return x * x * (3 - 2 * x)

def epaule(y, k):  # au-dessus de k, compresse doucement vers 1 (les blancs gardent leur matière)
    return np.where(y < k, y, k + (1 - k) * np.tanh((y - k) / (1 - k)))

def couleur(x, p=COUL):
    out = look(x, expo=p["expo"], force=p["force"], sat=1.0, gains=tuple(p["gains"]), pied=p["pied"], ombres=0)
    L, C, h = vers_lch(out)
    C = C * p["chroma"]
    # peau : teinte vers peau_h, chroma plafonnée en douceur
    wp = bande(h, 52, 26) * lisse(0.25, 0.5, L)
    plaf = p["peau_c"] * (1 + 0.5 * np.log1p(np.maximum(C / p["peau_c"] - 1, 0)))
    C = np.where(C > p["peau_c"], C + wp * (plaf - C), C); h = h + wp * 0.4 * ((p["peau_h"] - h + 180) % 360 - 180)
    # hautes lumières moins saturées (robe blanche propre), ombres neutres
    C = C * (1 - 0.5 * lisse(0.82, 0.98, L)) * (1 - p["ombres_neutres"] * (1 - lisse(0.08, 0.30, L)))
    out = depuis_lch(L, C, h % 360)
    # dominante olive dans les tons moyens (ajout en Lab, hors peau)
    a0, b0 = np.cos(np.radians(p["olive_h"])), np.sin(np.radians(p["olive_h"]))
    Lm, Cm, hm = vers_lch(out)
    w = (lisse(0.15, 0.45, Lm) * (1 - lisse(0.6, 0.9, Lm)) * (1 - 0.7 * bande(hm, 52, 26)))
    a = Cm * np.cos(np.radians(hm)) + w * p["olive"] * a0; b = Cm * np.sin(np.radians(hm)) + w * p["olive"] * b0
    out = depuis_lch(Lm, np.hypot(a, b), np.degrees(np.arctan2(b, a)) % 360)
    y = np.maximum(out @ np.array([0.2126, 0.7152, 0.0722]), 1e-6)[..., None]
    return np.clip(out * epaule(y, p["epaule"]) / y, 0, 1)

def nb(x, p=NB):
    lin = compresse_gamut(slog3_vers_lin(x) @ M.T) * (2 ** p["expo"])
    g = np.maximum(lin @ np.array(p["mix"]), 0)[..., None] * np.ones(3)
    film = applique_cube(lin_vers_cineon(g), *FILMC)
    y = film @ np.array([0.2126, 0.7152, 0.0722])                 # le 2383 teinte légèrement : on ne garde que sa luminance
    y = p["force"] * y + (1 - p["force"]) * np.clip(g[..., 0], 0, 1) ** (1 / 2.4)
    if p["pied"] > 0: y = y * y / (y + p["pied"]) * (1 + p["pied"])
    y = epaule(y, p["epaule"]) ** p["gamma"]
    return np.clip(np.stack([y, y, y], -1), 0, 1)

def ecrit_cube(f, fn, p, n=33, titre=""):
    gg = np.linspace(0, 1, n); b, g, r = np.meshgrid(gg, gg, gg, indexing="ij")
    out = fn(np.stack([r, g, b], -1).reshape(-1, 3), p)
    with open(f, "w") as h:
        h.write(f'TITLE "{titre}"\nLUT_3D_SIZE {n}\n'); [h.write(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n") for v in out]

if __name__ == "__main__":
    from PIL import Image
    if sys.argv[1] == "test":
        mode = sys.argv[4]; p = dict(COUL if mode == "couleur" else NB); p.update(json.loads(sys.argv[5]) if len(sys.argv) > 5 else {})
        import cv2
        im = cv2.imread(sys.argv[2], cv2.IMREAD_UNCHANGED)[..., ::-1].astype(np.float64) / 65535
        out = (couleur if mode == "couleur" else nb)(im.reshape(-1, 3), p).reshape(im.shape)
        Image.fromarray((out * 255 + 0.5).astype(np.uint8)).save(sys.argv[3]); print(sys.argv[3])
    else:
        mode = sys.argv[1]; p = dict(COUL if mode == "couleur" else NB); p.update(json.loads(sys.argv[3]) if len(sys.argv) > 3 else {})
        ecrit_cube(sys.argv[2], couleur if mode == "couleur" else nb, p, titre=f"P3 mariage-jo {mode}"); print("écrit", sys.argv[2], p)
