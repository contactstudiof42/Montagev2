"""Labo miniature YouTube : lisibilité du texte selon sa taille, son style, le nombre de mots et la taille d'affichage.
python3 -I miniature.py OUT_DIR > resultats.tsv
Miniature 1280×720 (le minimum recommandé est 640 de large ; YouTube accepte jusqu'à 3840×2160, 2026-10) ; deux fonds
synthétiques (« uni » : dégradé sombre ; « chargé » : texture colorée à haute fréquence, pire cas : foule, feuillage) ;
texte en Inter Black majuscule, hauteur de capitale = X % de la hauteur de la miniature ; trois styles (plein blanc,
blanc à contour noir, bandeau jaune texte noir) ; trois textes (2, 4, 8 mots). Chaque miniature est réduite aux tailles
d'affichage courantes (168×94 « vidéos suggérées » sur ordinateur, 246×138, 360×202 « recherche » ; tailles relevées
de mémoire sur l'interface, à vérifier en phase 2), puis réagrandie ×4 et lue par tesseract (fra).
Score = part des mots de plus d'une lettre retrouvés, OCR sur la seule bande du texte (v2 : sans recadrage, la texture
du fond chargé était lue comme des lettres et tous les scores tombaient à ~0,3 quelle que soit la taille). v3 : après
réduction à la taille d'affichage, agrandissement pour que la capitale fasse ~30 px (v2 agrandissait ×4 partout : les
grandes tailles donnaient des lettres de 300 px que tesseract ne lit plus, d'où des scores qui baissaient quand le texte grossit). L'OCR est un proxy (il lit mal le texte détouré, session 13) : il classe les cas,
il ne fixe pas un seuil d'œil."""
import os, subprocess, sys, tempfile, unicodedata
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
W, H = 1280, 720
FONT = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
TEXTES = {2: "IL A MENTI", 4: "J'AI TESTÉ LE PIRE", 8: "J'AI PASSÉ 24 HEURES DANS LE NOIR TOTAL"}
TAILLES = [6, 9, 12, 16, 22]                       # hauteur de capitale, % de la hauteur de la miniature
STYLES = ["plein", "contour", "bandeau"]
AFFICHAGES = [(168, 94), (246, 138), (360, 202)]
rng = np.random.default_rng(1)
y, x = np.mgrid[0:H, 0:W] / H
FONDS = {
    "uni": (np.dstack([0.10 + 0.15 * x, 0.08 + 0.05 * y, 0.20 - 0.1 * x]) * 255).clip(0, 255).astype(np.uint8),
    "charge": (np.kron(rng.uniform(0, 1, (H // 6, W // 6 + 1, 3)), np.ones((6, 6, 1)))[:H, :W] * 255).astype(np.uint8),
}
tmp = tempfile.mkdtemp()


def norm(s):
    s = unicodedata.normalize("NFD", s.upper())
    return "".join(c for c in s if c.isalnum() or c == " ")


def compose(fond, texte, cap_pct, style):
    im = Image.fromarray(FONDS[fond].copy()); d = ImageDraw.Draw(im)
    # taille de police telle que la hauteur de capitale vaille cap_pct % de H (Inter : capitale ≈ 0,727 em)
    px = int(H * cap_pct / 100 / 0.727); f = ImageFont.truetype(FONT, px)
    mots, lignes, cur = texte.split(), [], ""
    for m in mots:                                   # retour à la ligne à 90 % de la largeur
        t = (cur + " " + m).strip()
        if d.textlength(t, font=f) > 0.9 * W and cur:
            lignes.append(cur); cur = m
        else:
            cur = t
    lignes.append(cur)
    hl = int(px * 1.1)
    if hl * len(lignes) > 0.9 * H or max(d.textlength(l, font=f) for l in lignes) > 0.98 * W:
        return None, len(lignes)
    y0 = int(H * 0.06)
    global BOITE
    BOITE = (0, max(0, y0 - 12), W, min(H, y0 + hl * len(lignes) + 12))   # bande du texte (recadrage avant OCR, leçon session 13)
    for k, l in enumerate(lignes):
        yy = y0 + k * hl
        if style == "bandeau":
            tw = d.textlength(l, font=f)
            d.rectangle([40 - 12, yy - 6, 40 + tw + 12, yy + hl], fill=(255, 214, 0))
            d.text((40, yy), l, font=f, fill=(10, 10, 10))
        elif style == "contour":
            d.text((40, yy), l, font=f, fill=(255, 255, 255), stroke_width=max(2, px // 14), stroke_fill=(0, 0, 0))
        else:
            d.text((40, yy), l, font=f, fill=(255, 255, 255))
    return im, len(lignes)


def ocr(im):
    p = os.path.join(tmp, "o.png"); im.save(p)
    r = subprocess.run(["tesseract", p, "-", "-l", "fra", "--psm", "6"], capture_output=True, text=True, env={**os.environ, "OMP_THREAD_LIMIT": "1"})
    return norm(" ".join(r.stdout.split()))


print("fond\tstyle\tmots\tcap_pct\tlignes\taffichage\tcap_px_affiche\tscore\tlu")
for fond in FONDS:
    for style in STYLES:
        for n, texte in TEXTES.items():
            for cap in TAILLES:
                im, nl = compose(fond, texte, cap, style)
                if im is None:
                    print(f"{fond}\t{style}\t{n}\t{cap}\t{nl}\t-\t-\tne tient pas\t"); continue
                if n == 4 and cap == 12:
                    im.save(os.path.join(OUT, f"mini_{fond}_{style}.png"))
                for (aw, ah) in AFFICHAGES:
                    petit = im.resize((aw, ah), Image.LANCZOS)
                    b = [int(round(v * aw / W)) for v in BOITE]; b[3] = max(b[1] + 2, b[3])
                    bande = petit.crop(b)
                    fx = max(1.0, 30 / (ah * cap / 100))   # v3 : capitale ramenée à ~30 px (tesseract lit mal les lettres géantes)
                    lu = ocr(bande.resize((int(bande.width * fx), int(bande.height * fx)), Image.LANCZOS))
                    attendus = norm(texte).split()
                    attendus = [m for m in attendus if len(m) > 1]          # « A » isolé : l'OCR le colle ou le perd, bruit
                    score = sum(1 for m in attendus if m in lu.split()) / len(attendus)
                    print(f"{fond}\t{style}\t{n}\t{cap}\t{nl}\t{aw}x{ah}\t{ah * cap / 100:.1f}\t{score:.2f}\t{lu[:60]}", flush=True)
