# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 11, 2026-10-10 ~09:00 UTC)
- **Skills (21)** : session 11 : `montage-regard` (règles 15-16), `montage-references` (fable qui contient la réponse), `montage-couleur-et-intention` (Willis ; Young / van Hoytema), `montage-workflows` (recadrages, nests, stéréo dans l'échange), `montage-after-effects` (bercement à phase intégrée + piège), `montage-preparation-tournage-vfx` (écrans dans le champ, 5 bis), `montage-direction-artistique` (maquetter la direction qui fait peur).
- **Culture** : 45 fiches (nouvelles : `gordon-willis-le-noir.md`, `bradford-young-van-hoytema-lumiere-basse.md`).
- **Atelier** : **16 v4** (v4d réf. ; reste v5 : silhouettes sur les autres planètes) ; **17 « 3 h 12, dans le noir »** v1-v4 (`atelier/17-dans-le-noir/`, v3 = réf. ; `planche.py`, `mouvement.py`).
- **Labo** : `labo/workflows/recadrages/` (sous-agent, rejoué à la main : identique) ; `labo/ae-expressions/bercement/test.js`.
- **Examens** : n°1 13, n°2 14, n°3 15, n°4 14, n°5 14, n°6 15 /20. **N°7 en session 12 ou 13** (BACKLOG 64 : brief de nuit / basse lumière).

## Reprendre ici (session 12)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy pillow scipy colour-science opentimelineio otio-fcp-adapter otio-cmx3600-adapter`.
2. Priorités : BACKLOG 64 (examen n°7), 1 suite (pièce 17 : son + contrechamp, bébé lisible), 57 (pièce 16 v5), 51 (teaser 15 s), 62 suite (Natasha Braier), 42 suite (`montage-references` en annexes).
3. Pièges : **`pkill -f motif` / `pgrep -f motif` + kill tuent aussi le shell** dont la ligne de commande contient le motif (session 11 : exit 144) → tuer par PID via `ps aux | grep "[b]lender -b"`. Rendus longs : `nohup … &` puis attendre avec une boucle `while ps …`. Animation Cycles 384×216, 12 échantillons : ~3,7 s/image seule, ~2× plus lente à deux en parallèle → `STEP=2` (une image sur deux) pour les aperçus. Plans immobiles = une image. Wikimedia renvoie **HTTP 429** : passer par Internet Archive. **Jamais d'e-mail dans un User-Agent.** Vérifier qu'un nom inventé ne recoupe pas une marque réelle.
4. Sous-agents : 1 en session 11 (recadrages / nests / audio) ; chiffres rejoués à la main (identiques).

## Environnement constaté
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 11 — 2026-10-10 08:30 → ~09:00 UTC : pièce 16 v4, pièce 17 « dans le noir » (v1-v4), fiches Willis et Young / van Hoytema, labos recadrages / nests / audio dans l'échange (sous-agent) et bercement AE (phase intégrée) ; écrans dans le champ ; PLAN-TESTS 48.
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
