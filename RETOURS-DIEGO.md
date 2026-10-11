# Retours de Diego

Une section datée par retour. Claude marque chaque retour « intégré le <date> » une fois pris en compte.

## 2026-10-11 — Interstellar : fausse note attribuée à Diego
L'exemple qui figurait dans videos/NOTES-DIEGO.md (« J'adore la scène de l'amarrage (vers 1h52) et le compte à rebours ») n'était pas de Diego : c'était un exemple de format écrit par l'assistant de configuration. Retire de analyses/films/interstellar.md, de RAPPORT.md et des skills tout ce qui l'attribue à Diego. Ton analyse de l'amarrage et du combat avec Mann reste valable, mais comme ton choix, pas comme le sien. Diego n'a encore commenté aucun film.
**Intégré le 2026-10-11** : attribution retirée de `analyses/films/interstellar.md`, `RAPPORT.md` (doute « 1 h 52 » supprimé) et `PROGRESS.md` ; les skills ne citaient que GOUTS.md (« l'accélération du montage alterné »), inchangés ; leçon ajoutée à `PROMPT-PHASE-2.md`.

## 2026-10-11 — Nouveau dossier `videos/reseaux/` : 7 vidéos de réseaux
Diego a ajouté le dossier `videos/reseaux/` (7 vidéos de 11 à 43 s, téléchargées sur les réseaux, nommées d'après le compte de l'auteur). Ses mots : des vidéos « que j'aimais beaucoup », avec « beaucoup de kinétique, mais pas que ». Ce sont donc des références de son goût, pas des contre-exemples.
C'est la lacune prioritaire notée en fin de phase 2 (kinetic de réseaux). Traite-les comme de nouvelles références avec le skill `montage-nouvelle-reference` : une fiche par vidéo dans `analyses/reseaux/`, en une passe sur la vidéo entière, avec les contrôles obligatoires (bandes de 6 images avant toute rafale, spectrogramme, musique séparée avant tout calage). Vérifie à l'œil ce qui relève du kinetic et ce qui n'en relève pas. Puis fais un bilan court dans RAPPORT.md : ce qui confirme, corrige ou remplace ce qui était [SOURCÉ] ou [THÉORIQUE] dans `montage-kinetic-editing` et `montage-formats` (calage, SFX, captions, hook des 3 s), et mets ces skills à jour.
Attention : certaines sont en basse définition (une en 360x640) ; ne juge pas la netteté ou le grain sur celles-là.
Ajoute aussi `reseaux` à l'inventaire de PROGRESS.md.
**Intégré le 2026-10-11** (session 12) : 7 fiches dans `analyses/reseaux/` (toutes les images vues, spectrogramme, musique séparée avant tout calage, écart signé), inscrites dans `REFERENCES.md` ; bilan dans `RAPPORT.md` (« Bilan des sept vidéos réseaux ») ; `montage-kinetic-editing` et `montage-formats` mis à jour, corrections de calage reportées dans `montage-rythme`, `montage-expert`, `montage-references` ; leçons de méthode dans `PROMPT-PHASE-2.md` ; `reseaux` ajouté à l'inventaire de `PROGRESS.md`. La vidéo en 360x640 (darius) n'a pas été jugée sur la netteté ni le grain. Les fichiers sont laissés dans `videos/reseaux/` sous leurs noms.

## 2026-10-11 — `videos/a-traiter/video-by-david-foxprod-isuwou.mp4` : une méthode d'étalonnage, pas un montage
Voir la note de Diego dans `videos/NOTES-DIEGO.md`. Pour cette vidéo, **pas de fiche de montage** (ni coupes, ni rythme, ni calage). Regarde-la comme un tutoriel :
1. Lis les images où l'on voit l'interface de Resolve (arbre de nœuds, roues, courbes, scopes, image de référence) et reconstitue la méthode : ordre des nœuds, rôle de chacun, outils utilisés, façon de comparer avec la référence (split screen, scopes, galerie…).
2. Écris ce que tu as **lu sur l'écran** [VU SUR IMAGES] séparément de ce que tu **déduis** [THÉORIQUE]. Le fichier est très compressé (12 s, 530 Ko) : si un réglage ou un nom de nœud est illisible, écris-le comme illisible, n'invente pas de valeur.
3. Confronte la méthode à ce que disent déjà `montage-couleur-pipeline`, `montage-resolve` et `montage-couleur-et-intention` (match de référence, look, ordre des nœuds). Ajoute-la au skill le plus pertinent comme **une méthode parmi d'autres pour reproduire un look**, simple et rapide, avec ses limites (dans quels cas elle ne suffit pas).
4. Fiche courte dans `analyses/methodes/` (créer le dossier), inscription dans REFERENCES.md, puis déplace la vidéo dans un sous-dossier `videos/methodes/` comme le prévoit le skill `montage-nouvelle-reference` pour les références traitées.
**Intégré le 2026-10-11** (session 13) : 299 images lues, arbre de nœuds lu sur agrandissement, apport de chaque nœud mesuré sur l'image ; fiche `analyses/methodes/david-foxprod-look-seven.md` (lu à l'écran [VU SUR IMAGES] séparé du déduit [THÉORIQUE], outils des nœuds et type des mélangeurs écrits comme illisibles), inscrite dans `REFERENCES.md` ; méthode ajoutée dans `montage-resolve` § 2 bis comme une méthode parmi d'autres, avec ses limites, et un renvoi dans `montage-couleur-et-intention` ; vidéo rangée dans `videos/methodes/david-foxprod-recreer-colo-seven.mp4`.


