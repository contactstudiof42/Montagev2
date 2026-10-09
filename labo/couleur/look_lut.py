"""Labo couleur (b)+(c) : LUT 3D .cube « look » modéré, application ffmpeg vs Python.

Le look est DISPLAY-REFERRED : il attend une image déjà normalisée en Rec.709
(gamma 2.4 / BT.1886, valeurs 0-1). Il se place APRÈS la transformation technique
(log caméra -> Rec.709), jamais directement sur du log.

Look « teal & orange modéré » :
  1. contraste en S doux : f(x) = x - k*sin(2*pi*x)/(2*pi), k = 0.25
     (pente 0.75 aux extrémités = pied et épaule adoucis, 1.25 au milieu, noir/blanc fixes)
  2. ombres légèrement froides, hautes lumières légèrement chaudes,
     pondérées par la luminance (Rec.709) : poids ombres (1-Y)^2, poids hautes lumières Y^2
     (poids ramenés à 0 au noir et au blanc purs pour garder des extrêmes neutres)
  3. amplitude limitée (<= 0.03 sur 1.0) pour ne pas déformer les peaux.
Usage : python3 look_lut.py   (nécessite ffmpeg)
"""
import json, subprocess, time, warnings, os
warnings.filterwarnings("ignore")
import numpy as np
import colour

ICI = os.path.dirname(os.path.abspath(__file__))
RENDUS = os.path.abspath(os.path.join(ICI, "..", "rendus", "couleur"))
os.makedirs(RENDUS, exist_ok=True)
K = 0.25
OMBRES = np.array([-0.020, 0.004, 0.030])     # bleu-cyan
HAUTES = np.array([0.025, 0.008, -0.020])     # orangé
W709 = np.array([0.2126, 0.7152, 0.0722])

def look(rgb):
    rgb = np.asarray(rgb, dtype=np.float64)
    s = rgb - K * np.sin(2 * np.pi * rgb) / (2 * np.pi)
    y = np.clip(s @ W709, 0, 1)[..., None]
    # poids nuls au noir pur et au blanc pur : noir et blanc restent neutres
    ws = (1 - y) ** 2 * np.clip(y / 0.08, 0, 1)
    wh = y ** 2 * np.clip((1 - y) / 0.08, 0, 1)
    s = s + ws * OMBRES + wh * HAUTES
    return np.clip(s, 0, 1)

def write_ppm16(path, img):
    h, w, _ = img.shape
    data = np.round(np.clip(img, 0, 1) * 65535).astype(">u2").tobytes()
    with open(path, "wb") as f:
        f.write(f"P6\n{w} {h}\n65535\n".encode() + data)

def mire(w=960, h=540):
    img = np.zeros((h, w, 3))
    x = np.linspace(0, 1, w)
    img[0:90] = x[None, :, None]                                  # rampe de gris 0-1
    hsv = np.stack([x, np.ones_like(x), np.ones_like(x)], -1)     # balayage de teintes
    img[90:180] = colour.HSV_to_RGB(hsv)[None]
    hsv2 = np.stack([x, np.full_like(x, 0.35), np.full_like(x, 0.8)], -1)
    img[180:270] = colour.HSV_to_RGB(hsv2)[None]                  # teintes désaturées
    # ColorChecker 24 (valeurs sRGB/709 calculées par colour-science, D65)
    cc = colour.CCS_COLOURCHECKERS["ColorChecker24 - After November 2014"]
    xyY = np.array(list(cc.data.values()))
    XYZ = colour.xyY_to_XYZ(xyY)
    rgb = colour.XYZ_to_RGB(XYZ, "sRGB", illuminant=cc.illuminant, chromatic_adaptation_transform="Bradford")
    rgb = colour.eotf_inverse(np.clip(rgb, 0, 1), "ITU-R BT.1886")  # encodé pour un écran 709/2.4
    pw, ph = w // 6, (h - 270) // 4
    for i, c in enumerate(rgb):
        r, q = divmod(i, 6)
        img[270 + r * ph: 270 + (r + 1) * ph, q * pw:(q + 1) * pw] = c
    return img

def run(cmd):
    t = time.time(); p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode: raise RuntimeError(p.stderr[-800:])
    return time.time() - t

