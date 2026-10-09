#!/usr/bin/env python3
"""Labo : bandes (banding) d'un dégradé SOMBRE selon l'encodage.
Source : dégradé vertical 16 bits, luma 4 → 34 /255 (un fond nocturne type Ziak / pièce 02), 48 images, léger mouvement.
Variantes : quantification 8 bits brute ou tramée (dither), H.264 8 bits CRF 16/20/23, -tune grain, 10 bits, HEVC 10 bits.
Mesure perceptive approchée : on floute (σ=3 px, l'œil intègre le grain), on prend le profil vertical central,
et on compte les « marches » : indice = max|dérivée| / moyenne|dérivée| (1 = lisse ; >3 = marches visibles),
+ largeur max d'un palier plat (px). Usage : python3 banding.py ; sorties lourdes dans labo/rendus/encodage/."""
import json, os, subprocess
import numpy as np
ICI = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(ICI, "..", "rendus", "encodage"); os.makedirs(R, exist_ok=True)
W, H, N = 540, 960, 48
rng = np.random.default_rng(1)
y = np.linspace(0, 1, H)[:, None]; x = np.linspace(-1, 1, W)[None, :]
def image(k, dither):
    v = (4 + 30 * y**1.2) * (1 - 0.15 * x**2) * (1 + 0.03 * np.sin(k / 8))  # en niveaux /255
    v = np.repeat(v[:, :, None], 3, 2) * np.array([0.55, 1.0, 0.95])        # teinte cyan-vert
    if dither: v = v + rng.uniform(-0.5, 0.5, v.shape) + rng.uniform(-0.5, 0.5, v.shape)  # TPDF ±1 niveau
    return v
def ecrire_src(nom, dither, bits):
    p = os.path.join(R, nom)
    with open(p, "wb") as f:
        for k in range(N):
            v = image(k, dither)
            if bits == 8: f.write(np.clip(np.round(v), 0, 255).astype(np.uint8).tobytes())
            else: f.write(np.clip(np.round(v * 257), 0, 65535).astype("<u2").tobytes())
    return p
