#!/usr/bin/env python3
"""Mesure du keying ffmpeg (chromakey, avec et sans despill) contre l'alpha de vérité terrain (rendu transparent).
Usage : python3 mesure_key.py  (après les rendus de scene_vert.py dans labo/rendus/keying/)"""
import json, os, subprocess
import numpy as np
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "rendus", "keying")
def lire(p, filtre="null"):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-vf", f"{filtre},format=rgba", "-f", "rawvideo", "-pix_fmt", "rgba", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(270, 480, 4).astype(float) / 255
res = {}
for D in ("0.3", "1", "3"):
    gt = lire(f"{R}/d{D}_f0.png")[..., 3]; img = lire(f"{R}/d{D}_f1.png")
    sujet = gt > 0.99
    spill = float(np.mean(np.clip(img[..., 1] - np.maximum(img[..., 0], img[..., 2]), 0, 1)[sujet]) * 255)
    for nom, f in [("chromakey_0.12", "chromakey=0x5CFF7A:0.12:0.06"), ("chromakey_0.20", "chromakey=0x5CFF7A:0.20:0.06"),
                   ("chromakey_0.12+despill", "chromakey=0x5CFF7A:0.12:0.06,despill=type=green")]:
        k = lire(f"{R}/d{D}_f1.png", f)
        a = k[..., 3]
        bord = (gt > 0.02) & (gt < 0.98)
        res[f"D{D}_{nom}"] = {"erreur_alpha_moy_%": round(float(np.abs(a - gt).mean() * 100), 2),
                              "erreur_alpha_bords_%": round(float(np.abs(a - gt)[bord].mean() * 100), 1),
                              "trous_dans_sujet_%": round(float((a[sujet] < 0.5).mean() * 100), 2),
                              "vert_residuel_sujet": round(float(np.mean(np.clip(k[..., 1] - np.maximum(k[..., 0], k[..., 2]), 0, 1)[sujet]) * 255), 2),
                              "debordement_avant_key": round(spill, 2)}
        print(f"D{D}_{nom}", res[f"D{D}_{nom}"])
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resultats.json"), "w"), indent=1)
