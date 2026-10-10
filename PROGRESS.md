# PROGRESS — état actuel

_Lire en premier. Seul l'état présent compte ici. L'état de clôture de la phase 1 est archivé dans `archives/phase-1/PROGRESS-cloture-phase-1.md`, et l'historique des sessions 1 à 25 dans `archives/phase-1/PROGRESS-historique.md`._

## État (2026-10-11, session 0 de la phase 2)
- **Phase 2 en cours** : analyse de vraies vidéos, en local sur le Mac de Diego (M1 Max). Mission : `PROMPT-PHASE-2.md`. Démarrage de chaque session : `CLAUDE.md`.
- Session 0 faite : `videos/` ignoré par Git, fichiers de la phase 2 en place, ancien `PROMPT.md` archivé, 10 réponses de goût présentes dans `GOUTS.md`, outils installés, méthode testée sur un clip (`analyses/clips/sdm-malentoure.md`).
- **Reprendre ici** : étape 0 de `PROMPT-PHASE-2.md`, c'est-à-dire créer le skill `montage-nouvelle-reference` (il n'existe pas encore). Ensuite, films vague 1 en commençant par **Interstellar** (passe globale).

## Leçons de méthode (test sur SDM)
- Les détecteurs de coupes (`analyse_clip.py` et PySceneDetect) **ratent les coupes cachées** par l'occlusion d'un corps ou par un filé. Dans tout plan de plus de 15 s, il faut regarder une image toutes les 2 à 3 s, puis image par image autour des passages suspects.
- `labo/outils/planche.py` donne une planche (une image par plan, avec la courbe LUFS, les coupes et les temps en dessous). Il réduit le PNG en palette de 128 couleurs pour rester sous 500 Ko : les aplats saturés (rouge) se postérisent, donc **ne pas juger la couleur fine sur la planche**, mais sur une image extraite.

## Outils (installés le 2026-10-11, temps mesurés)
- Déjà présents : ffmpeg 8.1.1 (Homebrew), Homebrew. Le Python système (3.15 rc) est trop récent pour librosa : ne pas l'utiliser pour l'analyse.
- `brew install gh` (temps non mesuré) : connexion GitHub (compte contactstudiof42).
- `brew install uv whisper-cpp` : **23 s**.
- `uv venv --python 3.12 .venv` + `numpy pillow librosa scenedetect opencv-python-headless` : **5 s**. Lancer les scripts avec `.venv/bin/python -I`.
- Modèle Whisper `ggml-large-v3-turbo.bin` (1,5 Go), dans `~/.cache/whisper-cpp/` : **9 s**. Transcription : `whisper-cli -m ~/.cache/whisper-cpp/ggml-large-v3-turbo.bin -l fr -osrt -ojf -of <sortie> -f <audio 16 kHz mono>`. Un clip de 3 min se transcrit en moins d'une minute (Metal).
- `demucs` (séparation voix / musique) dans le même venv : **8 s**. Torch avec MPS disponible.
- Durée de toute la chaîne sur un clip de 3 min (fiche technique, loudness, coupes, tempo, transcription) : **60 s**.

