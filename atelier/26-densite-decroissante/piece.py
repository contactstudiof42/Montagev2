#!/usr/bin/env python3
"""Pièce 26 « Densité décroissante » : maquette échantillonnée du découpage B de l'examen n°11.

Usage : piece.py VERSION SORTIE_DIR      (VERSION = v1 | v2 | v3)
Écrit SORTIE_DIR/VERSION.mp4 (640x360, 24 i/s, son 48 kHz) et SORTIE_DIR/VERSION-evenements.json.
v1 : l'outil part à la relance (densité qui baisse tout de suite).
v2 : relance = pic (rafale de 3 s avec l'outil qui part), puis retrait.
v3 : v2 + mouvement interne dans les deux derniers extraits (flamme, souffle, dérive de lumière).
Tout est généré (formes Pillow, sons numpy) : aucune licence tierce.
"""
import json, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, SR = 640, 360, 24, 48000
VERSION, OUT = sys.argv[1], sys.argv[2]
rng = np.random.default_rng(26)
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
font_cap, font_cnt, font_slate = ImageFont.truetype(F, 30), ImageFont.truetype(FM, 16), ImageFont.truetype(FM, 22)

# Extraits : (heure du film, durée, densité avant, densité après, t relance ou None,
#             outils avant, outil qui part, objets restants début/fin, grade, éclairage)
TOUS = ["coupe", "punch", "sfx", "caption"]
EXTRAITS = [
    ("0:00", 25, 30, 30, None, TOUS + ["musique"], None, 48, 46, "chaud", "plein"),
    ("2:50", 25, 28, 22, 12.5, ["coupe", "punch", "sfx", "musique"], "musique", 38, 36, "chaud", "plein"),
    ("5:50", 25, 22, 18, 12.5, ["coupe", "punch", "sfx"], "sfx", 30, 28, "chaud", "plein"),
    ("9:20", 25, 14, 12, 12.5, ["coupe", "punch"], "punch", 21, 19, "chaud", "plein"),
    ("12:50", 25, 10, 12, 12.5, ["coupe"], None, 12, 11, "froid", "plein"),
    ("16:50", 25, 7, 5, 12.5, ["coupe"], "lumiere", 5, 4, "froid", "bascule"),
    ("18:00", 40, 0, 0, None, [], None, 2, 2, "froid", "bougie"),
]

