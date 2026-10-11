---
name: montage-kinetic-editing
description: Montage kinetic / dynamique de format court vertical (Reels, TikTok, Shorts, extraits) — cuts rapides, SFX denses (whoosh, impact, riser, click), speed ramp, punch-in, shake, whip et smash cut, flash, captions mot à mot (Hormozi), hook des 3 premières secondes, photosensibilité. Mots d'un monteur social media : « ça manque de punch », « mets des whoosh », « faut que ça claque », « high retention », « fast-paced », « ça décroche à 3 s », « sound design de Short », « le whoosh arrive en retard ». Vidéo YouTube longue et face caméra : `montage-youtube`.
---

# Kinetic editing (montage social « haute rétention »)

Marqueurs : [SOURCÉ] lu dans une source citée · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu seulement sur maquette Blender / Pillow / ffmpeg, hypothèse à confirmer en phase 2 · [THÉORIQUE] déduit, non vérifié.

**Fait foi sur** : la grammaire du format court rapide (durées, SFX et leur hiérarchie, transitions, speed ramp, shake, flash, captions mot à mot, hook 0-3 s) et la photosensibilité des flashs. Pour le jump cut et le punch-in **en face caméra long**, la rétention en minutes : `montage-youtube` ; structure des formats verticaux et Shorts narratifs : `montage-formats` ; tension kinetic contre Ziak : `montage-references`. Leçons d'atelier, recettes complètes et checklist détaillée : `details.md`.

**Goût de l'utilisateur** : il AIME ce style ; ne pas le traiter comme un cliché. Ici **la densité de SFX est le langage** ; l'amateur et le pro se distinguent par **la précision à l'image, la variété, la hiérarchie et les respirations**. « Whoosh sur chaque transition = cliché » vaut pour la pub, le corporate et la fiction ; en kinetic, le cliché c'est le **même** whoosh, au **même** niveau, **en retard**. Contrepoint : Ziak fait l'inverse (`montage-rythme`) ; le kinetic est un choix, pas un réflexe.

