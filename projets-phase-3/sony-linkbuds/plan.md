# Plan de montage — Sony LinkBuds Clip × KORE (V5)

**Genre : after movie / événementiel kinetic de marque, vertical 9:16, réseaux sociaux. Ton : énergique, « quasiment épileptique » (brief), fini premium. Que du visuel : aucun sous-titre, aucun texte hors titre et plan de fin.**
Règles qui s'appliquent : toutes les [universel] de `montage-regard` et du carnet, et les [genre : after movie kinetic] de `montage-kinetic-editing` (rafales qui reviennent, techniques variées tirées de la matière, un son sur chaque transition, jamais deux fois le même moment d'un rush, inversions, dernier pic avant la marque puis fin courte).

_Phase 3, 2026-10-11, après les notes de Diego sur la V4 (80 % livrable) et ses consignes dictées en session V5. Plan V4 : `archives/phase-3/sony-linkbuds/V4/plan.md`. Direction artistique : `da.md` (écrite avant les effets). Timeline Resolve : `SONY_V5` (projet `P3-sony-linkbuds-agent`, dupliquée de `SONY_V4`, qui reste intacte). Images de timeline à 25 i/s._

## Intention (inchangée)
**On entre chez KORE, on met les LinkBuds Clip, et la séance monte jusqu'au rouge ; le produit se porte comme un bijou et tient la tête en bas.** La V5 travaille le goût : chaque plan et chaque effet ont une raison, chaque élément graphique vient de la DA, la couleur se règle plan par plan, et le film finit sur un dernier pic au lieu d'un relâchement.

## Ce qui change par rapport à la V4
| Note de Diego | Réponse dans la V5 |
|---|---|
| Ouverture : plus vite, large KORE surexposé | Zoom E → KORE en 7 images (41-48), KORE tenu 48-60 ; exposition réglée sur tout le mouvement : lettres et comptoir au même béton (0,36-0,37), large 0,67 sans blanc brûlé |
| Plan de 16-17 s surexposé, écouteurs de fin surexposés | Étalonnage plan par plan : 19 plans corrigés après mesure et revue de chaque plan (C6581 0,35 → 0,15 ; packshots : 13-27 % de blanc brûlé → 0 % hors flash) |
| Noirs relevés, bruit | Noirs posés à 0 (p1 ≤ 0,01 sur les plans de salle), grain 35 → 20 % ; ombres vérifiées amplifiées ×4 |
| Tête bizarre (0:09), tapis flou (0:12), panoramique flou | Plans retirés ou remplacés ; tous les visages contrôlés image par image (`controle_plans.py`) ; C6627 (199) remplacé par un autre moment du même rush (12,3 s, yeux ouverts) |
| Collages : pourquoi ce plan ? fonds hors DA, détourage raté | Collage A1 (281-293) suivant ta piste ; collage C1 (678-686) ; collage B supprimé ; détourage BiRefNet contrôlé au bord ; aucun fond ajouté (`da.md`) |
| Inversions : un peu plus | Les flashs blancs des drops 233 et 690 deviennent des inversions ; deux inversions dans le pic (907, 942) |
| Un son sur chaque transition | 16 sons recalés à l'image, 5 retirés, 13 posés (collage A1, pic) : `sfx.md`, section V5 |
| Fin trop longue : un dernier pic de 4-5 s | **Dernier pic 831-948** (4,7 s) d'après la référence foebusdelapaz, dans notre palette ; les packshots restent sobres |
| Gyroflow prouvé plan par plan | Rendus Gyroflow à synchronisation imposée et mesurée ; preuve par plan dans la note de livraison |

