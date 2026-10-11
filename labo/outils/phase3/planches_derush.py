"""Planches de dérushage : une ligne par rush (8 vignettes verticales réparties, 16 sur deux lignes si > 20 s),
nom du rush, durée et temps de chaque vignette.
Usage : planches_derush.py inventaire.csv dossier_proxy dossier_sortie [rushes par page]
"""
import csv, subprocess, sys, io
from pathlib import Path
from PIL import Image, ImageDraw
inv, prox, out = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
par_page = int(sys.argv[4]) if len(sys.argv) > 4 else 8
out.mkdir(parents=True, exist_ok=True)
W, H, L, K = 135, 240, 92, 8
rows = list(csv.DictReader(open(inv)))
def frame(p, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", str(p), "-frames:v", "1", "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2",
                        "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
    return Image.open(io.BytesIO(r.stdout)).convert("RGB") if r.stdout else Image.new("RGB", (W, H), "gray")
lignes = []
for r in rows:
    n = r["fichier"].replace("20260929_", "").replace(".MP4", "")
    d = float(r["duree"]); k = 2 * K if d > 20 else K
    ts = [min(d - 0.1, (i + 0.5) * d / k) for i in range(k)]
    ims = [frame(prox / f"{n}.mp4", t) for t in ts]
    for j in range(0, k, K):
        lignes.append((n if j == 0 else "", d, ts[j:j + K], ims[j:j + K]))
page, cur, nb = 1, [], 0
def flush(cur, page):
    c = Image.new("RGB", (L + K * W, len(cur) * (H + 4)), (20, 20, 20)); d = ImageDraw.Draw(c)
    for i, (n, dur, ts, ims) in enumerate(cur):
        y = i * (H + 4)
        if n: d.text((4, y + 4), n, fill="yellow"); d.text((4, y + 20), f"{dur:.1f} s", fill="white")
        for j, (t, im) in enumerate(zip(ts, ims)):
            c.paste(im, (L + j * W, y)); d.text((L + j * W + 3, y + 2), f"{t:.1f}", fill="yellow")
    p = out / f"derush_{page:02d}.jpg"; c.save(p, quality=80); print(p, c.size)
for ln in lignes:
    if ln[0] and nb >= par_page:
        flush(cur, page); page += 1; cur, nb = [], 0
    cur.append(ln); nb += 1 if ln[0] else 0
if cur: flush(cur, page)