## 11/10/2026 — Réponses aux hypothèses de goût
1. Un mélange des deux. Mais là pas de sous titre. QUE DU VISUEL Pour la video sony
2. Oui
3. Oui
4. Oui
5. Oui, mais quand je n'ai pas d'idée ou que je dois livrer une video rapidement, je mets du film look.
Ces réponses sont ma parole : tu peux les recopier dans GOUTS.md.
_Questions correspondantes (ajoutées par l'assistant de configuration, d'après la synthèse de RAPPORT.md ; les réponses ci-dessus sont celles de Diego) :_
1. _Ton « kinetic » pour les réseaux, c'est un montage calé à l'image sur la musique, avec des transitions variées, un look pellicule, une typo serif fine, et qui respire ; pas le kinetic à whoosh et sous-titres mot à mot._
2. _Ce que tu aimes dans Interstellar et Joker ne vient pas de la vitesse mais de la structure (l'alternance qui accélère, la rupture). La vitesse, tu la réserves au kinetic._
3. _« L'équilibre de l'ensemble » de Joker, c'est une seule idée servie à la fois par le rythme, le cadre, la couleur et le son._
4. _Au-delà de trois lignes d'action en parallèle, l'alterné par blocs d'Avengers te convient aussi bien que l'accélération d'Interstellar._
5. _Le grain et le look film : à utiliser quand ils racontent quelque chose, pas comme un filtre posé partout._
**Intégré le 2026-10-11** (phase 3, session 1) : réponses recopiées dans `GOUTS.md` ; `montage-kinetic-editing` (le kinetic de Diego est un mélange des deux, sous-titres seulement à la demande) et `montage-couleur-et-intention` (look film = défaut quand il n'y a pas d'idée ou peu de temps).


## 2026-10-11 — Avant l'étape 1 du projet Sony : chercher un contournement pour l'animation
Le brief Sony est un kinetic : zooms et punch-ins animés, textes animés, rampes. Si rien ne s'anime, le test mesurera la limite de l'outil, pas ton montage. Avant le dérushage, prends 20 minutes dans `P3-BAC-A-SABLE` pour tester trois pistes, un geste puis une image de contrôle à chaque fois :
1. **Expressions Fusion au lieu de clés** : `SetExpression` sur une entrée (ex. `Size` d'un Transform calculé à partir de `time`). Une expression anime sans aucune clé.
2. **Fichier de réglages Fusion écrit par toi** : un `.setting` (texte, format Lua) qui contient déjà les clés d'une `BezierSpline` (zoom, texte qui entre), chargé dans la composition du plan, ou installé comme macro ou modèle d'effet (Fusion Titles / Effects) puis appliqué.
3. **Transitions et effets intégrés déjà animés** : `AddTransition` avec d'autres transitions que le fondu (zoom, glissement, flou), et les effets ou titres animés livrés avec Resolve.
En dernier recours seulement : un élément pré-calculé avec ffmpeg ou Python (punch-in rendu en fichier). Ça marche, mais l'effet n'est plus modifiable dans Resolve : note-le dans la note de livraison.
Note ce qui marche dans `labo/mcp/resolve-mcp.md` et `montage-resolve`, puis enchaîne sur l'étape 1.
Pour les détourages (Magic Mask) : dans `plan.md`, liste tous les plans à détourer avec leurs timecodes, pour que Diego trace tous les traits en une seule fois.
**Intégré le 2026-10-11** (phase 3, session 1) : pistes 1 et 3 réussies, piste 2 réussie sous une forme plus simple que le `.setting` (table de clés `BezierSpline.SetKeyFrames`, poignées d'easing comprises) ; contrôlées au rendu. Recettes dans `labo/mcp/journal-2026-10-11.md` (gestes 23-26), `labo/mcp/resolve-mcp.md` et `montage-resolve` § 4 ter. Plus besoin d'éléments pré-calculés. Les plans à détourer seront listés dans `plan.md`.

## 2026-10-11 — Projet Sony, notes de Diego sur la V2 (première salve de retours)
_Dictées par Diego, mises en forme et triées par l'assistant de configuration. Les phrases entre guillemets sont ses mots._

**Version de l'agent (V2) : livrable à — non chiffré.** Jugement global de Diego : « très moyen, voire vachement nul ». « J'ai vraiment l'impression que toute cette phase d'entraînement qu'on a eue pour lui apprendre le bon goût, ce qu'est un joli plan, il n'a quasiment rien retenu. »

### [gros] Étalonnage
- « Catastrophique » : on dirait une simple conversion S-Log3 → Rec.709, « rien d'un look professionnel ou cinématique ». L'image est lumineuse, plate, sans contraste : « c'est pas beau ».
- Attendu : un vrai look (contraste, noirs denses, couleurs choisies, même look sur tous les plans), au niveau de ses références réseaux (`analyses/reseaux/`).
- Piste : l'API ne règle que le nœud 1 et charge une LUT ou un DRX. Fabrique donc toi-même une LUT de look (base : `labo/couleur/look_lut.py`) ou un DRX, applique-la après la conversion S-Log3, et juge-la sur des images avant / après, à côté des références.

### [gros] Rythme
- « On se fait un peu chier », « c'est encore trop mou ». Tu as compris en phase 2 la notion d'accélérer et de ralentir, mais tu ne l'as pas appliquée avec assez d'écart.
- Ce qui marche : **le passage très rapide avec les flashs vers 15 s** (« c'est cool »). Ce genre de rafale doit **revenir plus souvent**, sans devenir toute la vidéo.
- Durée : tu peux descendre à **45 s**, voire **30 s** si tu le juges nécessaire.

### [gros] Texte de fin « LinkBuds Clip »
- « On dirait un enfant de 6 ans qui a fait un PowerPoint », dans le dessin du texte comme dans sa façon d'apparaître. « Il voit bien, dans les références que je lui ai mises, comment les textes sont faits. »
- Attendu : une typographie et une animation de niveau professionnel, à la manière de tes références réseaux, ou pas de texte du tout.

### [gros] Transitions « PowerPoint »
- La transition qui glisse vers la gauche, et celle entre le plan rouge et le premier packshot : « on ne peut pas faire des trucs comme ça ».
- Règle à retenir : **jamais de transitions intégrées de type glissement, poussée ou volet**. À la place : coupe franche, flash, whip avec flou de mouvement, raccord de mouvement, zoom qui traverse.

### [moyen] Packshots de fin qui tremblent
- Bien choisis, mais ils tremblent : « esthétiquement, c'est cata ». Ce n'est pas ta faute au tournage, mais tu devais le voir et le traiter sans attendre Diego.
- Piste : Diego stabilise avec **Gyroflow**, installé sur son Mac. Vérifie si tu peux l'utiliser en ligne de commande avec les données gyroscopiques de la caméra (Sony ZV-E1), rendu dans `_travail/`, sans toucher aux originaux. Sinon, la stabilisation de Resolve. Sinon, un autre plan.

### Leçon de méthode (de l'assistant de configuration, à partir de ces retours)
Ton autocritique a contrôlé les chiffres (loudness, crêtes, photosensibilité, plans sombres), pas la beauté. Avant toute livraison, mets **côte à côte six images de ta version et six images de tes références** (ouverture, produit, sommet, texte, transition, fin) et juge l'écart en monteur : look, contraste, typographie, transitions, énergie. Inscris cette règle dans `montage-regard` et dans les leçons de phase 3.

### Ce que tu fais de ces notes
1. Dès ta prochaine session, tire les leçons générales dans les skills (étalonnage, transitions, typographie, rythme, autocritique par comparaison d'images) et dans « Leçons de phase 3 » de `PROMPT-PHASE-3.md`.
2. Ne retouche pas le montage tant que Diego ne t'a pas lancé sur la suite : il fait d'abord monter le même projet à un Claude sans formation (test comparatif).
3. Ensuite viendra la V3, qui applique ces retours, dans une boucle de corrections où l'on comptera les allers-retours nécessaires pour livrer.
**Intégré le 2026-10-11** (phase 3, session 2) : leçons dans `montage-regard` (« Juger sa propre version »), `montage-couleur-et-intention`, `montage-kinetic-editing` (transitions interdites, rafales), `montage-motion-design-principes` (19, titre) et « Leçons de phase 3 » ; appliqué dans la V3 (look fabriqué et comparé, aucune transition intégrée, nouveau titre, 4 rafales, 44,6 s, packshots mesurés et stabilisés).

## 2026-10-11 — Ton regard sur ta propre image (suite des notes sur la V2)
Diego ajoute : « se comparer, ça ne veut pas dire se calquer ». Il ne veut pas valider ton look à mi-parcours : tu as assez de références pour savoir ce qu'est une belle image, à toi de te corriger seul, dans le style voulu par le brief. Il veut aussi que tu **voies le mouvement** (les packshots tremblants), et que tu utilises **Gyroflow**, installé sur son Mac.
Les règles sont dans la nouvelle section « Ton regard sur ta propre image » de `PROMPT-PHASE-3.md` (look comparé aux références avant le montage et avant la livraison, mesure du tremblement avec un outil à construire, Gyroflow en ligne de commande). Applique-les dès la V3.
- Précisions de Diego (même jour) : **ne copie pas les rushes** pour Gyroflow (le disque de travail n'aura pas toujours la place) : demande-lui l'accord d'écrire les fichiers stabilisés directement dans le dossier source. Et **garde Resolve léger** : le look décidé tôt ne doit pas alourdir tout le montage (section « Garder Resolve léger » de `PROMPT-PHASE-3.md`).
**Intégré le 2026-10-11** (session 2) : `labo/outils/tremblement.py` construit et calibré (plan fixe < 1,5 px ; packshots V2 4,3-4,7 px ; seuil 2 px / 5 px de pic) ; look sur 6 images avant le montage (`projets-phase-3/sony-linkbuds/look.md`) ; Gyroflow : accord donné, bloqué par le bac à sable de macOS (accès au dossier à donner par Diego, marche à suivre fournie) ; repli : stabilisation par trajectoire mesurée. Look en un seul nœud, effets sur pistes à part (flashs V3, titre V4, grain V5).

## 2026-10-11 — Projet Sony : pas de version de Diego, comparaison avec Claude nu seulement
Le brief Sony est **fictif** : les rushes sont réels, mais Diego avait livré à Sony une vidéo faite sur un autre brief. Il n'y aura donc **pas de dossier `final-diego/`** pour ce projet. L'étape 6 de `PROMPT-PHASE-3.md` se fait ainsi :
- tu compares ta V2 et la V1 de Claude nu (`videos/phase-3/sony-linkbuds/rendus-nu/P3_sony_linkbuds_clip_9x16_v1.mp4`, faite sans skills, sans mémoire, sur le même brief) ;
- les notes de Diego sur les deux versions (dans ce fichier) servent de juge ;
- `comparaison.md` dit ce que Claude nu a fait mieux que toi et pourquoi tu ne l'as pas fait (par exemple, il a réussi 3 détourages automatiques, que tu croyais impossibles par script), ce que tu as fait mieux que lui, et ce que ta formation a réellement apporté ;
- puis tu enchaînes sur la V3, qui applique les retours de Diego et les règles de « Ton regard sur ta propre image ».
**Intégré le 2026-10-11** (session 2) : `projets-phase-3/sony-linkbuds/comparaison.md` ; V3 rendue (`rendus/sony_linkbuds_V3.mp4`).

## 2026-10-11 — Projet Sony : comparaison de Diego, agent (V2) contre Claude nu (V1)
_Dictée par Diego, mise en forme par l'assistant de configuration ; les phrases entre guillemets sont ses mots._
- **À livrer, Diego prendrait plutôt la tienne** : « plus globalement plus propre ».
- **Mais celle de Claude nu est plus impressionnante** : il a mieux compris la volonté d'être dynamique, kinetic, « quasiment épileptique ».
- **Ses choix d'effets sont mieux posés** : « en toute honnêteté, ses choix d'effets sont mieux posés, ce qui est frustrant au vu de l'entraînement qu'a subi l'autre ».
- **Détourage** : Claude nu a trouvé un contournement au Magic Mask, « audacieux », qui « mérite d'être repeaufiné parce que les masques sont un peu bizarres », mais qui « dans le rythme, rend bien ». Tu l'avais déclaré impossible par script. Le test à l'aveugle est fini : tu peux maintenant lire ses notes et ses scripts (`/Volumes/SSD FAST/Test-Claude-nu/NOTES.md` et `work/`, en lecture seule) pour comprendre comment il a fait, puis reprendre l'idée en mieux.
- Ce que ça veut dire pour toi : ta formation t'a rendu propre et prudent ; sur un brief qui demande l'excès, tu es resté trop sage. Le brief prime sur tes habitudes : quand il dit « très rapide, beaucoup d'effets », ose autant qu'un monteur kinetic, puis rends-le propre.
- **Étalonnage** : celui de Claude nu est meilleur que le tien, « même si c'est pas pro ». Aucun des deux n'a un look professionnel.
- **Packshots de fin** : ils tremblent aussi chez Claude nu. Personne ne l'a vu : c'est bien un angle mort du « regard sur images fixes ».
- **Titre et transitions** : aussi amateurs chez lui que chez toi.
- **Note de Diego : ta V2 livrable à 50 %, la V1 de Claude nu à 40 %.** C'est le point de départ chiffré : la V3 doit faire monter ce chiffre.
- **[gros, pour les deux versions] L'intention du cadreur n'a pas été lue.** Dans le hall, le cadreur a filmé une série : un plan sur le K du logo KORE, puis le O, puis le R, puis le E, puis le logo en entier. C'est fait pour un raccord (match cut) qui épelle K-O-R-E avant d'afficher le mot entier. Claude nu ouvre sur le K puis passe directement au corps ; ton dérush avait vu « des lettres qui défilent » mais conseillait d'en garder un ou deux plans. « Un monteur humain aurait direct compris quelle était la volonté du cadreur. »
- **Leçon générale (à inscrire dans `montage-regard` et dans les leçons de phase 3)** : au dérushage, cherche les **séries pensées pour être montées ensemble** : plans consécutifs au même cadre ou à la même valeur, éléments d'un même objet filmés un par un (lettres, détails d'un produit), mouvements qui se répondent d'un plan à l'autre (raccord de mouvement), même geste répété sous plusieurs angles. Pour chacune, écris dans `derush.md` l'intention probable du cadreur et le montage qu'elle appelle. Dans la V3, utilise la série KORE si elle sert le film.
**Intégré le 2026-10-11** (session 2) : comparaison écrite ; scripts et notes de Claude nu lus ; détourage par carte de profondeur repris et corrigé (`montage-resolve` § 4 quinquies) ; leçons « séries du cadreur » et « le brief prime » dans `montage-regard` et `PROMPT-PHASE-3` ; série K-O-R-E en ouverture de la V3 et section « Séries » dans `derush.md`.

## 2026-10-11 — Projet Sony : l'ordre des plans (retour oublié, dicté en session)
_Dicté par Diego dans la conversation, mis en forme par l'agent._
- Sur l'ordre des plans, les deux versions ratent, **en sens opposés** : Claude nu est **trop chronologique** (il suit l'ordre de tournage des rushes) ; ta V2 est **trop désorganisée** (les plans semblent posés sans logique).
- Attendu : un juste milieu. Une **progression cohérente** (on comprend où on est et ce qui se passe, chaque bloc a sa raison d'être là), sans être prisonnier de l'heure de tournage, et **sans jamais placer un plan au hasard**.
- Pour chaque bloc de la V3, écris dans `plan.md` **pourquoi ces plans sont là et dans cet ordre**.
**Intégré le 2026-10-11** (session 2) : règle dans `montage-regard` (point 6) ; `plan.md` V3 : 9 blocs, chacun avec « pourquoi ces plans, dans cet ordre » (le chemin d'une participante, le corps de bas en haut, les rafales comme matière).

## 2026-10-11 — Projet Sony, notes de Diego sur la V3
_Dictées par Diego, mises en forme par l'assistant de configuration ; les phrases entre guillemets sont ses mots._

**V3 livrable à 65 %** (V2 : 50 %). « C'est beaucoup mieux, le rythme est mieux, c'est mieux compris. » Mais « pas parfait ».

### Principes rappelés par Diego (valables pour tous les projets)
- **Le brief prime** : « un brief, c'est un brief ; mes préférences, c'est mes préférences ». Ses goûts (`GOUTS.md`) servent quand le brief ne dit rien.
- **Compare l'image, libère-toi du chiffre** : les mesures servent à vérifier, le jugement se fait en regardant ton image à côté d'images pro.
- **Le temps ne compte pas** : « je préfère que ça mette plus de temps et que le rendu soit propre ». En phase 3, plus de limite de 50 minutes par session.
- **Jamais cheap** : « on ne fait pas les choses de manière cheap ». Un effet se fait seulement si la matière le permet et s'il peut être exécuté proprement : « si c'est possible, on met ; s'il y a la matière, on met ; sinon, on fait pas ». Toujours se comparer visuellement à quelque chose de propre et de pro.

### [gros] Texte de fin : police et animation, toujours pas ça
- Référence : la direction artistique statique de Sony pour le produit, `projets-phase-3/sony-linkbuds/references/da-linkbuds-clip-reference.png`. « LinkBuds » en gras et « Clip » en maigre, accolés, noir sur fond clair, beaucoup d'air, le produit beige seul. Reprends ce dessin (graisses SST correspondantes) plutôt que d'inventer un titre.
- Animation : « quelque chose d'assez simple et épuré, à la Apple », même si le reste de la vidéo est très dynamique. Pas d'effet, pas de « fou » : une apparition courte et douce (par exemple, une montée de quelques pixels avec un fondu, freinée en arrivant), parfaitement propre.

### [moyen] Effets et transitions : plus nombreux, mais répétitifs et sans folie
- « Il y en a beaucoup plus, ça marche bien. Maintenant, ils sont un peu répétitifs et ils manquent de folie. »
- Source d'idées : **https://eyecannndy.com/**, une bibliothèque de techniques de tournage et de montage, chacune illustrée par des GIF. Parcours-la dans Chrome, garde les techniques de montage (zoom infini, crash zoom, flash cut, match cut, speed ramp, step-print, stutter, split screen, double exposition, collage, masques, datamosh, slit-scan, arrêt sur image, typographie…), regarde les exemples, et note dans `montage-kinetic-editing` celles que tu sais exécuter proprement dans Resolve.
- **Zoom infini** : Diego le trouve pertinent « s'il est bien exécuté ». Pas le zoom cheap « à la CapCut », avec un simple flou qui laisse apparaître l'image d'après. Il faut la matière : un plan dont un détail devient exactement le plan suivant (alignement, échelle, mouvement continu). Si les rushes ne le permettent pas, on ne le fait pas.
- Varie les techniques d'une rafale à l'autre ; chacune doit avoir une raison dans la matière.

### Réponses de Diego aux questions complémentaires
- **Son** : musique sans problème. **SFX un peu répétitifs** : varie-les (familles, textures, hauteurs), comme les effets visuels.
- **[gros] Couleur** : « il y a du mieux », mais « toujours pas assez pro ».
    - « Une bouillie de pixels », « encore trop pâté de couleurs » : les teintes **ne sont pas assez séparées** (peaux, décor, néons, produit se fondent). Travaille la séparation des couleurs (courbes teinte contre teinte et teinte contre saturation, peaux isolées du décor, contraste de couleur entre sujet et fond), pas seulement le contraste global.
    - **Plans d'écouteurs un peu surexposés** : « je ne sais pas comment il a mesuré ça ». Le produit est blanc ou beige : vérifie ses hautes lumières sur l'oscilloscope (waveform) et en fausses couleurs, sur une image pleine résolution, et garde du détail dans le boîtier (pas de blanc brûlé). Explique dans ta note comment tu as mesuré l'exposition.
    - Une partie de la « bouillie » vient aussi de l'encodage (voir le point suivant).
- **[gros] Réglages d'export du rendu final** (Diego) : débit nettement plus élevé, encodage **H.265 Main 10** sur le GPU (VideoToolbox), **multipass activé**, **« Bypass re-encode when possible » désactivé**, et dans les réglages avancés tout en qualité maximale (« Force sizing to highest quality », « Force debayer to highest quality », rendu en qualité maximale). Ça ne doit pas prendre des heures, mais la qualité passe avant la vitesse. Vérifie ensuite avec ffprobe (profil, bits, débit) et compare une image du rendu à l'image de la timeline : aucun bloc, aucun aplat cassé. Note ces réglages dans `montage-loudness-livraison` comme réglages par défaut du studio.
- **[moyen] Détourages** : « encore un peu bizarres ». Recommence tant que ce n'est pas propre. Et plutôt qu'un fond de couleur, inspire-toi de tes références : des **collages avec arrêt sur image puis reprise du mouvement**, comme dans les vidéos réseaux de Diego (`analyses/reseaux/`, notamment le collage de captured-by-h). Ce n'est pas une règle immuable, mais ici ça s'y prête mieux.
- **[moyen] Ouverture K-O-R-E** : « c'est l'idée », mais revois le cadrage et la stabilisation pour que le raccord fonctionne (chaque lettre au même endroit, sans flottement).
- **[gros] Packshots** : on voit la stabilisation numérique (recadrage, déformation). **« L'utilisation de Gyroflow est indispensable. »** Diego règle l'accès de macOS ; dès qu'il te le confirme, stabilise les packshots et les plans K-O-R-E avec Gyroflow (règle de sécurité 2 : fichiers `_stabilized` à côté des originaux, avec son accord).

### Suite
V4 : applique ces notes. Avant de livrer, compare en pleine résolution ton titre à la référence Sony, et tes effets aux exemples d'eyecannndy.
