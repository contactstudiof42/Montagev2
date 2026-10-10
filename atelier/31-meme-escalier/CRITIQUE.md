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
