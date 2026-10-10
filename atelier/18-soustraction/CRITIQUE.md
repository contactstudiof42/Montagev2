# Pièce 18 « Soustraction » — critique (session 12)
Rendus : `scene.py` (Blender 4.2.3, Cycles 48 échantillons, 640×360, ~25 s par état, plan fixe = une image par état). Planches : `planche.py` (vignettes à 320 px = taille téléphone ; luminance moyenne, variation par état, taches lumineuses comptables > 200/255).
État de départ commun `e7` : 7 lampadaires LED blanc-bleu à droite, 4 fenêtres chaudes à gauche, le personnage sur le trottoir gauche avec une source ambre basse.

## v1 — `v1-planche.png` : deux ordres d'extinction
**Ligne 1, lointains d'abord** (`lf` : le plus facile en post, peu de lumière portée) : luminance 38 → 37 → 33 → 15 (**−4 %, −11 %**, −53 %).
- 7 → 5 est **invisible** : deux points de 3 px au fond qui disparaissent, la rue reste éclairée pareil. 5 → 3 à peine. Toute la lecture arrive à la fin.
- `lf1` n'est pas « il ne reste qu'une lumière » : le lampadaire restant est le plus proche, il éclaire encore toute la moitié droite. **Le noir n'est pas un noir** (critère 3 raté).
- Le compte des taches baisse pourtant (11 → 9 → 6 → 3) : **l'œil ne compte pas les sources, il lit l'énergie du cadre**. Ma phrase d'examen (« la différence se lit à la taille d'un téléphone si le nombre de sources baisse nettement ») était fausse dans sa forme : ce n'est pas le nombre, c'est la lumière portée.

**Ligne 2, proches d'abord** (`pr`) : 38 → 16 → 7,5 → 4 (−58 %, −54 %, −45 %).
- Chaque état se lit « plus noir » sans hésiter. Dès `pr5`, le personnage devient le point chaud le plus lisible du cadre : **il gagne en présence à mesure que la ville meurt** — exactement la phrase d'intention.
- `pr1` : presque noir, une source lointaine, une fenêtre, lui et son ambre : « il ne reste que lui et une lumière » se lit.
- Mais c'est l'ordre **le plus cher** : les lampadaires proches portent le plus de lumière sur le sol, les façades et lui ; les effacer en post, c'est relumer tout le cadre (correction de l'examen n°7 confirmée par l'image).
- Défaut : la chute est **trop régulière** (−58, −54, −45) : un escalier, pas une dramaturgie ; et dès le 2e état le film est déjà noir, il ne reste rien à éteindre au pont.

## v2 — `v2-planche.png` : ordre mixte « faisable » (`mx`)
Chaque étape retire **un lampadaire proche du personnage** (source contrôlée, éteinte réellement au tournage : un faux lampadaire) **et un lointain** (effacé en post, petit halo). Le lampadaire le plus proche de la caméra reste jusqu'au pont, où il s'éteint à l'écran.
- Luminance 38 → 28 → 21 → 5 (**−29 %, −25 %, −75 %**) : chaque étape passe le seuil de 20 % (critère 1 tenu), et la courbe a une forme : **deux marches discrètes puis une chute** — « lent puis brusque », le rythme que la marée imposait à l'atelier 04, retrouvé ici par la lumière.
- `mx5` : le noir s'ouvre **autour de lui** (le lampadaire voisin éteint), alors que la rue reste éclairée plus loin : on lit « la nuit est là où il est », sans qu'aucune extinction soit montrée. C'est plus juste que `pr5`, où tout le premier plan meurt d'un coup.
- `mx1` : équivalent à `pr1` (5 contre 4) : la fin est la même, mais on y arrive par une seule vraie chute, celle du pont.
- Faisabilité : 3 sources contrôlées à éteindre réellement (les voisines du personnage et celle du pont), 3 effacements lointains en post. Réaliste en une nuit.

## Ce qui reste faible
- **Le personnage est trop petit** (≈ 6 px de haut à 320 px) : au téléphone, son ambre se lit « lanterne » plus que « quelqu'un » ; critère 2 à moitié. Dans le clip, les retours du cadre-repère doivent être serrés d'un cran, ou alterner avec un plan rapproché de lui.
- Rue géométrique, sans texture (primitives) : la lecture « ville » est faible, « couloir » possible.
- Jugement sur images fixes ; l'extinction montrée au pont (LED instantanée contre décharge) reste à animer (BACKLOG).

## Leçons (versées dans `montage-regard` règle 18, `montage-couleur-et-intention`, `montage-preparation-tournage-vfx`)
1. **L'œil lit l'énergie lumineuse du cadre, pas le nombre de sources** : retirer des points lointains ne se voit pas ; retirer de la lumière portée se voit.
2. **Éteindre autour du sujet d'abord** : le sujet gagne la saillance que la ville perd (`mx5`, `pr5`).
3. **Le plus lisible est le plus cher en post** (lumière portée) → partager : sources proches **contrôlées et éteintes réellement**, sources lointaines effacées en post.
4. **Une soustraction a besoin d'une courbe** (marches puis chute), pas d'un escalier régulier.
