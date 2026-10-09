#!/usr/bin/env python3
"""Labo kinetic editing : démo 6 s, 540x960, 30 i/s, 14 plans, SFX numpy calés à l'image.

Usage : python3 labo/kinetic/kinetic_demo.py
Sorties lourdes : labo/rendus/kinetic/ ; légères : labo/kinetic/ (planche, forme d'onde, mesures.json).
"""
import json, os, re, subprocess, sys
import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
REND = os.path.join(ICI, "..", "rendus", "kinetic")
os.makedirs(REND, exist_ok=True)
W, H, FPS, SR = 540, 960, 30, 48000
SPF = SR // FPS  # 1600 échantillons par image
FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
rng = np.random.default_rng(42)

# ---------- 1. Montage : 14 plans, durées en images ----------
DUREES = [15, 15, 15, 13, 12, 10, 8, 6, 15, 15, 14, 12, 15, 15]  # 180 images = 6.0 s
SOURCES = [
    "testsrc2", "mandelbrot", "color=c=0xff3b30", "smptehdbars", "testsrc2",
    "color=c=0x0a84ff", "mandelbrot", "color=c=0xffd60a", "cellauto", "testsrc2",
    "color=c=0x30d158", "mandelbrot", "color=c=0x111111", "smptehdbars",
]
PUNCH = 4      # plan avec punch-in
IMPACT = 8     # plan d'impact : flash 1 image + camera shake
IMPACT2 = 12   # second impact (fin)
debuts = np.concatenate([[0], np.cumsum(DUREES)[:-1]]).astype(int)
TOTAL = int(sum(DUREES))
COUPES = [int(d) for d in debuts[1:]]  # numéros d'image des coupes


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        sys.exit(f"ÉCHEC : {' '.join(cmd)}\n{r.stderr[-1500:]}")
    return r


def plan(i):
    n = DUREES[i]
    src = SOURCES[i]
    seed = f":seed={i}" if src == "cellauto" else ""
    lav = f"{src}=s={W}x{H}:r={FPS}{seed}" if "=" not in src else f"{src}:s={W}x{H}:r={FPS}"
    f = ["format=yuv420p"]
    if src.startswith("color"):
        f.insert(0, f"drawtext=fontfile={FONT}:text='{i+1:02d}':fontsize=260:fontcolor=white@0.9:x=(w-tw)/2:y=(h-th)/2")
    if i == PUNCH:  # punch-in : 2 images larges puis zoom 1 -> 1.35 en 3 images (ease-out)
        f.insert(0, "zoompan=z='if(lt(on,2),1,1+0.35*(1-pow(1-min((on-1)/3,1),3)))':d=1:s=%dx%d:fps=%d"
                 ":x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2'" % (W, H, FPS))
    if i in (IMPACT, IMPACT2):  # shake amorti sur ~5 images + flash blanc 1 image
        f.insert(0, f"scale={W+60}:{H+106},crop={W}:{H}:x='30+26*sin(n*2.9)*exp(-n/3)':y='53+26*cos(n*3.7)*exp(-n/3)'")
        f.append("drawbox=c=white:t=fill:enable='eq(n,0)'")
    out = os.path.join(REND, f"p{i:02d}.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", lav, "-vf", ",".join(f),
         "-frames:v", str(n), "-c:v", "libx264", "-preset", "ultrafast", "-crf", "16", "-r", str(FPS), out])
    return out


# ---------- 2. SFX numpy ----------
def svf_bandpass(x, fc, q=2.0):
    """Filtre à variables d'état, fréquence centrale variable échantillon par échantillon."""
    lp = bp = 0.0
    y = np.empty_like(x)
    f = 2 * np.sin(np.pi * np.clip(fc, 20, SR / 6) / SR)
    d = 1.0 / q
    for k in range(len(x)):
        hp = x[k] - lp - d * bp
        bp += f[k] * hp
        lp += f[k] * bp
        y[k] = bp
    return y


def whoosh(avant_img=4, apres_img=3, f0=300, f1=4000):
    """Bruit filtré à balayage montant ; crête AU point de coupe (fin de la partie 'avant')."""
    na, nb = avant_img * SPF, apres_img * SPF
    n = na + nb
    fc = np.concatenate([np.geomspace(f0, f1, na), np.geomspace(f1, f1 * 0.6, nb)])
    env = np.concatenate([np.linspace(0, 1, na) ** 2, np.exp(-np.linspace(0, 5, nb))])
    y = svf_bandpass(rng.standard_normal(n), fc, q=1.5) * env
    return y / np.max(np.abs(y)), na  # (signal, offset de la crête)


def impact(dur=0.6):
    n = int(dur * SR); t = np.arange(n) / SR
    freq = 38 + 60 * np.exp(-t * 25)                      # pitch drop 98 -> 38 Hz
    sub = np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-t * 6)
    crack = rng.standard_normal(n) * np.exp(-t * 60)        # transitoire
    crack = np.convolve(crack, np.ones(6) / 6, mode="same")
    y = sub + 0.5 * crack
    y[:24] *= np.linspace(0, 1, 24)                         # attaque 0.5 ms, pas de clic DC
    return y / np.max(np.abs(y)), 0


