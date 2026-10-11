# RAPPORT — synthèse de la phase 2 (en cours)

_Réécrit à chaque session (dernière : 2026-10-11, session 9). Versions précédentes : `archives/phase-2/RAPPORT-session-8.md`, `archives/phase-2/RAPPORT-session-7.md`, `archives/phase-2/RAPPORT-session-6.md`, `archives/phase-2/RAPPORT-session-5.md`, `archives/phase-2/RAPPORT-session-2.md`. La synthèse de fin de phase 1 (niveau par domaine, 10 principes, audits) est dans `archives/phase-1/RAPPORT-synthese-cloture-phase-1.md` ; le journal de la phase 1 dans `archives/phase-1/RAPPORT-journal.md`._

## Où j'en suis
- **Vague 1 des films terminée** : Interstellar, Joker, Whiplash, Le Dîner de cons, Mad Max: Fury Road (fiches dans `analyses/films/`), plus SDM « #Malentouré » (test de méthode).
- **Clips terminés** (sessions 3-4) et **pubs terminées** (session 4) : fiches dans `analyses/clips/` et `analyses/pubs/`, bilans ci-dessous. **YouTube terminé** (sessions 4 à 6) : dix fiches complètes, bilan définitif ci-dessous. **Projets Studio F42 vus** (session 6) : sept fiches dans `analyses/projets-f42/` (Hirsingen : première passe + deux séquences), bilan ci-dessous. **Vague 2 terminée** (sessions 7-8) : *La Haine*, *Avengers: Infinity War*, *Forrest Gump*, *OSS 117* ; bilan définitif ci-dessous. **Vague 3 terminée** (sessions 8-9) : *The Social Network*, *Spotlight* (comparés), *Aftersun*, *Across the Spider-Verse* ; bilan définitif ci-dessous. **Prochaine étape : passe de révision** (étape 7 de la mission).
- La mission a changé (modification de Diego dans `PROMPT-PHASE-2.md`, commitée en session 3) : une **passe de révision** (étape 7) viendra avant la synthèse finale, pour relancer les outils récents sur les premières vidéos.
- Outils de la phase 2 (`labo/outils/`) : `passe_globale.sh` (avec `HDR=1`), `courbes_film.py`, `couleur_film.py`, `sequence.py`, `verif_plan.py`, `calage.py`, `coupes_parole.py`, en session 3 `echantillon_tiers.py` (placement du sujet, à compter à l'œil), en session 8 `spectro_coupes.py` (trancher à l'œil « coupe pendant la parole ») et l'option `SEUIL=haut` de `coupes_parole.py`. `centrage.py` (saillance automatique) a échoué à la calibration : ne pas citer ses chiffres.

## Bilan de la vague 1 (cinq films)
| Film | Plans (min.) | ASL / médiane | LUFS intégré | Forme de la densité | Couleur |
|---|---|---|---|---|---|
| Interstellar | 2 317 | 4,4 / 3,0 s | -15,4 | 12 à 18 coupes/min selon les actes | une matière par monde (ferme, glace, cockpit) |
| Joker | 1 101 | 6,6 / 4,5 s | -16,2 | environ 9/min presque tout le film | vert puis rouge, mérités ; sujet décentré |
| Whiplash | 1 511 | 4,2 / 2,4 s | -18,7 | maximum (36/min) à la première répétition | ambre (musique) / vert (vie), vert supprimé au final |
| Le Dîner de cons | 1 051 | 4,6 / 3,0 s | -24,8 | plate (10 à 20/min), au tempo des répliques | beige constant, ne raconte rien |
| Mad Max: Fury Road | 2 371 | 3,0 / 2,0 s | -16,0 | **vagues de 4 à 40/min** ; le final est la crête la plus longue | jour orange, nuit bleue, visions bleu-vert ; sujet centré |

