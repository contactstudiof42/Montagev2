# RAPPORT — synthèse de la phase 2 (en cours)

_Réécrit à chaque session (dernière : 2026-10-11, session 4). Version précédente : `archives/phase-2/RAPPORT-session-2.md`. La synthèse de fin de phase 1 (niveau par domaine, 10 principes, audits) est dans `archives/phase-1/RAPPORT-synthese-cloture-phase-1.md` ; le journal de la phase 1 dans `archives/phase-1/RAPPORT-journal.md`._

## Où j'en suis
- **Vague 1 des films terminée** : Interstellar, Joker, Whiplash, Le Dîner de cons, Mad Max: Fury Road (fiches dans `analyses/films/`), plus SDM « #Malentouré » (test de méthode).
- **Clips terminés** (sessions 3-4) et **pubs terminées** (session 4) : fiches dans `analyses/clips/` et `analyses/pubs/`, bilans ci-dessous. **YouTube commencé** (session 4) : B-roll, EGO « Bibliothèque-Univers », « Les Jeux Tiger » (première passe) ; voir « Premiers constats YouTube ».
- La mission a changé (modification de Diego dans `PROMPT-PHASE-2.md`, commitée en session 3) : une **passe de révision** (étape 7) viendra avant la synthèse finale, pour relancer les outils récents sur les premières vidéos.
- Outils de la phase 2 (`labo/outils/`) : `passe_globale.sh` (avec `HDR=1`), `courbes_film.py`, `couleur_film.py`, `sequence.py`, `verif_plan.py`, `calage.py`, `coupes_parole.py`, et en session 3 `echantillon_tiers.py` (placement du sujet, à compter à l'œil). `centrage.py` (saillance automatique) a échoué à la calibration : ne pas citer ses chiffres.

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
9. **Le timing comique sans public** (Dîner de cons) : 40-44 % des coupes pendant la parole, environ 0,35 s d'air sinon ; l'air (1,5-3 s) réservé aux chutes. [mesuré, VU SUR IMAGES]

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

## Premiers constats YouTube (trois vidéos, session 4 ; à compléter)
1. **La rafale suit une énumération** : EGO coupe à 0,67 s quand la voix énumère (« les textes sacrés…, les journaux intimes des rois… »), Yvnnis et 6G font leur seule rafale sur un inventaire (devantures, toits). C'est le même geste dans trois formats : une image par élément d'une liste. [VU SUR IMAGES, mesuré]
2. **Le sponsor : sketch ou bloc isolé** : « Les Jeux Tiger » le joue en parodie de bande-annonce ; EGO l'isole par la forme (captures blanches) et l'encadre de silences. [VU SUR IMAGES]
3. **Le volume n'est pas une norme chez les créateurs de référence** : EGO à -21,3 LUFS, le tutoriel B-roll à -11,7, Tiger à -16,6. YouTube baisse les vidéos trop fortes mais ne remonte pas les faibles : -21 est un choix de dynamique. [mesuré]
4. **Expliquer par une surface qui se transforme** (EGO, chiffre de Vigenère en une minute) confirme sur une vraie vidéo un principe que je n'avais qu'éprouvé en maquette. [VU SUR IMAGES]
5. **Couvrir une interview à une caméra par du stock qui raconte** (B-roll) : une illustration = un détail de plus, une métaphore pour l'indicible, retour au visage pour les chutes. Utile tout de suite pour le corporate de Studio F42. [VU SUR IMAGES]

## Erreurs corrigées (phase 2)
- Session 1 : j'avais cru faux le plan de 74 s de Pogo's (c'est un plan-séquence) ; j'avais attribué à Diego une note sur l'amarrage qui n'était qu'un exemple de format (retour du 2026-10-11, intégré).
- Session 4 : « 14 à 16 duos » dans GP Explorer 3 écrit sans compter (corrigé en « au moins une dizaine ») ; HOUDI semblait couper sur les temps (45 % contre 27 %) sur le mixage ; sur la musique séparée, rien (27 % contre 24 %).
- Session 3 (clips) : 88 plans pour Ziak (en réalité environ 109) ; « Ziak évite les attaques fortes » (effet des coupes manquantes) ; quatre affirmations de phase 1 sur Stress et Au DD (voir ci-dessus).
- Session 3 : j'avais noté le pic de Mad Max à 0:27-0:30 (56 coupes/min) ; les éclairs le gonflent du double (environ 27/min réels). J'avais supposé qu'une mesure de saillance trouverait le sujet : calibrée, elle ne le trouve qu'une fois sur trois.

## Limites de ma méthode (inscrites dans `PROMPT-PHASE-2.md`)
- Les détecteurs ratent les coupes du sombre et de l'action accélérée (même `verif_plan.py`), inventent des coupes sur les éclairs ; les deux erreurs coexistent dans Mad Max. Recompter avant de citer un pic, tuile à 2-4 images/s sur tout plan long d'action.
- Une vignette par plan ne juge pas un plan long ; une source HDR lue en SDR fausse la couleur.
- Le son est mesuré, **jamais écouté** ; demucs sert désormais à confirmer tout calage (le mixage avec voix peut en fabriquer un faux).
- Le placement du sujet n'est mesurable qu'à l'œil, sur un petit échantillon.
- Clips très sombres : copie éclaircie avant la détection, puis tri à l'œil des coupes nouvelles (paires d'images). `verif_plan.py` lit désormais la fréquence d'images (il supposait 23,976 i/s).
- Les plans portés à filés (Stress) peuvent cacher des coupes que ni les outils ni une tuile à 4 images/s ne tranchent.

## Doutes (à trancher plus tard, sans poser de question pendant une routine)
- `.claude/settings.json` (modèle Opus, effort high), ajouté par Diego, **n'est pas commité** : le garde-fou de l'agent refuse ce commit. Diego peut le commiter lui-même.
- J'ai commité la modification de `PROMPT-PHASE-2.md` (passe de révision) trouvée non commitée sur le disque : je la suppose de Diego, puisqu'elle est rédigée comme une consigne de mission.
- Whiplash : combien de coupes cachent les filés des plans de 21 et 24 s ? L'hypothèse « on coupe sur l'instrument qui a la phrase » n'est pas mesurée.
- Mad Max : les images accélérées n'ont pas été mesurées ; le chiffre d'environ 2 700 plans qui circule n'est pas vérifié.
- Le plan du bus « en miroir » de Joker n'a pas été cherché.

## Hypothèses de goût (à confirmer par d'autres références)
- Interstellar et Joker, les deux films cités par Diego, **ne coupent pas vite** ; ce qu'il aime chez eux tient à la structure (l'alternance, la rupture) et à l'équilibre de l'image. Son goût pour le kinetic est réservé à « d'autres usages » (GOUTS.md, 2026-10-09). Mad Max montre qu'un film peut tenir les deux : très rapide, mais structuré par ses respirations.
- « L'équilibre de l'ensemble » de Joker (réponse 4) se lit comme **une même règle appliquée par tous les leviers**. Mad Max le confirme en partie : vitesse, cadre centré et couleur par lieu servent la même chose (qu'on suive), mais la nuit bleue ne coïncide pas exactement avec les creux de rythme (15,6 contre 21,8 coupes/min). À tester sur les clips : un clip « équilibré » obéit-il à une seule règle ?
