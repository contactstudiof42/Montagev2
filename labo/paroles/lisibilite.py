"""Labo paroles incrustées : lisibilité au téléphone. python3 -I lisibilite.py FOND1.png FOND2.png ... > resultats.tsv
Pour chaque fond (agrandi et recadré en 1080×1920), chaque taille de police (% de la hauteur) et chaque style :
drawtext → H.264 à 2,5 Mb/s (ordre de grandeur d'une ré-encode plateforme en 9:16, hypothèse) → réduction à 360 px de large
(vignette « téléphone tenu à bout de bras », convention de l'atelier) → recadrage sur la bande du texte (sinon l'OCR lit la texture comme des lettres, session 13) → OCR tesseract (fra) → part des mots du vers retrouvés (rappel ; le ratio difflib global était noyé par les « lettres » lues dans la texture).
L'OCR est un proxy de lisibilité, pas un œil : il sert à classer les cas, pas à fixer un seuil absolu."""
import sys, subprocess, difflib, os, tempfile
VERS = ["Les vitrines me rendent", "un type que je connais pas"]
FONT = {"medium": "/usr/share/fonts/opentype/inter/Inter-Medium.otf", "thin": "/usr/share/fonts/opentype/inter/Inter-Thin.otf"}
STYLES = {"nu": "", "ombre": ":shadowcolor=black@0.7:shadowx=3:shadowy=3", "boite": ":box=1:boxcolor=black@0.55:boxborderw=14", "boite85": ":box=1:boxcolor=black@0.85:boxborderw=14"}
TAILLES = [1.2, 1.6, 2.0, 2.6, 3.5]          # % de la hauteur 1920
tmp = tempfile.mkdtemp()
def ocr(png):
    r = subprocess.run(["tesseract", png, "-", "-l", "fra", "--psm", "6"], capture_output=True, text=True); return " ".join(r.stdout.split())
print("fond\tpolice\tstyle\ttaille_pct\ttaille_px_1920\ttaille_px_360\tscore\tlu")
for fond in sys.argv[1:]:
    for police in ("medium", "thin"):
        for style in STYLES:
            if police == "thin" and style != "nu": continue
            for t in TAILLES:
                px = round(1920 * t / 100); y0 = int(1920 * 0.62)    # au-dessus de la zone d'interface basse (~ 20 % du bas)
                dt = ",".join(f"drawtext=fontfile={FONT[police]}:text='{v}':fontsize={px}:fontcolor=white:x=(w-tw)/2:y={y0 + k * int(px * 1.35)}{STYLES[style]}" for k, v in enumerate(VERS))
                mp4, png = f"{tmp}/a.mp4", f"{tmp}/a.png"
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", fond, "-t", "1", "-r", "25", "-vf",
                                f"scale=-2:1920,crop=1080:1920,{dt}", "-c:v", "libx264", "-b:v", "2500k", "-pix_fmt", "yuv420p", mp4], check=True)
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "0.5", "-i", mp4, "-vf", "scale=360:-2:flags=area", "-frames:v", "1", png], check=True)
                lu = ocr(png); cible = " ".join(VERS).lower().split(); mots = lu.lower().split(); sc = sum(m in mots for m in cible) / len(cible)   # rappel des mots (l'OCR lit aussi la texture : un ratio global serait noyé)
                print(f"{os.path.basename(fond)}\t{police}\t{style}\t{t}\t{px}\t{px * 360 / 1080:.1f}\t{sc:.2f}\t{lu[:60]}", flush=True)
