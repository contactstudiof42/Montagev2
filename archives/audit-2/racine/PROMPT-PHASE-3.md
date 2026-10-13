# MISSION — PHASE 3 : MONTER DE VRAIS PROJETS DANS RESOLVE (sessions lancées par Diego)

_Réécrit le 2026-10-12 (audit du règlement, `AUDIT.md`, validé par Diego). Version précédente : `archives/phase-3/PROMPT-PHASE-3-avant-audit.md` (tag Git `avant-audit`). Les règles de métier sont dans les skills, le goût dans `CARNET-DE-GOUT.md`, les recettes dans `montage-resolve` : ce fichier ne contient que la mission, l'ordre de travail et les règles de sécurité._

## Le but et la mesure
À partir de rushes, son et brief, livrer dans Resolve (par le MCP) une version presque finie, que Diego n'aurait plus qu'à peaufiner. Mesure : la part « livrable » que Diego donne à chaque version, et le nombre de retours nécessaires. Projet 1 (Sony LinkBuds, after movie kinetic, 2026-10-11) : V2 50 % → V5 80-85 %. Ce que je ne sais pas faire reste écrit : je n'entends pas le son, je juge sur mesures et images extraites ; tout jugement sonore est mesuré, et la note de livraison dit ce que Diego doit vérifier à l'oreille.

## Règles de sécurité (priment sur tout)
1. **Resolve** : projets `P3-<projet>-agent` seulement ; aucun autre projet ouvert, modifié ou supprimé ; `SaveProject` avant tout geste risqué et avant de finir.
2. **Médias en lecture seule** (dépôt ou dossier source externe indiqué par `brief.md`) : rien n'est déplacé, renommé, réencodé, écrasé. Travail dans `videos/phase-3/<projet>/_travail/`, rendus dans `rendus/`. Seule écriture dans un dossier source : les fichiers `_stabilized` de Gyroflow, **nouveaux** (jamais `-f` sur un nom existant), après accord de Diego dans la conversation (une fois par projet).
3. **Test à l'aveugle** : jamais chercher la version de Diego avant qu'il la dépose dans `final-diego/`. Si le projet a déjà été analysé en phase 2, le dire dès le début.
4. **`run_script_unsafe`** seulement si aucun outil dédié ne le permet, jamais pour supprimer ni toucher hors de `P3-*` ; chaque usage au journal.
5. **Sons et musiques** : Artlist (ou une banque indiquée par Diego) avec son compte dans Chrome (extension Claude in Chrome) ; rien d'acheté, aucun abonnement modifié, 100 téléchargements par jour au plus ; chaque son dans `videos/phase-3/<projet>/sfx/` et noté dans `sfx.md` (nom, banque, lien, usage). Choisi sur le nom, les mots-clés et la forme d'onde ; ceux que Diego doit écouter sont signalés dans la note de livraison.
6. En cas de doute qui peut abîmer quelque chose (projet Resolve, fichier, rendu) : demander. Pour le reste : décider et noter.

