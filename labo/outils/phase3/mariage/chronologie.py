# chronologie.py : place chaque rush sur l'horloge du Zoom (décalages mesurés par corrélation audio), écrit chrono.json
import json
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"
DEC = {"DIEGO": 3743.0, "QUENTIN": 838.4, "ROMS 1": 3707.0, "ROMS 2": 3707.0}   # s ; ROMS : à vérifier
r = json.load(open(f"{T}/inventaire.json"))
def hms(t): t = int(round(t)) % 86400; return f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}"
for x in r:
    h, m, s = map(int, x["date"][11:19].split(":")); tc = h*3600 + m*60 + s + (86400 if h < 12 else 0)
    x["t0"] = tc + DEC[x["cam"]]; x["t1"] = x["t0"] + x["duree_s"]; x["heure"] = hms(x["t0"])
r.sort(key=lambda x: x["t0"])
json.dump(r, open(f"{T}/chrono.json", "w"), indent=0, ensure_ascii=False)
# résumé par tranche de 15 min
from collections import defaultdict
d = defaultdict(lambda: defaultdict(float))
for x in r: d[int(x["t0"] // 900)][x["cam"]] += x["duree_s"]
for k in sorted(d): print(hms(k*900), {c: round(v/60, 1) for c, v in d[k].items()})
