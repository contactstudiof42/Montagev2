"""Inserts lumineux calés à 138 BPM (examen n°7, extraits kinetic) : python3 -I gen_test.py <dossier>
Fabrique des montages synthétiques de 4 s (25 i/s, 640×360) : une source claire (tache gaussienne blanc-bleu)
sur fond nocturne, allumée ou éteinte selon le motif, puis lance flash_check.py sur chacun.
Motifs : 'alt' = chaque événement alterne allumé / éteint (une coupe = une extinction ou un allumage) ;
'pulse' = à chaque événement la source s'allume puis s'éteint au milieu de l'intervalle (un flash par événement).
Événements : noires (2,3/s), croches (4,6/s), doubles croches (9,2/s). Taille : part de l'écran couverte par la source."""
import sys, subprocess, os
import numpy as np
d = sys.argv[1]; os.makedirs(d, exist_ok=True)
W, H, FPS, DUR = 640, 360, 25, 4.0
yy, xx = np.mgrid[0:H, 0:W]
here = os.path.dirname(os.path.abspath(__file__))
def video(nom, motif, sub, part):
    beat = 60 / 138 / sub                               # intervalle entre événements (s)
    r = np.sqrt(part * W * H / np.pi)                    # rayon d'un disque couvrant 'part' de l'écran
    tache = np.clip(1.15 - np.hypot(xx - W / 2, yy - H / 2) / r * 0.6, 0, 1) ** 1.5   # bord doux, cœur saturé
    fond = np.full((H, W, 3), (6, 8, 14), np.float64)
    frames = []
    for n in range(int(DUR * FPS)):
        t = n / FPS; k = int(t // beat); ph = (t % beat) / beat
        on = (k % 2 == 0) if motif == "alt" else (ph < 0.5)
        img = fond + (on * tache)[..., None] * np.array([200, 225, 245])
        frames.append(np.clip(img, 0, 255).astype(np.uint8))
    out = f"{d}/{nom}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                    "-i", "-", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out], input=np.stack(frames).tobytes(), check=True)
    r = subprocess.run(["python3", "-I", f"{here}/../flash_check.py", out, "--fps", "25"], capture_output=True, text=True).stdout.strip().splitlines()
    return r[-1] if r else "?"
for motif in ("alt", "pulse"):
    for sub, nsub in ((1, "noires"), (2, "croches"), (4, "doubles")):
        for part in (0.01, 0.05, 0.25):
            nom = f"{motif}_{nsub}_{int(part * 100)}pc"
            print(f"{nom:24s} {video(nom, motif, sub, part)}")
