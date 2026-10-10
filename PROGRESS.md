# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 5, 2026-10-10 03:05 UTC)
- **Skills (21)** : inchangés en nombre ; enrichis en session 5 : `montage-couleur-et-intention`, `montage-resolve`, `montage-references`, `montage-workflows`, `montage-pilotage-mcp`, `montage-regard`.
- **Culture** : 29 fiches. Nouveau en session 5 : Elastic (*Game of Thrones*), ManvsMachine, Buck, Åkerlund (« Smack My Bitch Up »), Gavras (« Stress », « Born Free »).
- **Atelier** : 01 (v6 réf.), 02 (v6 réf.), 03 (v3), 04 (v2b mystère / v6 suspense ; `scene.py` accepte maintenant `rust_col`), **05 « Trois étalonnages »** (v1-v6 + test de scintillement ; `grade.py` = arbre de nodes numpy, `scintillement.py`), **06 « Versions »** (Morris ; v3 = référence ; `scene.py` 3 variantes seule/tremble/ombre + insert, `montage.py <v> <edl.json>`).
- **Labo** : + `workflows/aaf_pistes.py` (AAF par familles, relu identique par pyaaf2 et OTIO).
- **Sources** : + `mcp-etat-public-2026-10.md`, `resolve-scripting-api-19-20.md` (versé dans `montage-resolve`).
- **Examens** : n°1 (13/20), n°2 (14/20), n°3 (15/20), n°4 (14/20, session 5). **N°5 en session 8.**

## Reprendre ici (session 6)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy pillow opentimelineio otio-fcp-adapter otio-cmx3600-adapter pyaaf2 otio-aaf-adapter` (utiliser `python3 -m pip`, `pip` seul vise un autre Python).
2. Pièges : tester la **1re et la dernière image** d'un plan Blender animé ; vérifier la **pose de repos** d'un objet qui tombe (pièce 06 v1 : la tasse finit dans le sol) ; ne jamais `cd` dans un paquet Python (son `types.py` masque la bibliothèque standard) ; `bash -c` multi-commandes bloqué → script `.sh` dans le scratchpad ; Cycles 480×270 16 échantillons ≈ 2,5 s/image avec 2 sources surfaciques.
3. Fiches *Aftersun* et *Les Revenants* (révélées par l'examen n°4), surround et présence hors champ.
4. Puis BACKLOG : pièce 06 v4 si utile (décor habité ; voir `atelier/06-versions/CRITIQUE.md` ; paramètres `v3-params-*.json`, ~2,5 s/image), verser la recherche Resolve 19-20 dans `montage-resolve`, pièce 04 (sous-marin animé, 9:16), « Spirale ».
5. Sous-agents de recherche en parallèle (3 en session 5, fiables) ; relire leurs fiches avant de les verser.

## Environnement constaté
- ffmpeg 6.1.1, Python 3 + numpy 2.5.3, Node 22 préinstallés. Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 5 — 2026-10-10 02:29 → 03:05 UTC : atelier 05 « Trois étalonnages » (6 versions + scintillement), atelier 06 « Versions » (v1-v3), examen n°4 (14/20), API Resolve 19-21.1, fiches Elastic, ManvsMachine, Buck, Åkerlund, Gavras, état public des MCP (tests 21-32), AAF par familles.
- Session 4 — 2026-10-10 01:30 → 02:10 UTC : loudness hors plateformes, atelier 04 (v1-v4/v5), fondus 3/4, marqueurs XML, `montage-workflows` + OTIO, fiches Marker, Morris, Burtt, Rydstrom, vérification IA.
- Session 3 — 2026-10-10 00:30 → ~00:50 UTC : `montage-pilotage-mcp`, atelier 03 « rythme macro » (3 versions), labo fondus (résultat négatif), `montage-premiere`, fiches Varda et Jonze, examen n°3 (15/20), `montage-formats`.
- Session 2 — 2026-10-09 23:52 → 2026-10-10 00:30 UTC : pièce 02 « Étincelle » (6 versions), labo encodage, `montage-blender`, `montage-resolve`, fiches Murai et Honda « Cog », examen n°2 (14/20).
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
