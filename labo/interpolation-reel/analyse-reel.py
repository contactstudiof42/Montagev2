"""PSNR Y (filtre psnr de ffmpeg) : images inventées (impaires) hors coupe et hors 4 dernières, pire image inventée,
images d'origine, et image inventée à travers la coupe si donnée. Usage : python3 analyse-reel.py <dossier> <i_coupe|-> noms..."""
import sys, json
R, ic = sys.argv[1], sys.argv[2]; ic = None if ic == "-" else int(ic); res = {}
for nom in sys.argv[3:]:
    p = {}
    for l in open(f"{R}/{nom}.psnr"):
        d = dict(kv.split(":") for kv in l.split()); i = int(d["n"]) - 1
        p[i] = 99.0 if d["psnr_y"] == "inf" else float(d["psnr_y"])
    fin = max(p) - 4
    inv = [p[i] for i in p if i % 2 == 1 and i != ic and i < fin]
    orig = [p[i] for i in p if i % 2 == 0 and i < fin]
    moy = lambda v: round(sum(v) / len(v), 2)
    res[nom] = {"images": len(p), "psnr_y_inventees": moy(inv), "min_inventees": round(min(inv), 2), "psnr_y_origine": moy(orig)}
    if ic is not None: res[nom]["coupe_i%d" % ic] = round(p[ic], 2)
    print(nom, res[nom])
json.dump(res, open(f"{R}/resultats.json", "w"), indent=1)
