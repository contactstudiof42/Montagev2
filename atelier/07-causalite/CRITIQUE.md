# Pièce 07 « Causalité » — critiques

## Avant le rendu : ce que la préparation a déjà appris (session 6)
- **La simulation a d'abord explosé** : tous les dominos partaient à l'image 2 et la tasse traversait la table. Cause : `transform_apply(scale=True)` applique aussi la position, donc les formes de collision se centraient sur l'origine. Corrigé, consigné dans `montage-blender`.
- **Le dernier domino touchait la tasse dès le départ** (moins de 1 cm de jeu) et la poussait à l'image 2 : la cause arrivait avant la cause. Il a fallu un jeu de 4 cm. En atelier comme sur un plateau, une chaîne causale se vérifie maillon par maillon **avant** de tourner.
- **Densité des contacts** (`evenements.json`) : bille → domino 0 à l'image 41, puis un contact toutes les 2-3 images (44, 48, 50, 53, 55, 56, 58, 60), domino → tasse à 63, tasse au sol à 76. **Entre 41 et 63, il n'existe aucun intervalle de 8 images sans contact** : impossible d'y couper à 4 images ou plus de tout contact. Le critère 2 de l'intention ne peut donc être tenu que si un même plan contient toute la cascade. C'est la mécanique, pas le montage, qui dicte où l'on peut couper : la chaîne a deux « respirations » (le roulement 4-41, le vol de la tasse 67-76).
- **Cadres ratés à l'image fixe** : la caméra « tasse » et la caméra « chaine », placées à 42-45 cm du sol, regardaient sous le plan de la table. Les dominos étaient coupés par le bord du plateau et le contact domino → tasse était caché. Relevées à 95 cm, inclinées de 18° vers le bas. Sans le contrôle à l'image du contact, la version B aurait coupé sur un contact invisible.
- **Eevee** (essayé pour aller vite) : 7 s/image en rendu logiciel, plus lent que Cycles. Abandonné.

## v1 : trois montages du même événement (A `v1-A-planche.png`, B `v1-B-planche.png`, C `v1-C-planche.png`)
Même simulation, même son (tiré de la simulation, attaques à ≤ 1 image des contacts, mesuré), 110 images (4,4 s), 480×270.

**A, plan unique large.**
- *Intention servie ?* Oui pour la preuve : bille, cascade, poussée, chute, tout est dans le même cadre, rien ne peut être truqué.
- *Lisibilité* : insuffisante. À 480 px, un domino fait 1 à 2 px de large ; la cascade se lit comme une ligne qui se couche, pas comme des objets. Critère 4 non tenu.
- *Composition* : la table est centrée, mais **l'événement final (la tasse au sol) a lieu au bord du cadre, en bas à droite**, et la tasse roule hors champ dès l'image 85. Les 25 dernières images ne montrent rien. Le cadre a été pensé pour la chaîne, pas pour sa conséquence.
- *Justesse* : honnête mais pauvre. C'est la version « caméra de surveillance ».

**B, coupe sur chaque contact (41, 63).**
- *Mesure* : distance coupe-contact = 0 et 0. Comme prévu, chaque coupe tombe exactement sur une cause.
- *Ce que montre la planche* : au début du plan dominos (image 41), la bille est encore hors cadre à gauche. Le domino 0 commence à bouger avant que l'on voie ce qui le pousse ; la bille n'apparaît qu'à l'image 45. Et le dernier plan (large) perd la tasse par le bas de l'image : **le choc au sol, le son le plus fort de la pièce, a lieu hors champ.**
- *Verdict* : B est le plus nerveux et chaque plan est lisible, mais **les deux contacts sont escamotés par les coupes**. C'est exactement ce que fait un montage truqué. Mon hypothèse se vérifie sur la planche : couper sur le contact, c'est couper la preuve. Le son synchrone (le clic sur la coupe) masque le manque à l'écoute, mais le regard attentif doute.

**C, coupes dans les respirations (30 pendant le roulement, 71 pendant le vol).**
- *Mesure* : distance coupe-contact = 11 et 5 images (critère 2 tenu ; 71 est à 4 images du départ de la tasse, à 5 de son arrivée au sol).
- *Ce que montre la planche* : la bille sort du plan « livre » vers la droite et entre dans le plan « chaîne » par la gauche à l'image 41 : raccord de direction juste. Bonus non prévu : de 30 à 40, le plan « chaîne » montre **les dominos qui attendent**, avant l'arrivée de la bille. On sait ce qui va se passer et on l'attend (le suspense de la bombe sous la table, au sens d'Hitchcock). Le plan « sol » (71) est vide pendant 5 images, puis la tasse y tombe : c'est l'attente de l'impact, et le choc est dans le cadre.
- *Défauts* : dans le plan « chaîne », les dominos restent petits. Et dans le plan « sol », la tasse roule et sort du cadre par la droite à partir de l'image 101 : la fin se dilue au lieu de se poser.

