#!/usr/bin/env python3
"""Courbe d'événements par minute d'un découpage YouTube long, et contrôles de rétention.

Entrée : JSON {"duree": s, "evenements": [[t, "type"], ...]}
  types comptés comme événements : coupe, punch, sfx, caption, insert
  types de structure : promesse, relance, recompense, fin_ecran (début de l'écran de fin)
Sortie : rapport texte + PNG (barres par minute, relances en rouge).

Contrôles (règles de montage-youtube) :
  - promesse avant 30 s ;
  - aucun plateau de plus de MAX_PLATEAU s sans relance ni récompense ;
  - écran de fin de 5 à 20 s (et vidéo d'au moins 25 s) ;
  - option --decroissante : la densité par tranche de 3 min ne remonte pas de plus de 20 %
    et le 1er temps long (minute < 8 év./min) vient après la 1re récompense.

Usage : densite.py decoupage.json sortie.png [--decroissante] [--max-plateau 240]
"""
import json, sys
from PIL import Image, ImageDraw

COMPTES = {"coupe", "punch", "sfx", "caption", "insert"}


def analyse(d, decroissante=False, max_plateau=240):
    duree = d["duree"]
    ev = sorted(d["evenements"])
    nmin = int(-(-duree // 60))
    parmin = [0] * nmin
    for t, k in ev:
        if k in COMPTES and t < duree:
            parmin[int(t // 60)] += 1
    # dernière minute partielle : ramener à la minute
    reste = duree - 60 * (nmin - 1)
    if 0 < reste < 60:
        parmin[-1] = round(parmin[-1] * 60 / reste, 1)
    erreurs = []
    promesses = [t for t, k in ev if k == "promesse"]
    if not promesses or min(promesses) > 30:
        erreurs.append("promesse absente avant 30 s")
    reperes = [0] + [t for t, k in ev if k in ("relance", "recompense")]
    fin = [t for t, k in ev if k == "fin_ecran"]
    fin_film = fin[0] if fin else duree
    reperes.append(fin_film)
    reperes = sorted(reperes)
    for a, b in zip(reperes, reperes[1:]):
        if b - a > max_plateau:
            erreurs.append(f"plateau de {b - a:.0f} s sans relance ({a / 60:.1f} → {b / 60:.1f} min)")
    if fin:
        lf = duree - fin[0]
        if not 5 <= lf <= 20:
            erreurs.append(f"écran de fin de {lf:.0f} s (attendu 5-20 s)")
    if duree < 25 and fin:
        erreurs.append("vidéo < 25 s : pas d'écran de fin possible")
    if decroissante:
        tr = [sum(parmin[i:i + 3]) / len(parmin[i:i + 3]) for i in range(0, nmin, 3)]
        for i in range(1, len(tr)):
            if tr[i] > tr[i - 1] * 1.2:
                erreurs.append(f"densité remonte à la tranche {3 * i}-{3 * i + 3} min ({tr[i - 1]:.1f} → {tr[i]:.1f})")
        rec = [t for t, k in ev if k == "recompense"]
        lent = [i for i, v in enumerate(parmin) if v < 8]
        if lent and (not rec or 60 * lent[0] < min(rec)):
            erreurs.append(f"1er temps long (min {lent[0]}) avant la 1re récompense")
    return parmin, erreurs, [t for t, k in ev if k in ("relance", "recompense")]


def dessin(parmin, rel, duree, out):
    W, H, m = 900, 300, 40
    im = Image.new("RGB", (W, H), (250, 250, 248))
    dr = ImageDraw.Draw(im)
    vmax = max(max(parmin), 1)
    bw = (W - 2 * m) / len(parmin)
    for i, v in enumerate(parmin):
        h = (H - 2 * m) * v / vmax
        dr.rectangle([m + i * bw + 2, H - m - h, m + (i + 1) * bw - 2, H - m], fill=(70, 90, 120))
        dr.text((m + i * bw + 4, H - m + 4), str(i), fill=(60, 60, 60))
        dr.text((m + i * bw + 4, H - m - h - 12), f"{v:g}", fill=(30, 30, 30))
    for t in rel:
        x = m + (W - 2 * m) * t / (60 * len(parmin))
        dr.line([x, m, x, H - m], fill=(200, 40, 40), width=2)
    dr.text((m, 10), f"evenements par minute (coupes, punch-ins, SFX, captions, inserts) - rouge : relances et recompenses - {duree / 60:.1f} min (police par defaut sans accents)", fill=(0, 0, 0))
    im.save(out)


if __name__ == "__main__":
    a = sys.argv[1:]
    dec = "--decroissante" in a
    mp = int(a[a.index("--max-plateau") + 1]) if "--max-plateau" in a else 240
    d = json.load(open(a[0]))
    parmin, err, rel = analyse(d, dec, mp)
    print("év./min :", parmin)
    print("OK" if not err else "\n".join("ÉCHEC : " + e for e in err))
    dessin(parmin, rel, d["duree"], a[1])
    sys.exit(1 if err else 0)
