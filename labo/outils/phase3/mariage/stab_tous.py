# stab_tous.py montage.json : Gyroflow + mesure avant/après pour chaque plan (piste 1) ; résultats ajoutés à stab.jsonl (reprise possible)
import sys, json, subprocess, os
J = json.load(open(sys.argv[1])); OUT = "/Volumes/SSD FAST/Montage-IA/projets-phase-3/mariage-jo/montage/stab.jsonl"
if isinstance(J, list): J = {"video": J}
fait = set()
if os.path.exists(OUT): fait = {(r["nom"], round(r["src"], 2)) for r in map(json.loads, open(OUT))}
for e in sorted([e for e in J["video"] if e["piste"] == 1], key=lambda e: e["rec"]):
    k = (e["nom"], round(max(0, e["src"]), 2))
    if k in fait: continue
    r = subprocess.run(["/Volumes/SSD FAST/Montage-IA/.venv/bin/python", "-I", "/Volumes/SSD FAST/Montage-IA/labo/outils/phase3/mariage/stab_gyro.py", e["nom"], f"{max(0, e['src']):.2f}", f"{e['dur'] * e['vitesse']:.2f}"], capture_output=True, text=True)
    line = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else json.dumps({"nom": e["nom"], "src": max(0, e["src"]), "erreur": r.stderr[-300:]})
    open(OUT, "a").write(line + "\n"); fait.add(k); print(line[:200], flush=True)
