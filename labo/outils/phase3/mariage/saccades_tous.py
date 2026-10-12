# saccades_tous.py montage.json : indice de saccade de chaque plan (rush brut, plage utilisée), en parallèle ; saccades.json
import sys, json, subprocess
from concurrent.futures import ThreadPoolExecutor
J = json.load(open(sys.argv[1])); R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
INV = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json"))}
ev = sorted([e for e in J["video"] if e["piste"] == 1], key=lambda e: e["rec"])
def f(e):
    t0 = max(0, e["src"]); t1 = t0 + max(0.5, e["dur"] * e["vitesse"])
    r = subprocess.run(["/Volumes/SSD FAST/Montage-IA/.venv/bin/python", "-I", "/Volumes/SSD FAST/Montage-IA/labo/outils/phase3/mariage/saccades.py", f"{R}/{INV[e['nom']]['fichier']}", f"{t0:.2f}", f"{t1:.2f}"], capture_output=True, text=True)
    try: return dict(rec=e["rec"], nom=e["nom"], src=e["src"], dur=e["dur"], **json.loads(r.stdout.strip().splitlines()[-1]), note=e.get("note", "")[:40])
    except Exception: return dict(rec=e["rec"], nom=e["nom"], erreur=r.stderr[-200:])
with ThreadPoolExecutor(3) as ex: res = list(ex.map(f, ev))
json.dump(res, open(sys.argv[1].replace("montage.json", "saccades.json"), "w"), indent=0, ensure_ascii=False)
for d in sorted(res, key=lambda d: -d.get("saccade", 0)): print(f"{d['rec']:7.2f} {d['nom']:16s} sacc {d.get('saccade')} vit {d.get('vitesse')} {d.get('note','')}")
