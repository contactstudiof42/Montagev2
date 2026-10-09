# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 1, 2026-10-09)
- **Skills (11)** : socle (`montage-expert`, `montage-regard`, `montage-direction-artistique`), artistiques (`montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-references`, `montage-couleur-et-intention`*), techniques (`montage-loudness-livraison`, `montage-after-effects`, `montage-ia-generative`, `montage-couleur-pipeline`*). *= produits en fin de session 1, à relire en session 2.
- **Culture** : 10 fiches de montage/title design + 1 fiche IA + fiches couleur (Storaro, Doyle, Deakins, si l'agent a fini : vérifier).
- **Atelier** : pièce 01 « Respiration », v1 → v5 (`atelier/01-respiration/CRITIQUE.md`). Reste : regarder la planche v5, trancher le son (v5a grondement / v5b silence), clore.
- **Labo** : loudness (testé), livraison H.264 (testé), détection de coupes scdet (testé), expressions AE sous Node (syntaxe/logique), couleur (lancé en fin de session 1 : vérifier `labo/couleur/RESULTATS.md`).
- **Examens** : aucun. Le premier est la priorité n°1 de la session 2.

## Reprendre ici (session 2)
1. Démarrage normal (PROMPT.md). Réinstaller Blender (30 s) : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad.
2. Polices libres : github.com est bloqué pour les dépôts hors périmètre, mais **jsDelivr fonctionne** : `https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/<famille>/<fichier>.ttf`.
3. Relire `montage-couleur-pipeline`, `montage-couleur-et-intention` et les fiches couleur produites en fin de session 1 (pas relues par moi).
4. Examen créatif n°1, puis BACKLOG dans l'ordre.

## Environnement constaté
- ffmpeg 6.1.1, Python 3 + numpy 2.5.3, Node 22 préinstallés. Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 1 — 2026-10-09 22:48 UTC : démarrage, structure, 11 skills, 10+ fiches, atelier 01 (5 versions), 4 labos.
