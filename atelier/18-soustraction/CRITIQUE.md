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

## v3 — `v3-planche.png` : cadrage serré (caméra plus basse et plus proche, 35 mm), silhouette articulée
- Le personnage se lit enfin comme **quelqu'un** (jambes, épaules, un bras qui tient la source) dans les quatre états ; son ambre éclaire son propre corps : critère 2 tenu.
- Mais avec le **même ordre mixte**, la courbe change : 45 → 31 → 15 → 7 (−32 %, −52 %, −53 %) : la chute du pont a disparu, remplacée par un escalier.
- Mesure de la **part de chaque source** depuis cette caméra (`part.py` : chaque lampadaire rendu seul, moins le fond) : lampadaire 0 = **2 %** (il est au bord du cadre, derrière la caméra), lampadaires 1 et 2 = **41 % et 34 %**, les quatre lointains 2-13 %. Le lampadaire que j'avais gardé « pour la chute » n'éclaire plus rien dans ce cadre ; c'est le voisin du personnage qui porte la lumière.
- **Leçon** : la part d'une source dépend du cadre, pas de la rue. **Mesurer la part de chaque source depuis la caméra** (au plateau : les allumer une par une devant le moniteur) avant de décider l'ordre d'extinction ; garder pour le moment montré celle qui porte le plus (ici le lampadaire 1, 41 %), et retirer d'abord les petites parts **par paires** pour que chaque étape dépasse le seuil de lecture.

## v4-v5 (session 14) — l'extinction **montrée**, animée : `v4-planche.png`, `v5-planche.png`
Méthode : `anime.py`. Deux rendus Cycles **EXR linéaires** (cadre v3), lampadaire 1 allumé / éteint ; la lumière étant additive, `L = avant − après`, et chaque image = `après + k(t)·teinte(t)·L`, vue AgX appliquée ensuite par OpenColorIO avec la config de Blender 4.2 (même rendu que Blender, 2 rendus au lieu de 100). 25 i/s, 4 s par variante, événement à l'image 40. Vidéos dans `atelier/rendus/p18v4/` (non versionnées).
Luminance du cadre : 21 → 4 (**−80 %**) quand le lampadaire 1 (41 % de la lumière) s'éteint ; saillance du personnage (boîte autour de l'ambre / moyenne du cadre) : **5,8** après extinction.

| Variante | Courbe | Ce que ça dit |
|---|---|---|
| A sèche (1 image) | marche | « ça s'éteint » ; **ambigu entre "il éteint" et "coupure"** : l'image seule ne donne pas de cause |
| B fondu linéaire 1 s (en lumière de scène) | tient puis plonge (la vue AgX courbe la rampe : −10 % sur la première moitié, tout le reste après) | **un variateur** : quelqu'un règle la lumière d'une scène de théâtre. Faux pour un lampadaire public (aucun ne se fond), et ça dit « effet » |
| C panne (2 rallumages de 1-2 images) | marche hachée | « panne », sans hésitation. Le contraire de l'intention : la ville lâche, il n'agit pas |
| D sodium rallumé (proche, depuis le noir) | 4 → 17 sur 3 s | le virage rose → orange est **invisible** tant que l'intensité est sous ~25 % (Y 4 → 6 pendant 1,5 s) ; à la fin la rue entière est orange et **le personnage disparaît** (saillance 5,8 → **1,5**) |
| E sodium rallumé **au loin** (lampadaire 4), départ à 25 % | 4 → 6 | une tache rose apparaît au fond (amorçage), vire à l'orange ; la ville « revient » loin de lui, **il reste le point** (saillance **3,7**). La tête de lampe reste blanche (AgX blanchit l'émission, cf. pièce 10) : **la teinte se lit sur la lumière portée au sol, pas sur la source** |