def click():
    n = int(0.012 * SR); t = np.arange(n) / SR
    y = np.sin(2 * np.pi * 3200 * t) * np.exp(-t * 600) + 0.3 * rng.standard_normal(n) * np.exp(-t * 900)
    return y / np.max(np.abs(y)), 0


def riser(dur_img=24):
    n = dur_img * SPF; t = np.arange(n) / SR
    fc = np.geomspace(200, 6000, n)
    noise = svf_bandpass(rng.standard_normal(n), fc, q=3)
    tone = np.sin(2 * np.pi * np.cumsum(np.geomspace(110, 880, n)) / SR)
    env = np.linspace(0, 1, n) ** 3
    y = (noise / np.max(np.abs(noise)) + 0.4 * tone) * env
    return y / np.max(np.abs(y)), n   # crête = fin du riser


piste = np.zeros(TOTAL * SPF + SR)
evenements = []


def poser(sig_off, image, gain_db, nom):
    sig, off = sig_off
    s0 = image * SPF - off
    g = 10 ** (gain_db / 20)
    a, b = max(s0, 0), min(s0 + len(sig), len(piste))
    piste[a:b] += g * sig[a - s0:b - s0]
    evenements.append({"sfx": nom, "image_crete": image, "debut_image": round(s0 / SPF, 2), "gain_db": gain_db})


# Hiérarchie : impacts (0 dB) > riser (-6) > whoosh (-10 à -14, variés) > clicks (-18) > ambiance (-30)
for k, c in enumerate(COUPES):
    idx = k + 1  # plan qui commence à cette coupe
    if idx in (IMPACT, IMPACT2):
        poser(impact(), c, 0, "impact")
    elif idx in (IMPACT - 1, IMPACT2 - 1):
        continue  # coupe sèche juste avant l'impact : on laisse monter le riser seul
    elif idx in (2, 5, 10, 13):
        av = [3, 4, 5, 6][[2, 5, 10, 13].index(idx)]
        poser(whoosh(av, 3, f0=250 + 80 * k, f1=3000 + 300 * k), c, -10 - (k % 3) * 2, f"whoosh_{av}i")
    else:
        poser(click(), c, -20, "click_coupe")
poser(riser(30), debuts[IMPACT], -6, "riser")
poser(whoosh(5, 4, 200, 2500), debuts[PUNCH], -12, "whoosh_punch")  # le punch-in a sa propre ponctuation

# Texte mot à mot (calé sur les plans 10-13) + click doux par mot
MOTS = [("CHAQUE", debuts[9]), ("SON", debuts[9] + 7), ("A", debuts[10]), ("SA", debuts[10] + 7),
        ("PLACE", debuts[11]), ("ICI.", debuts[12])]
for m, img in MOTS:
    poser(click(), img, -22, f"click_mot_{m}")

# Ambiance : bruit rose très bas pour éviter le vide numérique entre les SFX
amb = np.cumsum(rng.standard_normal(len(piste))); amb -= np.convolve(amb, np.ones(4800) / 4800, mode="same")
piste += 10 ** (-34 / 20) * amb / np.max(np.abs(amb))
piste = piste[:TOTAL * SPF]
stereo = np.stack([piste, piste], axis=1).astype(np.float32)
stereo /= max(1.0, np.max(np.abs(stereo)) / 0.5)
raw = os.path.join(REND, "sfx.f32")
stereo.tofile(raw)
sfx_wav = os.path.join(REND, "sfx_brut.wav")
run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", raw, "-c:a", "pcm_s24le", sfx_wav])


