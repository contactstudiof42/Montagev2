"""Lit les fichiers .psnr (filtre psnr de ffmpeg) et sépare : images d'origine (paires), images inventées (impaires),
image inventée à travers la coupe (i=119). Usage : python3 analyse.py <dossier> noms..."""
import sys, json, re, math
R = sys.argv[1]; res = {}
for nom in sys.argv[2:]:
    p = {}
    for l in open(f"{R}/{nom}.psnr"):
        d = dict(kv.split(":") for kv in l.split()); i = int(d["n"]) - 1
        p[i] = 99.0 if d["psnr_y"] == "inf" else float(d["psnr_y"])
    inv = [p[i] for i in p if i % 2 == 1 and i not in (119,) and i < 235]
    orig = [p[i] for i in p if i % 2 == 0 and i < 235]
    moy = lambda v: round(sum(v) / len(v), 2)
    res[nom] = {"psnr_y_inventees": moy(inv), "min_inventees": round(min(inv), 2), "psnr_y_origine": moy(orig),
                "coupe_i119": round(p[119], 2), "i121": round(p[121], 2)}
    print(nom, res[nom])
json.dump(res, open("resultats.json", "w"), indent=1)
