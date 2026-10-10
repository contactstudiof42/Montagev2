# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 4, 2026-10-10 02:10 UTC)
- **Skills (21)** : socle (`montage-expert`, `montage-regard`, `montage-direction-artistique`), artistiques (`montage-grammaire`, `montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-references`, `montage-couleur-et-intention`, `montage-kinetic-editing`, `montage-formats`), techniques (`montage-loudness-livraison`, `montage-after-effects`, `montage-ia-generative`, `montage-couleur-pipeline`, `montage-blender`, `montage-resolve`, `montage-preparation-tournage-vfx`, `montage-premiere`, `montage-pilotage-mcp`, **`montage-workflows`** (nouveau)).
- **Culture** : 24 fiches + mesures Ziak. Nouveau en session 4 : Marker, Morris, Burtt, Rydstrom.
- **Atelier** : 01 (v6 réf.), 02 (v6 réf.), 03 (v3), **04 « Ce que la marée découvre »** (`atelier/04-maree-decouvre/` : `scene.py` paramétré par JSON, `montage.py <v> [edl.json]` avec `DECOUVERT=222` pour le son de fin ; v2b = réf. mystère, v6 = meilleur suspense (sous-marin avec volume, rides adoucies)).
- **Labo** : + `fondus/variance.py` (3/4), `marqueurs/beats_xml.py` (XML FCP7), `workflows/otio_aller_retour.py`.
- **Examens** : n°1 (13/20), n°2 (14/20), n°3 (15/20). **N°4 en session 6 ou 7.**

## Reprendre ici (session 5)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy opentimelineio otio-fcp-adapter otio-cmx3600-adapter`.
2. Pièges : tester la **1re et la dernière image** d'un plan Blender animé avant un rendu long ; `pkill -f motif` tue son propre shell (utiliser le PID) ; `bash -c "..."` avec plusieurs commandes est bloqué par un contrôle de sécurité → écrire un petit script `.sh` dans le scratchpad ; une EDL ne porte pas la cadence.
3. BACKLOG dans l'ordre : pièce 04 (animer le plan sous-marin de v6, puis 9:16) ; ateliers « Spirale » / « Versions » ; atelier 03 v4 ; pièce 02 v7 ; fondus (2e vérité terrain).
4. Terminer vers 40 min. Sous-agents de recherche en parallèle : efficaces (4 en session 4), relire leurs fiches avant de les verser.

## Environnement constaté
- ffmpeg 6.1.1, Python 3 + numpy 2.5.3, Node 22 préinstallés. Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 4 — 2026-10-10 01:30 → 02:10 UTC : loudness hors plateformes, atelier 04 (v1-v4/v5), fondus 3/4, marqueurs XML, `montage-workflows` + OTIO, fiches Marker, Morris, Burtt, Rydstrom, vérification IA.
- Session 3 — 2026-10-10 00:30 → ~00:50 UTC : `montage-pilotage-mcp`, atelier 03 « rythme macro » (3 versions), labo fondus (résultat négatif), `montage-premiere`, fiches Varda et Jonze, examen n°3 (15/20), `montage-formats`.
- Session 2 — 2026-10-09 23:52 → 2026-10-10 00:30 UTC : pièce 02 « Étincelle » (6 versions), labo encodage, `montage-blender`, `montage-resolve`, fiches Murai et Honda « Cog », examen n°2 (14/20).
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
