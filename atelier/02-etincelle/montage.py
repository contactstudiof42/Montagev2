#!/usr/bin/env python3
"""Pièce 02 « Étincelle » — montage, SFX numpy, loudness, planche contact.
Usage : python3 montage.py <version> <blender>   (rendus lourds : atelier/rendus/02-etincelle/)
La liste de plans (EDL) est dans edl_<version>.json : [[camera, image_source, durée, rôle], ...]."""
import json, os, re, subprocess, sys
import numpy as np
V, BLENDER = sys.argv[1], sys.argv[2]
ICI = os.path.dirname(os.path.abspath(__file__))
REND = os.path.join(ICI, "..", "rendus", "02-etincelle"); FR = os.path.join(REND, "frames")
os.makedirs(FR, exist_ok=True)
FPS, SR = 30, 48000; SPF = SR // FPS
FONT = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
EDL = json.load(open(os.path.join(ICI, f"edl_{V}.json")))
rng = np.random.default_rng(7)
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit(f"ÉCHEC {cmd[:3]}\n{r.stderr[-1500:]}")
    return r

# ---- 1. Rendu Blender des seules images utilisées (plages contiguës par caméra) ----
besoin = {}
for cam, a, d, _ in EDL: besoin.setdefault(cam, set()).update(range(a, a + d))
jobs = []
for cam, fr in besoin.items():
    fr = sorted(f for f in fr if not os.path.exists(os.path.join(FR, f"{cam}_{f:04d}.png")))
    while fr:
        a = b = fr.pop(0)
        while fr and fr[0] == b + 1: b = fr.pop(0)
        jobs.append([cam, a, b])
if jobs:
    json.dump(jobs, open(os.path.join(REND, "jobs.json"), "w"))
    run([BLENDER, "-b", "-P", os.path.join(ICI, "scene.py"), "--", os.path.join(REND, "jobs.json"), FR])

# ---- 2. Montage : séquence d'images dans l'ordre de l'EDL ----
SEQ = os.path.join(REND, f"seq_{V}"); os.makedirs(SEQ, exist_ok=True)
debuts, n = [], 0
for cam, a, d, _ in EDL:
    debuts.append(n)
    for k in range(d):
        dst = os.path.join(SEQ, f"{n:04d}.png")
        if os.path.lexists(dst): os.remove(dst)
        os.symlink(os.path.join(FR, f"{cam}_{a + k:04d}.png"), dst); n += 1
TOTAL = n
role = {r: debuts[i] for i, (_, _, _, r) in enumerate(EDL) if r}
role["riser_fin"] = role["silence"]

# ---- 3. SFX ----
def svf_bandpass(x, fc, q=2.0):
    lp = bp = 0.0; y = np.empty_like(x); f = 2 * np.sin(np.pi * np.clip(fc, 20, SR / 6) / SR); d = 1 / q
    for k in range(len(x)):
        hp = x[k] - lp - d * bp; bp += f[k] * hp; lp += f[k] * bp; y[k] = bp
    return y
def norm(y): return y / np.max(np.abs(y))
def tic(f0=2400):  # tic métallique : deux partiels inharmoniques, très court
    t = np.arange(int(0.08 * SR)) / SR
    y = (np.sin(2*np.pi*f0*t) + 0.6*np.sin(2*np.pi*f0*2.76*t)) * np.exp(-t*90) + 0.4*rng.standard_normal(len(t))*np.exp(-t*900)
    y[:12] *= np.linspace(0, 1, 12); return norm(y), 0
def whoosh(av=4, ap=3, f0=300, f1=4000):
    na, nb = av*SPF, ap*SPF
    fc = np.concatenate([np.geomspace(f0, f1, na), np.geomspace(f1, f1*0.6, nb)])
    env = np.concatenate([np.linspace(0, 1, na)**2, np.exp(-np.linspace(0, 5, nb))])
    return norm(svf_bandpass(rng.standard_normal(na+nb), fc, 1.5) * env), na
