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
# v3 : quand l'estran est découvert (image 222), le ressac s'efface presque ; reste un seul son causé par l'image :
# l'eau qui goutte de la chaise (gouttes espacées, irrégulières). Activé par l'option DECOUVERT=image.
dec = int(os.environ.get("DECOUVERT", 0))
if dec:
    t_dec = dec / FPS
    eloigne = eloigne * np.where(t < t_dec, 1.0, np.exp(-(t - t_dec) / 0.35) * 0.85 + 0.15)
y = x * houle * eloigne; y /= np.abs(y).max() + 1e-9; y *= 0.5
if dec:
    for k, tg in enumerate([t_dec + 0.25, t_dec + 0.71, t_dec + 1.02, t_dec + 1.6]):
        if tg >= dur: break
        i = int(tg * SR); n_ = int(0.09 * SR); tt = np.arange(n_) / SR
        g = np.sin(2 * np.pi * (1400 - 5000 * tt) * tt) * np.exp(-tt * 55) * (0.5 if k % 2 else 0.35)
        y[0, i:i + n_] += g[:max(0, min(n_, N - i))]; y[1, i:i + n_] += 0.8 * g[:max(0, min(n_, N - i))]
raw = os.path.join(REND, V + ".f32"); y.T.astype(np.float32).tofile(raw)
wav = os.path.join(REND, V + ".wav")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", raw,
                "-c:a", "pcm_s24le", wav + ".brut.wav"], check=True)
# mesure + gain statique (méthode de montage-loudness-livraison), cible -18 LUFS (AES TD1008, lecture web non normalisée)
e = subprocess.run(["ffmpeg", "-nostats", "-i", wav + ".brut.wav", "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"], capture_output=True, text=True).stderr
I = float(e.split("I:")[-1].split("LUFS")[0]); tp = float(e.split("Peak:")[-1].split("dBFS")[0])
gain = min(-18 - I, -1.0 - tp)   # ne jamais dépasser -1 dBTP : si le crête limite, on reste sous la cible et on le note
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", wav + ".brut.wav", "-af", f"volume={gain:.2f}dB", "-c:a", "pcm_s24le", wav], check=True)
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
e = subprocess.run(["ffmpeg", "-nostats", "-i", wav, "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"], capture_output=True, text=True).stderr
json.dump({"lufs": float(e.split("I:")[-1].split("LUFS")[0]), "true_peak": float(e.split("Peak:")[-1].split("dBFS")[0]), "images": n, "duree_s": dur, "coupes": coupes, "pas_planche": pas}, open(os.path.join(ICI, f"{V}-mesures.json"), "w"))
print(V, n, "images", coupes)
