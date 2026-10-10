"""Pièce 04 — assemblage : séquence PNG (+ EDL optionnelle) → mp4 avec ressac synthétique, planche contact.
Usage : python3 montage.py v1            (plan unique : rendus/04/v1/0001.png ...)
        python3 montage.py v3 edl.json   (EDL : [[dossier_source, image_debut, image_fin], ...] en images absolues)
"""
import json, os, subprocess, sys, shutil
import numpy as np
ICI = os.path.dirname(os.path.abspath(__file__))
REND = os.path.join(ICI, "..", "rendus", "04")
V = sys.argv[1]; FPS = 25; SR = 48000
SEQ = os.path.join(REND, V + "_seq"); shutil.rmtree(SEQ, ignore_errors=True); os.makedirs(SEQ)
edl = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else [[V, 1, len(os.listdir(os.path.join(REND, V)))]]
n = 0; coupes = []
for src, a, b in edl:
    coupes.append(n)
    for f in range(a, b + 1):
        n += 1; os.symlink(os.path.join(REND, src, f"{f:04d}.png"), os.path.join(SEQ, f"{n:04d}.png"))
dur = n / FPS

# Ressac : bruit rose filtré, houle lente (période ~6 s) qui s'éloigne (niveau et aigus baissent avec la marée)
rng = np.random.default_rng(4); N = int(dur * SR); t = np.arange(N) / SR
x = rng.standard_normal((2, N)).astype(np.float32)
X = np.fft.rfft(x, axis=1); fr = np.fft.rfftfreq(N, 1 / SR); fr[0] = 1
X *= 1 / np.sqrt(fr) * (fr < 4000); x = np.fft.irfft(X, n=N, axis=1)
houle = 0.55 + 0.45 * np.sin(2 * np.pi * t / 6.2 - 1.2) ** 2
eloigne = 1.0 - 0.6 * (t / dur)
y = x * houle * eloigne; y /= np.abs(y).max() + 1e-9; y *= 0.5
raw = os.path.join(REND, V + ".f32"); y.T.astype(np.float32).tofile(raw)
wav = os.path.join(REND, V + ".wav")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", raw,
                "-af", "loudnorm=I=-23:TP=-2:LRA=7:print_format=none", "-ar", str(SR), "-c:a", "pcm_s24le", wav], check=True)
out = os.path.join(REND, V + ".mp4")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", os.path.join(SEQ, "%04d.png"), "-i", wav,
                "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True)
# Planche : 12 vignettes régulières, numéro d'image incrusté
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
pas = max(1, n // 12)
sel = "+".join(f"eq(n\\,{i * pas})" for i in range(12))
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", out, "-vf",
                f"drawtext=fontfile={FONT}:text='%{{n}}':fontsize=24:fontcolor=white:x=8:y=8,select='{sel}',scale=240:135,tile=4x3:padding=2",
                "-frames:v", "1", "-update", "1", os.path.join(ICI, f"{V}-planche.png")], check=True)
json.dump({"images": n, "duree_s": dur, "coupes": coupes, "pas_planche": pas}, open(os.path.join(ICI, f"{V}-mesures.json"), "w"))
print(V, n, "images", coupes)
