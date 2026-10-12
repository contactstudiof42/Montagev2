---
name: montage-formats
description: Choisir la structure et les conventions d'un format — pub 6/15/30/60 s, vertical (Reels, TikTok, Shorts, LinkedIn), Short narratif, clip, corporate / film de marque, documentaire, fiction courte, teaser et bande-annonce. Mots d'un client ou d'un réalisateur : « on a 30 secondes », « une version 15 s et une 6 s », « il faut une déclinaison verticale », « film d'entreprise », « portrait de collaborateur », « témoignage client », « le corporate fait chiant », « doc de 52 minutes ». YouTube long : `montage-youtube` ; kinetic et SFX : `montage-kinetic-editing`.
---

# Narration par format

Marqueurs : [VU SUR IMAGES] vérifié sur de vraies vidéos (phase 2, fiches dans `analyses/`) · [SOURCÉ] lu dans une source citée · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu seulement sur maquette Blender / Pillow / ffmpeg · [THÉORIQUE] déduit, non vérifié.

**Fait foi sur** : la structure et les conventions par format (pub, vertical et Shorts narratifs, clip, corporate, documentaire, fiction, teaser) et la grille de choix. Pour la vidéo YouTube longue : `montage-youtube` ; pour la grammaire du style kinetic (SFX, captions, punch-in) : `montage-kinetic-editing` ; pour l'intention (le « quoi ») : `montage-direction-artistique`. Les durées de structure (0-8 s, 8-22 s…) sont des repères de métier [THÉORIQUE] ; les **cadences mesurées** sur 45 vraies vidéos sont dans « Repères mesurés » ci-dessous.

## Principe général : le format est un contrat d'attention
Spectateur captif (salle, TV), choisi (clip, YouTube), volé (fil d'actualité) ou professionnel (réunion). Le spectateur volé peut partir à chaque seconde ; le captif attend qu'on lui demande quelque chose.

## Ce qui vaut pour tous les formats (45 vraies vidéos, phase 2)
- **La densité suit le type de phrase** : une liste dite reçoit une image par élément (0,5 à 1,8 s), une thèse un plan tenu, une preuve un plan tenu en temps réel, un récit un gros plan tenu de 5 à 16 s. Vu en doc YouTube, en talk-show, au cinéma (*Forrest Gump*, *The Social Network*) et dans les clips (rafale-inventaire). La règle la plus générale du corpus. [VU SUR IMAGES]
- **Le sommet n'est pas la partie la plus rapide** (13 films sur 13, les clips, KAIZEN) ; seul un sommet **d'information** peut l'être (« Les Jeux Tiger »). Le sommet d'émotion se porte par le volume, le cadre, le silence avant, la durée. [VU SUR IMAGES]
- **Ce qui signale, c'est l'écart à la norme du film**, pas une durée absolue (*La Haine* signale par ses deux rafales, *Spider-Verse* par un plan de 4 s). [VU SUR IMAGES]
- **La marque, le monde ou l'époque se reconnaissent à une matière** (couleur, format d'image, texture) avant d'être nommés : pubs, clips, YouTube (un format par époque), films. [VU SUR IMAGES]
- **Le calage à l'image est une convention des vidéos réseaux, pas des autres formats** : 8 clips, 5 pubs longues, *Whiplash*, *Spider-Verse* ne coupent pas sur les temps plus qu'au hasard ; **4 vidéos réseaux de référence sur 7 coupent sur les attaques de la musique, à l'image près** (40 à 53 % des coupes à ±1 image, contre 19 à 26 % au hasard), une cinquième place seulement ses mots et ses arrêts sur les plus forts accents. Détail et décalages : `montage-kinetic-editing`. [mesuré, musique séparée] (`analyses/reseaux/`)
- **La finition son se vérifie avant d'envoyer, quel que soit le format** : six fichiers du studio sur sept dépassaient -1 dBTP (`labo/outils/qc_livraison.sh`, `montage-loudness-livraison`). [mesuré]

