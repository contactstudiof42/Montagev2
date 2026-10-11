# PROGRESS — état actuel

_Lire en premier. Seul l'état présent compte ici. L'état de clôture de la phase 1 est archivé dans `archives/phase-1/PROGRESS-cloture-phase-1.md`, et l'historique des sessions 1 à 25 dans `archives/phase-1/PROGRESS-historique.md`._

## État (2026-10-11, session 8 de la phase 2, 08:04-08:45)
- **Phase 2 en cours** : mission `PROMPT-PHASE-2.md` (lire aussi « Avant chaque vidéo : repartir de la phase 1 », « Leçons de méthode », « Passe de révision », étape 7). Démarrage de chaque session : `CLAUDE.md`.
- Session 8 : aucun retour neuf, boîte vide. **Vague 2 terminée** (*OSS 117* fini : bagarre du poulailler ; mesure coupes / parole tranchée sur spectrogramme) et **bilan définitif de la vague 2** dans `RAPPORT.md`.
- **Vague 3 lancée** : *The Social Network* (ouverture, Facemash, Henley ; fiche de phase 1 confrontée) et *Spotlight* (ouverture 1976, appels à Sipe en plans de 67 et 115 s, dispute, cartons de fin) ; comparaison des deux dans `analyses/films/spotlight.md`. Chaque fiche a sa liste « À faire ».
- **Méthode corrigée** : `coupes_parole.py` surestimait la parole (seuil « plancher + 10 dB », absurde sur une voix séparée) ; option `SEUIL=haut` et nouvel outil `labo/outils/spectro_coupes.py` (trancher à l'œil). « Coupes pendant la parole » ne distingue pas un style (30 % chez Fincher comme chez McCarthy) : mesurer plutôt les silences entre répliques. Les chiffres sur voix séparée de YouTube (POPCORN, Boxho, Imposteur) sont à refaire en passe de révision.
- Skills mis à jour en session 8 : `montage-rythme` (accélérer sur la courbe, pas sur la grille ; timing comique : borne haute), `montage-grammaire` (le débit vient des trous retirés ; dispute montée par l'échelle), `montage-son-et-emotion` (révélation par une voix hors champ, plan tenu), `montage-youtube` (chiffres marqués À REVOIR).
- Passes globales d'*Aftersun* et de *Spider-Verse* faites en fin de session 8 (détails ci-dessous). Ne pas modifier `passe_globale.sh` pendant qu'il tourne : zsh lit le script au fil de l'exécution (erreur « unmatched " » en fin de passe d'*Aftersun*, sans effet sur les résultats).
- **Aftersun : passe globale faite, courbes et couleur calculées** (`videos/_travail/aftersun/`) : au moins 553 plans, ASL 11,0 s, médiane 4,3 s, **-26,4 LUFS**. **Pièges attendus** : 150 « plans » de moins de 1 s, surtout aux minutes 44-47, 75, 90-91 et 100 (médiane 0,5 s) = **stroboscopes de la rave** (fausses coupes de lumière) ; « plans » de 210 s (7:03), 160 s (1:34), 272 s (1:37, sans doute le générique) = scènes sombres ou cartons à vérifier avec `verif_plan.py` et tuile. À confronter à `culture/aftersun-wells-mcclendon.md` : trois régimes d'image (35 mm / MiniDV / rave), plan sur la surface de l'eau, rave + « Under Pressure » en alterné, fin à l'aéroport, transitions par le son.
- **Spider-Verse : passe globale faite** (HDR10 AV1 via libdav1d, 13 min), courbes et couleur calculées, transcription Whisper `-mc 0` de la VO faite (`videos/_travail/spiderverse/transcription.srt`, 2 124 segments, 2 min ; aucune boucle : la ligne la plus répétée est « What? » ×12 ; Whisper note aussi des bruits entre astérisques, « *Gunshot* », « *more music* », utiles pour repérer l'action). Au moins 2 931 plans, ASL 2,9 s, médiane 1,96 s, -21,3 LUFS ; **566 « plans » de moins de 1 s** et une crête à 60 coupes/min (minute 2) : flashs et changements de style graphique probables, à trier à l'œil avant de citer.
- **Reprendre ici** : *Aftersun* (séquences ci-dessus) ; *Spider-Verse* (séquences) ; finir les « À faire » de *Spotlight* et *The Social Network* si le temps le permet ; puis **bilan de la vague 3** dans `RAPPORT.md`. Ensuite, passe de révision (étape 7).
- `.claude/settings.json` (ajouté par Diego) n'est pas commité : le garde-fou de l'agent refuse ce commit. À laisser à Diego.

## Chaîne d'analyse d'un film (sessions 1-2)
1. `ffprobe` : pistes audio et sous-titres, **et `color_transfer`** (si `smpte2084`, préfixer `HDR=1`). Puis `labo/outils/passe_globale.sh FILM videos/_travail/<nom> <piste audio VO> <sous-titre texte ou -1>` en arrière-plan (6 à 9 min). Sans sous-titres texte : `whisper-cli` sur l'audio 16 kHz.
2. `courbes_film.py` (crée `coupes.json`, rythme et volume) et `couleur_film.py` (couleur).
3. Repérer les scènes dans les sous-titres, puis `LUFS=M sequence.py DOSSIER DEBUT FIN sortie.png [colonnes] [largeur]` pour chaque séquence (planche < 500 Ko). Lancer les planches en parallèle (fonction shell : zsh ne découpe pas une commande rangée dans une variable).
4. Vérifier tout plan long cité : `verif_plan.py` + tuile ffmpeg `fps=1/2` (puis 3 à 6 images/s sur le passage douteux) ; regarder s'il s'agit d'un filé.
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
