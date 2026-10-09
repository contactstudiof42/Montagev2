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
| 1 | tous | `get_host_status` puis lecture des skills serveur | liste des hôtes + doc lue et résumée dans `labo/mcp/` | montage-pilotage-mcp (à créer) |
| 2 | AE | créer une comp 1920×1080 25 i/s 5 s, un texte, 2 clés d'opacité avec easing, exporter une frame à 0, 1, 2 s | frames conformes, easing visible sur la courbe (`ae_get_keyframes`) | montage-after-effects (à créer) |
| 3 | Premiere | séquence test, import d'un média CC0, coupe sur beats détectés, export frame | coupes alignées sur les beats à ±1 image | montage-rythme (à créer) |
| 4 | Premiere | loudness : export d'un mix et mesure ffmpeg ebur128 | écart ≤ 0,5 LU avec la cible demandée | montage-loudness-livraison |
| 5 | Blender | refaire la pièce d'atelier 01 via `bl_execute` et comparer au rendu cloud | rendu identique à la planche contact `atelier/01-respiration/` | montage-blender (à créer) |
