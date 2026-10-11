# Plan de montage — Sony LinkBuds Clip × KORE (V3)

_Phase 3, 2026-10-11, après les notes de Diego sur la V2 et la comparaison avec Claude nu (`comparaison.md`). Plan de la V2 : `archives/phase-3/sony-linkbuds/plan-V2.md`. Timeline Resolve : `SONY_V3` (projet `P3-sony-linkbuds-agent`). Rendu : `videos/phase-3/sony-linkbuds/rendus/sony_linkbuds_V3.mp4`._

## Intention (une phrase)
**On entre chez KORE, on met les LinkBuds Clip, et la séance monte jusqu'au rouge ; le produit se porte comme un bijou et tient la tête en bas.** Le brief demande l'excès (« kinetic, très rapide, beaucoup d'effets, beaucoup de SFX ») : cette fois je l'applique, puis je le rends propre.

## Ce qui change par rapport à la V2
| Retour de Diego | Réponse dans la V3 |
|---|---|
| Rythme mou, rafale de 15 s à faire revenir | 44,6 s au lieu de 59,6 ; **4 rafales** (199-233, 421-468, 609-656, 784-807) ; 91 plans au lieu de 68 ; 19 impacts de zoom avec flou de bougé ; 3 accélérés |
| Étalonnage « catastrophique » | Look fabriqué et jugé avant le montage (`look.md`) : S-Log3 → tirage Kodak 2383 → noirs écrasés, une seule LUT |
| Transitions « PowerPoint » | **Aucune transition intégrée.** Coupes franches, flashs (28), arrêts sur image détourés, impacts |
| Titre « PowerPoint » | Titre SST Pro Roman, révélé par le bas sous un masque, interlettrage qui se resserre, pas de grossissement |
| Packshots qui tremblent | Mesurés (`labo/outils/tremblement.py`) et stabilisés par compensation de la trajectoire mesurée (Gyroflow bloqué, voir la note) |
| Série K-O-R-E non lue | Ouverture : K, O, R, E sur les 4 temps de la première mesure, puis KORE entier |
| Détourages déclarés impossibles | 3 arrêts sur image détourés par la carte de profondeur (idée de Claude nu, reprise : image figée dans Fusion, contour net, fond calculé à travers la LUT) |
| Ordre des plans sans logique | Une progression en 9 blocs, chacun justifié ci-dessous |

## Musique (montage musical)
`messwave - easy.mp3` : **99,498 → 125,736 s** puis **133,236 → 150,5 s** (images 0-656, puis 656-1114). La coupure retire la phrase des mesures 63 à 66 et raccorde un temps fort à 125,25 s avec son équivalent à 132,75 s (même phase de 0,486 s) : appel contre appel. **À vérifier à l'oreille.** Repères mesurés (images de la V3) : coups 128 et 140 ; **silence numérique 179-185 (noir)** ; relance 187 ; **drop 233** ; appels sans basse 281, 468 et 656 ; **dernier drop 690** ; coups forts tous les 47 images ensuite (737, 784, 831, 878, 925, 972, 1019) ; dernier coup 1072 → plan de fin Sony (1072-1114).

## Structure, et pourquoi ces plans dans cet ordre
Règle (retour de Diego du 2026-10-11) : ni l'heure de tournage, ni le hasard. Le film suit **le chemin d'une participante** (dehors → dans la salle → la séance qui monte → la fin → l'objet), et à l'intérieur de la séance **le corps de bas en haut** (jambes → bras → tête en bas), parce que c'est l'ordre d'un cours de pilates et que l'épreuve du produit (tenir la tête en bas) vient en dernier. Les rafales, elles, puisent dans toute la séance : ce ne sont pas des plans à lire, mais une matière qui annonce ou résume.

| # | Bloc | Images | Musique | Plans | Pourquoi ces plans, dans cet ordre |
|---|---|---|---|---|---|
| 1 | **Le lieu, épelé** | 0-94 | mesures 49-50, montée | C6491 K, C6492 O, C6493 R, C6494 E (un temps chacun, clic à chaque lettre), C6495 KORE entier (impact), C6540 elle entre et salue | Le cadreur a tourné chaque lettre au même endroit du cadre (centre à 53 % de la largeur, mesuré) pour qu'on épelle la marque en raccords. On sait où l'on est avant de savoir ce qu'on va voir ; la première personne nous accueille d'un signe de la main. |
| 2 | **Entrer et s'équiper** | 94-179 | mesures 51-52, sans basse puis presque silence | C6505 l'allée de néons (accéléré 200 %), C6506 et C6507 les boîtiers posés sur la machine (« photos » : flash et déclencheur), C6553 toute la salle porte les mains aux oreilles, C6559 la mise au point glisse vers l'écouteur (ralenti), C6560 l'oreille et la boucle | On passe la porte : du hall clair au noir de la salle. Le produit attend sur le reformer, puis on le met. Ordre du geste : l'objet, le geste collectif, le détail sur une oreille. La musique se vide, l'image se resserre sur l'oreille. |
| — | Silence | 179-185 | silence numérique | noir | Le trou de la musique est un noir : la respiration avant la séance. |
| 3 | **La coach lance, rafale** | 185-233 | mesure 53, relance | C6550 la coach au micro (poussée lente), puis 9 plans de 6 à 2 images (sangles, pieds, fentes, écouteur, rouge, bras, souffle) | La relance musicale, c'est la coach qui démarre le cours. La rafale accélère sous le riser et montre en un éclair tout ce qui va venir (une bande-annonce de la séance), jusqu'au drop. |
| 4 | **Le bas du corps** | 233-468 | mesures 54-58, drop | C6576 la coach démontre (drop : flash, secousse, impact), fentes C6583 et C6574, **arrêt détouré orange** C6594 (appel sans basse à 281), pieds C6589 et C6590, C6587, profil en effort au ralenti C6577 (écouteur porté), C6578, C6571, C6573, C6581 entre deux néons, puis rafale 421-468 | Le cours commence par les jambes et la machine, du plan d'ensemble au détail (la coach montre, les filles font, les pieds glissent sur le chariot). Au milieu, un plan tenu au ralenti sur un profil avec l'écouteur : le produit dans l'effort, sans démonstration. La rafale finale ramasse le bloc avant l'appel. |
| 5 | **Reprendre son souffle** | 468-515 | mesure 59, appel sans basse | C6608 souffle et sourire (ralenti), **arrêt détouré sur fond noir** C6566 (sourire, écouteur) | La musique enlève la basse : on respire. Le visage humain du film, puis un portrait figé où l'écouteur se lit seul sur le noir. |
| 6 | **Le haut du corps, puis la tête en bas** | 515-656 | mesures 60-62 | sangles C6619 et C6622, poignées C6632, bras qui montent C6624 (accéléré), C6637 bras en l'air, gainage tête en bas C6599, **punch-in sur l'écouteur tête en bas** C6612, puis rafale 609-656 (gainage, tirages, néons, la coach) | On remonte dans le corps : bras, puis tout le corps à l'envers. C'est là que le produit fait sa preuve (« la tête en bas, ça n'a pas bougé », disent les participantes) : le punch-in va chercher l'écouteur à ce moment précis. |
| 7 | **La lumière passe au rouge** | 656-690 | mesure 67, appel | C6660 oreille dans la lumière rouge (ralenti, poussée), **arrêt détouré sur fond rouge** C6657 | Coupure musicale (la phrase retirée) et bascule de lumière : on entre dans le dernier effort. Le rouge arrive d'abord sur une oreille, puis sur la salle. |
| 8 | **Le sommet rouge, puis la fin du cours** | 690-948 | dernier drop, coups toutes les 47 images | C6662 drop (secousse, impact), rires en rangée C6665, C6664, chouchou C6658, mini-rafale rouge 784-807, bras levés C6676, on se redresse C6674, le bras retombe C6672, **tout le monde allongé** C6669 (ralenti), C6566 profil apaisé | La salle entière dans le rouge, l'effort puis le rire, puis le corps qui se relâche : la séance finit sur les filles allongées et un profil calme. Les coupes tombent sur les coups forts. |
| 9 | **L'objet** | 948-1072 | fin du morceau | flash, C6725 boîtier rose ouvert, C6723 boîtier blanc, C6723 les trois ouverts + titre « LinkBuds Clip » | Après la séance, l'objet seul, net, en plein jour : ce qu'elles portaient. Rupture de lumière voulue (flash blanc), puis le nom. |
| 10 | Plan de fin Sony | 1072-1114 | dernier coup | fourni, tel quel, avec son logo sonore | — |

## Effets (tous posés par le MCP, détail dans `journal.md`)
- **Impacts de zoom** (19) : 1,08 à 1,25 → 1,0 en 5 images, départ rapide, freinage long, flou de bougé (obturateur 180°). **Poussées lentes** (11) : 1,0 → 1,06-1,12. **Punch-in** sur l'écouteur (597). **Secousses amorties** sur les deux drops (233, 690).
- **Flashs blancs** (28, piste V3, mode Add) : 1 à 3 images, jamais plus de 3 par seconde (test de photosensibilité réussi).
- **Arrêts sur image détourés** (281, 503, 678) : carte de profondeur → masque → contour blanc → fond orange, noir et blanc, rouge ; « pop » d'échelle à l'entrée.
- **Grain** : piste V5, mode Overlay, opacité 35 %, désactivable.
- **SFX** : 64 sons sur 6 pistes (clics par lettre, whooshs aux coupes, déclencheurs aux arrêts, glitchs dans les rafales, risers et aspirations vers les drops, impacts aux drops). Crête calée sur l'image de l'événement.

## Critères de réussite (mesurés sur le rendu)
| Critère | Cible | Mesure V3 |
|---|---|---|
| Durée | ≤ 60 s (45 s visés) | 44,6 s |
| Format | 1080x1920, 25 i/s, H.264, BT.709 | conforme |
| Loudness | -14 LUFS ±1, ≤ -1 dBTP | -14,1 LUFS, -1,1 dBTP |
| Photosensibilité | ≤ 3 flashs par seconde | 3 au pire |
| Première image | nette et lisible avant 0,2 s | le K, plein cadre, image 0 |
| Tremblement des packshots | < 2 px de moyenne | 0,7 à 2,7 px (voir l'autocritique) |
| Noirs (5e centile de luma) | 5 à 11, comme les références | voir `autocritique.md` |
