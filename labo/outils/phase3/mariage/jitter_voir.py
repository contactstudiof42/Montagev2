# jitter_voir.py VIDEO T0 [n=12] [crop=0.3] SORTIE.jpg : n images consécutives (50p) recadrées au centre, + différence avec la précédente (le tremblement se voit en saccades)
import sys, subprocess, numpy as np
from PIL import Image, ImageDraw
v, t0, n, c, out = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
W = 480
raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t0), "-i", v, "-frames:v", str(n), "-vf", f"crop=iw*{c}:ih*{c},scale={W}:-2,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
H = len(raw) // n // W; fr = np.frombuffer(raw, np.uint8).reshape(n, H, W)
g = Image.new("L", (n * (W + 2), 2 * H + 2))
for i in range(n):
    g.paste(Image.fromarray(fr[i]), (i * (W + 2), 0))
    if i: g.paste(Image.fromarray(np.clip(np.abs(fr[i].astype(int) - fr[i - 1]) * 3, 0, 255).astype(np.uint8)), (i * (W + 2), H + 2))
g.save(out, quality=80); print(out)
