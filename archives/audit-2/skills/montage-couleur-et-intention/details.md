Annexe de `SKILL.md` : mesures, détail des maquettes et des fiches de montage-couleur-et-intention ; les principes ne sont pas répétés ici (le SKILL.md fait foi).

# Couleur et intention : détails des maquettes et des fiches

Les pièces numérotées (`atelier/NN-*/CRITIQUE.md`) sont des maquettes Blender / Pillow : principes à confirmer sur de vraies images en phase 2. Tout ce qui suit est [ÉPROUVÉ EN MAQUETTE] sauf mention contraire.

## Accent rare (pièces 02, 03)
Pièce 03 : 1 apparition de la couleur chaude sur la coupure contre 4 en rotation ; pièce 02 : 0,14 % de pixels chauds avant l'allumage.

## Pièce 05 « Trois étalonnages » (`atelier/05-trois-etalonnages/CRITIQUE.md`)
- Mesures : une rouille presque noire ne devient pas « la seule chaleur » au grade (0,1 % de pixels chauds, liseré rouge sur les bords) ; rouille plus claire au décor + secondaire douce = 2 % de chaud, lisible comme matière ; la matière seule ne survit pas à un étalonnage dense (0,4 %).
- **L'étalonnage choisit le registre, le montage donne le sens** : « constat » et « menace » se lisent sur une image fixe ; « souvenir » se lit « brume » tant que rien (montage, voix, son, marqueur de support) ne dit « il y a longtemps ».
- **Une accentuation qui grandit avec le récit** : une clé prise sur la matière fait croître la chaleur à mesure que l'objet est découvert (0,05 % → 0,45 % → 1,7 %).
- Neutre ≠ froid : mesurer le biais R − B du ciel et du sol pour savoir quoi annuler.

## Pièce 08 « Souvenir » (`atelier/08-souvenir/CRITIQUE.md`)
- Le même passé, propre en 16:9, se lit « autre moment de la journée » ; en 4:3 entre barres avec une texture caméscope, « vidéo d'avant » dès la première image.
- Recette de texture : définition ÷ 2 réaccentuée, noirs relevés, bruit de chroma basse fréquence, balance chaude **modérée** (×1,04 / 1,02 / 0,93) ; à ×0,86 sur le bleu, on tombe dans le filtre jaune.
- La date incrustée répond à la question que le souvenir doit laisser ouverte.

