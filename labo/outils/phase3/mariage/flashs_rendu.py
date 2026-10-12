# flashs_rendu.py VIDEO T0 T1 : sur un rendu 25p, images où la luminance d'une bande horizontale augmente puis redescend (> 8 %) en <= 3 images
# (un vrai flash : aller-retour), à distinguer d'une coupe (saut sans retour)
import sys, subprocess, numpy as np
v, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(a), "-t", str(b - a), "-i", v, "-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
f = np.frombuffer(raw, np.uint8).reshape(-1, 90, 160).astype(float); bd = f.reshape(len(f), 9, 10, 160).mean(axis=(2, 3))
out = []
for i in range(1, len(bd) - 1):
    for k in (1, 2, 3):
        if i + k >= len(bd): break
        up = (bd[i] - bd[i - 1]).max(); back = (bd[i] - bd[i + k]).max()
        if up > 20 and back > 20: out.append(round(a + i / 25, 2)); break
print("allers-retours :", out)