**Ce que la vague dit, du plus solide au moins solide :**
1. **Le climax n'est pas plus rapide** (quatre films sur cinq ; le cinquième, Mad Max, l'est à peine : 34 contre 31 coupes/min). Ce qui marque le sommet, ce sont d'autres leviers : le volume, le format, la fréquence de changement de ligne d'un alterné (Interstellar), et **la durée de la crête** (Mad Max, 7 min d'affilée). [VU SUR IMAGES]
2. **Les plans longs sont réservés à ce qui compte** : la preuve (l'amarrage, Andrew qui joue vraiment), le corps qui prend l'espace (Joker), la sincérité (Pignon, 28-33 s), la nouvelle la plus dure (Furiosa, 35,5 s). Cinq films sur cinq. [VU SUR IMAGES]
3. **L'après est tenu, le plus fort est suivi du plus grand vide** : silence après l'amarrage, vide après le capot (Joker), creux après la tempête et 9 s de noir avec decrescendo après le sacrifice de Nux. Variante Whiplash : le silence juste **avant** le dernier coup. [VU SUR IMAGES ; son mesuré, pas écouté]
4. **La rafale va à l'acte voulu, la surprise arrive dans le plan** (Joker, Whiplash : l'accident en un plan de 36 s). [VU SUR IMAGES]
5. **Une couleur, une matière par monde** rend lisibles des plans de 0,5 à 2 s (Interstellar, Whiplash, Mad Max) ; la couleur se mérite et change de place (Joker). [VU SUR IMAGES]
6. **La vitesse se paie en lisibilité, et trois outils la rachètent** (Mad Max) : sujet au centre (environ 20 images sur 24 au tiers central, contre 12 pour Interstellar et 8 pour Joker), un plan de géographie toutes les 5 à 10 coupes, une couleur par lieu. Inversement, le décentrage va avec les plans tenus (Joker). [VU SUR IMAGES, échantillon jugé à l'œil]
7. **Plus un film coupe vite, plus il doit respirer** : Mad Max, le plus rapide, a le plus grand écart creux/crête (facteur 10). La règle « respiration obligatoire » du kinetic tient à l'échelle de deux heures. [VU SUR IMAGES]
8. **Ce qui ne monte pas** : un film de musique n'est pas forcément monté au beat (Whiplash, calage = hasard) ; une comédie de dialogue a une densité plate (Dîner de cons). [mesuré]
9. **Le timing comique sans public** (Dîner de cons) : environ 20 % des coupes au milieu d'une phrase (révisé en session 9 à l'œil ; l'outil disait 40-44 %, et autant dans la scène sincère), environ 0,35 s d'air sinon ; l'air (1,5-3 s) réservé aux chutes. [mesuré, VU SUR IMAGES]

**Ce que la vague a corrigé de la phase 1** : la contraction 8 / 4 / 2 / 1 s d'Interstellar (fausse : deux temps et une rupture) ; « extérieurs silencieux » ; « l'image de Joker s'assombrit » ; « le rouge remplace le vert » ; « la danse des toilettes en un seul plan ». Cinq affirmations de phase 1 corrigées sur les deux films de Diego : les fiches écrites sur des textes étaient justes dans l'esprit, fausses dans les chiffres.

**Pour Studio F42** (projets « souvent énergiques », GOUTS.md) : de cette vague, ce qui sert le plus vite est Mad Max pour le kinetic (respiration franche, sujet centré dans le 9:16, plan d'orientation), et Joker / Interstellar pour la retenue (plan tenu sur ce qui compte, couleur par monde). À éprouver en maquette avant d'en faire des règles de studio.

## Bilan des clips (huit, terminés en session 4)
| Clip | Plans (min.) | Médiane | LUFS | Calage (contre le hasard) | Forme |
|---|---|---|---|---|---|
| SDM « #Malentouré » | 28 | 3,9 s | — | non (structure du morceau) | plans-séquences de couplet, deux blocs découpés |
| Ziak « Même pas un grincement » | ~109 | 1,2 s | — | non ; densité selon la basse (32 / 16 coupes/min) | rapide sans kinetic |
| Justice « Stress » (Gavras) | 57 | 4,2 s | — | **grands accents** (38 % / 20 %) | plans portés longs, reportage |
| PNL « Au DD » | 75 | 2,9 s | — | non | régulier, trois plans longs aux articulations |
| Booba « 6G » | 74 | 1,7 s | — | non | intro trouée, une seule rafale, plans longs en mouvement |
| GENER8ION « STORM » (Gavras) | 142 | 1,5 s | -12,9 | **grands accents** (30 % / 19 %) | 131 plans en 4 min 17, puis le sommet en 5 plans de 21 à 60 s |
| HOUDI « Belle chanson » | 35 | — (ASL 6,2 s) | -10,9 | non (sur musique séparée) | niveau de jeu vidéo : traversées raccordées par le noir |
| Yvnnis « Gare du Nord » | ≥ 60 | 2,4 s | -11,6 | non | réseaux : mosaïque, rafale-inventaire, carte finale |

**Ce que les clips disent, du plus solide au moins solide :**
1. **Personne ne coupe sur les temps plus qu'au hasard** (huit sur huit, contrôlé sur la musique séparée quand il le fallait). Le rapport à la musique est ailleurs : la densité suit l'arrangement (Ziak, SDM), ou les rares coupes tombent sur les grands accents (les deux Gavras, 10 à 18 points au-dessus du hasard). Le calage sur les temps reste un trait du kinetic des réseaux, que je n'ai pas encore mesuré sur une vraie vidéo. [mesuré]
2. **Le sommet d'un clip n'est pas sa partie la plus rapide** : STORM le pousse au bout (33 coupes/min, puis 1 à 7 pendant la chorégraphie), comme les films de la vague 1. [VU SUR IMAGES]
3. **Les plans longs d'un clip sont des mouvements qui relient** (individu → foule, pièce → paysage, lieu → lieu dans un jeu), placés aux articulations ; entre eux, un rythme régulier ou **une seule rafale**, souvent un inventaire (devantures de Gare du Nord, toits de 6G). [VU SUR IMAGES]
4. **Dans un mix en plateau (-10 à -13 LUFS), les rares silences sont des ponctuations**, et le plus fort ouvre le sommet plutôt qu'il ne le clôt (Stress 0,6 s avant la bagarre, STORM 2 à 4 s quand Yung Lean se retourne). [mesuré, pas écouté]
5. **L'ouverture construit l'image** (cadre qui grandit, mosaïque, cartons sur noir puis plans lents et muets) et **l'habillage vient du sujet** (plan de métro, interface de jeu) : aucun des huit clips n'a de carton décoratif. [VU SUR IMAGES]
6. **Une couleur par monde, ou une couleur qui voyage** : froid → chaud (6G), horreur froide / écran chaud (HOUDI), refroidissement progressif (STORM). [mesuré]
7. **Fiabilité de mes fiches de phase 1** : celles qui avaient mesuré tiennent (Ziak : seul le nombre de plans était faux) ; celles écrites sans voir avaient faux 4 affirmations sur 9 (Stress, Au DD). Et en phase 2 même, j'ai failli écrire un calage faux sur le mixage (HOUDI) : une mesure sans contrôle peut mentir autant qu'un souvenir.

**Pour Studio F42** : le clip est peu demandé (GOUTS.md), mais trois principes passent au film de marque : la rafale-inventaire puis le plan tenu (présenter un lieu, une équipe), l'ouverture qui construit l'image, et le sommet porté par le cadre plutôt que par la coupe. À éprouver en maquette.

## Bilan des pubs (sept, session 4)
| Pub | Durée | Plans | Médiane | LUFS | Forme | Marque |
|---|---|---|---|---|---|---|
| Intermarché 2017 « L'amour » | 3:00 | 105 | 1,6 s | -23,1 | récit chanté, 90 % des plans de 0,9 à 2,6 s, fin qui ralentit | décor dès 0:00, nom à 2:55 |
| Intermarché « Conte de Noël » | 2:30 | 98 | 1,2 s | -23,1 | réel → conte animé → réel ; silence avant l'acceptation | carton puis nom à 2:28 |
| Lacoste « Life is a Beautiful Sport » | 1:11 | 47 | ~1,1 s | -23,2 | course à travers Paris, un plan long, 2,4 s de silence avant la fin | tenue dès 0:00, logo à 1:08 |
| iPhone 17 « Scratch Resistant » | 0:35 | 18 | — (ASL 2 s) | -16,1 | gag de genre tenu en plan large silencieux | objet dès 0:00, texte à 0:26 |
| Crunch Creator (bande-annonce) | 2:22 | 45 | — (ASL 3,2 s) | -15,7 | deux tirades en plans tenus encadrent l'action truquée | date à 2:02 |
| GP Explorer 3 (bande-annonce) | 2:17 | 64 | 1,1-1,3 s | -10,0 | line-up par paquets entre deux vols continus | logo à la fin |
| adidas « Backyard Legends » | 5:05 | 181 | ~1,1 s | -14,2 | narrateur peu fiable, format et couleur par époque | tenues, logo à 5:01 |

**Ce que les pubs disent :**
1. **Le nom de la marque arrive dans les dernières secondes dans les sept ; ce qui la représente (lieu, tenue, objet, couleur) est à l'écran dès la première image.** La règle télé « marque dans les 5 premières secondes » n'est tenue que par l'objet, jamais par le nom. [VU SUR IMAGES]
2. **Aucune ne coupe sur les temps plus qu'au hasard** (Crunch Creator : légère tendance aux accents, à la limite du hasard). Treize vidéos testées sur treize (huit clips, cinq pubs ; adidas et iPhone non testés), plus Whiplash : le calage sur les temps n’apparaît dans aucune des œuvres de référence mesurées, hors kinetic (pas encore mesuré). [mesuré]
3. **Les films longs (2 min 30 à 5 min) tiennent par une cadence régulière de 1 à 2 s et un récit**, pas par des variations de rythme ; la variation est réservée à la fin (un plan tenu) ou au gag (un plan large). [mesuré, VU SUR IMAGES]
4. **Le silence ouvre le sommet** (Lacoste 2,4 s, Conte de Noël 0,5 s), comme dans les clips (STORM, Stress). [mesuré, pas écouté]
5. **Une matière par monde, avec le format d'image en plus** : adidas (large froid / 4:3 chaud), Conte de Noël (réel / animation, forêt bleue / terrier orange), HOUDI (fiction froide / écran chaud). [VU SUR IMAGES]
6. **Couper sur le mot** quand un conteur porte le film (adidas : 68 % des coupes pendant la parole, la voix est une bande continue) ; **tenir la tirade** quand la parole est le spectacle (Crunch Creator, 10 et 16 s). [mesuré]
7. **Deux familles dans le choix de Diego** : le récit de marque émotionnel ou comique à la française (deux Intermarché, Lacoste, adidas, iPhone) et la bande-annonce d'événement de créateurs (Crunch Creator, GP Explorer 3), qui ressemble le plus aux commandes probables du studio. [DÉDUIT, à confirmer avec les projets F42]

**Pour Studio F42** : deux formules réutilisables tout de suite, à éprouver en maquette : (a) **la marque comme lieu ou costume** et le nom en signature ; (b) pour un événement de créateurs, **les noms par paquets de couleur** et un vol continu pour entrer et sortir.

## Bilan YouTube (dix vidéos, sessions 4 à 6 : définitif)
| Vidéo | Durée | Plans (min.) | Médiane | LUFS / LRA | Famille | Forme |
|---|---|---|---|---|---|---|
| B-roll (tutoriel) | 8:40 | — | — | -11,7 | tutoriel | interview couverte par du stock qui raconte |
| EGO « Bibliothèque-Univers » | 23:22 | — | — | -21,3 | doc | vagues de 3 à 29 coupes/min commandées par le texte ; chapitres par le noir et le silence |
| « Les Jeux Tiger » | 31:02 | 569 | 2,2 s | -16,6 / 4,8 | doc | présentateur ; liste → rafale, thèse → tirade, preuve → test tenu |
| « Le jour où la CIA… » | 48:58 | 930 | 2,2 s | -16,7 / 6 | doc | doc-thriller ; un cadre par source ; schéma qui se transforme = plus long plan (46 s) |
| « Créer YggTorrent » | 1:11:20 | 651 | 4,8 s | -22,0 / 5,2 | doc | enquête ; témoins anonymes = mannequin + couleur + police ; plans de 24-45 s |
| « Qui est l'imposteur » × 2 | 57:19 / 54:38 | 1 590 / 1 426 | 2,0 s | **-12,0 / 3,8** | plateau | multicaméra ; **densité plate, aucun silence** |
| « POPCORN » | 2:32:06 | 2 450 | 2,5 s | -18,2 / 7,7 | plateau | talk-show ; 15-20 coupes/min ; crêtes = inserts ; récits tenus |
| Philippe Boxho (LEGEND) | 1:07:44 | 929 | 3,4 s | **-24,0 / 9,7** | conversation | interview-conteur ; champ / contrechamp ; 308 silences gardés |
| « KAIZEN » (Everest) | 2:26:38 | 2 372 | 2,6 s | -17,0 / **12,3** | cinéma | vagues de 3 à 50 coupes/min ; sommet lent après une rafale de souvenirs et 5 s de silence |

**Ce que les dix vidéos disent, du plus solide au moins solide :**
1. **La densité suit le type de phrase, dans toutes les familles.** Une liste dite reçoit une image par élément (0,5 à 1,8 s : EGO, Tiger, CIA, ouverture de KAIZEN) ; une thèse un plan tenu face caméra ; une preuve un plan tenu en temps réel (Tiger, 12-19 s) ; **un récit d'invité un gros plan tenu 5 à 16 s, un échange des plans de 1 à 4 s** (Popcorn). Cinq vidéos sur cinq où je l'ai cherché (EGO, Tiger, CIA, KAIZEN, Popcorn). C'est la règle la plus générale de la phase 2, et le même geste que la rafale-inventaire des clips (Gare du Nord, 6G). [VU SUR IMAGES, mesuré]
2. **Le plus long plan porte la thèse, la preuve ou l'épreuve, et quelque chose change à l'intérieur** : schéma qui se transforme (CIA 46 s, EGO), citation qui s'écrit au rythme de la voix (Tiger 23-29 s), relevé d'écoute (CIA 27 s), sous-titre mot à mot d'un témoin (Ygg 24-45 s), **compte à rebours d'une manche de jeu** (Popcorn 62 et 68 s, écran partagé). **Le texte ou le compteur tient le plan long** ; le montage n'a pas à couper. [VU SUR IMAGES]
3. **Quatre familles, quatre régimes de son et de rythme** : le **doc** (densité en vagues, chapitres par le noir et 2-4 s de silence, silences rares donc lisibles) ; le **plateau** (densité plate ; -12 LUFS sans aucun silence pour le jeu, -18 avec des récits tenus pour le talk-show) ; la **conversation** (Boxho : plate et calme, -24 LUFS, 308 pauses gardées) ; le **cinéma sur YouTube** (KAIZEN : règles des films, LRA 12,3 LU). La règle « respirer par le montage » vaut pour le doc et le cinéma ; le plateau respire par les rires, les décors et les récits. [mesuré]
4. **Sommet d'émotion lent, sommet d'information rapide** : KAIZEN suit les films (la crête de 45 coupes/min est **juste avant** le sommet, une rafale de souvenirs coupée par 5 s de silence ; le sommet en plans larges de 3,6 à 22 s), Tiger met sa partie la plus rapide au sommet de son récit (l'emballement Furby). [VU SUR IMAGES]
5. **Dans la conversation filmée, le changement d'angle ignore la parole** : 76 à 88 % des coupes pendant la parole pour environ 80 % du temps parlé (Popcorn, sur 9 min), 71 % / 77 % (Boxho) ; quand la coupe tombe dans un trou, c'est **0,1-0,2 s avant la reprise**, sur celui qui va parler. Le jeu coupe un peu plus dans les trous (Imposteur, 49 % / 77 %), la comédie de dialogue de cinéma cherche l'air (*Le Dîner de cons*, 40-44 %, au milieu d'un trou de 0,8 s). [mesuré ; voix séparée quand il y a un fond musical, mixage vérifié équivalent sans fond]
6. **Changer de cadre ou de format pour changer de régime** : archive dans un téléviseur arrondi (CIA), aparté en sépia (Tiger), un décor par lieu de jeu (Imposteur), **un format par époque** (KAIZEN : archives N&B, webcam 4:3, défis 16:9, comme adidas), extrait en écran partagé avec la réaction (Popcorn). Prolonge « une matière par monde » des films. [VU SUR IMAGES]
7. **Les crêtes de densité d'un format de plateau viennent des inserts** (rubrique d'extraits à 28-36 coupes/min, jeu), jamais de la conversation ; l'extrait n'est jamais montré seul : le visage qui le regarde reste à l'écran. [VU SUR IMAGES]
8. **Les rafales ont un sens, et une seule couleur** : KAIZEN oppose deux rafales (le trop-plein de la vie de créateur à 1:08, l'entraînement à 1:12) ; celle de l'entraînement tient sous **une voix qui ordonne** (vocal du coach), d'une seule couleur (bleu), et le mot-clé reçoit son image littérale (« réveille-toi » → un œil qui s'ouvre). **Un voyage se compresse au métronome** de cartons « JOUR N », l'arrivée casse la cadence par le premier plan long. [VU SUR IMAGES]
9. **Un format de série est un système** : les deux « Imposteur » ont les mêmes chiffres à 10 % près et le même habillage ; Popcorn a un décor, un logo permanent, des cartons nom et un générique en mise en page. [mesuré]
10. **Trois façons d'isoler un sponsor** : le jouer en sketch (Tiger), l'isoler par la forme et le silence (EGO), par le décor et le tempo (Imposteur) ; Popcorn le garde pour la fin (26 s sur noir). [VU SUR IMAGES]
11. **L'habillage vient du monde du sujet** : interface d'envoi de YouTube comme charnière vers le titre (KAIZEN), une voix sans visage = un avatar, une couleur, une police (Ygg) ; ouvrir par la fin (Ygg, CIA) ou par l'inventaire du décor (Popcorn). [VU SUR IMAGES]
12. **Le volume n'est pas une norme chez les créateurs** : de -24,0 (Boxho) à -11,7 (B-roll), 12 LU d'écart ; la dynamique (LRA de 3,8 à 12,3) dit la famille mieux que le niveau. [mesuré]
13. **Des traces de montage automatique se mesurent** : Boxho a 89 plans de 1,52 s exactement et des pics de durée à 2, 4, 6, 8 s. Hypothèse, non prouvée. [mesuré, interprétation DÉDUITE]

**Ce que YouTube a corrigé ou nuancé** : « respirer par le montage » ne vaut pas pour le plateau ; « couper à la fin d'une pensée » (montage-grammaire) ne vaut que pour ce qu'on retire, pas pour le changement d'angle ; « le climax n'est pas plus rapide » (films) ne vaut que pour le sommet d'émotion. Skills mis à jour : `montage-youtube` (16 à 16 sexies), `montage-grammaire` (conversation multicaméra), `montage-rythme` (KAIZEN).

**Pour Studio F42** (à éprouver en maquette avant d'en faire des règles de studio) :
- **Corporate explicatif et film de marque** : densité selon le type de phrase ; le schéma qui se transforme comme plan-thèse ; un format ou un cadre par époque pour un historique d'entreprise.
- **Commande récurrente** (série, podcast de marque) : un système (cartons, couleur par décor, tempo fixe), un récit tenu, un extrait toujours avec le visage qui le regarde.
- **Témoignage anonyme** : un avatar, une couleur, une police.
- **Fin de film de marque ou d'événement** : rafale de mémoire d'une seule couleur, silence, puis plan tenu.

## Bilan des projets Studio F42 (sept, session 6)
| Projet | Format | Durée | Plans | Médiane | LUFS / LRA | True peak | Verdict |
|---|---|---|---|---|---|---|---|
| Benefit 1 (café) | pub réseau 9:16 | 0:23 | 9 | ~2,2 s | -14,5 / 3,1 | -0,6 | pas livrable : le produit ne cause rien (le regard arrive avant le produit) |
| Benefit 2 (roses) | pub réseau 9:16 | 0:26 | 7 | ~2,2 s | -14,7 / 3,3 | 0,0 | presque : le flou est l'idée (« blur »), mais 4,4 s avant le premier écran net |
| Oney (intro quiz) | 1:1 mobile | 0:37 | ≥ 12 | — | -13,5 / 5,4 | **+3,1** | montage livrable, fichier non : son saturé ; 2,5 s de noir final ; HEVC 10 bits |
| Swile « POW » | pub 16:9 | 1:19 | 26-38 | 2,6 s | **-11,1** / 5,0 | -0,8 | livrable après -14 LUFS et une piste stéréo ; le plus abouti des projets courts |
| Sephora × Laneige | brand content 9:16 | 2:46 | 73 | 2,0 s | -17,1 / 7,0 | -0,1 | pas livrable muet : sous-titres fins à ~2,5:1 ; 45 s avant le jeu |
| « Fou-Rire » | court métrage 2:1 | 2:21 | 47 | 1,9 s | -23,3 / 12,0 | -1,6 | livrable festival ; plans du public noirs, loge sans ambiance |
| « Hirsingen » | court métrage 2,35:1, 5.1 | 15:00 | ≥ 118 | 4,6 s | **-27,3 / 20,9** | 0,0 | image et montage maîtrisés ; mixage non diffusable hors salle |

**Ce que les projets disent du studio, du plus solide au moins solide :**
1. **La finition son est le point faible commun, et il est mesurable** : **six fichiers sur sept au-dessus de -1 dBTP** (Oney à +3,1 avec des crêtes décodées au-dessus de 0 dBFS), des niveaux de -11 à -27 LUFS sans lien avec la destination, deux pistes mono au lieu d'une stéréo (Swile), une dynamique de 20,9 LU (Hirsingen). Seul « Fou-Rire » passe. C'est la correction la moins chère et la plus rentable : un QC fixe avant chaque envoi (`labo/outils/qc_livraison.sh`, créé en session 6). [mesuré]
2. **Les fictions sont plus maîtrisées que les commandes courtes** : « Fou-Rire » et « Hirsingen » tiennent les principes des films de la vague 1 (plan long réservé à ce qui compte, rythme de l'état intérieur, couleur par lieu, le plus fort suivi du vide, changement de grammaire de caméra à la rupture). Les commandes ont de bonnes idées (le flou de Benefit 2, le POW de Swile, le jeu de Sephora) mais pèchent par **la lisibilité muette** (sous-titres de Sephora, flou d'ouverture de Benefit) et **la liaison** (Benefit 1). [VU SUR IMAGES]
3. **Le meilleur moment de chaque commande est quand la forme dit le bénéfice** : le flou qui révèle pour un produit qui « floute » (Benefit 2), une seule carte au lieu d'un portefeuille (Swile), les questions du jeu qui sont la formule du sérum (Sephora), la liste des lots collée sur la chemise au mot (Oney). C'est la règle « le gag porte le bénéfice » des pubs de référence ; le studio l'applique quand il a une idée de forme. [VU SUR IMAGES]
4. **Deux habitudes de son en fiction** : des dialogues sans ambiance continue (le son tombe au plancher entre les répliques dans la loge de « Fou-Rire » et à la bougie de « Hirsingen ») et des plans très sombres où l'information disparaît (le public de « Fou-Rire », Franz en plan large), alors que la règle dictée par Diego est « un minimum de lumière sur l'info ». [mesuré, VU SUR IMAGES ; son pas écouté]
5. **Le montage coupe juste par rapport à la parole selon le genre** : la fiction grave laisse l'air (Hirsingen, 27-42 % des coupes pendant la parole), comme le cinéma de référence. [mesuré]
6. **La marque est un lieu ou un objet dès le début dans les commandes** (table imprimée de Benefit, décor de Sephora, plateau de Swile), comme les sept pubs de référence ; le nom vient tôt seulement quand on parle à des clients déjà acquis (Oney), ce qui est juste. [VU SUR IMAGES]

**Montage ou tournage** : presque tout ce qui manque se corrige **au montage et à la finition** (ordre des plans de Benefit 1, flou d'ouverture, sous-titres, QC son, ambiances, étalonnage des plans noirs). Au tournage, trois choses à préparer : l'insert produit et l'insert peau (Benefit), un signe de couleur par équipe (Sephora), la lumière du public et les ambiances de salle (« Fou-Rire »).

**Pour le studio, dans l'ordre** : (1) QC son systématique ; (2) un passage « muet » de chaque commande réseau (sous-titres gras et contrastés, premier écran net avant 2 s) ; (3) vérifier que l'ordre des plans dit la cause dans les pubs sans voix ; (4) une ambiance continue sous tout dialogue de fiction.

## Bilan de la vague 2 (quatre films, définitif, session 8)
| Film | Plans (min.) | ASL / médiane | LUFS intégré | Forme de la densité | Image |
|---|---|---|---|---|---|
| La Haine | ≥ 347 | ~16 / 8,2 s | -19,9 | sous 10 coupes/min, deux crêtes seulement (générique d'archives, mort d'Abdel) | N&B, noir toujours atteint ; la nuit baisse, ne contraste pas plus |
| Avengers: Infinity War | ≥ 2 237 | 4,0 / 2,6 s | -24,7 | vagues de 10 à 33/min, crête à New York (minute 23), pas à la fin | sombre et froid puis clair et chaud |
| Forrest Gump | ≥ 1 004 | 8,5 / 4,65 s | -25,4 (VF) | vagues courtes de 3 à 24/min, crête sur un résumé d'archives | à mesurer par époque |
| OSS 117 : Le Caire | ≥ 1 317 | 4,5 / 2,9 s | -21,8 | plate, 10 à 22/min ; bagarre à ~28/min ; la crête finale (30/min) est fausse (explosions) | beige chaud, blocs de nuit américaine bleue ; N&B pour le prologue de 1945 |

**Ce que la vague dit, du plus solide au moins solide :**
1. **Le climax n'est pas plus rapide** : quatre films sur quatre (neuf sur neuf avec la vague 1 ; Mad Max l'est à peine). La fin de *La Haine* a une durée moyenne de plan de 16 s, le claquement d'*Avengers* est à 10 coupes/min, la fin d'*OSS 117* n'accélère qu'en apparence. [mesuré, VU SUR IMAGES]
2. **L'après est tenu, le plus fort suivi du vide** : *Avengers* ralentit par paliers après le claquement (médiane 1,8 → 2,3 → 4,6 → 23,8 s, son de -25 à -37/-42 LUFS) ; *La Haine* met un carton silencieux puis un plan de 25,6 s qui monte de 30 LU jusqu'à un coup de feu hors champ. [mesuré, VU SUR IMAGES]
3. **Le principe n'est pas « plan long = important », c'est l'écart à la norme** : dans *La Haine*, où le plan long est la règle (101 plans de 15 s ou plus), ce sont les deux seules rafales qui signalent. C'est l'apport le plus général de la vague : il recadre le principe n° 2 de la vague 1. [VU SUR IMAGES]
4. **Deux façons d'alterner** : *Interstellar* (le goût de Diego) accélère ses changements de ligne ; *Avengers*, avec cinq ou six lignes, monte par blocs de 1,5 à 7 min qui ne raccourcissent pas, et fait monter la tension en **faisant voyager un personnage d'une ligne à l'autre**. [VU SUR IMAGES, classement à l'œil à ±10 s]
5. **La rafale pour l'acte, le plan tenu pour la menace, le corps ou le gag** : ouverture d'*Avengers* (35 et 41 s, puis 1-2 s quand la violence commence), embuscade de *Forrest Gump* (attaque hachée, sauvetages tenus 19 à 40 s), bagarre d'*OSS 117* (coups en 0,5-2 s, mais le poulet tenu comme une arme en 5,6 s). [VU SUR IMAGES]
6. **Une liste dite, une image par élément** (*Forrest Gump* : cinq pluies, cinq plans ; la course, un plan par étape), suivie d'un plan tenu sur la relation (69 s). Deuxième famille après YouTube. [VU SUR IMAGES, mesuré]
7. **Le silence avant**, en drame comme en comédie : 30 s de quasi-silence avant « Je suis fatigué » (*Forrest Gump*), une attente presque muette avant la bagarre (*OSS 117*) ; **un carton récurrent peut être un trou de son** qui scande le film (*La Haine*, 13 cartons-horloge). [mesuré, pas écouté]
8. **La comédie de dialogue a une densité plate et presque pas d'air** (*OSS 117* comme *Le Dîner de cons*) : la coupe tombe au ras de la réplique (sur la dernière syllabe ou moins de 0,1 s après, tranché à l'œil sur 20 coupes) ; échange en champ-contrechamp rapide, gag de situation ou d'objet dans un plan qui dure. [VU SUR IMAGES ET SPECTROGRAMMES]
9. **Une matière par époque, et l'habillage vient du genre imité** : N&B pour 1945 et couleur pour 1955, nuit américaine, logo Gaumont d'époque, carton « FIN », casting nominatif (*OSS 117*) ; archives et formats par décennie (*Forrest Gump*). Même règle que les pubs (adidas) et YouTube (KAIZEN). [VU SUR IMAGES]

**Ce que la vague a corrigé** : ma méthode plus que mes skills. Trois « plans longs » faux sur trois films (*La Haine* 171,6 / 173 / 195 s, la plume de *Forrest Gump*, le guet d'*OSS 117*) : la nuit et le sombre cachent des coupes même aux outils de vérification. Et ma mesure « coupes pendant la parole » par énergie est une borne haute, très haute sur la voix séparée (90 % contre 20 % à l'œil). Aucun principe de la vague 1 n'est contredit ; un est recadré (l'écart à la norme), deux sont étendus (alterné par blocs, silence avant la chute comique).

