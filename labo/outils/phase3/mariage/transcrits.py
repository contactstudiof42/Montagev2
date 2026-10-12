# transcrits.py [motif] : segments Whisper des fichiers Zoom remis sur l'horloge du Zoom (hallucinations répétées filtrées)
import sys, re, glob, os
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/son"
Z = {"040626-161726": 58646, "040626-175038": 64238, "040626-192350": 69830, "040626-205702": 75422, "040626-223014": 81014, "050626-000326": 86400 + 206, "REC052": 63115.08}
pat = re.compile(sys.argv[1], re.I) if len(sys.argv) > 1 else None
def hms(t): t = int(t) % 86400; return f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}"
out = []
for n, t0 in Z.items():
    f = f"{T}/{n}.srt"
    if not os.path.exists(f): continue
    for b in open(f, encoding="utf-8", errors="ignore").read().strip().split("\n\n"):
        L = b.split("\n")
        if len(L) < 3: continue
        h, m, s = L[1][:8].split(":"); ms = int(L[1][9:12]); t = t0 + int(h)*3600 + int(m)*60 + int(s) + ms/1000
        txt = " ".join(L[2:]).strip()
        if re.search(r"Sous-titr|Amara|merci d'avoir regard", txt, re.I): continue
        out.append((t, n, txt))
out.sort(); prev = None
for t, n, txt in out:
    if txt == prev: continue
    prev = txt
    if pat is None or pat.search(txt): print(hms(t), "HF" if n == "REC052" else "Z ", txt)
