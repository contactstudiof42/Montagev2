"""Noir protégé (BACKLOG 65) : une image 16 bits de la pièce 17 (mur sombre en dégradé doux),
encodée 8 bits / 10 bits / grain, puis ré-encodée 8 bits comme le ferait une plateforme.
python3 -I mesure.py <image16.png> <dossier_travail> <sortie_planche.png>
Mesure, dans les zones sombres et lisses (Y de référence 16,3-30 en plage limitée, noir pur exclu, gradient faible) :
- écart lissé : RMS de (encodé - référence) après flou σ=3 px (l'œil intègre le grain), en niveaux 8 bits ;
- part des pixels de pénombre où l'image lissée s'écarte de plus d'un demi-niveau (marche visible)."""
import sys, subprocess, json, os
import numpy as np
from scipy.ndimage import gaussian_filter
src, wd, planche = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(wd, exist_ok=True)
W, H, N = 960, 540, 24

def run(*a): subprocess.run(["ffmpeg", "-v", "error", "-y", *a], check=True)

def lire_y(path, n=12):
    """Y de l'image n, en niveaux 8 bits flottants (0-255), lu en 16 bits."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"select=eq(n\\,{n})", "-frames:v", "1",
                          "-pix_fmt", "gray16le", "-f", "rawvideo", "-"], check=True, capture_output=True).stdout
    return np.frombuffer(raw, np.uint16).reshape(H, W).astype(np.float64) / 257.0

# référence : la même conversion en Y, sans quantification 8 bits
# PANO=1 : panoramique lent simulé (2 px/image) — une image fixe est le cas le plus favorable à l'encodeur
pano = ["-vf", f"crop=896:504:x=n*2:y=n,scale={W}:{H}:flags=bicubic"] if os.environ.get("PANO") else []
run("-loop", "1", "-i", src, "-frames:v", str(N), "-r", "24", *pano, "-pix_fmt", "yuv444p16le", "-c:v", "ffv1", f"{wd}/ref.mkv")
ref = lire_y(f"{wd}/ref.mkv")
# grain : bruit gaussien σ = 2 niveaux 8 bits, fin, par image (dans le domaine 16 bits)
# ffmpeg 'noise' travaille en 8 bits : on fabrique le grain en numpy pour garder le contrôle de σ
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{wd}/ref.mkv", "-pix_fmt", "yuv444p16le", "-f", "rawvideo", "-"],
                     check=True, capture_output=True).stdout
v = np.frombuffer(raw, np.uint16).reshape(N, 3, H, W).astype(np.float64)
rng = np.random.default_rng(17)
v0 = v.copy()
bruit = rng.normal(0, 2 * 257, size=(N, H, W))   # luma seulement, σ = 2 niveaux 8 bits
def ecrire(arr, nom):
    arr = np.clip(arr, 0, 65535).astype(np.uint16)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "yuv444p16le", "-s", f"{W}x{H}", "-r", "24",
                    "-i", "-", "-c:v", "ffv1", f"{wd}/{nom}.mkv"], input=arr.tobytes(), check=True)
v[:, 0] += bruit; ecrire(v, "grain")
# M : grain dosé par la luminance (nul dans le noir pur, plein 7 niveaux au-dessus, comme un grain qui ne vit que dans la pénombre)
y8 = v0[:, 0] / 257.0
poids = np.clip((y8 - 17.0) / 7.0, 0, 1)   # Y en plage limitée : noir = 16
vm = v0.copy(); vm[:, 0] += bruit * poids; ecrire(vm, "grainM")

def h264(inp, out, bits, crf):
    pf = "yuv420p10le" if bits == 10 else "yuv420p"
    run("-i", inp, "-c:v", "libx264", "-preset", "medium", "-crf", str(crf), "-pix_fmt", pf, out)

def plateforme_debit(inp, out, kbps):
    """ré-encodage à débit plafonné, plus proche d'une plateforme qu'un CRF (une image fixe coûte presque rien en CRF)"""
    run("-i", inp, "-c:v", "libx264", "-preset", "medium", "-b:v", f"{kbps}k", "-maxrate", f"{kbps}k",
        "-bufsize", f"{2 * kbps}k", "-pix_fmt", "yuv420p", out)

variantes = {}
h264(f"{wd}/ref.mkv", f"{wd}/A8.mp4", 8, 18);  variantes["A 8 bits CRF 18 (master 8 bits)"] = f"{wd}/A8.mp4"
h264(f"{wd}/ref.mkv", f"{wd}/B10.mp4", 10, 18); variantes["B 10 bits CRF 18 (master 10 bits)"] = f"{wd}/B10.mp4"
h264(f"{wd}/A8.mp4", f"{wd}/A8p.mp4", 8, 23);  variantes["A ré-encodé plateforme (8 bits CRF 23)"] = f"{wd}/A8p.mp4"
h264(f"{wd}/B10.mp4", f"{wd}/B10p.mp4", 8, 23); variantes["B ré-encodé plateforme"] = f"{wd}/B10p.mp4"
h264(f"{wd}/grain.mkv", f"{wd}/G10.mp4", 10, 18); variantes["G grain σ2 + 10 bits"] = f"{wd}/G10.mp4"
h264(f"{wd}/G10.mp4", f"{wd}/G10p.mp4", 8, 23); variantes["G ré-encodé plateforme"] = f"{wd}/G10p.mp4"
variantes["G source sans perte (grain seul)"] = f"{wd}/grain.mkv"
h264(f"{wd}/grainM.mkv", f"{wd}/M10.mp4", 10, 18); variantes["M grain dosé + 10 bits"] = f"{wd}/M10.mp4"
h264(f"{wd}/M10.mp4", f"{wd}/M10p.mp4", 8, 23); variantes["M ré-encodé plateforme"] = f"{wd}/M10p.mp4"
KB = int(os.environ.get("KBPS", "2000"))   # ~ débit d'une plateforme pour du 540p
for k, f in (("A", "A8"), ("B", "B10"), ("G", "G10"), ("M", "M10")):
    plateforme_debit(f"{wd}/{f}.mp4", f"{wd}/{f}d.mp4", KB); variantes[f"{k} plateforme {KB} kb/s"] = f"{wd}/{f}d.mp4"

# zone de mesure : sombre et lisse dans la référence
rb = gaussian_filter(ref, 3)
gy, gx = np.gradient(rb)
masque = (rb > 16.3) & (rb < 30) & (np.hypot(gx, gy) < 1.0)   # plage limitée : 16 = noir ; noir pur exclu
# fenêtre 320×280 qui contient le plus de pénombre lisse (choisie automatiquement : la session 12 visait d'abord le mur éclairé)
from scipy.ndimage import uniform_filter
dens = uniform_filter(masque.astype(float), (280, 320))
cy, cx = np.unravel_index(np.argmax(dens[140:H - 140, 160:W - 160]), dens[140:H - 140, 160:W - 160].shape)
y0, x0 = cy, cx   # coin haut-gauche (décalage des bornes compensé)
def indice(y):
    """part des pixels de pénombre où l'image lissée s'écarte de plus d'un demi-niveau : une marche visible"""
    return float((np.abs(gaussian_filter(y, 3) - rb)[masque] > 0.5).mean())