### Jugement
- **L'extinction juste est sèche** (vraie physique, session 12), mais **une extinction sèche n'a pas d'auteur** : c'est le montage qui la donne. Il faut une cause dans le plan précédent ou dans le son (le geste vers un interrupteur, le claquement d'un contacteur, un silence qui tombe avec la lumière), sinon le spectateur lit « coupure ». Le fondu n'est pas une solution : il remplace l'auteur par un régisseur.
- La panne est un outil à part entière, pour un autre sens (le monde lâche le personnage).
- **Rallumer la source qui portait la lumière annule la pièce** : on rend la ville et on reprend le personnage. Pour une outro, rallumer **une petite part** (lointaine) : la ville revient sans lui voler la place.
- Un virage de teinte n'existe que dans la **plage visible** : partir d'au moins 25 % de l'intensité finale, sinon trois secondes de virage passent pour trois secondes de noir.

### Leçons (versées dans `montage-couleur-et-intention`, `montage-regard`)
1. Sèche = physique ; fondu = variateur (un humain règle) ; clignement = panne (le monde lâche). Choisir la courbe d'extinction pour **qui agit**.
2. Une extinction sèche se lit comme un acte seulement si la cause est montée (image ou son) juste avant.
3. Un fondu de lumière calculé en lumière de scène ne descend pas linéairement à l'écran (la vue le courbe) : faire le fondu là où il sera jugé, ou le dessiner à l'œil.
4. Pour rendre de la lumière sans retirer la saillance du sujet, rallumer loin et petit.

## v6 (session 15) — la cause montée : `v6-A-planche.png`, `v6-B-planche.png`, `v6-B2-planche.png`, `v6-C-planche.png`, `v6-C2-planche.png`, `v6-C3-planche.png`
Méthode : `v6.py` (montage numpy + ffmpeg, 113 images = 4,5 s à 25 i/s, son synthétique mono 48 kHz) ; rue = les deux EXR du cadre v3 (`scene.py`, SERRE=1 LENS=35, Cycles 32 éch., lampadaire 1 allumé/éteint) vus en AgX par OCIO comme v4 ; insert = `insert.py` (Blender, 16 images, Cycles 12 éch.) : plaque d'interrupteur sur un mur, un index (trois cylindres : se lit « doigt » ou « bâton » selon la taille) appuie sur la bascule, qui claque sans interpolation à l'image 14. Même souffle de rue faible sur les trois ; le clac (transitoire de 3 ms + résonance courte à 2,3 kHz) seulement en B, sur la bascule. Vidéos dans `atelier/rendus/p18v6/out/` (non versionnées).
- **A sans cause** : rue allumée 0-39, sèche à 40, noir tenu. Luminance 23 → 6 (−74 %).
- **B cause avant** : rue 0-29, insert « presse » 30-45 (clac à 43), retour sur la rue **encore allumée** 46-47, extinction à 48.
- **C cause après** : extinction sèche **muette** à 40, noir tenu 1,4 s, insert « lache » 75-90 (bascule déjà en bas, le doigt se retire, sans clac), retour sur la rue noire.
- Contre-épreuves de lumière : **B2 / C2** = même montage, insert ramené par gain linéaire à la luminance du plan qui l'entoure (23 en B, visée 8 en C, obtenu 4-5) ; **C3** = insert C rendu `NUIT=1`, éclairé **seulement par sa lanterne**, basse et proche (luminance 39, flaque chaude sur le noir).

Photosensibilité (`python3 -I labo/photosensibilite/flash_check.py`, fenêtre 1/3) : A 0 flash ; B 1 (pire seconde 1) ; C 1 ; B2 0 ; C2 0 ; C3 1. Tous **OK** (seuil : plus de 3 par seconde). Le flash compté en B, C, C3 est l'aller-retour de luminance que fait l'insert lui-même : un indice, pas un risque.

| Montage | Intention (« il éteint la ville ») | Lisibilité | Rythme | Justesse | Se lit comme |
|---|---|---|---|---|---|
| A | absente : personne n'agit | forte (une marche, −74 %) | une marche dans un plan fixe : brutal, rien ne la prépare | physique juste (LED sèche) | **« coupure »** (comme v4 A) |
| B (insert brut) | présente : geste → clac → rue | trouble : l'insert (55) est **2,4 fois plus clair** que la rue allumée (23) ; le retour sur la rue fait déjà −58 %, l'extinction n'est que la **seconde** chute en 5 images | geste 0,5 s, clac, 2 images d'attente, noir : la chaîne est courte et tenue | le clac sur la bascule est le bon son (un interrupteur, pas une panne) | **« il éteint »**, mais la coupe vole une part de la chute |
| B2 (insert à la clé de la rue) | présente | **la meilleure** : la seule chute de luminance du film est l'extinction | idem | idem | **« il éteint »**, net sur la planche |
| C (insert brut) | arrive après, mais l'insert (55) est l'image la plus claire du film juste après le noir : **il rallume le film** | forte pour l'insert, contradictoire pour la pièce | noir 1,4 s puis un plan clair : le noir est annulé | contredit « il ne reste que lui et une lumière » | « coupure », puis « il touche un interrupteur » : **ambigu entre « il a éteint » et « il va rallumer »** (aucun changement d'état n'est vu, seule la bascule en bas le dit, à peine lisible à 160 px) |
| C2 (insert à la clé du noir) | perdue | **nulle** : à 4-5 de luminance l'interrupteur et le doigt disparaissent | — | juste en lumière, vide en sens | « coupure » puis un plan noir |
| C3 (insert éclairé par sa seule lanterne) | **la plus proche de la phrase** : la lumière de l'insert est celle qui reste | bonne (flaque chaude, bords noirs) | noir, puis une petite lumière qui montre la main : lent, posé | la source est motivée (la sienne) | **« on comprend après »** : c'est lui ; mais le doigt qui se retire peut encore se lire « il vient de toucher » plutôt que « il a coupé » |

### Ce qui ne se juge qu'en mouvement (phase 2)
- Les **2 images de rue encore allumée** après le clac en B : délai de relais crédible, ou décalage perçu comme une erreur de synchro ? (80 ms, sous le seuil d'un son « en retard » d'environ 45-100 ms selon le sens.)
- Si le clac est entendu **comme cause** en A (je ne l'y ai pas mis) : une variante A + clac seul, sans image d'insert, reste à monter (« un son de contacteur synthétique » de la ligne du BACKLOG) ; sur planche, impossible à juger.
- Si 16 images d'insert suffisent à lire « un doigt » (et pas un bâton) en temps réel ; la planche lit la bascule, pas la main.
- En C, si le spectateur relit l'extinction a posteriori (« ah, c'était lui ») ou s'il a déjà rangé l'événement en « coupure » : c'est une question de mémoire, la planche ne la pose pas.

### Jugement
- La cause **avant** donne l'auteur ; la cause **après** donne au mieux une découverte, et elle coûte le noir si l'insert est éclairé comme un plan normal.
- La clé de lumière de l'insert fait partie de la cause : **avant**, à la clé du plan qu'il précède (sinon la coupe fait la chute à la place de l'extinction) ; **après**, éclairé par ce qui reste (sa lanterne), ni à la clé du noir (illisible) ni à la clé du jour (il rallume le film).
- Pour la pièce : B2 si on veut l'acte ; C3 si on veut que le spectateur le comprenne en retard, avec un état de la bascule plus lisible (gros plan, ou bascule lumineuse témoin qui s'est éteinte elle aussi).
