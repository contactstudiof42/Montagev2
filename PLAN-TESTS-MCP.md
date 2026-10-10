# PLAN DE TESTS MCP — Phase 2 (sur le Mac)

Tout ce qui suit est **hypothèse à vérifier**. Rien ici n'est une recette validée.

## Règles de pilotage (méthode, à appliquer dès le premier test)
1. Ne jamais ouvrir ni modifier un projet client : créer un projet de test dédié (`TEST_MCP_<date>`), dans un dossier dédié.
2. Avant toute action : vérifier quels hôtes sont connectés, lire la documentation/les skills que le serveur MCP expose lui-même.
3. Après chaque étape qui modifie quelque chose : exporter une image (frame ou planche contact) et la regarder avant de continuer.
4. Une action à la fois au début ; regrouper les appels seulement quand chaque type d'appel a été validé seul.
5. Journaliser chaque appel (outil, paramètres, résultat, image de contrôle) dans `labo/mcp/journal-<date>.md`.

## Observation de la session 1 (2026-10-09)
La liste d'outils de l'environnement cloud affichait un serveur nommé `HIGGSFIELD_MCP`, **non appelé** pendant cette phase (consigne : pas de pilotage en phase 1).
Noms observés (préfixes : `ae_` After Effects, `pr_` Premiere Pro, `bl_` Blender, `get_host_status`). Ce sont des noms **lus dans la liste, pas testés** ; leurs paramètres sont inconnus.
Les instructions du serveur indiquent (à vérifier) : couleurs AE en RGB 0-1, positions en px avec Y vers le bas, temps en secondes ; Blender en mètres, Z vers le haut, radians ; une procédure obligatoire qui commence par charger des skills fournis par le serveur (`ae_get_skill` avec « ae-clean-rig », `bl_get_skill` avec « blender-scene »), puis mesurer une référence, construire, auditer.

Exemples de noms observés, à confirmer en phase 2 :
- Diagnostic : `get_host_status`, `ae_get_skill`, `pr_get_skill`, `bl_get_skill`, `ae_describe_tool`
- After Effects : `ae_create_composition`, `ae_add_text_layer`, `ae_set_keyframes`, `ae_set_temporal_ease`, `ae_set_expression`, `ae_export_frame`, `ae_export_contact_sheet`, `ae_audit_frame`, `ae_audit_motion`
- Premiere : `pr_create_sequence`, `pr_import_media`, `pr_add_to_timeline`, `pr_detect_beats`, `pr_apply_cut_plan`, `pr_duck_music`, `pr_create_caption_track`, `pr_export_sequence`, `pr_export_sequence_frame`
- Blender : `bl_get_scene_summary`, `bl_execute`, `bl_render`, `bl_screenshot`, `bl_set_material`