**Comparaison des deux vagues** : la vague 1 (les goûts de Diego et des formes extrêmes) a donné les principes ; la vague 2 (films populaires, deux comédies, un N&B) les a mis à l'épreuve de normes différentes, et ils tiennent. Ce qui change d'un film à l'autre, c'est **la norme** (plan de 16 s chez Kassovitz, de 2,6 s chez les Russo) ; ce qui reste, c'est **le rapport à la norme** aux moments qui comptent.

**Pour Studio F42** (à éprouver en maquette) : pour une pub parodique, imiter le genre jusqu'au générique et tenir le plan de l'objet absurde ; l'horloge sur noir avec trou de son pour un film sur une journée (événement, making-of) ; l'alterné par blocs avec un personnage qui relie les lieux pour un événement multi-sites ; la liste dite illustrée au même rythme puis le plan tenu, pour tout film de marque à voix off ; dans un dialogue de comédie, couper au ras de la réplique et garder l'air pour la chute.

## Bilan de la vague 3 (quatre films, définitif, session 9)
| Film | Plans (min.) | ASL / médiane | LUFS intégré | Forme de la densité | Image |
|---|---|---|---|---|---|
| The Social Network | ≥ 2 287 | 3,2 / 2,2 s | -20,9 | haute et plate (15-30/min), crêtes sur Facemash (44) et Henley (41) | sombre et ambrée (Y 41, comme *Whiplash*) |
| Spotlight | ≥ 1 182 | 6,6 / 4,1 s | -20,3 | basse et plate (4-15/min), aucune vraie crête | claire, neutre, la moins saturée des films en couleur |
| Aftersun | ≥ 458 (film seul) | 12,3 / 5,5 s ; **7,5 s hors raves** | **-26,4** | presque plate (3-8/min), trois crêtes = les trois raves | quatre textures : 35 mm, MiniDV, rave noire, présent froid |
| Across the Spider-Verse | ≥ 2 826 (film seul) | **2,8 / 1,96 s** | -21,3 | médiane 20/min, de 5 à 60 ; crête au récapitulatif (minute 2) | une matière graphique par monde |

