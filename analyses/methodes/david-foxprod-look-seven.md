# David Foxprod — « POV : tu essaies de recréer la colo de Seven » (méthode d'étalonnage)

_Fiche de **méthode**, pas de montage (consigne de Diego, `RETOURS-DIEGO.md` du 2026-10-11). Vidéo : `videos/methodes/david-foxprod-recreer-colo-seven.mp4` (11,96 s, 720x1280, 25 i/s, H.264 à 290 kb/s, 530 Ko). Analysée le 2026-10-11 (session 13) sur ses 299 images. Planche : `david-foxprod-look-seven.png` (référence, image de départ, image finale, arbre de nœuds agrandi)._

## Ce que dit Diego
« Ce qui compte, c'est ce qu'elle montre : un étalonneur qui reproduit un look, avec son arbre de nœuds visible (DaVinci Resolve). […] Ce n'est pas la seule façon de reproduire un look, mais elle a l'air plutôt simple, et je veux que tu la connaisses. » (`videos/NOTES-DIEGO.md`)

## Ce que montre l'écran [VU SUR IMAGES]
- **Mise en page de la vidéo** (trois bandes) : en haut, l'image de référence (gros plan de Brad Pitt dans *Seven*, arme floue au premier plan, ciel ocre) ; au milieu, le plan de l'étalonneur, **retourné à l'identique** (sosie, même cadre, même arme floue en amorce, même contre-jour sur ciel) ; en bas, l'arbre de nœuds de Resolve sur fond flou. Titre incrusté jusqu'à 7,8 s. Aucune roue, aucune courbe, aucun scope, aucune galerie, aucun split screen de Resolve n'apparaît : **la comparaison visible est celle du montage de la vidéo (référence posée au-dessus du plan)**, pas un outil de Resolve.
- **L'arbre final** (image 290), nœuds nommés par l'auteur, lus sur un agrandissement x3 :
  - entrée → **CST IN** (01) → **EXPO** (03) → **WB** (06) → **CON / SAT** (08) : branche du haut, en série ;
  - entrée (directement depuis la source, pas depuis CST IN : le trait part du point d'entrée) → **DENSITÉ** (02) → nœud sans nom (05) → **QUALIFIER** (04) : branche du bas, en série ;
  - les deux branches entrent dans un **mélangeur** (petit nœud carré ; parallèle ou layer : **illisible**) → **MASK** (09) → **OVERLAY** (10) ;
  - → **CST OUT** (11) → deux nœuds en parallèle **LOOK FUJI** (12, vignette assombrie : nœud désactivé) et **LOOK K…** (13, nom coupé à l'écran) → second mélangeur → sortie.
  - Petits badges d'outils sous chaque nœud (05 en a deux ronds, 09 un trait en biais, 10 une grille, 12 et 13 un carré) : **illisibles** à cette compression ; je n'en tire aucun outil. Une infobulle « RVB » apparaît sur l'entrée de CST IN (interface en français).
- **Démonstration nœud par nœud** : le curseur active les nœuds un à un et l'image du milieu change à chaque clic. Moyennes mesurées sur l'image du milieu (R, V, B, 0-255) :

| Temps | Nœud cliqué (curseur) | Ciel | Visage | Effet lu |
|---|---|---|---|---|
| 0,04 s | (aucun) | 189 189 195 | 100 87 86 | image log, grise et plate |
| 0,12 s | CST IN (et sortie) | 246 249 248 | 116 81 82 | image d'affichage : contraste, ciel blanc |
| 1,12 s | EXPO | 233 233 228 | 99 69 72 | tout baisse d'environ 14 |
| 1,88 s | WB | 236 233 216 | 106 68 56 | réchauffe (le bleu baisse) |
| 2,52 s | CON / SAT | 243 239 225 | 103 59 41 | ciel plus clair, visage plus dense et saturé |
| 3,68 s | DENSITÉ | 242 239 225 | 98 55 37 | léger alourdissement |
| 4,28 s | 05 (sans nom) | 248 235 193 | 97 55 35 | **le ciel jaunit** (B 225 → 193), visage inchangé |
| 4,8-5,6 s | QUALIFIER / mélangeur | 247 233 185 | 89 → 101 | retouche du visage (baisse puis remonte) |
| 6,48 s | MASK | 249 234 175 | 90 57 29 | ciel encore plus jaune, visage plus sombre |
| 7,0 s | OVERLAY | inchangé | inchangé | rien de mesurable (texture ? illisible) |
| 7,8-8,9 s | tout l'arbre sélectionné et désactivé | 251 253 253 | 167 124 119 | **avant / après** : retour à l'image brute |
| 8,9 s → fin | tout réactivé | 249 234 175 | 95 59 32 | image finale |

  Référence (*Seven*, même zone) : ciel 184 167 106, visage 81 46 14.
- **Montage de captures, pas un enregistrement continu** : sauts d'image à 0,08 s, 1,08 s et 10,72 s, et la **numérotation des nœuds change** entre le début (CST IN = 11, CST OUT = 07, looks 08 / 09, nœuds 04 et 10 absents) et la fin (CST IN = 01, CST OUT = 11, looks 12 / 13, nœud 07 absent). L'ordre d'activation montré a donc pu être arrangé pour la vidéo.

## La méthode reconstituée [THÉORIQUE, déduit de l'écran]
1. **Retourner le plan comme la référence** : même cadre, même focale apparente, même amorce, même contre-jour. C'est la moitié du travail, et elle se fait au tournage.
2. **Encadrer l'arbre par deux conversions** : CST IN (log caméra → espace de travail) au début, CST OUT (→ Rec.709) à la fin. Tout le travail se fait entre les deux.
3. **Primaires en série, une idée par nœud, nommée** : exposition, puis balance des blancs, puis contraste / saturation.
4. **Une branche parallèle pour le relief** : densité, une correction localisée (05, probablement des fenêtres : c'est le nœud qui jaunit le ciel sans toucher le visage), un qualifieur (visage). Elle part de la source, ce qui laisse les clés se prendre sur une image non encore écrasée.
5. **Après le mélange : un masque (MASK) puis une texture (OVERLAY)**, encore dans l'espace de travail.
6. **Le look en dernier, après CST OUT**, en deux versions parallèles (FUJI, K… : sans doute deux émulations de pellicule, Fuji et Kodak, **nom coupé, non vérifié**) : on en désactive une pour comparer, on garde l'autre.
7. **Juger** : activer les nœuds un à un pour voir l'apport de chacun, puis tout désactiver d'un coup (avant / après), en regardant la référence posée à côté.

## Confronté à mes skills
- **Confirme** `montage-resolve` § 2 (entrée normalisée, primaires avant secondaires, une idée par nœud, sortie en dernier) et `montage-couleur-pipeline` (« normaliser d'abord, regarder ensuite »). Confirme la leçon de maquette de `montage-resolve` : la clé prise sur l'entrée, dans une branche parallèle mélangée en sortie.
- **Diffère** sur la place du look : mon arbre de référence met le look **avant** la sortie ; ici il est **après** CST OUT, donc écrit pour du Rec.709. C'est cohérent avec mes propres LUT créatives (définies sur des valeurs Rec.709/2.4, `montage-couleur-pipeline` § 4.3) et c'est plus simple, mais le look ne survit pas à une sortie HDR ou cinéma.
- **Doute** : si la branche du bas reçoit vraiment la source log et la mélange à une image déjà convertie, les deux images ne sont pas dans le même espace ; soit ses nœuds contiennent leur propre conversion, soit le mélange ne sert qu'à transporter une clé. Illisible ici.
- **Complète** `montage-couleur-et-intention` : le look de la référence vient d'abord de la **prise de vue** (contre-jour, ciel brûlé, cadre) ; l'étalonnage ne fait que la teinte et la densité.

## Limites mesurées [TESTÉ EN LABO, sur la vidéo]
- **La teinte est rattrapée, pas la densité** : l'image finale reste bien plus claire que la référence (ciel 249 / 234 / 175 contre 184 / 167 / 106 ; visage 95 / 59 / 32 contre 81 / 46 / 14). Le ciel final est presque blanc, celui de *Seven* est ocre : un ciel brûlé au tournage ne redevient pas ocre dense à l'étalonnage. Réserve : les deux images ne sont pas le même plan et la référence est une copie web compressée.

## Principes transférables
1. Pour reproduire un look, **reproduire d'abord l'image** (cadre, lumière, valeur du ciel) : l'étalonnage finit ce que le tournage a commencé.
2. Un arbre court, **nommé**, encadré par CST IN / CST OUT, se lit et se juge nœud par nœud.
3. Deux looks en parallèle, un seul actif : la comparaison A / B la plus rapide.
4. Juger chaque nœud par son apport (activer un à un), et le tout par un avant / après franc.

## Doutes
- Outils exacts de chaque nœud, type des mélangeurs, contenu d'OVERLAY et de LOOK K… : illisibles (11,96 s à 290 kb/s).
- Changement de numérotation des nœuds : je n'en connais pas la cause (deux captures différentes, ou renumérotation de Resolve) [NON VÉRIFIÉ].
- *Seven* aurait eu des copies d'exploitation tirées avec un procédé à rétention d'argent (CCE de Deluxe) [NON VÉRIFIÉ] : si c'est le cas, une partie de la densité de la référence est un effet de tirage qu'aucun des nœuds visibles n'imite explicitement.
