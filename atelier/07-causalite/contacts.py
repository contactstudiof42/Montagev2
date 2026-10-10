"""Lit sim.json et en déduit les événements causaux (image de départ de chaque maillon)."""
import json, sys, math
d = json.load(open(sys.argv[1])); rec = d["rec"]; F1 = d["frames"][0]
def first(pred):
    for i, r in enumerate(rec):
        if pred(r): return F1 + i
    return None
ev = {}
b0 = rec[0]["bille"][0]
ev["bille_part"] = first(lambda r: abs(r["bille"][0][0] - b0[0]) > 0.003)
names = sorted(k for k in rec[0] if k.startswith("domino"))
for k in names:
    x0 = rec[0][k][0][0]
    ev[k + "_bouge"] = first(lambda r, k=k, x0=x0: abs(r[k][0][0] - x0) > 0.002 or abs(r[k][1][1]) > 0.03)
    ev[k + "_couche"] = first(lambda r, k=k: abs(r[k][1][1]) > math.radians(70))
t0 = rec[0]["tasse"][0]
ev["tasse_bouge"] = first(lambda r: abs(r["tasse"][0][0] - t0[0]) > 0.002)
ev["tasse_quitte"] = first(lambda r: r["tasse"][0][2] < t0[2] - 0.02)
ev["tasse_sol"] = first(lambda r: r["tasse"][0][2] < 0.08)
last = rec[-1]
ev["fin_tasse_z"] = round(last["tasse"][0][2], 3); ev["fin_bille_xyz"] = [round(v, 3) for v in last["bille"][0]]
print(json.dumps(ev, indent=1))
json.dump(ev, open(sys.argv[2], "w"), indent=1) if len(sys.argv) > 2 else None
