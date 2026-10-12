# stab_v4.py montage_V4.json : stabilisation de la V4, plan par plan, sur le passage exact utilisé.
# 1) tremblement du rush brut (tremblement.py : reste après lissage de 0,4 s, px ramenés à 1080 de large) ;
# 2) au-delà des seuils (moyenne > 1,5 px ou pic > 4 px), Gyroflow (stab_gyro.py : synchro auto sur une plage courte, zoom fixe ≤ 115 %)
#    puis mesure du FICHIER STABILISÉ sur la même plage, et contrôle que le mouvement voulu est gardé (vitesse_conservee 0,7-1,4) ;
# 3) on garde le stabilisé seulement s'il réduit le tremblement d'au moins 25 % ; sinon le brut, et le plan est signalé
#    (leviers suivants : ralentir, couper là où il est calme, remplacer : `montage-regard`, point 3).
# Sortie : stab_V4.json {"nom|src": {...}} ; reprise possible (les plans déjà mesurés sont gardés).
import sys, json, subprocess, os
J = json.load(open(sys.argv[1])); MD = os.path.dirname(os.path.abspath(sys.argv[1]))
INVERSE = "--inverse" in sys.argv                     # second passage en parallèle, depuis la fin du film, dans son propre fichier
OUT = f"{MD}/stab_V4{'_b' if INVERSE else ''}.json"; AUTRE = f"{MD}/stab_V4{'' if INVERSE else '_b'}.json"
R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"; PY = "/Volumes/SSD FAST/Montage-IA/.venv/bin/python"; L = "/Volumes/SSD FAST/Montage-IA/labo/outils"
INV = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json"))}
S = json.load(open(OUT)) if os.path.exists(OUT) else {}
def trem(v, t0, t1, avant=None):
    a = [PY, "-I", f"{L}/tremblement.py", v, f"{t0:.2f}", f"{t1:.2f}"] + (["--avant", avant] if avant else [])
    out = subprocess.run(a, capture_output=True, text=True).stdout.strip().splitlines()
    r = json.loads(out[0]) if out else {}
    if avant and len(out) > 1: r.update(json.loads(out[1]))
    return r
for e in sorted([e for e in J["video"] if e["piste"] == 1 and not e.get("gel")], key=lambda e: e["rec"], reverse=INVERSE):
    k = f"{e['nom']}|{e['src']}"
    deja = json.load(open(AUTRE)) if os.path.exists(AUTRE) else {}
    if k in S or k in deja: continue
    f = f"{R}/{INV[e['nom']]['fichier']}"; d = e["dur"] * e["vitesse"]
    av = trem(f, e["src"], e["src"] + d)
    m, p = av.get("moyenne_px", av.get("moyenne", 0)), av.get("pic_px", av.get("pic", 0))
    r = {"rec": e["rec"], "avant": av, "garder": False}
    if m > 1.5 or p > 4.0:
        g = json.loads(subprocess.run([PY, "-I", f"{L}/phase3/mariage/stab_gyro.py", e["nom"], f"{e['src']}", f"{d}", "0.5"], capture_output=True, text=True, timeout=1500).stdout.strip().splitlines()[-1])
        if g.get("fichier"):
            ap = trem(g["fichier"], e["src"] - g["debut_plage"], e["src"] - g["debut_plage"] + d)
            ma, pa = ap.get("moyenne_px", ap.get("moyenne", 0)), ap.get("pic_px", ap.get("pic", 0))
            r.update(fichier=g["fichier"], debut_plage=g["debut_plage"], apres=ap)
            r["garder"] = bool(ma < 0.75 * m and pa < max(p, 1e-6))
    S[k] = r; json.dump(S, open(OUT, "w"), indent=1)
    print(f"{e['rec']:7.2f} {e['nom']:16s} avant {m:.2f}/{p:.2f}" + (f"  après {r['apres'].get('moyenne_px', r['apres'].get('moyenne', 0)):.2f}/{r['apres'].get('pic_px', r['apres'].get('pic', 0)):.2f}  garder={r['garder']}" if "apres" in r else ""), flush=True)
