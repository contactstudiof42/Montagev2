"""Look V5 Sony : la LUT V4 (salle, jour, rouge) suivie d'un PIED DE COURBE plus profond (retour de Diego sur la V4 :
« du bruit visible : des noirs et des zones d'ombre encore trop relevés »).
Le pied agit sur la luminance (teinte et rapport des canaux gardés) : y2 = y^g * y / (y + t) * (1 + t), raccordé à
l'identité au-dessus de Y1 (les tons moyens et hauts ne bougent pas). Le bruit vit dans les ombres : on les pose plus bas.
Usage : look_sony_v5.py ENTREE_V4.cube SORTIE.cube [t=0.05] [y1=0.45] [negatif]
"""
import sys, numpy as np
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from look_sony import lit_cube
W709 = np.array([0.2126, 0.7152, 0.0722])

def pied_v5(rgb, t=0.05, y1=0.45):
    y = np.maximum(rgb @ W709, 1e-6)[..., None]
    y2 = y * y / (y + t) * (1 + t)                       # pied : écrase les ombres, presque rien aux tons moyens
    w = np.clip(y / y1, 0, 1) ** 2 * (3 - 2 * np.clip(y / y1, 0, 1))
    y3 = y2 * (1 - w) + y * w                            # raccord doux à l'identité au-dessus de y1
    return np.clip(rgb * (y3 / y), 0, 1)

if __name__ == "__main__":
    src, out = sys.argv[1], sys.argv[2]
    t = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
    y1 = float(sys.argv[4]) if len(sys.argv) > 4 else 0.45
    neg = len(sys.argv) > 5 and sys.argv[5] == "negatif"
    cube, n = lit_cube(src)
    v = pied_v5(cube.reshape(-1, 3), t, y1)
    if neg: v = 1 - v
    with open(out, "w") as h:
        h.write(f'TITLE "P3 Sony look V5 (V4 + pied t={t})"\nLUT_3D_SIZE {n}\n')
        for r in v: h.write(f"{r[0]:.6f} {r[1]:.6f} {r[2]:.6f}\n")
    print("écrit", out)
