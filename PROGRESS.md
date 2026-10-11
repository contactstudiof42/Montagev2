# PROGRESS — état actuel

_Lire en premier. Seul l'état présent compte ici. La chaîne d'analyse, les outils et les règles ci-dessous servent à analyser toute nouvelle référence. L'état de clôture de la phase 1 est archivé dans `archives/phase-1/PROGRESS-cloture-phase-1.md`, et l'historique des sessions 1 à 25 dans `archives/phase-1/PROGRESS-historique.md`._

## PHASE 3 EN COURS (`PROMPT-PHASE-3.md`, sessions lancées par Diego seulement)
- Sessions 0 à 2 (2026-10-11) : bac à sable Resolve ; projet Sony V2 (50 %), comparaison avec Claude nu, V3 (65 %). Fichiers V2 et V3 archivés dans `archives/phase-3/sony-linkbuds/`.
- **Session V4 (2026-10-11, 16:24-17:45)** : retours de Diego sur la V3 intégrés, plus trois consignes dictées (Gyroflow = mouvement fluide ; fixe ou rail selon l'intention du cadreur ; jamais deux fois le même moment d'un rush). **V4 rendue** : `videos/phase-3/sony-linkbuds/rendus/sony_linkbuds_V4.mp4` (44,6 s, HEVC Main 10 39 Mb/s, −14,0 LUFS, −1,1 dBTP, photosensibilité OK, 0 doublon), timeline **`SONY_V4`** du projet `P3-sony-linkbuds-agent`, enregistré. Documents : `plan.md`, `look.md`, `autocritique.md`, `note-de-livraison.md`, `journal.md` (gestes 41-56), `sfx.md`. Nouveaux outils : `labo/outils/stabiliser.py` (fixe / rail), `appliquer_stab.py`, `doublons_timeline.py`, `tremblement.py --avant --bande`, `labo/couleur/look_sony_v4.py` (+ `oklab.py`, `banc_look.py`, `planche_look4.py`), `labo/outils/phase3/v4/` (`detourage.py`, `collage.py`, `sfx_prep.py`, `partition_sfx.py`, `gen_ouverture.py`, `bande_rush.py`). LUT : `LUT/P3/P3_sony_look_V4_{salle,jour,rouge,rouge_negatif}.cube`.
- V4 notée **80 % livrable** par Diego ; ses notes et consignes (sections du 2026-10-11 « notes sur la V4 » à « Référence pour le dernier pic ») sont intégrées et appliquées dans la V5.

## V5 LIVRÉE (2026-10-11, reprise du soir 20:54-21:50) — en attente des notes de Diego
**Rendu** : `videos/phase-3/sony-linkbuds/rendus/sony_linkbuds_V5.mp4` (44,6 s, HEVC Main 10 39 Mb/s, −13,9 LUFS, −1,1 dBTP, photosensibilité 3 au pire, 0 doublon, packshots 0,66 / 0,68 / 0,84 px). Timeline **`SONY_V5`** du projet `P3-sony-linkbuds-agent`, enregistrée (`SONY_V4` intacte). Documents à jour : `plan.md` (genre en tête, variantes et pourquoi), `autocritique.md`, `note-de-livraison.md` (preuve Gyroflow plan par plan, ce que Diego doit écouter), `journal.md` (gestes 57-71), `sfx.md` § V5. Versions V4 archivées dans `archives/phase-3/sony-linkbuds/V4/`. État de la première session V5 : `archives/phase-3/PROGRESS-V5-session-1.md`.
**Fait dans la reprise** : dernier pic refait (version b : calé sur les attaques, photosensibilité, 2 doublons retirés, comptoir exposé, respiration « net » contre « écho ») et posé à 831-948 ; étalonnage plan par plan (19 plans, ouverture, C6581, packshots) ; grain 20 % ; inversions à la place des flashs des drops 233 et 690 ; un son par transition (16 recalés, 5 retirés, 13 posés) ; contrôles (doublons avec les plans calculés, `controle_plans.py`, photosensibilité, ombres ×4) ; C6627 remplacé (visage) ; rail rétabli sur les packshots (Gyroflow seul tremblait 3 à 6 fois plus) ; essai Gyroflow sur C6507 à 117 écarté (tremblait 7 fois plus que le brut).
**Prochaine étape** : attendre les notes de Diego sur la V5 (`RETOURS-DIEGO.md`), puis V6 si besoin. Questions ouvertes pour lui (note de livraison) : le pic à l'oreille, le bloc des fentes (9,4-18,7 s) répétitif ou non, la définition de « transition » pour les sons, le lavande un peu rosé, la fin de la liste des flous ratés (message coupé).
**Doutes** : son jamais écouté ; deux mesures du tremblement contradictoires sur le tapis en carbone (`tremblement.py` retenu) ; synchronisation Gyroflow non prouvable sur C6725 et K-O-R-E (mouvement trop faible) ; le pic et les collages sont calculés hors de Resolve.
- Accords de Diego : mes LUT dans `LUT/P3/` seulement ; Artlist via Chrome (62 SFX sur 100 le 2026-10-11, aucun téléchargement en V5) ; fichiers Gyroflow `_stabilized*` dans `SONY copy/RUSH/` ; arrêt forcé de Resolve figé : accord ponctuel du 2026-10-11, à redemander.
- Pièges (détail `montage-resolve`) : `comp.Lock()` casse le rendu des clés ; ne jamais lire les entrées d'un effet IA OpenFX ; `AppendToTimeline` d'un rush avec son : `"mediaType": 1` ; `SetTrackEnable` sur la page Montage seulement ; Gyroflow : plage courte, timecode du rush gardé ; `ExportCurrentFrameAsStill` exporte le plan du dessus ; image 0 d'une composition 50p ≠ point d'entrée (`COMPN_GlobalStart`) ; `DeleteFusionCompByName` échoue sur la composition active ; `SetSpeed` garde la durée.

