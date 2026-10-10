# BACKLOG — sujets priorisés

Légende : `[ART]` regard, culture, atelier, examens · `[TECH]` maîtrise technique.
Statut : `[ ]` à faire · `[~]` entamé · `[x]` fait (garder 1 ligne de trace).
Règle : alterner ART et TECH. Réalimenter dès qu'il reste moins de 10 sujets ouverts.

## Priorité haute (prochaines sessions)
0. [~] [ART] **Pièce 02 « Étincelle »** (`atelier/02-etincelle/`) : v1 → v5 en session 2. Reste : v6 = vraie flamme (simulation Blender ou particules) à la place du cône ; tester une durée de silence plus longue (9 → 15 images) ; un plan de « frôlement » raté à 170 pour planter l'attente (Chekhov) ; variante **macro façon Ziak** du même matériau (montage sur l'arrangement, aucun SFX surligné) pour comparer les deux usages.
0b. [x] [ART] Ziak analysé sur le fichier fourni (88 plans, montage calé sur l'arrangement et pas sur le beat, seconde horloge visuelle). Outil réutilisable : `labo/analyse-clip/analyse_clip.py`.
0c. [ ] [ART] **Atelier « rythme macro »** : un même plan de 30 s sur une instru drill CC0, monté (a) calé sur les temps, (b) calé sur l'arrangement à la Ziak ; critique comparée. Puis passer `analyse_clip.py` sur les références que l'utilisateur ajoutera.
1. [ ] [ART] **Atelier « même brief, direction A dans le noir »** (suite de l'examen n°1 : la piste la plus audacieuse, écartée trop vite) : 10 s, Blender, seule lumière = un écran de téléphone.
1b. [ ] [ART] Fiche sur les pubs santé/assurance et petite enfance : repérer les clichés du secteur (boîte à musique, bébé au ralenti, famille radieuse) — révélé par l'examen n°1.
2. [~] [TECH] Couleur technique → `montage-couleur-pipeline` v1 (labo session 1 : conversions exactes, LUT ffmpeg = Python). Reste : expliquer l'écart OCIO/colour de 2e-3 sur LogC3/S-Log3 ; tester un vrai rush log CC0.
3. [~] [ART] Couleur et intention → `montage-couleur-et-intention` v1 (fiches Storaro, Doyle, Deakins). Reste : atelier « même plan, trois étalonnages » avec la LUT du labo.
4. [x] [TECH] Encodage des dégradés sombres testé (session 2, `labo/encodage/`) : tramage ±1 tué par x264, 10 bits = solution master, grain σ≈2 = seule protection après ré-encodage plateforme. Reste [ ] : réappliquer à la pièce 01 (v7 avec grain) et mesurer.
5. [ ] [TECH] Fondamentaux : grammaire, raccords, 180°, montage son, J-cut/L-cut → skill `montage-grammaire`
6. [ ] [ART] Atelier rythme : un même matériau monté sur trois tempos (Bass / Gondry / Cooper — cf. `montage-references` B) ; mesure avec scdet
7. [ ] [TECH] Blender pour la vidéo : skill `montage-blender` (rendu CLI, Cycles vs Eevee headless, compositing, geometry nodes) — base déjà pratiquée dans l'atelier 01 ; tester Eevee en headless
8. [~] [TECH] DaVinci Resolve → `montage-resolve` v1 (session 2 : nodes, RCM, API d'après le README 2022-2023). Reste : Fusion, Fairlight, README 19-20 (objets Graph ? ColorGroup ?), atelier couleur « même plan, trois étalonnages » traduit en arbre de nodes.
9. [ ] [ART] Narration par format : pub 15/30 s, vertical, clip, corporate, doc, fiction → skill `montage-formats`
10. [ ] [TECH] Premiere Pro (« Premiere 26 » depuis janv. 2026 selon sources) : projet, proxies, multicam, sous-titres, Lumetri, exports → skill `montage-premiere`
11. [ ] [TECH] Préparer un tournage pour les effets → skill `montage-preparation-tournage-vfx`
12. [ ] [TECH] Pilotage MCP : état public (Higgsfield et autres), méthode d'agent → `montage-pilotage-mcp` + compléter `PLAN-TESTS-MCP.md`
13. [ ] [ART] Son : atelier « même image, trois bandes son » (avec, contre, silence) ; fiches Murch sound design, Ben Burtt, Gary Rydstrom
14. [ ] [TECH] Compositing / keying / tracking / roto (AE, Fusion, Blender) — test keying sur image CC0 avec ffmpeg (`chromakey`) et Blender
15. [ ] [TECH] Workflows transversaux et pipelines par format → skill `montage-workflows`
16. [ ] [TECH] Labo rythme : tester scdet sur du vrai matériau CC0 (faux positifs ? seuil ?) ; détecter les fondus (différence image à image sur fenêtre)
17. [~] [ART] Culture : fait en session 2 : Hiro Murai « This Is America », Honda « Cog ». Reste : documentaire (Varda *Les Glaneurs*, Errol Morris, Marker *Sans soleil*) ; clips (Spike Jonze, Jonas Åkerlund, et clips de rap français proches de Ziak) ; motion design de studio (Buck, ManvsMachine, Elastic) ; pub (Apple *1984*)
18. [ ] [ART] IA : vérifier les faits incertains de `montage-ia-generative` (Sora, AI Act art. 50), ajouter des fiches d'œuvres IA, définir une grille « est-ce que ça fait IA ? »
19. [ ] [ART] Relire les skills artistiques après l'examen n°1 ; fusionner les doublons (regard / motion-design / references se recoupent sur « un signe »)

20. [ ] [ART] **Examen créatif n°2** (dû en session 3 ou 4) : un clip de rap français, à traiter en montage macro (goût de l'utilisateur), avec préparation du tournage.
21. [ ] [ART] Atelier « causalité » : reprendre le principe de Honda « Cog » (chaque coupe montre une cause et son effet) sur 10 s de Blender, sans musique, seulement les sons des objets.
22. [x] [TECH] `montage-blender` v1 écrit (session 2) ; reste Eevee headless, geometry nodes, compositing, camera tracking — : consigner ce que l'atelier 02 a appris (cadre et fenêtres de source calculées depuis la cinématique, cache d'images par caméra, ~1 image/s en Cycles 270×480 12 échantillons + débruitage).

## Fait (trace)
- [x] [TECH] Labo encodage : bandes dans les noirs (session 2)
- [x] [ART] Culture : Murai « This Is America », Honda « Cog » (session 2)
- [x] [ART] Examen créatif n°1 « mutuelle jeunes parents » : 13/20, corrections dans `montage-direction-artistique` (session 1)
- [x] [ART] Socle v1 : `montage-expert`, `montage-regard`, `montage-direction-artistique` (session 1)
- [x] [TECH] Loudness et livraison, testé en labo (session 1) — leçon : mesure + gain > loudnorm 2 passes
- [x] [ART] Culture : 10 fiches (Murch, Schoonmaker, Bass, Cooper, Wright, Gondry, Glazer, Menke, Baxter/Wall, Clair) + 1 fiche IA (session 1)
- [x] [ART] `montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-references` v1 (session 1)
- [x] [TECH] `montage-after-effects` v1 (expressions testées sous Node), `montage-ia-generative` v1 daté (session 1)
- [x] [TECH] Labo rythme : détection de coupes scdet (session 1)
- [x] [ART] Atelier 01 « Respiration » v1 → v5 (session 1)
