"""Pièce 34 : python3 mesure.py EVENEMENTS.json [DUREE] -> trous (s) sans aucun événement, par type."""
import sys, json
E = json.load(open(sys.argv[1])); D = float(sys.argv[2]) if len(sys.argv) > 2 else 112.0
def trous(types):
    occ = sorted((e['t'], e.get('fin', e['t'] + 0.3)) for e in E if e['type'] in types); out, fin = [], 0.0
    for a, b in occ:
        if a > fin: out.append((round(fin, 1), round(a - fin, 1)))
        fin = max(fin, b)
    if D > fin: out.append((round(fin, 1), round(D - fin, 1)))
    return sorted(out, key=lambda x: -x[1])
for nom, ty in (('tout', {'replique', 'image', 'son', 'coupe'}), ('image seule', {'image', 'coupe'})):
    t = trous(ty); print(f"{nom:12s} trous > 8 s : {[x for x in t if x[1] > 8]}  | plus long {t[0]}")
