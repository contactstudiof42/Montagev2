# Pièce 21 — critique (session 17)

Planches : 2,5 images/s, 8 × 3 (`v1-A-planche.png`, `v1-B-planche.png`, `v1-C-planche.png`, `v2-B-planche.png`). Rendus régénérables : `piece.py A|B|C VOIX.wav OUT.mp4 [--v2]` (voix : la commande espeak-ng de `INTENTION.md`).

| Version | Ce que montre la planche | Verdict |
|---|---|---|
| A (pictogrammes, coupes sur la voix) | horloge, lune « 8 h », « 16 h » géant, 16 cases, téléphone « 3 h » : chaque image est juste et lisible | **un diaporama** : les chiffres se suivent, les **rapports** (8 sur 24, 3 sur 16) ne sont jamais montrés ; le spectateur doit faire le calcul pendant que la voix continue. Les 16 cases puis le téléphone : rien ne dit que les 3 h sont prises **dans** les 16. |
| B v1 (un cercle qui change de rôle) | la nuit se balaie dans le cadran, le reste se remplit en orange, la nuit s'efface, une part de 3 h sort et devient un écran | **l'argument est dans l'image** : on voit la proportion, et surtout **le trou** que laisse la part partie (non prévu : c'est l'image la plus forte de la pièce, le manque). Défaut : l'aiguille des minutes fait un tour en 1,7 s : ce n'est pas un mouvement de repos, c'est un événement (« le temps file ») qui sur-signifie et vole l'œil pendant la première phrase. Après le départ des 3 h, plus aucun chiffre ne nomme le reste. |
| C (même animation, grille fixe de 1,6 s) | les deux premières transformations arrivent **0,58 s et 0,39 s avant** la phrase qui les nomme (puis −0,11 et +0,03 s, par hasard) | **l'image contredit la voix** : le secteur de nuit apparaît pendant « vingt-quatre heures », le reste orange pendant « dormons huit ». Sur une grille, l'image ne tombe juste que par chance. |
| **B v2** | aiguilles quasi immobiles (minute à 0,25 rad/s : un tour en 25 s), « 13 h » nomme le reste après le départ de l'écran | le cercle respire (±1,2 %) et les aiguilles dérivent sous le seuil de l'événement ; la première phrase laisse lire le cadran ; la fin dit le résultat (13 h) que la voix tait. **Version retenue.** |

## Grille (B v2)
- **Intention servie** : oui, la proportion se voit ; A ne la montre pas, C la brouille.
- **Lisibilité** : un seul objet, deux couleurs signifiantes (bleu nuit, orange temps libre) + une troisième pour l'écran (cyan) : chaque couleur = un rôle.
- **Rythme** : 4 transformations en 8 s, chacune au début de sa phrase ; une phrase sans transformation (« Et sur ces seize heures ») où la nuit s'efface seulement : la respiration qui recentre.
- **Justesse** : aucun son ajouté, aucune transition gratuite ; le seul geste spectaculaire (la part qui sort) est celui qui porte l'idée.
- **Cliché** : palette sombre + orange saturé + formes plates = la grammaire Kurzgesagt reconnaissable. Pour une vraie commande, garder le principe (un objet, des rôles) et changer la matière.

## Leçons
1. **Un explicatif à pictogrammes montre des noms ; un objet qui change de rôle montre des rapports.** Quand l'argument est une proportion, une comparaison ou une cause, il doit être dans la transformation, pas dans la succession.
2. **Ce qui manque après une transformation peut être l'image la plus forte** (le trou laissé par les 3 h) : prévoir la trace d'un départ, pas seulement l'arrivée.
3. **Le mouvement de repos doit rester sous le seuil de l'événement** : une aiguille qui fait un tour en 1,7 s raconte quelque chose ; à un tour en 25 s, elle fait seulement vivre le plan.
4. **Caler l'image sur les idées, pas sur une grille** : sur une grille fixe, les deux premières transformations précédaient de 0,4-0,6 s la phrase qui les nommait et contredisaient la voix. Une image peut devancer le mot de 1 à 3 images (convention d'animation, à vérifier), pas d'une demi-seconde.
5. Méthode : **mesurer les débuts de phrase de la voix définitive** (silencedetect -40 dB, 0,25 s) et s'en servir comme feuille d'exposition.
