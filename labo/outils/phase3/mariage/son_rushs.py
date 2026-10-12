# son_rushs.py CAM : concatène le son de tous les rushes d'une caméra (16 kHz mono, 1 s de silence entre deux), table des décalages
import json, subprocess, numpy as np, sys, soundfile as sf
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"; R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"; cam = sys.argv[1]
r = [x for x in json.load(open(f"{T}/chrono.json")) if x["cam"] == cam]
out, table, pos = [], [], 0.0
for x in r:
    y = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{R}/{x['fichier']}", "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(y, np.int16); table.append({"nom": x["nom"], "debut": pos, "duree": len(a) / 16000, "t0": x["t0"]})
    out += [a, np.zeros(16000, np.int16)]; pos += len(a) / 16000 + 1
sf.write(f"{T}/son/cam_{cam}.wav", np.concatenate(out), 16000, subtype="PCM_16")
json.dump(table, open(f"{T}/son/cam_{cam}.json", "w")); print(cam, len(table), round(pos / 60, 1), "min")