## L'ordre de travail (fichiers texte dans `projets-phase-3/<projet>/`, commités ; jamais les médias)
0. **Le genre d'abord** : en tête de `plan.md`, le genre du film (after movie, pub, interview, corporate, clip, fiction…), son ton et sa destination. Il décide quelles règles [genre] s'appliquent et lesquelles ne s'appliquent pas. Puis relire : `brief.md`, `GOUTS.md`, les règles [universel] de `montage-regard` et du carnet, les skills du genre. **Si le corpus n'a aucune référence de ce genre, le dire à Diego avant de monter.** Si un élément du brief manque (durée, format, destination), choisir et noter.
1. **Dérusher** → `derush.md` : inventaire (`ffprobe` ; rotation, gamma et cadence lus avant tout proxy), copies légères, transcription de toute parole, planches ; pour chaque rush, ce qu'il contient, les bons moments avec timecodes, les prises écartées et pourquoi ; les séries du cadreur et le montage qu'elles appellent. C'est l'étape la plus importante : prendre le temps.
2. **Plan** → `plan.md` : intention en une phrase, durée et format, structure par blocs minutés avec, pour chaque bloc, « pourquoi ces plans, dans cet ordre » ; musique et calage ; références du corpus qui guident ; critères mesurables de réussite. En mode test, pas de validation attendue ; sur un vrai projet, Diego validera ce plan avant le montage.
3. **Direction artistique** → `da.md`, avant le moindre effet : ce qui se fait de mieux dans le domaine du film (8 à 12 images de référence pro, légères, dans `da/`, source notée), palette (avec les couleurs du client), matières, typographie, langage graphique, ce qui est exclu. Une page. Méthode : `montage-direction-artistique`, « La DA avant les effets ».
4. **Look et mouvement** → `look.md` : le look réglé sur 6 images aux moments clés du genre, posées en pleine résolution à côté de 6 images de références du même genre ; tremblement mesuré sur chaque plan retenu (`montage-regard`, « Voir le mouvement »). Gyroflow seulement si les rushes portent des données gyroscopiques et tremblent (`montage-resolve`).
5. **Monter** dans Resolve : timeline au format du brief ; un geste, une image de contrôle ; journal de chaque appel (`journal.md`). Resolve léger : look posé à la finition, effets sur des pistes à part, contrôle par rendu de plage (`montage-resolve`, « Garder Resolve léger »). Son : niveaux, fondus, ambiance continue sous la parole. Textes et sous-titres si le format l'exige (lisibilité sur téléphone).
6. **Juger et corriger** : V1 rendue dans `rendus/`, mesurée (`qc_livraison.sh`, contrôles de `montage-regard`), relue contre le carnet (entrées [universel] et du genre) ; `autocritique.md` par ordre de gravité ; des variantes réellement différentes sur les moments clés du genre, comparées en pleine résolution ; relire le film entier après chaque série de corrections. Deux ou trois versions au plus, puis `note-de-livraison.md` : ce que j'ai fait, mes choix, ce que Diego doit vérifier (surtout à l'oreille), ce que je n'ai pas su faire dans Resolve, tout plan remplacé hors de ses retours (quel plan, pourquoi, par quoi).
6 bis. **Le directeur artistique** (sous-agent `directeur-artistique`, écrit par le consultant de Diego ; je ne le modifie pas). Toujours un appel neuf, sans mon raisonnement (ni journal, ni contrôles, ni autocritique) :

| Moment | Ce qu'il reçoit | Sa question |
|---|---|---|
| Après `plan.md` | brief, goûts, références, plan | L'idée du film est-elle forte ? Qu'est-ce qui est banal ? |
| Après le look de base | 6 images du film contre 6 de références | Est-ce au niveau ? Blancs, noirs, densité ? |
| Après chaque moment clé | planche côte à côte : référence et rendu | Est-ce au niveau de la référence ? Qu'est-ce qui fait cheap ? |
| Avant chaque livraison | brief, références, le film entier en planches | Qu'est-ce qu'un client exigeant reprocherait ? |

   Je réponds à **chacune** de ses remarques dans `projets-phase-3/<projet>/da-retours.md` : « corrigé » (et comment) ou « je garde, parce que… ». Les désaccords vont dans la note de livraison ; Diego tranche.