src8 = ecrire_src("src8.rgb", False, 8); src8d = ecrire_src("src8d.rgb", True, 8); src16 = ecrire_src("src16.rgb", False, 16)
VAR = {
 "A_8bits_brut_crf20":        (src8,  "rgb24",  ["-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p"]),
 "B_8bits_tram_crf20":        (src8d, "rgb24",  ["-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p"]),
 "C_8bits_tram_crf20_grain":  (src8d, "rgb24",  ["-c:v", "libx264", "-crf", "20", "-tune", "grain", "-pix_fmt", "yuv420p"]),
 "D_8bits_tram_crf16_grain":  (src8d, "rgb24",  ["-c:v", "libx264", "-crf", "16", "-tune", "grain", "-pix_fmt", "yuv420p"]),
 "E_8bits_tram_crf23":        (src8d, "rgb24",  ["-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p"]),
 "F_10bits_x264_crf20":       (src16, "rgb48le", ["-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p10le"]),
 "G_10bits_x265_crf22":       (src16, "rgb48le", ["-c:v", "libx265", "-crf", "22", "-pix_fmt", "yuv420p10le", "-x265-params", "log-level=error"]),
 "H_16bits_vers_8_aq3":       (src16, "rgb48le", ["-c:v", "libx264", "-crf", "20", "-aq-mode", "3", "-pix_fmt", "yuv420p"]),
}
def mesure(path, ref=False):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", "select='eq(n,24)'", "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray16le", "-"],
                         capture_output=True).stdout
    g = np.frombuffer(raw, "<u2").reshape(H, W).astype(float) / 257.0
    k = np.exp(-np.arange(-9, 10)**2 / (2 * 9)); k /= k.sum()
    b = np.apply_along_axis(lambda c: np.convolve(c, k, "same"), 0, g)
    b = np.apply_along_axis(lambda r: np.convolve(r, k, "same"), 1, b)
    prof = b[20:-20, W//2-40:W//2+40].mean(1)
    d = np.abs(np.diff(prof))
    brut = g[20:-20, W//2]; plat = 0; run = 1
    for i in range(1, len(brut)):
        run = run + 1 if abs(brut[i] - brut[i-1]) < 0.02 else 1; plat = max(plat, run)
    return {"indice_marches": round(float(d.max() / d.mean()), 2), "palier_max_px": int(plat),
            "niveaux_distincts_colonne": int(len(np.unique(np.round(brut, 2))))}
res = {}
for nom, (src, pf, enc) in VAR.items():
    out = os.path.join(R, nom + ".mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", pf, "-s", f"{W}x{H}", "-r", "30", "-i", src,
                    "-vf", "scale=out_color_matrix=bt709:out_range=tv", *enc, "-preset", "medium", out], check=True)
    m = mesure(out); m["ko"] = os.path.getsize(out) // 1024; res[nom] = m; print(nom, m)
# Simulation de la ré-encode plateforme : le 10 bits et le tramé CRF16 repassent en 8 bits CRF 23 (« Instagram-like »)
for nom in ("D_8bits_tram_crf16_grain", "F_10bits_x264_crf20", "G_10bits_x265_crf22"):
    out = os.path.join(R, nom + "_reenc8.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(R, nom + ".mp4"), "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p", out], check=True)
    m = mesure(out); m["ko"] = os.path.getsize(out) // 1024; res[nom + "_reenc8"] = m; print(nom + "_reenc8", m)
json.dump(res, open(os.path.join(ICI, "banding_resultats.json"), "w"), indent=1)
# Contrôles du critère de mesure : sources sans perte (qp 0, 4:4:4) — le tramage doit y donner un indice bas
for nom, src, pf, fmt in [("T1_src8_brut_qp0", src8, "rgb24", "yuv444p"), ("T2_src8_tram_qp0", src8d, "rgb24", "yuv444p"),
                          ("T3_src8_tram_qp0_420", src8d, "rgb24", "yuv420p")]:
    out = os.path.join(R, nom + ".mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", pf, "-s", f"{W}x{H}", "-r", "30", "-i", src,
                    "-vf", "scale=out_color_matrix=bt709:out_range=tv", "-c:v", "libx264", "-qp", "0", "-pix_fmt", fmt, out], check=True)
    m = mesure(out); m["ko"] = os.path.getsize(out) // 1024; res[nom] = m; print(nom, m)
json.dump(res, open(os.path.join(ICI, "banding_resultats.json"), "w"), indent=1)
# Remède testé : grain volontaire plus fort (amplitude a niveaux, taille de grain t px), encodé CRF 20 puis ré-encodé CRF 23
def ecrire_grain(nom, a, t):
    p = os.path.join(R, nom)
    with open(p, "wb") as f:
        for k in range(N):
            v = image(k, False)
            g = rng.standard_normal((H // t + 1, W // t + 1))
            g = np.kron(g, np.ones((t, t)))[:H, :W][:, :, None] * a / 2   # σ = a/2 niveaux, grain monochrome
            f.write(np.clip(np.round(v + g), 0, 255).astype(np.uint8).tobytes())
    return p
for a, t in [(2, 1), (4, 1), (4, 2), (6, 2)]:
    nom = f"I_grain_a{a}_t{t}"; src = ecrire_grain(nom + ".rgb", a, t)
    out = os.path.join(R, nom + ".mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30", "-i", src,
                    "-vf", "scale=out_color_matrix=bt709:out_range=tv", "-c:v", "libx264", "-crf", "20", "-tune", "grain", "-pix_fmt", "yuv420p", out], check=True)
    m = mesure(out); m["ko"] = os.path.getsize(out) // 1024; res[nom] = m; print(nom, m)
    o2 = os.path.join(R, nom + "_reenc8.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", out, "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p", o2], check=True)
    m = mesure(o2); m["ko"] = os.path.getsize(o2) // 1024; res[nom + "_reenc8"] = m; print(nom + "_reenc8", m)
json.dump(res, open(os.path.join(ICI, "banding_resultats.json"), "w"), indent=1)