## 1. Quand et pourquoi
- Sur un fil, le spectateur décide en 1 à 3 s ; chaque coupe, zoom ou son est une petite interruption d'attention (pattern interrupt), à ne pas confondre avec la **relance** d'une vidéo longue, qui est un coup qualitatif et non une rafale (`montage-youtube` § 18). [SOURCÉ]
- **Le son est le moteur du rythme** : l'œil n'enregistre pas toutes les coupes, l'oreille si (whoosh = vitesse, impact = masse, click = précision). [THÉORIQUE]
- **La vitesse n'est pas le kinetic** : le clip de Ziak coupe plus vite que Mad Max (médiane 1,2 s) sans rien de kinetic (aucune coupe calée, aucun SFX, aucun effet). Ce qui fait le kinetic, c'est la synchronisation et le surlignage (SFX, punch-in, flash sur le temps), pas la durée des plans. [VU SUR IMAGES] (`analyses/clips/ziak-meme-pas-un-grincement.md`)
- **Respiration obligatoire** : accélérer puis relâcher, un trou de silence avant le gros impact, au moins un plan tenu par séquence de 5 à 8 s. [ÉPROUVÉ EN MAQUETTE] Vérifié à l'échelle d'un long métrage : *Mad Max: Fury Road* alterne crêtes à 30-40 coupes/min et creux à 4-10, et garde des plans tenus (7 s) au milieu de la poursuite finale. Pour que des plans de 1 à 2 s se lisent : **sujet au centre** (environ 20 images sur 24 au tiers central, contre 8 sur 24 pour Joker), **un plan de géographie toutes les 5 à 10 coupes**, **une couleur par lieu**. [VU SUR IMAGES] (`analyses/films/mad-max-fury-road.md`)
- **Quand ce style dessert** : deuil, témoignage intime, sujet grave, luxe lent, schéma à lire, humour de silence ; et **quand le sujet porte son propre tempo qui évolue** (balancier qui s'amortit, respiration qui ralentit) : la pulsation constante l'écrase ; couper sur les points morts de plus en plus espacés. [ÉPROUVÉ EN MAQUETTE] (pièce 14) Sinon : garder la précision, diviser la densité par 3.
- **Chaque séquence a sa règle** (point de vue, échelle, cadence), écrite en une ligne avant de monter (*Scott Pilgrim*) ; **caler d'abord, salir ensuite**. [SOURCÉ]

## 2. Grammaire
### Durées (à 30 i/s ; × 0,83 à 25 i/s) [THÉORIQUE : repères d'éditeurs, à confronter aux statistiques du compte]
| Usage | Images | Secondes |
|---|---|---|
| Plan éclair, liste de mèmes | 4-8 | 0,13-0,27 |
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
- **Goût de l'utilisateur (2026-10-10)** : transitions tournées **et** coupes sèches avec impact, « varier les plaisirs » ; un edit qui n'utilise qu'une famille de transitions devient un tic.
- **Captions** : le style (mot sec, pop, karaoké) dépend du client ; savoir faire les trois. **Mot à mot** : majuscules grasses, 1 à 4 mots, mot-clé en couleur ou agrandi, apparition sur la syllabe, zone sûre (hors 15 % du bas et interface droite). [SOURCÉ] Lisibilité après ré-encode, vue à 360 px : plancher **2 % de la hauteur en graisse Medium**, Thin illisible jusqu'à 2 %, sur fond clair et chargé **boîte ≈ 85 % dès 2,6 %** ; l'ombre portée n'aide jamais. [ÉPROUVÉ EN MAQUETTE] (proxy OCR, `labo/paroles/`)
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

Règles : un seul rang 1 par 5-10 s ; whoosh variés (3-5 variantes, **varier les durées avant les timbres**, longueur = longueur du mouvement, -10 à -14 dB sous l'impact) ; toutes les coupes n'ont pas de son ; **chaque SFX a une cause visible** et amplifie un événement qui existe [ÉPROUVÉ EN MAQUETTE] (pièce 02) ; voix intelligible (SFX baissés sous les consonnes, creux 1-4 kHz dans les whoosh) ; impacts sur les downbeats.

## 3. Ce qui sépare le pro de l'amateur
| Amateur | Pro |
|---|---|
| Whoosh après la coupe | Whoosh qui anticipe, crête sur la coupe |
| Même sample, même niveau | Variantes, hiérarchie impact > riser > whoosh > click > foley |
| Densité constante (« mur ») | Accélérations, relâchements, silences |
| Shake et zoom en continu | Effet = événement, amorti en 4-6 images |
| Plan qui commence dans le noir ou vide | Sujet lisible **dès la 1re image** (pièce 02 : 4 plans noirs sur 19) |
| Plans sans lien qui accélèrent (défilé) | Chaque plan montre une cause de l'événement final (une montée) [ÉPROUVÉ EN MAQUETTE] |
| SFX qui font le niveau | Voix d'abord, -14 LUFS mesuré sur le fichier encodé |

## 4. Recettes (code complet : `details.md`)
- **R1 Hook 0-3 s** [THÉORIQUE] : image 1 = la plus forte + impact ou drop ; captions dès la 1re syllabe ; 2-4 coupes ; promesse dite avant 3 s.
- **R2 Montée vers une révélation** [ÉPROUVÉ EN MAQUETTE] : plans 15 → 13 → 12 → 10 → 8 → 6 images ; riser coupé 1 image avant ; coupe sèche ; impact + flash 1 image + shake 5 images ; plan tenu ≥ 15 images.
- **R3 Punch-in** : 2 images larges puis ×1,35 en 3 images ease-out (`zoompan`). **R4 Shake + flash** (`crop` amorti + `drawbox`). [TESTÉ EN LABO pour la recette]
- **R5 Caler un SFX en script** [TESTÉ EN LABO] : échantillon = image × (fréquence / cadence), soit 1600 à 48 kHz / 30 i/s.
- **R6 Loudness d'un mix chargé** [TESTÉ EN LABO] : ebur128 → gain → limiteur sur-échantillonné → re-mesurer ; l'AAC remonte le true peak (+1,9 dB) : limiteur à -3 dBFS avant encodage ; résultat -14,3 LUFS / -1,1 dBTP (`montage-loudness-livraison`).
- **R7 Captions** : pop d'échelle 125 → 100 % sur la 1re image, click -20 dB sur les mots-clés seulement.

## 5. Photosensibilité (obligatoire dès qu'il y a flash ou strobe) [TESTÉ EN LABO]
- `python3 -I labo/photosensibilite/flash_check.py rendu.mp4` ; > 3 flashs dans une seconde = refus (WCAG 2.3.1, BT.1702) ; un flash d'1 image compte entier ; surface jugée dans la pire fenêtre de 1/3 × 1/3 de l'écran. Pub UK : test Harding.
- À ~140 BPM : **une transition de luminance par croche au plus** ; un coup par noire à 128 BPM tombe pile sur la limite (pire seconde 3).
- Strobe sûr : changer **teinte et forme à luminance égale** (Noé / Kan) ; baisser la luminosité du texte ne sert à rien, les leviers sont la surface et la fréquence. [ÉPROUVÉ EN MAQUETTE] (pièce 09)
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
Premiere (Time Remapping, captions sur transcription, Essential Sound), After Effects (`wiggle` amorti, motion blur : `montage-after-effects`), CapCut, Resolve ; SFX : Sonniss GDC, Mixkit (lire les licences). À vérifier en phase 2 (vraies vidéos) : calage 3-6 images à l'oreille et à 24/25/30/60 i/s, rétention réelle de deux densités ; en phase 3 (logiciels) : décalage AAC réel, captions auto de Premiere, speed ramp Premiere contre AE. Labo : `labo/kinetic/` ; sources : `sources/kinetic-editing.md`.