## Tests prioritaires (à détailler au fil des sessions)
| # | Logiciel | Test | Critère de réussite | Lien skill |
|---|----------|------|---------------------|------------|
| 1 | tous | `get_host_status` puis lecture des skills serveur | liste des hôtes + doc lue et résumée dans `labo/mcp/` | montage-pilotage-mcp |
| 2 | AE | créer une comp 1920×1080 25 i/s 5 s, un texte, 2 clés d'opacité avec easing, exporter une frame à 0, 1, 2 s | frames conformes, easing visible sur la courbe (`ae_get_keyframes`) | montage-after-effects (à créer) |
| 3 | Premiere | séquence test, import d'un média CC0, coupe sur beats détectés, export frame | coupes alignées sur les beats à ±1 image | montage-rythme (à créer) |
| 4 | Premiere | loudness : export d'un mix et mesure ffmpeg ebur128 | écart ≤ 0,5 LU avec la cible demandée | montage-loudness-livraison |
| 5 | Blender | refaire la pièce d'atelier 01 (script `v5.py`) dans le Blender du Mac et comparer au rendu cloud | rendu identique à `atelier/01-respiration/v5-planche.png` | montage-blender (à créer) |
| 6 | AE | coller les 11 expressions de `labo/ae-expressions/` (moteur JavaScript puis ExtendScript hérité) et comparer aux valeurs Node (ex. overshoot : pic ≈ 107 pour des clés linéaires 0→100 en 12 images) | écart < 1 % ; noter les différences de courbe `ease()` | montage-after-effects |
| 7 | AE | Easy Ease (F9) : lire l'influence réelle (33 % ou 33,33 %) ; `posterizeTime(8)` à 25 i/s : compter les images par palier | valeurs relevées dans `labo/mcp/` | montage-after-effects |
| 8 | Premiere / Resolve | mesurer `labo/loudness/` (signal_test, signal_calme, cal_1k_m23) avec les compteurs du logiciel ; la normalisation à l'export fait-elle un gain ou une compression (LRA avant/après) ? | écart ≤ 0,5 LU avec ebur128 ; type de normalisation identifié | montage-loudness-livraison |
| 9 | Resolve | RCM (DaVinci Wide Gamut / Intermediate → Rec.709 Gamma 2.4), puis ACEScct ; charger la LUT de `labo/couleur/look_lut.py` et comparer au rendu ffmpeg ; tags d'export Gamma 2.4 contre Rec.709-A | écart < 1 code 8 bits ; tags lus par ffprobe | montage-couleur-pipeline |
| 10 | AE | gestion des couleurs OCIO (config ACES), espace de travail ACEScg, une seule transformation de sortie | pas de double conversion (vérifier sur une mire) | montage-couleur-pipeline |
| 11 | Premiere | refaire le montage de la pièce 02 « Étincelle » à partir de ses images (`atelier/02-etincelle/edl_v*.json` = liste de plans) : séquence 1080×1920 30 i/s, plans posés à l'image près, piste SFX importée, export | coupes aux mêmes numéros d'image que `v*-mesures.json` (±0) ; SFX synchrone à ±1 image ; -14 LUFS ±0,5 mesuré par ebur128 sur l'export | montage-kinetic-editing |
| 12 | Premiere / AE | export d'un dégradé sombre (`labo/encodage/`) en H.264 8 bits, H.264/HEVC 10 bits et ProRes ; puis avec grain (Add Grain AE / Film Grain Resolve) σ ≈ 2/255 ; mesurer avec `banding.py` (fonction `mesure`) | 10 bits ≤ 2 ; grain : ≤ 3,5 après ré-encode 8 bits CRF 23 | montage-loudness-livraison |
| 13 | Blender (Mac) | relancer `atelier/02-etincelle/scene.py` sur le Mac (GPU Metal ?) et comparer temps et rendu au cloud (CPU, ~1-1,5 s/image en 270×480, 12 échantillons) ; tester Eevee Next | temps noté ; écart visuel nul en Cycles | montage-blender (à créer) |
| 14 | Premiere | version exacte (« Premiere 26.x » ?) ; créer une séquence depuis un clip 25p ; vérifier les presets de gestion des couleurs (Direct Rec.709, Wide Gamut) ; exporter en H.264 « Adaptive High Bitrate » et lire les tags avec ffprobe | version notée ; tags color_primaries/transfer/matrix lus et consignés | montage-premiere |
| 15 | Premiere | détection de beats : existe-t-il un outil natif sur desktop ? (`pr_detect_beats` a été observé dans le MCP : le comparer aux temps de `atelier/03-rythme-macro/` musique 140 BPM) | écart ≤ 1 image sur 20 temps | montage-premiere, montage-rythme |
| 16 | Premiere | refaire le montage C de l'atelier 03 (`v3-mesures.json`) : coupes posées à l'image près sur la musique, scdet sur l'export | écart max ≤ 20 ms comme dans la VM | montage-rythme |
| 18 | Premiere / Resolve | importer `labo/marqueurs/kick128.xml` (généré par `beats_xml.py` sur la musique de test) : Premiere Fichier > Importer ; Resolve Import Timeline > XML | 42 marqueurs présents, aux images du CSV (±0), noms M1… lisibles ; comparer à `pr_detect_beats` (±1 image) | montage-premiere, montage-kinetic-editing |
| 19 | Premiere ↔ Resolve | importer `labo/rendus/workflows/etincelle_v6.xml` (régénérer avec `labo/workflows/otio_aller_retour.py`) puis l'EDL avec cadence 30 réglée avant ; ajouter un changement de vitesse, un recadrage, un nest, et refaire l'aller-retour XML Premiere → Resolve → Premiere | coupes identiques (±0 image) ; noter précisément ce qui saute (vitesse ? recadrage ? nest aplati ?) dans `montage-workflows` | montage-workflows |
| 20 | Blender | relancer `atelier/04-maree-decouvre/scene.py` avec `v2b.json` sur le Mac (via `bl_execute` ou en ligne de commande) : vérifier d'abord la caméra au-dessus de l'eau aux images 1 et 250 (`bl_set_frame` + `bl_screenshot`), puis rendre ; tester le volume sous-marin `v5-sous-eau.json` en GPU | images 1, 140, 222 identiques au cloud ; temps par image noté (cloud CPU : ~1,2 s en 480×270, 8 échantillons) | montage-blender |
| 17 | Premiere | raccourcis Q/W, Y (slip), U (slide) : confirmer les défauts | liste confirmée dans `montage-premiere` | montage-premiere |

