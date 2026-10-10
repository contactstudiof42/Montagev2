"""Pièce 18 v6 : la cause montée. python3 -I v6.py <dossier_rendus> <config.ocio> <sortie> <dossier_planches>
Rue : deux EXR linéaires du cadre v3 (scene.py, SERRE=1 LENS=35, lampadaire 1 allumé / éteint), vue AgX par OCIO
comme anime.py (v4). Insert : insert.py (16 images PNG, « presse » = la bascule claque à l'image 14 ; « lache » =
déjà en bas, le doigt se retire). Trois montages de 113 images (4,5 s, 25 i/s), même ambiance sonore (souffle faible) :
  A sans cause : rue allumée, extinction sèche à l'image 40, noir tenu ; aucun son d'événement.
  B cause avant : rue 0-29, insert « presse » 30-45 (clac du contacteur à 43, sur la bascule), retour rue allumée
    46-47, extinction 48 (2 images de retard = le temps de lire « c'est la même rue »).
  C cause après : extinction sèche muette à 40, noir tenu jusqu'à 74, insert « lache » 75-90 (sans clac : la bascule
    est déjà en bas), retour sur la rue noire 91-112.
v6 bis (suffixe _cle, planches v6-B2 / v6-C2) : mêmes montages, insert ramené par gain linéaire à la luminance
du plan qui l entoure (23 = rue allumée en B, 8 = rue noire en C) : rendu brut, il était 2,4 fois plus clair que la rue.\nv6 ter (suffixe _nuit, planche v6-C3) : insert C rendu NUIT=1 (insert.py) : seule sa lanterne, basse, l éclaire."""
import sys, os, subprocess, wave
import numpy as np, OpenEXR, PyOpenColorIO as ocio
from PIL import Image, ImageDraw
d, cfg, out, pl_dir = sys.argv[1:5]; os.makedirs(out, exist_ok=True)
rd = lambda n: OpenEXR.File(f"{d}/{n}.exr").channels()["RGBA"].pixels[..., :3].astype(np.float32)
proc = ocio.Config.CreateFromFile(cfg).getProcessor("Linear Rec.709", "sRGB", "AgX", ocio.TRANSFORM_DIR_FORWARD).getDefaultCPUProcessor()
def vue(lin):
    x = np.ascontiguousarray(lin.copy()); proc.applyRGB(x); return Image.fromarray((np.clip(x, 0, 1) * 255 + 0.5).astype(np.uint8))
ALLUME, NOIR = vue(rd("e0100000")), vue(rd("e0000000"))
def Y(im): a = np.asarray(im).astype(float); return float((0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]).mean())
CLE = {"B": 23.0, "C": 8.0}   # v6 bis : insert ramené à la luminance du plan qui l'entoure (rue allumée en B, rue noire en C)
def ins(s, k, cle=None):
    im = Image.open(f"{d}/insert/{s}_{k:04d}.png").convert("RGB")
    if cle is None: return im
    a = np.asarray(im).astype(np.float32) / 255; lin = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)
    g = 1.0
    for _ in range(8):   # gain linéaire (exposition) cherché pour que la luminance moyenne affichée vaille « cle »
        v = np.clip(lin * g, 0, 1); v = np.where(v <= 0.0031308, v * 12.92, 1.055 * v ** (1 / 2.4) - 0.055)
        g *= (cle / Y(v * 255)) ** 2.2
    return Image.fromarray((v * 255 + 0.5).astype(np.uint8))
