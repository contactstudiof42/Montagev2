"""Pièce 09 « Générique de l'équipe » — cartons Pillow calés sur une boucle à 128 BPM.
python3 generique.py mode sortie_dir      mode = naif | lumconst | une_police
naif       : fonds noir / blanc alternés (l'effet stroboscopique « facile »)
lumconst   : fonds sombres de teintes différentes à luminance relative égale (~0,03), texte clair de teintes variées
une_police : comme lumconst, mais tout en Inter Bold (contrôle du principe « une coupe = une rupture de forme »)
Le son est fixé d'abord ; les durées des cartons en découlent (temps, demi-temps, quarts de temps).
"""
import colorsys, json, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

mode, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
V2 = "--v2" in sys.argv  # v2 : rupture d'échelle et de position (le nom peut déborder du cadre), texte moins lumineux en option
TXT_V = float(sys.argv[sys.argv.index("--txt") + 1]) if "--txt" in sys.argv else 1.0
W, H, FPS, BPM, SR = 480, 270, 25, 128, 48000
B = 60 / BPM * FPS                                     # 11,72 images par temps
rng = np.random.default_rng(42)
F = "/usr/share/fonts/"
POL = {  # métier -> (police, nom inventé) ; une police par « personnalité »
    "production": (F + "opentype/inter/InterDisplay-Black.otf", "NORA VASSEUR"),
    "montage": (F + "truetype/dejavu/DejaVuSansMono-Bold.ttf", "ILIES MARCHAND"),
    "image": (F + "truetype/freefont/FreeSerifItalic.ttf", "Joanna Prieto"),
    "son": (F + "opentype/unifont/unifont.otf", "BASILE KONE"),
    "scénario": (F + "truetype/liberation/LiberationSerif-Bold.ttf", "Mathilde Arnaud"),
    "décors": (F + "truetype/crosextra/Caladea-Bold.ttf", "SAMIR OUDJANE"),
    "costumes": (F + "truetype/crosextra/Carlito-Italic.ttf", "léa fontaine"),
    "script": (F + "truetype/liberation/LiberationMono-Regular.ttf", "Paul Henrion"),
    "effets": (F + "opentype/ipafont-gothic/ipag.ttf", "KENJI MORI"),
    "étalonnage": (F + "truetype/freefont/FreeMonoBold.ttf", "ADÈLE ROUX"),
}
ACTEURS = [("avec", "CLARA DUVAL"), ("et", "YANIS BEKKALI"), ("et", "ROSE AMIEL"), ("et", "THÉO LANG")]
TITRE = "SAS"
INTER = F + "opentype/inter/Inter-Bold.otf"
if not os.path.exists(INTER):
    INTER = F + "opentype/inter/InterDisplay-Bold.otf"

# --- découpage : (début en temps, durée en temps, type) ---
plan = [(b, 1, "lent") for b in range(4)] + [(4 + i / 2, .5, "mi") for i in range(8)] \
     + [(8 + i / 4, .25, "vite") for i in range(16)] + [(12 + i, 1, "acteur") for i in range(4)] + [(16, 5.33, "titre")]
roles = list(POL)


def lum(rgb):  # luminance relative (sRGB -> linéaire)
    c = np.array(rgb) / 255; c = np.where(c <= .04045, c / 12.92, ((c + .055) / 1.055) ** 2.4)
    return float(c @ [.2126, .7152, .0722])


def fond_lum(h, cible=.03):  # teinte h à luminance relative ~cible (recherche sur la valeur)
    best = None
    for v in np.linspace(.05, 1, 200):
        rgb = [int(255 * x) for x in colorsys.hsv_to_rgb(h, .85, v)]
        d = abs(lum(rgb) - cible)
        if best is None or d < best[0]: best = (d, rgb)
    return tuple(best[1])


