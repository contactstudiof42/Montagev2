---
name: montage-formats
description: Choisir la structure et les conventions d'un format — pub 6/15/30/60 s, vertical (Reels, TikTok, Shorts, LinkedIn), Short narratif, clip, corporate / film de marque, documentaire, fiction courte, teaser et bande-annonce. Mots d'un client ou d'un réalisateur : « on a 30 secondes », « une version 15 s et une 6 s », « il faut une déclinaison verticale », « film d'entreprise », « portrait de collaborateur », « témoignage client », « le corporate fait chiant », « doc de 52 minutes ». YouTube long : `montage-youtube` ; kinetic et SFX : `montage-kinetic-editing`.
---

# Narration par format

Marqueurs : [SOURCÉ] lu dans une source citée · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu seulement sur maquette Blender / Pillow / ffmpeg, hypothèse à confirmer en phase 2 · [THÉORIQUE] déduit, non vérifié.

**Fait foi sur** : la structure et les conventions par format (pub, vertical et Shorts narratifs, clip, corporate, documentaire, fiction, teaser) et la grille de choix. Pour la vidéo YouTube longue : `montage-youtube` ; pour la grammaire du style kinetic (SFX, captions, punch-in) : `montage-kinetic-editing` ; pour l'intention (le « quoi ») : `montage-direction-artistique`. Les durées citées sont des repères de métier [THÉORIQUE], à mesurer sur des références avec `labo/analyse-clip/` avant de s'y fier.

## Principe général : le format est un contrat d'attention
Spectateur captif (salle, TV), choisi (clip, YouTube), volé (fil d'actualité) ou professionnel (réunion). Le spectateur volé peut partir à chaque seconde ; le captif attend qu'on lui demande quelque chose.

## Pub 30 s / 15 s / 6 s (TV, préroll, cinéma)
- **30 s** : une idée, une seule. Installation (0-8 s), bascule (8-22 s), résolution + signature (22-30 s ; packshot 3-5 s). Deux blocs de cadence et une bascule valent mieux que trois idées (Glazer, `montage-references`). [THÉORIQUE]
- **15 s** : la bascule seule, pas un 30 s accéléré. **6 s** : un plan, un signe, la marque ; se pense installation / rupture / retour.
- **Son** activé en TV et cinéma ; **muet probable** en préroll mobile : comprendre sans son.
- **Principes de campagne** (17 campagnes d'opticiens, 3 films primés ; presse pub, aucune vidéo vue) [SOURCÉ] : un dispositif répétable + une même phrase de fin font de chaque 30 s un épisode (Specsavers) ; le gag porte le bénéfice (si on retire le produit sans casser la blague, elle est à côté) ; installer un genre pour le casser ; une révélation qui réécrit le début vaut un 2e visionnage ; séparer film d'émotion et films d'offre.
- **Pièges** : clichés de catégorie (boîte à musique, bébé au ralenti, « avant gris / après coloré ») ; **vérifier le secteur avant de défendre une évidence** (le flou → net n'est la base d'aucune des 17 campagnes d'opticiens) ; trop de texte ; logo trop tôt.
- Livraison TV France -23 LUFS (EBU R128) : `montage-loudness-livraison`.
- **Vu sur les sept pubs de référence de Diego** [VU SUR IMAGES] (`analyses/pubs/`) : (1) **le nom ou le logo arrive dans les dernières secondes dans les sept** (Intermarché à 2:55 sur 3:00, Lacoste, iPhone, adidas…) ; mais **l'objet, la tenue ou le lieu de la marque est à l'écran dès la première image** (uniformes orange et rayons, polo blanc à col vert, téléphone orange). Le « logo trop tôt » est évité, la marque n'est pas absente pour autant. (2) **Le gag porte le bénéfice** confirmé : iPhone 17, un téléphone glissé sur une table de négociation (geste du drame judiciaire) prouve la résistance aux rayures, tenu en plan large de 5,4 s dans le silence. (3) Films longs (2 min 30 à 5 min) : **cadence presque régulière de 1 à 2,5 s** (Intermarché « L'amour » : 90 % des plans), la variation vient du récit ; un seul plan tenu pour la fin. (4) **Silence avant le sommet** : Lacoste, 2,4 s sur le plan large du court avant le geste final ; Intermarché « Conte de Noël », une demi-seconde avant l'acceptation, et musique retirée au retour au réel. (5) Aucune ne coupe sur les temps plus qu'au hasard.

## Vertical réseaux (Reels, TikTok, Shorts, LinkedIn)
- **Premier écran = tout** : sujet lisible dès la 1re image de chaque plan, une question ou une tension avant 2 s. [ÉPROUVÉ EN MAQUETTE] (pièce 02 : 7 plans sur 19 illisibles à leur 1re image en v1)
  - **Un flou d'ouverture n'est permis que s'il est l'idée** (révélation par la mise au point, net avant 2 s). Vu sur deux pubs réseau du studio (Benefit, 2026) : 4,4 s de flou sous le titre dans les deux ; dans l'une, la mise au point qui révèle dit le bénéfice du produit (« blur ») et le logo finit sur le flou, c'est le meilleur moment ; dans l'autre, deux plans flous sans révélation retardent le premier écran. [VU SUR IMAGES] (`analyses/projets-f42/benefit-pubs-reseau.md`)
  - **Pub muette : l'ordre des plans est la seule phrase** ; le geste du produit doit précéder ce qu'il provoque (dans Benefit 1, le regard admiratif arrive avant le produit : la cause manque). [VU SUR IMAGES]
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
- Une idée de forme forte (concept, dispositif, plan-séquence) vaut mieux qu'un récit.
- Déclinaisons verticales tirées des mêmes rushes : un tournage, deux montages (`montage-direction-artistique`).

## Corporate, institutionnel, film de marque
- Spectateur **professionnel et sceptique** : des preuves, pas des adjectifs ; **la forme est l'argument** (paires de plans « deux vies » ; Honda « Cog » : quand la preuve est l'argument, ne pas couper).
- Durée : 1 min 30 à 3 min pour un film de présentation ; au-delà, chapitrer.
- **Pièges** : ukulélé start-up, drone sur le siège, sourires face caméra, mains d'artisan au ralenti en lumière dorée, têtes parlantes en série, mots-valeurs à l'écran.
- Son : dialogue au premier plan, musique basse ; loudness hors plateformes **à sourcer** (BACKLOG 0f).

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

## Fiction courte
- L'émotion d'abord (Murch) ; couper à la fin d'une pensée ; tenir la tension tant que le rapport de force n'a pas basculé (Menke) ; le son peut porter les raccords. Pudeur : rester sur celui qui écoute (`montage-direction-artistique`).

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
Aucune mesure sur des références réelles par format (durées de plans médianes) ; pas d'atelier en documentaire ni en fiction longue. Voir BACKLOG.
