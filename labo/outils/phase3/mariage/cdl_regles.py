# cdl_regles.py expo.txt montage.json : règles prudentes sur les mesures d'expo_plans.py -> cdl.json
# visage détecté : décalage calculé, borné à ±1 diaph ; sans visage : on ne touche que les plans trop sombres (médiane < 0,22 : jusqu'à +0,75 diaph)
# ou trop clairs (médiane > 0,78 : jusqu'à -0,5 diaph) ; un jour blanc reste clair (high key), une nuit reste sombre.
import sys, re, json
D = 0.077; out = {}
J = json.load(open(sys.argv[2])); par_rec = {round(e["rec"], 2): e for e in J["video"] if e["piste"] == 1}
for l in open(sys.argv[1]):
    m = re.match(r"\s*([\d.]+)\s+(\S+)\s+(\S+)\s+visages (\d+)\s+avant ([\d.]+) \(h ([\d.]+)\) -> décalage ([+-][\d.]+) diaph", l)
    if not m: continue
    rec, nom, look, nv, med, hi, dia = float(m[1]), m[2], m[3], int(m[4]), float(m[5]), float(m[6]), float(m[7])
    e = par_rec.get(round(rec, 2))
    if not e: continue
    if nv > 0: d = max(-1.0, min(1.0, dia))
    elif med < 0.22: d = max(0.0, min(0.75, dia))
    elif med > 0.78: d = max(-0.5, min(0.0, dia))
    else: d = 0.0
    if abs(d) >= 0.12: out[f"{e['nom']}|{e['src']}"] = round(d * D, 4)
json.dump(out, open(sys.argv[2].replace("montage.json", "cdl.json"), "w"), indent=0); print(len(out), "plans corrigés")
