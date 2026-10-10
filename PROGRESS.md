# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 9, 2026-10-10 ~07:15 UTC)
- **Skills (21)** : session 9 : `montage-grammaire` (cécité au changement à travers la coupe), `montage-regard` (règles 12-13), `montage-rythme` (le plan de retour), `montage-couleur-et-intention` (fond = monde, lumière = corps ; contraste simultané), `montage-workflows` + `montage-ia-generative` (interpolation, RIFE testé), `montage-references` (bande-annonce, Freeze, atelier 12).
- **Culture** : 41 fiches (nouvelles : `bande-annonce-montage.md`, `freeze-corleone-clips.md`).
- **Atelier** : **12 « Inquiétude calme »** v1-v7 (v7 réf.), **13 « Le fond raccorde »** v1-v4 (v4 réf.), **14 « Balancier »** A/B (voir `atelier/14-balancier/CRITIQUE.md`).
- **Labo** : `labo/interpolation/` (minterpolate + RIFE 4.25 en CPU, vérité terrain 60 i/s, deux scènes).
- **Examens** : n°1 13, n°2 14, n°3 15, n°4 14, n°5 14 /20. **N°6 en session 10 (BACKLOG 53).**

## Reprendre ici (session 10)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy pillow scipy colour-science`.
2. Priorités : **examen n°6** (BACKLOG 53) ; BACKLOG 50 (pièce 12 v8, lieu encombré) ; 51 (teaser 15 s) ; 49 (interpolation sur vrai plan CC0) ; 42 suite (`montage-references` en annexes, le fichier grossit : 90 lignes).
3. Pièges : **`pkill -f motif` tue le shell** → tuer par PID. **Un `sh -c "…"` lancé avec `nohup … &` est bloqué par le contrôle de sécurité** → utiliser `run_in_background` de l'outil Bash. Plans immobiles = une image. Viser une caméra par un point (`to_track_quat`). `zones.py` (labo interpolation) écrit sa planche dans le dossier courant. Le `pip install torch` d'un sous-agent casse un `.pth` de distutils (message d'erreur bénin à chaque `python3`, ignorer). Rendu Cycles 320×180, 8 éch., scène nocturne de la pièce 14 : ~1 image/s.
4. Sous-agents : 3 en session 9 (2 fiches, essai RIFE) ; tout recontrôlé à la main (vignette Freeze : confirmée, écart dû aux bandes ; chiffres RIFE : identiques).

## Environnement constaté
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 9 — 2026-10-10 06:29 → ~07:15 UTC : pièces 12 (v1-v7), 13 (v1-v4), 14 (A/B) ; labo interpolation (minterpolate, RIFE) ; fiches bande-annonce, Freeze Corleone ; PLAN-TESTS 43-45.
- Session 8 — 2026-10-10 05:29 → 05:53 UTC : pièce 10 v4-v6 (+ montage), pièce 11 « Dialogue » v1-v4, labos VFR et proxies, fiches Scott Pilgrim, génériques de séries doc, drill FR ; `montage-regard` distillé ; PLAN-TESTS 40-42.
- Session 7 — 2026-10-10 04:29 → ~05:10 UTC : examen n°5 (14/20), ateliers 08 « Souvenir » (v1-v4), 09 « Générique » (v1-v4) et 10 « Chaleur partout » (v1-v2), écart OCIO expliqué, labos photosensibilité, surround Lt/Rt, 180°, déterminisme Blender ; fiches Noé / Kan et Kuntzel + Deygas ; PLAN-TESTS 38-39.
- Session 6 — 2026-10-10 03:29 → ~04:05 UTC : fiches Aftersun et Les Revenants, recherche surround et hors champ (vérifiée en labo), atelier 07 « Causalité » (corps rigides, A/B/C), Eevee sans écran mesuré, PLAN-TESTS 36-37.
- Session 5 — 2026-10-10 02:29 → 03:05 UTC : atelier 05 « Trois étalonnages » (6 versions + scintillement), atelier 06 « Versions » (v1-v3), examen n°4 (14/20), API Resolve 19-21.1, fiches Elastic, ManvsMachine, Buck, Åkerlund, Gavras, état public des MCP (tests 21-32), AAF par familles.
- Session 4 — 2026-10-10 01:30 → 02:10 UTC : loudness hors plateformes, atelier 04 (v1-v4/v5), fondus 3/4, marqueurs XML, `montage-workflows` + OTIO, fiches Marker, Morris, Burtt, Rydstrom, vérification IA.
- Session 3 — 2026-10-10 00:30 → ~00:50 UTC : `montage-pilotage-mcp`, atelier 03 « rythme macro » (3 versions), labo fondus (résultat négatif), `montage-premiere`, fiches Varda et Jonze, examen n°3 (15/20), `montage-formats`.
- Session 2 — 2026-10-09 23:52 → 2026-10-10 00:30 UTC : pièce 02 « Étincelle » (6 versions), labo encodage, `montage-blender`, `montage-resolve`, fiches Murai et Honda « Cog », examen n°2 (14/20).
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
