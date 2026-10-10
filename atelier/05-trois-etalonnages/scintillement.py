"""Pièce 05 — la clé du qualifieur scintille-t-elle en mouvement ?
Lancer : python3 scintillement.py <version.json> <direction> <dossier_images> [sortie.mp4]
Applique l'arbre de nodes à chaque image, mesure image par image :
- surface de la clé (% de l'image), et sa variation d'une image à la suivante ;
- « scintillement » = moyenne |clé(t) - clé(t-1)| sur les pixels où la clé vaut > 0,05 à t ou t-1,
  comparé à la même mesure sur la luminance source (bruit du rendu / débruiteur) comme référence.
"""
import json, sys, os, glob, subprocess
import numpy as np
from PIL import Image
import grade

cfg = json.load(open(sys.argv[1])); arbre = cfg["directions"][sys.argv[2]]
fichiers = sorted(glob.glob(os.path.join(sys.argv[3], "[0-9][0-9][0-9][0-9].png")))
sortie = sys.argv[4] if len(sys.argv) > 4 else None
qual = [n for n in arbre if n["op"] == "secondaire"][-1]
prev_k = prev_y = None; R = []
tmp = os.path.join(sys.argv[3], "grade"); os.makedirs(tmp, exist_ok=True)
for i, f in enumerate(fichiers):
    x0 = np.asarray(Image.open(f).convert("RGB"), dtype=np.float64) / 255
    x = x0
    for n in arbre:
        x = grade.NODES[n["op"]](x, source=x0, **n)
    Image.fromarray((x * 255 + 0.5).astype(np.uint8)).save(os.path.join(tmp, f"{i:04d}.png"))
    k = grade.masque_qualif(x0, qual["h0"], qual["h1"], qual["s_min"], qual["v_min"], qual.get("doux", 8))
    y = grade.luma(x0)
    m = dict(image=os.path.basename(f), cle_pct=round(float((k > 0.5).mean() * 100), 3))
    if prev_k is not None:
        zone = (k > 0.05) | (prev_k > 0.05)
        m["scint_cle"] = round(float(np.abs(k - prev_k)[zone].mean()), 4)
        m["scint_luma_src"] = round(float(np.abs(y - prev_y)[zone].mean()), 4)
    R.append(m); prev_k, prev_y = k, y
sc = [r["scint_cle"] for r in R[1:]]; sl = [r["scint_luma_src"] for r in R[1:]]
print(json.dumps(dict(images=len(R), cle_pct_debut=R[0]["cle_pct"], cle_pct_fin=R[-1]["cle_pct"],
                      scint_cle_moy=round(float(np.mean(sc)), 4), scint_cle_max=max(sc),
                      scint_luma_src_moy=round(float(np.mean(sl)), 4)), indent=1))
json.dump(R, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "scintillement-mesures.json"), "w"), indent=1)
if sortie:
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", "25", "-i", os.path.join(tmp, "%04d.png"),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", sortie], check=True)