def main():
    res = {}
    # LUT 33 points
    lut = colour.LUT3D(colour.LUT3D.linear_table(33), name="F42 teal-orange modere (entree Rec709 g2.4)",
                       comments=["Look creatif display-referred. Entree: Rec.709 BT.1886 0-1. Sortie: idem.",
                                 "Ne PAS appliquer sur du log camera. Genere par labo/couleur/look_lut.py"])
    lut.table = look(lut.table)
    # .cube 33^3 ~ 1 Mo -> rangé dans labo/rendus/couleur (ignoré par git), régénérable
    cube = os.path.join(RENDUS, "look_teal_orange_modere_33.cube")
    colour.write_LUT(lut, cube)
    res["cube"] = {"fichier": os.path.basename(cube), "taille_octets": os.path.getsize(cube)}
    relu = colour.read_LUT(cube)
    res["cube"]["relecture_ecart_max"] = float(np.max(np.abs(relu.table - lut.table)))

    img = mire()
    src = os.path.join(RENDUS, "mire.ppm"); dst = os.path.join(RENDUS, "mire_look.ppm")
    write_ppm16(src, img)
    t = run(["ffmpeg", "-y", "-v", "error", "-i", src, "-vf", f"lut3d=file={cube}:interp=tetrahedral",
             "-pix_fmt", "rgb48be", "-f", "rawvideo", dst])
    res["ffmpeg_lut3d_secondes"] = round(t, 3)
    h, w, _ = img.shape
    ff = np.frombuffer(open(dst, "rb").read(), dtype=">u2").reshape(h, w, 3) / 65535.0

    src_q = np.round(img * 65535) / 65535  # même entrée quantifiée que ffmpeg
    py_lut = relu.apply(src_q, interpolator=colour.algebra.table_interpolation_tetrahedral)
    py_exact = look(src_q)
    def stats(a, b):
        d = np.abs(a - b)
        return {"moyen_8bit": round(float(d.mean() * 255), 4), "max_8bit": round(float(d.max() * 255), 4),
                "moyen_10bit": round(float(d.mean() * 1023), 4), "max_10bit": round(float(d.max() * 1023), 4)}
    res["ecart_ffmpeg_vs_python_LUT"] = stats(ff, py_lut)
    res["ecart_python_LUT_vs_fonction_exacte"] = stats(py_lut, py_exact)
    res["ecart_ffmpeg_vs_fonction_exacte"] = stats(ff, py_exact)
    # effet du look sur des valeurs repères
    rep = {"noir": [0, 0, 0], "gris 18% (0.4894 en 709/2.4)": [0.4894] * 3, "blanc": [1, 1, 1],
           "ombre 0.15": [0.15] * 3, "haute lumiere 0.85": [0.85] * 3, "peau ColorChecker #2": list(img[275, w // 6 + 5])}
    res["look_sur_reperes"] = {k: [round(float(v), 4) for v in look(np.array(vv))] for k, vv in rep.items()}
    res["entree_reperes"] = {k: [round(float(v), 4) for v in vv] for k, vv in rep.items()}

    # avant/après PNG léger
    png = os.path.join(ICI, "avant_apres.png")
    run(["ffmpeg", "-y", "-v", "error", "-i", src, "-i", dst.replace(".ppm", ".ppm"),
         "-f", "rawvideo", "-pix_fmt", "rgb48be", "-s", f"{w}x{h}", "-i", dst,
         "-filter_complex", "[0:v]scale=480:-2:flags=area[a];[2:v]scale=480:-2:flags=area[b];"
         "[a][b]hstack=inputs=2,format=rgb24", "-frames:v", "1", "-map", "0:v:0", png] if False else
        ["ffmpeg", "-y", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb48be", "-s", f"{w}x{h}", "-i", dst,
         "-filter_complex", "[0:v]scale=480:-2:flags=area[a];[1:v]scale=480:-2:flags=area[b];"
         "[a][b]hstack=inputs=2,format=rgb24[o]", "-map", "[o]", "-frames:v", "1", png])
    res["png"] = {"fichier": "avant_apres.png", "taille_ko": round(os.path.getsize(png) / 1024, 1)}
    print(json.dumps(res, ensure_ascii=False, indent=1))
    json.dump(res, open(os.path.join(ICI, "look_lut.json"), "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
