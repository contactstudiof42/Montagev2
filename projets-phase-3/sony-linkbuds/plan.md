# Plan de montage — Sony LinkBuds Clip × KORE (V4)

_Phase 3, 2026-10-11, après les notes de Diego sur la V3 (65 % livrable) et ses consignes dictées en session (Gyroflow, aucun moment répété). Plan V3 : `archives/phase-3/sony-linkbuds/plan-V3.md`. Timeline Resolve : `SONY_V4` (projet `P3-sony-linkbuds-agent`, dupliquée de `SONY_V3`). Temps des rushes en secondes depuis le début du rush (« rel »)._

## Intention (inchangée)
**On entre chez KORE, on met les LinkBuds Clip, et la séance monte jusqu'au rouge ; le produit se porte comme un bijou et tient la tête en bas.** Diego a validé le rythme et la compréhension de la V3 : la structure en 9 blocs et la musique restent. La V4 travaille la finition : chaque effet a une raison dans la matière, aucun n'est répété d'une rafale à l'autre, rien de cheap.

## Ce qui change par rapport à la V3
| Note de Diego | Réponse dans la V4 |
|---|---|
| Titre : police et animation « toujours pas ça » | Dessin de la DA Sony (`references/da-linkbuds-clip-reference.png`) : « **LinkBuds** » en SST Bold, « Clip » en SST Light, accolés, noir sur fond clair, beaucoup d'air. Apparition « à la Apple » : fondu et montée de quelques pixels, freinée, rien d'autre |
| Effets répétitifs, sans folie (eyecannndy) | Une technique par moment, chacune tirée de la matière : épellation épinglée + **zoom infini** (E → KORE), **flash cut aligné** (les oreilles), rafale **qui monte**, rafale **qui descend en step-print**, **écran partagé** en trois bandes, rafale rouge à **inversions négatives**, **collages** sur arrêt sur image. Table des techniques : `montage-kinetic-editing` § 4 bis |
| Zoom infini « s'il est bien exécuté » | La matière existe : les lettres et le mot KORE sont sur le même comptoir. Raccord d'échelle mesuré (points SIFT entre le E en gros plan et le E du plan large), recul continu, pas de flou de transition |
| SFX répétitifs | Nouvelles familles (bande, papier, argentique, scratch, tonal, ressorts…) : une famille par technique ; variations de hauteur |
| Couleur « bouillie », « pâté », produit surexposé | Séparation des teintes dans la LUT (peau isolée du décor, néons neutres, rouge gardé) ; packshots mesurés sur la forme d'onde et en fausses couleurs ; grain allégé ; export de qualité (`look.md`) |
| Export | H.265 Main 10, débit élevé, multipass ; vérifié au ffprobe et à l'image |
| Détourages « bizarres » | Collages sur arrêt sur image (captured-by-h) : détourage fait sur l'image figée en pleine résolution (carte de profondeur affinée), fond transformé, puis **le mouvement reprend** |
| K-O-R-E : cadrage et flottement | Gyroflow, puis chaque lettre **épinglée au même point** (le cadreur voulait un fixe sans trépied) |
| Packshots : stabilisation visible | Gyroflow (zoom fixe, lissage modéré) puis correction « rail » : on garde le travelling avant / arrière du cadreur, on retire la main (`montage-regard` point 3) |
| Jamais deux fois le même moment d'un rush | 11 doublons de la V3 (dans les rafales) supprimés ; `labo/outils/doublons_timeline.py` avant chaque rendu : 0 doublon exigé |

## Musique (inchangée)
`messwave - easy.mp3` : 99,498 → 125,736 s puis 133,236 → 150,5 s. Repères (images) : coups 128 et 140 ; silence 179-185 ; relance 187 ; drop 233 ; appels sans basse 281, 468, 656 ; dernier drop 690 ; coups toutes les 47 images ensuite ; dernier coup 1072. Tempo 129,2 : un temps = 11,6 images.

