"""Look V4 Sony : le tirage 2383 de `look_sony.py`, plus une SÉPARATION DES TEINTES (retour de Diego sur la V3 :
« bouillie », « pâté de couleurs » : peau, décor, chouchou rose et écouteur tombaient tous entre 28 et 41° de teinte OkLCh).

Étapes ajoutées, dans l'ordre :
  0. Balance des blancs avant le film (GAINS linéaires) : la lumière de salle (tungstène) était gardée trop chaude.
  1. Après le film, en OkLCh (L, C, h) :
     - chroma réduite dans les tons sombres (le décor recule, le sujet éclairé ressort) : SOMBRE ;
     - hautes lumières désaturées (écouteurs, néons, boîtiers : blancs propres) : HAUTES ;
     - bande peau (h ~ 40-75°) : chroma plafonnée en douceur (PEAU_C) et teinte ramenée vers PEAU_H (naturelle) ;
     - bande jaune-ambre (h ~ 75-100°, le bois et le tungstène du décor) : chroma réduite (AMBRE_C) ;
     - ombres légèrement froides (FROID) : contraste de couleur sujet chaud / fond neutre-froid.
Usage : look_sony_v4.py SORTIE.cube (réglages dans PARAMS ou en JSON en 2e argument).
"""
import sys, json, numpy as np
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from look_sony import look
from oklab import vers_lch, depuis_lch

PARAMS = dict(expo=0.25, force=1.0, sat=1.05, pied=0.08, ombres=0.5, gains=[0.90, 1.0, 1.12],
              sombre=0.55, hautes=0.6, peau_c=0.085, peau_h=55.0, ambre_c=0.6, froid=0.012)

def bande(h, centre, demi):  # poids 0-1 en cloche douce autour d'une teinte (degrés, circulaire)
    d = np.abs((h - centre + 180) % 360 - 180)
    return np.clip(1 - d / demi, 0, 1) ** 2 * (3 - 2 * np.clip(1 - d / demi, 0, 1))

def look4(x, p=PARAMS):
    out = look(x, expo=p["expo"], force=p["force"], sat=p["sat"], gains=tuple(p["gains"]), pied=p["pied"], ombres=p["ombres"])
    L, C, h = vers_lch(out)
    lisse = lambda a, b, v: np.clip((v - a) / (b - a), 0, 1) ** 2 * (3 - 2 * np.clip((v - a) / (b - a), 0, 1))
    # 1. sombres moins saturés
    C = C * (p["sombre"] + (1 - p["sombre"]) * lisse(0.18, 0.5, L))
    # 2. hautes lumières propres
    C = C * (1 - p["hautes"] * lisse(0.80, 0.97, L))
    # 3. peau : chroma plafonnée en douceur, teinte vers PEAU_H
    wp = bande(h, 52, 28) * lisse(0.3, 0.55, L)
    plafond = p["peau_c"] * (1 + np.log1p(np.maximum(C / p["peau_c"] - 1, 0)) * 0.5)
    C = np.where(C > p["peau_c"], C + wp * (plafond - C), C)
    h = h + wp * 0.5 * ((p["peau_h"] - h + 180) % 360 - 180)
    # 4. (pas de bande rose : le rouge de la salle a la même teinte que le chouchou ; la balance des blancs suffit)
    # 5. ambre du décor
    C = C * (1 - (1 - p["ambre_c"]) * bande(h, 88, 18))
    out = depuis_lch(L, C, h % 360)
    # 6. ombres légèrement froides (en RVB, après)
    w = (1 - lisse(0.08, 0.40, L))[..., None]
    out = out + w * p["froid"] * np.array([-1.0, 0.1, 1.2])
    return np.clip(out, 0, 1)

def ecrit_cube(f, p=PARAMS, n=33):
    g = np.linspace(0, 1, n); b, gg, r = np.meshgrid(g, g, g, indexing="ij")
    out = look4(np.stack([r, gg, b], -1).reshape(-1, 3), p)
    with open(f, "w") as h:
        h.write(f'TITLE "P3 Sony look V4 2383 separation"\nLUT_3D_SIZE {n}\n')
        for v in out: h.write(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")

if __name__ == "__main__":
    p = dict(PARAMS); p.update(json.loads(sys.argv[2]) if len(sys.argv) > 2 else {})
    ecrit_cube(sys.argv[1], p); print("écrit", sys.argv[1], p)
