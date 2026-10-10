# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 3, 2026-10-10 ~00:50 UTC)
- **Skills (20)** : socle (`montage-expert`, `montage-regard`, `montage-direction-artistique`), artistiques (`montage-grammaire`, `montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-references`, `montage-couleur-et-intention`, `montage-kinetic-editing`), techniques (`montage-loudness-livraison`, `montage-after-effects`, `montage-ia-generative`, `montage-couleur-pipeline`, `montage-blender`, `montage-resolve`, `montage-preparation-tournage-vfx`, **`montage-premiere`** (nouveau, théorique), **`montage-pilotage-mcp`** (nouveau, méthode)) + **`montage-formats`** (nouveau, artistique, synthèse).
- **Culture** : 20 fiches + mesures Ziak. Nouveau en session 3 : Varda *Les Glaneurs*, Spike Jonze (*Weapon of Choice*, *Welcome Home*).
- **Atelier** : 01 « Respiration » (v6 réf.), 02 « Étincelle » (v6 réf.), **03 « Rythme macro »** (`atelier/03-rythme-macro/`, v1 → v3 : A micro, B macro, C hybride ; `build.py <dossier> v2|v3`, ≈ 1 min).
- **Labo** : loudness, livraison, scdet, expressions AE, couleur, kinetic, analyse-clip, encodage, keying, **fondus** (nouveau : scdet rate tous les fondus ; deux détecteurs simples échouent sur le mouvement ; `labo/fondus/RESULTATS.md`).
- **Examens** : n°1 (13/20), n°2 (14/20), **n°3 « Seconde main » (corporate, 15/20, session 3)**. N°4 en session 6 ou 7.

## Reprendre ici (session 4)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). numpy : `python3 -m pip install -q numpy`.
2. Pièges : `until pgrep` se trouve lui-même ; `xfade` exige des bases de temps identiques (`fps=25,settb=AVTB`) et ses `offset` après `concat` sont traîtres → composer une vérité terrain en numpy ; en montage scripté, couper sur des numéros d'image absolus.
3. BACKLOG dans l'ordre : loudness hors plateformes (0f) ; atelier 03 v4 (plans Blender avec sujet, A + SFX) ; labo fondus (courbe de variance) ; pièce 02 v7 ; atelier « ce que la marée découvre ».
4. **Terminer vers 40 min** (dernier commit ≥ 15 min avant la session suivante, sinon elle s'arrête à l'anti-doublon : arrivé en sessions 2 et 3).
5. WebFetch renvoie 403 sur helpx.adobe.com : passer par WebSearch (extraits) ou par des miroirs.

## Environnement constaté
- ffmpeg 6.1.1, Python 3 + numpy 2.5.3, Node 22 préinstallés. Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 3 — 2026-10-10 00:30 → ~00:50 UTC : `montage-pilotage-mcp`, atelier 03 « rythme macro » (3 versions), labo fondus (résultat négatif), `montage-premiere`, fiches Varda et Jonze, examen n°3 (15/20), `montage-formats`.
- Session 2 — 2026-10-09 23:52 → 2026-10-10 00:30 UTC : pièce 02 « Étincelle » (6 versions), labo encodage, `montage-blender`, `montage-resolve`, fiches Murai et Honda « Cog », examen n°2 (14/20).
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
