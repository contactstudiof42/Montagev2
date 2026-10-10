# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 10, 2026-10-10 ~07:55 UTC)
- **Skills (21)** : session 10 : `montage-direction-artistique` (étape 0 inventaire des rushes, ralenti demandé sur 25 i/s, coupable désigné, dispositifs d'atelier recyclés ; annexe `signature-et-cartons.md`), `montage-rythme` (dilater par la durée : l'attente doit être habitée), `montage-grammaire` (décor chargé : couleur saturée derrière l'anomalie), `montage-workflows` (vitesses dans l'aller-retour, `verif_edl.py`, interpolation sur vrais plans), `montage-ia-generative` (RIFE sous le fondu sur eau/feuillage), `montage-references` (John Lewis).
- **Culture** : 43 fiches (nouvelles : `pub-emotionnelle-noel-john-lewis.md`, `dougal-wilson-kim-gehrig-pub.md`) ; `cliches-de-secteur.md` + ligne caritatif / personnes âgées.
- **Atelier** : **12 v8** (lieu encombré, v8c réf.), **15 « Deux sonneries de trop »** (A, B, C, D, B2 ; B2 = réf. : la main posée qui ne décroche pas), **16 « La fable »** v1-v3 (v4 à faire : la Terre coupée par le cadre pour ne plus lire « ballon »).
- **Labo** : `labo/workflows/vitesses/` + `labo/workflows/verif_edl.py` ; `labo/interpolation-reel/` (sous-agent, 2 plans CC0 Internet Archive, recontrôlé).
- **Examens** : n°1 13, n°2 14, n°3 15, n°4 14, n°5 14, **n°6 15** /20. **N°7 en session 13.**

## Reprendre ici (session 11)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy pillow scipy colour-science opentimelineio otio-fcp-adapter otio-cmx3600-adapter`.
2. Priorités : BACKLOG 57 (pièce 16 v4), 51 (teaser 15 s), 59 (fiche Dougal Wilson / Kim Gehrig), 15 suite (recadrages, nests, audio multipiste dans l'échange), 42 suite (`montage-references` en annexes : 90+ lignes), 1 (« direction A dans le noir »).
3. Pièges : **`pkill -f motif` tue le shell** → tuer par PID. Lancer les rendus longs avec `run_in_background` de l'outil Bash. Plans immobiles = une image. Wikimedia (upload.wikimedia.org) renvoie **HTTP 429** depuis la VM : passer par Internet Archive pour les médias CC0. **Ne jamais mettre d'identifiant personnel (e-mail) dans un User-Agent** (incident du sous-agent, session 10). Vérifier qu'un nom inventé ne recoupe pas une marque réelle (session 10 : « Allô Voisins »).
4. Sous-agents : 1 en session 10 (interpolation sur vrais plans) ; chiffres recontrôlés à la main (identiques).

## Environnement constaté
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
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