def impact(dur=0.7, grave=38):
    t = np.arange(int(dur*SR)) / SR
    sub = np.sin(2*np.pi*np.cumsum(grave + 60*np.exp(-t*25))/SR) * np.exp(-t*6)
    crack = np.convolve(rng.standard_normal(len(t)) * np.exp(-t*60), np.ones(6)/6, "same")
    y = sub + 0.5*crack; y[:24] *= np.linspace(0, 1, 24); return norm(y), 0
def riser(nimg):
    m = nimg*SPF; fc = np.geomspace(200, 6000, m)
    y = norm(svf_bandpass(rng.standard_normal(m), fc, 3)) + 0.4*np.sin(2*np.pi*np.cumsum(np.geomspace(110, 880, m))/SR)
    return norm(y * np.linspace(0, 1, m)**3), m
def craquement():  # frottement de l'allumette + embrasement : bruit large, attaque sèche, queue de souffle
    t = np.arange(int(0.9*SR)) / SR
    y = svf_bandpass(rng.standard_normal(len(t)), np.geomspace(5000, 900, len(t)), 0.8) * np.exp(-t*7)
    y[:24] *= np.linspace(0, 1, 24); return norm(y), 0
def feu(nimg):  # grésillement : souffle grave + crépitements aléatoires
    m = nimg*SPF
    souffle = np.convolve(rng.standard_normal(m), np.ones(40)/40, "same")
    crep = (rng.random(m) > 0.9993) * rng.standard_normal(m)
    crep = np.convolve(crep, np.exp(-np.arange(200)/25), "same")
    y = norm(souffle)*0.6 + norm(crep); y[:SPF*3] *= np.linspace(0, 1, SPF*3); y[-SPF*10:] *= np.linspace(1, 0, SPF*10)
    return norm(y), 0
piste = np.zeros(TOTAL*SPF + SR); ev = []
def poser(sig_off, image, db, nom):
    sig, off = sig_off; s0 = int(image*SPF - off); g = 10**(db/20)
    a, b = max(s0, 0), min(s0+len(sig), len(piste)); piste[a:b] += g*sig[a-s0:b-s0]
    ev.append({"sfx": nom, "image": image, "db": db})