La vague va des deux extrêmes du corpus : le film le plus lent et le plus calme (*Aftersun*) et le plus rapide (*Spider-Verse*), plus deux films de dialogue opposés (*Social Network* / *Spotlight*).

**Ce que la vague dit, du plus solide au moins solide :**
1. **Le climax n'est pas plus rapide** : treize films sur treize maintenant. Même le film le plus rapide (*Spider-Verse*) met sa crête au récapitulatif de la minute 2 et finit à sa médiane (environ 21 coupes/min). [mesuré]
2. **Ce qui signale, c'est l'écart à la norme, dans les deux sens** : *Aftersun* (72 % de la durée en plans de 15 s ou plus) réserve ses seules rafales aux raves, l'espace mental de l'adulte ; *Spider-Verse* (médiane 1,96 s) ralentit seulement de moitié pour sa scène intime ; *The Social Network* finit sur ses plans les plus longs. La règle de la vague 2 (*La Haine*) tient sur les deux extrêmes. [VU SUR IMAGES, mesuré]
3. **Une matière par monde rend la vitesse lisible** : poussée au bout par *Spider-Verse* (un style graphique par univers, plans de 0,5 s lisibles), et retournée en mémoire par *Aftersun* (une texture par temps). Nouveau : **dans un même monde, la couleur peut suivre l'émotion plan par plan** (Gwen et son père). [VU SUR IMAGES]
4. **La révélation par la voix, le plan tenu sur celui qui reçoit** (*Spotlight*, appels de 67 et 115 s) ; **la gêne tenue sur celle qui la vit** (*Aftersun*, karaoké en cinq plans, un seul contrechamp). Les plans les plus longs vont à la réception, pas à l'information. [VU SUR IMAGES]
5. **Unir les temps par un mouvement, pas par une coupe** (*Aftersun*, dernier plan de 160 s : archive → présent → souvenir) ; **ouvrir sur la fin rendue illisible** (la cassette rembobinée). Nouveau dans le corpus. [VU SUR IMAGES]
6. **Le son le plus fort marque l'écart entre les personnages, pas la fête** (*Aftersun* : les deux minutes les plus fortes sont deux chansons refusées) ; et le plus fort est suivi du plus grand vide (12 s de noir dont 8 de silence, puis 16 s de couloir vide avant le générique). Exception attendue : une fin de première partie (*Spider-Verse*) coupe net sur un carton. [mesuré, pas écouté]
7. **Le dialogue** : la part de coupes pendant la parole ne distingue pas Fincher de McCarthy (30 % chacun, à l'œil sur spectrogramme) ; l'air entre les répliques et la durée des plans, si. [VU SUR SPECTROGRAMME]
8. **Le calage sur les temps reste absent** des œuvres de référence : *Spider-Verse* (récapitulatif et batterie) = hasard sur les temps, à peine au-dessus sur les accents (56 % contre 46 %, limite du 95e centile). La rafale y est structurée par la voix (un refrain répété quatre fois). [mesuré sur musique séparée]
9. **La liste, un élément par plan ou par carton** (Facemash, cartons de *Spotlight*) : cinquième et sixième cas du corpus. [VU SUR IMAGES]

**Fiches de phase 1 confrontées** : *The Social Network* juste dans l'esprit, fausse sur trois chiffres ; ***Aftersun* sans erreur relevée**, peut-être parce qu'elle ne donnait aucun chiffre ; aucune fiche sur *Spotlight* ni *Spider-Verse*.

**Ce que la vague a corrigé** : ma méthode encore. J'avais annoncé en session 8 que la crête des minutes 44-47 d'*Aftersun* était « les stroboscopes de la rave » ; c'est un magasin de tapis où le détecteur sature (environ 60 fausses coupes, 5 vraies). Les séries de « plans » à la durée minimale (0,5 s) signalent un détecteur saturé (tapis, générique, personnage animé en collage).

**Comparaison des trois vagues** : la vague 1 a donné les principes, la vague 2 les a éprouvés sur des films populaires et deux comédies, la vague 3 sur les extrêmes de vitesse. Les principes de structure (climax pas plus rapide, écart à la norme, une matière par monde, vide après le plus fort) tiennent de la médiane 1,96 s à la médiane 7,5 s. Ce qui change avec la vitesse, c'est **l'amplitude des écarts**, pas leur logique.

**Pour Studio F42** (projets « souvent énergiques », GOUTS.md ; à éprouver en maquette) : *Spider-Verse* est la référence la plus utile pour un kinetic de marque : une texture par univers (produit, pays, gamme) avant d'accélérer, une voix off en refrain pour structurer une rafale, le logo redessiné dans le langage du film. *Aftersun* pour un film de marque lent ou un portrait : garder la seule rafale pour un seul moment, unir passé et présent par un mouvement, finir sur le décor vide. Le grain et le look film que Diego préfère (réponse 7) ont dans *Aftersun* une fonction (deux supports, deux temps) : c'est mon rapprochement, pas sa parole.

## Erreurs corrigées (phase 2)
- Session 9 : j'avais écrit (PROGRESS de session 8) que les « plans » de moins de 1 s d'*Aftersun* aux minutes 44-47 étaient les stroboscopes de la rave, sans regarder : c'est un magasin de tapis, plans fixes où le détecteur déclenche toutes les 0,5 s. Et `calage.py` plantait sur la virgule finale de `ffprobe` (corrigé).
- Session 8 : la mesure « coupes pendant la parole » d'*OSS 117* (57 % mixage / 90 % voix séparée) : tranchée à l'œil sur spectrogramme, 4 coupes sur 20 seulement sont clairement pendant la parole. Cause : le seuil « plancher + 10 dB » de `coupes_parole.py`, absurde sur une voix séparée (plancher numérique). Option `SEUIL=haut` ajoutée ; les chiffres sur voix séparée de YouTube (POPCORN 82 %, Boxho 71 %, Imposteur 49 %) sont à refaire. Et un « plan » de 13,2 s du guet d'*OSS 117* contient une coupe cachée dans le noir.
- Session 7 : le « plan suivi de 171,6 s » de *La Haine* (fiche de session 6) contient une coupe cachée dans le noir d'une cage d'escalier (113,5 + 57,7 s) ; deux « plans » de nuit de 173 et 195 s en contenaient 27 et 9 ; le « plan de la plume » de *Forrest Gump* (159 s) se termine par quatre ou cinq plans rapprochés que `verif_plan.py` n'a pas vus.
- Session 6 (projets F42) : dans la fiche Swile, j'avais cité le true peak (-0,8 dBTP) sans le signaler ; en recoupant les fichiers, il dépasse lui aussi -1 dBTP (six fichiers sur sept). Et sur une tuile à 1 image / 2 s de Hirsingen, une grosse amorce (un manteau au premier plan) m'a fait croire à une alternance de plans : à 4 images/s, c'est un seul cadre.
- Session 6 : j'avais écrit « *Le Dîner de cons* : 35 % des coupes pendant la parole pour 60 % du temps » dans les constats YouTube ; la fiche mesurée dit 40-44 % (21 % dans la scène sincère). Chiffre recopié de mémoire : toujours reprendre une mesure dans sa fiche, pas dans un résumé.
- Session 1 : j'avais cru faux le plan de 74 s de Pogo's (c'est un plan-séquence) ; j'avais attribué à Diego une note sur l'amarrage qui n'était qu'un exemple de format (retour du 2026-10-11, intégré).
- Session 5 : le « plan » de 19,7 s de Tiger (graphique puis présentateur, coupe ratée) ; « les deux extrémités les plus rapides » de CIA (la fin l'est surtout par son générique monté) ; « le témoin à la bougie » de CIA (deux témoins, deux lumières) ; la mesure coupes / parole sur un mixage avec fond musical (34 % de parole contre 77 % sur la voix séparée) ; un « plan » de 123 s de cartons de texte sur noir (YggTorrent) qui en contient au moins 20.
- Session 4 : « 14 à 16 duos » dans GP Explorer 3 écrit sans compter (corrigé en « au moins une dizaine ») ; HOUDI semblait couper sur les temps (45 % contre 27 %) sur le mixage ; sur la musique séparée, rien (27 % contre 24 %).
- Session 3 (clips) : 88 plans pour Ziak (en réalité environ 109) ; « Ziak évite les attaques fortes » (effet des coupes manquantes) ; quatre affirmations de phase 1 sur Stress et Au DD (voir ci-dessus).
- Session 3 : j'avais noté le pic de Mad Max à 0:27-0:30 (56 coupes/min) ; les éclairs le gonflent du double (environ 27/min réels). J'avais supposé qu'une mesure de saillance trouverait le sujet : calibrée, elle ne le trouve qu'une fois sur trois.

## Limites de ma méthode (inscrites dans `PROMPT-PHASE-2.md`)
- Film N&B de nuit (*La Haine*) : le détecteur fusionne des dizaines de plans ; `verif_plan.py` sur tout plan de nuit de plus de 60 s. Et `verif_plan.py` rate les coupes entre plans rapprochés de même lumière (*Forrest Gump*) : la tuile à 1 image/s reste obligatoire.
- Les détecteurs ratent les coupes du sombre et de l'action accélérée (même `verif_plan.py`), inventent des coupes sur les éclairs ; les deux erreurs coexistent dans Mad Max. Recompter avant de citer un pic, tuile à 2-4 images/s sur tout plan long d'action.
- Une vignette par plan ne juge pas un plan long ; une source HDR lue en SDR fausse la couleur.
- Whisper invente des phrases sur les pistes sans voix et boucle sur les longues vidéos : vérifier les répétitions avant de citer ; `-mc 0` corrige la boucle (testé sur KAIZEN, session 5).
- La parole détectée par l'énergie se trompe sous une musique, et sur la voix séparée avec l'ancien seuil (90 % contre 20 % à l'œil) : `SEUIL=haut` sur la voix séparée, chiffres tenus pour des bornes hautes, coupes au bord d'un mot tranchées sur spectrogramme (`spectro_coupes.py`). Les cartons de texte sur noir cachent leurs coupes au détecteur.
- Le son est mesuré, **jamais écouté** ; demucs sert désormais à confirmer tout calage (le mixage avec voix peut en fabriquer un faux).
- Le placement du sujet n'est mesurable qu'à l'œil, sur un petit échantillon.
- Clips très sombres : copie éclaircie avant la détection, puis tri à l'œil des coupes nouvelles (paires d'images). `verif_plan.py` lit désormais la fréquence d'images (il supposait 23,976 i/s).
- Les plans portés à filés (Stress) peuvent cacher des coupes que ni les outils ni une tuile à 4 images/s ne tranchent.

## Doutes (à trancher plus tard, sans poser de question pendant une routine)
- *Aftersun* : la version désossée de « Under Pressure » et la pulsation régulière sous le couloir final (peut-être la rave derrière les portes) ne sont pas écoutées ; le plan de nuit de 157 s (7:56) est peut-être plusieurs plans. *Spider-Verse* : crédits (réalisateurs, monteur Mike Andrews) écrits de mémoire ; flashs non comptés (photosensibilité) ; la saturation mesurée plafonne et ne distingue plus rien.
- *Social Network* : la rumeur du bar passe dans la voix séparée par demucs et réduit les silences mesurés ; l'écart avec *Spotlight* va dans le même sens à l'œil, mais le chiffre (0,24 contre 0,48 s) est approximatif. Henley : le calage « sur les coups de rame » (visuel) n'est pas mesurable avec mes outils.
- Spectrogramme regardé à l'œil : je ne distingue pas toujours une fin de mot d'un souffle ou d'une réverbération ; les 20 coupes d'*OSS 117* ont trois cas limites (comptés à part). Le son n'est toujours pas écouté.
- *La Haine* : un tronc d'arbre passe devant l'objectif à 13:04 ; coupe cachée ou non, je ne peux pas trancher sur l'image. *Avengers* : le classement des lignes de l'acte final est fait à l'œil au pas de 2-3 s (±10 s). *Forrest Gump* : mesures de son sur la **version française** (choisie pour les sous-titres français complets) ; le silence de la fin de la course vaut pour la VF.
- Projets F42 : je n'ai aucun rush ni brief ; les intentions, contraintes et destinations (festival, application, réseau) sont déduites. Oney : les 2,5 s de noir final sont peut-être demandées par l'intégration. Hirsingen : les appels « Monsieur, vous m'entendez ? » transcrits aux débuts des fenêtres de 30 s sont plausiblement réels (elle l'appelle plusieurs fois à l'image), non écoutés. Le son n'est jamais écouté : les remarques « loge sans ambiance » sont des lectures de courbe.
- `.claude/settings.json` (modèle Opus, effort high), ajouté par Diego, **n'est pas commité** : le garde-fou de l'agent refuse ce commit. Diego peut le commiter lui-même.
- J'ai commité la modification de `PROMPT-PHASE-2.md` (passe de révision) trouvée non commitée sur le disque : je la suppose de Diego, puisqu'elle est rédigée comme une consigne de mission.
- Whiplash : combien de coupes cachent les filés des plans de 21 et 24 s ? L'hypothèse « on coupe sur l'instrument qui a la phrase » n'est pas mesurée.
- Mad Max : les images accélérées n'ont pas été mesurées ; le chiffre d'environ 2 700 plans qui circule n'est pas vérifié.
- Le plan du bus « en miroir » de Joker n'a pas été cherché.
- adidas « Backyard Legends » : « 68 % des coupes pendant la parole » a été mesuré sur le mixage avec musique ; à refaire sur la voix séparée en passe de révision.
- Boxho : montage multicaméra automatique ou règle fixe du monteur ? Les durées le suggèrent, rien ne le prouve.

## Hypothèses de goût (à confirmer par d'autres références)
- « L'accélération du montage alterné » (Diego, à propos d'*Interstellar*) n'est pas la seule façon de faire monter un alterné : *Avengers* monte par la jonction des lignes. Je ne sais pas si Diego aime aussi cette forme ; à garder comme alternative quand il y a plus de trois lignes, pas comme son goût.
- Interstellar et Joker, les deux films cités par Diego, **ne coupent pas vite** ; ce qu'il aime chez eux tient à la structure (l'alternance, la rupture) et à l'équilibre de l'image. Son goût pour le kinetic est réservé à « d'autres usages » (GOUTS.md, 2026-10-09). Mad Max montre qu'un film peut tenir les deux : très rapide, mais structuré par ses respirations.
- « L'équilibre de l'ensemble » de Joker (réponse 4) se lit comme **une même règle appliquée par tous les leviers**. Mad Max le confirme en partie : vitesse, cadre centré et couleur par lieu servent la même chose (qu'on suive), mais la nuit bleue ne coïncide pas exactement avec les creux de rythme (15,6 contre 21,8 coupes/min). À tester sur les clips : un clip « équilibré » obéit-il à une seule règle ?
