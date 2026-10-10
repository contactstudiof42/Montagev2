"""Détecteur de micro-sauts aux coupes (BACKLOG Y17).
Usage : python3 micro_sauts.py AVANT.png APRES.png   ou   python3 micro_sauts.py --video V.mp4 --coupes 3.2,7.84,...
Pour chaque coupe : image juste avant / juste après, recherche de l'échelle (1/1,5 à 1,5) puis translation par corrélation de phase.
Sortie : échelle (punch-in), décalage en % de largeur, pic de corrélation (confiance ; < 0,08 = plans différents, pas un jump cut)."""
import sys, subprocess, numpy as np
from PIL import Image
L = 320                                                   # largeur d'analyse
def gris(img):
    im = img.convert('L'); h = round(im.height * L / im.width); return np.asarray(im.resize((L, h), Image.BILINEAR), np.float64)
def zoom(a, s):                                           # agrandissement centré d'un facteur s (punch-in simulé sur l'image « avant »)
    h, w = a.shape; im = Image.fromarray(a.astype(np.float32), 'F'); cw, ch = w / s, h / s
    return np.asarray(im.resize((w, h), Image.BILINEAR, box=((w - cw) / 2, (h - ch) / 2, (w + cw) / 2, (h + ch) / 2)), np.float64)
def phase(a, b):
    win = np.outer(np.hanning(a.shape[0]), np.hanning(a.shape[1]))
    A, B = np.fft.fft2((a - a.mean()) * win), np.fft.fft2((b - b.mean()) * win)
    R = A * np.conj(B); R /= np.abs(R) + 1e-9; r = np.real(np.fft.ifft2(R)); k = np.unravel_index(np.argmax(r), r.shape)
    dy, dx = [(k[i] if k[i] <= r.shape[i] // 2 else k[i] - r.shape[i]) for i in (0, 1)]
    return r.max(), dx, dy
def mesurer(av, ap):
    a, b = gris(av), gris(ap); best = None
    for s in np.arange(1.0, 1.501, 0.01):                 # punch-in (après plus serré) puis punch-out (avant plus serré)
        pk, dx, dy = phase(zoom(a, s), b)
        if best is None or pk > best[0]: best = (pk, s, dx, dy)
        pk, dx, dy = phase(a, zoom(b, s))
        if pk > best[0]: best = (pk, 1 / s, -dx * s, -dy * s)
    pk, s, dx, dy = best
    return dict(echelle=round(float(s), 2), dx_pct=round(-100 * dx / L, 2), dy_pct=round(-100 * dy / L, 2), pic=round(float(pk), 3))
def image_a(video, t):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', f'{t:.3f}', '-i', video, '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
    import io; return Image.open(io.BytesIO(raw))
if __name__ == '__main__':
    if sys.argv[1] == '--video':
        v, cs = sys.argv[2], [float(x) for x in sys.argv[4].split(',')]
        for c in cs: print(c, mesurer(image_a(v, c - 0.04), image_a(v, c + 0.001)))
    else: print(mesurer(Image.open(sys.argv[1]), Image.open(sys.argv[2])))
