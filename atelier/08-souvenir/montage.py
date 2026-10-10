"""Pièce 08 « Souvenir » — montage, texture « caméscope » et son.
python3 montage.py edl.json sortie_dir
edl.json : {"texture": "camescope" | "propre" | "camescope_date", "plans": [[source, debut, n_images], ...]}
Les sources S_* (passé) reçoivent la texture ; les P_* (présent) restent nets en 16:9.
Texture caméscope (tout en numpy, graine fixe) : recadrage 4:3, définition divisée par 2 puis
réaccentuée (le halo d'accentuation des caméscopes), noirs relevés, balance des blancs chaude et verte,
bruit de chrominance basse fréquence (plus visible que le bruit de luminance sur la vidéo grand public).
"""
import json, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

R = "/home/user/Montagev2/atelier/rendus/08"
E = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
FPS, W, H = 25, 480, 270
rng = np.random.default_rng(8)


def camescope(im, k, date=False):
    a = im.convert("RGB")
    x0 = (W - 360) // 2
    a = a.crop((x0, 0, x0 + 360, H)).resize((180, 135), Image.BILINEAR).resize((360, 270), Image.BILINEAR)
    a = a.filter(ImageFilter.UnsharpMask(radius=2, percent=90, threshold=0))
    v = np.asarray(a).astype(np.float32) / 255
    v = 0.07 + 0.88 * v                                   # noirs relevés, blancs écrêtés tôt
    v = v * np.array([1.08, 1.03, 0.86])                  # balance chaude, un peu verte
    # bruit de chrominance : basse fréquence (bruit 45×34 agrandi), opposé sur R et B
    n = rng.normal(0, 1, (34, 45)).astype(np.float32)
    n = np.asarray(Image.fromarray(n).resize((360, 270), Image.BILINEAR))
    v[..., 0] += 0.025 * n; v[..., 2] -= 0.025 * n
    v += rng.normal(0, 0.012, v.shape[:2])[..., None]     # bruit de luminance fin
    v = np.clip(v, 0, 1)
    img = Image.fromarray((v * 255).astype(np.uint8))
    if date:  # le cliché, testé une fois pour le juger
        ImageDraw.Draw(img).text((240, 245), "JUL 08 1998", fill=(255, 255, 255))
    canvas = Image.new("RGB", (W, H)); canvas.paste(img, (x0, 0)); return canvas


frames, segs = [], []
for src, deb, n in E["plans"]:
    segs.append((src, len(frames), n))
    for i in range(n):
        f = deb + i
        frames.append((src, f))
tex = E.get("texture", "camescope")
for j, (src, f) in enumerate(frames):
    im = Image.open(f"{R}/{src}/{f:04d}.png").convert("RGB")
    if src.startswith("S_") and tex != "propre":
        im = camescope(im, j, date=(tex == "camescope_date"))
    im.save(f"{out}/{j:04d}.png")

# Son : présent = ton de pièce (bruit brun très bas) ; passé = souffle de bande + oiseau lointain
SR = 48000; N = len(frames) * SR // FPS; a = np.zeros(N, np.float32)
brown = np.cumsum(rng.normal(0, 1, N)); brown -= np.convolve(brown, np.ones(4801) / 4801, "same")
brown /= np.abs(brown).max()
hiss = rng.normal(0, 1, N); hiss = hiss - np.convolve(hiss, np.ones(8) / 8, "same"); hiss /= np.abs(hiss).max()
for src, i0, n in segs:
    s0, s1 = i0 * SR // FPS, (i0 + n) * SR // FPS
    if src.startswith("P_"):
        a[s0:s1] += 0.02 * brown[s0:s1]
    else:
        a[s0:s1] += 0.035 * hiss[s0:s1] + 0.01 * brown[s0:s1]
        t = np.arange(s1 - s0) / SR
        for c in np.arange(0.3, (s1 - s0) / SR - 0.2, 0.9):  # gazouillis : glissandos courts
            m = (t > c) & (t < c + 0.12)
            ph = 2 * np.pi * (3200 * (t - c) + 9000 * (t - c) ** 2)
            a[s0:s1] += m * 0.04 * np.sin(ph) * np.sin(np.pi * np.clip((t - c) / 0.12, 0, 1))
with wave.open(f"{out}/son.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())
name = os.path.basename(out.rstrip("/"))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{out}/%04d.png",
                "-i", f"{out}/son.wav", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-shortest", f"{R}/{name}.mp4"], check=True)
# Planche : une image toutes les 10 (0,4 s), en grille de 6
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{R}/{name}.mp4", "-vf",
                "select='not(mod(n\\,10))',scale=240:-1,tile=6x5:padding=2", "-frames:v", "1",
                f"{os.path.dirname(os.path.abspath(sys.argv[1]))}/{name}-planche.png"], check=True)
print(name, len(frames), "images", [(s, i0 / FPS, n / FPS) for s, i0, n in segs])
