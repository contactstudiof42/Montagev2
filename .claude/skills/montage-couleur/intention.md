Annexe de `SKILL.md` : le savoir de l'intention couleur (films mesurés, constats de 45 vraies vidéos, principes éprouvés en maquette, méthode du brief à l'intention, mots entendus, clichés, maquettes) ; tiré de `montage-couleur-et-intention` à l'audit 2 (2026-10-13). Le SKILL.md fait foi. Principes de pure source (Storaro, Doyle, Deakins…) et « Limites » périmées : `archives/audit-2/skills/montage-couleur-et-intention/`.

# montage-couleur — intention

**Marqueurs** : [VU SUR IMAGES] mesuré ou vérifié sur de vraies vidéos (phase 2, `analyses/`) · [SOURCÉ] fiche ou source écrite · [THÉORIQUE] convention du métier non vérifiée ici · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette Blender / Pillow, hypothèse à confirmer sur de vraies images (phase 2).

Détail des maquettes et des fiches : section « Détails des maquettes et des fiches », plus bas. Sources : `culture/storaro-apocalypse-now-couleur.md`, `culture/christopher-doyle-wong-kar-wai.md`, `culture/roger-deakins-sicario-1917-blade-runner-2049.md`, Willis, Young / van Hoytema, Braier (`culture/`).

## Idée centrale
La couleur n'est pas une finition, c'est **un sens**. Avant de toucher une roue : « que doit ressentir le spectateur, et comment ça change du début à la fin ? ». Un look sans réponse est un filtre.

## Les films de référence, mesurés (la parole de Diego sur eux est dans `GOUTS.md`) [VU SUR IMAGES]
- **Joker** : garder la dominante « fausse » (fluos, sodium) qui raconte un lieu et un état, ne rendre juste que la peau ; faire **mériter** la couleur forte (une seule couleur lâchée à la bascule) ; lumières motivées. [VU SUR IMAGES] (mesuré sur le film, `analyses/films/joker.md`) : vert dominant pendant 95 min (maximum dans le métro), rouge saturé presque nul jusqu'au plateau de Murray (1:35) ; les seules touches rouges avant appartiennent à **des lieux de spectacle** (scène du club, théâtre) : la couleur méritée s'annonce par petites touches attachées à un lieu symbolique, puis le personnage la porte. L'image ne s'assombrit pas au fil du film ; la fin est claire et désaturée. La première vraie plage rouge est **un passage** : la lumière des coulisses de Pogo's (0:42:42), sur le chemin de la scène. À la fin, le vert n'est pas remplacé : il **passe du personnage au décor** (fumée bleu-vert de l'émeute) et le rouge prend le corps ; la couleur dominante change de place plutôt que de disparaître.
- **Whiplash** (sélection de la phase 2, pas un goût cité par Diego) : **deux mondes codés par la couleur**, l'ambre de la musique (tungstène, bois, cuivres) et le vert ou le neutre de la vie (dehors, famille, route). La chaleur monte avec l'obsession et le final est le passage le plus chaud et le plus saturé du film, **sans vert** (part de vert 0,06 contre 0,41 au début). [VU SUR IMAGES] (`analyses/films/whiplash.md`)
- **Spider-Man: Across the Spider-Verse** (sélection de la phase 2) : **une matière graphique par monde** (aquarelle rose et bleu pour Gwen, chaleur maximale pour Mumbattan, rouge et noir pour la Terre sans Spider-Man), ce qui rend lisibles des plans de 0,5 s dans le film le plus rapide du corpus (médiane 1,96 s) ; et **dans un seul monde, la couleur suit l'émotion plan par plan** (Gwen face à son père : rose pendant l'aveu, cyan quand il pointe son arme, les deux mélangés quand elle s'enfuit). Le monde du héros (Brooklyn) est le moins saturé. [VU SUR IMAGES, mesuré] (`analyses/films/spider-man-across-the-spider-verse.md`) Variante mémoire dans *Aftersun* : une texture par temps (MiniDV neutre à chaud, 35 mm des vacances, rave noire, présent de l'adulte le plus froid, rouge - bleu -17 à -25). [mesuré] (`analyses/films/aftersun.md`)
- **Ziak** (mesuré sur le clip réel) : luminance médiane 8/255, quasi monochrome froid, une seule couleur chaude sur 0,16 % de l'image dans 24 s sur 229. Le noir est la matière, la couleur un événement compté.

