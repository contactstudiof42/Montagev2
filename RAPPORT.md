# RAPPORT — synthèse de fin de phase 2

_Réécrit le 2026-10-11 (session 11, clôture de la phase 2) ; complété en session 12 (sept vidéos réseaux de Diego) et en session 13 (un tutoriel d'étalonnage). **Les bilans détaillés** (tableaux et constats par vague, clips, pubs, YouTube, projets F42, révision, erreurs corrigées, version complète des doutes) sont archivés dans `archives/phase-2/RAPPORT-bilans-detailles-phase-2.md` ; les versions de session dans `archives/phase-2/RAPPORT-session-*.md`. Synthèse de fin de phase 1 : `archives/phase-1/RAPPORT-synthese-cloture-phase-1.md`._

## Où j'en suis
**Phase 2 terminée.** 45 vidéos vues et analysées (13 films, 8 clips, 7 pubs, 10 vidéos YouTube, 7 projets du studio), une fiche chacune dans `analyses/` ; passe de révision faite (45 conclusions revérifiées avec les outils récents) ; tous les skills de création révisés à la lumière de la phase 2 (sessions 10-11). Les skills techniques (After Effects, Blender, Resolve, Premiere, pipeline couleur, workflows, IA générative, pilotage MCP) n'ont rien reçu de la phase 2, qui portait sur le regard ; seul le QC de livraison est entré dans `montage-loudness-livraison`.

**Session 12** : Diego a ajouté sept vidéos réseaux qu'il aime (`videos/reseaux/`) : analysées image par image, sept fiches dans `analyses/reseaux/`, bilan ci-dessous ; la lacune prioritaire de fin de phase (le kinetic de réseaux) est en partie comblée.

**Session 13** : Diego a déposé un tutoriel d'étalonnage (David Foxprod, « recréer la colo de *Seven* ») à lire comme une méthode : arbre de nœuds lu, apport de chaque nœud mesuré, méthode ajoutée à `montage-resolve` § 2 bis avec ses limites (fiche `analyses/methodes/david-foxprod-look-seven.md`).

**Phase 3, projet Sony LinkBuds (sessions 0 à V4, 2026-10-11)** : premier projet monté de bout en bout dans Resolve par le MCP. Notes de Diego : V2 **50 %** (Claude nu 40 %), V3 **65 %**. **V4 rendue** (`rendus/sony_linkbuds_V4.mp4`, timeline `SONY_V4`) : sept techniques différentes tirées de la matière (zoom infini E → KORE, flash cut des oreilles, rafale qui monte, step-print qui descend, écran partagé, inversions dans le rouge, trois collages sur arrêt) ; couleur séparée en OkLCh, noirs neutres, packshots mesurés ; titre d'après la DA Sony ; Gyroflow synchronisé + stabilisation fixe ou rail selon l'intention du cadreur ; 0 doublon ; HEVC Main 10 39 Mb/s, −14,0 LUFS. Ce que je sais faire par script, désormais : animations par clés (sans `comp.Lock`), Fusion (masques, TimeStretcher, Text+), LUT fabriquées, son à la crête. Ce qui reste hors API : Magic Mask, cases « Force… » du rendu. Détail : `projets-phase-3/sony-linkbuds/` (plan, look, autocritique, note de livraison, journal).

**Doutes de la session V4** : (1) le son n'a jamais été écouté (63 sons, dont 25 nouveaux) ; (2) le flash cut grossit d'un plan à l'autre au lieu de garder l'échelle (variante de la technique) ; (3) les collages sont pré-calculés hors de Resolve ; (4) Gyroflow n'améliore presque rien sur les plans déjà stables (C6723) : gardé à la demande de Diego, mesuré à chaque fois ; (5) graisse du titre : Medium d'après une référence floue (Bold possible).

Hors phase 3, chaque session ne fait que le démarrage de `CLAUDE.md` : retours de Diego, boîte à références (`montage-nouvelle-reference`).

## Ce que j'ai appris, par domaine
Du plus solide au moins solide dans chaque domaine. Les principes vus sur plusieurs œuvres de familles différentes sont les plus fiables ; aucun d'eux n'est tombé à la révision.

### Structure et rythme (`montage-rythme`, `montage-formats`)
1. **Le climax n'est pas la partie la plus rapide** : 13 films sur 13, les clips, KAIZEN. Le sommet d'émotion se porte par le volume, le cadre, la durée de la crête, le silence juste avant ; la crête de densité est souvent **juste avant** le sommet. Seul un sommet d'information peut être le plus rapide. [VU SUR IMAGES]
2. **Ce qui signale, c'est l'écart à la norme que l'œuvre a installée**, pas « plan long = important » : *La Haine* et *Aftersun* (plans longs de règle) signalent par leurs rares rafales, *Spider-Verse* par un ralentissement de moitié. La norme varie d'un facteur 4 (médiane 1,96 à 8,2 s) ; la logique de l'écart ne varie pas. C'est l'apport le plus général de la phase 2. [VU SUR IMAGES]
3. **La densité suit le type de phrase** : liste → une image par élément, thèse → plan tenu, preuve → temps réel tenu, récit → gros plan tenu. Vu en doc, talk-show, cinéma, clip (rafale-inventaire). La règle la plus transversale du corpus. [VU SUR IMAGES]
4. **Plan long pour ce qui compte (la preuve, le corps, la sincérité, la réception), rafale pour l'acte ; la surprise arrive dans le plan.** Le plan le plus long va à celui qui reçoit, pas à l'information. [VU SUR IMAGES]
5. **Le plus fort est suivi du plus grand vide** (six films), ou précédé d'un silence (*Whiplash*, *Forrest Gump*, KAIZEN). **Plus on coupe vite, plus on doit respirer franchement** (*Mad Max*, facteur 10 entre creux et crêtes). [VU SUR IMAGES, son mesuré]
6. **Alterner** : accélérer les changements de ligne jusqu'à trois lignes (*Interstellar*, le goût de Diego), suspendre l'alternance sur l'action la plus tendue ; au-delà, des blocs et un personnage qui passe d'une ligne à l'autre (*Avengers*). [VU SUR IMAGES]
7. **Hors vidéos réseaux, personne ne coupe sur les temps plus qu'au hasard** (8 clips, 5 pubs, *Whiplash*, *Spider-Verse*, Henley), sur musique séparée ; **dans les vidéos réseaux de Diego, quatre sur sept coupent sur les attaques à l'image près** (session 12, voir le bilan). La musique commande la densité (arrangement, courbe du morceau) ou les rares coupes sur les grands accents. Le calage micro reste un trait de genre du kinetic, non mesuré. [mesuré]

### Formats (`montage-formats`, `montage-youtube`)
- **Pub** : le nom de la marque arrive à la fin dans les sept, ce qui la représente (lieu, tenue, objet, couleur) dès la première image ; le gag porte le bénéfice ; les films longs tiennent par une cadence régulière de 1 à 2 s et un récit. [VU SUR IMAGES]
- **Clip** : une seule rafale (souvent un inventaire), des plans longs qui sont des mouvements qui relient, un sommet porté par le cadre, une ouverture qui construit l'image, un habillage tiré du sujet. [VU SUR IMAGES]
- **YouTube** : quatre familles, quatre régimes (doc en vagues, plateau plat et sans silence, conversation calme, cinéma) ; le plus long plan porte la thèse et quelque chose change dedans (schéma, texte qui s'écrit) ; un format de série est un système. [VU SUR IMAGES, mesuré]
- **Dialogue** : la part de coupes pendant la parole ne distingue pas les styles (Fincher et McCarthy à 30 %) ; l'air entre les répliques et la durée des plans, si. La conversation multicaméra change d'angle au milieu des phrases ; la comédie coupe au ras de la réplique et garde l'air pour la chute. [VU SUR SPECTROGRAMME]
- Repères chiffrés par format (médianes, loudness) : tableau dans `montage-formats`. Ce sont des minimums pour les montages rapides.

### Couleur et image (`montage-couleur-et-intention`)
**Une matière par monde** (teinte, mais aussi format, support, texture) est le principe de couleur le plus répandu (au moins douze œuvres) et ce qui rend lisibles des plans de 0,5 à 2 s ; **la couleur forte se mérite et change de place** (*Joker*) ; **le monde de référence est le moins coloré** ; une couleur peut ne rien raconter (comédie) ; **la nuit baisse plus qu'elle ne contraste**, la lumière restant sur ce qu'il faut voir ; une rafale tient en une seule couleur ; le souvenir passe par le support. La vitesse se rachète par le sujet au centre (*Mad Max*), le décentrage va avec les plans tenus (*Joker*). [VU SUR IMAGES]
**Reproduire un look de référence** (session 13, tutoriel Foxprod) : un arbre court et nommé (CST IN, exposition, balance, contraste, branche parallèle densité / fenêtres / qualifieur, masque, texture, CST OUT, deux looks en A / B) rattrape la teinte ; **la densité perdue au tournage ne revient pas** (son image finale reste bien plus claire que *Seven*). Le look d'une référence se prépare au tournage. [VU SUR IMAGES, mesuré sur la vidéo]

### Son (`montage-son-et-emotion`, `montage-loudness-livraison`)
Le silence ouvre le sommet dans les mix en plateau (clips, pubs) ; un carton récurrent peut être un trou de son ; le son le plus fort peut marquer l'écart entre les personnages, pas la fête ; le niveau n'est une norme chez aucun créateur, la dynamique (LRA) dit la famille. **Tout a été mesuré, rien écouté.** [mesuré, pas écouté]

### Typographie et habillage (`montage-motion-design-principes`)
Le texte qui s'écrit au rythme de la voix tient un plan long ; une police et une couleur par voix anonyme ; les noms d'un line-up passent par paquets de couleur ; le logo redessiné dans le langage du film ; aucun carton décoratif dans les clips de référence. [VU SUR IMAGES]

### Méthode d'analyse (`PROMPT-PHASE-2.md` § « Leçons de méthode », `montage-regard` § « Juger une vraie vidéo »)
**Quand j'ai regardé une image et écrit ce qu'elle montrait, je ne me suis pas trompé dans la révision ; quand j'ai écrit un nombre d'outil sans le contrôler, je me suis trompé une fois sur trois** (45 conclusions revérifiées : 28 confirmées, 14 corrigées, 3 nouvelles). Les erreurs vont toujours dans le même sens pour un même outil : parole par énergie trop haute ; rafales vraies sous-comptées (PySceneDetect ignore les plans de moins de 0,6 s) ; rafales fausses sur-comptées (éclairs, écrans, plan porté flou, détecteur saturé) ; coupes du sombre ratées. D'où les contrôles obligatoires : spectrogramme avant tout pourcentage de parole, bandes de 6 images avant toute rafale, `verif_plan.py` + tuile avant tout plan long, musique séparée avant tout calage, générique retiré avant toute statistique, `color_transfer` avant toute mesure de couleur. Les fiches de phase 1 écrites sur des textes étaient justes dans l'esprit et souvent fausses dans les chiffres.

## Bilan des sept vidéos réseaux (session 12, retour de Diego du 2026-10-11)
Sept vidéos de 11 à 43 s que Diego « aimait beaucoup », avec « beaucoup de kinétique, mais pas que ». Toutes les images regardées (environ 3 900), spectrogramme mix / musique / voix, calage contre le hasard sur la musique séparée, écart signé. Rien écouté. À l'œil : **deux kinetic de rafales** (captured-by-h, malkimikee : médiane 2 à 3 images) ; **cinq qui n'en sont pas** au sens de mon skill : transitions variées (Sephora / lucasbosc, yungchillyboy), look film (pasalu, darius), film d'annonce en blocs (équipe de France).

| Point du skill (avant) | Statut avant | Ce que montrent les sept | Statut après |
|---|---|---|---|
| Calage micro sur le beat | [THÉORIQUE] ; « personne ne cale » sur le reste du corpus | **4 sur 7 coupent sur les attaques à l'image** (40-53 % à ±1 image contre 19-26 % au hasard) ; écart médian 0 à +0,3 image, ou **1 à 2 images avant** (yungchillyboy) ; jamais après ; dans les rafales de 2 images, seuls mots et arrêts sont calés | **confirmé et précisé** [mesuré] ; synthèse de phase 2 corrigée |
| Calage du whoosh 3-6 images avant | [TESTÉ EN LABO] / [THÉORIQUE] | pas de whoosh systématique au spectrogramme ; un balayage, un souffle, un riser de 6 s au drop | **non vérifié** (rien écouté), mais la densité de whoosh du skill n'est pas celle de ses références |
| SFX denses, hiérarchie | [SOURCÉ] | le son des coupes est la musique ; SFX rares et causés (riser → drop, impacts d'ouverture, annonce de métro comme légende, compte à rebours dans le silence) | **corrigé** : densité de SFX ≠ goût de Diego en réseaux, à doser selon le client |
| Captions mot à mot | [SOURCÉ] | **aucune** des sept ; mots seuls sur les accents, titres serif, claim dans le décor | **remplacé** pour son goût ; reste une demande client (face caméra) |
| Hook 3 s : image 1 la plus forte + impact | [THÉORIQUE] | quatre formes : bande-annonce de 0,5 s, visage connu, phrase de coulisses, construction avec drop à 6 s | **corrigé** |
| Plan éclair 4-8 images | [THÉORIQUE] | 2-3 images dans les rafales | **corrigé** [VU SUR IMAGES] |
| Respiration, silence avant le fort | [ÉPROUVÉ EN MAQUETTE] | dans les sept ; l'arrêt porte une transformation | **confirmé** [VU SUR IMAGES] |
| Vertical, 15-60 s | [THÉORIQUE] | 5 sur 7 horizontales ; 11-15 s pour une idée, ~40 s en blocs | **complété** |
| Pub courte : marque à la fin (7 pubs longues) | [VU SUR IMAGES] | pub réseau 15 s : marque à 1,3 s | **complété** : dépend de la durée |
Skills mis à jour : `montage-kinetic-editing`, `montage-formats` ; corrections reportées dans `montage-rythme`, `montage-expert`, `montage-references`.

## Ce que le goût de Diego et les projets F42 impliquent
**Ce que Diego a dit** (GOUTS.md, seule source de sa parole) : *Interstellar* pour l'accélération du montage alterné, *Joker* pour l'équilibre de l'ensemble, Ziak (montage qui ne colle pas au beat) et le kinetic à SFX denses pour des usages différents, EGO pour YouTube, le grain et le look film en préférence personnelle, des visages sombres avec un minimum de lumière sur l'info, l'IA générative non assumée et sans « slop », des projets « souvent énergiques ».

**Ce que j'en déduis** (mes rapprochements, pas sa parole) :
1. Les deux films qu'il cite **ne coupent pas vite** : ce qu'il aime tient à la structure (l'alternance qui accélère, la rupture) et à l'accord de tous les leviers sur une même règle. Son goût pour le kinetic est un goût de genre, pour les réseaux. Je ne dois pas confondre énergie et vitesse : *Mad Max* et STORM montrent que l'énergie d'un sommet vient du cadre, de la durée et du silence avant.
2. « L'équilibre de l'ensemble » de *Joker* se lit comme **une seule règle servie par la vitesse, le cadre, la couleur et le son**. C'est le critère à appliquer en relecture (`montage-regard`).
3. Le grain et le look film ont dans *Aftersun* une fonction (deux supports, deux temps) : à proposer quand ils disent quelque chose, pas comme un filtre.

**Ce que les sept projets disent du studio** (déduit sans brief ni rushes) :
- **Le point faible commun est la finition son, et c'est le moins cher à corriger** : six fichiers sur sept au-dessus de -1 dBTP, des niveaux de -11 à -27 LUFS sans lien avec la destination, deux pistes mono, l'ambiance qui tombe entre les répliques en fiction. Un QC fixe avant chaque envoi : `labo/outils/qc_livraison.sh`.
- **Les fictions sont plus maîtrisées que les commandes courtes** ; les commandes ont de bonnes idées de forme mais pèchent par **la lisibilité muette** (sous-titres fins, flou d'ouverture trop long) et **la liaison** (ordre des plans qui ne dit pas la cause).
- **Le meilleur moment de chaque commande est quand la forme dit le bénéfice** (le flou de Benefit 2, la carte unique de Swile, le jeu-formule de Sephora). C'est ce qu'il faut chercher en premier dans un brief.
- **Pour le studio, dans l'ordre** : (1) QC son systématique ; (2) un passage muet de chaque commande réseau (sous-titres gras, premier écran net avant 2 s) ; (3) vérifier que l'ordre des plans dit la cause dans les pubs sans voix ; (4) une ambiance continue sous tout dialogue de fiction ; (5) un minimum de lumière sur l'info dans les plans de nuit (sa propre règle).
- **Références les plus utiles pour ses commandes probables** : *Spider-Verse* pour un kinetic de marque (une texture par univers, une voix en refrain pour structurer une rafale) ; GP Explorer 3 pour un événement de créateurs (noms par paquets de couleur, vol continu) ; Swile « POW » (son propre projet) pour l'onomatopée qui nomme la campagne ; EGO et « Le jour où la CIA… » pour un film explicatif ; *Aftersun* pour un portrait lent.

## Ce qui reste [THÉORIQUE] ou non vérifié
- **Le kinetic de réseaux** : sept références vues (session 12) ; restent non vus le face caméra à captions mot à mot (format Hormozi), la densité de SFX à l'oreille et la rétention.
- **Le face caméra en jump cuts et le format MrBeast** : non vus ; seuils de micro-saut et de durée retirée non tranchés.
- **La pub courte (6, 15, 30 s)** et **le corporate classique** (interview de dirigeant, film de présentation) : non vus.
- **Le son n'a jamais été écouté** : tous les constats sonores viennent des courbes, des spectrogrammes et de demucs.
- **Le cadre** : la saillance automatique a échoué ; le placement du sujet n'est mesuré qu'à l'œil sur de petits échantillons ; la règle des 30 % et l'aire de regard ne sont pas vérifiées.
- **Les durées fines des maquettes** (2 images après le mot-clé, plan de retour 4 puis 6 s, J-cut de 12 images) : non vérifiées sur de vraies vidéos.
- Les principes [ÉPROUVÉ EN MAQUETTE] des skills restent des hypothèses ; les nombres de plans et médianes des montages rapides sont des minimums.

## Limites de ma méthode
Détail et parades dans `PROMPT-PHASE-2.md` (« Leçons de méthode ») et `montage-regard` (« Juger une vraie vidéo ») ; liste complète archivée. En une ligne chacune : PySceneDetect ne voit pas les plans de moins de 0,6 s, rate les coupes du sombre, du N&B de nuit, des cartons sur noir et de l'action accélérée, invente des coupes sur les éclairs, les écrans, les animations en collage et le plan porté flou ; `verif_plan.py` échoue sur l'action accélérée et les plans rapprochés de même lumière ; la parole par énergie se trompe sous une musique et sur la voix séparée ; Whisper invente et boucle (`-mc 0`, contrôle des répétitions) ; une source HDR lue en SDR fausse la couleur ; le son n'est pas écouté.

## Doutes (à trancher plus tard ; liste complète dans l'archive)
- Projets F42 : aucun rush ni brief ; intentions et destinations déduites (Oney : les 2,5 s de noir final sont peut-être demandées par l'intégration).
- *Aftersun* : plan de nuit de 157 s (7:56) peut-être composé ; « Under Pressure » non écouté. *Spider-Verse* : film entier non recompté sans durée minimale de plan ; crédits écrits de mémoire. *Avengers* : lignes de l'acte final classées à ±10 s. *Forrest Gump* : son mesuré sur la VF.
- Boxho : montage multicaméra automatique ou règle fixe du monteur, non prouvé.
- `.claude/settings.json` (ajouté par Diego) n'est pas commité : le garde-fou de l'agent refuse ce commit. Diego peut le commiter lui-même.
- Session 12 : `flash_check.py` fait échouer les sept vidéos réseaux, même la pub Sephora sans flash visible ; l'outil compte sans doute les coupes contrastées. À confronter à un vrai test (Harding) avant de s'y fier sur des coupes ordinaires. Les sept vidéos sont toutes à -14,0/-14,2 LUFS : probablement renormalisées par la plateforme ou le téléchargement, le mix d'origine n'est pas jugeable. Darius et lucasbosc ont des crêtes à +0,4 dBFS.
- Session 13 (tutoriel Foxprod) : outils de chaque nœud, type des mélangeurs, contenu d'OVERLAY et de « LOOK K… » illisibles à 290 kb/s ; la branche DENSITÉ semble partir de la source log et être mélangée à une branche convertie (deux espaces différents ?) ; la numérotation des nœuds change en cours de vidéo (montage de deux captures ?). Rétention d'argent sur les copies de *Seven* : de mémoire, non vérifié.
- Session 12 : même anomalie d'horloge (11:48 à environ 12:00 pour sept vidéos vues image par image et la mise à jour de cinq skills).
- Session 11 : l'horloge système a très peu avancé (11:04 à environ 11:10) pour la révision de sept skills et la synthèse ; même anomalie qu'en session 10. Je la note sans pouvoir l'expliquer.

## Hypothèses de goût (à confirmer par d'autres références ou par Diego)
- **Session 13** : après pasalu, darius et l'équipe de France, un tutoriel sur le look d'un film de pellicule (avec deux émulations Fuji / Kodak probables) : le **look film** revient pour la quatrième fois, ce qui va avec sa préférence dictée (« le grain et le look film »). Ce que Diego en attend ici est une méthode simple pour reproduire un look, pas un goût nouveau.
- **Session 12** : ses sept vidéos réseaux suggèrent que son « kinetic » est **un montage calé à l'image, aux transitions variées, au look film, qui respire**, plutôt que le kinetic à whoosh et captions de mon skill ; deux traits reviennent dans au moins trois des sept : le look pellicule (pasalu, darius, équipe de France) et la typo serif fine (darius, équipe de France). Hypothèse, pas sa parole.
- L'alterné par blocs d'*Avengers* est une alternative à l'accélération d'*Interstellar* quand il y a plus de trois lignes ; je ne sais pas si Diego l'aime.
- *Interstellar* et *Joker* ne coupent pas vite ; son goût pour la vitesse est réservé au kinetic. *Mad Max* montre qu'un film peut tenir les deux.
- « L'équilibre de l'ensemble » = une même règle appliquée par tous les leviers ; *Mad Max* le confirme en partie (la nuit bleue ne coïncide pas exactement avec les creux de rythme).
