"""Rushes de festival avec stroboscope : peut-on les rendre livrables (WCAG 2.3.1) et à quel prix ?
python3 -I strobe.py OUT_DIR
Fabrique un faux rush 360×640, 25 i/s, 8 s : foule en silhouettes (sombre), lasers lents, et un strobe blanc
plein cadre à ~8,3 Hz (1 image allumée sur 3). Puis applique des traitements et mesure chacun avec flash_check.py.
Coût artistique mesuré : 'pic' = luminance moyenne des 5 % d'images les plus claires / médiane (ce qui reste du coup
de strobe), 'mouv' = différence absolue moyenne entre images voisines de la foule (ce qui reste du mouvement).
"""
import os, subprocess, sys
import numpy as np

out = sys.argv[1]; os.makedirs(out, exist_ok=True)
W, H, FPS, N = 360, 640, 25, 200
rng = np.random.default_rng(42)
xs = np.arange(W)[None, :]; ys = np.arange(H)[:, None]
heads = [(rng.uniform(0, W), rng.uniform(380, 520), rng.uniform(18, 30), rng.uniform(0, 6.28)) for _ in range(14)]
frames = []
for n in range(N):
    t = n / FPS
    img = np.zeros((H, W, 3)) + [0.04, 0.02, 0.08]                       # salle sombre violacée
    for k, ang0 in enumerate((0.3, 1.2, 2.1)):                            # lasers lents (verts)
        a = ang0 + 0.5 * np.sin(t * 0.7 + k)
        d = np.abs((xs - W / 2) * np.cos(a) + (ys - 60) * np.sin(a))
        img += (np.exp(-(d / 3.0) ** 2) * 0.6)[..., None] * [0.1, 1.0, 0.3]
    if n % 3 == 0:                                                        # strobe : 1 image sur 3
        img += [0.85, 0.85, 0.9]
    crowd = np.zeros((H, W), bool)                                        # foule : têtes + épaules qui sautent
    for (x0, y0, r, ph) in heads:
        y = y0 - 25 * max(0, np.sin(t * 2 * np.pi * 2.3 + ph))          # sauts à 138 BPM / 60 = 2,3 Hz
        crowd |= ((xs - x0) ** 2 + (ys - y) ** 2) < r ** 2
        crowd |= (np.abs(xs - x0) < r * 1.8) & (ys > y + r * 0.8)
    img[crowd] = img[crowd] * 0.08
    frames.append((np.clip(img, 0, 1) ** (1 / 2.2) * 255).astype(np.uint8))
raw = np.stack(frames)
brut = os.path.join(out, "brut.mp4")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", brut],
               input=raw.tobytes(), check=True)

T = {
    "brut": None,
    "tmix3": "tmix=frames=3",
    "tmix5": "tmix=frames=5",
    "deflicker9": "deflicker=size=9:mode=am",
    "deflicker25": "deflicker=size=25:mode=am",
    "tirage8_phase_libre": "select='not(mod(n\\,8))',setpts=N/FRAME_RATE/TB,fps=25,setpts=PTS",  # remplacé plus bas
    "tirage_sombre_8": None,
    "tirage_allume_8": None,
    "tmix3_tirage4": None,
}


def held(phase, step):
    """tirage par saccade : on garde l'image (k*step + phase) et on la tient step images."""
    idx = [(i // step) * step + phase for i in range(N)]
    return raw[np.clip(idx, 0, N - 1)]


def enc(arr, path):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                    "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", path],
                   input=arr.tobytes(), check=True)


def decode(path):
    b = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                       capture_output=True, check=True).stdout
    return np.frombuffer(b, np.uint8).reshape(-1, H, W, 3)


here = os.path.dirname(os.path.abspath(__file__))
check = os.path.join(here, "..", "flash_check.py")
lignes = []
for nom, vf in T.items():
    p = os.path.join(out, nom + ".mp4")
    if nom == "brut":
        pass
    elif nom == "tirage8_phase_libre":
        enc(held(1, 8), p)          # phase 1 : 1 image sur 8 tenue ; 8 et 3 premiers entre eux → alterne allumé / éteint
    elif nom == "tirage_sombre_8":
        enc(held(1, 8), p) if False else enc(np.stack([raw[min(((i // 8) * 8 // 3) * 3 + 1, N - 1)] for i in range(N)]), p)
    elif nom == "tirage_allume_8":
        enc(np.stack([raw[((i // 8) * 8 // 3) * 3] for i in range(N)]), p)
    elif nom == "tmix3_tirage4":
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", brut, "-vf", "tmix=frames=3", "-c:v", "libx264",
                        "-crf", "16", "-pix_fmt", "yuv420p", p + ".tmp.mp4"], check=True)
        a = decode(p + ".tmp.mp4"); os.remove(p + ".tmp.mp4")
        enc(np.stack([a[(i // 4) * 4] for i in range(N)]), p)
    else:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", brut, "-vf", vf, "-c:v", "libx264", "-crf", "16",
                        "-pix_fmt", "yuv420p", p], check=True)
    r = subprocess.run([sys.executable, "-I", check, p, "--fps", "25"], capture_output=True, text=True).stdout.strip()
    a = decode(p).astype(np.float64) / 255
    lum = (a ** 2.2 @ [0.2126, 0.7152, 0.0722]).mean((1, 2))
    pic = np.percentile(lum, 95) / max(np.median(lum), 1e-6)
    zone = a[:, 380:540, :, :].mean(-1)
    mouv = np.abs(np.diff(zone, axis=0)).mean()
    lignes.append(f"| {nom} | {r.split(': ', 1)[1]} | {pic:.2f} | {mouv:.4f} |")
    print(lignes[-1])
open(os.path.join(out, "table.md"), "w").write("\n".join(lignes) + "\n")
