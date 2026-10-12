# transcrits_cam.py CAM [motif] : segments Whisper du son des rushes concaténés, rendus au rush et à l'heure Zoom
import sys, re, json
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/son"; cam = sys.argv[1]
pat = re.compile(sys.argv[2], re.I) if len(sys.argv) > 2 else None
tab = json.load(open(f"{T}/cam_{cam}.json"))
def hms(t): t = int(t) % 86400; return f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}"
prev = None
for b in open(f"{T}/cam_{cam}.srt", encoding="utf-8", errors="ignore").read().strip().split("\n\n"):
    L = b.split("\n")
    if len(L) < 3: continue
    h, m, s = L[1][:8].split(":"); t = int(h)*3600 + int(m)*60 + int(s) + int(L[1][9:12])/1000
    txt = " ".join(L[2:]).strip()
    if txt == prev or re.search(r"Sous-titr|Amara|abonnez|Tipeurs", txt, re.I): continue
    prev = txt
    x = next((r for r in tab if r["debut"] <= t < r["debut"] + r["duree"] + 0.5), None)
    if x and (pat is None or pat.search(txt)):
        print(hms(x["t0"] + t - x["debut"]), x["nom"].replace("20260604_", ""), f"{t - x['debut']:.1f}s", txt)
