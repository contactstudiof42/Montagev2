# qui.py HH:MM:SS [HH:MM:SS] : rushes qui couvrent l'instant (ou la plage), avec le temps dans le rush
import sys, json
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"
def sec(h): p = [float(x) for x in h.split(":")]; s = p[0]*3600 + p[1]*60 + (p[2] if len(p) > 2 else 0); return s + (86400 if p[0] < 12 else 0)
a = sec(sys.argv[1]); b = sec(sys.argv[2]) if len(sys.argv) > 2 else a
for x in json.load(open(f"{T}/chrono.json")):
    if x["t0"] <= b and x["t1"] >= a:
        print(f"{x['nom']:16s} {x['cam']:8s} {x['heure']}  dur {x['duree_s']:6.1f}  -> {max(0,a-x['t0']):6.1f}-{min(x['duree_s'],b-x['t0']):6.1f} s du rush  {x.get('objectif','')}")