## PHASE 2 TERMINÉE (2026-10-11, session 11)
- 45 vidéos analysées (fiches dans `analyses/`), passe de révision faite (`analyses/REVISION.md`), skills de création révisés (sessions 10-11 : regard, couleur-et-intention, expert, references, formats, rythme condensé à 13 Ko avec les preuves dans `details.md`, son-et-emotion, grammaire, youtube, kinetic-editing, motion-design-principes). **Synthèse de fin de phase dans `RAPPORT.md`** ; bilans détaillés archivés dans `archives/phase-2/RAPPORT-bilans-detailles-phase-2.md` ; état de session 10 dans `archives/phase-2/PROGRESS-session-10.md`.
- **Désormais, chaque session ne fait que le démarrage de `CLAUDE.md`** : `git pull`, retours de Diego (`RETOURS-DIEGO.md`), boîte à références (`videos/a-traiter/`, `videos/NOTES-DIEGO.md`) avec le skill `montage-nouvelle-reference`. S'il n'y a rien de neuf : le dire en une ligne et s'arrêter.
- **Session 12 (2026-10-11)** : retour de Diego intégré : 7 vidéos de `videos/reseaux/` analysées image par image (fiches `analyses/reseaux/`, bilan dans `RAPPORT.md`), `montage-kinetic-editing` et `montage-formats` mis à jour. Scripts de la méthode « toutes les images » : `labo/outils/reseaux/`.
- **Session 13 (2026-10-11)** : retour de Diego intégré : vidéo de méthode d'étalonnage (David Foxprod, look de *Seven*) lue comme un tutoriel, fiche `analyses/methodes/`, méthode dans `montage-resolve` § 2 bis. Nouvelle catégorie `videos/methodes/` (tutoriels : on en tire une méthode, pas une analyse de montage).
- **Lacunes restantes** si une référence arrive : face caméra en jump cuts et captions mot à mot (Hormozi, MrBeast), pub de 6 et 30 s, corporate classique ; écouter un kinetic (rien n'a été écouté).
- `.claude/settings.json` (ajouté par Diego) n'est pas commité : le garde-fou de l'agent refuse ce commit. À laisser à Diego.

## Chaîne d'analyse d'un film (sessions 1-2)
1. `ffprobe` : pistes audio et sous-titres, **et `color_transfer`** (si `smpte2084`, préfixer `HDR=1`). Puis `labo/outils/passe_globale.sh FILM videos/_travail/<nom> <piste audio VO> <sous-titre texte ou -1>` en arrière-plan (6 à 9 min). Sans sous-titres texte : `whisper-cli` sur l'audio 16 kHz.
2. `courbes_film.py` (crée `coupes.json`, rythme et volume) et `couleur_film.py` (couleur).
3. Repérer les scènes dans les sous-titres, puis `LUFS=M sequence.py DOSSIER DEBUT FIN sortie.png [colonnes] [largeur]` pour chaque séquence (planche < 500 Ko). Lancer les planches en parallèle (fonction shell : zsh ne découpe pas une commande rangée dans une variable).
4. Vérifier tout plan long cité : `verif_plan.py` + tuile ffmpeg `fps=1/2` (puis 3 à 6 images/s sur le passage douteux) ; regarder s'il s'agit d'un filé.
4 bis. Vérifier toute rafale citée (session 10) : la passe globale fusionne les plans de moins de 0,6 s. `scenedetect -i proxy.mp4 -m 1 -d 2 time -s Ds -e Fs detect-adaptive list-scenes` sur le passage, puis `bandes_coupes.py` (6 images consécutives par coupe) ; si les plans semblent à 2-3 images, tuile à pleine cadence sur 2 s (`tile=10x5`).
5. Musique : `calage.py DOSSIER DEBUT FIN 2 97` (coupes contre attaques fortes et temps, avec le hasard). Dialogue : `coupes_parole.py DOSSIER DEBUT FIN` (il faut `audio16k.wav` dans le dossier).

## Leçons de méthode (test sur SDM)
- Les détecteurs de coupes (`analyse_clip.py` et PySceneDetect) **ratent les coupes cachées** par l'occlusion d'un corps ou par un filé, ainsi que les coupes des scènes sombres. Ils inventent aussi des coupes quand la lumière clignote (voir `PROMPT-PHASE-2.md`).
- `labo/outils/planche.py` donne une planche (une image par plan, avec la courbe LUFS, les coupes et les temps en dessous). Il réduit le PNG en palette (128 couleurs ou moins) jusqu'à passer sous 500 000 octets : les aplats saturés (rouge) se postérisent, donc **ne pas juger la couleur fine sur la planche**, mais sur une image extraite.

## Outils (installés le 2026-10-11, temps mesurés)
- Déjà présents : ffmpeg 8.1.1 (Homebrew), Homebrew. Le Python système (3.15 rc) est trop récent pour librosa : ne pas l'utiliser pour l'analyse.
- `brew install gh` (temps non mesuré) : connexion GitHub (compte contactstudiof42).
- `brew install uv whisper-cpp` : **23 s**.
- `uv venv --python 3.12 .venv` + `numpy pillow librosa scenedetect opencv-python-headless` : **5 s**. Lancer les scripts avec `.venv/bin/python -I`.
- Modèle Whisper `ggml-large-v3-turbo.bin` (1,5 Go), dans `~/.cache/whisper-cpp/` : **9 s**. Transcription : `whisper-cli -m ~/.cache/whisper-cpp/ggml-large-v3-turbo.bin -l fr -osrt -mc 0 -ojf -of <sortie> -f <audio 16 kHz mono>`. Un clip de 3 min se transcrit en moins d'une minute (Metal).
- `demucs` (séparation voix / musique) dans le même venv : **8 s**.
- QC d'un fichier livré : `labo/outils/qc_livraison.sh` (session 6, aucune installation). Coupes et parole à l'œil : `labo/outils/spectro_coupes.py` (session 8). Torch avec MPS disponible.
- Durée de toute la chaîne sur un clip de 3 min (fiche technique, loudness, coupes, tempo, transcription) : **60 s**.

## Inventaire de `videos/` (2026-10-11)
| Catégorie | Titre | Durée | Analysé |
|---|---|---|---|
| films | Aftersun (2022) | 1 h 41 min | ✔ 2026-10-11 (6 séquences, 14 plans longs vérifiés ; eau et miroir à faire) |
| films | Avengers: Infinity War (2018) | 2 h 29 min | ✔ 2026-10-11 (4 séquences + acte final ; couleur fine à faire) |
| films | Forrest Gump (1994), 2160p HDR10 | 2 h 22 min | ✔ 2026-10-11 (4 séquences ; couleur et fin à faire) |
| films | Interstellar (2014), IMAX | 2 h 49 min | ✔ 2026-10-11 |
| films | Joker (2019) | 2 h 01 min | ✔ 2026-10-11 (7 séquences) |
| films | La Haine (1995) | 1 h 33 min | ✔ 2026-10-11 (5 séquences, 9 plans longs vérifiés) |
| films | Le Dîner de cons (1998) | 1 h 20 min | ✔ 2026-10-11 (4 séquences + timing) |
| films | Mad Max: Fury Road (2015) | 2 h 00 min | ✔ 2026-10-11 (7 séquences) |
| films | OSS 117 : Le Caire, nid d'espions (2006) | 1 h 39 min | ✔ 2026-10-11 (4 séquences + nuits + coupes / parole tranchées) |
| films | Spider-Man: Across the Spider-Verse (2023), HDR10, AV1 | 2 h 20 min | ✔ 2026-10-11 (5 séquences + générique + calage ; poursuite à faire) |
| films | Spotlight (2015) | 2 h 09 min | ✔ 2026-10-11 (4 séquences + comparaison ; témoignages à faire) |
| films | The Social Network (2010) | 2 h 00 min | ✔ 2026-10-11 (3 séquences ; dépositions et fin à faire) |
| films | Whiplash (2014), 2160p HDR | 1 h 46 min | ✔ 2026-10-11 (6 séquences) |
| clips | Booba — 6G | 3 min 39 s | ✔ 2026-10-11 |
| clips | GENER8ION — STORM (starring Yung Lean) | 7 min 34 s | ✔ 2026-10-11 |
| clips | HOUDI — Belle chanson | 3 min 37 s | ✔ 2026-10-11 |
| clips | Justice — Stress | 6 min 44 s | ✔ 2026-10-11 |
| clips | PNL — Au DD | 4 min 50 s | ✔ 2026-10-11 |
| clips | SDM — #Malentouré | 2 min 54 s | ✔ 2026-10-11 (test de méthode) |
| clips | Yvnnis — Gare du Nord | 3 min 09 s | ✔ 2026-10-11 |
| clips | Ziak — Même pas un grincement | 3 min 49 s | ✔ 2026-10-11 (recompté : 109 plans) |
| pubs | Crunch Creator — bande-annonce | 2 min 22 s | ✔ 2026-10-11 |
| pubs | GP Explorer 3 — bande-annonce | 2 min 17 s | ✔ 2026-10-11 |
| pubs | Intermarché — Conte de Noël | 2 min 30 s | ✔ 2026-10-11 |
| pubs | Intermarché 2017 — L'amour | 3 min 00 s | ✔ 2026-10-11 |
| pubs | Lacoste — Life is a Beautiful Sport | 1 min 10 s | ✔ 2026-10-11 |
| pubs | adidas — Backyard Legends | 5 min 05 s | ✔ 2026-10-11 |
| pubs | iPhone 17 — 3x More Scratch Resistant | 0 min 35 s | ✔ 2026-10-11 |
| youtube | Créer YggTorrent, puis le détruire (480p) | 1 h 11 min | ✔ 2026-10-11 |
| youtube | KAIZEN : 1 an pour gravir l'Everest (480p) | 2 h 26 min | ✔ 2026-10-11 (8 séquences) |
| youtube | Les Jeux Tiger ! (720p) | 31 min 02 s | ✔ 2026-10-11 (6 séquences) |
| youtube | La seule façon de monter les B-roll | 8 min 40 s | ✔ 2026-10-11 |
| youtube | Le jour où la CIA a trahi la France (720p) | 48 min 58 s | ✔ 2026-10-11 (6 séquences) |
| youtube | Philippe Boxho, médecin légiste, partie 1 (480p) | 1 h 07 min | ✔ 2026-10-11 |
| youtube | Popcorn avec Anyme, Léna Situations & Etoiles (480p) | 2 h 32 min | ✔ 2026-10-11 (6 séquences) |
| youtube | Qui est l'imposteur (ft Eric & Ramzy) (720p) | 57 min 19 s | ✔ 2026-10-11 (fiche commune) |
| youtube | Qui est l'imposteur (ft Theodora & Guy2Bezbar) (480p) | 54 min 38 s | ✔ 2026-10-11 (fiche commune) |
| youtube | Visite extraordinaire d'une Bibliothèque-Univers (EGO, confirmé : vidéo du 23/09/2026) | 23 min 22 s | ✔ 2026-10-11 |
| projets-f42 | Benefit — pub réseau (vertical) | 0 min 23 s | ✔ 2026-10-11 (fiche commune) |
| projets-f42 | Benefit — pub réseau 2 (vertical) | 0 min 26 s | ✔ 2026-10-11 (fiche commune) |
| projets-f42 | Fou rire — court métrage | 2 min 21 s | ✔ 2026-10-11 |
| projets-f42 | Hirsingen (5.1) | 14 min 59 s | ✔ 2026-10-11 |
| projets-f42 | Oney — vidéo d’intro « 169 » V3 mobile (fichier en 1:1) | 0 min 37 s | ✔ 2026-10-11 |
| projets-f42 | Sephora — brand content | 2 min 45 s | ✔ 2026-10-11 |
| projets-f42 | Swile — POW 16:9 V5 | 1 min 19 s | ✔ 2026-10-11 |
| reseaux | captured-by-h — collage d'archives (16:9) | 0 min 14 s | ✔ 2026-10-11 (toutes les images) |
| reseaux | dariusbuesch — Nike Air Max Muse (9:16, **360x640**) | 0 min 38 s | ✔ 2026-10-11 (toutes les images ; netteté non jugée) |
| reseaux | Équipe de France — Coupe du monde 2026 (9:16) | 0 min 43 s | ✔ 2026-10-11 (toutes les images) |
| reseaux | lucasbosc — Sephora Collection « Stretch » (16:9) | 0 min 15 s | ✔ 2026-10-11 (toutes les images) |
| reseaux | malkimikee — Paris (4:3) | 0 min 12 s | ✔ 2026-10-11 (toutes les images) |
| reseaux | pasalu.jpg — chambre, look film (16:9) | 0 min 13 s | ✔ 2026-10-11 (toutes les images) |
| reseaux | yungchillyboy — fête foraine (16:9) | 0 min 13 s | ✔ 2026-10-11 (toutes les images) |
| methodes | David Foxprod — recréer la colo de *Seven* (9:16, 530 Ko) | 0 min 12 s | ✔ 2026-10-11 (méthode d'étalonnage, pas de montage) |

Total : 13 films (environ 26 h), 8 clips, 7 pubs, 10 vidéos YouTube (environ 10 h 40), 7 projets du studio, 7 vidéos réseaux (2 min 28 s, ajoutées par Diego le 2026-10-11, noms de fichiers laissés tels quels), 1 tutoriel d'étalonnage (`methodes/`). `a-traiter/` et `_a-supprimer/` sont vides. `NOTES-DIEGO.md` ne contient que les titres des projets, sans commentaire : Diego n'a encore commenté aucun film (l'ancienne note sur l'amarrage d'Interstellar était un exemple de format, pas sa parole).

## Règles de session encore valables
- Relever `date` au début de la session et le relire avant de clôturer : estimée « au ressenti », la durée écoulée est surévaluée d'un facteur 3 à 8.
- Jamais d'identifiant personnel (adresse e-mail…) dans un en-tête de requête.
- Le serveur `HIGGSFIELD_MCP` peut consommer des crédits payants : ne rien générer sans accord explicite.
- `pkill -f motif` tue le shell appelant : tuer par PID. Les calculs longs se lancent avec `run_in_background`, pas avec `&`.
- ffmpeg Homebrew sans `drawtext` (pas de texte sur les tuiles) : annoter avec Pillow. L'option `framelog=verbose` d'ebur128 ne sort rien sans `-v verbose` : utiliser `ebur128` simple.
- ffmpeg en `yuv*` = plage limitée (noir = 16). PIL lit un PNG 16 bits en 8 bits.
- Ne jamais modifier un script zsh pendant qu'une exécution le lit (zsh lit au fil de l'eau). Sortie `ffprobe -of csv=p=0` : peut finir par une virgule ; préférer `-of default=nw=1:nk=1`.
- zsh : `====` en début de mot déclenche une erreur (« = not found ») ; écrire des séparateurs entre guillemets.