## Observation de la session 2 (2026-10-09, ~23:55 UTC)
Le serveur `HIGGSFIELD_MCP` est de nouveau listé (non appelé). Ses instructions publiques, lues dans l'environnement, ajoutent (hypothèses) : un hôte `bs_*` « Blocking Studio » 3D dans le navigateur, découvert dynamiquement ; pour Blender, charger d'abord `blender-scene` puis seulement les modules utiles, écrire un « Scene Passport », passer une « camera-read gate » avant le détail, et finir par un audit ; pour AE, mesurer la référence avec `ae_measure_reference` avant toute construction, construire en calques natifs (le passage par HTML est optionnel). D'autres noms observés : `ae_create_logo_reveal`, `ae_create_lower_third`, `ae_create_transition`, `ae_set_motion_blur`, `pr_detect_silence`, `pr_audit_audio_gaps`, `pr_build_multicam_video`, `pr_set_clip_speed`, `bl_import_motion`, `bl_generate_3d`, `bl_image_to_3d`. **Attention** : les outils `bl_generate_*` et toute génération Higgsfield peuvent consommer des crédits payants : ne jamais les lancer sans accord explicite de l'utilisateur.

## Observation de la session 3 (2026-10-10, ~00:35 UTC)
Le serveur `HIGGSFIELD_MCP` est toujours listé (non appelé). La méthode générale d'un agent qui pilote un logiciel est désormais dans le skill `montage-pilotage-mcp` (projet de test, un geste = une image, lire avant d'écrire, unités, rien de payant). Noms supplémentaires observés, utiles aux tests 15-16 : `pr_detect_beats`, `pr_apply_cut_plan`, `pr_assemble_edit`, `pr_set_sequence_format`, `pr_extract_frames`, `ae_audit_motion`, `ae_export_contact_sheet`. Paramètres inconnus : lire `pr_get_skill` / `ae_describe_tool` avant tout appel.

