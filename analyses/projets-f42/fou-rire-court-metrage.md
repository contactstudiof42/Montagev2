# « Fou-Rire » — court métrage (2 min 21)

_Fiche ouverte le 2026-10-11 (phase 2, session 6, projet Studio F42 n°6). **État : complète** (vue en entier à 1 image / 2 s, sept images pleine définition, 47 plans, quatre plans longs vérifiés par `verif_plan.py`, courbe de loudness, QC du fichier, transcription Whisper lue). Source : `FOU RIRE COURT METRAGE.mov`, H.264 3840×1920 (2:1), 25 i/s, 2 min 21,4, AAC stéréo. Je ne nomme pas les comédiens. Pas de rushes._

**Lu avant l'analyse** : `A-LIRE.md`, `montage-regard` (grille), `montage-grammaire` (champ / contrechamp), `montage-rythme` (sommet, état intérieur), `montage-son-et-emotion` (silence, hors champ), `montage-couleur-et-intention`, bilan de la vague 1 des films. **Goût de Diego qui s'applique** (`GOUTS.md`, réponse 8) : « des visages sombres, mais avec un minimum de lumière sur l'info à voir » ; et réponse 7 : préférence pour le grain et le look film.

## Intention et contraintes probables
- **Intention** : la première scène d'un humoriste, vécue de l'intérieur. Dans la loge, une voix lui demande « Et si je ne ris pas ? » (le rire parle) ; sur scène, le public se tait et la voix devient celle du public : « sans nous, tu n'existes pas… c'est le public qui détient le pouvoir ». La peur du bide comme un dialogue avec ce qui décide de vous. [transcription]
- **Contraintes probables** [DÉDUIT] : un court de festival (carton final avec une sélection en laurier), deux décors (loge, salle), un comédien principal et un second rôle, une figuration dans le noir, une nuit de tournage.

## Forme [mesuré, VU SUR IMAGES]
- **47 plans, médiane 1,9 s, ASL 3,0 s** ; densité 16, 20 puis 10 coupes/min (la dernière minute contient le titre).
- **Quatre temps** : la loge (0:00-0:44 ; champ / contrechamp, plans de 6 à 9 s, vérifiés sans coupe) ; **le passage vers la scène sans un mot** (0:44-1:00 : couloir, public dans le noir, projecteur, micro) ; le début du spectacle (1:00-1:30 ; « Bonsoir à tous », puis 13 s jusqu'à « Vous allez bien ? ») ; **la voix du public et la panique** (1:30-2:08 : le comédien se tait, la voix parle, les plans tombent à 0,6 s entre 1:59 et 2:02, gros plans qui perdent le point) ; puis deux plans tenus, un creux de son, le titre « FOU-RIRE » (2:20).
- **Couleur** : la loge en vert et ampoules chaudes du miroir ; la salle en bleu-cyan (néon, projecteur blanc), public presque noir. **Un monde par lieu.**
- **Son** : -23,3 LUFS intégrés, **LRA 12,0 LU** (dynamique de cinéma), true peak -1,6 dBTP. La loge est presque muette entre les répliques (momentané de -50 à -68 LUFS) ; à partir de 0:48, un fond continu vers -25/-27 ; **crescendo jusqu'à -18 sous la voix du public (1:46-2:06)**, puis chute à -33 (2:12-2:16) avant le titre. [mesuré, pas écouté]

## Ce qui marche (avec la preuve)
1. **Le rythme suit l'état intérieur** (`montage-regard`, Schoonmaker) : posé dans la loge (plans de 6 à 9 s, il est sûr de lui : « Je sais ce que j'ai à faire »), puis haché quand il perd pied (0,6 s par plan, 1:59-2:02) et flou (le point se perd sur ses gros plans, 2:00). Ici la partie la plus rapide est le sommet, et c'est juste : le sommet est une panique, pas une délivrance (les films de la vague 1 accélèrent avant le sommet d'émotion ; ici l'émotion est la perte de contrôle). [VU SUR IMAGES]
2. **Le passage vers la scène est muet et dure 16 s** (0:44-1:00) : couloir, public, projecteur, micro seul dans le néon. Le spectateur entre dans la salle avec lui ; c'est un plan d'orientation qui fait aussi monter l'attente. [VU SUR IMAGES]
3. **Une couleur par monde** : vert et ampoules chaudes (la loge, l'intime), cyan et noir (la scène, l'exposition). La rupture de couleur à 0:48 dit le changement d'état sans un mot (« une matière par monde » des films). [VU SUR IMAGES]
4. **Le silence est le sujet** : 13 s entre « Bonsoir à tous » et « Vous allez bien ? » (1:00-1:13), le public muet, quelqu’un sur son téléphone (vers 1:54). Le bide est montré par l'absence de son, et la phrase sur « les réseaux sociaux » trouve son image dans ce téléphone allumé. [VU SUR IMAGES, transcription]
5. **L'après est tenu** : après la panique, deux plans tenus (2,7 et 5,7 s) et un creux de son à -33 LUFS avant le titre (2:12-2:16), comme les films de référence (le plus fort suivi du plus grand vide). [mesuré, VU SUR IMAGES]
6. **Le niveau est un niveau de festival** (-23,3 LUFS, true peak -1,6 dBTP) : le seul fichier du studio vu en session 6 qui passe le QC, pour sa destination probable.

