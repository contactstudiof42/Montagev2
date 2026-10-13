# MISSION — PHASE 3 : PROJETS ET EXERCICES DANS LES LOGICIELS (sessions lancées par Diego)

_Réécrit le 2026-10-13 (audit 2, `AUDIT-2.md`, validé par Diego). Versions précédentes : `archives/audit-2/racine/PROMPT-PHASE-3.md` (tag `avant-audit-2`) et `archives/phase-3/PROMPT-PHASE-3-avant-audit.md`. Les règles de métier sont dans les skills, le goût dans `GOUTS.md` et le carnet, les exercices dans `PLAN-TESTS.md`._

## Le but et la mesure
Livrer dans le logiciel une version que Diego n'aurait plus qu'à peaufiner : Resolve par son MCP, After Effects et Blender par script (et par MCP quand Diego en a installé un). Mesure : la part « livrable » qu'il donne et le nombre de retours. Bilan : projet 1 (kinetic, 1 min) 50 → 80-85 % en quatre retours très guidés ; projet 2 (mariage, 5 min) 10 → 25 %, clos. Exercices techniques courts : `PLAN-TESTS.md`.

## Sécurité (prime sur tout)
1. Logiciels : projets de test seulement (Resolve : `P3-<projet>-agent` ; After Effects et Blender : fichiers dans `videos/phase-3/<projet>/_travail/`) ; aucun projet de Diego ouvert ni modifié ; enregistrer avant tout geste risqué et avant de finir.
2. Médias en lecture seule : rien n'est déplacé, renommé, réencodé, écrasé ; travail dans `_travail/`, rendus dans `rendus/`. Seule écriture dans un dossier source : des fichiers stabilisés nouveaux, après accord de Diego (une fois par projet).
3. Test à l'aveugle : jamais chercher la version de Diego avant qu'il la dépose dans `final-diego/`.
4. `run_script_unsafe` seulement si aucun outil dédié ne le permet, jamais pour supprimer ; chaque usage au journal.
5. Sons : Artlist (ou une banque indiquée par Diego), avec son compte ; rien d'acheté ; 100 téléchargements par jour au plus ; chaque son noté dans `sfx.md`.
6. Un doute qui peut abîmer quelque chose : demander. Pour le reste : décider et noter.

## Au début de chaque projet ou exercice : la liste des moyens
Ce qui manque pour faire au mieux (logiciel, serveur MCP, plugin, modèle IA, licence, autorisation de macOS, réglage d'un logiciel), avec pour chaque élément : à quoi il sert, gratuit ou payant, officiel ou communautaire. Diego valide ; j'installe ce qui s'installe sans compte, sans achat et sans autorisation de macOS ; il fait le reste (principe de Diego du 2026-10-13, `CLAUDE.md`).

## L'ordre de travail d'un projet (fichiers texte dans `projets-phase-3/<projet>/`)
0. Genre, ton, destination en tête de `plan.md` ; relire le brief, `GOUTS.md`, `videos/NOTES-DIEGO.md`, les skills du genre. Pas de référence du même genre et de la même durée : le dire à Diego avant de monter.
1. Dérush → `derush.md` : métadonnées lues avant tout proxy ; toute la parole transcrite ; par rush, les bons moments et les prises écartées ; les séries du cadreur (plans faits pour être montés ensemble) et ce qu'elles appellent ; la valeur humaine repérée (regard caméra, sourire, geste). En mariage, événementiel, after movie, run and gun : passe serrée (une image par seconde, bandes) sur les moments forts (Diego, 2026-10-12).
2. Plan → `plan.md` : intention en une phrase ; blocs minutés, chacun avec « pourquoi ces plans, dans cet ordre » (ni chronologique, ni au hasard) et sa durée comparée à la référence.
3. DA → `da.md`, avant le moindre effet (`montage-direction-artistique`) : chaque ligne dit sa source (brief, Diego, référence, moi).
4. Look et mouvement → `look.md` : planche côte à côte avec la référence ; seuil de tremblement calibré sur un plan stable du projet.
5. Monter : un geste, une image de contrôle ; chaque appel au journal (`journal.md`). Resolve léger (`montage-resolve`) ; ambiance continue sous la parole ; textes lisibles sur téléphone si le format l'exige.
6. Juger : rendu ; contrôles de `montage-regard` ; directeur artistique (ci-dessous) ; autocritique qui montre ou doute ; variantes réellement différentes sur les moments clés ; film entier relu après chaque série de corrections. Deux ou trois versions, puis `note-de-livraison.md` : choix, plans remplacés hors des retours, triches, désaccords avec le DA, ce que Diego doit regarder et écouter (minuté), ce que je n'ai pas su faire.
7. Comparaison, si Diego dépose sa version (`final-diego/`) → `comparaison.md`.

## Le directeur artistique (sous-agent `directeur-artistique`, écrit par le consultant de Diego ; je ne le modifie qu'avec l'accord explicite de Diego)
Toujours un appel neuf, sans mon raisonnement (ni journal, ni contrôles, ni autocritique) :

| Moment | Ce qu'il reçoit | Sa question |
|---|---|---|
| Après `plan.md` | brief, goûts, références, plan | L'idée du film est-elle forte ? Qu'est-ce qui est banal ? |
| Après le look de base | 6 images du film contre 6 de références, comparables (portrait contre portrait, N&B contre N&B) | Est-ce au niveau ? Blancs, noirs, densité ? |
| Après chaque moment clé | planche côte à côte : référence et rendu | Est-ce au niveau de la référence ? Qu'est-ce qui fait cheap ? |
| Avant chaque livraison | brief, références, le film entier en planches | Qu'est-ce qu'un client exigeant reprocherait ? |

Je réponds à **chacune** de ses remarques dans `projets-phase-3/<projet>/da-retours.md` : « corrigé » (et comment) ou « je garde, parce que… ». Les désaccords vont dans la note de livraison ; Diego tranche.

## Chaque session
Démarrage de `CLAUDE.md` ; reprendre où `PROGRESS.md` s'est arrêté ; pas de limite de temps (Diego : « je préfère que ça mette plus de temps et que le rendu soit propre ») ; s'arrêter à une étape propre, projets enregistrés, journal à jour ; commit et push à chaque étape terminée (fichiers texte seulement, `git status` avant) ; fin : `PROGRESS.md` (où reprendre) et synthèse de `RAPPORT.md` réécrits, commit, push.

## Accords de Diego encore valables
Mes LUT dans le sous-dossier `P3/` du dossier de LUT de Resolve ; Artlist via Chrome ; forcer Resolve à quitter quand il est figé : à redemander chaque fois.
