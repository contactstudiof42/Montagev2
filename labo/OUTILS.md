# Index des outils et des contrôles du dépôt

_Créé le 2026-10-13 (audit 2) à partir de la section « Ressources du dépôt » de l'ancien skill `montage-expert` (archivé) et de la section « Outils » de `PROGRESS.md`. Du savoir consultable, pas des règles : les contrôles obligatoires sont dans `montage-regard` (liste maître) ; la chaîne d'analyse d'une vraie vidéo et ses leçons, dans `montage-nouvelle-reference/methode-analyse.md`. Outils du projet 2 (dérush, synchro, parole, relecture) : `labo/outils/phase3/mariage/`._

## Outils installés sur le Mac
- Déjà présents : ffmpeg 8.1.1 (Homebrew), Homebrew. Le Python système (3.15 rc) est trop récent pour librosa : ne pas l'utiliser pour l'analyse.
- `brew install gh` (temps non mesuré) : connexion GitHub (compte contactstudiof42).
- `brew install uv whisper-cpp` : **23 s**.
- `uv venv --python 3.12 .venv` + `numpy pillow librosa scenedetect opencv-python-headless` : **5 s**. Lancer les scripts avec `.venv/bin/python -I`.
- Modèle Whisper `ggml-large-v3-turbo.bin` (1,5 Go), dans `~/.cache/whisper-cpp/` : **9 s**. Transcription : `whisper-cli -m ~/.cache/whisper-cpp/ggml-large-v3-turbo.bin -l fr -osrt -mc 0 -ojf -of <sortie> -f <audio 16 kHz mono>`. Un clip de 3 min se transcrit en moins d'une minute (Metal).
- `demucs` (séparation voix / musique) dans le même venv : **8 s**.
- QC d'un fichier livré : `labo/outils/qc_livraison.sh` (session 6, aucune installation). Coupes et parole à l'œil : `labo/outils/spectro_coupes.py` (session 8). Torch avec MPS disponible.
- Durée de toute la chaîne sur un clip de 3 min (fiche technique, loudness, coupes, tempo, transcription) : **60 s**.
- WhisperX (alignement forcé mot à mot, local) : `.venv-whisperx` (installé le 2026-10-12) ; voir `montage-grammaire`, « Couper dans la parole ».
- Logiciels relevés le 2026-10-13 : DaVinci Resolve Studio 21.1.1 (serveur MCP natif), After Effects 26.3 et `aerender`, Premiere 26.3.0, Blender 5.2.2 LTS, Gyroflow (version GitHub dans `~/Applications/`), Topaz Video AI 7.1.4 (sans ses modèles d'interpolation). Serveurs MCP et ponts : Resolve (natif) ; Blender Lab (module v1.0.3 dans Blender, extension de Claude v1.0.1 désactivée) ; Higgsfield pour After Effects et Premiere (extension `ai.higgsfield.cep` v1.0.57, outil `higgsfield` 1.1.26 ; connecteur pas encore visible dans mes sessions). État et règles : `PLAN-TESTS.md`, section 6.

## Ressources et contrôles du dépôt (texte de l'ancien `montage-expert`)
- `culture/` : fiches d'œuvres (montage, title design, couleur, goûts de l'utilisateur : Interstellar, Joker, Ziak ; clips et pubs : Murai, Honda « Cog » ; IA).
- `atelier/` : pièces créées et leurs versions critiquées.
- `labo/` : scripts techniques testés. **Contrôles à lancer avant de livrer ou de juger** :
  - **regarder et mesurer un montage autour de ses coupes** (EDL CMX3600 avec fondus, OTIO, ou scdet ; bande-film avec son, coupes/min, activité nette du grain) : `python3 -I labo/outils/coupes.py export.mp4 --edl seq.edl --scdet 10 --sortie verif` (session 24) ;
  - **micro-sauts d'un jump cut** (échelle du punch-in et décalage en % de largeur à chaque coupe ; pic < 0,15 = changement de plan) : `python3 -I labo/micro-sauts/micro_sauts.py --video export.mp4 --coupes 3.2,7.84` (session 25) ;
  - **trous sans événement** dans un plan long (répliques, sons, événements d'image) : `atelier/34-de-dehors/mesure.py evenements.json` — ne dit pas si l'événement est visible : regarder la planche (session 25) ;
  - photosensibilité : `python3 -I labo/photosensibilite/flash_check.py rendu.mp4` (WCAG 2.3.1, fenêtre locale) ;
  - coupes, flashs, calage musical d'un clip : `python3 -I labo/analyse-clip/analyse_clip.py video sortie` ;
  - loudness : mesure ebur128 **sur le fichier encodé**, puis gain (`montage-loudness-livraison`) ;
  - 180° / regards à l'écran pour des plans Blender : `labo/grammaire/axe180.py` (projection tête / regard) ;
  - cadence variable et synchro : `labo/vfr/mesure_vfr.py` ; proxies rattachables : `labo/proxies/verif_proxy.py` ;
  - couleur d'un événement : `atelier/10-chaleur-partout/mesure_zone.py` (zone = différence allumé / éteint) ;
  - downmix 5.1 → stéréo / mono : `labo/surround/labo_surround.py` ;
  - où va le regard / une anomalie d'un plan à l'autre (saillance grossière, aire du changement) : `atelier/12-inquietude-calme/mesure.py plan1.png plan3.png` ;
  - peau et fond en Lab, induction chromatique estimée : `atelier/13-fond-raccorde/mesure.py` (masque de peau rendu) ;
  - une coupe à l'image près (bande-film image par image + enveloppe du son, repères mot-clé / coupe / réaction) : `atelier/27-jamais/bande.py` ;
  - lisibilité d'un objet flou (corrélation à l'échelle de l'objet, pas variance du laplacien) : `atelier/28-flou-net/CRITIQUE.md` (code en v2) ;
  - qualité d'un ralenti interpolé contre vérité terrain : `labo/interpolation/` (`compare.sh`, `analyse.py`, `zones.py`, `rife60.py`).
- `analyses/` : les fiches des 45 vidéos de la phase 2 (films, clips, pubs, YouTube, projets du studio), `analyses/REVISION.md` (passe de révision). Chaîne d'analyse d'une vraie vidéo (`labo/outils/`, mode d'emploi dans `montage-nouvelle-reference/methode-analyse.md`) : `passe_globale.sh` (copie légère, coupes, loudness, sous-titres ; `HDR=1`), `courbes_film.py`, `couleur_film.py`, `sequence.py` (planche d'une séquence), `verif_plan.py` (plan long), `bandes_coupes.py` (rafale), `calage.py` (coupes contre musique, contre le hasard), `coupes_parole.py` et `spectro_coupes.py` (coupes et parole), `qc_livraison.sh` (contrôle d'un fichier livré).
- `PLAN-TESTS.md` : les exercices techniques et la liste des moyens ; l'ancien `PLAN-TESTS-MCP.md` est archivé dans `archives/phase-3/`.
- `archives/phase-2/PHASE-2-BESOINS.md` : vidéos attendues en phase 2 (archivé).
