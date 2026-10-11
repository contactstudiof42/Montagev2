# PROGRESS — état actuel

_Lire en premier. Seul l'état présent compte ici. La chaîne d'analyse, les outils et les règles ci-dessous servent à analyser toute nouvelle référence. L'état de clôture de la phase 1 est archivé dans `archives/phase-1/PROGRESS-cloture-phase-1.md`, et l'historique des sessions 1 à 25 dans `archives/phase-1/PROGRESS-historique.md`._

## PHASE 3 EN COURS (`PROMPT-PHASE-3.md`, sessions lancées par Diego seulement)
- Sessions 0 à 2 (2026-10-11) : bac à sable Resolve ; projet Sony V2 (50 %), comparaison avec Claude nu, V3 (65 %). Fichiers V2 et V3 archivés dans `archives/phase-3/sony-linkbuds/`.
- **Session V4 (2026-10-11, 16:24-17:45)** : retours de Diego sur la V3 intégrés, plus trois consignes dictées (Gyroflow = mouvement fluide ; fixe ou rail selon l'intention du cadreur ; jamais deux fois le même moment d'un rush). **V4 rendue** : `videos/phase-3/sony-linkbuds/rendus/sony_linkbuds_V4.mp4` (44,6 s, HEVC Main 10 39 Mb/s, −14,0 LUFS, −1,1 dBTP, photosensibilité OK, 0 doublon), timeline **`SONY_V4`** du projet `P3-sony-linkbuds-agent`, enregistré. Documents : `plan.md`, `look.md`, `autocritique.md`, `note-de-livraison.md`, `journal.md` (gestes 41-56), `sfx.md`. Nouveaux outils : `labo/outils/stabiliser.py` (fixe / rail), `appliquer_stab.py`, `doublons_timeline.py`, `tremblement.py --avant --bande`, `labo/couleur/look_sony_v4.py` (+ `oklab.py`, `banc_look.py`, `planche_look4.py`), `labo/outils/phase3/v4/` (`detourage.py`, `collage.py`, `sfx_prep.py`, `partition_sfx.py`, `gen_ouverture.py`, `bande_rush.py`). LUT : `LUT/P3/P3_sony_look_V4_{salle,jour,rouge,rouge_negatif}.cube`.
- V4 notée **80 % livrable** par Diego ; ses notes et consignes sont dans `RETOURS-DIEGO.md` (sections du 2026-10-11 « notes sur la V4 » à « Rien n'est figé »).

## V5 EN COURS — arrêtée proprement le 2026-10-11 vers 19:35 (Diego a repris Resolve pour un autre projet)
**Où reprendre** : projet Resolve `P3-sony-linkbuds-agent`, timeline **`SONY_V5`** (dupliquée de `SONY_V4`, qui reste intacte), enregistrée. Aucun rendu V5 complet n'existe encore.

**Fait (commité)** :
1. Consignes de Diego commitées ; **carnet de goût** créé (`CARNET-DE-GOUT.md`, 18 entrées dont 16 illustrées dans `carnet/`, portée de chacune) ; règles [universel] dans `montage-regard` (§ « Le goût de chaque plan », points 1-13), [genre] dans `montage-kinetic-editing`.
2. **Direction artistique** : `projets-phase-3/sony-linkbuds/da.md` (11 références dans `da/`, gardées hors Git : images de tiers ; sources citées).
3. **Référence du dernier pic** : `analyses/reseaux/foebusdelapaz-nike-basket.md` (image par image ; passage retenu 0-4 s, Diego n'avait pas précisé les bornes), inscrite dans `REFERENCES.md`, carnet 18.
4. **Outils** : `labo/outils/controle_plans.py` (passage exact : 3 images par plan, netteté, exposition, visages image par image en tuiles carrées) ; `detourage_modeles.py` + `controle_detourage.py` (BiRefNet portrait retenu, comparé à 3 modèles) ; `gyro_sync.py` (corrélation gyroscope / image, décalage), `gyro_rendu.py` (rendu Gyroflow à décalage imposé et vérifié ; convention : offset Gyroflow = − décalage mesuré), `residu_lk.py` ; `labo/couleur/look_sony_v5.py` ; `labo/outils/phase3/v5/collage_v5.py`, `pic_v5.py`.
5. **Dans `SONY_V5`** : LUT V5 sur les 83 plans (`LUT/P3/P3_sony_look_V5_{salle,jour,rouge,rouge_negatif,salle_negatif}.cube` = V4 + pied de courbe t 0,05) ; **ouverture** plus rapide (zoom E → KORE en 5 images, KORE tenu 48-60, salut 60-83, allée 83-117) ; **remplacements** : 117 C6507 @39 s (au lieu du panoramique flou C6506), 129 C6507 Gyroflow synchronisé, 205 C6637 @2,5 s et 226-231 C6626 (les deux C6624 « tête bizarre » retirés), 305→ C6589 / 293-305 C6580 (le tapis C6590 retiré), 375 C6585 (au lieu de C6571), 431 C6587 @25,2 s net, 455 C6584 (au lieu de C6571), 497-521 C6566 continu (**pas de collage B** : variantes B1/B3/B4 sans raison ni force) ; **collage A1** à 281-293 (sur son image figée en noir et blanc, C6580 glisse depuis le bas, elle disparaît par balayage ; variantes A2, A3 écartées) ; **collage C1** à 678-686 (tête positive, le monde en négatif ; C2 réservé au pic, C3 = effet de cadre) ; **packshots** : rendus Gyroflow synchronisés sans correction rail (948 C6725_gf_s0, 972 C6723_gf_s12, 995 C6723_gf_s27) dans `videos/phase-3/sony-linkbuds/_travail/gyroflow/v5/` (preuves `*_preuve.json`, mesures `sync_*.json`).
6. **Dernier pic rendu hors Resolve** (pas encore posé) : `videos/_travail/sony_v5/pic/pic_v5.mov` (117 images, 831-948) + `pic_v5_planche.jpg` + `pic_v5_sources.json` (sources pour le contrôle des doublons). Pas encore regardé ni contrôlé (photosensibilité !).

**Reste à faire, dans cet ordre** :
1. Regarder `pic_v5_planche.jpg`, corriger, puis le poser dans `SONY_V5` à 831-948 en supprimant C6674 (831), C6672 (854), C6669 (878), C6566 (925) ; `flash_check.py` sur la plage (≤ 3 flashs/s, attention aux négatifs et seuils de P2/P4).
2. **Étalonnage plan par plan** : les CDL ont sauté sur tous les plans remplacés ou reposés (ancien tableau : `projets-phase-3/sony-linkbuds/v5/cdl_V4.json`). À régler : ouverture (K −0,023, O −0,031, R −0,038, E et zoom −0,046, KORE large −0,065) ; C6581 (398, surexposé) ; C6661 (789, dos brûlé) ; packshots plus sombres que −0,081 (comparer à la photo produit Sony) ; noirs denses partout ; grain V5 (piste 5, 35 %) à réduire.
3. **Inversions en plus** : remplacer les flashs blancs du drop 233-235 et du drop rouge 690-692 par des inversions (LUT `salle_negatif` / `rouge_negatif`).
4. **SFX** : chaque transition a son son (liste des transitions contre la liste des sons), sons à revoir aux endroits modifiés (ouverture, collages A et C, bloc 4, pic, packshots) ; SFX déjà téléchargés seulement.
5. **Contrôles avant rendu** : `doublons_timeline.py` (ajouter les plages Gyroflow v5 et les sources du pic / des collages), `controle_plans.py` sur un rendu (visages, flous, remplissage), relecture du film entier d'un œil neuf (règle « rien n'est figé »), carnet relu entrée par entrée.
6. Rendu V5 (H.265 Main 10, comme la V4), QC, `autocritique.md`, `note-de-livraison.md` (méthode Gyroflow plan par plan avec preuves ; ce qui a bougé hors des retours ; ce que Diego doit écouter), `journal.md`, `plan.md` V5 (genre en tête, variantes et pourquoi), PROGRESS, RAPPORT.

**Retours de Diego pas encore appliqués** : couleur plan par plan, noirs, surexpositions (16-17 s, écouteurs de fin, large KORE) ; son sur chaque transition ; inversions « un peu plus » ; dernier pic (rendu, pas posé) ; preuve Gyroflow écrite dans la note (mesures faites : C6507 −34 ms → 4 ms résiduels, C6723 −2 et 6 ms ; plans fixes K-O-R-E et C6725 : synchro non mesurable, mouvement trop faible ; l'autosynchronisation de la ligne de commande ne laisse aucune trace : non prouvable pour la V4).
**Doutes notés** : `tremblement.py` (corrélation de phase) et `residu_lk.py` ne sont pas fiables sur le tapis en carbone et les bascules de point ; les dernières phrases de deux messages de Diego étaient coupées ou incomplètes (liste des flous ratés ; bornes de la référence).
- Accords de Diego : mes LUT dans `LUT/P3/` seulement ; Artlist via Chrome (62 SFX sur 100 le 2026-10-11) ; fichiers Gyroflow `_stabilized*` dans `SONY copy/RUSH/` ; il a autorisé l'arrêt forcé de Resolve figé le 2026-10-11 (accord ponctuel, à redemander).
- Pièges à ne pas refaire (détail `montage-resolve`) : `comp.Lock()` casse le rendu des clés ; ne jamais lire les entrées d'un effet IA OpenFX (Resolve figé) ; `AppendToTimeline` d'un rush avec son : `"mediaType": 1` ; `SetTrackEnable` sur la page Montage seulement, relire avant le rendu ; Gyroflow : autosync sur plage courte, la sortie d'une plage garde le timecode du rush ; `ExportCurrentFrameAsStill` exporte le plan du dessus.

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