N, FPS, SR = 113, 25, 48000
def montage(nom):
    cle = CLE[nom[0]] if nom.endswith("_cle") else None
    seq, clacs = [], []
    for i in range(N):
        if nom.startswith("A"): im, lab = (ALLUME if i < 40 else NOIR), "rue"
        elif nom.startswith("B"):
            if i < 30: im, lab = ALLUME, "rue"
            elif i < 46: im, lab = ins("presse", i - 29, cle), "insert"
            else: im, lab = (ALLUME if i < 48 else NOIR), "rue"
        else:
            if i < 75: im, lab = (ALLUME if i < 40 else NOIR), "rue"
            elif i < 91: im, lab = ins("lache_nuit" if nom.endswith("_nuit") else "lache", i - 74, cle), "insert"
            else: im, lab = NOIR, "rue"
        seq.append((im, lab))
    if nom.startswith("B"): clacs = [43]
    return seq, clacs
def son(clacs, path):
    rng = np.random.default_rng(18); n = N * SR // FPS
    a = np.convolve(rng.normal(0, 1, n), np.ones(40) / 40, "same") * 0.02          # souffle de rue, faible et constant
    for f in clacs:   # contacteur : transitoire de 3 ms + résonance métallique courte à 2,3 kHz
        s = f * SR // FPS; t = np.arange(int(0.08 * SR)) / SR
        c = rng.normal(0, 1, t.size) * np.exp(-t / 0.003) * 0.6 + np.sin(2 * np.pi * 2300 * t) * np.exp(-t / 0.015) * 0.35
        a[s:s + t.size] += c[: n - s]
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())
for nom in ("A_sans_cause", "B_cause_avant", "C_cause_apres", "B_cause_avant_cle", "C_cause_apres_cle", "C_cause_apres_nuit"):
    seq, clacs = montage(nom); od = f"{out}/{nom}"; os.makedirs(od, exist_ok=True)
    for i, (im, _) in enumerate(seq): im.save(f"{od}/{i:03d}.png")
    son(clacs, f"{out}/{nom}.wav")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", f"{od}/%03d.png", "-i", f"{out}/{nom}.wav",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-c:a", "aac", "-shortest", f"{out}/{nom}.mp4"], check=True)
    ys = [Y(im) for im, _ in seq]
    print(nom, "luminance /5 :", " ".join(f"{y:.0f}" for y in ys[::5]))
    # planche : images clés (coupes et événements) à 160 px + bande de luminance + marque du clac
    cles = {"A_sans_cause": [0, 30, 38, 39, 40, 41, 45, 60, 90, 112],
            "B_cause_avant": [29, 30, 36, 40, 42, 43, 45, 46, 47, 48, 60, 112],
            "C_cause_apres": [39, 40, 60, 74, 75, 80, 85, 90, 91, 112]}[nom.replace("_cle", "").replace("_nuit", "")]
    W, H = 160, 90; pl = Image.new("RGB", (W * 6, (H + 18) * 2 + 70), (20, 20, 20)); dr = ImageDraw.Draw(pl)
    for k, i in enumerate(cles):
        x, y = (k % 6) * W, (k // 6) * (H + 18)
        pl.paste(seq[i][0].resize((W, H), Image.LANCZOS), (x, y + 16))
        dr.text((x + 3, y + 2), f"{i} {seq[i][1]}{' CLAC' if i in clacs else ''}", fill=(255, 220, 90) if i in clacs else (220, 220, 220))
    y0 = (H + 18) * 2 + 4; gx = W * 6 / N; m = max(ys)
    for i, lab in enumerate(seq):
        if lab[1] == "insert": dr.rectangle([gx * i, y0, gx * (i + 1), y0 + 60], fill=(45, 45, 70))
    dr.line([(gx * i, y0 + 60 - 56 * v / m) for i, v in enumerate(ys)], fill=(255, 200, 80), width=2)
    for f in clacs: dr.line([(gx * f, y0), (gx * f, y0 + 60)], fill=(255, 80, 80), width=2)
    dr.text((4, y0 + 46), f"{nom} : luminance par image (bleu = insert, rouge = clac), 113 images", fill=(200, 200, 200))
    pl.save(f"{pl_dir}/v6-{nom[0]}{'2' if nom.endswith('_cle') else '3' if nom.endswith('_nuit') else ''}-planche.png", optimize=True)
