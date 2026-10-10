"""PSNR Y (filtre psnr de ffmpeg) : images inventées hors coupe et hors 2k dernières, pire image inventée,
images d'origine, et image inventée à travers la coupe si donnée. Usage : python3 analyse-reel.py <dossier> <i_coupe|-> [k=2] noms...  (k = facteur ; inventées = i non multiple de k)"""
import sys, json
R, ic = sys.argv[1], sys.argv[2]; ic = None if ic == "-" else int(ic); res = {}
noms = sys.argv[3:]; k = 2
if noms and noms[0].isdigit(): k = int(noms.pop(0))
for nom in noms:
    p = {}
    for l in open(f"{R}/{nom}.psnr"):
        d = dict(kv.split(":") for kv in l.split()); i = int(d["n"]) - 1
        p[i] = 99.0 if d["psnr_y"] == "inf" else float(d["psnr_y"])
    fin = max(p) - 2 * k
    inv = [p[i] for i in p if i % k != 0 and i != ic and i < fin]
    orig = [p[i] for i in p if i % k == 0 and i < fin]
    moy = lambda v: round(sum(v) / len(v), 2)
    res[nom] = {"images": len(p), "psnr_y_inventees": moy(inv), "min_inventees": round(min(inv), 2), "psnr_y_origine": moy(orig)}
    if ic is not None: res[nom]["coupe_i%d" % ic] = round(p[ic], 2)
    print(nom, res[nom])
json.dump(res, open(f"{R}/resultats.json" if k == 2 else f"{R}/resultats-k{k}.json", "w"), indent=1)
