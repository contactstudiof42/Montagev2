"""Pièce 05 « Trois étalonnages » — étalonnage scripté en « arbre de nodes » (numpy).
Lancer : python3 grade.py <version> <dossier_sources> <dossier_sortie>
Chaque direction est une liste de nodes appliqués en série, comme un arbre Resolve
(primaires → secondaires qualifiées → look). Les opérations imitent les outils Resolve
(Lift/Gamma/Gain, Contrast/Pivot, Sat, qualifieur HSL), sans prétendre les reproduire au bit près.
Sortie : images étalonnées, planche (lignes = directions, colonnes = instants), mesures JSON.
"""
import json, sys, os, colorsys
import numpy as np
from PIL import Image, ImageDraw

LUMA = np.array([0.2126, 0.7152, 0.0722])


def luma(x):
    return x @ LUMA


def hsv(x):
    mx, mn = x.max(-1), x.min(-1); d = mx - mn + 1e-9
    r, g, b = x[..., 0], x[..., 1], x[..., 2]
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    return h, (mx - mn) / (mx + 1e-9), mx


# --- nodes -------------------------------------------------------------------
def primaires(x, lift=(0, 0, 0), gamma=(1, 1, 1), gain=(1, 1, 1), **_):
    x = np.array(gain) * (x + np.array(lift) * (1 - x))
    return np.clip(x, 0, 1) ** (1 / np.array(gamma))


def contraste(x, c=1.0, pivot=0.435, **_):
    return np.clip((x - pivot) * c + pivot, 0, 1)


def saturation(x, s=1.0, **_):
    y = luma(x)[..., None]
    return np.clip(y + (x - y) * s, 0, 1)


def split(x, ombres=(0, 0, 0), hautes=(0, 0, 0), **_):
    """Teinte des ombres / des hautes lumières, pondérée par la luminance (split toning)."""
    y = luma(x)[..., None]
    return np.clip(x + np.array(ombres) * (1 - y) ** 2 + np.array(hautes) * y ** 2, 0, 1)


def haute_compression(x, seuil=0.7, plafond=0.88, **_):
    """Hautes lumières compressées (genou doux) : le laiteux du haut."""
    t = np.clip((x - seuil) / (1 - seuil), 0, 1)
    return np.where(x > seuil, seuil + (plafond - seuil) * (1 - (1 - t) ** 2), x)


def masque_qualif(x, h0=0, h1=40, s_min=0.2, v_min=0.04, doux=8):
    h, s, v = hsv(x)
    hm = np.clip(np.minimum(h - h0 + doux, h1 + doux - h) / doux, 0, 1)
    return hm * np.clip((s - s_min) / 0.1 + 0.5, 0, 1) * (v > v_min)


def secondaire(x, h0=0, h1=40, s_min=0.2, v_min=0.04, doux=8, sat_in=1.0, gain_in=(1, 1, 1),
               sat_out=1.0, cle=None, source=None, **_):
    """Qualifieur HSL : à l'intérieur on pousse, à l'extérieur on retire (sat_out).
    cle="source" : la clé ET la correction partent de l'image source (node parallèle Resolve
    branché sur l'entrée), pour ne pas qualifier une matière déjà écrasée par les primaires."""
    base = source if cle == "source" else x
    m = masque_qualif(base, h0, h1, s_min, v_min, doux)[..., None]
    dedans = np.clip(saturation(base, sat_in) * np.array(gain_in), 0, 1)
    dehors = saturation(x, sat_out)
    return dedans * m + dehors * (1 - m)


NODES = dict(primaires=primaires, contraste=contraste, saturation=saturation, split=split,
             haute_compression=haute_compression, secondaire=secondaire)


# --- mesures -----------------------------------------------------------------
def mesures(x, chaise_box):
    y = luma(x) * 255
    h, s, v = hsv(x)
    chaud = (h < 50) & (s > 0.25) & (v > 0.08)
    H, W = y.shape
    x0, y0, x1, y1 = [int(a) for a in (chaise_box[0] * W, chaise_box[1] * H, chaise_box[2] * W, chaise_box[3] * H)]
    hors = np.ones_like(chaud); hors[y0:y1, x0:x1] = False
    ciel, sable = x[: H // 5], x[int(H * 0.85):]
    def biais(z):  # (R-B) moyen en 1/255 : >0 chaud, <0 froid
        return round(float((z[..., 0] - z[..., 2]).mean() * 255), 1)
    return dict(luma_mediane=round(float(np.median(y)), 1), luma_p1=round(float(np.percentile(y, 1)), 1),
                luma_p99=round(float(np.percentile(y, 99)), 1),
                chaud_pct=round(float(chaud.mean() * 100), 2),
                chaud_hors_chaise_pct=round(float((chaud & hors).mean() * 100), 2),
                biais_ciel=biais(ciel), biais_sable=biais(sable),
                sat_moy=round(float(s.mean()), 3))


def main():
    version, src, out = sys.argv[1:4]
    cfg = json.load(open(os.path.join(os.path.dirname(__file__), f"{version}.json")))
    os.makedirs(out, exist_ok=True)
    frames = cfg["frames"]; R = {}
    rows = []
    for nom, arbre in [("SOURCE", [])] + list(cfg["directions"].items()):
        tiles = []
        for f in frames:
            x = np.asarray(Image.open(os.path.join(src, f"{f:04d}.png")).convert("RGB"), dtype=np.float64) / 255
            x0 = x
            for node in arbre:
                x = NODES[node["op"]](x, source=x0, **node)
            img = Image.fromarray((np.clip(x, 0, 1) * 255 + 0.5).astype(np.uint8))
            img.save(os.path.join(out, f"{version}-{nom}-{f:04d}.png"))
            R[f"{nom}/{f}"] = mesures(x, cfg["chaise_box"][str(f)])
            t = img.resize((320, 180)); ImageDraw.Draw(t).text((6, 4), f"{nom} f{f}", fill=(255, 255, 255))
            tiles.append(t)
        rows.append(tiles)
    planche = Image.new("RGB", (320 * len(frames), 180 * len(rows)))
    for r, tiles in enumerate(rows):
        for c, t in enumerate(tiles):
            planche.paste(t, (320 * c, 180 * r))
    planche.save(os.path.join(os.path.dirname(__file__), f"{version}-planche.png"), optimize=True)
    json.dump(R, open(os.path.join(os.path.dirname(__file__), f"{version}-mesures.json"), "w"), indent=1)
    for k, m in R.items():
        print(k, m)


if __name__ == "__main__":
    main()
