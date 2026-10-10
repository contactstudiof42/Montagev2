# BACKLOG — sujets priorisés

Légende : `[ART]` regard, culture, atelier, examens · `[TECH]` maîtrise technique.
Statut : `[ ]` à faire · `[~]` entamé · `[x]` fait (garder 1 ligne de trace).
Règle : alterner ART et TECH. Réalimenter dès qu'il reste moins de 10 sujets ouverts.

## Priorité haute (prochaines sessions)
0. [~] [ART] **Pièce 02 « Étincelle »** (`atelier/02-etincelle/`) : v1 → v5 en session 2. Reste : v6 = vraie flamme (simulation Blender ou particules) à la place du cône ; tester une durée de silence plus longue (9 → 15 images) ; un plan de « frôlement » raté à 170 pour planter l'attente (Chekhov) ; variante **macro façon Ziak** du même matériau (montage sur l'arrangement, aucun SFX surligné) pour comparer les deux usages.
0b. [x] [ART] Ziak analysé sur le fichier fourni (88 plans, montage calé sur l'arrangement et pas sur le beat, seconde horloge visuelle). Outil réutilisable : `labo/analyse-clip/analyse_clip.py`.
0c. [~] [ART] **Atelier 03 « rythme macro »** : v1-v3 faites (session 3 : micro / macro / hybride, leçons dans `montage-rythme`). Reste v4 : plans Blender avec un sujet (objet industriel démonté, cf. Ziak) pour tester l'intro tenue ; version A **avec SFX** (vrai concurrent kinetic) ; seconde horloge à +15 %. Puis `analyse_clip.py` sur les références que l'utilisateur ajoutera.
0d. [x] [ART] Examen n°3 « Seconde main » (corporate réemploi) : 15/20 (session 3). **Examen n°4 en session 6 ou 7** : fiction courte ou documentaire long.
0e. [~] [ART] Skill `montage-formats` v1 écrit (session 3). Reste : mesurer des durées de plans médianes sur des références réelles par format ; (remonté par l'examen n°3) : conventions et pièges par format ; section « dispositifs pour filmer l'humain en corporate » (objets-témoins, gestes, portraits muets, un salarié = un objet).
0f. [x] [TECH] Loudness hors plateformes (session 4) : AES TD1008 (-18 parole / -16 musique), corporate web -16 / salle -18, cinéma Leq(m) → `montage-loudness-livraison`, `sources/loudness-hors-plateformes-2026-10.md`. Reste [ ] : relire le PDF TD1008 (403) pour le true peak.
1. [ ] [ART] **Atelier « même brief, direction A dans le noir »** (suite de l'examen n°1 : la piste la plus audacieuse, écartée trop vite) : 10 s, Blender, seule lumière = un écran de téléphone.
1b. [x] [ART] (session 4 : `culture/cliches-de-secteur.md`, 10 secteurs, non mesuré ; reste à l'étayer de références datées) Fiche sur les pubs santé/assurance et petite enfance : repérer les clichés du secteur (boîte à musique, bébé au ralenti, famille radieuse) — révélé par l'examen n°1.
2. [~] [TECH] Couleur technique → `montage-couleur-pipeline` v1 (labo session 1 : conversions exactes, LUT ffmpeg = Python). Reste : expliquer l'écart OCIO/colour de 2e-3 sur LogC3/S-Log3 ; tester un vrai rush log CC0.
3. [x] [ART] Couleur et intention : atelier 05 « Trois étalonnages » fait (session 5, 6 versions + test de scintillement, `atelier/05-trois-etalonnages/`). Reste [ ] : refaire depuis un EXR linéaire (latitude) ; « souvenir » avec un vrai contexte de montage (contrechamp, voix).
4. [x] [TECH] Encodage des dégradés sombres testé (session 2, `labo/encodage/`) : tramage ±1 tué par x264, 10 bits = solution master, grain σ≈2 = seule protection après ré-encodage plateforme. Reste [ ] : réappliquer à la pièce 01 (v7 avec grain) et mesurer.
5. [ ] [TECH] Fondamentaux : grammaire, raccords, 180°, montage son, J-cut/L-cut → skill `montage-grammaire`
6. [ ] [ART] Atelier rythme : un même matériau monté sur trois tempos (Bass / Gondry / Cooper — cf. `montage-references` B) ; mesure avec scdet
7. [ ] [TECH] Blender pour la vidéo : skill `montage-blender` (rendu CLI, Cycles vs Eevee headless, compositing, geometry nodes) — base déjà pratiquée dans l'atelier 01 ; tester Eevee en headless
8. [~] [TECH] DaVinci Resolve → `montage-resolve` v1 (session 2 : nodes, RCM, API d'après le README 2022-2023). Reste : Fusion, Fairlight, README 19-20 (objets Graph ? ColorGroup ?), atelier couleur « même plan, trois étalonnages » traduit en arbre de nodes.
9. [~] [ART] Narration par format → `montage-formats` v1 (session 3), cf. 0e.
10. [~] [TECH] `montage-premiere` v1 écrit (session 3, théorique). Fait en session 4 : marqueurs de temps importables (`labo/marqueurs/beats_xml.py`, XML FCP7, ~10 ms). Reste : lire les pages Adobe en entier (WebFetch 403), Color mode, ExtendScript, raccourcis Q/W ; `beats_xml.py` testé sans grosse caisse et avec levée (M1 par l'accent, avertissement si ambigu) ; reste : tempo variable, vraie musique.
11. [~] [TECH] `montage-preparation-tournage-vfx` v1 écrit (session 2, théorique). Reste : tests de keying et de tracking sur des médias CC0 (avec BACKLOG 14).
12. [x] [TECH] `montage-pilotage-mcp` v1 + état public des MCP (session 5, `sources/mcp-etat-public-2026-10.md`, tests 21-31). Reste [ ] : revérifier tous les 2 mois (info volatile).
13. [ ] [ART] Son : atelier « même image, trois bandes son » (avec, contre, silence) ; fiches Murch sound design, Ben Burtt, Gary Rydstrom
14. [~] [TECH] Keying : labo à vérité terrain fait (session 2, `labo/keying/`). Reste : tracking, roto, keyers à alpha doux, compositing Blender/Fusion
15. [~] [TECH] `montage-workflows` v1 (session 4) + labo aller-retour OTIO (`labo/workflows/`). Reste : tester vitesses, recadrages, nests, audio multipiste dans l'aller-retour XML ; AAF (pyaaf2 ?) ; proxies et cadence variable des téléphones avec ffmpeg.
16. [~] [TECH] Labo fondus : session 4, `variance.py` (écart au milieu + détecteur noir) = 3/4, 0 faux positif ; hypothèse du creux de variance réfutée. 2e vérité terrain indépendante : 4/4, 0 faux positif (mêmes seuils). Reste : fusionner les segments du fondu au noir, chroma, puis matériau CC0 réel.
17. [~] [ART] Culture : faits : Elastic (*Game of Thrones*), ManvsMachine, Buck, Åkerlund, Gavras (s5) ; Murai, Honda « Cog » (s2), Varda *Les Glaneurs*, Spike Jonze (s3), Marker *Sans soleil*, Morris *The Thin Blue Line* (s4). Reste : clips ( Jonas Åkerlund, et clips de rap français proches de Ziak) ; motion design de studio (Buck, ManvsMachine, Elastic) ; pub (Apple *1984*)
18. [~] [ART] IA : faits vérifiés en session 4 (Sora, AI Act art. 50 non reporté, Wan 2.2 dernier ouvert, LTX-2). Reste : fiches d'œuvres IA, grille « est-ce que ça fait IA ? », relire le texte de l'Omnibus sur EUR-Lex.
19. [ ] [ART] Relire les skills artistiques après l'examen n°1 ; fusionner les doublons (regard / motion-design / references se recoupent sur « un signe »)

20. [x] [ART] Examen créatif n°2 « Marée basse » (clip de rap) : 14/20 (session 2). **Examen n°3 en session 5 ou 6** : documentaire ou corporate.
20b. [~] [ART] Atelier 04 « ce que la marée découvre » (session 4 : v1-v3, `atelier/04-maree-decouvre/`). v2b = réf. mystère, v6 = meilleur suspense (son : ressac puis gouttes, -18,4 LUFS). Reste : animer le plan sous-marin (particules, reflet ondulant), variante 9:16, et un plan d'ouverture sous-marin qui se lise sans hésiter. : une image-concept propre au sujet (révélé par l'examen n°2), 10 s Blender, l'eau qui se retire et découvre un objet.
21. [ ] [ART] Atelier « causalité » : reprendre le principe de Honda « Cog » (chaque coupe montre une cause et son effet) sur 10 s de Blender, sans musique, seulement les sons des objets.
22. [x] [TECH] `montage-blender` v1 écrit (session 2) ; reste Eevee headless, geometry nodes, compositing, camera tracking — : consigner ce que l'atelier 02 a appris (cadre et fenêtres de source calculées depuis la cinématique, cache d'images par caméra, ~1 image/s en Cycles 270×480 12 échantillons + débruitage).

23. [ ] [ART] Atelier « le montage se retire » (principe Jonze) : un corps ou un objet qui produit lui-même le rythme (pendule, danse d'un objet Blender), 3 plans max sur 15 s, comparé à une version kinetic.
24. [ ] [ART] Atelier « voix écrite après » (principe Varda) : monter d'abord 20 s d'images glanées (plans des ateliers), écrire ensuite une voix off qui relie ; critique : la voix illustre-t-elle ou relie-t-elle ?

25. [ ] [ART] Atelier « Spirale » (principe Marker) : 30 s qui font revenir 3 motifs des ateliers 01-04, chaque retour changeant de sens ; voix écrite après.
26. [~] [ART] Atelier « Versions » (principe Morris) — entamé en session 5 (`atelier/06-versions/`) : la même action Blender (un objet qui tombe) rejouée 3 fois avec un détail changé ; la musique en boucle ; critique : est-ce qu'on doute ?
27. [x] [TECH] AAF par familles avec `pyaaf2`, relu identique par OTIO (session 5). Reste [ ] : poignées, gain, fondus ; AAF depuis l'EDL JSON d'une vraie pièce (06).

28. [x] [ART] Examen n°4 « La Veilleuse » (fiction, 14/20, session 5). **Examen n°5 en session 8** : documentaire long ou pub 6 s. Révélé : [ ] fiches *Aftersun* (Wells, montage Blair McClendon) et *Les Revenants* ; [ ] surround et présence hors champ (`montage-son-et-emotion`) ; [ ] spec PAD Arte sourcée.
29. [ ] [ART] Culture : rap français proche de Ziak (réalisateurs de clips : Kourtrajmé au-delà de Gavras, clips de PNL, Freeze Corleone) ; clips Åkerlund et Gavras à confronter à Murai dans `montage-regard` (quand monter le choc).
30. [x] [TECH] Resolve API 19-21.1 versée dans `montage-resolve` (session 5 ; Graph, ColorGroup, dépréciations, Studio requis en 21.1). Reste [ ] : Fusion, Fairlight par script.
31. [ ] [ART] Atelier « causalité » et atelier « le montage se retire » : réutiliser la scène de la pièce 06 (table, tasse) comme plateau.

## Fait (trace)
- [x] [ART] Session 5 : atelier 05 « Trois étalonnages » (6 versions), fiches Elastic, ManvsMachine, Buck, Åkerlund, Gavras
- [x] [TECH] Session 5 : état public des MCP, AAF par familles (pyaaf2 + OTIO), scintillement d'une clé
- [x] [TECH] Session 4 : loudness hors plateformes, marqueurs de temps, `montage-workflows` + OTIO, fondus 3/4, vérif IA
- [x] [ART] Session 4 : fiches Marker et Morris, atelier 04 v1-v3
- [x] [ART] Atelier 03 v1-v3, culture Varda et Jonze (session 3)
- [x] [TECH] `montage-pilotage-mcp`, `montage-premiere` v1, labo fondus (session 3)
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
