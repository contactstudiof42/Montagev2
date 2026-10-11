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
