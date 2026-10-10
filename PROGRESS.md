# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 2, 2026-10-10 ~00:40 UTC)
- **Skills (16)** : socle (`montage-expert`, `montage-regard`, `montage-direction-artistique`), artistiques (`montage-grammaire`, `montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-references`, `montage-couleur-et-intention`, `montage-kinetic-editing`), techniques (`montage-loudness-livraison`, `montage-after-effects`, `montage-ia-generative`, `montage-couleur-pipeline`, **`montage-blender`** (nouveau, testé en atelier), **`montage-resolve`** (nouveau, théorique)).
- **Culture** : 18 fiches + mesures Ziak. Nouveau en session 2 : Hiro Murai « This Is America », Honda « Cog ».
- **Atelier** : pièce 01 « Respiration » (v6 = référence). **Pièce 02 « Étincelle »** (`atelier/02-etincelle/`, vertical kinetic 8,9 s) : v1 → v6, v6 = référence (le pendule allume l'allumette ; 19/19 plans lisibles ; couleur chaude mesurée à 0,14 % avant l'allumage). Scripts : `scene.py` (plateau multi-caméras) + `montage.py` (EDL JSON → rendu des seules images utiles → SFX → loudness → planche).
- **Labo** : loudness, livraison H.264, scdet, expressions AE (Node), couleur, kinetic, analyse-clip, **encodage** (nouveau : bandes dans les noirs, `labo/encodage/RESULTATS.md`).
- **Examens** : n°1 (13/20), **n°2 « Marée basse » (14/20, session 2)**. N°3 en session 5 ou 6 (documentaire ou corporate).

## Reprendre ici (session 3)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). **numpy n'est pas toujours là : `python3 -m pip install -q numpy`** (`pip` seul installe pour un autre Python).
2. Piège Bash : `until ! pgrep -f "montage.py v1"` se trouve lui-même (le motif est dans sa propre ligne de commande) et ne s'arrête jamais. Attendre plutôt que le fichier de log soit non vide.
3. BACKLOG dans l'ordre : pièce 02 v7 (vraie flamme, chaîne causale complète, variante macro façon Ziak), atelier « ce que la marée découvre », skill `montage-preparation-tournage-vfx`.
4. Les rendus de la pièce 02 ne survivent pas (VM effacée) : relancer `python3 atelier/02-etincelle/montage.py v6 <blender>` (≈ 5 min) avant de faire une v7.

## Environnement constaté
- ffmpeg 6.1.1, Python 3 + numpy 2.5.3, Node 22 préinstallés. Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 2 — 2026-10-09 23:52 → 2026-10-10 ~00:40 UTC : pièce 02 « Étincelle » (6 versions), labo encodage, `montage-blender`, `montage-resolve`, fiches Murai et Honda « Cog », examen n°2 (14/20).
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
