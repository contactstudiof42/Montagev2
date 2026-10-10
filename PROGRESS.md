# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 7, 2026-10-10 ~05:05 UTC)
- **Skills (21)** : enrichis en session 7 : `montage-kinetic-editing` (photosensibilité testée, leçons de l'atelier 09), `montage-loudness-livraison` (Lo/Ro, Lt/Rt Hilbert, mono : les arrières disparaissent), `montage-grammaire` (180° mesuré, J-cut de mémoire), `montage-couleur-et-intention` (souvenir par le support et le format), `montage-blender` (déterminisme, plans immobiles, caméra portée), `montage-references` (Noé / Kan, Kuntzel + Deygas), `montage-motion-design-principes`, `montage-regard`, `montage-expert` (sommaire et outils de contrôle).
- **Culture** : 36 fiches. Nouveau : *Enter the Void* (générique Noé / Tom Kan), *Catch Me If You Can* (Kuntzel + Deygas).
- **Atelier** : **08 « Souvenir »** (v1-v4, v4 = référence : présent figé / passé caméscope 4:3, J-cut, trace de tasse dans le présent) ; **09 « Générique de l'équipe »** (v1-v4, v4 = référence : rupture d'échelle, sommet qui change de règle, contrôle de flashs, -14,5 LUFS).
- **Labo** : `labo/photosensibilite/` (flash_check v2, fenêtre WCAG), `labo/surround/` (downmix, Hilbert), `labo/grammaire/` (180°). Déterminisme Blender vérifié.
- **Examens** : n°1 13, n°2 14, n°3 15, n°4 14 /20. **N°5 en session 8** (BACKLOG 39).

## Reprendre ici (session 8)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy pillow scipy`.
2. **Examen n°5 en premier** (BACKLOG 39) : pub 6 s ou documentaire long, avec contrainte 5.1 + mono et photosensibilité ; répondre uniquement avec les skills.
3. Puis BACKLOG 40 (atelier « dialogue » sur le labo 180°), 33 (« inquiétude calme » : plans fixes = une image rendue chacun), 41 (écart OCIO), 42 (fusion des skills artistiques).
4. Pièges : **`pkill -f motif` tue le shell si le motif apparaît N'IMPORTE OÙ dans la commande** (refait en session 7 : le motif était dans un nom de fichier plus loin) → tuer par PID (`ps aux | grep "[b]lender"`). Rendus : plans immobiles = une image. Viser une caméra par un point (`to_track_quat`) plutôt que régler des angles.
5. Sous-agents : 3 en session 7 (labo surround, 2 fiches), fiables ; chiffre clé revérifié à la main avant versement (-52,4 / -70 LUFS).

## Environnement constaté
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 7 — 2026-10-10 04:29 → ~05:05 UTC : ateliers 08 « Souvenir » (v1-v4) et 09 « Générique » (v1-v4), labos photosensibilité, surround Lt/Rt, 180°, déterminisme Blender ; fiches Noé / Kan et Kuntzel + Deygas ; PLAN-TESTS 38-39.
- Session 6 — 2026-10-10 03:29 → ~04:05 UTC : fiches Aftersun et Les Revenants, recherche surround et hors champ (vérifiée en labo), atelier 07 « Causalité » (corps rigides, A/B/C), Eevee sans écran mesuré, PLAN-TESTS 36-37.
- Session 5 — 2026-10-10 02:29 → 03:05 UTC : atelier 05 « Trois étalonnages » (6 versions + scintillement), atelier 06 « Versions » (v1-v3), examen n°4 (14/20), API Resolve 19-21.1, fiches Elastic, ManvsMachine, Buck, Åkerlund, Gavras, état public des MCP (tests 21-32), AAF par familles.
- Session 4 — 2026-10-10 01:30 → 02:10 UTC : loudness hors plateformes, atelier 04 (v1-v4/v5), fondus 3/4, marqueurs XML, `montage-workflows` + OTIO, fiches Marker, Morris, Burtt, Rydstrom, vérification IA.
- Session 3 — 2026-10-10 00:30 → ~00:50 UTC : `montage-pilotage-mcp`, atelier 03 « rythme macro » (3 versions), labo fondus (résultat négatif), `montage-premiere`, fiches Varda et Jonze, examen n°3 (15/20), `montage-formats`.
- Session 2 — 2026-10-09 23:52 → 2026-10-10 00:30 UTC : pièce 02 « Étincelle » (6 versions), labo encodage, `montage-blender`, `montage-resolve`, fiches Murai et Honda « Cog », examen n°2 (14/20).
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
