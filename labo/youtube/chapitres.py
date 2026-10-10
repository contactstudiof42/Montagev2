"""Valide une liste de chapitres YouTube (texte de description) et écrit un FFMETADATA pour le fichier.
python3 -I chapitres.py description.txt DUREE_S [--ffmeta out.txt]
Règles (aide YouTube 9884579, consultée le 2026-10-10) : premier horodatage à 00:00, au moins 3, ordre croissant,
10 s minimum par chapitre (le dernier : jusqu'à la fin de la vidéo). Formats acceptés : M:SS, MM:SS, H:MM:SS en début de ligne.
YouTube lit les chapitres dans la description, pas dans le fichier : le FFMETADATA sert aux autres lecteurs (VLC, QuickTime)."""
import re, sys
src, duree = sys.argv[1], float(sys.argv[2])
chap = []
for ligne in open(src, encoding="utf-8"):
    m = re.match(r"^\s*(?:(\d+):)?(\d{1,2}):(\d{2})\s*[-–—:]?\s*(.+)$", ligne)
    if m:
        h, mi, s, titre = m.groups()
        chap.append((int(h or 0) * 3600 + int(mi) * 60 + int(s), titre.strip()))
err = []
if not chap: err.append("aucun horodatage trouvé")
else:
    if chap[0][0] != 0: err.append(f"le premier chapitre commence à {chap[0][0]} s, pas à 00:00")
    if len(chap) < 3: err.append(f"{len(chap)} chapitres : il en faut au moins 3")
    fins = [c[0] for c in chap[1:]] + [duree]
    for (t, titre), fin in zip(chap, fins):
        if fin <= t: err.append(f"« {titre} » ({t} s) : ordre non croissant")
        elif fin - t < 10: err.append(f"« {titre} » ({t} s) dure {fin - t:.0f} s : moins de 10 s")
    if chap[-1][0] >= duree: err.append("un chapitre commence après la fin de la vidéo")
for t, titre in chap: print(f"{t // 60:02d}:{t % 60:02d}  {titre}")
print("OK" if not err else "REFUSÉ :\n- " + "\n- ".join(err))
if "--ffmeta" in sys.argv and not err:
    out = open(sys.argv[sys.argv.index("--ffmeta") + 1], "w", encoding="utf-8"); out.write(";FFMETADATA1\n")
    for (t, titre), fin in zip(chap, [c[0] for c in chap[1:]] + [duree]):
        out.write(f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={int(t * 1000)}\nEND={int(fin * 1000)}\ntitle={titre}\n")
sys.exit(1 if err else 0)
