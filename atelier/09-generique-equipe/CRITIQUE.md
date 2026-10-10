# Pièce 09 « Générique de l'équipe » — critiques successives

Script : `generique.py` (Pillow + numpy + ffmpeg, ~10 s de calcul par version). Rendus non conservés (`atelier/rendus/09/`). Contrôle : `python3 -I labo/photosensibilite/flash_check.py`.
Découpage identique pour toutes les versions (son fixé d'abord, 128 BPM = 11,7 images par temps) : 4 cartons d'un temps (12 images), 8 d'un demi-temps (6), 16 d'un quart de temps (3, sous un riser coupé 1 image avant le sommet, clic sur chaque coupe), 4 acteurs d'un temps avec impact, titre tenu 62 images sur un sous-grave qui descend.

## v1 — trois versions (`v1-naif-planche.png`, `v1-lumconst-planche.png`, `v1-une_police-planche.png`)
- **Naïf (fonds noir / blanc alternés)** : `flash_check` **ÉCHEC**, 16 flashs, pire seconde 5 (la section en quarts de temps). C'est l'effet « Enter the Void » le plus facile, et il est inlivrable. Prévu, et confirmé par l'outil sur une pièce réelle.
- **Luminance constante** (fonds sombres de teintes différentes à luminance relative ~0,03, texte clair) : **OK, 0 flash**. Mais à l'œil la planche se lit **diaporama de cartons colorés**, pas une agression : nom centré, petit (10 à 16 % de la hauteur), même composition partout.
- **Une seule police** (contrôle) : presque aussi variée que la version à dix polices. **À cette échelle, la police est un paramètre faible ; la couleur du fond domine.** Le principe « une coupe = une rupture de forme » est faux tel que je l'avais appliqué : changer de police ne rompt pas la forme si la composition ne bouge pas.

## v2 — la rupture d'échelle et de position (`v2-planche.png`, contrôle `v2c-planche.png`)
- Dans les sections rapides, l'échelle saute entre 10, 18, 35 et 60 % de la hauteur, l'ancrage change (gauche, droite, centre, débord), le nom peut sortir du cadre (« UDJANE », « a fontai »). La planche devient **kinetic** : chaque coupe est un choc de forme.
- **Et là, la police compte** : en grand, une chasse fixe, une italique à empattements et une linéale noire n'ont plus rien à voir ; le contrôle à une police (v2c) est nettement plus monotone. Le principe de Kan tient **à condition que la lettre soit assez grande pour qu'on voie sa forme**. Correction du principe : *une coupe = une rupture d'échelle, de position et de teinte ; la police n'ajoute que si elle est grande*.
- Photosensibilité : **toujours OK** malgré de grands aplats de texte clair (la part d'écran qui change dépasse rarement 25 %). Un texte moins lumineux (v2b, valeur 0,75) passe aussi mais terne : inutile.
- **Défaut** : la courbe est inversée. Les acteurs (le sommet voulu) sont **plus petits** que les noms géants du chaos qui précède : on redescend au lieu d'arriver.

## v3 — le sommet doit dépasser le chaos (`v3-planche.png`)
- Acteurs agrandis : limités par la largeur (un nom sur une ligne), ils remplissent tout le cadre en largeur, couleurs saturées, impact sourd à chaque temps. Meilleur, mais pas encore assez : ils restent moins hauts que les plus gros débords du chaos. Il faut changer de **règle** au sommet, pas seulement d'échelle : deux lignes géantes (prénom / nom), ou le même fond pour les quatre (la stabilité dit « voilà les gens qui comptent » après le désordre).
- Loudness : -22,9 LUFS intégré, crête -2,1 dBFS (non normalisé). Pour les réseaux, mesurer puis gain vers -14 LUFS / -1 dBTP (`montage-loudness-livraison`).
- Titre « SAS » noir tenu 2,5 s : la respiration après le sommet fonctionne sur la planche (cinq vignettes identiques = repos).

## Correction (même session, outil durci)
Avec le critère de surface juste (pire fenêtre de 1/3 × 1/3 de l'écran, WCAG), la v3 donne **6 flashs, pire seconde 3 : elle passe à la limite** (la v1 naïve : 14 flashs, pire seconde 5). Ce ne sont pas les fonds (luminance égale) mais **les grands mots clairs** qui flashent localement en apparaissant et disparaissant toutes les 3 images. Ma leçon 2 était trop optimiste. v4 : quarts de temps à 4 images ou texte à valeur 0,75 pendant la montée, et recontrôle.

## Leçons (versées dans `montage-kinetic-editing` et `montage-motion-design-principes`)
1. **Rupture de forme = échelle + position + teinte d'abord ; la police n'ajoute qu'en grand.** Une police par carton à 12 % de hauteur, c'est du décor.
2. **L'effet stroboscopique se fait à luminance constante** : fonds de teintes différentes à luminance relative égale (~0,03) ; mais le texte clair et grand flashe localement (pire seconde 3 à 3 images par carton : limite). Le noir / blanc alterné échoue dès 4 cartons par seconde.
3. **Le sommet doit changer de règle, pas seulement de taille** : après un chaos varié, l'arrivée se signale par la stabilité (même fond, même police, grande taille), pas par un chaos de plus.

## v4 proposée
Acteurs sur deux lignes géantes et fond commun ; ralentir le titre (apparition lettre à lettre sur le sous-grave) ; normaliser à -14 LUFS ; version 9:16 (la rupture d'échelle y est encore plus forte : un mot = l'écran).

## v4 — le sommet change de règle (`v4-planche.png`)
- Acteurs : **fond commun** (le même bleu nuit à luminance égale), **deux lignes géantes** (prénom / nom, 46 % de la hauteur chacune), même police noire, même jaune pâle. Après 28 cartons où tout change, quatre cartons où rien ne change sauf le nom : la stabilité dit « voilà ceux qui comptent ». C'est la première version où la courbe **arrive** au lieu de redescendre. Référence.
- Quarts de temps : texte à valeur 0,72 au lieu de 1 pour gagner une marge de photosensibilité : **inutile** (5 flashs, pire seconde 3, comme v3). Le seuil est une variation de 10 % de luminance relative : un texte encore lisible le dépasse toujours. **Les leviers réels sont la surface (taille du mot dans sa fenêtre) et la fréquence, pas la luminosité.** À garder en tête pour la v5 : quelques quarts de temps en mots petits, ou fusionner deux quarts en un demi.
- Son normalisé par mesure puis gain (+11,4 dB) et limiteur à 0,7 : **-14,5 LUFS, -1,3 dBTP mesurés sur le MP4** (deux essais ratés avant : -15,1 / -0,9 puis -14,9 / -1,5 : l'AAC remonte la crête de ~1 dB au-dessus du réglage du limiteur).
