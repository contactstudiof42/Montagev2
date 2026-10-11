# sfx_prep.py DOSSIER_SFX : (1) mesure, pour chaque WAV, le début (premier dépassement de -30 dB sous la crête) et la
# crête (s) -> crete.json ; (2) fabrique des variantes de hauteur (demi-tons) des sons répétés, dans variantes/.
import sys, os, json, subprocess, numpy as np
D = sys.argv[1]
def lire(f):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "48000", "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)
VAR = {"Phil Michalski - UI - Glassy Click.wav": [0, 2, 4, 5, 7, 9, 12],
       "Artlist Foley - Vintage Cameras - Konica EE Matic Mechanical Lever Pull Film Advance.wav": [-3, -1, 0, 2, 4, 5],
       "DeanKR - Glitch Transitions - Digital Whoosh Buzzing.wav": [0, 3, -2],
       "Cinemear - Petite Transitions - Fabric Whoosh Swift.wav": [0, -3, 3]}
for f, st in VAR.items():
    if not os.path.exists(os.path.join(D, f)): print("absent", f); continue
    for s in st:
        o = os.path.join(D, "variantes", f.rsplit(".", 1)[0] + f" ({s:+d}).wav")
        sr = int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=sample_rate", "-of",
                                 "default=nw=1:nk=1", os.path.join(D, f)], capture_output=True, text=True).stdout.strip())
        r = 2 ** (s / 12)   # hauteur ET durée changent (comme une bande accélérée) : voulu pour des tics et des clics
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(D, f), "-af", f"asetrate={sr}*{r},aresample=48000", "-ar", "48000", o])
res = {}
for base in (D, os.path.join(D, "variantes")):
    for f in sorted(os.listdir(base)):
        if not f.lower().endswith(".wav"): continue
        x = lire(os.path.join(base, f)); a = np.abs(x); pk = int(a.argmax()); seuil = a[pk] * 10 ** (-30 / 20)
        deb = int(np.argmax(a > seuil))
        res[os.path.relpath(os.path.join(base, f), D)] = dict(duree=round(len(x) / 48000, 3), debut=round(deb / 48000, 3), crete=round(pk / 48000, 3),
                                                               crete_db=round(float(20 * np.log10(a[pk] + 1e-9)), 1))
json.dump(res, open(os.path.join(D, "crete.json"), "w"), indent=0, ensure_ascii=False)
print(len(res), "sons mesurés")
