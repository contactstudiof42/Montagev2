# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Consigne durable de l'utilisateur (2026-10-10)
- Développer une **culture YouTube / internet** (divertissement, essai vidéo, vulgarisation, vlog, motion de chaîne, Shorts, cultures d'edit) au même niveau que cinéma et clip. Voir BACKLOG « Consigne » (Y1-Y6) : une part de chaque session jusqu'à parité.

## Où on en est (après la session 25, 2026-10-10)
- **Session 25** (20:29 → 21:04 UTC) : veille IA (rien de neuf) ; **pièce 34 « De dehors »** v1-v6 (maquette de la direction B de l'examen n°13 ; v6 = recommandée : buée + poussée lente + lanterne, sans coupe dedans) ; **labo micro-sauts** (`labo/micro-sauts/`, vérité terrain 8/8) ; **pièce 31 v4-v4d** (figure articulée : axe de lecture d'une posture ; focale = 4e levier ; diptyque animé, la visée monte avec la caméra) ; micro-sauts par zones et jusqu'à ×3 ; pièce 34 v7 (îlot de lumière) ; fiches live YouTube (enrichie) et Haneke (sous-agents). Examens : … n°13 14. Prochain examen n°14 vers la session 27 (documentaire ou clip).

## Reprendre ici (session 26)
0. Relever `date -u`, clôturer à début + 45 min. Veille IA (sous-agent). `python3 -m pip install -q numpy pillow` ; `apt-get install -y espeak-ng` ; Blender 4.2.3 : `curl -sSL -o /tmp/blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf /tmp/blender.tar.xz -C /tmp` (27 s).
1. Y41 reste : le corps qui bouge (danse) et le son ; Y52 (pièce 34 v8, mouvement continu) ; Y49 (laisser chercher, Haneke). Commande escalier : `blender -b -P atelier/31-meme-escalier/scene_v4.py -- OUT.png froid|chaud haute|basse voute|ouvert v2 az=DEG [murfou] [lens=MM]`.
2. Y40 (main qui motive la coupe cachée), Y39 (pièce 29 en 9:16), Y43, Y35 ; pièce 34 : un vrai modèle de voiture et la buée animée par matériau (phase 2 via MCP, PLAN-TESTS 75).
3. Commandes pièce 34 : `blender -b -P atelier/34-de-dehors/scene.py -- OUT.png ext|int [lampe] [phares] [buee] [hd]` ; `python3 atelier/34-de-dehors/montage.py v6 atelier/rendus/34` (60 s) ; `mesure.py`.

## Où on en est (après la session 24, 2026-10-10)
- **Session 24** (19:29 → 20:02 UTC, horloge relevée à chaque commit) : labo `labo/outils/coupes.py` (EDL avec fondus / OTIO / XML FCP7 / scdet ; bande-film avec son ; activité nette du grain) et `tempos.py` ; pièce 29 « Deux horloges » v1-v9 (Interstellar ; v9 jonction = recommandée, v7 pudique) ; pièce 30 « Coupe cachée » A-H (Short 9:16, Zach King) ; pièce 31 « Le même escalier » v1-v3 (Joker, Blender) ; pièce 32 « Trois façons » (Short, LaBelle : le cadre est la règle graduée) ; pièce 33 « Voix écrite après » (Varda) ; sous-agents : veille IA (rien de neuf), fiches Shorts narratifs et montage alterné ; montage-regard 26-28. **Examen n°13 fait (fiction, 14/20).** Examens : … n°12 14, n°13 14. Prochain examen n°14 vers la session 27 (documentaire ou clip).

## Reprendre ici (session 25)
0. Relever `date -u` au début, clôturer à début + 45 min. Veille IA (sous-agent). `python3 -m pip install -q numpy pillow opentimelineio otio-fcp-adapter` (17 s) ; Blender 4.2.3 : `curl … && tar xf` (27 s), 9 s par image fixe Cycles 480×270 32 éch.
1. Y47 (maquette de la direction « de dehors » de l'examen n°13 : 2 min de plan fixe, voix filtrée, mesurer le décrochage), Y48 (fiche réactions tenues dans le drame, sous-agent).
2. Puis Y41 (escalier : figure articulée), Y40 (coupe cachée : flou de bougé, boucle), Y39 (pièce 29 en 9:16 alterné, tempo 1,24 s).
3. Outils : `python3 labo/outils/coupes.py VIDEO --edl X.edl [--xml X.xml] [--otio X.otio] --scdet 10 --sortie P` (bande-film + courbe + JSON) ; `labo/outils/tempos.py` ; mesure de raccord `atelier/30-coupe-cachee/mesure.py`.

## Où on en est (après la session 23, 2026-10-10)
- **Session 23** (18:29 → 18:34, clôture prématurée relevée par l'utilisateur, reprise 18:44 → 19:07 UTC) : veille IA (Vidu Q4 Preview), pièce 27 « Jamais » v1-v4 (gag de contradiction, règle de trois, silence-gag), fiche timing comique sitcom, **examen n°12** (pub opticien, 14/20), pièce 28 « Flou → net » v1-v3 (Blender : flou optique / gaussien, courbe de bascule, reflet par la lumière). Examens : … n°11 15, **n°12 14**. Prochain examen n°13 vers la session 26 (fiction courte).

## Reprendre ici (session 24)
0. **Relever `date -u` au début et clôturer à début + 45 min, pas avant** (l'horloge est juste). Veille IA du jour (sous-agent). `python3 -m pip install -q numpy pillow` ; Blender : `curl -sSL -o /tmp/blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf …` (45 s).
1. Y38 (pièce 28 en mouvement), Y35 reste (lecture du visage, son), Y25 reste (larges dans le noir), Y29 (bande.py général), Y23/Y26 ; examen n°13 (Y37) vers la session 26.
2. Fait en fin de session 23 : Y22 (pièce 25 v4, G = réf.), Y25 en partie (pièce 26 v5), Y32 (fiche pubs), Y36 (montage-regard 23-25, sommaire montage-expert).

## Ancien point (après la session 22, 2026-10-10)
- **Session 22** (lancée par l'utilisateur, « feu vert », après un arrêt de l'anti-doublon : la session 21 avait commité 2 min avant) : veille IA (sous-agent : seul nouveau, Suno Speech bêta et Studio), fiche **gags de montage** (Y21, sous-agent), **pièce 26 « Densité décroissante »** (Y20, v1-v4, v4 = réf.). Examens : … n°11 15. Prochain examen n°12 vers la session 24-25 (Y24, pas YouTube).

## Reprendre ici (session 23)
0. Veille IA du jour (Y11, sous-agent dès le démarrage). `pip install numpy pillow` (9 s).
1. **Y27** atelier « un gag de montage » (écarts en images, réaction tenue, silence-gag) ; **Y25** pièce 26 v5 (flamme 3-5 %, couper vers la lumière) ; Y22 (pièce 25 v4), Y16, Y9.
2. Pièce 26 : `python3 atelier/26-densite-decroissante/piece.py v4 atelier/rendus/26` (~80 s) puis `mesure.py` (16 s par version).
3. **L'horloge de la VM est FIABLE (vérifié session 23 par l'utilisateur : `date` = heure réelle).** L'ancienne note « horloge peu fiable » était fausse et a fait finir les sessions 16 à 23 après 5 à 20 min au lieu de 50. Règle : relever `date -u` au début, le relire avant chaque clôture, et ne clôturer qu'à début + 45 min. Mon estimation du temps au ressenti surestime la durée d'un facteur 3 à 8.

## Ancien point (après la session 21, 2026-10-10)
- **Session 21** : examen n°11 (Y10, divertissement YouTube de groupe, 15/20), labo `labo/youtube/densite.py` (courbe d'événements/min, vérité terrain 3/3 ; la relance doit être un pic), sous-agents : veille IA (rien de neuf), fiche slow TV / ASMR (Y18). Examens : … n°10 15, **n°11 15**. Prochain examen n°12 vers la session 24-25 (sujet non YouTube : fiction ou pub, pour équilibrer).

## Reprendre ici (session 22)
0. Veille IA du jour (Y11, sous-agent dès le démarrage). `pip install pillow` (4 s) suffit pour `densite.py`.
1. **Y20** maquette « densité décroissante » (3 min compressées du découpage B de l'examen n°11, plans Blender simples ou formes, avec la correction « relance = pic ») : la regarder et juger si ça décroche ; mesurer avec `densite.py`.
2. **Y21** fiche « gags de montage » (sous-agent) ; **pièce 25 v4** (2 plans, une seule direction lente, d'après la fiche slow TV) ; Y16 (pièce 24 v4) ; Y9.

## Ancien point (après la session 20, 2026-10-10)
- **Session 20** : pièce 24 « Face caméra » (Y4, v1-v3, F = réf.), pièce 25 « Au lit » (Y14, v1-v3, E = réf.), labo écho de poses (88), sous-agents : veille IA, infrarouge sourcé (Y15), Resolve et saccade choisie (90), affiches de festivals (89). Examens : … n°10 15. **Prochain examen n°11 en session 21 ou 22** (Y10 : divertissement YouTube).

## Reprendre ici (session 21)
0. Veille IA du jour (Y11, sous-agent dès le démarrage). Livrables 89 (affiches de festivals) et 90 (Resolve retime) commités en session 20.
1. **Examen n°11 (Y10, divertissement YouTube)** ; puis Y9 (une nuit sans musique), Y7 (pièce 21, autre matière), 87 (pièce 20 v10 son), Y13 (pièce 22 noir + douche).
2. Pièce 24 v4 : REC éteint **sur le mot « rien »** ; version 9:16 ; reprendre la règle « ne pas faire de jump cut sur moins de ~0,5 s retirée » sur un vrai rush (phase 2). Pièce 25 : voix qui s'arrête vers 45 s, version téléphone en mode nuit.
3. Outils réutilisables créés : `atelier/24-face-camera/planche.py` (paires avant / après chaque coupe, type d'événement), `atelier/25-au-lit/mesure.py` (YAVG + LUFS court terme par 5 s + bande-film), `labo/echo/echo.py`.

## Ancien point (après la session 19)
- **Session 19** : veille IA (sous-agent, Y11 fait pour ce jour), pièce 22 v3-v5 (plafond AgX → blanc au grade ; plan final ; variante noire ; B3 ; v4 chaise isolée par l'espace ; v5 colonne de la lignée), **examen n°10** (15/20, vulgarisation sommeil), pièce 23 « Infrarouge de nuit » v1-v3. Examens : … n°9 14, **n°10 15**. Prochain examen vers la session 22-23 (Y10 : divertissement YouTube).

## Reprendre ici (session 20)
0. Veille IA du jour (Y11, sous-agent en arrière-plan dès le démarrage). Puis : Y4 (atelier face caméra), Y7, Y8 ; pièce 22 v6 (variante noire sur la base v5 avec douche de lumière sur la silhouette ; moiré ; commande exacte : `blender -b -P scene.py -- OUT 48 --v3 --v3b --v4 --v5 --x0 1.6 [--noir]`, puis `montage.py B3` et courbe de point blanc ffmpeg, voir CRITIQUE) ; pièce 23 v4 si utile (dormeur moins schématique, une voiture qui passe = mouvement interne d'un plan long) ; vérifier le chiffre « dormeurs simultanés » de l'examen n°10.

## Après la session 18
- **Session 18** : pièce 22 « Cent dix-sept milliards » (à la manière d'EGO, Blender + voix espeak, versions A explicatif / B EGO / v2), fiche `culture/createurs-ia-video-2025-2026.md`, **mise à jour de l'IA générative au 2026-10-10 demandée par l'utilisateur** (sous-agent : `montage-ia-generative/etat-de-l-art-2026-10.md`, `sources/ia-generative-2026-10-10.md`) ; PLAN-TESTS 64.

## État après la session 17
- **Skills (22)** : nouveau `montage-youtube` (grammaire du long format par genre, contraste cinéma / clip, specs officielles, miniatures testées à l'œil) ; session 17 aussi : `montage-motion-design-principes` (l'objet qui change de rôle, seuil du mouvement de repos), `montage-references` (§ G YouTube et internet), `montage-formats` (YouTube long), `montage-direction-artistique` (sans musique : le son-refrain), `montage-expert` (sommaire, consigne).
- **Culture** : ~63 fiches, dont **12-15 YouTube / internet** (session 17 : MrBeast et rétention, divertissement FR, essai vidéo, doc explicatif Vox / Johnny Harris, vulgarisation FR, Kurzgesagt, motion de chaîne, vlog, cultures d'edit ; 2e vague : gaming / Twitch, podcasts vidéo, YouTube musique, animation en ligne, critique de cinéma FR).
- **Atelier** : pièce 21 « L'objet qui change de rôle » (A / B / C / B v2).
- **Labo** : `labo/youtube/` (validateur de chapitres testé ; banc de miniatures : OCR inutilisable, jugement à l'œil sur planche 168 px).
- **Examens** : n°1 13, n°2 14, n°3 15, n°4 14, n°5 14, n°6 15, n°7 15, n°8 15, **n°9 14** /20. N°10 vers la session 20 (Y10 : divertissement YouTube).

## Reprendre ici (session 19)
0. **Consigne durable (2026-10-10)** : l'état de l'art IA doit rester à jour à la date du jour ; à chaque session, une recherche web « nouveautés IA vidéo des 7 derniers jours » et mise à jour datée de `etat-de-l-art-2026-10.md`. Pièce 22 : v3 (variante `--noir`, nappe qui monte au lieu du silence), puis examen n°10 (brief de vulgarisation au rendu cinéma, Y0).

## Ancien « reprendre ici » (session 18)
1. Démarrage normal. `python3 -m pip install -q numpy pillow scipy` (25 s) ; `apt-get install -y tesseract-ocr tesseract-ocr-fra espeak-ng` (15 s) si besoin ; Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz` (30 s).
2. Priorités : **consigne YouTube** (Y4 atelier face caméra, Y7 pièce 21 autre matière, Y8 densité de coupes, Y9 nuit sans musique, Y5 restant : créateurs IA 2025-2026) ; 87 (pièce 20 v10) ; 88 ; 76 ; 84.
3. Pièges : **`pkill -f motif` tue le shell appelant, et `pgrep -f motif` dans une boucle `until` se trouve lui-même** → tuer et attendre par PID. **Une commande lancée avec `&` survit à la fin de l'appel Bash** : utiliser `run_in_background`. **tesseract multi-fils** : `OMP_THREAD_LIMIT=1` (0,17 s par image au lieu de blocages). L'OCR ne mesure pas la lisibilité d'une miniature (non monotone avec la taille) : juger à l'œil sur planche. Plage limitée en `yuv*` (noir = 16). PIL lit un PNG 16 bits en 8 bits. helpx.adobe.com et support.google.com : WebFetch passe pour Google, pas pour Adobe (403). `piece.py` (pièce 20) lit `argv[3]` = sous-poses.

## Environnement constaté
- **YouTube bloqué depuis la VM (testé session 22, à la demande de l'utilisateur)** : recherche yt-dlp OK (titres, durées, vues), mais lecture refusée (429 puis « Connectez-vous pour confirmer que vous n'êtes pas un robot »), y compris dans Chromium/Playwright : c'est l'IP de datacenter. Ne pas contourner (pas de cookies de compte). La page reste lisible : miniatures et titres analysables par capture. Décision de l'utilisateur : **analyse de vraies vidéos en phase 2** (Mac) ; d'ici là, seulement par lien de fichier (Dropbox, Drive, WeTransfer joignables) si l'utilisateur en fournit.
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 25 — 2026-10-10 20:29 → 21:04 UTC : veille IA ; pièce 34 (v1-v6) ; labo micro-sauts ; pièce 31 v4-v4b ; fiches live YouTube et Haneke (sous-agents) ; skills regard, rythme, direction-artistique, preparation-tournage-vfx, youtube, references, expert ; PLAN-TESTS 75.
- Session 24 — 2026-10-10 19:29 → 20:02 UTC : coupes.py, tempos.py ; pièces 29 (v1-v9), 30 (A-I), 31 (v1-v3), 32, 33 ; fiches Shorts narratifs et montage alterné (sous-agents) ; veille IA ; skills rythme, references, youtube, preparation-tournage-vfx, couleur-et-intention, regard, expert ; PLAN-TESTS 73-74.
- Session 23 — 2026-10-10 18:29 UTC → 18:34 (clôture prématurée, corrigée sur remarque de l'utilisateur), reprise 18:44 → 19:07 UTC : veille IA (sous-agent), pièce 27 « Jamais » v1-v2, bande.py ; montage-rythme ; PLAN-TESTS 71.
- Session 22 — 2026-10-10 17:38 UTC → ~18:20 réel (horloge VM ~17:50) : veille IA, fiche gags de montage (sous-agents), pièce 26 v1-v4 ; skills youtube, rythme, son-et-emotion, ia-generative ; PLAN-TESTS 69.
- Session 21 — 2026-10-10 17:29 UTC → fin (horloge peu fiable) : examen n°11 (15/20), labo densite.py, sous-agents veille IA / fiche slow TV-ASMR ; skills direction-artistique, youtube, references, ia-generative.
- Session 20 — 2026-10-10 16:29 UTC → fin (horloge peu fiable) : pièces 24 (face caméra) et 25 (au lit), labo écho, sous-agents veille IA / infrarouge / Resolve retime / affiches de festivals ; skills youtube, rythme, couleur-et-intention, motion-design-principes, preparation-tournage-vfx, ia-generative ; PLAN-TESTS 67.
- Session 19 — 2026-10-10 15:29 → ~16:00 UTC (horloge peu fiable) : veille IA (sous-agent), pièce 22 v3, examen n°10 (15/20), pièce 23 v1-v3 ; skills blender, couleur-et-intention, direction-artistique, youtube, preparation-tournage-vfx, ia-generative.
- Session 18 — 2026-10-10 14:54 → ~15:40 UTC (horloge VM peu fiable ; relancée par l'utilisateur après un faux positif de l'anti-doublon) : pièce 22 v1-v2, fiche créateurs IA, MAJ IA générative au 2026-10-10 (sous-agent) ; skills references / youtube / motion-design-principes / blender ; PLAN-TESTS 64.
- Session 17 — 2026-10-10 13:41 → ~14:15 UTC : consigne YouTube de l'utilisateur ; 9 + 5 fiches YouTube / internet (sous-agents), skill `montage-youtube`, specs officielles YouTube, labo `labo/youtube/` (chapitres, miniatures), pièce 21 « L'objet qui change de rôle », examen n°9 (14/20) ; PLAN-TESTS 63.
- Session 16 — 2026-10-10 13:30 UTC → (horloge VM peu fiable) : pièce 20 v8 / v8-uniforme / v9 (hiérarchie d'une liste, sections calées sur la barre), fiche chronophotographie Marey / Muybridge (sous-agent), recherche saccade choisie Premiere / AE (sous-agent) ; PLAN-TESTS 61-62.
- Session 15 — 2026-10-10 12:30 → ~13:15 UTC : examen n°8 « Nuit Basse » (15/20), labo rushes à strobe, pièce 20 « La lumière écrit » v1-v7, fiche step-printing, sous-agents (vitesse de lecture FR vérifiée ; son d'un strobe et lecture de repérage ; pièce 18 v6) ; PLAN-TESTS 58-60.
- Session 14 — 2026-10-10 11:29 → ~12:00 UTC : pièce 18 v4-v5 (extinction animée par passes EXR), pièce 19 v5-v8 (gestes), labo paroles ASS mot à mot, fiche monteurs d'edits (sous-agent) ; PLAN-TESTS 57.
- Session 13 — 2026-10-10 10:30 → ~11:03 UTC : pièce 19 « Le texte et le corps » (v1-v3), labo flot optique à la coupe (sous-agent + validation Blender), labo paroles incrustées (OCR), fiche « illustrer ou contredire les paroles » ; PLAN-TESTS 54-56.
- Session 12 — 2026-10-10 09:29 → ~10:15 UTC : examen n°7 « Heure creuse » (15/20), labo noir protégé (pièce 17 en 16 bits, fixe / panoramique), pièce 18 « Soustraction » v1-v3, fiche Natasha Braier (sous-agent) ; PLAN-TESTS 52-53.
- Session 11 — 2026-10-10 08:30 → 08:56 UTC : pièce 16 v4, pièce 17 « dans le noir » (v1-v4), fiches Willis et Young / van Hoytema, labos recadrages / nests / audio dans l'échange (sous-agent) et bercement AE (phase intégrée) ; écrans dans le champ ; PLAN-TESTS 48.
- Session 10 — 2026-10-10 07:30 → ~07:55 UTC : examen n°6 (15/20), pièce 12 v8, pièce 15 « Deux sonneries de trop », fiche John Lewis, labos vitesses dans l'échange + vérificateur d'EDL, interpolation sur vrais plans CC0 (sous-agent) ; PLAN-TESTS 46-47.
- Session 9 — 2026-10-10 06:29 → 07:05 UTC : pièces 12 (v1-v7), 13 (v1-v4), 14 (A/B) ; labos interpolation (minterpolate, RIFE) et saillance (résidu spectral) ; fiches bande-annonce, Freeze Corleone ; PLAN-TESTS 43-45.
- Session 8 — 2026-10-10 05:29 → 05:53 UTC : pièce 10 v4-v6 (+ montage), pièce 11 « Dialogue » v1-v4, labos VFR et proxies, fiches Scott Pilgrim, génériques de séries doc, drill FR ; `montage-regard` distillé ; PLAN-TESTS 40-42.
- Session 7 — 2026-10-10 04:29 → ~05:10 UTC : examen n°5 (14/20), ateliers 08 « Souvenir » (v1-v4), 09 « Générique » (v1-v4) et 10 « Chaleur partout » (v1-v2), écart OCIO expliqué, labos photosensibilité, surround Lt/Rt, 180°, déterminisme Blender ; fiches Noé / Kan et Kuntzel + Deygas ; PLAN-TESTS 38-39.
- Session 6 — 2026-10-10 03:29 → ~04:05 UTC : fiches Aftersun et Les Revenants, recherche surround et hors champ (vérifiée en labo), atelier 07 « Causalité » (corps rigides, A/B/C), Eevee sans écran mesuré, PLAN-TESTS 36-37.
- Session 5 — 2026-10-10 02:29 → 03:05 UTC : atelier 05 « Trois étalonnages » (6 versions + scintillement), atelier 06 « Versions » (v1-v3), examen n°4 (14/20), API Resolve 19-21.1, fiches Elastic, ManvsMachine, Buck, Åkerlund, Gavras, état public des MCP (tests 21-32), AAF par familles.
- Session 4 — 2026-10-10 01:30 → 02:10 UTC : loudness hors plateformes, atelier 04 (v1-v4/v5), fondus 3/4, marqueurs XML, `montage-workflows` + OTIO, fiches Marker, Morris, Burtt, Rydstrom, vérification IA.
- Session 3 — 2026-10-10 00:30 → ~00:50 UTC : `montage-pilotage-mcp`, atelier 03 « rythme macro » (3 versions), labo fondus (résultat négatif), `montage-premiere`, fiches Varda et Jonze, examen n°3 (15/20), `montage-formats`.
- Session 2 — 2026-10-09 23:52 → 2026-10-10 00:30 UTC : pièce 02 « Étincelle » (6 versions), labo encodage, `montage-blender`, `montage-resolve`, fiches Murai et Honda « Cog », examen n°2 (14/20).
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