## Ce qui pourrait être meilleur, et comment
### Montage et finition (corrigeable avec les mêmes rushes)
1. **Des plans du public sont noirs** : vers 0:52 et surtout **1:31,7-1:33,6** (1,8 s détectées comme du noir par `blackdetect`, on n'y voit qu'un reflet de boucle d'oreille). C'est contraire à la règle que Diego a lui-même dictée (`GOUTS.md` : « un minimum de lumière sur l'info à voir »). À l'étalonnage : remonter un contour (une joue, un regard) par une fenêtre, ou retirer le plan ; un plan noir de 1,8 s en pleine montée est un trou.
2. **La loge sonne vide** : entre les répliques, le son tombe à -50 / -68 LUFS momentané, alors que la première phrase est « Arrivée du public dans 5 minutes ». **Le public pourrait être là dès la loge**, en rumeur derrière la porte, qui monte doucement : le thème du film (le public détient le pouvoir) serait entendu avant d'être dit, et la loge ne sonnerait plus comme un silence numérique. Hors champ sonore (`montage-son-et-emotion`). [mesuré, pas écouté : à confirmer à l'écoute]
3. **La voix du public n'a pas de corps sonore distinct** de la voix de la loge (je ne peux pas l'entendre, mais la courbe ne montre aucun changement de texture à 1:30) : si c'est le même traitement, le spectateur peut ne pas comprendre que « nous » est la salle. Une autre spatialisation (plus large, réverbération de salle, plusieurs voix) ferait le passage de « je » (le rire) à « nous » (le public). [THÉORIQUE, à écouter]
4. **Une version web** : -23 LUFS est juste pour un festival ; sur YouTube ou Instagram, le film sera 9 LU plus bas que ce qui l'entoure. Garder le master festival et faire un master web à -16/-14 LUFS, true peak -1 dBTP, avec une compression douce pour ne pas tuer le crescendo.

### Tournage (à préparer autrement la prochaine fois)
1. **Prévoir la lumière du public** : un contre-jour ou une découpe de projecteur sur quelques visages de la salle (la règle « visages sombres, un minimum de lumière sur l'info »). Le noir total ne se rattrape pas à l'étalonnage sans bruit.
2. **Enregistrer des ambiances de salle** (rumeur, toux, chaises, silence plein) pendant le tournage : c'est la matière des points 2 et 3.

## Grille (`montage-regard`, 0 à 3)
| Critère | Note | Preuve |
|---|---|---|
| Intention | 3 | la peur du bide comme dialogue avec le rire, puis avec le public |
| Lisibilité | 2 | plans du public noirs (1:31,7, 1,8 s) |
| Liaison | 3 | passage muet vers la scène ; couleur qui bascule ; téléphone qui illustre la réplique |
| Rythme | 3 | posé → haché → tenu, au rythme de l'état intérieur |
| Composition | 3 | gros plans décentrés, néon et micro en amorce, profondeur de champ courte |
| Cohérence | 3 | deux mondes de couleur, une même grammaire |
| Couleur | 3 | vert-chaud / cyan-noir, tenus |
| Mouvement | 2 | perte de point de la panique juste ; peu d'autres mouvements |
| Originalité | 2 | le rire qui parle est une idée ; le bide sur scène est un sujet connu |
| Justesse | 2 | plans noirs ; loge sans ambiance |

**Verdict** : **le plus maîtrisé des projets vus** ; livrable pour un festival ; deux reprises valent le coup (les plans noirs, l'ambiance de loge).

## Confirme, contredit, complète
- **Confirme** sur un film du studio « le rythme suit l'état intérieur » (`montage-regard`), « une matière par monde » et « l'après est tenu » (bilan de la vague 1).
- **Nuance** « le climax n'est pas plus rapide » (vague 1) : quand le sommet est une **perte de contrôle**, il peut être la partie la plus rapide (comme le sommet d'information de Tiger) ; c'est le sommet de délivrance qui est lent.
- **Applique** la règle dictée par Diego (`GOUTS.md`, 8) comme critère de jugement : deux plans la manquent.

## Principes transférables (pour le studio)
1. **Le sommet de panique se hache, le sommet de délivrance se tient.**
2. **Faire entendre le sujet avant de le dire** : le public en rumeur dès la loge.
3. **Le passage d'un lieu à l'autre en silence**, comme un plan d'orientation qui fait monter l'attente.
4. **Deux masters** : festival (-23, dynamique) et web (-14/-16).

## Ce que Diego en a dit
Rien sur ce projet (titre seulement dans `NOTES-DIEGO.md`). Le critère de lumière vient de `GOUTS.md` (réponse 8).
