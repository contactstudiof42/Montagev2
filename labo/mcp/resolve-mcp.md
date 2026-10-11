# Le serveur MCP DaVinci Resolve — ce qu'il sait faire (session 0 de la phase 3, 2026-10-11)

Tout ce qui suit a été **exécuté** sur le Mac de Diego (Resolve Studio 21.1.1.10, base « TEST IA », projet `P3-BAC-A-SABLE`) sauf mention contraire. Détail de chaque appel : `journal-2026-10-11.md`.

## Les outils du serveur
| Outil | Rôle | Usage retenu |
|---|---|---|
| `get_resolve_status` | Resolve lancé ? version | au début de chaque session |
| `launch_resolve` | lance Resolve | non utilisé (déjà lancé) |
| `get_whats_new(since)` | changelog après une version | lu depuis 19.1 : rien d'annoncé après 21.0.4 |
| `get_scripting_api` / `search_scripting_api` / `get_scripting_docs` | stubs `.pyi` (API 21.1.1, Fusion, UI) et README officiel | **`as_file=True`** puis `grep` : rien ne coûte de contexte |
| `run_script` | Python 3.14 **sandboxé** : `resolve` et `project` injectés, ni fichiers ni `os` ; `result = …` renvoie des données ; 10 s par défaut, 60 s max | **tout le travail** passe par lui |
| `run_script_unsafe` | même chose sans bac à sable | **jamais utilisé**, inutile jusqu'ici |
| `list_luts` | liste le dossier de LUT de Resolve | lecture seule |
| `generate_lut` / `delete_lut`, `list_dctls` / `update_dctl` / `delete_dctl` | écrivent ou effacent dans les dossiers **partagés** de LUT et de DCTL de Resolve | **non utilisés** : hors des projets P3, à demander à Diego |

Le sandbox empêche d'écrire des fichiers depuis Python, mais **Resolve, lui, écrit** où on lui dit (`ExportCurrentFrameAsStill`, rendus, exports de timeline). C'est ainsi qu'on récupère les images de contrôle.

## Ce qu'il sait faire (vérifié)
- Créer un projet, régler résolution et cadence (projet ou timeline : `tl.SetSetting("useCustomSettings","1")` puis largeur, hauteur, cadence).
- Importer (ProRes, HEVC 4:2:2 10 bits UHD 50p, WAV, ProRes 4444 avec alpha « Straight »).
- Poser des plans **à l'image près** (`AppendToTimeline` : `startFrame` / `endFrame` en images **de la source**, `endFrame` **exclusif**, `recordFrame` absolu, la timeline commence à 90000 = 01:00:00:00). Vérifié contre ffmpeg : chaque image tombe juste.
- Couper / raccourcir / déplacer : **pas de lame ni de trim dans l'API** ; on supprime (`DeleteClips`) et on repose avec les nouveaux points. Marche, à l'image près.
- Niveau et fondus de clip son (`SetProperties({"AudioVolume": dB})`, `SetFades({"FadeIn": n, "FadeOut": n})`) : mesurés au rendu, exacts.
- Texte dans une police installée (SST) : **plan porteur sur une piste haute + Text+ dans sa composition Fusion**.
- CDL sur le nœud 1 (`SetCDL`), LUT du dossier de Resolve (`GetNodeGraph().SetLUT(1, "chemin/relatif.cube")`), activer / couper un nœud (`SetNodeEnabled`).
- Rendre (`SetCurrentRenderFormatAndCodec("mp4","H264")`, `SetRenderSettings`, `AddRenderJob`, `StartRendering`, `GetRenderJobStatus`) : 5 s rendues en 1 à 2 s ; tags bt709 posés.
- Recadrer du UHD 16:9 en 1080x1920 (`ZoomX/ZoomY` = 3,1605 pour remplir, `Pan` en pixels de timeline).
- Synchroniser un son externe à la forme d'onde (`MediaPool.AutoSyncAudio`, mode `AUDIO_SYNC_WAVEFORM`) : décalage trouvé à l'échantillon près.
- Ralenti (`SetSpeed({"Percentage": 50})`) : rush 50p dans une timeline 25p = une image source par image, sans interpolation.
- Flash blanc de 2 images, SFX à l'image, plan de fin avec alpha en surimpression, fondu enchaîné (`AddTransition`), masque Fusion fixe (ellipse).

## Ce qu'il ne sait pas faire (ou pas encore)
- **Créer un Magic Mask** : `CreateMagicMask("F")` renvoie False sans traits dessinés à la main ; il ne fait que lancer le suivi.
- **Animer dans Fusion** (clés d'une `BezierSpline`) : les clés ne prennent pas par ce pont. Donc pas de rampe de vitesse lisse, pas de texte animé par clés, pas de masque animé par script.
- **Courbes de vitesse / clés de retime** de la page Edit : absentes de l'API. Contournement : rampe **en paliers** (segments à 100, 85, 70, 60, 50 %).
- **Insérer un titre ou un générateur sans casser la timeline** : `InsertFusionTitleIntoTimeline` / `Insert…Generator` font un **montage par insertion** sur la piste active (coupe et pousse tout, son compris). À ne jamais utiliser sur une timeline montée.
- Charger une LUT hors du dossier de LUT de Resolve (chemin absolu ailleurs : False).
- Lire le compteur de loudness Fairlight, le bus, la page Fairlight : non exposés ; on mesure le rendu à ffmpeg.
- Voir l'image en direct : seulement des images exportées une par une.

## Fin de session 0 : qui fait quoi sur le projet Sony
**Ce que je peux faire seul** : importer les rushes et les sons ; synchroniser HF / perche avec le son caméra (forme d'onde) ; poser et recadrer chaque plan en 1080x1920 à l'image près ; ralentis à 50 % (vrais, depuis le 50p) ; rampes en paliers ; flashs, aplats ; textes en police SST (statiques) ; SFX et musique à l'image, niveaux, fondus ; fondus enchaînés ; plan de fin Sony avec alpha ; CDL et LUT du dossier de Resolve ; rendre et contrôler (images, loudness, QC).
**Ce que je ne peux pas faire** : animer quoi que ce soit par clés (texte cinétique, zoom ou punch-in animé, masque qui suit, rampe lisse) ; créer un Magic Mask ; construire un arbre de nœuds (je ne peux que régler le nœud 1 et charger une LUT ou un DRX préparé) ; régler le mix dans Fairlight (je mesure le rendu) ; entendre le son.
**Ce que Diego devra faire à la main** (ou préparer pour que je l'applique) : tracer les traits de Magic Mask sur les plans à détourer (je lance ensuite le suivi) ; les rampes de vitesse lisses et les animations par clés (zooms, textes animés), ou me donner des modèles (macros Fusion, PowerGrades / DRX) que j'applique ; écouter le mix et les SFX ; me dire si je peux déposer des LUT dans le dossier de LUT de Resolve.
