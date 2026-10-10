"""Pièce 14 v2 : (1) serré à -1 diaphragme (linéaire x 0,5) ; (2) B2 « honnête » : coupes sur les points morts,
de plus en plus espacées à mesure que l'amplitude baisse (1 sur 1, puis 1 sur 2, puis 1 sur 4), whoosh proportionnel à l'amplitude.
Usage : python3 v2.py <rendus14>"""
import json, math, os, subprocess, sys, wave, numpy as np
from PIL import Image
R = sys.argv[1]; FPS, N = 25, 375
os.makedirs(f"{R}/serre2", exist_ok=True)
for f in range(1, N + 1):
    a = np.asarray(Image.open(f"{R}/serre/{f:04d}.png").convert("RGB"), float) / 255
    lin = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4) * 0.5
    s = np.where(lin <= 0.0031308, lin * 12.92, 1.055 * lin ** (1 / 2.4) - 0.055)
    Image.fromarray((np.clip(s, 0, 1) * 255 + 0.5).astype(np.uint8)).save(f"{R}/serre2/{f:04d}.png")
bal = json.load(open(f"{R}/large/balancier.json")); morts = bal["points_morts"]
cuts = [m for i, m in enumerate(morts) if (m < 6 * FPS) or (m < 11 * FPS and i % 2 == 0) or (i % 4 == 0)]
bornes = [1] + cuts + [N + 1]
edl = [("large" if i % 2 == 0 else "serre2", bornes[i], bornes[i + 1] - 1) for i in range(len(bornes) - 1)]
json.dump(edl, open("edl-B2.json", "w")); print("B2", len(edl), "plans", [round((b - a + 1) / FPS, 1) for _, a, b in edl])
A = json.load(open("edl-A.json")); A = [("serre2" if c == "serre" else c, a, b) for c, a, b in A]
json.dump(A, open("edl-A2.json", "w"))
sys.argv = ["", R]; src = open("montage.py").read()
son = src[src.index("sr = 48000"):src.index("for nom, edl, wh in")]
exec(son)
for nom, e, wh in (("A2", A, False), ("B2", edl, True)):
    d = f"{R}/seq-{nom}"; os.makedirs(d, exist_ok=True); i = 0
    for cam, a0, b0 in e:
        for f in range(a0, b0 + 1):
            i += 1; dst = f"{d}/{i:04d}.png"
            if os.path.lexists(dst): os.remove(dst)
            os.symlink(f"{R}/{cam}/{f:04d}.png", dst)
    x = son_fn(e, wh) if False else son(e, wh)
    with wave.open(f"{R}/{nom}.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(48000); w.writeframes(x.tobytes())
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", "25", "-i", f"{d}/%04d.png", "-i", f"{R}/{nom}.wav", "-shortest",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-c:a", "aac", f"{R}/{nom}.mp4"], check=True)
