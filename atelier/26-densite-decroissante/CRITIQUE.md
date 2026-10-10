# Pièce 26 — critique (session 22)

Rendus (non commités) : `atelier/rendus/26/v1..v4.mp4`, `python3 piece.py vN atelier/rendus/26` (~80 s chacun). Mesures : `python3 mesure.py atelier/rendus/26 atelier/26-densite-decroissante v1 v2 v3 v4` → `mesures.png`, `mesures.json`, `vN-planche.png` (1 image / 5 s). Maquette échantillonnée : 6 extraits de 25 s + le temps long de 40 s, cartons « ≈ heure du film » (3:14 au total).

| | v1 (examen) | v2 (rafale 3 s) | v3 (v2 + mouvement interne) | v4 (relance = changement de régime) |
|---|---|---|---|---|
| év. dans les 3 s avant les relances 1-3 | 1 / 1 / 0 | 2 / 2 / 2 | 2 / 2 / 2 | 2 / 2 / 2 |
| relance 4 (la triche, 12:50) | 0 év., rien ne la marque | idem | idem | caméra cachée 6 s (IR + timecode), son appauvri, un clac |
| LUFS max avant relance 3 | -20,7 | -14,6 | -14,6 | -14,9 |
| YDIF moyen du temps long (40 s) | 0,03 | 0,03 | 0,34 | 0,34 |

## Ce que les versions m'ont appris
1. **Une rafale ne fait pas un pic** (v1 → v2). Densifier 3 s avant la relance (×2,2) n'ajoute qu'**un événement** à 14-28 év./min : invisible au compte comme à la planche. Ce qui change vraiment, c'est le **son** : la musique qui part **sur** un drop (v2) au lieu d'être coupée net (v1, chute de loudness d'un coup, la courbe orange plonge pile sur la ligne rouge : c'est l'essoufflement que le labo prédisait). Correction de ma règle de la session 21 : la relance = pic veut dire **un coup qualitatif** (le dernier bruitage, le drop, le plus fort de la séquence), pas « plus d'événements ».
2. **Quand il n'y a plus d'outil à retirer, la relance n'a plus rien pour la porter** (relance 4, v1-v3 : zéro événement, la triche passe comme un plan de plus). La découverte : dans une densité décroissante, les relances tardives doivent être portées par **un changement de régime d'image ou de son** (la caméra cachée : autre grain, autre couleur, timecode, son lointain), qui est le seul « nouvel outil » du dernier tiers. Sur la planche v4, c'est la seule image qu'on remarque dans la rangée 3. C'est l'emprunt à la direction C de l'examen qui sauve la direction B : je ne l'avais pas vu comme une **fonction** de relance.
3. **Le mouvement interne se dose en dixièmes** (v3). La flamme + les souffles + la dérive rendent au temps long une vie (YDIF 0,03 → 0,34 : ce n'est plus une image arrêtée). Mais 0,34, c'est seulement **3 fois** moins que l'ouverture en pleine retention editing : ma flamme (15 % de variation sur toute la pièce) bouge autant qu'un montage. Un vrai feu de bougie est plus discret ; une lumière globale qui palpite se lit comme un événement (et à 7 Hz, il faudrait la passer à `flash_check.py`). Objectif écrit dans l'intention (≥ 10× plus calme que l'ouverture, mais pas zéro) : **raté**, à refaire avec une amplitude de 3-5 % et le souffle seul.
4. **Le cadre doit s'élargir avec le noir** (planche v4, rangées 4-5). Après l'extinction, mes coupes allaient encore vers les plans serrés : un serré dans le noir ne montre rien (un rond sombre). Quand la lumière meurt, le serré meurt d'abord ; le montage doit passer au large ou suivre la source (la bougie). Règle de découpage pour le dernier tiers : **on ne coupe que vers ce que la lumière montre**.
5. **Mesure** : YDIF est gonflé par le grain (relance 4 de v4 : 5,06, du bruit, pas du mouvement) et par les coupes vers des plans très différents ; il compte l'activité, pas l'attention. Les extraits tardifs (12:50, 16:50) ont un YDIF moyen plus haut que l'ouverture alors qu'ils ont 3 fois moins d'événements : **chaque coupe qui reste est un choc plus gros** quand les ponctuations ont disparu. À retenir : retirer les outils sans allonger les plans ne calme pas l'image.

## Grille
- Intention servie ? Oui pour la question posée (les relances), en partie pour le temps long (trop d'agitation en v3).
- Lisibilité : les serrés dans le noir sont illisibles (faute de découpage, pas de rendu).
- Rythme : la descente se lit sur la planche (chaud plein → froid vide → bougie) ; la relance 4 n'existait pas avant v4.
- Cliché : la caméra cachée IR est un code de télé-réalité ; ici elle a une fonction (la seule chose nouvelle du dernier tiers), je la garde, une fois.
- En fait-on trop ? La flamme, oui.

**Référence actuelle : v4** (avec l'amplitude de flamme à réduire). Suites : BACKLOG Y25.
