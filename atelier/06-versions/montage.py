"""Pièce 06 « Versions » — montage, musique en boucle, planches.
Lancer : python3 montage.py <version> <edl.json>
edl.json : {"plans": [[source, debut, fin], ...], "noir_fin": 25, "boucle_images": 72,
            "musique_stop": <image de la timeline où la musique s'arrête net>}
source = dossier de rendu sous atelier/rendus/06/ (seule, tremble, ombre, insert) ; debut/fin inclus.
"""
import json, os, sys, shutil, subprocess, wave
import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
REND = os.path.join(ICI, "..", "rendus", "06")
FPS, SR = 25, 48000


def musique(n_images, boucle, stop):
    """Arpège répétitif (la mineur, croches) dont la boucle dure exactement `boucle` images,
    pour que chaque version redémarre la boucle au même endroit. Coupé net à `stop`."""
    duree = n_images / FPS; t = np.arange(int(duree * SR)) / SR
    notes = [220.0, 261.63, 329.63, 440.0, 329.63, 261.63, 220.0, 329.63] * 2
    pas = boucle / FPS / len(notes); y = np.zeros_like(t)
    for k in range(int(duree / pas) + 1):
        t0 = k * pas; f = notes[k % len(notes)]
        m = (t >= t0) & (t < t0 + pas * 1.8); tt = t[m] - t0
        y[m] += 0.18 * np.sin(2 * np.pi * f * tt) * np.exp(-tt * 6) * np.minimum(tt * 400, 1)
    y += 0.05 * np.sin(2 * np.pi * 110 * t) * (0.6 + 0.4 * np.sin(2 * np.pi * t / (boucle / FPS)))  # bourdon
    y[t >= stop / FPS] = 0.0  # arrêt net : pas de fondu, pas de son de casse
    return np.clip(y, -1, 1)


def main():
    v, edl_path = sys.argv[1], sys.argv[2]
    E = json.load(open(edl_path))
    seq = os.path.join(REND, f"seq-{v}"); shutil.rmtree(seq, ignore_errors=True); os.makedirs(seq)
    i = 0; debuts = []
    for src, a, b in E["plans"]:
        debuts.append((i, src, a))
        for f in range(a, b + 1):
            shutil.copy(os.path.join(REND, src, f"{f:04d}.png"), os.path.join(seq, f"{i:04d}.png")); i += 1
    noir = E.get("noir_fin", 25)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", os.path.join(seq, "0000.png"), "-vf", "geq=0:128:128",
                    os.path.join(seq, "noir.png")], check=True)
    for _ in range(noir):
        shutil.copy(os.path.join(seq, "noir.png"), os.path.join(seq, f"{i:04d}.png")); i += 1
    y = musique(i, E.get("boucle_images", 72), E.get("musique_stop", i))
    for f, _ in E.get("sfx", []):  # choc sourd (la table cognée) : 55 Hz amorti + bruit filtré grossièrement
        t = np.arange(int(0.35 * SR)) / SR; a = int(f / FPS * SR)
        choc = (0.5 * np.sin(2 * np.pi * 55 * t) + 0.15 * np.convolve(np.random.default_rng(3).normal(0, 1, t.size),
                np.ones(40) / 40, "same")) * np.exp(-t * 14)
        y[a:a + t.size] = np.clip(y[a:a + t.size] + choc[: max(0, min(t.size, y.size - a))], -1, 1)
    wav = os.path.join(REND, f"{v}.wav")
    with wave.open(wav, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((y * 32767).astype(np.int16).tobytes())
    mp4 = os.path.join(REND, f"versions-{v}.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(seq, "%04d.png"),
                    "-i", wav, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", mp4], check=True)
    # Planche 1 : première image de chaque plan (lisibilité à la coupe)
    sel = "+".join(f"eq(n\\,{d})" for d, _, _ in debuts)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", mp4, "-vf",
                    f"select='{sel}',scale=320:-1,tile={len(debuts)}x1", "-frames:v", "1", "-update", "1",
                    os.path.join(ICI, f"{v}-coupes.png")], check=True)
    # Planche 2 : mêmes images dans les trois versions (lignes) — preuve du cadre identique et du détail changé
    imgs = E.get("comparer", [20, 30, 38, 46, 58, 64])
    ent = []; filt = []
    dossiers = E.get("dossiers", {})
    for r, src in enumerate(["seule", "tremble", "ombre"]):
        src = dossiers.get(src, src)
        for c, f in enumerate(imgs):
            ent += ["-i", os.path.join(REND, src, f"{f:04d}.png")]
    n = len(imgs)
    for k in range(3 * n):
        filt.append(f"[{k}]scale=240:-1[s{k}]")
    lignes = []
    for r in range(3):
        filt.append("".join(f"[s{r * n + c}]" for c in range(n)) + f"hstack={n}[l{r}]"); lignes.append(f"[l{r}]")
    filt.append("".join(lignes) + "vstack=3")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", *ent, "-filter_complex", ";".join(filt),
                    os.path.join(ICI, f"{v}-comparaison.png")], check=True)
    # Mesures
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp4, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    lufs = [l for l in r.splitlines() if "I:" in l][-1].strip()
    json.dump(dict(images=i, duree_s=i / FPS, debuts_plans=debuts, loudness=lufs),
              open(os.path.join(ICI, f"{v}-mesures.json"), "w"), indent=1)
    print(i, "images", lufs)


if __name__ == "__main__":
    main()
