# AUDIT du règlement — avant le projet test 2

_Session de maintenance du 2026-10-12, à la demande de Diego. Resolve n'a pas été touché ; `GOUTS.md` a été lu, jamais ouvert en écriture._

**Décisions de Diego et application (même jour)** : point 2 validé en entier ; contradictions C1 à C16 toutes appliquées ; archivage en option 4.2-2 ; `CLAUDE.md` et `PROMPT-PHASE-3.md` validés avec deux réflexes ajoutés (« aucun plan de remplissage » ; « la valeur humaine d'un plan se repère et se garde ») ; le projet 2 n'est pas choisi, « interview corporate » n'était qu'un exemple : rien de spécifique au corporate n'a été écrit dans les règles, seule la règle générale « si le corpus n'a aucune référence du genre, le dire à Diego avant de monter » a été gardée. État avant l'audit : tag Git `avant-audit`. Les notes V5 ont été intégrées (point 4.3). Le point 2.4 ci-dessous reste tel qu'il a été écrit, comme exemple de ce que le mécanisme des portées doit permettre sur un genre nouveau. Push à faire par Diego depuis le Mac (`git push origin claude/expert-montage --tags`)._

**Lu en entier** : `CLAUDE.md`, `PROMPT-PHASE-2.md`, `PROMPT-PHASE-3.md`, `RETOURS-DIEGO.md`, `CARNET-DE-GOUT.md`, `GOUTS.md`, `PROGRESS.md`, `BACKLOG.md`, `REFERENCES.md`, la synthèse de `RAPPORT.md`, les 22 `SKILL.md` (en détail : regard, kinetic-editing, resolve, grammaire, couleur-et-intention, formats, motion-design, loudness, direction-artistique, expert, pilotage-mcp, nouvelle-reference ; les autres au peigne des mentions Diego / Sony / phase 3), les annexes des skills (`details.md`, `journal.md`, `regles-atelier.md`), `projets-phase-3/sony-linkbuds/plan.md` et `note-de-livraison.md`.

**Deux faits à connaître avant de lire** :
- La dernière section de `RETOURS-DIEGO.md` (« notes de Diego sur la V5 », 60 lignes) **n'est pas commitée** (`git status` : `M RETOURS-DIEGO.md`) et **n'est pas marquée « intégrée »**. Elle contient la liste « Portée des règles nées sur Sony (pour l'audit) » : c'est elle qui sert de juge au point 2 ci-dessous.
- `PROGRESS.md` dit encore « attendre les notes sur la V5, puis V6 si besoin » ; les notes disent « pas de V6, audit puis projet test 2 ». `PROGRESS.md` est donc en retard d'une étape.

---

## Résumé en dix lignes

1. Le règlement est juste sur le fond mais **écrit quatre à six fois** : la même règle vit dans `PROMPT-PHASE-3`, `montage-regard`, le carnet, `RETOURS-DIEGO` et souvent un skill de genre. Chaque nouvelle version diverge un peu des autres.
2. **Une règle née sur Sony est marquée [universel] à tort** dans `PROMPT-PHASE-3` § 8 : « ne jamais réutiliser un même passage de rush ». Diego la classe [genre : after movie]. Les skills (grammaire, formats, carnet) l'avaient bien limitée au genre ; c'est le prompt qui déborde.
3. **Sept règles [universel] sont écrites avec les mots de Sony** (produit, packshot, références réseaux, noirs denses, eyecannndy, `analyses/reseaux/`) : vraies partout, mais un projet d'interview corporate ne s'y reconnaîtra pas. À reformuler, pas à rétrograder.
4. **Trois contradictions réelles** : le titre (« jamais un fondu » contre « fondu + montée ») ; la stabilisation (« stabiliser, remplacer **ou justifier** » contre « un plan qu'on ne peut pas stabiliser, on le remplace ») ; le son des transitions (« toutes les coupes n'ont pas de son » contre « un son sur chaque transition ») : la réconciliation existe (transition ≠ coupe, validée par Diego) mais n'est écrite nulle part dans le skill.
5. **Huit passages périmés** : `PROMPT-PHASE-3` demande encore de construire `tremblement.py` et de chercher l'exécutable Gyroflow (faits, et la version App Store ne marche pas) ; le sommaire de `montage-expert` dit Resolve [THÉORIQUE] et « aucune vidéo kinetic dans le corpus » ; `montage-nouvelle-reference` ignore les catégories `reseaux/` et `methodes/` ; `PROGRESS.md` attend une V6.
6. **Les marqueurs de fiabilité n'ont pas de liste canonique** : `CLAUDE.md` en donne cinq, les skills en utilisent neuf ([SOURCÉ], [TESTÉ EN CONDITIONS RÉELLES], [RÈGLE DU STUDIO], [VU SUR SPECTROGRAMME], [mesuré]…).
7. **Pour le projet test 2 (interview corporate) : le corpus ne contient aucune interview corporate** (`montage-formats`, « Lacunes » ; `PROGRESS.md`). La règle « 6 images à côté de 6 références du genre » ne peut pas s'appliquer sans d'abord déposer deux ou trois références du genre dans `videos/a-traiter/`.
8. Proposition : **une règle, un fichier maître, les autres renvoient**. Skills = règles ; carnet = le goût avec images ; `PROMPT-PHASE-3` = mission et ordre de travail ; `RETOURS-DIEGO` = la parole brute, archivée une fois intégrée.
9. `CLAUDE.md` passe de 30 à environ 25 lignes, mais plus denses ; `PROMPT-PHASE-3` passe de 23 Ko à une page essentielle plus quatre annexes (dont la session 0, terminée, et les recettes qui sont déjà dans les skills).
10. Archivage : 17 des 18 sections de `RETOURS-DIEGO.md` sont intégrées ; proposition de les copier dans `archives/retours/RETOURS-DIEGO-2026-10-11-sony.md` en gardant dans le fichier vivant un index d'une ligne par retour, plus les points encore ouverts. Rien n'est perdu.

---

## 1. Doublons et contradictions

### 1.1 Doublons : la même règle écrite en plusieurs endroits

| Règle | Où elle est écrite | Fichier maître proposé |
|---|---|---|
| 6 images de ma version à côté de 6 images de références, avant le montage (look) et avant chaque livraison | `PROMPT-PHASE-3` § 1 (deux fois), « Leçons de phase 3 » (comparaison), `montage-regard` « Juger sa propre version » 1, `CARNET` entrée 1, `montage-couleur-et-intention` (paragraphe Sony), `RETOURS` (leçon de méthode V2) | `montage-regard` |
| Jamais de transition intégrée (glissement, poussée, volet) | `PROMPT-PHASE-3` § 1 et leçons, `montage-regard` (intro de « Juger sa propre version »), `montage-kinetic-editing` § 2 « Transitions interdites », `CARNET` 3, `RETOURS` V2 | `montage-regard` (règle [universel]) ; le skill kinetic renvoie |
| Jamais deux fois le même passage d'un rush | `PROMPT-PHASE-3` § 8 (exemple), `montage-grammaire` (section entière), `montage-formats` (vertical réseaux), `montage-regard` 7, `CARNET` (rythme et son), `montage-kinetic-editing` (« à écarter : stutter »), `RETOURS` | `montage-grammaire` ; les autres renvoient |
| Séries du cadreur (K-O-R-E) | `PROMPT-PHASE-3` leçons (comparaison), `montage-regard` 5, `CARNET` 4, `RETOURS` | `montage-regard` |
| Gyroflow : philosophie (fluide, pas figé ; fixe ou rail) et recette | `PROMPT-PHASE-3` § 3, `montage-resolve` (recette complète), `montage-regard` 3, `montage-pilotage-mcp` (bac à sable macOS), `CARNET` 5, `RETOURS` (deux sections) | philosophie : `montage-regard` ; recette : `montage-resolve` |
| Direction artistique avant les effets (`da.md`, 8 à 12 images) | `PROMPT-PHASE-3` § 5, `montage-regard` 9, `CARNET` 12, `RETOURS` « Trois outils » ; **absente de `montage-direction-artistique`**, le skill qui « fait foi » sur la DA | `montage-direction-artistique` (à y ajouter) |
| Variantes sur les moments clés | `PROMPT-PHASE-3` § 6, `montage-regard` 11, `RETOURS` | `montage-regard` |
| Carnet de goût (quoi, quand le relire) | `PROMPT-PHASE-3` § 7, `montage-regard` 12, en-tête du `CARNET`, `RETOURS` | en-tête du `CARNET` |
| Portée d'une règle ([universel] / [genre] / [projet]) | `CLAUDE.md`, `PROMPT-PHASE-3` § 8, en-têtes de deux sections de `RETOURS`, en-tête du `CARNET` | `CLAUDE.md` (définition courte) ; `PROMPT-PHASE-3` renvoie |
| Le brief prime ; jamais cheap | `PROMPT-PHASE-3` § 1 et leçons, `montage-regard` 2, `CARNET` (rythme et son, deux entrées), `montage-kinetic-editing` § 2 et § 4 bis, `RETOURS` V3 « Principes rappelés », `montage-direction-artistique` (« le goût du client prime sur le mien ») | `CLAUDE.md`, bloc « Les principes de Diego » (proposé au point 3) |
| Étalonner plan par plan, visages image par image, noirs denses | `montage-regard` « Le goût de chaque plan », `CARNET` 8-10, `PROMPT-PHASE-3` § 8 (exemples), `RETOURS` V4 | `montage-regard` |
| Pas de limite de temps en phase 3 | `PROMPT-PHASE-3` « Chaque session », `RETOURS` V3 ; `PROMPT-PHASE-2` dit 50 min (phase 2 seulement) | `CLAUDE.md` |
| Démarrage de session | `CLAUDE.md`, `PROMPT-PHASE-3` « Chaque session », `PROMPT-PHASE-2` « Chaque session », `PROGRESS.md` (« désormais… »), `RAPPORT.md` (« hors phase 3… ») | `CLAUDE.md` seul |
| Monter un projet confié (ordre de travail) | `PROMPT-PHASE-3` étapes 1-5, `montage-expert` « Travailler en autonomie » (parle d'`INTENTION.md`, nom de l'atelier), `montage-pilotage-mcp` « Boucle de travail » | `PROMPT-PHASE-3` ; les deux skills renvoient |
| Règles de sécurité (pas de dépense, projet de test, médias en lecture seule) | `CLAUDE.md` « Règles permanentes », `PROMPT-PHASE-3` « Règles de sécurité », `montage-pilotage-mcp` règles 1, 9, 12 | `CLAUDE.md` (permanentes) + `PROMPT-PHASE-3` (propres à Resolve) |
| Marqueurs de fiabilité | `CLAUDE.md` (5 marqueurs), redéfinis en tête de chaque skill avec des listes différentes | `CLAUDE.md`, liste canonique (point 3) |
| Pièges zsh (`=====`), lire les fichiers un par un | `CLAUDE.md` étape 2, `PROGRESS.md` « Règles de session » | `PROGRESS.md` seul |
| Bibliothèque eyecannndy | `PROMPT-PHASE-3` § 1, `montage-kinetic-editing` § 4 bis (table), `CARNET` (dernier pic) | `montage-kinetic-editing` |

### 1.2 Contradictions (à trancher)

| # | Contradiction | Où | Proposition |
|---|---|---|---|
| C1 | **Portée de « jamais deux fois le même passage »** : `PROMPT-PHASE-3` § 8 la cite parmi les exemples [universel] ; `montage-grammaire`, `montage-formats`, `montage-regard` 7 et le carnet la limitent à l'after movie, l'événementiel et le run and gun ; Diego (notes V5) : [genre : after movie], avec « beaucoup d'exceptions ailleurs : flashback, humour, podcast ». | `PROMPT-PHASE-3` § 8 | Retirer l'exemple de la liste [universel] du § 8 ; remplacer dans `montage-grammaire` le tag non standard [RÈGLE DU STUDIO] par [genre : after movie, événementiel, run and gun]. |
| C2 | **Titre** : `montage-motion-design-principes` principe 19 : « révélation qui a une matière […], **jamais** un grossissement uniforme ou un fondu » (leçon de la V2) ; section « Titre de marque » du même skill : « **fondu** + montée de 15 à 20 px + léger flou […] pas de grossissement » (leçon de la V3, « simple et épuré, à la Apple », consigne de Diego). | `montage-motion-design-principes` | La V3 l'emporte (c'est la consigne de Diego). Réécrire le 19 : « une révélation choisie et sobre ; jamais un grossissement uniforme ni un effet de bibliothèque ; sinon, pas de texte ». |
| C3 | **Stabilisation impossible** : `montage-regard` 3 : « au-delà du seuil : stabiliser, remplacer **ou justifier** dans la note de livraison » ; Diego (notes V5, [universel]) : « un plan qu'on ne peut pas stabiliser, on le remplace », au maximum 10 essais, sauf tremblement voulu. | `montage-regard` 3, `PROMPT-PHASE-3` § 2 (« sinon justifie-le ») | Retirer « justifier » ; écrire la règle des 10 essais et l'exception du tremblement voulu (brief). |
| C4 | **Son sur les transitions** : `montage-kinetic-editing` § 2 (règles SFX) : « toutes les coupes n'ont pas de son » et statut : « aucune [référence] ne pose un whoosh sur chaque coupe » ; § 4 bis [genre] : « un son sur chaque transition, ou aucun ». Réconciliation : transition = effet ou changement de bloc, pas les coupes franches internes ; Diego l'a validée (notes V5), mais la définition n'est écrite que dans `note-de-livraison.md` et les doutes de `RAPPORT.md`. | `montage-kinetic-editing` | Écrire la définition validée à côté de la règle [genre] : « transition = effet ou changement de bloc ; les coupes franches à l'intérieur d'un bloc n'ont pas de son à elles ». |
| C5 | **Gyroflow, où et comment** : `PROMPT-PHASE-3` § 3 : « trouve l'exécutable (probablement dans `/Applications/Gyroflow.app`) et lis son `--help` » ; `montage-resolve` : la version App Store est en bac à sable et ne lit pas les disques externes, utiliser `~/Applications/Gyroflow-GitHub.app`. `RETOURS` V2 : « rendu dans `_travail/`, sans toucher aux originaux » ; précision suivante : « ne copie pas les rushes, écris à côté des originaux ». | `PROMPT-PHASE-3` § 3 | Le § 3 du prompt ne garde que la règle de sécurité (accord de Diego avant d'écrire dans le dossier source, suffixe `_stabilized`, jamais `-f` sur un nom existant) et renvoie à `montage-resolve` pour la recette. |
| C6 | **« Toujours Gyroflow d'abord »** (`montage-resolve`) contre « mesurer le résultat, garder le brut s'il est meilleur » (`montage-resolve`, `montage-regard`) et « Gyroflow seul tremblait 3 à 6 fois plus » (`PROGRESS.md`). Les deux sont vrais mais lus à la suite, ils se contredisent. | `montage-resolve` | « Gyroflow d'abord **quand le rush a des données gyroscopiques et que le plan tremble au-delà du seuil** ; puis mesure du rendu ; le brut ou le rail l'emportent s'ils mesurent mieux. » Une interview sur pied n'en a pas besoin. |
| C7 | **Nom du projet de test** : `PROMPT-PHASE-3` : préfixe `P3-` (`P3-<projet>-agent`) ; `montage-pilotage-mcp` règle 1 : `TEST_<sujet>_<date>` ; squelette de `montage-resolve` : `TEST_SCRIPT_2026`. | trois fichiers | Une convention : `P3-<projet>-agent` ; les deux skills renvoient. |
| C8 | **Où vont les retours de Diego** : `CLAUDE.md` : dans `RETOURS-DIEGO.md` ; `montage-pilotage-mcp` « Boucle de travail » 7 : « ses retours vont (par lui) dans `GOUTS.md` ». | `montage-pilotage-mcp` | Corriger la boucle : retours → `RETOURS-DIEGO.md` ; goûts dictés → `GOUTS.md`. |
| C9 | **Réglages d'export** : `montage-loudness-livraison` « Master du studio depuis Resolve » : H.265 Main 10, ≈ 40 Mb/s, « par défaut pour tout rendu final » ; même skill, « Vérifier le livrable » : attendu `High`, `yuv420p` (H.264 8 bits) ; conseil « -1,5 dBTP » contre verdict de `montage-regard` « ≤ -1 dBTP » et rendus Sony à -1,1. | `montage-loudness-livraison`, `montage-regard` | Écrire : « réglage par défaut du studio (Diego) : H.265 Main 10 ; **la spec du client prime** (TV, plateforme, agence) » ; mettre la vérification à jour pour les deux cas ; une seule cible de crête (-1,5 dBTP visé, ≤ -1 accepté). |
| C10 | **Look par défaut** : `montage-couleur-et-intention` donne deux défauts quand le brief ne dit rien : « look film léger = bon point de départ » (dicté par Diego) et « proposition par défaut : images basses et denses, environnement froid » (hypothèse de l'agent). | `montage-couleur-et-intention` | Ordre explicite : brief > `GOUTS.md` (look film) > hypothèse de l'agent, à ne proposer que comme variante. |
| C11 | **Sommaire de `montage-expert` périmé** : Resolve et pilotage-mcp [THÉORIQUE], kinetic « aucune vidéo kinetic des réseaux dans le corpus », « rien n'est encore vérifié dans un vrai logiciel », goûts « état au 2026-10-10 ». Contredit `PROGRESS.md`, `montage-kinetic-editing` et `montage-resolve`. | `montage-expert` | Mettre le tableau à jour (ou le supprimer : chaque skill dit déjà sur quoi il fait foi). |
| C12 | **Catégories de références** : `montage-nouvelle-reference` § 1 ne connaît que `films/ clips/ pubs/ youtube/ projets-f42/` ; `reseaux/` et `methodes/` existent depuis le 2026-10-11 (`REFERENCES.md`, `PROGRESS.md`). | `montage-nouvelle-reference` | Ajouter les deux catégories et la règle « tutoriel = méthode, pas analyse de montage ». |
| C13 | **Étape 6 (comparaison)** suppose `final-diego/` et une version de Claude nu (`rendus-nu/`) ; Sony n'a pas eu de version de Diego, et rien ne dit si le projet 2 aura un Claude nu. | `PROMPT-PHASE-3` | Rendre l'étape conditionnelle : « si Diego dépose sa version et / ou une version de Claude nu ». |
| C14 | **`PROGRESS.md`** : « prochaine étape : attendre les notes sur la V5, puis V6 si besoin » ; notes V5 : « pas de V6 ». | `PROGRESS.md` | À réécrire à la prochaine session (après validation de cet audit). |
| C15 | **Numérotations cassées** : `montage-regard` « Juger sa propre version » : 1, 2, 3, **7**, 4, 5, 6, 7 ; `PROMPT-PHASE-3` étapes : 1, 2, 3, **2 bis, 3 bis**, 4, 5. | deux fichiers | Renuméroter (et mettre les « bis » à leur place dans l'ordre de travail : genre → dérush → plan → DA → look / mouvement → montage → juger). |
| C16 | **Marqueurs** : `CLAUDE.md` liste [VU SUR IMAGES], [TESTÉ EN LABO], [ÉPROUVÉ EN MAQUETTE], [THÉORIQUE], [NON VÉRIFIÉ] ; les skills utilisent aussi [SOURCÉ], [TESTÉ EN CONDITIONS RÉELLES], [RÈGLE DU STUDIO], [VU SUR SPECTROGRAMME], [mesuré], [INCERTAIN], [À TRANCHER EN PHASE 3]. | partout | Liste canonique de sept marqueurs dans `CLAUDE.md` (point 3) ; les variantes locales (spectrogramme, mesuré) deviennent une précision entre parenthèses. |

---

## 2. Portée des règles : vérification tag par tag

Juge : la liste « Portée des règles nées sur Sony (pour l'audit) » dictée par Diego (notes V5), puis le cas test « interview corporate » : si la règle n'a pas de sens pour une interview filmée sur pied, elle n'est pas [universel] telle qu'elle est écrite.

### 2.1 Les onze règles classées par Diego, et ce que disent les fichiers

| Règle | Portée selon Diego | Tag dans les fichiers | Verdict |
|---|---|---|---|
| Jamais deux fois le même passage d'un rush | [genre : after movie] (au sens large), beaucoup d'exceptions ailleurs | `PROMPT-PHASE-3` § 8 : cité comme **[universel]** ; grammaire : [RÈGLE DU STUDIO] limité au genre ; formats, regard 7, carnet : genre | **Faute** dans `PROMPT-PHASE-3` § 8. Les skills sont justes. |
| Chaque transition a son son | [genre : kinetic], ~80 % des after movies | kinetic § 4 bis [genre], carnet [genre], `PROMPT-PHASE-3` § 8 exemple [genre] | Juste. Il manque la définition de « transition » (C4). |
| Analyser les visages | [universel] | regard 3, carnet 10 [universel] | Juste. |
| Pas de flou raté (le flou volontaire reste permis) | [universel] ; liste des flous ratés **provisoire** (message coupé) | regard 2, carnet 16 [universel], provisoire signalé | Juste ; la fin de la liste reste à dicter. |
| Ne jamais brûler les blancs | [universel] sauf volonté artistique du brief | regard 7 et carnet 6 : « le blanc **du produit** garde sa matière » | Juste mais **écrit pour un packshot**. Reformuler : « aucun blanc brûlé (produit, peau, fenêtre, ciel), sauf si le brief veut dégrader l'image ». |
| Packshots propres, vérifiés à 200 % (cheveux, poussière) | [universel] | **nulle part** (les notes V5 ne sont pas intégrées) ; regard 10 ne parle que du bord d'un détourage | À ajouter dans `montage-regard` « Le goût de chaque plan » : « tout plan produit ou objet se vérifie à 200 % : poussière, cheveux, traces, reflets ». |
| Remplacer un plan qu'on n'arrive pas à stabiliser | [universel] sauf tremblement voulu | regard 3 : « stabiliser, remplacer **ou justifier** » | **Contradiction** (C3) : retirer « justifier », ajouter « 10 essais au plus ». |
| Pas de transitions façon PowerPoint | [universel] sauf parodie demandée par le brief | carnet 3 [universel] ; kinetic § 2 **sans tag, dans un skill de genre** ; regard : dans le texte, sans tag | Déplacer la règle maître dans `montage-regard` avec [universel] et l'exception « parodie » ; kinetic renvoie. |
| Jamais cheap | [universel] | partout [universel] | Juste. |
| Contrôle de photosensibilité | [universel] dès qu'il y a des flashs ; inutile sinon | kinetic § 5 « obligatoire dès qu'il y a flash ou strobe » ; absent du verdict « livrable » de regard | Ajouter au verdict de `montage-regard` : « et `flash_check.py` si le film contient un flash ». |
| Flashs et inversions sur les temps forts | [genre : kinetic], parfois after movie, très rarement ailleurs | carnet 14 [genre], kinetic [genre], `PROMPT-PHASE-3` § 8 | Juste. |

### 2.2 Règles marquées [universel] mais écrites avec les mots de Sony

Elles sont vraies partout ; c'est leur formulation qui est [projet]. Sur une interview corporate, l'agent risque soit de les ignorer (« il n'y a pas de produit »), soit de les appliquer de travers (« il faut des noirs denses » sur un fond blanc de studio).

| Où | Formulation actuelle | Ce qui est Sony dedans | Reformulation proposée |
|---|---|---|---|
| `montage-regard` « Juger sa propre version » 1 ; `PROMPT-PHASE-3` § 1 | « 6 images (ouverture, **produit**, sommet, texte, transition, fin) […] avec 6 images des références (**`analyses/reseaux/`**, films, pubs) » | les six moments et le dossier de références sont ceux d'un film de marque kinetic | « 6 images aux moments clés **du genre** (pour une interview : ouverture, le visage en lumière, un insert, un titre ou un sous-titre, la fin) […] à côté de 6 images de références **du même genre** ; s'il n'y en a pas dans le corpus, en demander avant de monter » |
| `montage-regard` 2 | « Le brief prime sur le goût moyen des références. Quand il demande "très rapide, beaucoup d'effets", j'ose autant qu'un monteur kinetic » | l'exemple est le brief Sony | « Le brief fixe le niveau d'énergie et de retenue ; les références fixent le niveau de finition. Un brief calme se monte calme, un brief excessif se monte excessif, puis propre. » |
| `montage-regard` 3 | seuils « 2 px de moyenne / 5 px de pic », « calibrés le 2026-10-11 » | calibrés sur les rushes Sony ZV-E1, image 1080 verticale | garder la méthode [universel] ; marquer les seuils « [calibrés sur Sony ; à recalibrer sur un plan fixe du nouveau projet] » |
| `montage-regard` « Le goût de chaque plan » 7 ; carnet 6 | « Un blanc **de produit** garde sa matière : le comparer à la **photo produit de la marque** » | packshot | voir 2.1 (blancs brûlés) |
| `montage-regard` 9 ; carnet 9 | « **Noirs denses**, pas de bruit » | la salle de sport sombre de KORE | « Les noirs sont posés où le brief et la DA les veulent ; des ombres relevées qui montrent le bruit du capteur sont une faute, pas un style. » (Une interview corporate lumineuse n'a pas de noirs denses.) |
| `montage-regard` 11 ; `PROMPT-PHASE-3` § 6 | variantes sur « ouverture, **chaque collage ou détourage**, transition majeure, sommet, titre et fin » | la liste des moments clés est celle de Sony | « sur les moments clés du genre (pour une interview : ouverture, premier insert, titre / sous-titres, fin) » |
| `PROMPT-PHASE-3` § 1 | « Bibliothèque d'idées : eyecannndy.com […] pour varier les effets » | utile en kinetic seulement | [genre : kinetic, dynamique] ; renvoyer à `montage-kinetic-editing` § 4 bis |
| `PROMPT-PHASE-3` § 2 et § 3 | mesure du tremblement « pour chaque plan retenu » ; Gyroflow | la mesure est [universel] ; Gyroflow suppose des rushes à données gyroscopiques (ZV-E1), tournés à la main | « Mesure sur chaque plan retenu [universel]. Gyroflow seulement si les rushes portent des données gyroscopiques et tremblent ; une interview sur pied n'en a pas besoin. » |
| `montage-couleur-et-intention` (paragraphe Sony) | « noirs 5 à 11 sur 255 » comme référence | mesuré sur sept vidéos réseaux | marquer [genre : réseaux, look film] |
| `montage-couleur-et-intention` « Séparer les teintes » | méthode OkLCh (universelle) mêlée à « peau ≈ 50-60° », « Sony : −0,8 diaph », « une LUT par lumière (salle, jour, rouge) » | les chiffres et les LUT sont Sony | séparer : méthode [universel] ; chiffres « [mesurés sur Sony, à revérifier] » ; les LUT en [projet] |
| `montage-motion-design-principes` « Titre de marque » | « animer à la Apple », sobre même dans une vidéo très dynamique | « à la Apple » est la consigne de Diego pour Sony | [genre : film de marque] : « reprendre la DA du client ; apparition sobre par défaut, sauf si la DA du client a son propre langage de mouvement » |
| `montage-loudness-livraison` « Master du studio » | « par défaut pour tout rendu final : H.265 Main 10, ≈ 40 Mb/s » | réglage dicté sur Sony | garder comme défaut du studio, avec « la spec du client prime » (C9) |
| `montage-resolve` « Toujours Gyroflow d'abord » | cité comme règle de Diego | conditionnée au matériel | voir C6 |
| carnet 2 | « Le titre reprend la DA **de la marque** » | film de marque | « la DA du client (marque, charte, logo existant) » |
| `PROMPT-PHASE-3` « Leçons de phase 3 » | quatre paragraphes Sony **sans aucun tag**, qui mêlent [universel] (rendre tôt, séries du cadreur, DA avant effets, variantes, mesurer le résultat) ; [genre] (la musique décide de la structure, techniques tirées de la matière, dernier pic, un son par transition) ; [projet] (KORE, oreilles, rouge) | tout | voir point 3 : annexe A4 avec un tag par leçon |

### 2.3 Règles [genre] correctement limitées (rien à changer)

Rafales qui reviennent avec écart ; techniques variées tirées de la matière ; un son sur chaque transition (sous réserve de C4) ; inversions à la place de certains flashs ; dernier pic avant la signature puis fin courte ; états de l'image (naturel / N&B / négatif / seuil) ; stutter et boomerang écartés ; le kinetic de Diego = mélange des deux. Toutes portent leurs contre-indications (film calme, luxe, interview, documentaire).

### 2.4 Ce que le projet « interview corporate » va mettre à l'épreuve

- **Aucune référence du genre dans le corpus** (`montage-formats` « Lacunes » : « corporate classique : aucun vu » ; `PROGRESS.md` idem). Avant la première session du projet 2, déposer dans `videos/a-traiter/` deux ou trois interviews corporate que Diego juge réussies (et, s'il en a, une de Studio F42). Sans cela, la règle « se comparer aux références du genre » tourne à vide.
- Les skills qui s'appliquent vraiment : `montage-grammaire` (interview, J-cut / L-cut, plans de coupe), `montage-formats` (corporate : « des preuves, pas des adjectifs », dispositifs pour filmer l'humain), `montage-son-et-emotion`, `montage-loudness-livraison` (film d'entreprise : -16 LUFS web, -18 salle), `montage-couleur-et-intention` (peau, lumière motivée), `montage-motion-design-principes` (lower third, lisibilité). Leur statut : [THÉORIQUE] pour l'interview (« seuil du jump cut non tranché », « aucun face caméra en jump cuts mesuré »).
- Ce qui devient hors sujet et doit le rester : eyecannndy, flashs, SFX sur transitions, dernier pic, Gyroflow, inversions, collages. Le mécanisme existe déjà (`plan.md` commence par le genre ; `PROMPT-PHASE-3` § 8 : « relis seulement les règles [universel] et celles du genre ») ; il tiendra si le point 2.2 est appliqué.
- Nouveau pour l'agent : la parole structure le film (pas la musique) ; il n'entend pas le son (toute coupe dans la parole se juge au spectrogramme) ; le genre impose une règle [genre] qui n'existe pas encore : **une ambiance continue sous toute la parole**, « jamais de fondu au milieu d'une phrase » (`montage-grammaire`, déjà là, [THÉORIQUE]).

---

## 3. Proposition : `CLAUDE.md` et `PROMPT-PHASE-3.md` plus courts et hiérarchisés

Principe : **une règle, un fichier maître**. `CLAUDE.md` = qui je suis, le démarrage, les interdits, les principes de Diego, les conventions (portée, marqueurs). `PROMPT-PHASE-3` = la mission, l'ordre de travail, les règles de sécurité propres à Resolve ; le détail en annexes. Les règles de métier sont dans les skills ; le goût dans le carnet ; les recettes dans `montage-resolve`.

### 3.1 `CLAUDE.md` proposé (texte complet)

```markdown
# CLAUDE.md — assistant expert en montage de Studio F42

Tu es l'assistant expert en montage, motion design, truquage et étalonnage de Studio F42 (Diego).
Ta mémoire est ce dépôt : tu ne sais que ce que tu as écrit, commité et poussé (branche `claude/expert-montage`, jamais une autre).

## Démarrage, à chaque session
1. `git pull`. Lis `PROGRESS.md`, puis `RETOURS-DIEGO.md` (chaque retour non marqué « intégré » : intègre-le là où sa portée l'envoie, puis marque-le « intégré le <date> »), puis `videos/a-traiter/` et `videos/NOTES-DIEGO.md` (nouvelle référence → skill `montage-nouvelle-reference`, puis `REFERENCES.md`).
2. Routine (lancée seule) : rien d'autre. Si la boîte est vide et qu'aucun retour n'attend, dis-le en une ligne et arrête-toi. Une routine ne pose aucune question (doutes → `RAPPORT.md`), ne lance jamais la phase 3 et ne touche jamais à Resolve.
3. Session phase 3 (Diego la lance et le dit) : `PROMPT-PHASE-3.md`. Lis alors aussi `GOUTS.md`, `CARNET-DE-GOUT.md` et la synthèse de `RAPPORT.md`.

## Interdits
- Aucun média dans Git (`videos/` est ignoré ; `git status` avant chaque commit ; planches PNG < 500 Ko).
- `GOUTS.md` est la parole de Diego : tu n'y écris que ce qu'il dicte. Tes hypothèses de goût vont dans `RAPPORT.md`.
- Aucune dépense, aucun compte créé, rien de publié, aucun message envoyé. Seule exception, en phase 3 : télécharger des sons sur les banques où Diego est déjà abonné, avec son compte (voir `PROMPT-PHASE-3.md`).
- Aucune leçon [projet] ne remonte dans un skill ; aucune leçon [genre] ne s'écrit sans le nom du genre et ses contre-indications.

## Les principes de Diego (ses mots ; ils priment sur les skills)
- « Un brief, c'est un brief ; mes préférences, c'est mes préférences. » Le brief d'abord, `GOUTS.md` quand le brief ne dit rien, mon goût en dernier.
- « On ne fait pas les choses de manière cheap. » Un effet seulement si la matière le permet et s'il peut être exécuté proprement ; sinon, on ne le fait pas.
- « Compare l'image, libère-toi du chiffre. » Les mesures vérifient ; le jugement se fait en regardant mon image à côté d'images pro, en pleine résolution.
- « Je préfère que ça mette plus de temps et que le rendu soit propre. » Pas de limite de temps en phase 3.
- « Mon silence n'est pas une validation. » Rien n'est figé ; mais je ne remplace jamais un plan non critiqué sans l'écrire dans la note de livraison.

## Conventions
- **Portée de chaque règle** : [universel] (tout montage) · [genre : …] (un type de film, avec ses contre-indications) · [projet : …] (ce film seulement ; reste dans `projets-phase-3/<projet>/`). Une règle née sur un projet est [projet] jusqu'à ce que Diego la classe autrement.
- **Marqueurs de fiabilité** (un par affirmation) : [SOURCÉ] · [THÉORIQUE] · [ÉPROUVÉ EN MAQUETTE] · [TESTÉ EN LABO] · [VU SUR IMAGES] · [TESTÉ EN CONDITIONS RÉELLES (date)] · [NON VÉRIFIÉ]. Une précision de méthode va entre parenthèses (« mesuré sur spectrogramme »), pas dans un nouveau marqueur.
- **Mémoire courte** : `PROGRESS.md` et la synthèse de `RAPPORT.md` se réécrivent, ne s'empilent pas ; l'historique va dans `archives/`. Commit et push à chaque étape terminée et en fin de session.
- Pièges de shell et d'outils : `PROGRESS.md`, « Règles de session ».
```

Ce qui sort de l'actuel `CLAUDE.md` : les conseils zsh (déjà dans `PROGRESS.md`), la mention de `PROMPT.md` phase 1 et de `PROMPT-PHASE-2.md` terminée (une ligne dans `PROGRESS.md` suffit), la lecture systématique du carnet et de `GOUTS.md` en routine (inutile quand il n'y a rien à faire). Ce qui entre : les principes de Diego (dispersés aujourd'hui dans `RETOURS` et `PROMPT-PHASE-3`), la liste canonique des marqueurs, la règle « né sur un projet = [projet] par défaut ».

### 3.2 `PROMPT-PHASE-3.md` proposé : une page essentielle, quatre annexes

**Partie essentielle (ce que l'agent relit à chaque session de phase 3)**

```markdown
# MISSION — PHASE 3 : MONTER DE VRAIS PROJETS DANS RESOLVE (sessions lancées par Diego)

## Le but et la mesure
À partir de rushes, son et brief, livrer dans Resolve (par le MCP) une version presque finie. Mesure : la part « livrable » que Diego donne à chaque version, et le nombre de retours nécessaires. Projet 1 (Sony LinkBuds, kinetic) : V2 50 % → V5 80-85 %. Ce que je ne sais pas faire reste écrit : je n'entends pas le son, je juge sur mesures et images extraites.

## Règles de sécurité (priment sur tout)
1. Resolve : projets `P3-<projet>-agent` seulement ; aucun autre projet ouvert, modifié ou supprimé ; `SaveProject` avant tout geste risqué et avant de finir.
2. Médias en lecture seule (dépôt ou dossier source externe indiqué par `brief.md`) : rien n'est déplacé, renommé, réencodé, écrasé. Travail dans `videos/phase-3/<projet>/_travail/`, rendus dans `rendus/`. Seule écriture dans un dossier source : les fichiers `_stabilized` de Gyroflow, nouveaux, après accord de Diego (une fois par projet).
3. Test à l'aveugle : jamais chercher la version de Diego avant qu'il la dépose dans `final-diego/`.
4. `run_script_unsafe` seulement si aucun outil dédié ne le permet, jamais pour supprimer ; chaque usage au journal.
5. Sons et musiques : Artlist (ou une banque indiquée par Diego) avec son compte dans Chrome ; rien d'acheté, 100 téléchargements par jour au plus ; chaque son dans `sfx/` et `sfx.md`.
6. En cas de doute qui peut abîmer quelque chose : demander. Pour le reste : décider et noter.

## L'ordre de travail (fichiers texte dans `projets-phase-3/<projet>/`)
0. **Le genre d'abord** : en tête de `plan.md`, le genre, le ton, la destination. Il décide quelles règles [genre] s'appliquent. Puis relire : `brief.md`, `GOUTS.md`, les règles [universel] de `montage-regard` et du carnet, les skills du genre. Si le corpus n'a aucune référence de ce genre, le dire à Diego avant de monter.
1. **Dérusher** → `derush.md` : inventaire (métadonnées lues avant tout proxy), transcription de toute parole, planches ; par rush, les bons moments, les prises écartées et pourquoi ; les séries du cadreur et ce qu'elles appellent. L'étape la plus importante.
2. **Plan** → `plan.md` : intention en une phrase, structure par blocs avec, pour chaque bloc, « pourquoi ces plans, dans cet ordre » ; critères mesurables.
3. **Direction artistique** → `da.md`, avant le moindre effet : références pro du domaine (8 à 12 images dans `da/`), palette, matières, typographie, ce qui est exclu. Méthode : `montage-direction-artistique`.
4. **Look et mouvement** → `look.md` : le look sur 6 images à côté de 6 références du genre, en pleine résolution ; tremblement mesuré sur chaque plan retenu (`montage-regard`, « Voir le mouvement »).
5. **Monter** : un geste, une image de contrôle ; journal de chaque appel (`journal.md`). Resolve léger : look posé à la finition, effets sur des pistes à part, contrôle par rendu de plage (annexe A2).
6. **Juger et corriger** : V1 rendue, mesurée (`qc_livraison.sh`, contrôles de `montage-regard`), relue contre le carnet ; `autocritique.md` par ordre de gravité ; des variantes réellement différentes sur les moments clés ; relire le film entier après chaque série de corrections. Deux ou trois versions, puis `note-de-livraison.md` : choix, ce que Diego doit vérifier (surtout à l'oreille), ce que je n'ai pas su faire.
7. **Comparaison** (si Diego dépose sa version ou celle d'un Claude nu) → `comparaison.md` ; leçons reversées avec leur portée (annexe A4).

## Les réflexes avant chaque rendu (détail et outils : `montage-regard`)
Passage exact de chaque plan vu en pleine résolution (première, milieu, dernière image) · visages image par image · chaque plan montre ce que `plan.md` dit qu'il montre · tremblement mesuré, plan remplacé après 10 essais · exposition et couleurs clés constantes d'un plan à l'autre, aucun blanc brûlé · aucun élément graphique hors de `da.md` · un détourage ou un plan produit vérifié à 200 % · aucune transition intégrée · doublons de rush (genres concernés) · photosensibilité s'il y a un flash · 6 images contre 6 références · loudness et crête sur le fichier encodé.

## Chaque session
Démarrage de `CLAUDE.md` ; reprendre où `PROGRESS.md` s'est arrêté ; pas de limite de temps ; s'arrêter à une étape propre, projet Resolve enregistré, journal à jour ; commit et push ; `PROGRESS.md` et synthèse de `RAPPORT.md` réécrits.

Annexes : A1 session 0 (faite) · A2 recettes et méthodes (renvois) · A3 ce que le projet Sony a établi · A4 leçons de phase 3, avec leur portée.
```

**Annexe A1 — Session 0 (faite le 2026-10-11)** : le texte actuel de « Étape 0 », tel quel, avec en tête « Terminée ; résultats dans `labo/mcp/resolve-mcp.md`, `PLAN-TESTS-MCP.md`, `montage-resolve` § 4 ter. À refaire seulement si Resolve ou le MCP change de version. »

**Annexe A2 — Recettes et méthodes** : plus aucun texte de recette ; un renvoi par sujet. Se comparer aux références → `montage-regard` « Juger sa propre version » 1 · tremblement et intention du cadreur → `montage-regard` 3 · Gyroflow → `montage-resolve` (recette, version GitHub, synchronisation, plage courte) · Resolve léger (proxies, look tardif, pistes d'effets, rendu de plage) → `montage-resolve` (section à créer en y déplaçant le § 4 actuel) · DA avant les effets → `montage-direction-artistique` (section à créer en y déplaçant le § 5 actuel) · variantes et carnet → `montage-regard` 11-12 et en-tête du carnet · portée → `CLAUDE.md`. Les paragraphes actuels « construis `tremblement.py` », « trouve l'exécutable Gyroflow », « calibre le seuil » sont faits : ils disparaissent.

**Annexe A3 — Ce que le projet Sony a établi** (six lignes) : ce que je sais faire par script (clés Fusion sans `comp.Lock`, LUT fabriquées, son à la crête, rendu de plage) ; ce qui reste hors API (Magic Mask, cases « Force… » du rendu) ; les accords de Diego encore valables (LUT dans `LUT/P3/`, Artlist, `_stabilized` dans `SONY copy/RUSH/`) ; les accords ponctuels à redemander (forcer Resolve à quitter).

**Annexe A4 — Leçons de phase 3, une ligne par leçon, avec sa portée** (reprise des quatre paragraphes actuels) :
- [universel] Lire rotation et gamma des rushes avant tout proxy · dérusher en planches par rush · le dérush trouve ce que le brief ne dit pas · chercher les séries du cadreur · rendre une V0 tôt et la mesurer · l'ordre des plans a une raison écrite par bloc · un geste bloqué n'est pas un résultat impossible (chercher l'autre porte) · comparer 6 images aux références avant le montage et avant chaque livraison · la DA avant les effets · des variantes réellement différentes · mesurer le résultat, pas la méthode (un rendu « prouvé » peut trembler plus que le rush) · contrôler chaque animation par un rendu de plage · ne jamais lire les réglages d'un effet IA par script · la couleur se mesure en teinte (OkLCh) et la couleur des noirs amplifiée · le titre reprend la DA du client.
- [genre : film sur musique, kinetic, after movie] La musique décide de la structure · la folie vient de techniques différentes tirées de la matière · un dernier pic construit sur les attaques mesurées, réglé en photosensibilité à l'image près · un son par transition, calé sur l'attaque ou la crête du fichier · stabiliser selon l'intention du cadreur (fixe ou rail), Gyroflow d'abord quand les rushes ont des données gyroscopiques.
- [projet : Sony] Le zoom infini E → KORE, le flash cut des sept oreilles, la rafale « glisse » abandonnée, le passage au rouge comme sommet : exemples, pas règles ; détail dans `projets-phase-3/sony-linkbuds/`.

### 3.3 Retouches dans les skills (conséquences du point 1 et 2 ; une ligne chacune)
- `montage-regard` : renuméroter ; règle maître « transitions intégrées » avec [universel] et exception parodie ; retirer « ou justifier », ajouter « 10 essais » ; « blancs brûlés » et « noirs » reformulés ; « plan produit à 200 % » ajouté ; seuils de tremblement marqués « calibrés sur Sony » ; verdict livrable : ajouter la photosensibilité s'il y a un flash ; les listes de moments clés deviennent « du genre ».
- `montage-kinetic-editing` : « Transitions interdites » devient un renvoi ; définition de « transition » écrite à côté de la règle [genre] (C4).
- `montage-grammaire` : [RÈGLE DU STUDIO] → [genre : after movie, événementiel, run and gun].
- `montage-motion-design-principes` : principe 19 réécrit (C2) ; « Titre de marque » tagué [genre : film de marque].
- `montage-couleur-et-intention` : ordre brief > GOUTS > hypothèse (C10) ; « Séparer les teintes » : méthode [universel], chiffres et LUT marqués Sony.
- `montage-direction-artistique` : nouvelle section « La DA avant les effets sur un projet monté » (déplacée du prompt).
- `montage-resolve` : section « Garder Resolve léger » (déplacée du prompt) ; « Gyroflow d'abord » conditionné (C6) ; nom de projet `P3-` (C7).
- `montage-pilotage-mcp` : règle 1 → `P3-<projet>-agent` ; boucle 7 → `RETOURS-DIEGO.md` (C8) ; « Boucle de travail » devient un renvoi à `PROMPT-PHASE-3`.
- `montage-loudness-livraison` : défaut du studio + « la spec du client prime » ; vérification pour H.264 et H.265 ; une cible de crête (C9).
- `montage-expert` : tableau du sommaire mis à jour ou supprimé ; « Travailler en autonomie » devient un renvoi (C11).
- `montage-nouvelle-reference` : catégories `reseaux/` et `methodes/` (C12).
- `PROGRESS.md` : état réel (pas de V6 ; audit ; projet 2 à venir) (C14).

---

## 4. Archiver les retours déjà intégrés (sans rien supprimer)

### 4.1 État de `RETOURS-DIEGO.md` (18 sections, 49 Ko)

| Section (2026-10-11) | Intégrée | Reste ouvert |
|---|---|---|
| Interstellar : fausse note | oui | — |
| Dossier `videos/reseaux/` | oui | — |
| David Foxprod : une méthode | oui | — |
| Réponses aux hypothèses de goût | oui (dans `GOUTS.md`) | — |
| Contournement pour l'animation | oui | — |
| Notes sur la V2 | oui | — |
| Ton regard sur ta propre image | oui | — |
| Pas de version de Diego, Claude nu | oui | — |
| Comparaison agent / Claude nu | oui | — |
| L'ordre des plans | oui | — |
| Notes sur la V3 | oui | — |
| Gyroflow : mouvement fluide | oui | — |
| Jamais deux fois le même passage | oui | portée corrigée par Diego en V5 : [genre], pas [universel] (C1) |
| Notes sur la V4 | oui | — |
| Détourages : défaut technique | oui | — |
| Trois outils pour le goût | oui | — |
| Deux retours de plus, deux règles (flous) | oui | **la fin de la liste des flous ratés** (message coupé) |
| Fin de la V4 trop longue · Rien n'est figé · Référence dernier pic | oui | — |
| **Notes sur la V5** | **non** (section non commitée) | tout : plans, stabilisation (10 essais), couleur, effets (traînées [genre]), portée des règles, « [projet, à confirmer] » N&B en hauteur, DCTL « plus tard » |

### 4.2 Proposition

1. Créer `archives/retours/RETOURS-DIEGO-2026-10-11-sony-linkbuds.md` avec **le texte intégral** des 17 sections intégrées, dans l'ordre, sans une virgule changée (en-tête : « Archive ; le fichier vivant est `RETOURS-DIEGO.md` »).
2. Dans `RETOURS-DIEGO.md`, remplacer chaque section archivée par **une ligne d'index** : date, titre, où elle a été intégrée (skills, carnet, prompt), lien vers l'archive. Le fichier vivant garde en entier : la section V5 (à intégrer), et une section « Points ouverts » (fin de la liste des flous ratés ; N&B en hauteur [projet, à confirmer] ; DCTL ; la définition de « transition » validée ; les seuils à recalibrer).
3. Variante si Diego préfère **ne rien retirer du fichier vivant** : l'archive est une copie, `RETOURS-DIEGO.md` reste tel quel et gagne seulement la section « Points ouverts ». Coût : 49 Ko relus à chaque démarrage de session pour rien.
4. Dans les deux cas, l'historique Git garde tout. Même logique, plus tard, pour chaque projet : un fichier d'archive par projet.

### 4.3 Intégration des notes V5 (à faire à la prochaine session, après validation)
Avec la liste de portée de Diego comme loi : [universel] → `montage-regard` et carnet (sensibilité humaine : regard caméra, sourire, geste vers l'objectif ; intention ↔ image vérifiée ; un plan bon seulement à la fin se coupe là où il est bon ; 10 essais de stabilisation puis remplacement ; couleurs clés constantes ; chercher en permanence des références très esthétiques ; plan produit à 200 %) · [genre : kinetic] → `montage-kinetic-editing` (traînées de hautes lumières au moment où ça accélère, référence foebusdelapaz) · [projet] → `projets-phase-3/sony-linkbuds/` (coucou remplacé, plan qui suit, dernier packshot, peaux vertes, rouge, top shot). Puis marquer la section « intégrée », et commiter.

---

## 5. Ce qui n'a pas été fait, volontairement
- Aucun fichier modifié, aucun commit, Resolve fermé. La section V5 de `RETOURS-DIEGO.md` reste non commitée : c'est à toi de dire si je la commite à la prochaine session.
- `GOUTS.md` : lu, intact. Rien à y signaler.
- Je n'ai pas rédigé les nouvelles versions des skills (point 3.3) : une ligne par retouche suffit pour valider le principe ; le texte viendra après ton accord, retouche par retouche, pour que tu puisses en refuser une sans bloquer les autres.

## 6. Ce que j'attends de toi
1. Valider ou corriger les tags du point 2 (surtout 2.2 : reformulations).
2. Trancher les contradictions C2, C3, C4, C6, C9, C10 (les autres sont des corrections de fait).
3. Choisir entre 4.2-2 (index + archive) et 4.2-3 (copie seule).
4. Dire si `CLAUDE.md` et la partie essentielle de `PROMPT-PHASE-3` (3.1, 3.2) te conviennent tels quels, ou ce qui manque.
5. Pour le projet 2 : déposer deux ou trois interviews corporate de référence dans `videos/a-traiter/` avant la première session.