res = {"zone_px": int(masque.sum()), "fenetre": [int(x0), int(y0)]}
crops = [("référence 16 bits", ref)]
for nom, f in variantes.items():
    y = lire_y(f)
    e = gaussian_filter(y, 3) - rb
    res[nom] = {"ecart_lisse_rms": round(float(np.sqrt((e[masque] ** 2).mean())), 3),
                "part_marche_visible": round(indice(y), 4), "ko": os.path.getsize(f) // 1024}
    crops.append((nom, y))
print(json.dumps(res, ensure_ascii=False, indent=1))
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(planche)), "resultats" + ("_pano" if os.environ.get("PANO") else "") + ".json"), "w"), ensure_ascii=False, indent=1)

# planche : la pénombre, contraste ×8,5 (Y 16-28,75 → 0-255, ×20), pour voir les marches
from PIL import Image, ImageDraw
tiles = []
for nom, y in crops:
    c = np.clip((y[y0:y0 + 280, x0:x0 + 320] - 16) * 20, 0, 255).astype(np.uint8)
    im = Image.fromarray(c).convert("RGB"); ImageDraw.Draw(im).text((4, 4), nom, fill=(255, 255, 0)); tiles.append(im)
cols = 4 if len(tiles) <= 8 else 5; rows = (len(tiles) + cols - 1) // cols
pl = Image.new("RGB", (320 * cols, 280 * rows))
for i, t in enumerate(tiles): pl.paste(t, ((i % cols) * 320, (i // cols) * 280))
pl.save(planche, optimize=True)
