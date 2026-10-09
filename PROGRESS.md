# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 1, 2026-10-09)
- **Skills (13)** : socle (`montage-expert`, `montage-regard`, `montage-direction-artistique`), artistiques (`montage-grammaire`, `montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-references`, `montage-couleur-et-intention`*), techniques (`montage-loudness-livraison`, `montage-after-effects`, `montage-ia-generative`, `montage-couleur-pipeline`*). *= produits en fin de session 1, survolés seulement : à relire en session 2.
- **Culture** : 10 fiches de montage/title design + 3 fiches couleur (Storaro, Doyle/Wong Kar-wai, Deakins) + 1 fiche IA.
- **Atelier** : pièce 01 « Respiration » (`atelier/01-respiration/CRITIQUE.md`). v1 → v6, v6 + son « silence » = référence. Le « bruit » de la v5 venait de l'encodage H.264 du dégradé, pas du rendu (mesuré). Reste : test d'encodage des dégradés. Puis pièce 02.
- **Labo** : loudness (testé), livraison H.264 (testé), détection de coupes scdet (testé), expressions AE sous Node (syntaxe/logique), couleur (lancé en fin de session 1 : vérifier `labo/couleur/RESULTATS.md`).
- **Examens** : n°1 fait (`examens/01-mutuelle-jeunes-parents.md`, 13/20 : audace insuffisante, clichés de catégorie non vus). Prochain examen : session 4 ou 5, autre format (clip ou documentaire).

## Reprendre ici (session 2)
1. Démarrage normal (PROMPT.md). Réinstaller Blender (30 s) : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad.
2. Polices libres : github.com est bloqué pour les dépôts hors périmètre, mais **jsDelivr fonctionne** : `https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/<famille>/<fichier>.ttf`.
3. Relire en détail `montage-couleur-pipeline` et les fiches couleur (survolées seulement).
4. BACKLOG dans l'ordre (atelier « direction A dans le noir », clôture de la pièce 01, grammaire).

## Environnement constaté
- ffmpeg 6.1.1, Python 3 + numpy 2.5.3, Node 22 préinstallés. Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
