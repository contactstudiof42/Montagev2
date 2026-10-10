# Pièce 31 « Le même escalier » — critique (session 24, 2026-10-10)

Rendus : `blender -b -P scene.py -- OUT.png froid|chaud haute|basse voute|ouvert [v2]` (Blender 4.2.3, Cycles 32 éch. + débruitage, 480×270, **9 s par image**).
Mesure : `python3 mesure.py atelier/rendus/31 R1 R2b …` (Δ chroma a*b*, Δ L*, contours communs à cadre égal seulement).
Planches : `v1-planche.png`, `v2-planche.png`.

## v1 (`v1-planche.png`)
- R1 aller (froid, plongée, voûté) : lisible, l'escalier écrase la silhouette. Le corps « voûté » ne se lit pas (maquette trop schématique : un cylindre penché ressemble à un robot). Limite assumée de la pièce.
- R2 (lumière seule inversée) : le lieu est reconnu (contours communs r = 0,38 au même cadre), mais on lit **une autre heure**, pas un autre homme.
- **R3 / R4 ratés** : en contre-jour pur, les marches passent à l'ombre et **disparaissent** ; l'image devient un couloir quelconque, plus sombre de 62 niveaux. Inverser la lumière a effacé le repère qui fait reconnaître le lieu. Et le réverbère, autre repère, est sorti du cadre.

