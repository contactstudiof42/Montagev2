"""Détourage d'une personne par de vrais modèles de segmentation, locaux et gratuits (retour de Diego du 2026-10-11 :
la carte de profondeur donne des bords grossiers).

Modèles (rembg, ONNX) : birefnet-portrait, birefnet-general, u2net_human_seg, isnet-general-use.
Deux passes : 1) image entière -> boîte du sujet ; 2) recadrage serré (marge 8 %) segmenté à la définition du modèle,
puis recollé : le modèle voit le sujet en grand, les bords gagnent en définition.
Option --affine : filtre guidé (rayon r, eps) sur l'image pour coller le bord aux vrais contours (cheveux).

Usage : python detourage_modeles.py SOURCE.png SORTIE_DIR [--modeles a,b] [--affine]
Sorties : SORTIE_DIR/<base>_<modele>.png (masque 8 bits, pleine définition)
"""
import sys, os, argparse
import numpy as np
from PIL import Image


def filtre_guide(I, p, r, eps):
    """Filtre guidé (He et al.) en niveaux de gris, I et p dans [0,1]."""
    import cv2
    m = lambda x: cv2.boxFilter(x, -1, (r, r))
    mI, mp = m(I), m(p)
    a = (m(I * p) - mI * mp) / (m(I * I) - mI * mI + eps)
    b = mp - a * mI
    return np.clip(m(a) * I + m(b), 0, 1)


def segmente(session, im):
    from rembg import remove
    out = remove(im, session=session, only_mask=True, post_process_mask=False)
    return np.asarray(out.convert("L"), np.float32) / 255


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source"); ap.add_argument("sortie")
    ap.add_argument("--modeles", default="birefnet-portrait,birefnet-general,u2net_human_seg,isnet-general-use")
    ap.add_argument("--affine", action="store_true")
    a = ap.parse_args()
    from rembg import new_session
    os.makedirs(a.sortie, exist_ok=True)
    im = Image.open(a.source).convert("RGB")
    W, H = im.size
    base = os.path.splitext(os.path.basename(a.source))[0]
    for nom in a.modeles.split(","):
        s = new_session(nom)
        m1 = segmente(s, im)
        ys, xs = np.where(m1 > 0.5)
        if len(xs) == 0:
            print(nom, "rien trouvé"); continue
        mx, my = int((xs.max() - xs.min()) * 0.08) + 40, int((ys.max() - ys.min()) * 0.08) + 40
        x0, x1 = max(0, xs.min() - mx), min(W, xs.max() + mx); y0, y1 = max(0, ys.min() - my), min(H, ys.max() + my)
        crop = im.crop((x0, y0, x1, y1))
        m2 = segmente(s, crop)
        m = np.zeros((H, W), np.float32)
        m[y0:y1, x0:x1] = m2
        if a.affine:
            g = np.asarray(im.convert("L"), np.float32) / 255
            m = filtre_guide(g, m, 9, 1e-4)
        Image.fromarray((m * 255).astype(np.uint8)).save(os.path.join(a.sortie, f"{base}_{nom}{'_af' if a.affine else ''}.png"))
        print(nom, "boîte", (x0, y0, x1, y1), flush=True)


main()
