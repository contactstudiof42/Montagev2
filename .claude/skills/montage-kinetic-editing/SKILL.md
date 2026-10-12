---
name: montage-kinetic-editing
description: Montage kinetic / dynamique de format court vertical (Reels, TikTok, Shorts, extraits) — cuts rapides, SFX denses (whoosh, impact, riser, click), speed ramp, punch-in, shake, whip et smash cut, flash, captions mot à mot (Hormozi), hook des 3 premières secondes, photosensibilité. Mots d'un monteur social media : « ça manque de punch », « mets des whoosh », « faut que ça claque », « high retention », « fast-paced », « ça décroche à 3 s », « sound design de Short », « le whoosh arrive en retard ». Vidéo YouTube longue et face caméra : `montage-youtube`.
---

# Kinetic editing (montage social « haute rétention »)

Marqueurs : [SOURCÉ] lu dans une source citée · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu seulement sur maquette Blender / Pillow / ffmpeg · [VU SUR IMAGES] vérifié sur de vraies vidéos (phase 2) · [THÉORIQUE] déduit, non vérifié.

**Statut (2026-10-11, après les sept vidéos réseaux de Diego)** : le corpus contient désormais **sept vidéos réseaux que Diego aime** (`analyses/reseaux/`, 11 à 43 s, « beaucoup de kinétique, mais pas que »), vues image par image avec spectrogramme et calage contre le hasard. Deux sont des kinetic de rafales (captured-by-h, malkimikee), cinq tiennent par les transitions, le look film ou la structure (équipe de France, yungchillyboy, darius, pasalu, Sephora / lucasbosc). Ce qu'elles établissent [VU SUR IMAGES, mesuré] : (1) **le calage à l'image existe dans ce genre** (quatre sur sept, coupe sur l'attaque ou 1 à 2 images avant, jamais après), contrairement à tous les autres formats mesurés ; (2) **les plans éclairs font 2 à 3 images**, pas 4 à 8 ; (3) **aucune n'a de sous-titres mot à mot** ; (4) **aucune ne pose un whoosh sur chaque coupe** : le son des coupes est la musique elle-même ; (5) **toutes respirent** (arrêts de 1,3 à 3,7 s, coupure de musique avant la fin). Restent [SOURCÉ] ou [THÉORIQUE] : le face caméra à captions mot à mot, la densité de SFX entendue (rien n'a été écouté), la rétention.

**Fait foi sur** : la grammaire du format court rapide (durées, SFX et leur hiérarchie, transitions, speed ramp, shake, flash, captions mot à mot, hook 0-3 s) et la photosensibilité des flashs. Pour le jump cut et le punch-in **en face caméra long**, la rétention en minutes : `montage-youtube` ; structure des formats verticaux et Shorts narratifs : `montage-formats` ; tension kinetic contre Ziak : `montage-references`. Leçons d'atelier, recettes complètes et checklist détaillée : `details.md`.

**Goût de l'utilisateur** : il AIME ce style ; ne pas le traiter comme un cliché. Ici **la densité de SFX est le langage** ; l'amateur et le pro se distinguent par **la précision à l'image, la variété, la hiérarchie et les respirations**. « Whoosh sur chaque transition = cliché » vaut pour la pub, le corporate et la fiction ; en kinetic, le cliché c'est le **même** whoosh, au **même** niveau, **en retard**. Contrepoint : Ziak fait l'inverse (`montage-rythme`) ; le kinetic est un choix, pas un réflexe.

## 1. Quand et pourquoi
- Sur un fil, le spectateur décide en 1 à 3 s ; chaque coupe, zoom ou son est une petite interruption d'attention (pattern interrupt), à ne pas confondre avec la **relance** d'une vidéo longue, qui est un coup qualitatif et non une rafale (`montage-youtube` § 18). [SOURCÉ]
- **Le son est le moteur du rythme** : l'œil n'enregistre pas toutes les coupes, l'oreille si (whoosh = vitesse, impact = masse, click = précision). [THÉORIQUE]
- **La vitesse n'est pas le kinetic** : le clip de Ziak coupe plus vite que Mad Max (médiane 1,2 s) sans rien de kinetic (aucune coupe calée, aucun SFX, aucun effet). Ce qui fait le kinetic, c'est la synchronisation et le surlignage (SFX, punch-in, flash sur le temps), pas la durée des plans. [VU SUR IMAGES] (`analyses/clips/ziak-meme-pas-un-grincement.md`)
- **Respiration obligatoire** : accélérer puis relâcher, un trou de silence avant le gros impact, au moins un plan tenu par séquence de 5 à 8 s. **[VU SUR IMAGES] sur les sept vidéos réseaux** : captured-by-h alterne rafales de 2 images et arrêts de 1,3 à 2,3 s et finit 1,9 s dans le silence ; l'équipe de France coupe la musique 0,3 s avant un impact (15,9 s) et 10 s sous ses affiches ; darius coupe la musique 3,7 s avant le logo. **Un arrêt n'est pas immobile** : il porte une apparition ou une transformation (corps qui apparaissent, encre qui s'étend, passage en négatif). Vérifié à l'échelle d'un long métrage : *Mad Max: Fury Road* alterne crêtes à 30-40 coupes/min et creux à 4-10, et garde des plans tenus (7 s) au milieu de la poursuite finale. Pour que des plans de 1 à 2 s se lisent : **sujet au centre** (environ 20 images sur 24 au tiers central, contre 8 sur 24 pour Joker), **un plan de géographie toutes les 5 à 10 coupes**, **une couleur par lieu**. [VU SUR IMAGES] (`analyses/films/mad-max-fury-road.md`)
- **Quand ce style dessert** : deuil, témoignage intime, sujet grave, luxe lent, schéma à lire, humour de silence ; et **quand le sujet porte son propre tempo qui évolue** (balancier qui s'amortit, respiration qui ralentit) : la pulsation constante l'écrase ; couper sur les points morts de plus en plus espacés. [ÉPROUVÉ EN MAQUETTE] (pièce 14) Sinon : garder la précision, diviser la densité par 3.
- **Chaque séquence a sa règle** (point de vue, échelle, cadence), écrite en une ligne avant de monter (*Scott Pilgrim*) ; **caler d'abord, salir ensuite**. [SOURCÉ]

## 2. Grammaire
### Durées (à 30 i/s ; × 0,83 à 25 i/s) [THÉORIQUE : repères d'éditeurs ; première ligne corrigée sur images]
| Usage | Images | Secondes |
|---|---|---|
| **Plan éclair d'une rafale (vu)** | **2-3** | 0,07-0,10 (médiane de captured-by-h et malkimikee) |
| Plan éclair lisible, liste de mèmes | 4-8 | 0,13-0,27 |
| B-roll, plan de rythme | 8-20 | 0,3-0,7 |
| Phrase face caméra entre deux jump cuts | 30-90 | 1-3 |
| Respiration / chute / réaction | 45-120 | 1,5-4 |

### Coupes et effets
- **Jump cut** : retirer silences et hésitations ; changer d'échelle seulement là où l'on veut l'emphase (sinon le punch-in tombe au hasard) ; éviter les micro-sauts nés de respirations coupées. Fait foi : `montage-youtube` §5.
- **Punch-in** : zoom brusque (2-3 images) sur le mot-clé, **ease-out** et flou de bougé ; en linéaire, c'est mou. [ÉPROUVÉ EN MAQUETTE]
- **Smash cut** : coupe sèche d'un calme à un fort, souvent après un silence.
- **Whip / speed ramp** : rampe en cloche (100 → 400 % fin de A, 400 → 100 % début de B, Bézier), flou de bougé, whoosh à crête sur la coupe. [THÉORIQUE] Un plan 3D qui coupe en mouvement s'anime **au-delà de ses bords**, sinon la coupe accroche sur deux images nettes. [TESTÉ EN LABO] (`labo/kinetic/whip/`)
- **Direction du filé** : raccord si elle se prolonge à 30° près ; sens inverse = choc (à réserver à l'impact) ; perpendiculaire = changement d'espace ; pas de rayures ni de stores dans un filé. Mesure [TESTÉ EN LABO], perception [ÉPROUVÉ EN MAQUETTE] (`labo/kinetic/whip-flot/`).
- **Transition invisible** : il faut un **point commun aux deux plans** (direction et vitesse du mouvement, texture, couleur), idéalement tourné, sinon trouvé au banc ou fabriqué en post ; sans point commun, aucun effet ne la sauve. [SOURCÉ] (Kolder, Schiffer, Brandon Li). Ordre de jugement : attention, émotion, puis technique ; une transition-signature appliquée à tout devient un preset.
- **Camera shake** : sur l'impact seulement, amorti en 4 à 6 images. **Flash blanc** : 1 image (2 max). [ÉPROUVÉ EN MAQUETTE]
- **Masque de transition** : un objet qui passe devant l'objectif cache la coupe.
- **Le kinetic de Diego en réseaux (dicté le 2026-10-11, `GOUTS.md`)** : « un mélange des deux » : le calage à l'image, les transitions variées, le look film et la respiration de ses références **et** l'énergie à SFX et effets du kinetic classique. Sous-titres seulement si le client les demande (Sony : « que du visuel »). La vitesse est réservée au kinetic ; ses films de référence tiennent par la structure.
- **Goût de l'utilisateur (2026-10-10)** : transitions tournées **et** coupes sèches avec impact, « varier les plaisirs » ; un edit qui n'utilise qu'une famille de transitions devient un tic. **[VU SUR IMAGES]** sur ses références réseaux : Sephora / lucasbosc enchaîne cinq familles en 15 s sans en répéter une (rotation, ballon dans l'objectif qui ressort en produit, volet, changement de décor, poussée en flou radial) ; pasalu (flash de surexposition, filé, iris, double exposition, écran partagé) ; yungchillyboy (volet en bande, petits rectangles qui découvrent le plan suivant, négatif).
- **Effets vus sur ses références** [VU SUR IMAGES] : **inversion positif / négatif** de 1 à 3 images comme flash sans nouvelle image (captured-by-h, plus de 15 fois ; darius, yungchillyboy) ; **image noire de 1 à 3 images** comme ponctuation dans une rafale (malkimikee) ; **saut de temps dans un même plan** toutes les 5 images sur la pulsation (équipe de France, 33-34,4 s) ; **déclinaison d'une image** en variantes (négatif, teinte plate, grille) pour faire une rafale ; **un motif graphique décliné** sur tout le film (la mosaïque de l'équipe de France : ouverture, action en tuiles, regards en bandes) ; **refrain visuel** (même rafale de textures à 5,2 et 10,2 s chez malkimikee).
- **Projet Sony, comparaison avec Claude nu (2026-10-11)** [TESTÉ EN CONDITIONS RÉELLES] : sur un brief « kinetic, très rapide, beaucoup d'effets et de SFX », ma V2 (68 plans, 6 flashs, 19 SFX, 4 punch-ins) a été jugée trop sage ; un Claude sans formation (83 plans dont 15 coupés par un saut de zoom, environ 60 flashs, 55 SFX, 30 impacts de zoom avec flou de bougé, accélérés à 150-200 %, 3 arrêts sur image détourés) plus impressionnant, « effets mieux posés ». **Le brief prime sur la retenue des références** : j'ose d'abord, je nettoie ensuite. Ce que Diego a aimé chez moi : **la rafale très rapide avec flashs** (vers 15 s) ; elle doit **revenir à chaque phrase musicale**, sans devenir toute la vidéo (contraste rafale / plan tenu). Recettes Resolve : `montage-resolve` § 4 quinquies.
- **Transitions interdites** [universel, règle maître dans `montage-regard`, « Juger sa propre version » 5] : jamais de transitions intégrées de type glissement, poussée ou volet (« PowerPoint », Diego), sauf parodie demandée par le brief. À la place : coupe franche, flash, whip avec flou de mouvement, raccord de mouvement, zoom qui traverse.
- **Captions** : le style (mot sec, pop, karaoké) dépend du client ; savoir faire les trois. **Aucune des sept références réseaux de Diego n'a de sous-titres mot à mot** [VU SUR IMAGES] : texte rare, mots seuls posés sur les plus forts accents (malkimikee : « EIFFEL » 3,47 s, « TOWER » 3,90 s, « PARIS » 4,57 s sur l'attaque), titres en serif fin (darius, équipe de France), claim peint dans le décor (Sephora « FOR 24H » sur la pelouse). Le mot à mot reste une demande de client pour le face caméra. **Mot à mot** : majuscules grasses, 1 à 4 mots, mot-clé en couleur ou agrandi, apparition sur la syllabe, zone sûre (hors 15 % du bas et interface droite). [SOURCÉ] Lisibilité après ré-encode, vue à 360 px : plancher **2 % de la hauteur en graisse Medium**, Thin illisible jusqu'à 2 %, sur fond clair et chargé **boîte ≈ 85 % dès 2,6 %** ; l'ombre portée n'aide jamais. [ÉPROUVÉ EN MAQUETTE] (proxy OCR, `labo/paroles/`)
- **Tenir le vers** 1/2 s à 1 s après le dernier mot : tenue = max(0, caractères / 15 − (mots − 1) × 0,3) (`labo/paroles/temps_lecture.py`). [TESTÉ EN LABO] (calcul sur normes [SOURCÉ] : ATAA 14-15 car./s, Netflix FR 17)
- **B-roll / mèmes** : illustrer le mot au moment où il est dit.

### SFX : hiérarchie (du plus fort au plus discret)
| Rang | SFX | Sert à | Placement |
|---|---|---|---|
| 1 | Impact / hit (sub + transitoire) | LA révélation, le chiffre | attaque **sur** la 1re image du plan |
| 2 | Riser / reverse | l'attente | crête sur la coupe ou coupé 1 image avant l'impact |
| 3 | Whoosh / swish | vitesse | début 3-6 images AVANT, crête SUR la coupe |
| 4 | Pop / click / UI | précision (texte, icône) | sur l'image d'apparition |
| 5 | Glitch, scratch, mème | rupture comique | ponctuel |
| 6 | Foley, ambiance | liant | continu, très bas |
Crête sur le moment clé [SOURCÉ] (Epidemic Sound, Morphic) ; la fourchette 3-6 images vient du labo [TESTÉ EN LABO pour le calage, THÉORIQUE pour le ressenti].

**Calage de la coupe sur la musique, mesuré sur les références de Diego** [mesuré, musique séparée par demucs, contre le hasard ; écart signé coupe / attaque la plus proche] :
| Vidéo | Coupes à ±1 image d'une attaque forte | Hasard (95e centile) | Écart médian |
|---|---|---|---|
| pasalu (musique clairsemée) | 53 % | 24 % (42 %) | +0,1 image |
| équipe de France | 45 % | 19 % (34 %) | +0,3 image |
| darius | 40 % | 26 % (38 %) | 0,0 image |
| yungchillyboy | 9 % à ±1, **74 % à ±2** | 33 % à ±2 (61 %) | **la coupe précède l'attaque de 1 à 2 images** (17 coupes sur 17 après 3,4 s) |
| malkimikee, captured-by-h | 16 % | 18-20 % | rafales non calées ; seuls les mots et les arrêts tombent sur les plus fortes attaques |
Règle qui en sort : **quand la coupe suit la musique, elle tombe sur l'attaque ou 1 à 2 images avant, jamais après** ; elle suit les **attaques** (notes, coups) plus que la grille des temps ; dans une rafale de 2 images, on ne cale plus rien, on cale les **événements** (mot, arrêt, image finale). La chaîne de mesure est la même pour toutes (pasalu à +0,1) : l'avance de yungchillyboy est dans le montage.

**Le son des références réseaux** [VU SUR SPECTROGRAMME, non écouté] : pas de whoosh sur chaque coupe ; les sons sur les coupes sont ceux de la musique. SFX repérés : **riser de 6 s jusqu'au drop sur le logo** (équipe de France), impacts et glitchs sous la rafale d'ouverture (captured-by-h), un balayage sous un titre (Sephora), un souffle avant une double exposition (pasalu), **un son du lieu comme légende** (annonce RATP « Bir-Hakeim, Tour Eiffel » sur le plan du métro, malkimikee), une voix de compte à rebours dans le silence avant le logo (darius).

Règles : un seul rang 1 par 5-10 s ; whoosh variés (3-5 variantes, **varier les durées avant les timbres**, longueur = longueur du mouvement, -10 à -14 dB sous l'impact) ; toutes les coupes n'ont pas de son ; **chaque SFX a une cause visible** et amplifie un événement qui existe [ÉPROUVÉ EN MAQUETTE] (pièce 02) ; voix intelligible (SFX baissés sous les consonnes, creux 1-4 kHz dans les whoosh) ; impacts sur les downbeats.

**Onomatopée graphique plein cadre (rang 5 en image)** : une par chute, toutes les 6-7 s, elle peut devenir le nom de la campagne (Swile « POW », projet du studio : « POW ! » en 3D magenta qui clôt chaque sketch, revient dans le bandeau du faux numéro et nomme le produit fictif P.O.W.). [VU SUR IMAGES] (`analyses/projets-f42/swile-pow.md`)

## 3. Ce qui sépare le pro de l'amateur
| Amateur | Pro |
|---|---|
| Whoosh après la coupe | Whoosh qui anticipe, crête sur la coupe |
| Même sample, même niveau | Variantes, hiérarchie impact > riser > whoosh > click > foley |
| Densité constante (« mur ») | Accélérations, relâchements, silences |
| Shake et zoom en continu | Effet = événement, amorti en 4-6 images |
| Plan qui commence dans le noir ou vide | Sujet lisible **dès la 1re image** (pièce 02 : 4 plans noirs sur 19) |
| Plans sans lien qui accélèrent (défilé) | Chaque plan montre une cause de l'événement final (une montée) [ÉPROUVÉ EN MAQUETTE] |
| Rafale-inventaire où chaque plan doit se lire | **Clignotement** de dizaines d'images de même cadre à 2 images chacune (une matière, pas une lecture), ponctué de 5-6 arrêts de 0,3-0,7 s qui seuls se lisent, puis un plan tenu (Yvnnis « Gare du Nord », 1:34-1:42 puis 13,3 s) [VU SUR IMAGES, chaque image] |
| Rafale « montage-souvenir » sans structure | Rafale en strophes portée par un refrain de voix off (*Across the Spider-Verse*, 1:22-2:44 : environ 130 plans de 0,2-1,5 s, moyenne 0,63 s, recomptés image par image en révision, sous « And he's not the only one » ×4 ; calage sur les temps = hasard) [VU SUR IMAGES, mesuré] |
| SFX qui font le niveau | Voix d'abord, -14 LUFS mesuré sur le fichier encodé |
| Coupe posée « à peu près » sur le temps | Coupe sur l'attaque à l'image, ou 1 à 2 images avant ; jamais après (pasalu, équipe de France, darius, yungchillyboy) [mesuré] |
| Une seule famille de transitions | Une famille par temps du film, jamais répétée dans un 15 s (Sephora / lucasbosc) [VU SUR IMAGES] |

## 4. Recettes (code complet : `details.md`)
- **R1 Hook 0-3 s** [THÉORIQUE pour la recette ; corrigé sur images] : quelque chose de lisible avant 1 s, mais **quatre formes vues** sur les références de Diego : (a) **bande-annonce de 0,5 s** (5 à 7 éclats de 1 à 3 images tirés de la suite, yungchillyboy) ou rafale d'ouverture (captured-by-h, malkimikee) ; (b) un visage connu (Sephora) ; (c) une phrase de coulisses en face caméra (darius) ; (d) une construction sous la voix, **drop retardé à 6 s** sur l'image la plus forte (équipe de France). « Image 1 = la plus forte + impact » n'est qu'une des quatre.
- **R2 Montée vers une révélation** [ÉPROUVÉ EN MAQUETTE] : plans 15 → 13 → 12 → 10 → 8 → 6 images ; riser coupé 1 image avant ; coupe sèche ; impact + flash 1 image + shake 5 images ; plan tenu ≥ 15 images.
- **R3 Punch-in** : 2 images larges puis ×1,35 en 3 images ease-out (`zoompan`). **R4 Shake + flash** (`crop` amorti + `drawbox`). [TESTÉ EN LABO pour la recette]
- **R5 Caler un SFX en script** [TESTÉ EN LABO] : échantillon = image × (fréquence / cadence), soit 1600 à 48 kHz / 30 i/s.
- **R6 Loudness d'un mix chargé** [TESTÉ EN LABO] : ebur128 → gain → limiteur sur-échantillonné → re-mesurer ; l'AAC remonte le true peak (+1,9 dB) : limiteur à -3 dBFS avant encodage ; résultat -14,3 LUFS / -1,1 dBTP (`montage-loudness-livraison`).
- **R7 Captions** : pop d'échelle 125 → 100 % sur la 1re image, click -20 dB sur les mots-clés seulement.

## 4 bis. Bibliothèque de techniques : eyecannndy.com (lue le 2026-10-11, demandé par Diego)
_https://eyecannndy.com/technique/… : chaque technique illustrée par des GIF. Lu : 56 pages ; GIF regardés pour Infinite Zoom, Flash Cut, Echo print, Match Cut [VU SUR IMAGES], le reste d'après définitions [NON VÉRIFIÉ]. Règle de Diego : **jamais cheap** ; un effet seulement si la matière le permet et s'il s'exécute proprement. Varier la technique d'une rafale à l'autre, chacune avec une raison dans la matière._

| Technique (page) | Ce qui la rend propre | Matière nécessaire | Resolve par script |
|---|---|---|---|
| **Flash cut aligné** (`flash-cut`) | rafale de 2-4 images où **seul le sujet change, cadre et point focal strictement identiques** (le verrou d'alignement fait l'effet) | plusieurs plans de même échelle sur le même objet (oreilles, boîtiers, lettres) | facile : recadrage `Transform` calé sur le centre mesuré de l'objet |
| **Match cut de forme / de mouvement** (`match-cut`, `match-motion`) | la forme ou le mouvement continue au même endroit, au même angle | une forme commune (rond de l'écouteur ↔ O), un mouvement dans la même direction | facile : alignement mesuré |
| **Zoom infini** (`zoom-in#infinite-zoom`) | échelle continue qui accélère régulièrement, aucun à-coup ; **pas le flou « CapCut » qui laisse voir le plan suivant** | un détail du plan A qui est exactement le plan B (même objet à deux échelles, plans stables, 4K pour ×2) | possible avec soin : `Transform` chaînés, échelle exponentielle, raccord au point d'échelle égale |
| **Crash zoom / cut-in** (`zoom-in#crash-zoom`, `cut-ins`) | 4-8 images, flou de bougé, coupe au maximum de vitesse ; cut-in = recadrage plus serré du même plan | sujet net et centré, source 4K | facile |
| **Speed ramp** (`speed-ramping`) | ralenti posé sur l'instant clé du geste | 50p ou plus, un geste qui a un sommet | possible avec soin (`TimeSpeed` + clés ; l'interpolation abîme mains et câbles) |
| **Step-print / echo print** (`step-printing`, `echo-printing`) | saccade traînante (Chungking Express) ou copies qui s'éventaillent sur fond uni | sujet qui bouge, caméra quasi fixe, fond sombre | facile (`Trails`, `TimeSpeed` + `floor`) ; cheap si la caméra bouge (tout bave) |
| **Color shift + light flash** (`color-shift`, `light-flash`) | la bascule de couleur vient du tournage ; flash d'1-2 images motivé par une lumière | une bascule réelle (le passage au rouge) | facile |
| **Split screen / match split** (`split-screen`) | bandes de même échelle qui composent une seule image | même échelle, même horizon | facile (`Merge` + masques `Rectangle`) |
| **Arrêt sur image** (`freeze-frame`) + **collage** | rare ; dans un collage, l'arrêt porte une transformation puis **le mouvement reprend** (captured-by-h, choix de Diego) | une image nette, une pose lisible | facile ; détourage soigné sur l'image figée |
| Double exposition, masques, portail d'objet | possible si la forme est forte | silhouette sur fond sombre, objet qui remplit le cadre | possible avec soin (pas de Magic Mask scriptable) |
| Slit-scan | lourd | caméra fixe, mouvement régulier | difficile, plutôt hors de Resolve |
| **Exécutées dans la V4 Sony (2026-10-11)** : zoom infini E → KORE (SIFT), flash cut des oreilles (échelle en crescendo, variante), rafale qui monte (mouvements vers le haut, 300 %), step-print qui descend (`floor(time/4)*4`), écran partagé en 3 bandes, inversions d'une image dans le rouge (LUT négative), 3 collages sur arrêt (orange + cerne, papier millimétré, photo sur image inversée) | | | |
| **À écarter** : stutter et boomerang (répètent un même moment : interdit dans un événementiel), datamosh (pas premium), kaléidoscope (cheap) | | | |

### SFX : varier comme les effets (note de Diego sur la V3 : « SFX un peu répétitifs ») [TESTÉ EN CONDITIONS RÉELLES 2026-10-11, non écouté]
- **Une famille de sons par technique visuelle** : tics de verre qui montent (flash cut), bégaiement + riser aspiré (rafale qui monte), armement d'appareil argentique (step-print), papier / scratch / Polaroid (collages), sangles et câbles (écran partagé), glitch (inversions), néon (bascule de lumière), whoosh tonal (packshot). Jamais deux fois le même son à la suite.
- **Variantes de hauteur** pour un son répété (montée d'un demi-ton à un ton par occurrence, `asetrate` à la vraie fréquence d'échantillonnage du fichier, ou `AudioPitchSemiTones` dans Resolve).
- **Crête calée sur l'image** de l'événement (`labo/outils/phase3/v4/sfx_prep.py` → `crete.json`, `partition_sfx.py`).

### Genre « after movie / événementiel kinetic » : notes de Diego sur la V4 Sony (2026-10-11) [genre : after movie kinetic] [TESTÉ EN CONDITIONS RÉELLES, non écouté]
- **Un son sur chaque transition, ou aucun** : dans ce genre, mélanger des transitions sonorisées et des transitions muettes se lit comme un oubli. **Définition validée par Diego (V5) : une transition est un effet ou un changement de bloc ; les coupes franches à l'intérieur d'un bloc n'ont pas de son à elles.** C'est ce qui réconcilie cette règle avec « toutes les coupes n'ont pas de son » (§ 2) et avec les références de Diego, où le son des coupes est la musique. Sur Sony : toutes, chacune avec un son qui lui correspond (contrôle : liste des transitions de la timeline contre la liste des SFX, 0 transition muette). Portée précisée par Diego : [genre : kinetic] et environ 80 % des after movies. **Contre-indication** : les films où le son des coupes est la musique elle-même (plusieurs références réseaux de Diego : lucasbosc, pasalu, darius), les films de marque calmes, l'interview.
- **Les inversions d'image changent des flashs** : « tu peux en faire un peu plus » (en alternance avec les flashs blancs, dans la limite de photosensibilité). **Contre-indication** : luxe, beauté douce, corporate.
- **Le collage ou le détourage doit préparer le plan suivant** (piste de Diego : sujet détouré, le plan suivant se glisse derrière, puis elle disparaît par un glitch) ; fond et matière tirés de la DA (`da.md`), jamais d'une bibliothèque d'idées.
- **Un dernier pic d'énergie juste avant la signature de marque, puis une fin courte et propre** (Diego, V4 : « après tout le déferlement d'effets, ça s'arrête trop longtemps ») : 4-5 s très accélérées, de gros effets tirés de la matière et de la DA, puis des packshots sobres. **Contre-indication** : film de marque calme, portrait, documentaire, où la respiration avant la fin est juste.
- **Faire le dernier pic** [genre : after movie kinetic] [TESTÉ EN CONDITIONS RÉELLES 2026-10-11, V5 Sony, référence foebusdelapaz] : changer l'**état** de l'image (naturel, noir et blanc, négatif, seuil) autant que le plan ; une respiration tenue au milieu (un héros en noir et blanc, pas un écho : l'écho d'un plan à la main voile toute l'image) ; les grands changements sur les attaques fortes mesurées de la musique, les micro-coupes libres. Photosensibilité : le stroboscope d'états se règle **à l'image près** (`flash_check.py --detail` donne les images) : un négatif ou un seuil sur une image sombre = un flash ; sur une image claire, un noir et blanc qui assombrit (gamma) en est un aussi : **noir et blanc à luminance conservée**. Un négatif par seconde dans un stroboscope, pas trois.
- **Le traitement est un montage** (foebusdelapaz, kinetic de basket, 3,17-3,71 s) [VU SUR IMAGES] : une rafale peut changer d'**état** sans changer de plan (naturel, duotone, seuil, négatif, flash blanc, une image chacun) ; révélation par seuil de luminance (une image par palier) ; écho et traînées du geste en noir et blanc après le pic ; deux plans tenus de 14-15 images au milieu ; les changements de bloc sur les attaques les plus fortes, les micro-coupes libres. Les états se prennent dans la palette de la DA du film. Fiche : `analyses/reseaux/foebusdelapaz-nike-basket.md`.
- La table ci-dessus est un **répertoire, pas une liste à remplir** : une technique n'entre que si le genre, la DA et la matière la demandent (`PROMPT-PHASE-3.md`, « La portée d'une règle »).

## 5. Photosensibilité (obligatoire dès qu'il y a flash ou strobe) [TESTÉ EN LABO]
- **Les sept références réseaux de Diego échouent toutes à `flash_check.py`** (pire seconde 4 à 6), y compris la pub Sephora qui n'a aucun flash visible : l'outil simplifié compte sans doute les coupes entre plans de luminances très différentes. Conséquence : ce genre ne respecte pas le seuil WCAG ; pour une diffusion qui l'exige (TV, pub UK), mesurer et adapter ; l'outil reste à confronter à un vrai test Harding avant de juger une coupe ordinaire. [mesuré, doute sur l'outil]
- `python3 -I labo/photosensibilite/flash_check.py rendu.mp4` ; > 3 flashs dans une seconde = refus (WCAG 2.3.1, BT.1702) ; un flash d'1 image compte entier ; surface jugée dans la pire fenêtre de 1/3 × 1/3 de l'écran. Pub UK : test Harding.
- À ~140 BPM : **une transition de luminance par croche au plus** ; un coup par noire à 128 BPM tombe pile sur la limite (pire seconde 3).
- Strobe sûr : changer **teinte et forme à luminance égale** (Noé / Kan) ; baisser la luminosité du texte ne sert à rien, les leviers sont la surface et la fréquence. [ÉPROUVÉ EN MAQUETTE] (pièce 09) **[VU SUR IMAGES, mesuré]** sur Yvnnis « Gare du Nord » (1:33,7-1:41,8) : environ 65 devantures de 2 images chacune (12,5 changements par seconde), cadrées de face, de luminances voisines : pire seconde 2 flashs, conforme.
- **Le sommet plus long, pas plus fort** : un coup clair tenu 8 images reste un seul flash et pèse plus. [ÉPROUVÉ EN MAQUETTE] (pièce 20)
- Rushes avec stroboscope : mesurer chaque plan ; seul le tirage par saccade (image tenue ≥ 8 images à 25 i/s) garde le coup et passe toujours. Détail : `details.md`.

## 6. Checklist avant livraison
- [ ] Planche « 1re image de chaque plan » : chaque vignette se lit seule.
- [ ] Image 1 et son 1 accrochent ; promesse avant 3 s.
- [ ] Whoosh avant la coupe, crête dessus ; impacts sur l'image (vérifié image par image).
- [ ] Au plus un rang 1 par 5-10 s ; au moins un plan tenu par séquence de 5 à 8 s (§ 1).
- [ ] Shake ≤ 6 images, flash ≤ 2 images, `flash_check.py` passé.
- [ ] Captions : zone sûre, 1-4 mots, orthographe, mot-clé marqué.
- [ ] Voix intelligible sur haut-parleur de téléphone ; -14 LUFS ±0,5 / ≤ -1 dBTP mesurés sur le MP4.
- [ ] Le style sert le sujet (sinon densité ÷ 3).

## 7. Outils, phases 2 et 3
Premiere (Time Remapping, captions sur transcription, Essential Sound), After Effects (`wiggle` amorti, motion blur : `montage-after-effects`), CapCut, Resolve ; SFX : Sonniss GDC, Mixkit (lire les licences). Non vérifié (les sept références réseaux n'ont pas été écoutées) : calage du whoosh 3-6 images à l'oreille, densité réelle des SFX, rétention réelle de deux densités, face caméra à captions mot à mot ; en phase 3 (logiciels) : décalage AAC réel, captions auto de Premiere, speed ramp Premiere contre AE. Labo : `labo/kinetic/` ; sources : `sources/kinetic-editing.md`.