## Pièce 10 : un événement froid dans un monde chaud (session 7)
- Chaleur partout « intime » : la source et le dégradé de la maquette étaient une lampe hors champ et des coins sombres.
- v1-v3 : l'événement froid sortait blanc (0 % de pixels froids mesurés). Avec une feuille blanche (v3), il attire l'œil mais sort encore blanc.
- **v4 (12 essais à une seule variable, mesurés dans la zone de l'événement) : la cause n'est pas AgX** (en vue Standard, la feuille sort *plus* chaude) ; c'est (a) une source à 3 cm de la surface, qui sature ou disparaît sans réglage intermédiaire, et (b) une couleur d'écran réaliste trop pâle à côté d'une lampe orangée saturée. L'hypothèse « AgX / une émission intense blanchit le froid » est **réfutée** ; le seul fait mesuré sur AgX est le plafond du blanc (≈ 222/255, `montage-blender`).
- Mesures des remèdes : source gélatinée plus bleue, vue de face, B − R +0,02 → lisible ; clé secondaire sur la zone, +0,10, le plus net.
- v5 : la lumière d'un écran ne se voit que sur les surfaces tournées vers lui ; une plongée qui montre la source cache ce qu'elle éclaire → **deux plans** (la source s'allume / le visage bleuit) : c'est le montage qui fait entrer le froid.
- Règle de méthode : une explication de couleur ne va dans un skill qu'après un essai qui isole la variable.

## Pièce 13 « Le fond raccorde » (`atelier/13-fond-raccorde/CRITIQUE.md`) (perception estimée par modèle, à confirmer)
- Refroidir le mur : la peau ne bouge presque pas (ΔE 1,7, rebond du mur). Refroidir sa lumière : ΔE 6,5 (il pâlit, s'éteint), et faux raccord si l'autre personnage, dans la même pièce, ne change pas.
- Pour « il se ferme » : le monde d'abord (fond, en marches), le corps une seule fois, à la bascule.
- Un décor orange (Joker, intérieur au tungstène) demande une peau protégée ou légèrement poussée, sinon elle paraît livide.

## Fiches : ce que le SKILL.md ne reprend pas
- **Doyle / Wong** : le flou de mouvement montre le temps intérieur.
- **Deakins** : tenir le plan quand la silhouette parle.
- **Willis** (`culture/gordon-willis-le-noir.md`) : les yeux dans le noir = le secret ; le noir n'existe que par opposition (le mariage au soleil) ; direction de la lumière = lecture morale (dessus : masque, dessous : menace, côté bas : confidence). Protéger le noir en post : le **10 bits** est la solution au master, pas de relevage des noirs ; le grain donne une matière au noir mais **n'est pas une protection** à l'encodage : sur une image surtout noire, il consomme le débit et fait pire (`labo/encodage/noir-protege/RESULTATS.md`, `montage-loudness-livraison`) [TESTÉ EN LABO].
- **Young / van Hoytema** (`culture/bradford-young-van-hoytema-lumiere-basse.md`) : dans le noir, éclairer **par rebond** (la source éclaire un objet clair qui éclaire le visage) ; la **température d'une solitude est un jugement** (froid : on la plaint, chaud : on la respecte) ; motiver l'ambiance par le dehors.
- **Braier** (`culture/natasha-braier-lumiere-de-nuit.md`) : une source dans le champ qui ne touche pas le visage = décor lumineux posé sur une image neutre, l'effet « clip » ; réserver la lumière la plus saturée aux rares moments qui la justifient.

## Pièces 17 et 18 : sources pratiques et soustraction
- Pièce 17 (variable isolée : seul l'écran passe du chaud au froid) : chambre → hôpital, peau → plâtre ; la scène ne devient pas plus angoissante.
- Pièce 18 (mesuré à 320 px, `atelier/18-soustraction/CRITIQUE.md`) : éteindre autour du sujet d'abord ; courbe de luminance −29 %, −25 %, puis −75 % au moment montré.
- v4-v5 (rendu Blender ; perception à valider) : la teinte d'un virage se lit sur la **lumière portée** (sol, murs) plus que sur la source vue de face. **Fondu de lumière** : une rampe linéaire en lumière de scène ne descend pas linéairement à l'écran (presque rien la première moitié, tout ensuite) : faire le fondu dans l'espace où il sera jugé, ou le dessiner à l'œil.
- **Recette** : 2 rendus EXR linéaires (avant / après), la différence = la contribution de la source ; toute courbe d'extinction ou de rallumage se compose par addition, puis vue appliquée par OCIO (`atelier/18-soustraction/anime.py`). En compositing (AE 32 bits linéaire, Fusion, Nuke) : une **passe par source** au rendu 3D permet de régler la dramaturgie de la lumière au montage. Au tournage : `montage-preparation-tournage-vfx` §5 ter.

## Pièce 22 v3 : le blanc et le noir comme mondes (rendu Blender ; perception à valider)
- Une silhouette noire sur fond noir disparaît (faute invisible tant qu'on n'a pas fait la variante). Dans le noir, éclairer le sujet seul (une douche motivée) ; un liseré en contre-jour seul donne une présence fantôme, juste pour la fragilité, trop faible pour un sujet principal.
- Exemples : blanc clinique = « tout le monde, calme, hors du temps » (salle d'attente, laboratoire) ; noir à lumière froide = « les morts, l'abîme ». Choisir selon le ton du texte, pas selon la chaîne qu'on imite.
- Blanc pur : AgX plafonne le blanc vers 222/255 [TESTÉ EN LABO] (les autres transformées filmiques, ARRI, ACES, compressent aussi les hautes lumières [THÉORIQUE]) ; le « blanc EGO » (luminance médiane 225+ en plage limitée) se pose avec un point blanc en grade. Mesurer le maximum avant de corriger. Recette : `montage-blender`.

## Pièce 23 : l'infrarouge
Le vert et le bruit coloré à gros grain codent la surveillance même avec une lumière sculptée ; pour l'intime, ajouter une vignette douce ; un noir à 6 % fait un voile laiteux. Le vert reste juste pour le malaise ou le found footage, comme choix. Tournage : `montage-preparation-tournage-vfx/infrarouge.md`.

## Pièce 25 « Au lit » : une descente de lumière (YAVG mesuré)
- Un gradateur de −60 % sur tout le montage ne fait pas descendre l'image si les plans ne sont pas ordonnés (une lampe de chevet à 25 s faisait le pic de la seconde moitié).
- La descente se lit mieux comme **un événement du monde** (les fenêtres de la ville qui s'éteignent une à une) que comme un réglage.
- 20 s à YAVG 19 se lisent « écran éteint ». En v3, la lune **non graduée** sur un ciel qui s'éteint paraît s'allumer : la dernière lumière devient l'image. Un cadre clair qui revient **à la fin** réveille (20 → 32) : placer les retours au milieu de la descente.

## Pièce 31 « Le même escalier » (principe Joker n°3 ; images fixes Blender ; perception à valider)
- Ce que dit chaque levier : lumière = l'heure et la valeur (chaud = désir, froid = isolement), hauteur de caméra = rapport de force, corps = qui a changé. Seul : lumière = « le soir est tombé » ; contre-plongée en froid = menace, pas éclosion (R4b).
- Le contre-jour pur **efface le repère du lieu** (marches à l'ombre) ; contre-jour **rasant et de biais** : il redessine les arêtes ; garder un repère fixe (mât, rampe, fenêtre).
- Le rouge réservé au plan de bascule signe la transformation. Détail : `atelier/31-meme-escalier/CRITIQUE.md`.
