# verif_edl.py montage.json : chaque plan tient-il dans son rush (src >= 0, src + dur*vitesse <= durée) ? doublons de moments ?
import sys, json
J = json.load(open(sys.argv[1])); INV = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json"))}
pb = 0; vus = {}
for e in J["video"]:
    d = INV[e["nom"]]["duree_s"]; fin = e["src"] + e["dur"] * e["vitesse"]
    if e["src"] < 0 or fin > d - 0.02: print(f"HORS RUSH {e['rec']:.2f} {e['nom']} src {e['src']:.2f} fin {fin:.2f} > {d:.2f}"); pb += 1
    for (a, b, r) in vus.get(e["nom"], []):
        if min(fin, b) - max(e["src"], a) > 0.05: print(f"DOUBLON {e['nom']} [{e['src']:.2f}-{fin:.2f}] à {e['rec']:.2f} recoupe [{a:.2f}-{b:.2f}] à {r:.2f}"); pb += 1
    vus.setdefault(e["nom"], []).append((e["src"], fin, e["rec"]))
recs = sorted((e["rec"], e["rec"] + e["dur"]) for e in J["video"] if e["piste"] == 1)
for (a0, a1), (b0, b1) in zip(recs, recs[1:]):
    if b0 < a1 - 0.01: print(f"CHEVAUCHEMENT {a0:.2f}-{a1:.2f} / {b0:.2f}"); pb += 1
    elif b0 > a1 + 0.01: print(f"TROU {a1:.2f}-{b0:.2f}")
print("problèmes :", pb)