## Repères mesurés en projet (à revérifier sur chaque projet)
- Peau naturelle ≈ 50-60° de teinte OkLCh, chroma 0,06-0,09 (film de marque kinetic) ; au mariage, peaux du jour à 51° de médiane (80 % entre 43 et 58°), chroma 0,065 ; sous une lumière rose ou violette du soir, 38-49°, chroma 0,10-0,13 (lumière réelle). [TESTÉ EN CONDITIONS RÉELLES]
- Noirs (5e centile de luma) des sept références réseaux de Diego : 5 à 11 sur 255 (60 pour un look laiteux voulu) [genre : réseaux, look film] ; ma V2 du film de marque était à 17.
- Exposition d'un objet blanc : part des pixels ≥ 97 % sur l'objet et ≥ 250 sur l'image, en pleine résolution, comme indice seulement (le compteur ne voit pas des blancs tassés sous 250).

## Ce que 45 vraies vidéos confirment (phase 2) [VU SUR IMAGES]
Mesuré sur une vignette toutes les 10 s par film (luminance, saturation, chaleur rouge - bleu), puis vérifié sur images extraites. Bilans : `archives/phase-2/RAPPORT-bilans-detailles-phase-2.md` (synthèse : `RAPPORT.md`).
1. **Une matière par monde est le principe de couleur le plus répandu du corpus** : dans au moins douze œuvres de toutes familles (*Interstellar*, *Whiplash*, *Mad Max*, *Spider-Verse*, *Aftersun*, *OSS 117*, *Forrest Gump*, HOUDI, Gare du Nord, adidas, « Conte de Noël », KAIZEN). Elle **rend lisibles des plans de 0,5 à 2 s** : on sait où l'on est avant de savoir ce qu'on voit. Le levier n'est pas que la teinte : **format d'image, support et texture** comptent autant (adidas : 4:3 chaud pour la légende, large et froid pour le présent ; *Aftersun* : MiniDV, 35 mm, rave noire, présent froid ; *OSS 117* : N&B pour 1945, nuit américaine bleue).
2. **La couleur forte se mérite et change de place** (*Joker* : rouge presque absent 95 min, annoncé par des lieux de spectacle, puis porté par le corps ; le vert passe au décor). Variantes : la couleur **voyage** sur toute la durée (6G du froid au chaud, STORM se refroidit) ; dans un seul monde, elle **suit l'émotion plan par plan** (*Spider-Verse*, Gwen et son père). Confirme « couleur d'accent = ressource rare » (maquette).
3. **Le monde de référence est le moins coloré** : Brooklyn, monde du héros de *Spider-Verse*, est le moins saturé ; *Spotlight* (saturation 0,26, la plus basse des films en couleur) efface l'image pour rendre l'enquête crédible. Le neutre est un choix, pas une absence.
4. **Une couleur peut ne rien raconter** : *Le Dîner de cons* garde un beige constant ; la comédie de dialogue mise tout sur le jeu. Ne pas exiger une courbe de couleur de chaque film.
5. **La nuit baisse plus qu'elle ne contraste** (*La Haine* : le noir est atteint partout, la nuit descend sans durcir ; *Mad Max* et *OSS 117* : la nuit est un bloc bleu, un monde de plus). Dans les trois, la lumière va à ce qu'il faut voir, ce qui rejoint la règle de nuit de l'utilisateur (rapprochement de ma part).
6. **La marque est une couleur ou un costume dès la première image**, son nom à la fin (sept pubs sur sept) ; un événement à plusieurs équipes se lit par **paquets de couleur** (GP Explorer 3), ce qui manquait à une commande du studio (un signe de couleur par équipe, à prévoir au tournage).
7. **Une rafale tient en une seule couleur** (KAIZEN : l'entraînement en bleu ; Gare du Nord : 65 devantures de face à luminance voisine, conforme au contrôle de photosensibilité).
8. **Le souvenir passe par le support et le format** (maquette, pièce 08) : confirmé par *Aftersun*, adidas et les archives de *Forrest Gump*.
Pièges de mesure : une source HDR lue en SDR donne une image grise et des mesures fausses (vérifier `color_transfer`) ; une planche réduite en palette postérise les aplats saturés : juger la couleur fine sur une image extraite.

## Principes éprouvés en maquette [ÉPROUVÉ EN MAQUETTE]
- **Couleur d'accent = ressource rare** : une seule apparition au moment clé ; répétée, elle devient décor. (pièces 02, 03) **[VU SUR IMAGES]** : *Joker*, Ziak (une seule chaleur sur 0,16 % de l'image, 24 s sur 229).
- **La chaleur se tourne, l'étalonnage la protège** : la matière au décor **et** une clé au grade ; ce que le décor porte, toutes les directions en héritent. **Neutre ≠ froid** : annuler la dominante, ne pas ajouter du bleu. (pièce 05)
- **Le souvenir passe par le support et le format** (4:3, texture caméscope, chaleur modérée) plus que par la couleur ; refuser la date incrustée. (pièce 08) **[VU SUR IMAGES]** : *Aftersun* (MiniDV), adidas (4:3 chaud).
- **Chaleur partout** = « intime » si elle a une source et un dégradé, « filtre » si uniforme. **Un événement froid dans un monde chaud** : gélatiner la source plus bleue que nature ou une clé secondaire, sur une surface neutre ou habitée (main, visage) ; la saillance vient de la luminance. (pièce 10 v4 ; l'hypothèse « AgX blanchit le froid » est réfutée)
- **Le fond est attribué au monde, la lumière au corps** : refroidir le mur isole le personnage, refroidir sa lumière change son corps. Un fond froid réchauffe la peau perçue (logique et piège du teal & orange : pour une peau plus chaude, refroidir le fond). (pièce 13)
- **La température d'une source pratique change la matière** de ce qu'elle touche (peau → plâtre), plus que l'angoisse. (pièce 17)
- **Une lumière qui s'éteint** se lit par la lumière portée qui disparaît ; une courbe qui a une forme, pas un escalier ; un virage de teinte part d'au moins ~25 % de l'intensité finale. (pièce 18 ; capture : `montage-preparation-tournage-vfx`)
- **Blanc ou noir est un ton, pas un style** (tendre → blanc clinique ; funèbre → noir à lumière froide) ; dans le noir, le sujet devient la lumière ; le blanc pur se pose au grade (point blanc), pas au plateau. (pièce 22)
- **Infrarouge** : vert + bruit coloré = surveillance ; monochrome neutre, grain fin, noir ~3 % = intime. (pièce 23)
- **Descente de lumière** : ordonner les plans par leur luminance avant de graduer ; plancher au-dessus du noir, un dernier point vivant. (pièce 25)
- **Lumière, hauteur de caméra, corps** disent chacun une chose ; la transformation se lit quand les trois vont dans le même sens. (pièce 31)

## Méthode : du brief à l'intention couleur
1. **Émotion cible** en 2-3 mots ; sinon demander « à la fin, le spectateur doit se sentir comment ? ».
2. **Courbe** : état de départ → état d'arrivée (sans changement, la retenue compte double).
3. **Couleurs pivots** : une dominante par état ou lieu + un contrepoint, justifiés par le récit.
4. **Curseurs par état** : contraste, saturation, température, place de la peau.
5. **Contraintes** : charte, produit fidèle, diffusion, matière tournée.
6. **Intention** en une demi-page : 2-3 références **précises** (un plan), ce qu'on refuse.
7. **Tester sur 3 plans clés** (début, pic, fin), en mouvement et dans le montage.
8. **Si le client montre un plan de référence** (« je veux la colo de *Seven* ») : le look d'une référence vient d'abord de sa **prise de vue** (contre-jour, valeur du ciel, cadre) ; l'étalonnage rattrape la teinte, pas une densité perdue au tournage [VU SUR IMAGES, David Foxprod, `analyses/methodes/david-foxprod-look-seven.md`]. Le dire avant le tournage ; la méthode d'arbre est dans `montage-resolve` § 2 bis.

### Traduire les mots entendus [THÉORIQUE]
| Mot | Piste |
|---|---|
| « chaud », « humain » | ambre, peaux protégées, noirs légèrement relevés |
| « froid », « clinique » | blancs neutres à bleutés, saturation basse, contraste net |
| « dense », « riche » | noirs profonds, saturation localisée sur la dominante |
| « laiteux », « nostalgique » | noirs relevés, hautes lumières compressées, légère chaleur |
| « poisseux », « malade » | dominante vert-jaune, peaux tirées vers la teinte |
| « ça fait cheap » | trop de teintes, peaux incohérentes, saturation uniforme, lumière sans source |
| « c'est fade » | pas de contrepoint, plutôt qu'un manque de saturation |

## Clichés à refuser (sauf intention explicite) — mon goût (niveau 4)
- **Teal & orange par défaut** : ne dit rien et date l'image ; seulement si chaud / froid porte un sens (dosage et vectorscope : `pipeline.md`).
- LUT « cinématique » plaquée ; désaturer pour faire « sérieux » ; saturer pour faire « joyeux » ; néons rose / cyan sans raison ; noirs relevés « vintage » partout ; une couleur par plan ; étalonner pour sauver un plan sans source crédible.

## Format de sortie (« quelle couleur pour ce film ? »)
1. Émotion et courbe (2 lignes) ; 2. palette avec la raison de chaque couleur ; 3. curseurs par état ; 4. 2-3 références précises ; 5. ce qu'on refuse ; 6. un risque et son test (3 plans).

## Détails des maquettes et des fiches (ancienne annexe `details.md`)

Les pièces numérotées (`atelier/NN-*/CRITIQUE.md`) sont des maquettes Blender / Pillow : principes à confirmer sur de vraies images en phase 2. Tout ce qui suit est [ÉPROUVÉ EN MAQUETTE] sauf mention contraire.

### Accent rare (pièces 02, 03)
Pièce 03 : 1 apparition de la couleur chaude sur la coupure contre 4 en rotation ; pièce 02 : 0,14 % de pixels chauds avant l'allumage.

### Pièce 05 « Trois étalonnages » (`atelier/05-trois-etalonnages/CRITIQUE.md`)
- Mesures : une rouille presque noire ne devient pas « la seule chaleur » au grade (0,1 % de pixels chauds, liseré rouge sur les bords) ; rouille plus claire au décor + secondaire douce = 2 % de chaud, lisible comme matière ; la matière seule ne survit pas à un étalonnage dense (0,4 %).
- **L'étalonnage choisit le registre, le montage donne le sens** : « constat » et « menace » se lisent sur une image fixe ; « souvenir » se lit « brume » tant que rien (montage, voix, son, marqueur de support) ne dit « il y a longtemps ».
- **Une accentuation qui grandit avec le récit** : une clé prise sur la matière fait croître la chaleur à mesure que l'objet est découvert (0,05 % → 0,45 % → 1,7 %).
- Neutre ≠ froid : mesurer le biais R − B du ciel et du sol pour savoir quoi annuler.

### Pièce 08 « Souvenir » (`atelier/08-souvenir/CRITIQUE.md`)
- Le même passé, propre en 16:9, se lit « autre moment de la journée » ; en 4:3 entre barres avec une texture caméscope, « vidéo d'avant » dès la première image.
- Recette de texture : définition ÷ 2 réaccentuée, noirs relevés, bruit de chroma basse fréquence, balance chaude **modérée** (×1,04 / 1,02 / 0,93) ; à ×0,86 sur le bleu, on tombe dans le filtre jaune.
- La date incrustée répond à la question que le souvenir doit laisser ouverte.

### Pièce 10 : un événement froid dans un monde chaud (session 7)
- Chaleur partout « intime » : la source et le dégradé de la maquette étaient une lampe hors champ et des coins sombres.
- v1-v3 : l'événement froid sortait blanc (0 % de pixels froids mesurés). Avec une feuille blanche (v3), il attire l'œil mais sort encore blanc.
- **v4 (12 essais à une seule variable, mesurés dans la zone de l'événement) : la cause n'est pas AgX** (en vue Standard, la feuille sort *plus* chaude) ; c'est (a) une source à 3 cm de la surface, qui sature ou disparaît sans réglage intermédiaire, et (b) une couleur d'écran réaliste trop pâle à côté d'une lampe orangée saturée. L'hypothèse « AgX / une émission intense blanchit le froid » est **réfutée** ; le seul fait mesuré sur AgX est le plafond du blanc (≈ 222/255, `montage-blender`).
- Mesures des remèdes : source gélatinée plus bleue, vue de face, B − R +0,02 → lisible ; clé secondaire sur la zone, +0,10, le plus net.
- v5 : la lumière d'un écran ne se voit que sur les surfaces tournées vers lui ; une plongée qui montre la source cache ce qu'elle éclaire → **deux plans** (la source s'allume / le visage bleuit) : c'est le montage qui fait entrer le froid.
- Règle de méthode : une explication de couleur ne va dans un skill qu'après un essai qui isole la variable.

### Pièce 13 « Le fond raccorde » (`atelier/13-fond-raccorde/CRITIQUE.md`) (perception estimée par modèle, à confirmer)
- Refroidir le mur : la peau ne bouge presque pas (ΔE 1,7, rebond du mur). Refroidir sa lumière : ΔE 6,5 (il pâlit, s'éteint), et faux raccord si l'autre personnage, dans la même pièce, ne change pas.
- Pour « il se ferme » : le monde d'abord (fond, en marches), le corps une seule fois, à la bascule.
- Un décor orange (Joker, intérieur au tungstène) demande une peau protégée ou légèrement poussée, sinon elle paraît livide.

### Fiches : ce que le SKILL.md ne reprend pas
- **Doyle / Wong** : le flou de mouvement montre le temps intérieur.
- **Deakins** : tenir le plan quand la silhouette parle.
- **Willis** (`culture/gordon-willis-le-noir.md`) : les yeux dans le noir = le secret ; le noir n'existe que par opposition (le mariage au soleil) ; direction de la lumière = lecture morale (dessus : masque, dessous : menace, côté bas : confidence). Protéger le noir en post : le **10 bits** est la solution au master, pas de relevage des noirs ; le grain donne une matière au noir mais **n'est pas une protection** à l'encodage : sur une image surtout noire, il consomme le débit et fait pire (`labo/encodage/noir-protege/RESULTATS.md`, `montage-loudness-livraison`) [TESTÉ EN LABO].
- **Young / van Hoytema** (`culture/bradford-young-van-hoytema-lumiere-basse.md`) : dans le noir, éclairer **par rebond** (la source éclaire un objet clair qui éclaire le visage) ; la **température d'une solitude est un jugement** (froid : on la plaint, chaud : on la respecte) ; motiver l'ambiance par le dehors.
- **Braier** (`culture/natasha-braier-lumiere-de-nuit.md`) : une source dans le champ qui ne touche pas le visage = décor lumineux posé sur une image neutre, l'effet « clip » ; réserver la lumière la plus saturée aux rares moments qui la justifient.

### Pièces 17 et 18 : sources pratiques et soustraction
- Pièce 17 (variable isolée : seul l'écran passe du chaud au froid) : chambre → hôpital, peau → plâtre ; la scène ne devient pas plus angoissante.
- Pièce 18 (mesuré à 320 px, `atelier/18-soustraction/CRITIQUE.md`) : éteindre autour du sujet d'abord ; courbe de luminance −29 %, −25 %, puis −75 % au moment montré.
- v4-v5 (rendu Blender ; perception à valider) : la teinte d'un virage se lit sur la **lumière portée** (sol, murs) plus que sur la source vue de face. **Fondu de lumière** : une rampe linéaire en lumière de scène ne descend pas linéairement à l'écran (presque rien la première moitié, tout ensuite) : faire le fondu dans l'espace où il sera jugé, ou le dessiner à l'œil.
- **Recette** : 2 rendus EXR linéaires (avant / après), la différence = la contribution de la source ; toute courbe d'extinction ou de rallumage se compose par addition, puis vue appliquée par OCIO (`atelier/18-soustraction/anime.py`). En compositing (AE 32 bits linéaire, Fusion, Nuke) : une **passe par source** au rendu 3D permet de régler la dramaturgie de la lumière au montage. Au tournage : `montage-preparation-tournage-vfx` §5 ter.

### Pièce 22 v3 : le blanc et le noir comme mondes (rendu Blender ; perception à valider)
- Une silhouette noire sur fond noir disparaît (faute invisible tant qu'on n'a pas fait la variante). Dans le noir, éclairer le sujet seul (une douche motivée) ; un liseré en contre-jour seul donne une présence fantôme, juste pour la fragilité, trop faible pour un sujet principal.
- Exemples : blanc clinique = « tout le monde, calme, hors du temps » (salle d'attente, laboratoire) ; noir à lumière froide = « les morts, l'abîme ». Choisir selon le ton du texte, pas selon la chaîne qu'on imite.
- Blanc pur : AgX plafonne le blanc vers 222/255 [TESTÉ EN LABO] (les autres transformées filmiques, ARRI, ACES, compressent aussi les hautes lumières [THÉORIQUE]) ; le « blanc EGO » (luminance médiane 225+ en plage limitée) se pose avec un point blanc en grade. Mesurer le maximum avant de corriger. Recette : `montage-blender`.

### Pièce 23 : l'infrarouge
Le vert et le bruit coloré à gros grain codent la surveillance même avec une lumière sculptée ; pour l'intime, ajouter une vignette douce ; un noir à 6 % fait un voile laiteux. Le vert reste juste pour le malaise ou le found footage, comme choix. Tournage : `montage-preparation-tournage-vfx/infrarouge.md`.

### Pièce 25 « Au lit » : une descente de lumière (YAVG mesuré)
- Un gradateur de −60 % sur tout le montage ne fait pas descendre l'image si les plans ne sont pas ordonnés (une lampe de chevet à 25 s faisait le pic de la seconde moitié).
- La descente se lit mieux comme **un événement du monde** (les fenêtres de la ville qui s'éteignent une à une) que comme un réglage.
- 20 s à YAVG 19 se lisent « écran éteint ». En v3, la lune **non graduée** sur un ciel qui s'éteint paraît s'allumer : la dernière lumière devient l'image. Un cadre clair qui revient **à la fin** réveille (20 → 32) : placer les retours au milieu de la descente.

### Pièce 31 « Le même escalier » (principe Joker n°3 ; images fixes Blender ; perception à valider)
- Ce que dit chaque levier : lumière = l'heure et la valeur (chaud = désir, froid = isolement), hauteur de caméra = rapport de force, corps = qui a changé. Seul : lumière = « le soir est tombé » ; contre-plongée en froid = menace, pas éclosion (R4b).
- Le contre-jour pur **efface le repère du lieu** (marches à l'ombre) ; contre-jour **rasant et de biais** : il redessine les arêtes ; garder un repère fixe (mât, rampe, fenêtre).
- Le rouge réservé au plan de bascule signe la transformation. Détail : `atelier/31-meme-escalier/CRITIQUE.md`.
