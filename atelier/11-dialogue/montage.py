"""Pièce 11 : monte v1 / v2 / v3 depuis les images de ../rendus/11, avec voix synthétiques (A grave, B aigu).
python3 montage.py → ../rendus/11/v*.mp4, planches v*-planche.png, edl.json"""
import json, subprocess
import numpy as np
from PIL import Image, ImageDraw
R = "/home/user/Montagev2/atelier/rendus/11"; SR = 48000; FPS = 25
AV = [("E_avant", 2.0), ("A1_avant", 2.4), ("B1_avant", 1.2), ("A1_avant", 2.0)]
EDL = {
    "v1": AV + [("B1_apres", 2.4), ("A1_apres", 1.6), ("B1_apres", 1.6), ("E_apres", 1.8)],
    "v2": AV + [("B2_apres", 2.4), ("A2_apres", 1.6), ("B2_apres", 1.6), ("E2_apres", 1.8)],
    "v4": AV + [("B2_apres", 1.4), ("E2_apres", 1.4), ("A2_apres", 1.6), ("B2_apres", 2.0), ("A2_apres", 1.0)],
    "v3": AV[:3] + [("A1_avant", 1.2), ("trav", 2.0), ("B2_apres", 2.0), ("A2_apres", 1.6), ("B2_apres", 1.6), ("E2_apres", 1.0)],
}
VOIX = {  # (qui, début, fin) : A domine avant la bascule, B après ; A se tait
    "v1": [("A", .6, 4.3), ("B", 4.5, 5.5), ("A", 5.7, 7.7), ("B", 8.1, 10.3), ("B", 12.1, 13.5)],
    "v3": [("A", .6, 4.3), ("B", 4.5, 5.5), ("A", 5.7, 6.7), ("B", 8.9, 10.7), ("B", 12.4, 13.8)]}
VOIX["v2"] = VOIX["v4"] = VOIX["v1"]


def voix(qui, d, rng):
    """syllabes : impulsions glottiques filtrées, enveloppe par syllabe ; A 115 Hz, B 205 Hz"""
    f0 = 115 if qui == "A" else 205; n = int(d * SR); t = np.arange(n) / SR
    s = np.sign(np.sin(2 * np.pi * f0 * (1 + .04 * np.sin(2 * np.pi * 3 * t)) * t))
    for fc in (700, 1200):  # deux résonances grossières
        k = np.exp(-np.arange(200) / SR * 2 * np.pi * 120) * np.sin(2 * np.pi * fc * np.arange(200) / SR)
        s = s + .5 * np.convolve(s, k, "same") / 20
    env = np.zeros(n); p = 0
    while p < n:
        L = int(rng.uniform(.12, .26) * SR); env[p:p + L] = np.sin(np.pi * np.arange(min(L, n - p)) / L); p += L + int(rng.uniform(.02, .12) * SR)
    return .25 * s * env * (1.0 if qui == "A" else .9)


for v, edl in EDL.items():
    rng = np.random.default_rng(1); a = (np.random.default_rng(9).standard_normal(SR * 15) * .004)  # ton de pièce
    for qui, t0, t1 in VOIX[v]:
        x = voix(qui, t1 - t0, rng); a[int(t0 * SR):int(t0 * SR) + len(x)] += x
    (a.astype(np.float32)).tofile(f"{R}/{v}.f32")
    with open(f"{R}/{v}.txt", "w") as f:  # concat : images fixes ou séquence du travelling
        f.write("ffconcat version 1.0\n")
        for nom, d in edl:
            if nom == "trav":
                for i in range(50): f.write(f"file trav/{i:03d}.png\nduration 0.04\n")
            else: f.write(f"file {nom}.png\nduration {d}\n")
        f.write(f"file {edl[-1][0]}.png\n")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-safe", "0", "-f", "concat", "-i", f"{R}/{v}.txt", "-f", "f32le", "-ar", str(SR), "-ac", "1",
                    "-i", f"{R}/{v}.f32", "-vf", f"fps={FPS},format=yuv420p", "-t", "15", "-c:v", "libx264", "-c:a", "aac", "-b:a", "128k", f"{R}/{v}.mp4"], check=True)
    # planche : une vignette par plan (milieu du plan) avec son temps de début
    W = 240; th = []; t = 0
    for nom, d in edl:
        img = Image.open(f"{R}/trav/024.png" if nom == "trav" else f"{R}/{nom}.png").convert("RGB").resize((W, 135))
        ImageDraw.Draw(img).text((4, 4), f"{t:.1f}s {nom}", fill=(255, 255, 0)); th.append(img); t += d
    pl = Image.new("RGB", (W * 3, 135 * ((len(th) + 2) // 3)))
    for i, im in enumerate(th): pl.paste(im, (W * (i % 3), 135 * (i // 3)))
    pl.save(f"{v}-planche.png", optimize=True)
json.dump(dict(EDL=EDL, VOIX=VOIX), open("edl.json", "w"), indent=1); print("ok")
