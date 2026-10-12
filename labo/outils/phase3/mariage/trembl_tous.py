# trembl_tous.py montage.json : tremblement de chaque plan de la piste 1 sur la plage utilisée (rush brut), sortie JSON + tableau
import sys, json, subprocess, re
J = json.load(open(sys.argv[1])); R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
INV = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json"))}
out = []
for e in sorted([e for e in J["video"] if e["piste"] == 1], key=lambda e: e["rec"]):
    f = f"{R}/{INV[e['nom']]['fichier']}"; t0 = max(0, e["src"]); t1 = t0 + e["dur"] * e["vitesse"]
    if t1 - t0 < 0.5: t0 = max(0, t0 - 0.25); t1 = t0 + 0.6
    r = subprocess.run(["/Volumes/SSD FAST/Montage-IA/.venv/bin/python", "-I", "/Volumes/SSD FAST/Montage-IA/labo/outils/tremblement.py", f, f"{t0:.2f}", f"{t1:.2f}"], capture_output=True, text=True).stdout
    try: jj = json.loads(r.strip().splitlines()[-1])
    except Exception: jj = {}
    d = dict(rec=e["rec"], nom=e["nom"], src=e["src"], dur=e["dur"], moy=jj.get("moyenne"), pic=jj.get("pic"), note=e.get("note", "")[:50])
    out.append(d); print(f"{d['rec']:7.2f} {d['nom']:16s} moy {d['moy']}  pic {d['pic']}  {d['note']}", flush=True)
json.dump(out, open(sys.argv[1].replace("montage.json", "tremblement.json"), "w"), indent=0, ensure_ascii=False)