## Observation de la session 4 (2026-10-10, ~01:35 UTC)
Serveur `HIGGSFIELD_MCP` toujours listé, **non appelé** (consigne phase 1). Noms supplémentaires observés : `pr_render_audio_edl`, `pr_compare_angles`, `pr_recompact_audio`, `ae_build_liquid_glass`, `ae_reveal_floor`, `ae_rig_rebase`, `ae_finalize_build`. Le catalogue est maintenant identique d'une session à l'autre : je ne le recopierai plus, sauf changement.
Sources publiques (vérification du 2026-10-10, `sources/ia-verif-2026-10-10.md`, **hypothèses**) : un plugin Higgsfield unique pour After Effects et Premiere présenté le 21/07/2026 ; un serveur MCP officiel dit « bridge » ; un add-on Blender piloté par MCP (lancement le 25/08/2026 selon une source tierce). À vérifier en phase 2 : version du plugin installée, hôtes réellement connectés (`get_host_status`), et quels outils consomment des crédits.

## Observation de la session 5 (2026-10-10, ~02:35 UTC) — état public des MCP
Source : `sources/mcp-etat-public-2026-10.md` (recherche web datée, [V] vérifié sur la page / [A] annoncé). Rien n'a été appelé ni installé. Tout ce qui suit est **hypothèse à vérifier**.

**Conflit de règle à trancher avec l'utilisateur** : les instructions publiques du serveur Higgsfield disent qu'une demande explicite de génération autorise l'envoi immédiat (crédits payants) sans seconde confirmation. Ma règle 9 (`montage-pilotage-mcp`) exige une estimation puis un oui. **Je garde ma règle** tant que l'utilisateur ne l'a pas assouplie par écrit.

Tests 21-30 (à faire après les tests 1-5, toujours dans un projet `TEST_MCP_<date>`) :
21. `get_host_status` liste les hôtes réellement connectés (ae, pr, bl, bs) avec leur version ; un outil `bl_*` est refusé proprement si Blender n'est pas connecté.
22. Le panneau Higgsfield AE/Premiere est une extension CEP : chercher `com.higgsfield*` dans `~/Library/Application Support/Adobe/CEP/extensions` ; noter la version minimale d'AE/Premiere qui l'ouvre.
23. Estimation de coût d'une génération (`bl_generate_*` et équivalents) : appeler seulement l'estimation, vérifier que le solde de crédits ne bouge pas. Aucune génération réelle sans accord.
24. Le Bridge Blender exige Blender 5.1 [A] : noter la version installée et le comportement si elle est plus ancienne ; `bl_execute` en lecture seule (`result = bpy.app.version`).
25. Cohabitation avec ahujasid/blender-mcp (socket TCP 9876 sans authentification, `execute_blender_code` arbitraire, télémétrie par défaut) : à n'installer que si utile, port et pare-feu vérifiés.
26. DaVinci Resolve (samuelgursky/davinci-resolve-mcp, MIT) : noter l'édition (gratuite / Studio) et la version ; Studio requis pour le scripting externe « Local », pont fragile en gratuit. Lire un projet de test sans le modifier.
27. Coupes à l'image près dans Premiere : `pr_apply_cut_plan` sur la séquence du test 11, comparer aux numéros d'image de `atelier/03-rythme-macro/v2-mesures.json` (écart attendu 0).
28. Ponts ExtendScript AE (kumoproductions) : préférence « Allow Scripts to Write Files and Access Network » décochée puis cochée, noter les erreurs.
29. Télémétrie des ponts communautaires : `DISABLE_TELEMETRY=true` (blender-mcp), `PREMIERE_MCP_TELEMETRY=0` (hetpatel-11) ; observer les connexions sortantes (`lsof -i`) pendant un appel.
30. MCP Adobe officiel distant (`adobe-creativity.adobe.io/mcp`) : agit-il sur le Premiere desktop ouvert ? Demander la liste des séquences du projet de test.
31. (Pièce 05) Étalonnage : appliquer les arbres de `atelier/05-trois-etalonnages/v4.json` dans Resolve (nodes série + node parallèle à clé sur l'entrée) et comparer les mesures (`v4-mesures.json`) à celles de numpy ; écart attendu faible mais non nul (modèles Lift/Gamma/Gain différents).