# Personnages (5) et objets (48) dans une pièce vue de face
PERSOS = [(120, 250), (210, 262), (320, 255), (430, 262), (520, 250)]
COUL_P = [(230, 90, 70), (80, 160, 220), (240, 200, 60), (120, 200, 110), (200, 120, 210)]
OBJ = []
for i in range(48):
    x = 20 + (i % 16) * 38 + rng.integers(-4, 4)
    y = 70 + (i // 16) * 55 + rng.integers(-6, 6)
    OBJ.append((x, y, int(rng.integers(18, 32)), int(rng.integers(14, 40)),
                tuple(int(c) for c in rng.integers(60, 230, 3))))
# Plans : (cx, cy, zoom) — le témoin large et des plans serrés sur les personnes
PLANS = [(320, 180, 1.0)] + [(x, y - 40, 2.2) for x, y in PERSOS] + [(200, 120, 1.8), (440, 120, 1.8)]
CAPS = ["IL PART !", "NON NON NON", "LE CANAPÉ ?!", "48 H.", "PLUS RIEN", "AÏE"]


def planifier(ex, version):
    """Événements (t local, type) d'un extrait."""
    nom, dur, d0, d1, tr, outils, part, *_ = ex
    ev = []
    if not outils:  # temps long : un seul plan, la porte-refrain une fois
        return [(14.0, "porte")]
    t = 0.0
    while t < dur:
        apres = tr is not None and t >= tr
        d = d1 if apres else d0
        dispo = [o for o in outils if o != "musique" and not (apres and o == part)]
        if part == "lumiere" and apres:
            dispo = ["coupe"]
        if version != "v1" and tr is not None and tr - 3 <= t < tr:  # rafale : relance = pic
            d = d0 * 2.2
            if part in ("sfx", "punch"):
                dispo = dispo + [part] * 3
        pas = 60.0 / max(d, 1)
        k = dispo[int(rng.integers(len(dispo)))] if dispo else "coupe"
        ev.append((round(t, 3), k))
        t += pas * float(rng.uniform(0.75, 1.25))
    if tr is not None:
        ev.append((tr, "relance"))
    return sorted(ev)


def rendre_image(ex, ev, t, etat, version):
    nom, dur, d0, d1, tr, outils, part, n0, n1, grade, eclair = ex
    apres = tr is not None and t >= tr
    froid = grade == "froid"
    sombre = eclair == "bougie" or (eclair == "bascule" and apres)
    img = Image.new("RGB", (W, H), (30, 34, 44) if froid else (70, 58, 48))
    dr = ImageDraw.Draw(img)
    mur = (88, 98, 118) if froid else (196, 170, 140)
    sol = (60, 66, 80) if froid else (150, 112, 82)
    dr.rectangle([0, 0, W, 215], fill=mur)
    dr.rectangle([0, 215, W, H], fill=sol)
    restants = round(n0 + (n1 - n0) * min(t / dur, 1))
    for i, (x, y, w, h, c) in enumerate(OBJ[:restants]):
        dr.rectangle([x, y, x + w, y + h], fill=c)
    vivants = {"0:00": 5, "2:50": 5, "5:50": 5, "9:20": 4, "12:50": 4, "16:50": 3}.get(nom, 2)
    for i, (x, y) in enumerate(PERSOS[:vivants] if vivants > 2 else [PERSOS[1], PERSOS[3]]):
        bob = 2 * math.sin(t * 3 + i) if not sombre else 0
        dr.ellipse([x - 22, y - 60 + bob, x + 22, y - 16 + bob], fill=COUL_P[i])
        dr.rectangle([x - 26, y - 16, x + 26, y + 50], fill=tuple(int(v * 0.7) for v in COUL_P[i]))
    if sombre:
        # la bougie au centre ; v3 : flamme qui bouge, souffles, lumière qui dérive
        arr = np.asarray(img).astype(np.float32)
        yy, xx = np.mgrid[0:H, 0:W]
        cx, cy = 320, 270
        flick = 1.0
        if version == "v3":
            flick = 0.85 + 0.15 * math.sin(t * 7.3) * math.sin(t * 2.1 + 1) + 0.05 * math.sin(t * 17)
            cx += 6 * math.sin(t * 0.15)  # la lumière dérive lentement (on déplace la bougie d'un rien)
        r = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
        lum = 0.06 + 0.9 * flick * np.exp(-(r / 170) ** 2)
        tint = np.array([1.0, 0.72, 0.42]) * lum[..., None] + np.array([0.10, 0.14, 0.26]) * (1 - lum[..., None])
        arr = arr * tint
        img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
        dr = ImageDraw.Draw(img)
        h = 14 * (flick if version == "v3" else 1)
        dr.rectangle([cx - 4, cy - 2, cx + 4, cy + 22], fill=(220, 210, 190))
        dr.ellipse([cx - 4, cy - 2 - h, cx + 4, cy - 2], fill=(255, 210, 120))
        if version == "v3":  # souffles visibles dans le froid, un toutes les ~4 s par personne
            for j, (x, y) in enumerate([PERSOS[1], PERSOS[3]]):
                ph = (t + j * 1.9) % 4.0
                if ph < 1.5:
                    a = int(120 * (1 - ph / 1.5))
                    rr = 6 + 14 * ph
                    dr.ellipse([x + 20 + ph * 10 - rr, y - 44 - rr, x + 20 + ph * 10 + rr, y - 44 + rr],
                               outline=(a, a, a + 20), width=2)
    # plan courant (coupes) et punch-in
    cx, cy, z = PLANS[etat["plan"]]
    if etat["punch_jusqua"] > t:
        z *= 1.3
    cw, ch = W / z, H / z
    x0 = min(max(cx - cw / 2, 0), W - cw)
    y0 = min(max(cy - ch / 2, 0), H - ch)
    img = img.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.BILINEAR)
    dr = ImageDraw.Draw(img)
    if etat["caption_jusqua"] > t:
        txt = etat["caption_txt"]
        bw = dr.textlength(txt, font=font_cap)
        dr.rectangle([W / 2 - bw / 2 - 10, 280, W / 2 + bw / 2 + 10, 322], fill=(250, 230, 40))
        dr.text((W / 2 - bw / 2, 284), txt, font=font_cap, fill=(10, 10, 10))
    # compteur : fixe, ne s'anime jamais
    dr.text((470, 14), f"OBJETS RESTANTS {restants:02d}", font=font_cnt, fill=(255, 255, 255))
    return img


