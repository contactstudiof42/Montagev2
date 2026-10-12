# titres.py : fabrique les titres en ProRes 4444 avec alpha (UHD, 25 i/s), apparition 8 images (fondu + flou qui se résout), disparition 8 images.
import subprocess, os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
O = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/titres"; os.makedirs(O, exist_ok=True)
W, H, FPS = 3840, 2160, 25; CREME = (238, 230, 211)
DIDOT = "/System/Library/Fonts/Supplemental/Didot.ttc"
def police(taille, index=0): return ImageFont.truetype(DIDOT, taille, index=index)
def calque(lignes):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for txt, font, pos, track in lignes:
        x, y = pos
        if track:  # espacement des lettres
            for ch in txt: d.text((x, y), ch, font=font, fill=CREME + (255,)); x += d.textlength(ch, font=font) + track
        else: d.text((x, y), txt, font=font, fill=CREME + (255,))
    return im
def rendu(nom, im, dur_s):
    n = round(dur_s * FPS); out = f"{O}/{nom}.mov"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-alpha_bits", "16", out], stdin=subprocess.PIPE)
    for i in range(n):
        a = min(1, (i + 1) / 8, (n - i) / 8); flou = (1 - min(1, (i + 1) / 8)) * 14
        f = im.filter(ImageFilter.GaussianBlur(flou)) if flou > 0.5 else im
        arr = np.asarray(f).copy(); arr[..., 3] = (arr[..., 3] * a).astype(np.uint8); p.stdin.write(arr.tobytes())
    p.stdin.close(); p.wait(); im.save(f"{O}/{nom}.png"); print(out, n)
def mesure(txt, font): return ImageDraw.Draw(Image.new("RGB", (10, 10))).textbbox((0, 0), txt, font=font)
import sys, json
if __name__ == "__main__":
    T = json.load(open(sys.argv[1]))["textes"]
    for t in T:
        nom = {"titre": "titre", "personnage": "nael", "fin": "fin"}[t["style"]] if t["style"] != "personnage" else "personnage_" + t["texte"].lower().replace("ë", "e")
        if t["style"] == "titre":
            f1 = police(int(H * 0.085)); f2 = police(int(H * 0.026))
            bb = mesure(t["texte"], f1); x0, y0 = (W - bb[2]) // 2, int(H * 0.44)
            sous = "LE REMARIAGE  ·  4 JUIN 2026"; tr = int(H * 0.008); d0 = ImageDraw.Draw(Image.new("RGB", (10, 10))); ls = sum(d0.textlength(c, font=f2) + tr for c in sous) - tr
            im = calque([(t["texte"], f1, (x0, y0), 0), (sous, f2, ((W - int(ls)) // 2, y0 + bb[3] + int(H * 0.035)), tr)])
        elif t["style"] == "personnage":
            f1 = police(int(H * 0.055)); im = calque([(t["texte"], f1, (int(W * 0.06), int(H * 0.80)), 0)])
        else:
            f1 = police(int(H * 0.06)); bb = mesure(t["texte"], f1); im = calque([(t["texte"], f1, ((W - bb[2]) // 2, (H - bb[3]) // 2), 0)])
        rendu(nom, im, t["dur"])
