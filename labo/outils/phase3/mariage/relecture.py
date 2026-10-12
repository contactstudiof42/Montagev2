"""Relire ce que le spectateur entend : re-transcription (WhisperX, local) du son d'un rendu, phrase par phrase, avec le bloc.
Usage (venv .venv-whisperx) : relecture.py RENDU.mp4 montage.json SORTIE.txt
Signale : segment qui commence sans majuscule ou finit sans ponctuation forte (phrase coupée probable), mot de moins de 60 ms
au bord d'un segment (mot coupé probable). Le jugement reste une lecture : le fichier texte se lit en entier, comme un spectateur.
"""
import sys, json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import aligne
rendu, mj, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
J = json.load(open(mj)); blocs = sorted(J.get("blocs", []))
def bloc(t): return ([b for s, b in blocs if s <= t] or ["?"])[-1]
r = aligne.aligne(rendu)
L = []; n_alerte = 0
for s in r["segments"]:
    al = []
    if s["texte"][:1].islower(): al.append("commence en minuscule")
    if not s["texte"].rstrip(" »\"").endswith((".", "!", "?", "…")): al.append("finit sans ponctuation")
    if s["mots"] and (s["mots"][0]["e"] - s["mots"][0]["s"] < 0.06 or s["mots"][-1]["e"] - s["mots"][-1]["s"] < 0.06): al.append("mot très court au bord")
    n_alerte += bool(al)
    L.append(f"{bloc(s['s'])}  {int(s['s'] // 60)}:{s['s'] % 60:05.2f}-{int(s['e'] // 60)}:{s['e'] % 60:05.2f}  {s['texte']}" + (f"   <<< {', '.join(al)}" if al else ""))
open(sortie, "w").write("\n".join(L) + f"\n\n{len(L)} segments, {n_alerte} signalés\n")
print("\n".join(L)); print(len(L), "segments,", n_alerte, "signalés")
