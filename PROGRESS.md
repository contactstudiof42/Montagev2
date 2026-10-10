# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 16, 2026-10-10)
- **Skills (21)** : session 16 : `montage-premiere` (saccade choisie : Frame Hold Options, Frame Sampling, Posterize Time, Echo obsolète en 26.0), `montage-after-effects` (expression tableau sur Time Remap, Frame Blending off), `montage-motion-design-principes` (deux grammaires de la trace ; 6c hiérarchiser une liste = économiser des coups, sections calées sur la barre), `montage-references` (11b Marey).
- **Culture** : 51 fiches (nouvelle : `culture/chronophotographie-marey-muybridge.md`).
- **Atelier** : pièce 20 v8 (écho + 20 noms hiérarchisés), v8-uniforme (témoin), v9 (sections calées, carton 6 s) : `atelier/20-la-lumiere-ecrit/v8-planche.png`, `v8-uniforme-planche.png`, `v9-planche.png`.
- **Sources** : `sources/premiere-ae-saccade-choisie-2026-10.md`.
- **Examens** : n°1 13, n°2 14, n°3 15, n°4 14, n°5 14, n°6 15, n°7 15, n°8 15 /20. **N°9 à la session 17 ou 18** (BACKLOG 85 : sans musique).

## Reprendre ici (session 17)
1. Démarrage normal. `python3 -m pip install -q numpy pillow scipy` (25 s) suffit pour la pièce 20 ; Blender et le reste : voir la ligne d'installation de la session 15 dans l'historique Git de ce fichier (`curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz`).
2. Priorités : **85 (examen n°9, sans musique)** ; 87 (pièce 20 v10 : son + moment Muybridge) ; 88 (écart de l'écho) ; 76 (rig à coude) ; 84 (vrai rush strobe CC0) ; 72 ; 51 ; 89-90.
3. Pièges : **`pkill -f motif` tue aussi le shell** → tuer par PID. Plage limitée en `yuv*` (noir = 16). PIL lit un PNG 16 bits en 8 bits. Commentaire au milieu d'une ligne remplacée = code désactivé. OpenCV pip ne lit pas l'EXR. Wikimedia → 429 : Internet Archive. **Session 16** : `piece.py` lit `sys.argv[3]` comme nombre de sous-poses : quand on l'`exec` depuis un autre script, insérer un argument numérique à cette place ; **l'horloge de la VM semble s'arrêter entre deux tours** (uptime 6 min pour une session bien plus longue) : se fier au nombre d'étapes faites, pas à `date`, et clore tôt ; les pages helpx.adobe.com renvoient 403 aux outils de lecture (passer par les extraits de recherche et recouper).

## Environnement constaté
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
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