## v2 (`v2-planche.png`) : soleil rasant de biais, caméra basse à 0,9 m
- Le soleil bas et de biais fait accrocher la lumière aux nez de marches et au mur droit : l'escalier **se redessine en lumière** au lieu de disparaître. Le mât du réverbère reste dans le cadre. Le lieu se reconnaît (marches, mât, fenêtres) sans aucun plan de rappel.
- R2b (lumière seule) : toujours « le soir est tombé », pas une transformation.
- R5b (caméra basse seule, lumière froide) : la contre-plongée rend la silhouette **massive et menaçante**, pas libre. La hauteur donne la puissance, pas la joie.
- R3b (lumière + caméra) : chaud et puissant, mais le corps voûté contredit l'image : on lit un homme fatigué dans un beau soir.
- **R4b (lumière + caméra + corps) → référence** : seule combinaison qui se lit comme une transformation (le rouge de la veste n'apparaît qu'ici, comme dans le film où la couleur forte est retenue jusqu'à la bascule). Δ chroma 31, ΔL −33 par rapport à l'aller.

## Ce que j'en retiens (versé dans `montage-couleur-et-intention`)
1. Dans un « même décor inversé », chaque levier dit une chose : **la lumière dit l'heure et la valeur** (chaud = désir, froid = isolement), **la hauteur de caméra dit le rapport de force**, **le corps dit qui a changé**. La transformation d'un personnage ne se lit que si les trois vont dans le même sens ; un seul levier ne change que ce qu'il dit.
2. Inverser la lumière peut **effacer le repère** du lieu (le contre-jour plonge les marches dans l'ombre). Choisir un contre-jour **rasant et de biais** qui redessine les arêtes du décor ; garder au moins un repère fixe dans le cadre (mât, rampe, fenêtre).
3. La couleur forte (le rouge) n'est réservée qu'au plan de bascule : elle signe la transformation.
4. La contre-plongée seule, en lumière froide, produit la menace : utile pour un antagoniste, à éviter si l'on veut l'éclosion.

## v3 — aller fixe 3 s, coupe, retour en grue montante 3 s (`v3-planche-grue.png` ; rendu animé 320×180, 12 éch., 75 images en ~1 min 30)
- La grue **découvre le lieu** : à 0,9 m, les marches sont des lignes sombres ; en montant, leurs nez accrochent le soleil un à un et l'escalier se reconstruit sous le personnage. Le mouvement fait le travail de reconnaissance que le cadre fixe bas ne faisait pas : la caméra qui monte élève le personnage **et** rend le décor. Je ne l'avais pas prévu.
- Le mât du réverbère sort du cadre en fin de grue : ce n'est plus grave, les marches ont pris le relais comme repère. Un repère peut passer de l'un à l'autre pendant un mouvement, pas à travers une coupe.
- Juxtaposés sans rien entre eux, aller et retour se lisent « avant / après » (une pub, pas un film) : dans *Joker*, une heure de film sépare les deux passages. En pub courte, il faudrait un plan intermédiaire (le personnage ailleurs, la bascule) ou assumer le diptyque.
- La silhouette reste un pantin : le voûté de l'aller ne se lit toujours pas.

## Limites et suite (BACKLOG Y41)
Silhouette trop schématique (le voûté ne se lit pas) ; mouvement de caméra (fixe → grue) non testé ; une seule focale (28 mm).
Suite : rendu animé court des deux passages (aller 3 s fixe, retour 3 s en grue montante) et figure articulée ; tester une focale plus courte au retour (Sher : courte focale portée).

## v4 — figure articulée et axe de lecture d'une posture (session 25, `v4-planche-azimuts.png`)
`scene_v4.py` : figure en capsules par cinématique directe (dos, cou, bras, avant-bras, cuisses, tibias), poses `voute` (dos 38°, tête tombée, bras pendants) et `ouvert` (dos cambré, tête levée, bras ouverts en V) ; argument `az=DEG` = caméra tournée autour de la figure à 3 m ; `murfou` = mur droit invisible pour la caméra (« mur volant » de studio : il garde son ombre et sa lumière). Haut : aller (froid, plongée) à 0° / 30° / 60° / 90° ; bas : retour (chaud, contre-plongée) aux mêmes angles. 14 s par image.
- **Le voûté ne se lit qu'en profil** (60-90°) : de dos (0°), la flexion du dos est dans l'axe de la caméra, raccourcie à rien ; la figure devient une capsule droite. C'était la vraie cause de l'échec de v1-v3 : ce n'était pas la silhouette trop schématique, c'était **l'axe**.
- **L'ouverture des bras ne se lit que de face ou de dos** (0°) : en profil, les bras se superposent et la figure « attrape quelque chose en haut » ; la joie disparaît.
- Donc **chaque posture a son plan de lecture** : une flexion (dos, nuque) se lit dans le plan sagittal → caméra de profil ; une ouverture (bras, épaules) dans le plan frontal → caméra de face ou de dos. Dans un diptyque aller / retour, le **changement d'axe** entre les deux passages n'est pas un choix de style : il est dicté par ce que le corps doit dire. Ici : aller en 3/4 profil (60°), retour de face.
- Le décor décide si l'axe est possible : dans un escalier-couloir, le profil exige un mur volant (studio) ou un escalier ouvert d'un côté (repérage). À noter en préparation de tournage.
- À 30°, le mât du réverbère coupe le cadre et la figure est minuscule : un repère du lieu peut devenir un obstacle quand l'axe tourne.

## v4b — la focale à taille de figure constante (`v4-planche-focales.png` ; haut : aller 60°, bas : retour de face ; 16 / 28 / 60 mm, distance ∝ focale)
- **Retour** : à 16 mm, les murs du couloir s'écartent en fuyant, la lumière chaude prend de la place, la figure domine un espace qui **s'ouvre** autour d'elle (l'éclosion). À 60 mm, les murs deviennent deux verticales parallèles, l'escalier derrière lui s'empile : il est **encore dans la boîte**, même bras ouverts. La courte focale dit l'éclosion mieux que la posture seule.
- **Aller** : à 16 mm, l'escalier fuit loin devant : la montée est **longue** (la distance qui reste) ; à 60 mm, les marches s'empilent en mur devant lui : la montée est **écrasante** (l'obstacle). Les deux sont justes, pour deux intentions différentes ; pour le contraste avec un retour en 16 mm, je choisis **60 mm à l'aller**.
- Leçon : la focale est un **quatrième levier** du même décor inversé (après lumière, hauteur, corps) : elle dit **l'espace dont le personnage dispose**. Long = enfermé ou écrasé ; court et proche = l'espace s'ouvre. Diptyque retenu : aller 60 mm, 3/4 profil, plongée, froid, voûté → retour 16 mm, face, contre-plongée, chaud, bras ouverts, veste rouge.

## v4c / v4d — le diptyque animé (`v4c-diptyque.png` : aller fixe 3 s puis retour ; `v4d-retour.png` : retour corrigé ; 75 images 320×180, 12 éch., ~1 min 30 de rendu)
- Aller : 60 mm, 3/4 profil, plongée, froid, tenu 3 s sans mouvement : le voûté se lit dès la 1re image, et l'immobilité de la caméra ajoute au poids (rien ne l'aide).
- Retour v4c : travelling avant montant (16 mm, +0,6 m vers lui, +0,7 m de hauteur) avec la visée **fixe à la taille** : en fin de mouvement la tête sort du cadre. L'élan devient absurde (un torse rouge et des bras). **Dans un mouvement qui monte, la visée doit monter avec** (ou la tête est coupée exactement au moment de la bascule).
- Retour v4d (visée taille → tête, même courbe sinus) : la figure grandit et ses bras **embrassent les bords du cadre** à la fin : en courte focale proche, l'ouverture du geste devient l'ouverture du cadre. Prix : les marches ne sont plus qu'une bande en bas, le lieu se lit par la tache de soleil du mur. Le repère passe des marches à la lumière, pendant le mouvement (cohérent avec v3).
- Diptyque aller 60 mm fixe → retour 16 mm en mouvement : le changement de focale et le passage du fixe au mouvement disent la même chose (l'espace s'ouvre, le monde se met à bouger avec lui). Les quatre leviers + le mouvement vont dans le même sens : **c'est la première version où la transformation se lit sans le rouge**. Le rouge reste la signature, plus la seule preuve.