7. **Comparaison** (si Diego dépose sa version dans `final-diego/` et / ou une version d'un Claude sans formation dans `rendus-nu/`) → `comparaison.md` : ce que l'autre version a fait de mieux et pourquoi, l'apport réel de ma formation, ce qui se mesure ; leçons reversées dans les skills avec leur portée et dans l'annexe A4 ; bilan court dans `RAPPORT.md`. Un principe confirmé par la version de Diego passe en [TESTÉ EN CONDITIONS RÉELLES].

## Les réflexes avant chaque rendu (détail et outils : `montage-regard`)
Passage exact de chaque plan vu en pleine résolution (première, milieu, dernière image) · aucun plan de remplissage · la valeur humaine d'un plan (regard caméra, sourire, geste vers l'objectif) se repère et se garde · visages image par image · chaque plan montre ce que `plan.md` dit qu'il montre · tremblement mesuré, plan remplacé après 10 essais · exposition et couleurs clés constantes d'un plan à l'autre, aucun blanc brûlé · aucun élément graphique hors de `da.md` · un détourage ou un plan produit vérifié à 200 % · aucune transition intégrée · doublons de rush (genres concernés) · photosensibilité sur les effets ajoutés (flashs réels des rushes : seulement en salve de plus de 3 par seconde) · parole coupée au mot près par alignement forcé, et re-transcription du rendu lue en phrases complètes · 6 images contre 6 références · loudness et crête sur le fichier encodé.

## Chaque session
Démarrage de `CLAUDE.md` ; reprendre où `PROGRESS.md` s'est arrêté ; pas de limite de temps (Diego : « je préfère que ça mette plus de temps et que le rendu soit propre ») ; s'arrêter à une étape propre, projet Resolve enregistré, journal à jour ; commit et push à chaque étape terminée (fichiers texte seulement, `git status` avant) ; fin : `PROGRESS.md` (où reprendre) et synthèse de `RAPPORT.md` réécrits, commit, push.

---

# Annexes