## Structure, techniques, et pourquoi
| # | Bloc | Images | Plans (rel) | Technique, et pourquoi elle est là |
|---|---|---|---|---|
| 1 | **Le lieu, épelé** | 0-94 | K C6491, O C6492, R C6493, E C6494 (Gyroflow, épinglées), **zoom infini** du E vers KORE C6495 (40-48), KORE tenu, C6540 salut (14,6) | Le cadreur a filmé chaque lettre pour qu'on épelle la marque : une lettre par temps, toutes au même point. Les lettres sont sur le comptoir du plan large : le recul du E jusqu'au mot entier est un vrai zoom infini (la matière le permet), qui tombe sur le coup 48. |
| 2 | **Entrer et s'équiper** | 94-179 | allée C6505 (200 %), boîtiers dans la salle C6506 et C6507 (Gyroflow + rail), mains aux oreilles C6553, puis **flash cut des oreilles** 152-179 : C6555, C6628, C6611, C6630, C6559, C6561 | Après le geste collectif (tout le monde met ses écouteurs), on vérifie oreille par oreille : l'écouteur reste au même point du cadre pendant que le cadre se resserre d'une participante à l'autre, de plus en plus vite, jusqu'à la macro. Un tic par oreille. Puis le silence. |
| — | Silence | 179-185 | noir | La respiration avant la séance. |
| 3 | **La coach lance, tout monte** | 185-233 | coach C6550 (4,0), puis **rafale qui monte** : bras et corps qui se lèvent (C6624, C6627, C6578, C6636, C6646, C6633) | La musique monte (riser) : chaque plan est un mouvement vers le haut, coupé pendant le geste, le suivant le continue. La montée se voit autant qu'elle s'entend. |
| 4 | **Le bas du corps** | 233-468 | drop sur la coach C6576, fentes, **collage** C6594 (281), pieds, profil en effort C6577 (ralenti), …, puis **rafale qui descend en step-print** 421-468 (C6587 24,2, C6590 2,1, C6568 1,3, C6569 0,7, C6571 1,5) | On travaille les jambes : la rafale finale est faite de mouvements vers le bas (la caméra descend aux pieds, on se penche aux ressorts), en step-print (chaque image tenue deux fois) : la saccade du run and gun devient un parti pris, et c'est l'inverse de la rafale 3. |
| 5 | **Reprendre son souffle** | 468-515 | souffle C6608 (ralenti), **collage** C6566 (503) | La basse disparaît : un visage, puis un arrêt où le sujet se détache et l'écouteur se lit seul. Le mouvement reprend. |
| 6 | **Le haut du corps, puis la tête en bas** | 515-656 | sangles C6619, C6622, poignées C6632, bras C6624 (9,0), C6637, tête en bas C6599, punch-in sur l'écouteur C6612, puis **écran partagé** 609-656 : trois bandes, trois participantes qui tirent leur sangle (C6618, C6621, C6629, C6620, C6631) | Le même exercice, fait par toute la salle en même temps : les bandes s'ouvrent une à une sur les temps, puis les trois tirent ensemble. Le format vertical sert l'idée (trois corps empilés). |
| 7 | **La lumière passe au rouge** | 656-690 | oreille dans le rouge C6660 (ralenti), **collage** C6657 (678) | Bascule de lumière (color shift du tournage) : le rouge arrive d'abord sur une oreille. |
| 8 | **Le sommet rouge, puis la fin du cours** | 690-948 | drop C6662, rires C6665, C6664, chouchou C6658, **rafale rouge à inversions** 784-807 (C6659, C6661 2,2, C6663, C6662 2,4, C6664 3,5 ; inversions d'une image à la place des flashs blancs), bras levés C6676, C6674, C6672, allongées C6669, profil apaisé C6566 | Dans le rouge, un flash blanc ne se voit plus : l'inversion (le rouge devient cyan une image) est le flash de ce monde, signature de captured-by-h. Puis le corps se relâche. |
| 9 | **L'objet** | 948-1072 | flash, packshot rose C6725 (Gyroflow + rail), blanc C6723 (13,4), les trois C6723 (29,0) + titre | Après la séance, l'objet seul en plein jour. Les packshots gardent le travelling du cadreur, sans la main. Le titre dessiné comme la DA Sony, posé avec retenue : la vidéo est folle, la marque est calme. |
| 10 | Plan de fin Sony | 1072-1114 | fourni | — |

## Critères de réussite (mesurés sur le rendu)
| Critère | Cible |
|---|---|
| Doublons (même moment d'un rush deux fois) | **0** (`doublons_timeline.py`) |
| Tremblement (plans stabilisés) | K-O-R-E épinglées : < 1,5 px ; packshots : < 2 px autour de la trajectoire lissée, vitesse du geste gardée (0,8-1,3) |
| Packshots | aucun blanc brûlé dans le boîtier (forme d'onde, fausses couleurs) |
| Durée, format | 44,6 s ; 1080x1920, 25 i/s, **H.265 Main 10**, débit élevé, BT.709 |
| Loudness | −14 LUFS ±1, ≤ −1 dBTP |
| Photosensibilité | ≤ 3 flashs (blancs ou inversions) par seconde |
| Titre | comparé en pleine résolution à la DA Sony |
| Effets | comparés aux exemples d'eyecannndy |
