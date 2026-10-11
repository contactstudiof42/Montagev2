#!/usr/bin/env python3
"""Vérifier un plan long : cherche les coupes par pics de différence d'image (luminance normalisée, 96x52, toutes les images).
Usage : verif_plan.py VIDEO DEBUT_s DUREE_s   (lancer avec .venv/bin/python -I). Confirmé sur Joker (session 2) : trouve les coupes du quai, aucune dans la danse des toilettes.
Limite : une coupe entre deux plans très proches (même décor, même lumière) peut passer ; toujours compléter par une tuile ffmpeg fps=1/2."""
import sys, subprocess, numpy as np
f, a, d = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
W,H=96,52
raw = subprocess.run(["ffmpeg","-v","error","-ss",str(a),"-t",str(d),"-i",f,"-vf",f"scale={W}:{H},format=rgb24","-f","rawvideo","-"],capture_output=True).stdout
fr = np.frombuffer(raw,np.uint8).reshape(-1,H,W,3).astype(float)
# histogramme normalisé en luminance + diff pixel
def hist(x):
    y = x.mean(2); y = (y - y.mean())/(y.std()+1e-6)
    return y
dif = np.array([np.abs(hist(fr[i])-hist(fr[i-1])).mean() for i in range(1,len(fr))])
med = np.array([np.median(dif[max(0,i-6):i+7]) for i in range(len(dif))])
r = dif/(med+1e-3)
fps=24000/1001
pk=[i for i in range(len(dif)) if r[i]>3.5 and dif[i]>0.25 and dif[i]==dif[max(0,i-3):i+4].max()]
print(len(fr),"images ;", len(pk),"coupes probables :", " ".join(f"{a+(i+1)/fps:.1f}" for i in pk))