## A1 — Session 0 : apprendre l'outil (faite le 2026-10-11)
_Terminée. Résultats dans `labo/mcp/resolve-mcp.md`, `labo/mcp/journal-2026-10-11.md`, `PLAN-TESTS-MCP.md` et `montage-resolve` § 4 ter. À refaire seulement si Resolve ou son serveur MCP change de version. Texte d'origine :_
1. Diagnostic : `get_resolve_status`, version, `get_whats_new` depuis ta date de connaissance, `get_scripting_docs` / `get_scripting_api` / `search_scripting_api`. Résume dans `labo/mcp/resolve-mcp.md` ce que le serveur sait faire et ce qu'il ne sait pas.
2. Bac à sable : projet `P3-BAC-A-SABLE`, avec 3 ou 4 courts extraits de `videos/clips/` copiés dans `videos/_travail/p3-bac-a-sable/` (jamais l'original). Teste, **un geste puis une image de contrôle** à chaque fois : importer des médias · créer une timeline (résolution, cadence) · poser des plans avec points d'entrée et de sortie à l'image près · couper, raccourcir, déplacer · poser une musique et régler un niveau · un fondu son · un texte · un nœud d'étalonnage simple et une LUT · rendre un H.264 · relire le rendu (ffprobe, `qc_livraison.sh`, planche). Puis les gestes qu'exige le premier projet (Sony, kinetic vertical) : timeline 1080x1920 à 25 i/s à partir de rushes UHD 16:9 à 50 i/s (recadrage et position par plan) · synchroniser un son externe avec le son caméra · un flash blanc d'une ou deux images · un changement de vitesse (ralenti, rampe) · un détourage (Magic Mask ou masque de Fusion) · un texte dans une police installée sur le Mac · un SFX posé à l'image près · un plan de fin fourni (ProRes avec alpha) en surimpression. Enfin, le navigateur : recherche d'un SFX sur Artlist, téléchargement d'un seul son, déplacement du fichier vers le dossier `sfx/` du bac à sable. Pour chacun : faisable par le MCP, faisable seulement à la main, ou impossible.
3. Pour chaque geste : réussi, échoué ou contourné, avec l'appel exact. Résultats dans `PLAN-TESTS-MCP.md` et dans les skills `montage-resolve` et `montage-pilotage-mcp`, marqués [TESTÉ EN CONDITIONS RÉELLES] (date).
4. Fin de session 0 : la liste « ce que je peux faire seul / ce que je ne peux pas faire / ce que Diego devra faire à la main ». Commit, push.

## A2 — Recettes et méthodes : où elles sont
Une règle, un fichier maître ; ce prompt ne les répète pas.
- Se comparer aux références (6 images, pleine résolution, avant le montage et avant chaque livraison ; se comparer n'est pas copier) → `montage-regard`, « Juger sa propre version », point 1.
- Le brief fixe l'énergie, les références fixent la finition → `montage-regard`, point 2 ; `CLAUDE.md`, principes de Diego.
- Voir le mouvement : mesure du tremblement (`labo/outils/tremblement.py`, seuils), intention du cadreur (fixe ou rail), stabiliser sans figer, 10 essais puis remplacer → `montage-regard`, point 3.
- Gyroflow : version GitHub (pas App Store), synchronisation automatique sur une plage courte, zoom fixe, mesure avant / après, rail → `montage-resolve`, § 4 quinquies.
- Garder Resolve léger : proxies, look décidé tôt et appliqué tard, effets sur des pistes à part, rendu de plage pour contrôler → `montage-resolve`, « Garder Resolve léger pendant le montage ».
- La direction artistique avant les effets (`da.md`, 8 à 12 images, ce qui est exclu) → `montage-direction-artistique`, « La DA avant les effets ».
- Des variantes sur les moments clés ; le carnet de goût (quoi, quand le relire) → `montage-regard`, points 11 et 12 ; en-tête de `CARNET-DE-GOUT.md`.
- La portée d'une règle ([universel] / [genre] / [projet]) et les marqueurs → `CLAUDE.md`, « Conventions ».
- Bibliothèque de techniques eyecannndy.com [genre : kinetic, dynamique] → `montage-kinetic-editing`, § 4 bis.
- Réglages d'export par défaut du studio (la spec du client prime) → `montage-loudness-livraison`, « Master du studio depuis Resolve ».
- Détourage : contrôle au bord à 200 %, choix de l'outil → `montage-regard`, « Le goût de chaque plan » ; recette → `montage-resolve`.

## A3 — Ce que le projet Sony a établi (état au 2026-10-12)
- **Par script, je sais** : poser des plans à l'image près, animer par clés Fusion (poignées relatives, jamais `comp.Lock()`), expressions, LUT fabriquées (`LUT/P3/`), CDL par plan, SFX calés à la crête mesurée, rendu de plage pour contrôler, détourage par modèle local (BiRefNet) ou carte de profondeur, Gyroflow en ligne de commande puis rail.
- **Hors API** : Magic Mask (ne fait que suivre des traits tracés à la main), les cases « Force sizing / debayer » et « Bypass re-encode » du rendu (préréglage enregistré à la main), déplacer un plan ou un son (on supprime et on repose), courbe de vitesse (paliers).
- **Accords de Diego encore valables** : mes LUT dans `LUT/P3/` seulement ; Artlist via Chrome ; fichiers `_stabilized*` à côté des originaux dans `SONY copy/RUSH/`.
- **Accords ponctuels, à redemander** : forcer Resolve à quitter quand il est figé.
- **Pièges** : `montage-resolve` et `PROGRESS.md` (liste courte).
- **Dossiers** : `projets-phase-3/sony-linkbuds/` (plan, derush, da, look, autocritique, note de livraison, journal, sfx, comparaison) ; versions antérieures dans `archives/phase-3/sony-linkbuds/`.

## A4 — Leçons de phase 3, avec leur portée (à enrichir à chaque projet)
**[universel]**
- Lire rotation, gamma et cadence des rushes avant tout proxy (Sony : 252 rushes verticaux en S-Log3, vingt minutes de proxies perdues).
- Dérusher en planches par rush ; le dérush trouve ce que le brief ne dit pas (un changement de lumière qui porte le sommet, un son qui dispense de sous-titre).
- Chercher les séries du cadreur (plans consécutifs au même cadre, éléments d'un objet filmés un par un, mouvements qui se répondent) ; en écrire l'intention probable.
- Rendre une V0 tôt et la mesurer (loudness, luminance par plan) : le premier rendu de 16 s a révélé une saturation qu'aucune relecture de timeline n'aurait montrée.
- L'ordre des plans a une raison écrite par bloc : ni chronologique, ni au hasard.
- Un geste bloqué n'est pas un résultat impossible : chercher l'autre porte (Magic Mask refusé ≠ pas de détourage).
- Comparer 6 images de ma version à 6 images de références, en pleine résolution, avant le montage et avant chaque livraison ; mes contrôles chiffrés ne voient pas la beauté.
- La direction artistique avant les effets : `da.md` a supprimé les fautes de goût graphiques.
- Des variantes réellement différentes se jugent mieux qu'une idée réussie du premier coup.
- Mesurer le résultat, pas la méthode : un rendu Gyroflow « prouvé » peut trembler plus que le rush.
- Contrôler chaque animation par un rendu de plage ; ne jamais lire les réglages d'un effet IA par script (Resolve figé).
- La couleur se mesure en teinte (OkLCh sur des points témoins) et la couleur des noirs se vérifie amplifiée.
- Le titre reprend la DA du client, animé sobrement ; un titre de niveau pro ou pas de titre.
- Jamais de transition intégrée de type glissement, poussée ou volet.
- Le son se cale à l'image : attaque ou crête mesurée de chaque fichier, pas le début du clip.
- Vérifier que chaque plan montre ce que `plan.md` dit qu'il montre (intention ↔ image) ; ne jamais remplacer un plan non critiqué sans l'écrire.

**[genre : film sur musique, kinetic, after movie]**
- La musique décide de la structure (un extrait continu de 60 s existait dans le morceau, avec un silence avant le drop).
- Sur un brief qui demande l'excès, oser comme un monteur kinetic, puis rendre propre : ma formation m'avait rendu trop sage.
- La folie vient de techniques différentes tirées de la matière, pas d'effets ajoutés ; ce que la matière ne permet pas, on ne le fait pas.
- Un dernier pic construit sur les attaques mesurées de la musique, réglé en photosensibilité à l'image près (un noir et blanc qui assombrit une image claire est un flash).
- Un son par transition (effet ou changement de bloc), calé sur l'attaque ou la crête du fichier.
- Stabiliser selon l'intention du cadreur (fixe ou rail) ; Gyroflow d'abord quand les rushes ont des données gyroscopiques, toujours synchronisé, sur une plage courte.

**[projet : mariage-jo]** (2026-10-12 ; portées proposées entre crochets, à classer par Diego)
- Un film de 5 min tient par une idée qui revient (« dans dix ans »), deux rappels comiques tirés de la matière (le panini, l'orage annoncé par l'officiant) et un seul changement de look qui a un sens (le oui rallume la couleur) [proposé : genre mariage].
- Dérusher le son autant que l'image : transcrire tout l'enregistreur et le son de chaque rush concaténé par caméra a trouvé les « petits mots », le maillot, le rappel du panini par Sylvain [proposé : universel, films avec parole].
- Caler les horloges par corrélation audio avant tout ; synchro fine plan par plan sur le HF [technique, déjà dans `montage-workflows`].
- Les flashs des photographes et des téléphones sont dans les rushes d'événement : chercher les salves (bandes horizontales, volet roulant) avant de choisir un moment de bal, de gâteau, de cadeau [proposé : genre événement].
- Construire le montage comme un programme (`edl.py` → JSON → Resolve) : chaque plan porte sa raison, chaque triche est listée d'office, la reconstruction d'une version prend quelques minutes [méthode].

**[projet : Sony LinkBuds]**
- Le zoom infini E → KORE, le flash cut des sept oreilles, la rafale « glisse » abandonnée (les pieds ne glissaient pas), le passage au rouge comme sommet, le plan de la dame qui fait coucou : des exemples, pas des règles. Détail : `projets-phase-3/sony-linkbuds/`.