def carton(i, typ, d):
    V4 = "--v4" in sys.argv
    if V4 and typ == "acteur":  # v4 : le sommet change de règle : fond commun, deux lignes géantes, même police
        prenom, nomf = ACTEURS[i - 28][1].split(" ", 1)
        im = Image.new("RGB", (W, H), fond_lum(.62)); dr = ImageDraw.Draw(im)
        for k, mot in enumerate((prenom, nomf)):
            t = int(H * .46)
            ft = ImageFont.truetype(F + "opentype/inter/InterDisplay-Black.otf", t)
            while dr.textlength(mot, font=ft) > W * .96: t -= 2; ft = ImageFont.truetype(F + "opentype/inter/InterDisplay-Black.otf", t)
            dr.text(((W - dr.textlength(mot, font=ft)) / 2, 8 + k * H * .47), mot, font=ft, fill=(245, 225, 140))
        return im, dict(police="InterDisplay-Black", fond=fond_lum(.62), echelle=.46)
    if typ == "titre":
        role, (pol, nom), echelle = "", (F + "opentype/inter/InterDisplay-Black.otf", TITRE), 0.55
    elif typ == "acteur":
        role, nom = ACTEURS[i - 28]; pol = F + "opentype/inter/InterDisplay-Black.otf"
        echelle = 0.5 if "--v3" in sys.argv else 0.22  # v3 : le sommet doit être plus gros que le chaos qui le précède
    else:
        role = roles[i % len(roles)]; pol, nom = POL[role]; echelle = {"lent": .1, "mi": .13, "vite": .16}[typ]
        echelle *= rng.uniform(.8, 1.25)
        if V2 and typ in ("mi", "vite"):
            echelle = rng.choice([.1, .18, .35, .6])
    if mode == "une_police": pol = INTER
    h = (i * 0.37) % 1
    if mode == "naif":
        bg = (0, 0, 0) if i % 2 == 0 else (255, 255, 255)
        fg = (255, 255, 255) if i % 2 == 0 else (0, 0, 0)
    else:
        tv = .72 if ("--v4" in sys.argv and typ == "vite") else TXT_V  # v4 : marge de photosensibilité au plus rapide
        bg = fond_lum(h); fg = tuple(int(255 * x) for x in colorsys.hsv_to_rgb((h + .5) % 1, .35, tv))
    if typ == "titre": bg, fg = (0, 0, 0), (235, 235, 230)
    im = Image.new("RGB", (W, H), bg); dr = ImageDraw.Draw(im)
    taille = int(H * echelle)
    try:
        f = ImageFont.truetype(pol, taille)
    except OSError:
        f = ImageFont.truetype(INTER, taille)
    while dr.textlength(nom, font=f) > W * (2.2 if V2 and typ in ("mi", "vite") else .97) and taille > 8:
        taille -= 2; f = ImageFont.truetype(pol if mode != "une_police" else INTER, taille)
    tw = dr.textlength(nom, font=f)
    y = H / 2 - taille / 2 + (rng.uniform(-40, 40) if typ in ("mi", "vite") else 0)
    x = (W - tw) / 2
    if V2 and typ in ("mi", "vite"):  # ancrage changeant : gauche, droite, débord, haut, bas
        x = rng.choice([12, W - tw - 12, (W - tw) / 2, -tw * .25]); y = rng.uniform(-taille * .2, H - taille * .9)
    dr.text((x, y), nom, font=f, fill=fg)
    if role and typ in ("lent", "mi", "acteur"):
        fr = ImageFont.truetype(pol if mode != "une_police" else INTER, max(10, taille // 3)) if typ != "acteur" else ImageFont.truetype(INTER, 14)
        dr.text(((W - dr.textlength(role, font=fr)) / 2, y - taille * .5 - 6), role, font=fr, fill=fg)
    return im, dict(police=os.path.basename(pol), fond=bg, echelle=round(taille / H, 3))


# --- images ---
meta, n = [], 0
for i, (b0, db, typ) in enumerate(plan):
    f0, f1 = round(b0 * B), min(250, round((b0 + db) * B))
    im, m = carton(i, typ, f1 - f0); meta.append(dict(i=i, debut=f0, fin=f1, type=typ, **m))
    for f in range(f0, f1):
        im.save(f"{out}/{f:04d}.png")

# --- son : boucle (kick, charleston, basse) + SFX de coupe ---
N = 10 * SR; t = np.arange(N) / SR; a = np.zeros(N)
bs = 60 / BPM
def env(n, k): return np.exp(-np.arange(n) / (k * SR))
for k in range(int(16 / 1)):  # boucle jusqu'au temps 16 ; le titre est un autre monde
    s = int(k * bs * SR); n = int(.25 * SR)
    ph = 2 * np.pi * np.cumsum(50 + 90 * env(n, .03)) / SR
    a[s:s + n] += .9 * np.sin(ph) * env(n, .12)                         # kick
    for h in (0, .5):
        s2 = int((k + h + .25) * bs * SR); m = int(.04 * SR)
        a[s2:s2 + m] += .15 * rng.normal(0, 1, m) * env(m, .008)        # charleston (contretemps)
    m = int(bs * SR); notes = [55, 55, 65.4, 49]
    a[s:s + m] += .25 * np.sin(2 * np.pi * notes[k % 4] * t[:m]) * env(m, .3)
# riser sur les temps 8-12, coupé 1 image avant le temps 12
s, e = int(8 * bs * SR), int((12 * bs - 1 / FPS) * SR)
tt = t[:e - s]; a[s:e] += .25 * rng.normal(0, 1, e - s) * (tt / tt[-1]) ** 2
for m_ in meta:  # SFX : clic sur chaque coupe rapide, impact sur les acteurs, sous-grave sur le titre
    s = int(m_["debut"] / FPS * SR)
    if m_["type"] == "vite":
        n = int(.015 * SR); a[s:s + n] += .3 * rng.normal(0, 1, n) * env(n, .003)
    if m_["type"] == "acteur":
        n = int(.4 * SR); a[s:s + n] += .6 * (np.sin(2 * np.pi * 45 * t[:n]) + .5 * rng.normal(0, 1, n) * env(n, .02)) * env(n, .15)
    if m_["type"] == "titre":
        n = min(N - s, int(2.5 * SR)); a[s:s + n] += .7 * np.sin(2 * np.pi * np.cumsum(60 - 25 * t[:n] / 2.5) / SR) * env(n, .9)
a = np.clip(a / np.abs(a).max() * .9, -1, 1)
with wave.open(f"{out}/son.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((a * 32767).astype(np.int16).tobytes())
R = os.path.dirname(os.path.abspath(out.rstrip("/"))); name = os.path.basename(out.rstrip("/"))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "25", "-i", f"{out}/%04d.png", "-i", f"{out}/son.wav",
                "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", f"{R}/{name}.mp4"], check=True)
json.dump(meta, open(f"{out}/cartons.json", "w"), ensure_ascii=False, indent=0)
print(name, len(meta), "cartons ; durées (images) :", [m_["fin"] - m_["debut"] for m_ in meta])