## Repères mesurés par format (médianes de durée de plan ; minimums pour les montages rapides, le détecteur ne voit pas les plans de moins de 0,6 s)
| Format | Médiane mesurée | Loudness mesuré | Vidéos |
|---|---|---|---|
| Pub longue (récit de marque, 1 à 5 min) | 1,1 à 1,6 s, cadence presque régulière | -23 (TV) ; -14 à -16 (web) | Intermarché ×2, Lacoste, adidas |
| Bande-annonce d'événement de créateurs | 1,1 à 1,3 s (ASL 3,2 s avec tirades) | -10 à -16 | GP Explorer 3, Crunch Creator |
| Pub réseau du studio (9:16) | ~2,2 s | -14,5 | Benefit ×2 |
| Vidéo réseau de référence, kinetic (collage, ville) | **0,07 à 0,10 s (2-3 images)**, arrêts de 0,7 à 2,3 s | -14 (renormalisé ?) | captured-by-h, malkimikee |
| Vidéo réseau de référence, transitions / look film | 0,40 à 1,16 s, plans tenus de 2 à 3,7 s | -14 | équipe de France, yungchillyboy, darius, pasalu, Sephora (lucasbosc) |
| Clip | 1,2 à 4,2 s | -10,9 à -12,9 (plateau) | 8 clips |
| YouTube doc / plateau / conversation / cinéma | 2,2-4,8 / 2,0-2,5 / 3,4 / 2,6 s | -16 à -22 / -12 à -18 / -24 / -17 | 10 vidéos |
| Film d'action ou d'animation rapide | 1,96 à 2,6 s | -16 à -25 | Mad Max, Avengers, Spider-Verse |
| Film de dialogue, comédie | 2,2 à 4,5 s | -20 à -25 | Social Network, Spotlight, OSS 117, Dîner de cons |
| Film d'auteur lent | 4,5 à 8,2 s | -16 à -26 | Joker, Forrest Gump, Aftersun (7,5 hors raves), La Haine |
| Court métrage du studio | 1,9 (comédie) et 4,6 s (drame) | -23 et -27 | Fou-Rire, Hirsingen |
Ces chiffres situent une norme ; ils ne la prescrivent pas : ce qui compte est l'écart à la norme aux moments qui comptent. [mesuré]