def synth(ex, ev, version):
    nom, dur, d0, d1, tr, outils, part, *_, eclair = ex
    n = int(dur * SR)
    tt = np.arange(n) / SR
    a = 0.02 * rng.standard_normal(n)  # ambiance de pièce
    if eclair == "bougie" or nom == "16:50":
        vent = np.convolve(rng.standard_normal(n), np.ones(400) / 400, "same")
        a += 0.25 * vent * (0.6 + 0.4 * np.sin(2 * np.pi * 0.07 * tt))
    if "musique" in outils:
        fin = n if (part != "musique" or tr is None) else int(tr * SR)
        if version != "v1" and part == "musique":  # dernier drop : la musique part sur un pic
            fin = int((tr + 0.6) * SR)
        beat = 0.5
        for b in np.arange(0, fin / SR, beat):
            i = int(b * SR)
            L = min(int(0.18 * SR), n - i)
            k = np.arange(L) / SR
            a[i:i + L] += 0.5 * np.sin(2 * np.pi * (110 * np.exp(-k * 18) + 45) * k) * np.exp(-k * 14)
        bass = 0.12 * np.sin(2 * np.pi * 55 * tt) * (np.sin(2 * np.pi * 2 * tt) > 0)
        a[:fin] += bass[:fin]
        if version != "v1" and part == "musique":
            i = int(tr * SR); L = int(0.8 * SR)
            k = np.arange(L) / SR
            a[i:i + L] += 0.7 * np.sin(2 * np.pi * 40 * k) * np.exp(-k * 3)  # drop
    for t, kind in ev:
        i = int(t * SR)
        if kind == "sfx":
            L = min(int(0.25 * SR), n - i); k = np.arange(L) / SR
            a[i:i + L] += 0.35 * np.sin(2 * np.pi * (300 + 900 * k * 4) * k) * np.exp(-k * 9)
        elif kind == "punch":
            L = min(int(0.2 * SR), n - i); k = np.arange(L) / SR
            a[i:i + L] += 0.25 * rng.standard_normal(L) * np.sin(np.pi * k / 0.2)
        elif kind == "caption":
            L = min(int(0.02 * SR), n - i)
            a[i:i + L] += 0.4 * np.sin(2 * np.pi * 2000 * np.arange(L) / SR)
        elif kind == "porte":
            L = min(int(0.6 * SR), n - i); k = np.arange(L) / SR
            a[i:i + L] += 0.8 * (np.sin(2 * np.pi * 70 * k) + 0.4 * rng.standard_normal(L)) * np.exp(-k * 10)
    # voix : bouffées de « babil » (bruit filtré modulé), plus rares et plus fortes vers la fin
    nv = max(2, int(dur * (0.5 if outils else 0.12)))
    for _ in range(nv):
        t0 = float(rng.uniform(0, dur - 1.5)); L = int(rng.uniform(0.6, 1.4) * SR); i = int(t0 * SR)
        k = np.arange(L) / SR
        src = np.convolve(rng.standard_normal(L), np.ones(12) / 12, "same")
        a[i:i + L] += (0.5 if outils else 0.8) * src * (0.5 + 0.5 * np.sin(2 * np.pi * 5 * k)) * np.sin(np.pi * k / k[-1])
    return np.clip(a, -0.99, 0.99).astype(np.float32)


def main():
    os.makedirs(OUT, exist_ok=True)
    vid = os.path.join(OUT, f"{VERSION}-video.raw"); aud = os.path.join(OUT, f"{VERSION}.f32")
    journal = []
    tglob = 0.0
    with open(vid, "wb") as fv, open(aud, "wb") as fa:
        for ex in EXTRAITS:
            # carton de 0,6 s : l'heure du film
            slate = Image.new("RGB", (W, H), (0, 0, 0))
            ImageDraw.Draw(slate).text((270, 165), f"≈ {ex[0]}", font=font_slate, fill=(160, 160, 160))
            for _ in range(int(0.6 * FPS)):
                fv.write(slate.tobytes())
            fa.write(np.zeros(int(0.6 * SR), np.float32).tobytes())
            tglob += 0.6
            ev = planifier(ex, VERSION)
            journal.append({"extrait": ex[0], "debut": round(tglob, 3), "duree": ex[1],
                            "evenements": [[round(tglob + t, 3), k] for t, k in ev]})
            etat = {"plan": 0, "punch_jusqua": -1, "caption_jusqua": -1, "caption_txt": ""}
            j = 0
            for f in range(int(ex[1] * FPS)):
                t = f / FPS
                while j < len(ev) and ev[j][0] <= t:
                    k = ev[j][1]
                    if k == "coupe":
                        etat["plan"] = int(rng.choice([p for p in range(len(PLANS)) if p != etat["plan"]]))
                    elif k == "punch":
                        etat["punch_jusqua"] = t + 0.5
                    elif k == "caption":
                        etat["caption_jusqua"] = t + 0.9
                        etat["caption_txt"] = CAPS[int(rng.integers(len(CAPS)))]
                    elif k == "relance" and ex[6] == "lumiere":
                        etat["plan"] = 0
                    j += 1
                if not ex[5]:
                    etat["plan"] = 0  # temps long : un seul plan
                fv.write(rendre_image(ex, ev, t, etat, VERSION).tobytes())
            fa.write(synth(ex, ev, VERSION).tobytes())
            tglob += ex[1]
    mp4 = os.path.join(OUT, f"{VERSION}.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                    "-r", str(FPS), "-i", vid, "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", aud,
                    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                    "-shortest", mp4], check=True)
    os.remove(vid); os.remove(aud)
    with open(os.path.join(OUT, f"{VERSION}-evenements.json"), "w") as f:
        json.dump(journal, f)
    print(mp4, round(tglob, 1), "s")


if __name__ == "__main__":
    main()
