---
name: montage-kinetic-editing
description: Montage kinetic / dynamique pour réseaux sociaux (Reels, TikTok, Shorts, YouTube) — cuts rapides, beaucoup de SFX (whoosh, swoosh, impact, hit, riser, click, glitch), speed ramp, punch-in, zoom, camera shake, whip et smash cut, flash, captions animées mot à mot (style Hormozi), hook des 3 premières secondes, rétention, pattern interrupt, B-roll, mèmes. Mots d'un monteur social media : « ça manque de punch », « mets des whoosh », « faut que ça claque », « high retention », « fast-paced », « ça décroche à 3 s », « sound design de Short ».
---

# Kinetic editing (montage social « haute rétention »)

> **Contrepoint (goût de l'utilisateur)** : le clip de Ziak qu'il adore fait exactement l'inverse : coupes non calées sur le beat, aucun SFX surligné (`montage-rythme`, section Ziak). Le kinetic est un choix pour l'énergie et la rétention, pas un réflexe.

Goût de l'utilisateur : il AIME ce style. Ne pas le traiter comme un cliché à corriger. Ici, **la densité de SFX est le langage**. L'amateur et le pro ne se distinguent pas par la quantité de sons mais par **la précision (à l'image), la variété, la hiérarchie**, et par les respirations.

> Nuance aux autres skills : « whoosh sur chaque transition = cliché » vaut pour la pub, le corporate et la fiction. En kinetic editing, un son par événement visuel est la norme (Ali Abdaal : « un son à chaque fois que quelque chose apparaît à l'écran »). Le cliché, c'est le **même** whoosh, au **même** niveau, **en retard**.

## 1. Quand et pourquoi
- **Pourquoi ça marche** : sur un fil, le spectateur décide en 1 à 3 s. Le guide interne de MrBeast (fuite d'août 2024) fait de la 1re minute la zone critique et prévoit des relances régulières. Chaque coupe, zoom ou son est une petite relance d'attention (pattern interrupt).
- **Le son est le moteur du rythme** : à cette vitesse, l'œil n'enregistre pas toutes les coupes, l'oreille si. Le son fait sentir la coupe, lui donne un poids (whoosh = vitesse, impact = masse, click = précision) et rend lisible un plan de 6 images.
- **Respiration obligatoire** : un montage à 6 images constantes devient un mur. Il faut accélérer puis relâcher (labo : 15 → 6 images jusqu'à l'impact, puis 15), placer un trou de silence avant le gros impact et laisser au moins un plan « tenu » par séquence de 5 à 8 s.
- **Quand ce style dessert** : deuil, témoignage intime, sujet grave, marque de luxe lente, explication technique qui demande de lire un schéma, humour qui repose sur un silence ou un temps de réaction. Dans ces cas, garder la précision du style (captions, sons calés) mais diviser la densité par 3. Ou le dire à l'utilisateur.

## 2. Grammaire
### Durées (à 30 i/s ; × 0,83 à 25 i/s)
| Usage | Images | Secondes |
|---|---|---|
| Plan éclair, montage-choc, liste de mèmes | 4-8 | 0,13-0,27 |
| B-roll illustratif, plan de rythme | 8-20 | 0,3-0,7 |
| Phrase face caméra entre deux jump cuts | 30-90 | 1-3 |
| Plan « respiration » / chute / réaction | 45-120 | 1,5-4 |
Repères sourcés : jump cuts toutes les 1-3 s (style Hormozi), interruptions visuelles toutes les 2-4 s (guides CapCut / retention editing, 2025-2026). [THÉORIQUE : chiffres d'éditeurs, à confronter aux statistiques de rétention du compte]

### Types de coupe et d'effet
- **Jump cut** : retirer silences et hésitations de la parole ; changer d'échelle (100 % → 115 %) pour masquer la saute.
- **Punch-in** : zoom brusque (1 à 3 images) sur le mot-clé. Avec l'ease-out, ça claque ; en linéaire, c'est mou. [TESTÉ EN LABO]
- **Smash cut** : coupe sèche d'un calme à un fort (ou l'inverse), souvent avec un silence juste avant.
- **Whip / swish** : flou directionnel ou speed ramp en cloche (accélération en fin de plan A, décélération en début de plan B), avec flou de bougé (Shutter Angle).
- **Speed ramp** : Time Remapping > Speed dans Premiere, keyframes séparés en Bézier. [THÉORIQUE]
- **Camera shake** : sur l'impact seulement, amorti en 4 à 6 images ; jamais en continu. [TESTÉ EN LABO]
- **Flash blanc** : 1 image (2 max) sur l'impact ; au-delà, c'est un fondu. [TESTÉ EN LABO]
- **Masque de transition** : un objet qui passe devant l'objectif (ou un mouvement de caméra rapide) sert de rideau, et la coupe est cachée dedans.
- **Captions mot à mot** : majuscules grasses, contour épais, 1 à 4 mots à l'écran, mot-clé en couleur (le jaune chez Hormozi) ou agrandi, apparition calée sur la syllabe. Les captions restent dans la zone sûre (hors 15 % du bas et interface de droite).
- **B-roll / mèmes** : illustrer le mot au moment où il est dit, pas une seconde après.

### Les SFX et leur rôle (hiérarchie, du plus fort au plus discret)
| Rang | SFX | Sert à | Placement |
|---|---|---|---|
| 1 | **Impact / hit / boom** (sub + transitoire) | ponctuer LA révélation, le chiffre, la chute | attaque **sur** la 1re image du plan (labo : +2 ms) |
| 2 | **Riser / reverse** | créer l'attente | crête sur la coupe ou coupé 1 image avant l'impact (suck-out) |
| 3 | **Whoosh / swoosh / swish** | vitesse : whip, zoom, texte qui entre, glissé | début 3-6 images AVANT, crête SUR la coupe |
| 4 | **Pop / click / tick / UI** | précision : texte, icône, coche, mot de caption | sur l'image d'apparition |
| 5 | **Glitch, rewind, record scratch, cash, mème** | effet comique ou de rupture | ponctuel, avec parcimonie |
| 6 | **Foley** (pas, tissu, objet) et **ambiance** | réalité, liant, éviter le vide numérique | continu, très bas |
Sources du placement : crête du riser sur le moment clé (Epidemic Sound) ; son démarré avant la coupe, crête sur la 1re image, sinon il paraît en retard (Morphic). La fourchette « 3 à 6 images » n'apparaît dans aucune source écrite : elle vient du labo et reste à valider à l'oreille. [TESTÉ EN LABO pour le calage, THÉORIQUE pour le ressenti]

**Règles de hiérarchie**
- Un seul rang 1 par séquence de 5 à 10 s, sinon plus rien n'est gros.
- Les whoosh varient : longueur (= longueur du mouvement), hauteur, filtre, niveau (-10 à -14 dB sous l'impact au labo). Au moins 3 à 5 variantes en rotation.
- Toutes les coupes n'ont pas de son. Une coupe sèche juste avant un impact le rend plus fort.
- La voix reste intelligible : SFX coupés ou baissés sous les consonnes importantes, et EQ qui creuse 1-4 kHz dans les whoosh pendant la parole.
- Musique : couper sur les temps forts, impacts sur les downbeats ; à défaut, varier la musique (drop, coupure, filtre passe-bas) comme un SFX.

## 3. Ce qui sépare le pro de l'amateur
| Amateur | Pro |
|---|---|
| Whoosh posé APRÈS la coupe → effet en retard | Whoosh qui anticipe, crête sur la coupe, calé à l'image |
| Le même sample partout | Banque de variantes, longueur adaptée au geste |
| Tous les SFX au même niveau | Hiérarchie : impact > riser > whoosh > click > foley |
| Densité constante, montage « mur » | Accélérations, relâchements, silences tactiques |
| Shake et zoom en continu | Effet = événement, amorti en 4-6 images |
| Captions qui recouvrent l'interface, 8 mots | 1-4 mots, zone sûre, mot-clé marqué |
| Hook « Salut, aujourd'hui… » | Hook visuel + sonore à l'image 1 : résultat, question, contraste |
| SFX qui écrasent la voix ou font le niveau | Voix d'abord ; SFX dans le mix, -14 LUFS mesuré sur le fichier encodé |
| Punch-in linéaire, sans flou de bougé | Ease-out 2-3 images, motion blur |
| Plan de 4-8 images où le sujet entre, sort ou est dans le noir | Sujet lisible **dès la 1re image** du plan (atelier 02 : 4 plans noirs sur 19 en v1) |
| Whoosh sur un mouvement qu'on ne voit pas | Chaque SFX a une cause visible ; sinon il devient du bruit (atelier 02 v1) |

## 3b. Leçon d'atelier (pièce 02 « Étincelle », 6 versions)
- Un montage qui accélère sur des plans **sans lien** reste un défilé ; quand chaque plan montre une cause de l'événement final (le pendule = le temps qui frotte l'allumette), la même accélération devient une montée. Les SFX y gagnent une cause visible.
- La couleur forte réservée à la fin se **mesure** : ≤ 0,14 % de pixels chauds avant l'allumage, 3,7 % après (v6).
- Calculer les fenêtres de source depuis la cinématique dans le script : deux régressions (v2, v5) sont venues de fenêtres recopiées à la main.

## 3c. Leçon d'atelier (pièce 09 « Générique de l'équipe », session 7)
- **Strobe sans risque** [TESTÉ EN ATELIER] : cartons de 3 images sur des fonds de teintes différentes à **luminance relative égale** (~0,03 ; recherche de la valeur HSV qui donne la luminance cible), texte clair : le fond ne flashe plus, mais **les grands mots clairs flashent localement** (critère WCAG de la fenêtre 1/3 × 1/3) : 6 flashs, pire seconde 3, à la limite ; marge : cartons de 4 images ou texte moins lumineux dans les passages les plus rapides. Les mêmes cartons sur fonds noir / blanc alternés : 16 flashs, pire seconde 5, inlivrable.
- **Rupture de forme** : varier échelle (10 → 60 % de la hauteur), position et débord à chaque coupe ; la police ne compte qu'en grand. Le sommet (les noms qui comptent) doit changer de règle, pas seulement grossir : v4 = fond commun, deux lignes géantes, même police pour les 4 acteurs, après 28 cartons où tout change.
- **Photosensibilité : baisser la luminosité du texte ne sert à rien** (v4 : texte à 0,72, toujours pire seconde 3) ; les leviers sont la **surface** du mot dans sa fenêtre locale et la **fréquence**.

## 4. Recettes
**R1 — Hook 0-3 s** [THÉORIQUE] : image 1 = l'image la plus forte (résultat, chiffre, action) + impact ou drop musical à l'image 1 ; captions dès la 1re syllabe ; 2 à 4 coupes dans les 3 premières secondes ; la promesse est dite avant la 3e seconde.

**R2 — Montée vers une révélation** [TESTÉ EN LABO] : plans 15 → 13 → 12 → 10 → 8 → 6 images ; riser de 1 s à -12 dB sous l'impact, coupé 1 image avant ; coupe sèche ; impact + flash 1 image + shake amorti 5 images ; puis un plan tenu de 15 images ou plus.

**R3 — Punch-in sur mot-clé** [TESTÉ EN LABO] : 2 images larges puis ×1,35 en 3 images ease-out ; whoosh court à crête sur le début du zoom.
ffmpeg : `zoompan=z='if(lt(on,2),1,1+0.35*(1-pow(1-min((on-1)/3,1),3)))':d=1:s=540x960:fps=30:x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2'`

**R4 — Shake + flash** [TESTÉ EN LABO] : `scale=W+60:H+106,crop=W:H:x='30+26*sin(n*2.9)*exp(-n/3)':y='53+26*cos(n*3.7)*exp(-n/3)',drawbox=c=white:t=fill:enable='eq(n,0)'`

**R5 — Caler un SFX à l'image en script** [TESTÉ EN LABO] : échantillon = image × (fréq. d'échantillonnage / cadence), soit 1600 à 48 kHz / 30 i/s. Whoosh : début = coupe − k × 1600 (k = 3 à 6), crête à la coupe. Impact : attaque à la coupe, montée de 0,5 ms pour éviter le clic.

**R6 — Loudness d'un mix chargé en SFX** [TESTÉ EN LABO] : mesurer avec ebur128 → gain → limiteur sur-échantillonné → re-mesurer, et itérer, car le limiteur mange le niveau (5 passes au labo). **L'AAC fait remonter le true peak** (+1,9 dB au labo sur des impacts) : plafonner le limiteur à -3 dBFS (`alimiter=limit=0.7079` à 192 kHz) avant l'encodage, puis mesurer le MP4. Résultat : -14,3 LUFS / -1,1 dBTP. Voir `montage-loudness-livraison`.

**R7 — Captions mot à mot** [THÉORIQUE pour Premiere/CapCut ; TESTÉ EN LABO avec drawtext] : 1 mot ou groupe par segment, « pop » d'échelle sur la 1re image (125 % → 100 %), click à -20 dB sous l'impact pour les mots-clés seulement.

**R8 — Speed ramp en transition** [THÉORIQUE] : fin du plan A en rampe 100 → 400 % sur 6-8 images, début du plan B 400 → 100 %, keyframes en Bézier, flou de bougé activé, whoosh dont la crête tombe sur la coupe au sommet de la vitesse.

## 5. Outils
- **Premiere** : Time Remapping, Essential Graphics / captions automatiques (texte basé sur la transcription), Essential Sound, Remix. **After Effects** : expressions de shake (`wiggle` amorti), motion blur, animateurs de texte (voir `montage-after-effects`).
- **CapCut** : captions auto avec styles « Hormozi », effets de shake et de zoom intégrés. **DaVinci Resolve** : Speed Ramp, Fairlight, Text+.
- **Captions automatiques** : Submagic, Kapwing, Opus Clip (pages éditeurs).
- **SFX gratuits** : Sonniss GDC Bundle (licence sans attribution), Mixkit (Mixkit License) ; packs Gumroad : lire la licence avant usage commercial.

## 6. Checklist avant livraison
- [ ] Planche contact de la 1re image de chaque plan : chaque vignette se lit seule (sujet, pas du noir).
- [ ] L'image 1 et le son 1 accrochent ; la promesse est dite avant 3 s.
- [ ] Chaque whoosh démarre avant sa coupe et culmine dessus ; chaque impact tombe sur l'image (vérifié image par image).
- [ ] Au plus un rang 1 (impact) par séquence de 5 à 10 s ; les whoosh varient.
- [ ] Au moins une respiration (plan tenu, silence ou baisse de densité) toutes les 5 à 10 s.
- [ ] Shake et flash amortis en ≤ 6 images, flash ≤ 2 images. **Photosensibilité** [TESTÉ EN LABO, session 7] : `python3 -I labo/photosensibilite/flash_check.py rendu.mp4` ; > 3 flashs dans une seconde = refus diffuseur (WCAG 2.3.1, BT.1702). Un flash d'1 image = 1 flash entier : 4 impacts flashés par seconde échouent. **La surface se juge localement** (pire fenêtre de 1/3 × 1/3 de l'écran) : un mot ou un logo de 6 % de l'écran qui clignote vite échoue. Pour un effet « strobe » sûr, changer **teinte et forme à luminance égale** (principe Noé / Kan, `culture/enter-the-void-generique-noe-tom-kan.md`). Pub UK : test Harding obligatoire.
- [ ] Captions : zone sûre, 1-4 mots, orthographe, mot-clé marqué.
- [ ] La voix est intelligible au téléphone, haut-parleur intégré.
- [ ] -14 LUFS ±0,5 / ≤ -1 dBTP **mesurés sur le MP4 encodé**.
- [ ] Le style sert le sujet (sinon, densité ÷ 3).

## 7. À vérifier en phase 2 (Premiere / After Effects)
- Le calage whoosh 3-6 images avant / impact sur l'image tient-il à l'oreille, au casque et sur téléphone ? À 24, 25, 30 et 60 i/s ?
- Le décalage audio réel des MP4 exportés (prime AAC) : rester sous 1 image, comme au labo (+2 ms).
- Les captions automatiques de Premiere : précision du calage mot à mot, styles, export SRT.
- Le speed ramp Premiere (Bézier) comparé à AE (Timewarp, Pixel Motion) sur de vrais rushes ; le motion blur.
- Le shake par expression AE (`wiggle` multiplié par une décroissance) comparé au preset CapCut.
- Le true peak après export AAC depuis Premiere avec un limiteur à -1, -2 et -3 dBTP.
- La rétention réelle : comparer 2 versions (densité forte / modérée) dans les statistiques de la plateforme.

Labo : `labo/kinetic/` (script, RESULTATS.md, planche, forme d'onde). Sources : `sources/kinetic-editing.md`.
