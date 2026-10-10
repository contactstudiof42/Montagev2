#!/usr/bin/env python3
"""Vérité terrain pour densite.py : découpage B de l'examen n°11 (doit passer) et deux découpages fautifs."""
import json, random, subprocess, sys
random.seed(11)

def remplir(tranches):
    ev = []
    for a, b, n in tranches:  # de a à b min, n év./min, espacement régulier + gigue
        t = a * 60.0
        while t < b * 60:
            ev.append([round(t, 2), random.choice(["coupe", "coupe", "coupe", "punch", "sfx", "caption"])])
            t += 60.0 / n * random.uniform(0.8, 1.2)
    return ev

# B : courbe visée de l'examen n°11 (20:00 + 15 s d'écran de fin)
B = remplir([(0, 3, 28), (3, 6, 22), (6, 9, 16), (9, 13, 10), (13, 17, 7), (17, 20, 4)])
B += [[6, "promesse"], [180, "relance"], [360, "relance"], [570, "recompense"], [780, "relance"], [960, "recompense"], [1020, "relance"], [1190, "recompense"], [1200, "fin_ecran"]]
cas = {
  "B-examen11": ({"duree": 1215, "evenements": B}, True, 0),
  # fautif : promesse tardive, plateau 6-13 min, densité qui remonte, temps long avant récompense, écran de fin 30 s
  "fautif": ({"duree": 1230, "evenements": remplir([(0, 3, 20), (3, 6, 6), (6, 13, 9), (13, 20, 25)]) + [[40, "promesse"], [180, "relance"], [780, "recompense"], [1200, "fin_ecran"]]}, True, 1),
  # A : densité constante 24/min (sans --decroissante) avec relances toutes les 3 min
  "A-constant": ({"duree": 1215, "evenements": remplir([(0, 20, 24)]) + [[5, "promesse"]] + [[t, "relance"] for t in range(180, 1200, 180)] + [[1200, "fin_ecran"]]}, False, 0),
}
ok = True
for nom, (d, dec, attendu) in cas.items():
    json.dump(d, open(f"densite-{nom}.json", "w"))
    r = subprocess.run([sys.executable, "densite.py", f"densite-{nom}.json", f"densite-{nom}.png"] + (["--decroissante"] if dec else []), capture_output=True, text=True)
    print(f"== {nom} (attendu {'échec' if attendu else 'OK'}) code {r.returncode}\n{r.stdout}")
    ok &= (r.returncode == attendu)
print("VÉRITÉ TERRAIN :", "toutes conformes" if ok else "ÉCART")