## Pub 30 s / 15 s / 6 s (TV, préroll, cinéma)
- **30 s** : une idée, une seule. Installation (0-8 s), bascule (8-22 s), résolution + signature (22-30 s ; packshot 3-5 s). Deux blocs de cadence et une bascule valent mieux que trois idées (Glazer, `montage-references`). [THÉORIQUE]
- **15 s** : la bascule seule, pas un 30 s accéléré. **6 s** : un plan, un signe, la marque ; se pense installation / rupture / retour.
- **Son** activé en TV et cinéma ; **muet probable** en préroll mobile : comprendre sans son.
- **Principes de campagne** (17 campagnes d'opticiens, 3 films primés ; presse pub, aucune vidéo vue) [SOURCÉ] : un dispositif répétable + une même phrase de fin font de chaque 30 s un épisode (Specsavers) ; le gag porte le bénéfice (si on retire le produit sans casser la blague, elle est à côté) ; installer un genre pour le casser ; une révélation qui réécrit le début vaut un 2e visionnage ; séparer film d'émotion et films d'offre.
- **Pièges** : clichés de catégorie (boîte à musique, bébé au ralenti, « avant gris / après coloré ») ; **vérifier le secteur avant de défendre une évidence** (le flou → net n'est la base d'aucune des 17 campagnes d'opticiens) ; trop de texte ; logo trop tôt.
- Livraison TV France -23 LUFS (EBU R128) : `montage-loudness-livraison`.
- **Vu sur les sept pubs de référence de Diego** [VU SUR IMAGES] (`analyses/pubs/`) : (1) **le nom ou le logo arrive dans les dernières secondes dans les sept** (Intermarché à 2:55 sur 3:00, Lacoste, iPhone, adidas…) ; mais **l'objet, la tenue ou le lieu de la marque est à l'écran dès la première image** (uniformes orange et rayons, polo blanc à col vert, téléphone orange). Le « logo trop tôt » est évité, la marque n'est pas absente pour autant. (2) **Le gag porte le bénéfice** confirmé : iPhone 17, un téléphone glissé sur une table de négociation (geste du drame judiciaire) prouve la résistance aux rayures, tenu en plan large de 5,4 s dans le silence. (3) Films longs (2 min 30 à 5 min) : **cadence presque régulière de 1 à 2,5 s** (Intermarché « L'amour » : 90 % des plans), la variation vient du récit ; un seul plan tenu pour la fin. (4) **Silence avant le sommet** : Lacoste, 2,4 s sur le plan large du court avant le geste final ; Intermarché « Conte de Noël », une demi-seconde avant l'acceptation, et musique retirée au retour au réel. (5) Aucune ne coupe sur les temps plus qu'au hasard.

## Vertical réseaux (Reels, TikTok, Shorts, LinkedIn)
- **Vu sur les sept vidéos réseaux de référence de Diego** [VU SUR IMAGES, chaque image] (`analyses/reseaux/`, 11 à 43 s) :
  - **Cinq sur sept sont horizontales** (16:9, 4:3) et une montre un film 4:3 dans un cadre vertical : le « vertical » n'est pas une obligation du genre qu'il aime.
  - **Durée : 11 à 15 s** pour une idée (cinq sur sept) ; **38 à 43 s** quand il y a une histoire ou des informations (darius, équipe de France), en blocs nets.
  - **Hook** : quatre façons, toutes lisibles avant 1 s : une rafale qui promet le film (yungchillyboy : 7 éclats tirés de la suite en 0,47 s ; captured, malkimikee) ; un visage connu (Sephora : l'égérie au 1er plan) ; une phrase de coulisses en face caméra (darius : « Client almost rejected this.. ») ; une construction (équipe de France : mosaïque de portraits qui se remplit sous la voix, **drop seulement à 6,1 s**). Personne ne met « l'image la plus forte + impact » à l'image 1 de façon systématique.
  - **La densité suit encore le type de phrase** : l'équipe de France tient ses trois affiches de match 3 s chacune, musique coupée, puis repart plus vite que jamais.
  - **Pub réseau de 15 s (Sephora Collection, lucasbosc)** : égérie (0 s) → **marque écrite à 1,3 s** sous son nom → produit (3,7 s) → bénéfice écrit (4,9 s) → démonstration → promesse chiffrée peinte sur la pelouse (9,6 s) → packshot (12,1 s) → logo sur noir (13,8 s). Contrairement aux pubs longues, **la marque arrive dès la première seconde**.
  - **Aucune n'a de sous-titres mot à mot** : du texte rare, en mots seuls sur les accents (« EIFFEL », « TOWER », « PARIS »), en titres serif fins (darius, équipe de France), en claim dans le décor (Sephora).
  - **Toutes finissent sur un plan tenu**, souvent après une coupure de musique (captured, darius, équipe de France).
- **Premier écran = tout** : sujet lisible dès la 1re image de chaque plan, une question ou une tension avant 2 s. [ÉPROUVÉ EN MAQUETTE] (pièce 02 : 7 plans sur 19 illisibles à leur 1re image en v1)
  - **Un flou d'ouverture n'est permis que s'il est l'idée** (révélation par la mise au point, net avant 2 s). Vu sur deux pubs réseau du studio (Benefit, 2026) : 4,4 s de flou sous le titre dans les deux ; dans l'une, la mise au point qui révèle dit le bénéfice du produit (« blur ») et le logo finit sur le flou, c'est le meilleur moment ; dans l'autre, deux plans flous sans révélation retardent le premier écran. [VU SUR IMAGES] (`analyses/projets-f42/benefit-pubs-reseau.md`)
  - **Pub muette : l'ordre des plans est la seule phrase** ; le geste du produit doit précéder ce qu'il provoque (dans Benefit 1, le regard admiratif arrive avant le produit : la cause manque). [VU SUR IMAGES]
- **After movie, événementiel, run and gun (règle de Diego, 2026-10-11)** : jamais deux fois le même moment d'un même rush, rafales comprises ; un rush peut donner plusieurs plans à des moments différents. Exception : ressort de récit écrit dans `plan.md` (flashback, rappel). Contrôle avant chaque rendu : `labo/outils/doublons_timeline.py` (détail : `montage-grammaire`).
- **Muet par défaut** : sous-titres incrustés, mots-clés à l'image, SFX à cause visible (`montage-kinetic-editing`).
- **Structure hybride** : accroche forte, densité qui suit la musique par sections, une image d'exception sur le break, boucle ou chute à la fin. [ÉPROUVÉ EN MAQUETTE] (pièce 03)
- Zones sûres : rien d'important en bas (légende) ni à droite (boutons).
- **LinkedIn** (B2B) : même grammaire muette, énergie retenue, 4:5 ou 1:1 ; hook possible en question professionnelle.

### Shorts narratifs (Zach King, Khaby Lame, Daniel LaBelle, Roman Doduik ; `culture/shorts-narratifs-verticaux.md`, découpages non vérifiés)
- Situation lisible en 1 s sans le son ; une idée, une émotion ; **la chute est la dernière image** (+ une réaction au plus).
- **Cacher la coupe quand l'effet est la continuité** (trucage : cache sur l'union des silhouettes, rien de vivant hors du cache) ; **la montrer quand l'effet est la comparaison** (cut sec, même cadre = règle graduée) ; peu de montage quand le sujet est la simplicité. [ÉPROUVÉ EN MAQUETTE] (pièces 30, 32)
- **Une boucle parfaite tue une chute** (finir sur l'état de départ) : boucler seulement quand le sujet est un cycle. [ÉPROUVÉ EN MAQUETTE] (pièce 30)
- Le 9:16 montre un corps, pas un espace : champ-contrechamp et plan large deviennent des exceptions ; un écran partagé fait **comprendre** un écart, l'alternance plein cadre le fait **sentir**. [ÉPROUVÉ EN MAQUETTE] (pièce 29)

## YouTube long format (5-60 min)
Spectateur choisi mais révocable : promesse tenue avant 30 s, relances, voix d'abord, fin nette. Tout le détail : `montage-youtube` (fait foi).

## Clip musical
- La musique est le scénario : couper sur l'arrangement (macro) ou sur les temps (micro), le décider (`montage-rythme`). Ziak : macro ; Gondry : une couche sonore = une famille visuelle ; Jonze : quand le corps produit le rythme, le montage se retire.
- **Vu sur huit clips** [VU SUR IMAGES] (`analyses/clips/`) : aucun ne coupe sur les temps plus qu'au hasard ; la densité suit l'arrangement (Ziak 32 / 16 coupes/min selon la basse) ou les rares coupes tombent sur les grands accents (Gavras). Les plans longs sont **des mouvements qui relient** (individu → foule, lieu → lieu), placés aux articulations ; entre eux, un rythme régulier ou **une seule rafale**, souvent un inventaire (Gare du Nord, 6G). **Le sommet est porté par le cadre**, pas par la coupe (STORM : 131 plans en 4 min 17, puis le sommet en 5 plans de 21 à 60 s). L'ouverture construit l'image ; l'habillage vient du sujet (plan de métro, interface de jeu), aucun carton décoratif.
- Une idée de forme forte (concept, dispositif, plan-séquence) vaut mieux qu'un récit.
- Déclinaisons verticales tirées des mêmes rushes : un tournage, deux montages (`montage-direction-artistique`).

## Corporate, institutionnel, film de marque
- Spectateur **professionnel et sceptique** : des preuves, pas des adjectifs ; **la forme est l'argument** (paires de plans « deux vies » ; Honda « Cog » : quand la preuve est l'argument, ne pas couper).
- Durée : 1 min 30 à 3 min pour un film de présentation ; au-delà, chapitrer.
- **Pièges** : ukulélé start-up, drone sur le siège, sourires face caméra, mains d'artisan au ralenti en lumière dorée, têtes parlantes en série, mots-valeurs à l'écran.
- Son : dialogue au premier plan, musique basse ; loudness hors plateformes **à sourcer** (BACKLOG 0f).
- **Vu sur des vidéos réelles** [VU SUR IMAGES] : le meilleur moment des commandes du studio est **quand la forme dit le bénéfice** (une seule carte au lieu d'un portefeuille chez Swile, les questions du jeu qui sont la formule du sérum chez Sephora) ; le défaut le plus fréquent est **la lisibilité muette** (sous-titres fins de Sephora). Emprunts au doc YouTube pour un film explicatif : densité selon le type de phrase, **le schéma qui se transforme comme plan-thèse** (CIA, 46 s), **un format ou un cadre par époque** pour un historique (KAIZEN, adidas), **un témoin anonyme = un avatar, une couleur, une police** (YggTorrent). Pour une série de marque : un système fixe (cartons, couleur par décor, tempo), comme les deux « Qui est l'imposteur » (mêmes chiffres à 10 % près).

### Dispositifs pour filmer l'humain (sans l'interview en intermède)
1. **La compétence** : un geste de métier précis, filmé assez longtemps pour qu'on comprenne qu'il est difficile.
2. **L'objet-témoin** : chacun raconte un objet ou un dossier qu'on suit ensuite.
3. **Le portrait muet** : 3-4 s de regard caméra, rare.
4. **La voix sur le geste** : interview en son seul sur la personne au travail.
5. **La question-cadre** : une situation (réunion, visite, objection) dont les témoignages deviennent les réponses.
6. **Éthique** : aucune situation personnelle (insertion, santé, handicap) sans accord explicite ; présenter par la fonction.
7. **Série de portraits** : un fond, un plan, une règle jamais trahie (modèle des live sessions, `montage-youtube`).

## Documentaire
- Le récit se trouve au montage : dérushage complet, transcription, structure (`montage-premiere`).
- **Le fil est une voix ou un regard**, pas un sujet (Varda) ; la voix off s'écrit après le montage, par passes.
- Ne pas monter le choc quand le plan continu est la vérité du moment (Murai) ; ellipse, digression, rimes d'objets.
- **Vu sur quatre docs YouTube et KAIZEN** [VU SUR IMAGES] : densité en vagues **commandées par le texte** (EGO, de 3 à 29 coupes/min) ; chapitres par le noir et 2 à 4 s de silence, silences rares donc lisibles ; **le plus long plan porte la thèse et quelque chose change dedans** (schéma, citation qui s'écrit, sous-titre d'un témoin) ; un cadre par source (archive dans un téléviseur, CIA) ; ouvrir par la fin (YggTorrent, CIA). Un voyage se compresse au métronome de cartons « JOUR N », l'arrivée casse la cadence par un plan long (KAIZEN).

## Fiction courte
- L'émotion d'abord (Murch) ; couper à la fin d'une pensée ; tenir la tension tant que le rapport de force n'a pas basculé (Menke) ; le son peut porter les raccords. Pudeur : rester sur celui qui écoute (`montage-direction-artistique`).
- **Vu sur 13 films et deux courts du studio** [VU SUR IMAGES] : le plan le plus long va **à la réception**, pas à l'information (*Spotlight*, appels de 67 et 115 s sur celui qui écoute) ; le plus fort est suivi du plus grand vide ; le climax n'accélère pas. Les deux courts de F42 tiennent ces règles ; ce qui leur manque est de finition : **une ambiance continue sous tout dialogue** et **un minimum de lumière sur l'info** (règle dictée par Diego, GOUTS.md) dans les plans très sombres.

## Film de mariage (ajouté le 2026-10-12, trois références réseaux de Diego) [genre : mariage] [VU SUR IMAGES]
Trois films courts (44 à 49 s, verticaux, le film lui-même en 16:9 ou 1,85:1 posé au milieu ; fiches `analyses/reseaux/shcreativedept-…`, `plustwofilms-…`, `noahlazoproductions-…`). Ce qu'ils ont en commun :
- **Coupés sur les temps** (53 à 61 % des coupes à ±1 image d'un temps contre 15 % au hasard pour deux d'entre eux), plans médiane 0,9 à 1,1 s ; les détails (papeterie, fleurs, tissu, alliances) en rafale d'un temps, les gestes humains sur 3 à 5 temps.
- **Pas chronologiques** : un détail ou un cri de joie ouvre, le titre (prénoms) arrive sur le premier plan du couple, vers 9-10 s ; fin sur un geste adressé (bras levés, doigt pointé vers l'objectif) ou sur la fête.
- **La valeur humaine d'abord** : regards caméra, cris de joie, rires ; l'humour vient des mariés eux-mêmes (dialogue gardé et écrit en grand, regard vers l'objectif), pas d'effets.
- **Look pellicule** : noirs denses, blancs tenus, chroma faible, dominante olive (teinte OkLCh 106-129°) ; ou **noir et blanc neutre** à blancs doux ; le changement de look (couleur ↔ N&B) marque une séquence ou présente un personnage.
- **Voix** : les vœux ou un dialogue en voix off portent le film (plustwofilms) ; ou aucune voix (shcreativedept).
- Contre-indications : ces trois films durent 45 s ; un film de 4-6 min (le format courant d'un film de mariage livré au couple) doit tenir sur la durée : récit en actes, respirations, son direct des discours. Aucune référence de cette durée dans le corpus au 2026-10-12.

## Teaser et bande-annonce
Promettre sans raconter : poser le monde, la règle, le conflit, couper au sommet ; paliers de densité, un silence, une signature (`montage-references` § E).
- **Vu sur deux bandes-annonces d'événements de créateurs** [VU SUR IMAGES] (`analyses/pubs/crunch-creator-bande-annonce.md`, `gp-explorer-3-bande-annonce.md`) : **les noms écrits sont l'information principale** ; un line-up d’au moins une dizaine de duos (non comptés un par un) passe **par paquets** (une équipe = une couleur de garage, un plan large nommé de 1,5 à 2 s, trois à cinq portraits courts) ; **entrer et sortir du monde par un vol continu** (19,6 et 17 s sans coupe) ; dans la comédie de créateurs, **la tirade se tient en plan long** (10 et 16 s) au début et à la fin, l'action truquée et exagérée entre les deux, assumée comme gag. Ni l'une ni l'autre n'est du kinetic : peu de coupes calées, pas de SFX sur chaque coupe.

## Grille rapide
| Format | Spectateur | Son | Premier écran | Rythme dominant | Risque n°1 |
|---|---|---|---|---|---|
| Pub TV 30 s | captif | oui | moyen | une bascule | cliché de catégorie |
| Préroll / vertical | volé | non | **critique** | hybride, dense | illisible sans son |
| Short narratif | volé | non | **critique** | une chute | épilogue après la chute |
| YouTube long | choisi, révocable | oui | promesse < 30 s | l'idée, relances | promesse non tenue |
| Clip | choisi | oui | moyen | musique (micro / macro) | illustrer les paroles |
| Corporate | professionnel | oui (faible) | faible | lent → preuve | têtes parlantes |
| Documentaire | choisi, patient | oui | faible | voix / regard | commenter au lieu de montrer |
| Fiction courte | captif | oui | faible | émotion, tension | tout expliquer |

## Lacunes
- Kinetic des réseaux : **sept vidéos vues** (`analyses/reseaux/`, 2026-10-11) ; ce qui reste non vu : le face caméra à captions mot à mot (format Hormozi), la rétention réelle, les SFX à l'oreille.
- Pub de 6 et 30 s : aucune vue ; **une pub réseau de 15 s vue** (Sephora Collection, lucasbosc) ; la structure 30 s reste [THÉORIQUE]. Corporate classique (interview de dirigeant, film de présentation) : aucun vu.
- Le son est mesuré, jamais écouté. Médianes des montages rapides : des minimums.