## Inventaire de `videos/` (2026-10-11)
| Catégorie | Titre | Durée | Analysé |
|---|---|---|---|
| films | Aftersun (2022) | 1 h 41 min | |
| films | Avengers: Infinity War (2018) | 2 h 29 min | |
| films | Forrest Gump (1994), 2160p HDR10 | 2 h 22 min | |
| films | Interstellar (2014), IMAX | 2 h 49 min | |
| films | Joker (2019) | 2 h 01 min | |
| films | La Haine (1995) | 1 h 33 min | |
| films | Le Dîner de cons (1998) | 1 h 20 min | |
| films | Mad Max: Fury Road (2015) | 2 h 00 min | |
| films | OSS 117 : Le Caire, nid d'espions (2006) | 1 h 39 min | |
| films | Spider-Man: Across the Spider-Verse (2023), HDR10, AV1 | 2 h 20 min | |
| films | Spotlight (2015) | 2 h 09 min | |
| films | The Social Network (2010) | 2 h 00 min | |
| films | Whiplash (2014), 2160p HDR | 1 h 46 min | |
| clips | Booba — 6G | 3 min 39 s | |
| clips | GENER8ION — STORM (starring Yung Lean) | 7 min 34 s | |
| clips | HOUDI — Belle chanson | 3 min 37 s | |
| clips | Justice — Stress | 6 min 44 s | |
| clips | PNL — Au DD | 4 min 50 s | |
| clips | SDM — #Malentouré | 2 min 54 s | ✔ 2026-10-11 (test de méthode) |
| clips | Yvnnis — Gare du Nord | 3 min 09 s | |
| clips | Ziak — Même pas un grincement | 3 min 49 s | |
| pubs | Crunch Creator — bande-annonce | 2 min 22 s | |
| pubs | GP Explorer 3 — bande-annonce | 2 min 17 s | |
| pubs | Intermarché — Conte de Noël | 2 min 30 s | |
| pubs | Intermarché 2017 — L'amour | 3 min 00 s | |
| pubs | Lacoste — Life is a Beautiful Sport | 1 min 10 s | |
| pubs | adidas — Backyard Legends | 5 min 05 s | |
| pubs | iPhone 17 — 3x More Scratch Resistant | 0 min 35 s | |
| youtube | Créer YggTorrent, puis le détruire (480p) | 1 h 11 min | |
| youtube | KAIZEN : 1 an pour gravir l'Everest (480p) | 2 h 26 min | |
| youtube | Les Jeux Tiger ! (720p) | 31 min 02 s | |
| youtube | La seule façon de monter les B-roll | 8 min 40 s | |
| youtube | Le jour où la CIA a trahi la France (720p) | 48 min 58 s | |
| youtube | Philippe Boxho, médecin légiste, partie 1 (480p) | 1 h 07 min | |
| youtube | Popcorn avec Anyme, Léna Situations & Etoiles (480p) | 2 h 32 min | |
| youtube | Qui est l'imposteur (ft Eric & Ramzy) (720p) | 57 min 19 s | |
| youtube | Qui est l'imposteur (ft Theodora & Guy2Bezbar) (480p) | 54 min 38 s | |
| youtube | Visite extraordinaire d'une Bibliothèque-Univers (EGO, à confirmer) | 23 min 22 s | |
| projets-f42 | Benefit — pub réseau (vertical) | 0 min 23 s | |
| projets-f42 | Benefit — pub réseau 2 (vertical) | 0 min 26 s | |
| projets-f42 | Fou rire — court métrage | 2 min 21 s | |
| projets-f42 | Hirsingen (5.1) | 14 min 59 s | |
| projets-f42 | Oney — vidéo d'intro 16:9 V3 mobile | 0 min 37 s | |
| projets-f42 | Sephora — brand content | 2 min 45 s | |
| projets-f42 | Swile — POW 16:9 V5 | 1 min 19 s | |

Total : 13 films (environ 26 h), 8 clips, 7 pubs, 10 vidéos YouTube (environ 10 h 40), 7 projets du studio. `a-traiter/` et `_a-supprimer/` sont vides. Le contenu de `NOTES-DIEGO.md` se limite pour l'instant à l'exemple Interstellar (l'amarrage, vers 1 h 52) et aux titres des projets, sans commentaire.

## Règles de session encore valables
- Relever `date` au début de la session et le relire avant de clôturer : estimée « au ressenti », la durée écoulée est surévaluée d'un facteur 3 à 8.
- Jamais d'identifiant personnel (adresse e-mail…) dans un en-tête de requête.
- Le serveur `HIGGSFIELD_MCP` peut consommer des crédits payants : ne rien générer sans accord explicite.
- `pkill -f motif` tue le shell appelant : tuer par PID. Les calculs longs se lancent avec `run_in_background`, pas avec `&`.
- ffmpeg en `yuv*` = plage limitée (noir = 16). PIL lit un PNG 16 bits en 8 bits.
- zsh : `====` en début de mot déclenche une erreur (« = not found ») ; écrire des séparateurs entre guillemets.
