# titres_v4.py montage_V4.json : textes de la V4 en ProRes 4444 avec alpha (UHD, 25 i/s), une famille (Source Serif 4, graisse Light,
# taille optique « display »), crème #EEE6D3 ; apparition 8 images (fondu + flou qui se résout), disparition 8 images.
# Styles : titre (deux lignes, bas droite, sur l'eau du plan du lac), nom (arrêt sur image, bas gauche), replique (bas centre), fin (centre).
import subprocess, os, sys, json, glob, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
O = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/titres_v4"; os.makedirs(O, exist_ok=True)
W, H, FPS = 3840, 2160, 25; CREME = (238, 230, 211)
SS4 = [x for x in glob.glob(os.path.expanduser("~/Library/Fonts/SourceSerif4-VariableFont*")) + glob.glob("/Library/Fonts/SourceSerif4-VariableFont*") if "Italic" not in x][0]
def police(taille, graisse=300, opsz=60):
    f = ImageFont.truetype(SS4, taille); f.set_variation_by_axes([opsz, graisse]); return f
def trace(d, xy, txt, f, track=0):
    x, y = xy
    for ch in txt: d.text((x, y), ch, font=f, fill=CREME + (255,)); x += d.textlength(ch, font=f) + track
def largeur(d, txt, f, track=0): return sum(d.textlength(c, font=f) + track for c in txt) - track
def rendu(nom, im, dur_s):
    n = max(2, round(dur_s * FPS)); out = f"{O}/{nom}.mov"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-alpha_bits", "16", out], stdin=subprocess.PIPE)
    for i in range(n):
        a = min(1, (i + 1) / 8, (n - i) / 8); flou = (1 - min(1, (i + 1) / 8)) * 12
        f = im.filter(ImageFilter.GaussianBlur(flou)) if flou > 0.5 else im
        arr = np.asarray(f).copy(); arr[..., 3] = (arr[..., 3] * a).astype(np.uint8); p.stdin.write(arr.tobytes())
    p.stdin.close(); p.wait(); im.save(f"{O}/{nom}.png"); return out
def fabrique(t):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if t["style"] == "titre":
        f = police(int(H * 0.16), 300); l1, l2 = t["texte"].split(" & ")[0] + " &", t["texte"].split(" & ")[1] + "."
        tr = -int(H * 0.002); x = int(W * 0.94) - max(largeur(d, l1, f, tr), largeur(d, l2, f, tr)); y = int(H * 0.60)
        y = int(H * 0.52); trace(d, (x, y), l1, f, tr); trace(d, (x, y + int(H * 0.17)), l2, f, tr)
    elif t["style"] == "nom":
        f = police(int(H * 0.15), 300); trace(d, (int(W * 0.06), int(H * 0.70)), t["texte"], f, int(H * 0.006))
    elif t["style"] == "replique":
        f = police(int(H * 0.095), 300); lw = largeur(d, t["texte"], f); trace(d, ((W - lw) / 2, int(H * 0.80)), t["texte"], f)
    else:
        f = police(int(H * 0.10), 300); trace(d, (int(W * 0.06), int(H * 0.12)), t["texte"], f)     # en haut à gauche : jamais sur les visages
    a_ = np.asarray(im)[..., 3].astype(float)
    ombre = np.asarray(Image.fromarray(a_.astype(np.uint8)).filter(ImageFilter.GaussianBlur(H * 0.012)), float) * 0.45
    fond = np.zeros((H, W, 4), np.uint8); fond[..., 3] = ombre.astype(np.uint8)
    im = Image.alpha_composite(Image.fromarray(fond), im)                 # ombre portée douce : le crème se lit sur un fond clair
    import hashlib; nom = f"{t['style']}_{hashlib.md5(np.asarray(im).tobytes() + str(t['dur']).encode()).hexdigest()[:8]}"   # nom = contenu : Resolve garde en mémoire un fichier remplacé sous le même nom
    return rendu(nom, im, t["dur"])
if __name__ == "__main__":
    J = json.load(open(sys.argv[1])); res = {}
    for t in J["textes"]:
        res[t["texte"]] = fabrique(t); print(t["style"], t["texte"], res[t["texte"]])
    json.dump(res, open(f"{O}/fichiers.json", "w"), ensure_ascii=False, indent=1)
