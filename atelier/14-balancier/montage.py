"""Pièce 14 : monte A (3 plans, coupes sur points morts) et B (kinetic : une coupe par point mort, puis par demi-période
à la fin, whoosh sur chaque coupe). Son commun : un grincement de crochet à chaque point mort, amorti avec l'amplitude.
Usage : python3 montage.py <rendus14> ; écrit edl-A.json, edl-B.json, mesures.json ; vidéos dans <rendus14>/A.mp4, B.mp4"""
import json, math, os, subprocess, sys, wave, numpy as np
R = sys.argv[1]; FPS, N = 25, 375
bal = json.load(open(f"{R}/large/balancier.json")); morts = bal["points_morts"]; T0 = bal["periode_s"]
def proche(f): return min(morts, key=lambda m: abs(m - f))
# A : large -> serré -> large, coupes au point mort le plus proche de 7 s et 12 s
cA = [proche(7 * FPS), proche(12 * FPS)]
A = [("large", 1, cA[0] - 1), ("serre", cA[0], cA[1] - 1), ("large", cA[1], N)]
# B : coupe à chaque point mort ; après 10 s, aussi à chaque passage au milieu (demi-intervalle)
cB = [m for m in morts if m > 1]
cB += [int((a + b) / 2) for a, b in zip(cB, cB[1:]) if a > 10 * FPS]
cB = sorted(set(cB)); bornes = [1] + cB + [N + 1]
B = [("large" if i % 2 == 0 else "serre", bornes[i], bornes[i + 1] - 1) for i in range(len(bornes) - 1)]
def ecart(cuts): return [min(abs(c - m) for m in morts) for c in cuts]
mes = {"periode_s": T0, "points_morts": morts, "A_coupes": cA, "A_ecart_point_mort_images": ecart(cA),
       "B_nb_plans": len(B), "B_duree_mediane_s": float(np.median([(b - a + 1) / FPS for _, a, b in B]))}
json.dump(A, open("edl-A.json", "w")); json.dump(B, open("edl-B.json", "w")); json.dump(mes, open("mesures.json", "w"), indent=1)
print(mes)
sr = 48000; rng = np.random.default_rng(4)
def son(edl, whoosh):
    a = np.zeros(int(N / FPS * sr) + sr, np.float32)
    for m in morts:  # grincement : bruit filtré résonant court, plus faible quand l'amplitude baisse
        t = (m - 1) / FPS; amp = math.exp(-t / 6.0); k = int(t * sr); n = int(0.18 * sr)
        x = rng.standard_normal(n) * np.exp(-np.arange(n) / (0.05 * sr))
        y = np.convolve(x, np.sin(2 * np.pi * 820 * np.arange(200) / sr) * np.hanning(200), "same")
        a[k:k + n] += 0.25 * amp * y / np.abs(y).max()
    a += 0.004 * rng.standard_normal(len(a)).astype(np.float32)  # air de pièce
    if whoosh:
        for _, s0, _ in edl[1:]:
            k = int((s0 - 1) / FPS * sr) - int(0.12 * sr); n = int(0.2 * sr)
            x = rng.standard_normal(n) * np.hanning(n); x = np.convolve(x, np.ones(30) / 30, "same")
            a[max(k, 0):k + n] += 0.5 * x[: len(a[max(k, 0):k + n])] / np.abs(x).max()
    a = np.clip(a, -1, 1); return (a * 32767).astype(np.int16)
for nom, edl, wh in (("A", A, False), ("B", B, True)):
    d = f"{R}/seq-{nom}"; os.makedirs(d, exist_ok=True); i = 0
    for cam, a0, b0 in edl:
        for f in range(a0, b0 + 1):
            i += 1; dst = f"{d}/{i:04d}.png"
            if os.path.lexists(dst): os.remove(dst)
            os.symlink(f"{R}/{cam}/{f:04d}.png", dst)
    with wave.open(f"{R}/{nom}.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(son(edl, wh).tobytes())
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", "25", "-i", f"{d}/%04d.png", "-i", f"{R}/{nom}.wav",
                    "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-c:a", "aac", f"{R}/{nom}.mp4"], check=True)