**Ce que la v1 m'apprend.**
1. **Dans une chaîne causale, la mécanique décide où l'on peut couper.** Une cascade (un contact toutes les 2-3 images) ne se coupe pas ; il faut la tenir dans un plan. Les seules coupes honnêtes tombent dans les **respirations** (roulement, vol, chute), là où l'objet voyage entre deux contacts, et de préférence **sur la direction du mouvement**.
2. **Couper sur le contact escamote la preuve** (B). Pour la pub ou les réseaux, où l'on coupe sur l'impact pour l'énergie (kinetic), c'est acceptable *si la preuve n'est pas l'argument*. Quand elle l'est (démonstration produit, Cog), c'est une faute.
3. **Un plan qui commence avant la cause crée l'attente** : montrer l'effet en puissance (les dominos debout) avant la cause.
4. **Cadrer la conséquence, pas seulement la chaîne** : en A et en B, l'impact final est au bord du cadre ou hors champ.

**v2 (proposée et lancée)** : C seulement. Tasse amortie (`angular_damping` = 1 : une vraie tasse a une anse qui l'empêche de rouler loin ; elle s'arrête en 9 images à 2 cm du point d'impact, dans le cadre du plan « sol »). Plan « chaîne » plus serré (`chaine2`, 32 mm, centré sur la cascade). La pièce passe à 135 images, avec 2 s de silence sur la tasse immobile.

## v2 : C resserré, tasse amortie (`v2-C-planche.png`)
- Plan « chaine2 » (32 mm) : les dominos passent de 1-2 px à 3-4 px de large, la cascade se lit comme une suite d'objets. Mieux.
- **Raté majeur** : avec `angular_damping = 1` dès le début, la tasse ne tourne plus du tout. Elle glisse du bord **debout**, tombe debout et atterrit debout. C'est physiquement faux, et ça se lit comme une tasse posée par une main invisible : un trucage, l'inverse exact du propos. **En corrigeant la fin, j'ai abîmé le milieu.** Un réglage physique global agit sur toute la trajectoire.
- Accident heureux : la bille, qui a roulé jusqu'au bout de la table et en est tombée, **revient entrer dans le dernier plan à l'image 125**, et roule vers la tasse. La cause vient voir son effet. Je le garde (Varda : garder l'accident qui rime).

## v3 : amortissement seulement après l'impact (`v3-C-planche.png`, référence)
- `amort_apres = [77, 0.9]` : amortissement angulaire et linéaire mis en clé à l'image de l'impact (les propriétés de corps rigide s'animent). Vérifié dans la simulation : la tasse bascule (rotation 2,2 rad à l'image 69), atterrit inclinée à 76, oscille, se couche sur le flanc vers 105, reste dans le cadre (x = 1,13 m).
- Planche : la bascule est lisible (65-69), l'impact est dans le cadre (77), l'oscillation 81-97 donne du poids, puis l'immobilité 105-135 avec le seul souffle de pièce. Le son du choc tombe à 1 image de l'impact.
- Critères : 1 (chaque contact visible dans un plan) **tenu** pour la bille, la cascade, la poussée et le sol ; 2 (distance coupe-contact ≥ 4) **tenu** (11 et 5) ; 3 (son à 1 image) **tenu** ; 4 (lisibilité à 480 px) **partiel** : les dominos restent petits, il faudrait du 960×540 ou un 3e plan serré de la cascade, impossible à couper sans tomber sur un contact.
- *Reste à juger en mouvement* (phase 2) : l'oscillation de la tasse est-elle crédible à 25 i/s ? Le silence de 1,2 s avant le retour de la bille est-il juste ou trop long ?

## Prochaine version (v4, pour une session suivante)
1. Allonger la fin (≈ 160 images) pour que la bille **atteigne** la tasse et s'y arrête : dernière image = la cause et l'effet côte à côte, immobiles. Vérifier que ce n'est pas trop « écrit » (le hasard qui fait trop bien les choses se voit).
2. Écrire des respirations dans la mécanique elle-même (un domino plus espacé, une petite rampe) pour permettre un plan serré de la cascade sans couper sur un contact : en tournage réel, c'est au plateau que se décide le découpage d'une chaîne causale.
3. ~~Rendre A en 960×540~~ : fait, voir le test de lisibilité ci-dessous ; à la place, un recadrage plus serré de A.

## Test de lisibilité de A : 480 contre 960 px (`lisibilite-480-vs-960.png`)
Même image (50, la cascade en cours) ; en haut, recadrage du rendu 480×270 agrandi ×2 au plus proche voisin ; en bas, le même recadrage dans un rendu 960×540 (9 s en 4 processus).
- **Surprise** : à 480 px, l'information est déjà là. Chaque domino fait ~3 px et se distingue nettement une fois agrandi ; le 960 n'apporte que de la netteté.
- Donc la lisibilité de A ne vient pas d'un manque de **résolution**, mais de la **part du cadre** : la chaîne n'occupe qu'un tiers de la largeur, et sur un téléphone, ça fait moins de 2 cm. Le remède est un cadre plus serré ou un recadrage dans l'image (zoom numérique dans un master 4K), pas un rendu plus fin.
- Principe : avant de monter la résolution, mesurer **la taille de l'objet en pourcentage de la largeur du cadre** et la rapporter à l'écran de diffusion (un objet de 3 % de large sur un écran de 6 cm fait moins de 2 mm).
