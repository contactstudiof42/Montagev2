"""Pièce 13 : Lab moyen du visage (masque rendu) et du mur (bande gauche/droite hors personnage), ΔE76 de la peau
par rapport au premier plan du même personnage, et décalage perçu estimé par induction chromatique (hypothèse :
la peau perçue s'écarte du fond de k x (a*, b*) du fond, k = 0,2). Usage : python3 mesure.py <dossier_rendus> v1 v2 v3"""
import sys, json, numpy as np
from PIL import Image
import colour
R = sys.argv[1]; K = 0.2
def lab(im):
    rgb = np.asarray(Image.open(im).convert("RGB"), float) / 255
    return colour.XYZ_to_Lab(colour.sRGB_to_XYZ(rgb))
masque = {p: np.asarray(Image.open(f"{R}/masque-{p}.png").convert("L")) > 128 for p in "AB"}
res = {}
for v in sys.argv[2:]:
    ref = {}
    for k in range(4):
        for p in "AB":
            L = lab(f"{R}/{v}-{k}{p}.png"); m = masque[p]
            peau = L[m].mean(0)
            mur = np.concatenate([L[:60, :60].reshape(-1, 3), L[:60, -60:].reshape(-1, 3)]).mean(0)
            ref.setdefault(p, peau)
            dE = float(np.linalg.norm(peau - ref[p]))
            percue = peau.copy(); percue[1:] -= K * mur[1:]
            res[f"{v}-{k}{p}"] = {"peau_Lab": [round(float(x), 1) for x in peau], "mur_Lab": [round(float(x), 1) for x in mur],
                                  "dE_peau_vs_plan0": round(dE, 2), "peau_percue_ab_estimee": [round(float(x), 1) for x in percue[1:]]}
            print(f"{v}-{k}{p}", res[f"{v}-{k}{p}"])
json.dump(res, open("mesures.json", "w"), indent=1)
