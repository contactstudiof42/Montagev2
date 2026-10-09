# BACKLOG — sujets priorisés

Légende : `[ART]` regard, culture, atelier, examens · `[TECH]` maîtrise technique.
Statut : `[ ]` à faire · `[~]` entamé · `[x]` fait (garder 1 ligne de trace).
Règle : alterner ART et TECH. Réalimenter dès qu'il reste moins de 10 sujets ouverts.

## Priorité haute (prochaines sessions)
1. [ ] [ART] **Atelier « même brief, direction A dans le noir »** (suite de l'examen n°1 : la piste la plus audacieuse, écartée trop vite) : 10 s, Blender, seule lumière = un écran de téléphone.
1b. [ ] [ART] Fiche sur les pubs santé/assurance et petite enfance : repérer les clichés du secteur (boîte à musique, bébé au ralenti, famille radieuse) — révélé par l'examen n°1.
2. [~] [TECH] Couleur technique → `montage-couleur-pipeline` v1 (labo session 1 : conversions exactes, LUT ffmpeg = Python). Reste : expliquer l'écart OCIO/colour de 2e-3 sur LogC3/S-Log3 ; tester un vrai rush log CC0.
3. [~] [ART] Couleur et intention → `montage-couleur-et-intention` v1 (fiches Storaro, Doyle, Deakins). Reste : atelier « même plan, trois étalonnages » avec la LUT du labo.
4. [~] [ART] Atelier 01 : v5 faite ; corriger le bruit Cycles du fond clair (16 éch. + débruitage), trancher v5a/v5b (préférence v5b), clore. Puis **pièce 02 spectaculaire et rapide** (contraste avec la 01) : montage « hip-hop » de 8 plans Blender de 6 à 12 images avec bruitages synthétiques, 6 s, vertical 9:16.
5. [ ] [TECH] Fondamentaux : grammaire, raccords, 180°, montage son, J-cut/L-cut → skill `montage-grammaire`
6. [ ] [ART] Atelier rythme : un même matériau monté sur trois tempos (Bass / Gondry / Cooper — cf. `montage-references` B) ; mesure avec scdet
7. [ ] [TECH] Blender pour la vidéo : skill `montage-blender` (rendu CLI, Cycles vs Eevee headless, compositing, geometry nodes) — base déjà pratiquée dans l'atelier 01 ; tester Eevee en headless
8. [ ] [TECH] DaVinci Resolve : nodes, RCM, Fusion, Fairlight, API de scripting Python (doc officielle)
9. [ ] [ART] Narration par format : pub 15/30 s, vertical, clip, corporate, doc, fiction → skill `montage-formats`
10. [ ] [TECH] Premiere Pro (« Premiere 26 » depuis janv. 2026 selon sources) : projet, proxies, multicam, sous-titres, Lumetri, exports → skill `montage-premiere`
11. [ ] [TECH] Préparer un tournage pour les effets → skill `montage-preparation-tournage-vfx`
12. [ ] [TECH] Pilotage MCP : état public (Higgsfield et autres), méthode d'agent → `montage-pilotage-mcp` + compléter `PLAN-TESTS-MCP.md`
13. [ ] [ART] Son : atelier « même image, trois bandes son » (avec, contre, silence) ; fiches Murch sound design, Ben Burtt, Gary Rydstrom
14. [ ] [TECH] Compositing / keying / tracking / roto (AE, Fusion, Blender) — test keying sur image CC0 avec ffmpeg (`chromakey`) et Blender
15. [ ] [TECH] Workflows transversaux et pipelines par format → skill `montage-workflows`
16. [ ] [TECH] Labo rythme : tester scdet sur du vrai matériau CC0 (faux positifs ? seuil ?) ; détecter les fondus (différence image à image sur fenêtre)
17. [ ] [ART] Culture : documentaire (Agnès Varda *Les Glaneurs*, Errol Morris, Chris Marker *Sans soleil*) ; clips (Spike Jonze, Hiro Murai, Jonas Åkerlund) ; motion design de studio (Buck, ManvsMachine, Elastic) ; pubs (Honda *Cog*, Apple *1984*)
18. [ ] [ART] IA : vérifier les faits incertains de `montage-ia-generative` (Sora, AI Act art. 50), ajouter des fiches d'œuvres IA, définir une grille « est-ce que ça fait IA ? »
19. [ ] [ART] Relire les skills artistiques après l'examen n°1 ; fusionner les doublons (regard / motion-design / references se recoupent sur « un signe »)

## Fait (trace)
- [x] [ART] Examen créatif n°1 « mutuelle jeunes parents » : 13/20, corrections dans `montage-direction-artistique` (session 1)
- [x] [ART] Socle v1 : `montage-expert`, `montage-regard`, `montage-direction-artistique` (session 1)
- [x] [TECH] Loudness et livraison, testé en labo (session 1) — leçon : mesure + gain > loudnorm 2 passes
- [x] [ART] Culture : 10 fiches (Murch, Schoonmaker, Bass, Cooper, Wright, Gondry, Glazer, Menke, Baxter/Wall, Clair) + 1 fiche IA (session 1)
- [x] [ART] `montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-references` v1 (session 1)
- [x] [TECH] `montage-after-effects` v1 (expressions testées sous Node), `montage-ia-generative` v1 daté (session 1)
- [x] [TECH] Labo rythme : détection de coupes scdet (session 1)
- [x] [ART] Atelier 01 « Respiration » v1 → v5 (session 1)
