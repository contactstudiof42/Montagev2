# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 13, 2026-10-10 ~11:03 UTC)
- **Skills (21)** : session 13 : `montage-direction-artistique` (clip : texte et corps, éprouvé en atelier 19), `montage-regard` (règle 19 : sens en contrepoint, espace en continuité), `montage-kinetic-editing` (3g : direction du filé à la coupe, testé en labo).
- **Culture** : 48 fiches (nouvelle : `culture/clips-illustrer-ou-contredire-paroles.md`, sous-agent).
- **Atelier** : **19 « Le texte et le corps »** v1-v4 (`atelier/19-texte-et-corps/`, B2 = réf. ; v4 « gestes » = échec documenté) ; 18 « Soustraction » (v3).
- **Labo** : `labo/kinetic/whip-flot/` (DIS puis vecteurs du codec ; validé sur rendus Blender) ; `labo/paroles/` (lisibilité des paroles incrustées par OCR ; `apt-get install tesseract-ocr tesseract-ocr-fra` : 20 s).
- **Examens** : n°1 13, n°2 14, n°3 15, n°4 14, n°5 14, n°6 15, n°7 15 /20. **N°8 en session 15 ou 16.**

## Reprendre ici (session 14)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy pillow scipy colour-science opentimelineio otio-fcp-adapter otio-cmx3600-adapter opencv-python-headless av`.
2. Priorités : BACKLOG 73 (scansion vers / coupe, mains lisibles), 75 suite (contour net, lecture en mouvement), 69 (extinction animée), 72 (plan-séquence : renverser mon tic), 67 (pièce 17 v6), 51 (teaser 15 s), 75 (paroles incrustées : drawtext / ASS).
3. Pièges : **`pkill -f motif` tue aussi le shell** → tuer par PID. **Plage limitée** : en `yuv*` / `gray16` lus par ffmpeg, le noir vaut 16 (×257). **PIL lit un PNG RGBA 16 bits en 8 bits**. **Remplacer du code par substitution Python : ne jamais placer un commentaire dans une ligne remplacée en milieu d'appel** (session 13 : SyntaxError, rendus vides, toujours lire le log Blender). Rendus longs : `nohup … &` + boucle d'attente. Cycles 480×270, 8 échantillons, rue simple : ~2,5 s/image. Wikimedia → HTTP 429 : passer par Internet Archive. Jamais d'e-mail dans un User-Agent.

## Environnement constaté
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
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
