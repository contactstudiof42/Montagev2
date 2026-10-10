# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 15, 2026-10-10 ~13:15 UTC)
- **Skills (21)** : session 15 : `montage-direction-artistique` (texte = durée, « la technique du matin »), `montage-kinetic-editing` (R7b temps de lecture ; §6 rushes à strobe, 128 BPM noires = limite, sommet plus long pas plus fort), `montage-regard` (règle 21 : le texte prend la valeur opposée à l'image ; dispositif automatique), `montage-son-et-emotion` (13 : son d'un strobe), `montage-motion-design-principes` (6b : carton-liste en lecture de repérage).
- **Culture** : 50 fiches (nouvelle : `culture/step-printing-wong-kar-wai-et-autres.md`).
- **Atelier** : pièce 20 « La lumière écrit » v1-v7 (`atelier/20-la-lumiere-ecrit/`) ; pièce 18 v6 confiée à un sous-agent (voir le journal du RAPPORT pour l'état).
- **Labo** : `labo/photosensibilite/strobe-rushes/` (rushes à strobe : saccade choisie = seul traitement qui garde le coup) ; `labo/paroles/temps_lecture.py`.
- **Examens** : n°1 13, n°2 14, n°3 15, n°4 14, n°5 14, n°6 15, n°7 15, n°8 15 /20. **N°9 vers la session 18** (BACKLOG 85 : sans musique).

## Reprendre ici (session 16)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy pillow scipy colour-science opencolorio OpenEXR opentimelineio otio-fcp-adapter otio-cmx3600-adapter opencv-python-headless av`.
2. Priorités : 80 (pièce 20 v8 : traînée + lasers + 20 noms variés) ; 77 si la v6 de la pièce 18 n'est pas close ; 76 (rig à coude) ; 84 (vrai rush strobe CC0) ; 83 (fiche chronophotographie) ; 72 ; 51.
3. Pièges : **`pkill -f motif` tue aussi le shell** → tuer par PID. **Plage limitée** : en `yuv*` / `gray16` lus par ffmpeg, le noir vaut 16 (×257). **PIL lit un PNG RGBA 16 bits en 8 bits**. **Commentaire au milieu d'une ligne remplacée = code désactivé** : commentaire sur sa propre ligne. **OpenCV pip ne lit pas l'EXR** : `OpenEXR`. Vue AgX hors Blender : `PyOpenColorIO` + config de Blender. Wikimedia → HTTP 429 : Internet Archive. Jamais d'e-mail dans un User-Agent. **Session 15** : `exec` d'un script qui lit `sys.argv` écrase les variables (réassigner après) ; **vérifier les listes de textes contre les doublons** ; `loudnorm` une passe sur 10 s à kicks reste à -18 LUFS : boucle R6 ; une moyenne de 8 poses à 1/25 s fait des **fantômes discrets**, pas un flou (sous-échantillonner) ; rendu numpy à 32 sous-poses par image : ~5 min pour 10 s.

## Environnement constaté
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
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