## Structure, techniques, et pourquoi
| # | Bloc | Images | Plans | Technique, et pourquoi elle est là |
|---|---|---|---|---|
| 1 | **Le lieu, épelé** | 0-117 | K C6491, O C6492, R C6493, E C6494, zoom infini E → KORE C6495 (41-48), KORE tenu, salut C6540 (60), allée C6505 (83, 200 %) | Le cadreur a filmé chaque lettre pour qu'on épelle la marque ; les lettres sont sur le comptoir du plan large : le recul du E jusqu'au mot est un vrai zoom infini. |
| 2 | **Entrer et s'équiper** | 117-179 | boîtiers C6507, gros plan C6507 Gyroflow (129, flash), mains aux oreilles C6553, flash cut des oreilles 152-179 | On vérifie oreille par oreille : l'écouteur au même point, de plus en plus vite. Puis le silence. |
| — | Silence | 179-185 | noir | Le silence de la musique : la respiration avant la séance. |
| 3 | **La coach lance, tout monte** | 185-233 | coach C6550, rafale qui monte (C6627 12,3, C6637, C6636, C6627 20,6, C6646, C6578, C6626, C6633 ; 300 %) | Chaque plan est un mouvement vers le haut ; la montée se voit autant qu'elle s'entend. |
| 4 | **Le bas du corps** | 233-468 | drop C6576 (inversion), fentes, collage A1 (281-293), pieds, profil C6577, … rafale qui descend en step-print 421-468 | La rafale finale descend (pieds, ressorts) en step-print : l'inverse de la rafale 3. |
| 5 | **Reprendre son souffle** | 468-521 | souffle C6608 (yeux fermés, voulu), profil souriant C6566 continu | La basse disparaît : un visage qui souffle, puis l'écouteur porté, sans effet. (Le collage B est supprimé : ni raison ni force.) |
| 6 | **Le haut du corps, puis la tête en bas** | 521-656 | sangles, poignées, bras, tête en bas, punch-in sur l'écouteur, écran partagé 609-656 | Le même exercice fait par toute la salle : les bandes s'ouvrent sur les temps. |
| 7 | **La lumière passe au rouge** | 656-690 | oreille dans le rouge C6660, collage C1 (678-686 : la tête positive, le monde en négatif) | La bascule de lumière arrive d'abord sur une oreille ; le négatif annonce le rouge. |
| 8 | **Le sommet rouge** | 690-831 | drop C6662 (inversion), rires, chouchou, rafale rouge à inversions (784, 793), bras levés C6676 | Dans le rouge, un flash blanc ne se voit plus : l'inversion est le flash de ce monde. |
| 8 bis | **Le dernier pic** | 831-948 | `pic_v5.mov` (calculé hors Resolve, `labo/outils/phase3/v5/pic_v5.py`) : P1 révélation par seuil de la sangle KORE (la couleur sur l'attaque de 837) ; P2 rafale récapitulative de 14 plans de 2 images, chacun dans un état ; P3 respiration sur un héros de dos en noir et blanc (878) ; P4 stroboscope d'états dans la salle rouge, punch-in sur les temps, un négatif (907), un seuil (919) ; P5 crash zoom sur le mot KORE du comptoir (931), un négatif (942), balayage, blanc (948) | Diego : après le déferlement, la fin ne doit pas retomber. Le pic reprend tout le film en accéléré (la sangle, les participantes, le rouge) et se termine sur le mot KORE : **rappel voulu de l'ouverture** (même comptoir, autre moment du rush), puis la marque Sony. Changements d'état sur les attaques fortes de la musique, micro-coupes libres (référence foebusdelapaz). |
| 9 | **L'objet** | 948-1072 | packshot C6725 (Gyroflow), C6723 ×2 (Gyroflow) + titre (1003) | Après la séance, l'objet seul en plein jour, sobre ; le titre dessiné comme la DA Sony. |
| 10 | Plan de fin Sony | 1072-1114 | fourni | — |

## Variantes sur les moments clés, et pourquoi
| Moment | Gardée | Écartées, et pourquoi |
|---|---|---|
| Collage A (281-293) | **A1** : son image figée en noir et blanc, le plan suivant glisse depuis le bas derrière elle, elle disparaît par balayage | A2 (fond négatif, révélation par lignes) : le négatif est déjà le langage du collage C, et deux balayages se suivraient ; A3 (échos qui grandissent, entrée latérale filée) : l'écho derrière une image figée décore sans bouger, et l'entrée latérale se lit comme une poussée (transition exclue). _Raisons écrites après coup (la session V5 n'avait noté que le choix)._ |
| Collage B (503-515) | **aucun** : C6566 continu | B1, B3, B4 : aucun ne servait le plan suivant ni le sens (« sans raison ni force ») ; le plan seul, un sourire et l'écouteur, suffit. |
| Collage C (678-686) | **C1** : tête positive, le monde en négatif | C2 (stroboscope d'états) : gardé pour le pic ; C3 : la tête réduite dans son image négative fait un cadre (exclu par la DA). |
| Dernier pic, respiration P3 | **plan net tenu**, noir et blanc dense, poussée lente | Écho par flux optique (traînée continue) : la caméra bouge, tout le décor traîne, voile laiteux et noirs relevés (`variantes/pic_P3_net-contre-echo.jpg`). La référence respire aussi sur un héros tenu en noir et blanc. |
| Dernier pic, fin P5 | **crash zoom du comptoir vers le mot**, exposé −0,13 | Flash cut aligné hall / façade / sangles : sur la façade l'enseigne est en haut de l'image et un visage reste dans le cadre ; sur les sangles le mot est petit et penché. |
| Dernier pic, première version | **version b** | Version a : 6 flashs dans la pire seconde (stroboscope à trois négatifs et alternance noir et blanc qui assombrit), 2 doublons (C6578, C6664), comptoir brûlé, parties décalées de 4 à 6 images sur les attaques. |

## Musique (inchangée)
`messwave - easy.mp3` : 99,498 → 125,736 s puis 133,236 → 150,5 s. Repères : coups 128 et 140 ; silence 179-185 ; relance 187 ; drop 233 ; appels sans basse 281, 468, 656 ; dernier drop 690 ; attaques fortes du pic 837, 878, 901, 907, 931, 948 ; dernier coup 1072. 129,2 BPM : un temps = 11,6 images.

## Critères de réussite (mesurés sur le rendu V5)
| Critère | Cible | V5 |
|---|---|---|
| Doublons | 0 | **0** (99 plans, sources du pic comprises) |
| Packshots | aucun blanc brûlé dans le boîtier | 0 % ≥ 0,97 hors flash |
| Photosensibilité | ≤ 3 flashs par seconde | **3** au pire |
| Loudness | −14 LUFS ±1, ≤ −1 dBTP | **−13,9 LUFS, −1,1 dBTP** |
| Durée, format | 44,6 s ; 1080x1920, 25 i/s, H.265 Main 10 | 44,6 s, HEVC Main 10, 39 Mb/s, BT.709 |
| Visages | aucun moment peu flatteur sans raison | C6627 remplacé ; C6608 (yeux fermés) voulu |
| Son | un son sur chaque transition | tableau dans `sfx.md` (V5) |