ARRET = role["silence"]; IGN = role["allumage"]
# Seconde horloge : tic toutes les 15 images, indépendant des coupes, jusqu'au silence
# v3 : le tic est calé sur les passages du pendule à l'écran quand il y a un hook pendule (image 1 = passage)
T0 = 1 if "hook" in role else 0
for img in range(T0, ARRET, 15): poser(tic(2400 if (img//15) % 2 else 2150), img, -8 if img == T0 and T0 else -16, "tic")
# Coupes : whoosh sur les plans de sphères (crête sur la coupe), impacts sur les poses du cube
for i, (cam, a, d, r) in enumerate(EDL):
    c = debuts[i]
    if cam == "spheres" and c > 0: poser(whoosh(min(5, max(3, d//3)), 3, 250 + 40*i, 2800 + 200*i), c, -11 - (i % 3)*2, "whoosh")
    if cam == "cube":
        pose = 10 - a  # le cube touche le sol à l'image source 10
        if 0 <= pose < d: poser(impact(0.5 if c else 0.7), c + pose, -2 if c else 0, "impact_cube")
poser(riser(role["riser_fin"] - role["riser"]), role["riser_fin"] - 1, -12, "riser")  # coupé 1 image avant le silence
poser(craquement(), IGN, -3, "craquement"); poser(impact(0.9, 32), IGN, 0, "impact_allumage")
poser(feu(TOTAL - IGN), IGN, -14, "feu")
# Drone froid très bas jusqu'au silence (évite le vide numérique), coupé net
t = np.arange(ARRET*SPF) / SR
piste[:ARRET*SPF] += 10**(-30/20) * (np.sin(2*np.pi*55*t) + 0.5*np.sin(2*np.pi*82.7*t)) * np.minimum(1, t*4)
for img, mot in [(0, "ATTENDS"), (15, "L'ÉTINCELLE")]: poser(tic(3200), img, -20, f"click_{mot}")
piste = piste[:TOTAL*SPF]
st = np.stack([piste, piste], 1).astype(np.float32); st /= max(1, np.max(np.abs(st))/0.5)
raw = os.path.join(REND, f"sfx_{V}.f32"); st.tofile(raw)
wav = os.path.join(REND, f"sfx_{V}.wav")
run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", raw, "-c:a", "pcm_s24le", wav])
def ebur(p):
    e = subprocess.run(["ffmpeg", "-nostats", "-i", p, "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"], capture_output=True, text=True).stderr
    s = e[e.rfind("Summary"):]
    return {"I": float(re.search(r"I:\s+(-?[\d.]+) LUFS", s).group(1)), "TP": float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", s).group(1))}
gain, m = 0.0, ebur(wav); wn = os.path.join(REND, f"sfx_{V}_norm.wav")
for _ in range(5):  # gain + limiteur sur-échantillonné, itéré (recette R6 de montage-kinetic-editing)
    gain += -14 - m["I"]
    run(["ffmpeg", "-y", "-v", "error", "-i", wav, "-af", f"volume={gain:.2f}dB,aresample=192000,alimiter=limit=0.7079:attack=1:release=50:level=false,aresample=48000", "-c:a", "pcm_s24le", wn])
    m = ebur(wn)
    if abs(m["I"] + 14) < 0.3: break

# ---- 4. Image : agrandissement, flash 1 image + shake amorti à l'allumage, captions, mux ----
vf = [f"scale=540:960:flags=lanczos",
      f"scale=600:1066,crop=540:960:x='30+22*sin((n-{IGN})*2.9)*exp(-(n-{IGN})/3)*gte(n,{IGN})':y='53+22*cos((n-{IGN})*3.7)*exp(-(n-{IGN})/3)*gte(n,{IGN})'",
      f"drawbox=c=0xFFE8C0:t=fill:enable='eq(n,{IGN})'"]
if V >= "v2": vf.append("noise=c0s=4:allf=t")  # grain σ≈2/255 : leçon de labo/encodage (bandes dans les noirs)
for a, b, mot in [(0, 14, "ATTENDS"), (15, 29, "L’ÉTINCELLE")]:
    vf.append(f"drawtext=fontfile={FONT}:text='{mot}':fontsize='if(eq(n,{a}),70,58)':fontcolor=0xE8F4F0:borderw=5:bordercolor=black@0.8:x=(w-tw)/2:y=h*0.80:enable='between(n,{a},{b})'")
out = os.path.join(REND, f"etincelle_{V}.mp4")
run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", os.path.join(SEQ, "%04d.png"), "-i", wn, "-vf", ",".join(vf),
     "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
     "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-shortest", out])
mf = ebur(out)
# ---- 5. Planche contact : 1re image de chaque plan + 3 images du plan final ----
idx = debuts + [IGN + 1, IGN + 30, TOTAL - 5]
sel = "+".join(f"eq(n,{i})" for i in sorted(set(idx)))
k = len(set(idx)); cols = 8; rows = (k + cols - 1)//cols
run(["ffmpeg", "-y", "-v", "error", "-i", out, "-vf", f"select='{sel}',scale=120:213,drawtext=fontfile={FONT}:text='%{{n}}':fontsize=14:fontcolor=white:x=4:y=4,tile={cols}x{rows}:padding=2", "-frames:v", "1", "-update", "1", os.path.join(ICI, f"{V}-planche.png")])
mes = {"version": V, "images": TOTAL, "duree_s": round(TOTAL/FPS, 2), "coupes": debuts, "allumage": IGN, "silence": ARRET,
       "loudness_mp4": mf, "sfx": ev}
json.dump(mes, open(os.path.join(ICI, f"{V}-mesures.json"), "w"), indent=1, ensure_ascii=False)
print(json.dumps({k_: mes[k_] for k_ in ("images", "duree_s", "allumage", "loudness_mp4")}))
