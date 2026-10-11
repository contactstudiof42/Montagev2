# PROGRESS — état actuel

_Lire en premier. Seul l'état présent compte ici. L'état de clôture de la phase 1 est archivé dans `archives/phase-1/PROGRESS-cloture-phase-1.md`, et l'historique des sessions 1 à 25 dans `archives/phase-1/PROGRESS-historique.md`._

## État (2026-10-11, session 10 de la phase 2, 10:04-10:20 à l'horloge)
- **Phase 2 en cours** : mission `PROMPT-PHASE-2.md` (lire aussi « Avant chaque vidéo : repartir de la phase 1 », « Leçons de méthode », « Passe de révision »). Démarrage de chaque session : `CLAUDE.md`.
- Session 10 : aucun retour neuf, boîte vide. **Passe de révision (étape 7) terminée** (sessions 9-10), suivi dans `analyses/REVISION.md`, **bilan chiffré définitif dans `RAPPORT.md`** : 45 conclusions vérifiées, 28 confirmées (62 %), 14 corrigées (31 %), 3 nouvelles ; toutes les corrections viennent d'un instrument (parole par énergie, fausses rafales, plans de moins de 0,6 s fusionnés, générique compté), aucune d'une image regardée.
- Découverte de session 10 : **PySceneDetect ne garde aucun plan de moins de 0,6 s** (réglage par défaut de `passe_globale.sh`). Gare du Nord : la rafale-inventaire = environ 65 plans de 2 images (photosensibilité conforme, pire seconde 2) ; *Spider-Verse* : récapitulatif d'environ 130 plans (calage = hasard) ; HOUDI : deux images-éclair. Confirmés : 6G, KAIZEN, Joker, Mad Max, Whiplash (contre-épreuve). Avengers : ASL du film seul 3,7 s. La Haine : rien à changer. Nouvel outil `labo/outils/bandes_coupes.py`. Leçon inscrite dans `PROMPT-PHASE-2.md`. Skills corrigés : `montage-kinetic-editing` (Spider-Verse, clignotement de Gare du Nord, strobe sûr vu sur images), `montage-rythme` (crête de Spider-Verse).
- **Reprendre ici : étape 8, synthèse finale.** Plan proposé : (1) relire chaque skill contre les bilans de `RAPPORT.md` (vagues 1-3, clips, pubs, YouTube, projets, révision) : principes de phase 2 intégrés avec leur marqueur, contradictions levées, nombres « minimums » signalés ; priorités d'après le décompte des marqueurs (session 10) : ~~`montage-regard`~~ (**fait en session 10** : section « Juger une vraie vidéo : règles de vérification », piège du climax dans la grille, QC dans le verdict, limite du son), ~~`montage-couleur-et-intention`~~ (**fait en session 10** : section « Ce que 45 vraies vidéos confirment », deux principes de maquette passés en [VU SUR IMAGES]), ~~`montage-expert`~~ (**fait en session 10** : six acquis de la phase 2 avec renvois, statuts du sommaire mis à jour, chaîne d'analyse dans les ressources), `montage-formats` (déjà 4 [VU SUR IMAGES] sur les pubs : à relire) et ~~`montage-references`~~ (**fait en session 10** : section G « Œuvres vues en phase 2 », EGO, Gavras, PNL, *Aftersun*, Henley passés en [VU SUR IMAGES], lacunes réécrites) ; `montage-rythme` (21,8 Ko, 22 [VU SUR IMAGES]) est à condenser ; les skills techniques (After Effects, Blender, Resolve, Premiere, pipeline, loudness, workflows, IA) n'ont rien reçu de la phase 2 et restent tels quels sauf le QC de livraison (loudness). (2) Écrire dans `RAPPORT.md` la synthèse de fin de phase 2 (ce que j'ai appris par domaine, ce que le goût de Diego et les projets F42 impliquent, ce qui reste [THÉORIQUE]), et archiver les bilans détaillés dans `archives/phase-2/`. (3) Écrire « PHASE 2 TERMINÉE » ici. Compter une session, deux au plus.
- Fichiers de travail de session 10 : `videos/_travail/revision/bandes/`, `videos/_travail/revision/m1b/`, `m1full/`, `m1content/` (détections sans durée minimale ; non commités, ignorés par Git).
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

Total : 13 films (environ 26 h), 8 clips, 7 pubs, 10 vidéos YouTube (environ 10 h 40), 7 projets du studio. `a-traiter/` et `_a-supprimer/` sont vides. `NOTES-DIEGO.md` ne contient que les titres des projets, sans commentaire : Diego n'a encore commenté aucun film (l'ancienne note sur l'amarrage d'Interstellar était un exemple de format, pas sa parole).

## Règles de session encore valables
- Relever `date` au début de la session et le relire avant de clôturer : estimée « au ressenti », la durée écoulée est surévaluée d'un facteur 3 à 8.
- Jamais d'identifiant personnel (adresse e-mail…) dans un en-tête de requête.
- Le serveur `HIGGSFIELD_MCP` peut consommer des crédits payants : ne rien générer sans accord explicite.
- `pkill -f motif` tue le shell appelant : tuer par PID. Les calculs longs se lancent avec `run_in_background`, pas avec `&`.
- ffmpeg Homebrew sans `drawtext` (pas de texte sur les tuiles) : annoter avec Pillow. L'option `framelog=verbose` d'ebur128 ne sort rien sans `-v verbose` : utiliser `ebur128` simple.
- ffmpeg en `yuv*` = plage limitée (noir = 16). PIL lit un PNG 16 bits en 8 bits.
- Ne jamais modifier un script zsh pendant qu'une exécution le lit (zsh lit au fil de l'eau). Sortie `ffprobe -of csv=p=0` : peut finir par une virgule ; préférer `-of default=nw=1:nk=1`.
- zsh : `====` en début de mot déclenche une erreur (« = not found ») ; écrire des séparateurs entre guillemets.
