# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 8, 2026-10-10 05:53 UTC)
- **Skills (21)** : session 8 : `montage-couleur-et-intention` (pièce 10 v4-v6 : cause « AgX » réfutée ; gélatine CTB, clé secondaire, peau = perte de chaleur, deux plans), `montage-grammaire` (casser l'axe avec un sens), `montage-workflows` (VFR et proxies testés), `montage-regard` (journal → `journal.md`, 12 règles distillées), `montage-references` (Scott Pilgrim, génériques de séries, drill FR), `montage-kinetic-editing`, `montage-expert`.
- **Culture** : 39 fiches (nouvelles : *Scott Pilgrim*, génériques de séries doc, clips drill / rap FR proches de Ziak).
- **Atelier** : **10 « Chaleur partout »** v1-v6 (+ montage 8 s ; v7 à faire : gros plan contre l'ombre) ; **11 « Dialogue »** v1-v4 (v4 = référence).
- **Labo** : `labo/vfr/` (cadence variable : −400 ms en lecture naïve, 0 ms après CFR), `labo/proxies/` (`-map 0:a` obligatoire).
- **Examens** : n°1 13, n°2 14, n°3 15, n°4 14, n°5 14 /20. **N°6 en session 10.**

## Reprendre ici (session 9)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy pillow scipy`.
2. Priorités : (pièce 10 close en v7) BACKLOG 47 « le fond raccorde » ; BACKLOG 33 (« inquiétude calme ») ; BACKLOG 42 suite (`montage-references` : annexes).
3. Pièges : **`pkill -f motif` tue le shell** → tuer par PID. Plans immobiles = une image. Viser une caméra par un point (`to_track_quat`). Ne pas couper un `for` de rendus avec `| head` (SIGPIPE arrête la boucle). Le paramètre `main` de `scene.py` (pièce 10) est la caméra portée ; la main/tête est `main_ecran` / `visage`. Concat ffmpeg d'images à durées libres : `option framerate 90000` + `-safe 0`.
4. Sous-agents : 3 en session 8 (fiches) ; revérification à la main : 2 chiffres confirmés, 2 corrigés (un sous-agent a mal mesuré une vignette) → **toujours recontrôler une mesure d'image faite par un sous-agent**.

## Environnement constaté
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 8 — 2026-10-10 05:29 → 05:53 UTC : pièce 10 v4-v6 (+ montage), pièce 11 « Dialogue » v1-v4, labos VFR et proxies, fiches Scott Pilgrim, génériques de séries doc, drill FR ; `montage-regard` distillé ; PLAN-TESTS 40-42.
- Session 7 — 2026-10-10 04:29 → ~05:10 UTC : examen n°5 (14/20), ateliers 08 « Souvenir » (v1-v4), 09 « Générique » (v1-v4) et 10 « Chaleur partout » (v1-v2), écart OCIO expliqué, labos photosensibilité, surround Lt/Rt, 180°, déterminisme Blender ; fiches Noé / Kan et Kuntzel + Deygas ; PLAN-TESTS 38-39.
- Session 6 — 2026-10-10 03:29 → ~04:05 UTC : fiches Aftersun et Les Revenants, recherche surround et hors champ (vérifiée en labo), atelier 07 « Causalité » (corps rigides, A/B/C), Eevee sans écran mesuré, PLAN-TESTS 36-37.
- Session 5 — 2026-10-10 02:29 → 03:05 UTC : atelier 05 « Trois étalonnages » (6 versions + scintillement), atelier 06 « Versions » (v1-v3), examen n°4 (14/20), API Resolve 19-21.1, fiches Elastic, ManvsMachine, Buck, Åkerlund, Gavras, état public des MCP (tests 21-32), AAF par familles.
- Session 4 — 2026-10-10 01:30 → 02:10 UTC : loudness hors plateformes, atelier 04 (v1-v4/v5), fondus 3/4, marqueurs XML, `montage-workflows` + OTIO, fiches Marker, Morris, Burtt, Rydstrom, vérification IA.
- Session 3 — 2026-10-10 00:30 → ~00:50 UTC : `montage-pilotage-mcp`, atelier 03 « rythme macro » (3 versions), labo fondus (résultat négatif), `montage-premiere`, fiches Varda et Jonze, examen n°3 (15/20), `montage-formats`.
- Session 2 — 2026-10-09 23:52 → 2026-10-10 00:30 UTC : pièce 02 « Étincelle » (6 versions), labo encodage, `montage-blender`, `montage-resolve`, fiches Murai et Honda « Cog », examen n°2 (14/20).
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