# ---------- 3. Loudness : mesure -> gain -> limiteur si besoin -> re-mesure ----------
def ebur(path):
    err = subprocess.run(["ffmpeg", "-nostats", "-i", path, "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    summ = err[err.rfind("Summary"):]
    I = float(re.search(r"I:\s+(-?[\d.]+) LUFS", summ).group(1))
    tp = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", summ).group(1))
    lra = float(re.search(r"LRA:\s+(-?[\d.]+) LU", summ).group(1))
    return {"I": I, "TP": tp, "LRA": lra}


m1 = ebur(sfx_wav)
gain = -14.0 - m1["I"]
af = f"volume={gain:.2f}dB"
if m1["TP"] + gain > -1.5:
    af += ",aresample=192000,alimiter=limit=0.8414:attack=1:release=50:level=false,aresample=48000"
sfx_norm = os.path.join(REND, "sfx_norm.wav")
run(["ffmpeg", "-y", "-v", "error", "-i", sfx_wav, "-af", af, "-ar", "48000", "-c:a", "pcm_s24le", sfx_norm])
m2 = ebur(sfx_norm)
gain2 = 0.0
if abs(m2["I"] + 14) > 0.5:  # le limiteur a mangé du niveau : 2e passe de gain sous limiteur
    gain2 = -14.0 - m2["I"]
    af2 = f"volume={gain2:.2f}dB,aresample=192000,alimiter=limit=0.8414:attack=1:release=50:level=false,aresample=48000"
    run(["ffmpeg", "-y", "-v", "error", "-i", sfx_wav, "-af", af.split(",")[0] + "," + af2, "-ar", "48000",
         "-c:a", "pcm_s24le", sfx_norm])
    m2 = ebur(sfx_norm)

# ---------- 4. Vidéo : plans -> concat -> texte mot à mot -> mux ----------
fichiers = [plan(i) for i in range(len(DUREES))]
lst = os.path.join(REND, "liste.txt")
open(lst, "w").write("".join(f"file '{f}'\n" for f in fichiers))
txt = []
for j, (m, img) in enumerate(MOTS):
    fin = MOTS[j + 1][1] if j + 1 < len(MOTS) else TOTAL
    # pop d'échelle simulé : taille 1.25x sur la 1re image du mot, puis taille normale
    txt.append(f"drawtext=fontfile={FONT}:text='{m}':fontsize='if(eq(n,{img}),150,120)':fontcolor=white:"
               f"borderw=8:bordercolor=black:x=(w-tw)/2:y=h*0.70:enable='between(n,{img},{fin-1})'")
final = os.path.join(REND, "kinetic_demo.mp4")
run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", sfx_norm,
     "-vf", ",".join(txt), "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
     "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart",
     "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-shortest", final])
m3 = ebur(final)

# ---------- 5. Vérifications : coupes détectées vs onsets audio dans le MP4 final ----------
err = subprocess.run(["ffmpeg", "-i", final, "-vf", "select='gt(scene,0.25)',showinfo", "-an", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
coupes_det = sorted({round(float(t) * FPS) for t in re.findall(r"pts_time:([\d.]+)", err)})
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", final, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                     capture_output=True).stdout
a = np.frombuffer(pcm, np.float32)
# onset d'impact : 1er échantillon dépassant 50 % du max dans la fenêtre ±3 images de la coupe
onsets = {}
for idx in (IMPACT, IMPACT2):
    c = int(debuts[idx]) * SPF
    w = a[c - 3 * SPF:c + 3 * SPF]
    k = int(np.argmax(np.abs(w) > 0.5 * np.max(np.abs(w))))
    onsets[f"plan{idx}"] = {"coupe_image": int(debuts[idx]), "onset_ms_vs_coupe": round((k - 3 * SPF) / SR * 1000, 1)}

# ---------- 6. Planche contact + forme d'onde ----------
sel = "+".join(f"eq(n,{int(d + DUREES[i] // 2)})" for i, d in enumerate(debuts))
planche = os.path.join(ICI, "planche_contact.png")
run(["ffmpeg", "-y", "-v", "error", "-i", final, "-vf", f"select='{sel}',scale=96:170,tile=7x2:padding=4:color=white",
     "-frames:v", "1", "-vsync", "0", planche])
WW, HH = 1200, 240
img = np.full((HH, WW, 3), 250, np.uint8)
spp = len(a) / WW
for x in range(WW):
    seg = a[int(x * spp):int((x + 1) * spp)]
    if len(seg):
        h = int(min(1, np.max(np.abs(seg))) * (HH / 2 - 4))
        img[HH // 2 - h:HH // 2 + h + 1, x] = (40, 40, 40)
for c in COUPES:
    x = int(c * SPF / spp)
    col = (220, 30, 30) if c in (debuts[IMPACT], debuts[IMPACT2]) else (30, 110, 220)
    img[:, max(x - 1, 0):x + 1] = col
ppm = os.path.join(REND, "onde.ppm")
with open(ppm, "wb") as fh:
    fh.write(f"P6 {WW} {HH} 255\n".encode()); fh.write(img.tobytes())
onde = os.path.join(ICI, "forme_onde_coupes.png")
run(["ffmpeg", "-y", "-v", "error", "-i", ppm, onde])

res = {"durees_images": DUREES, "coupes_images": COUPES, "coupes_detectees_mp4": coupes_det,
       "sfx": evenements, "loudness_sfx_brut": m1, "gain_db": round(gain, 2), "gain2_db": round(gain2, 2),
       "filtre": af, "loudness_sfx_norm": m2, "loudness_mp4": m3, "onsets_impact": onsets,
       "planche_ko": round(os.path.getsize(planche) / 1024, 1), "onde_ko": round(os.path.getsize(onde) / 1024, 1)}
json.dump(res, open(os.path.join(ICI, "mesures.json"), "w"), indent=1, ensure_ascii=False, default=int)
print(json.dumps({k: v for k, v in res.items() if k != "sfx"}, indent=1, ensure_ascii=False, default=int))
