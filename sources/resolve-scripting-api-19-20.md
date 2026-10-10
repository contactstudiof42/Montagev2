# API de scripting DaVinci Resolve : changements de 18.x à 21.1 (état au 2026-10-10)

Légende : [V] lu dans un texte officiel Blackmagic ou dans une copie fidèle du README/CHANGELOG/.pyi livré dans `Developer/Scripting`.
[A] vient d'un tiers (presse, projet communautaire). Une ligne « signature [V] / version [A] » veut dire que la signature est
tirée du README et que la version d'apparition vient de notes de version relayées par la presse.
Rien n'est inventé : ce qui n'a pas de source n'est pas listé.

## Sources (abréviations)
- **W23** : README du 18 juillet 2023 (≈ 18.5), page de base pour la comparaison. https://wiki.dvresolve.com/developer-docs/scripting-api
- **G25** : README « Last Updated: 7 May 2025 » (Resolve 20.0), copie intégrale. https://gist.github.com/Manouchehri/e32461dccd824167bac8358bb21c8040
- **R26** : README « Last Updated: 24 Jul 2026 » (21.0.4), copie dans un dépôt tiers. https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/docs/reference/resolve_scripting_api.txt
- **CL** : `Developer/Scripting/CHANGELOG.md` « Last Updated: 1 Sep 2026 » (couvre 20.0 à 21.1), même dépôt, copié depuis Studio 21.1.0.14. https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/docs/reference/resolve_scripting_changelog_21.1.md
- **PYI** : `DaVinciResolveScript.pyi` (stub typé livré avec 21.1, non modifié selon le dépôt). https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/docs/reference/DaVinciResolveScript.pyi
- **BMD21** : page officielle « About DaVinci Resolve 21 ». https://www.blackmagicdesign.com/support/content/readme/59dd4eef1f4941c29fb8dc48b33f5c87
- **N1864** (18.6.4) : https://www.newsshooter.com/?p=214323 · **RS19b2** (19.0 bêta 2) : https://www.redsharknews.com/davinci-resolve-19-moves-on-to-public-beta-2
- **N1902** (19.0.2) : https://www.newsshooter.com/2024/10/01/blackmagic-design-davinci-resolve-19-0-2-update/ · **N191** (19.1) : https://www.newsshooter.com/2024/11/11/blackmagic-design-davinci-resolve-19-1-update-released/
- **DP211** : https://digitalproduction.com/2026/09/08/resolve-21-1-adds-mcp-and-finally-gets-presets/

Méthode : j'ai extrait les noms de méthodes de W23, G25 et R26 et comparé les listes ; les signatures ci-dessous sont recopiées de G25/R26/PYI.
Note : les copies G25, R26, CL et PYI sont hébergées par des tiers. Je les classe [V] parce qu'elles reproduisent le texte livré, avec date et en-tête d'origine.

## 1. Changements de structure (ce qui casse un script 18.x)
- **Nouvelle classe `Graph`** (19.0 bêta 2, « Ability to query timeline, clip and group node graphs » RS19b2 [A]). Signatures [V] G25 :
  `GetNumNodes() --> int` · `SetLUT(nodeIndex, lutPath) --> Bool` · `GetLUT(nodeIndex) --> String` · `GetNodeLabel(nodeIndex) --> string`
  `GetToolsInNode(nodeIndex) --> [toolsList]` · `SetNodeEnabled(nodeIndex, isEnabled) --> Bool`
  `SetNodeCacheMode(nodeIndex, cache_value) --> Bool` · `GetNodeCacheMode(nodeIndex) --> cache_value` (cache : 19.1, N191 [A])
  `ApplyGradeFromDRX(path, gradeMode) --> Bool` (gradeMode 0 = sans keyframes, 1 = aligné sur le TC source, 2 = aligné sur la première image)
  `ApplyArriCdlLut() --> Bool` · `ResetAllGrades() --> Bool` (ces trois-là : 19.1, « Apply grade from DRX and CDL LUT to layers from the Graph API », « Reset all grades and nodes », N191 [A])
- **Points d'entrée vers un Graph** [V] G25 :
  `Timeline.GetNodeGraph() --> Graph` (graphe timeline) · `TimelineItem.GetNodeGraph(layerIdx) --> Graph` (layerIdx facultatif, numéroté à partir de 1, au plus `project.GetSetting("nodeStackLayers")`)
  `ColorGroup.GetPreClipNodeGraph() --> Graph` · `ColorGroup.GetPostClipNodeGraph() --> Graph`
- **Dépréciés sur TimelineItem** [V] G25 (section « Deprecated ») : `GetNumNodes()`, `SetLUT(nodeIndex, lutPath)`, `GetLUT(nodeIndex)`, `GetNodeLabel(nodeIndex)`. Il faut passer par `item.GetNodeGraph()`.
  `TimelineItem.SetCDL([CDL map])` **reste** dans la liste active (NodeIndex numéroté à partir de 1) [V] G25 et R26.
- **`Timeline.ApplyGradeFromDRX(path, gradeMode, [items])`** figure dans W23 [V], mais n'apparaît plus ni dans G25 ni dans R26 [V], et pas non plus dans la liste des fonctions dépréciées. Le seul `ApplyGradeFromDRX` documenté se trouve désormais sur `Graph`.
- **Python 2 n'est plus pris en charge** et les « overloaded function signatures are deprecated » en 21.1 [V] CL. (R26, qui documente 21.0.4, cite encore Python 2.7 et Python >= 3.6.)

## 2. Étalonnage : ColorGroup, LUT, galerie
- **Nouvelle classe `ColorGroup`** (19.0 bêta 2, « Support for managing clip color groups » RS19b2 [A]). Signatures [V] G25 :
  `GetName() --> String` · `SetName(groupName) --> Bool` · `GetClipsInTimeline(Timeline=CurrTimeline) --> [TimelineItem]`
  `Project.GetColorGroupsList() --> [ColorGroups...]` · `Project.AddColorGroup(groupName) --> ColorGroup` · `Project.DeleteColorGroup(colorGroup) --> Bool`
  `TimelineItem.GetColorGroup() --> ColorGroup` · `TimelineItem.AssignToColorGroup(ColorGroup) --> Bool` · `TimelineItem.RemoveFromColorGroup() --> Bool`
- **`TimelineItem.ExportLUT(exportType, path) --> Bool`** (19.0 bêta 2, « Ability to export clip LUTs » RS19b2 [A]) [V] G25. Valeurs de exportType :
  `resolve.EXPORT_LUT_17PTCUBE`, `EXPORT_LUT_33PTCUBE`, `EXPORT_LUT_65PTCUBE`, `EXPORT_LUT_PANASONICVLUT`.
- **Export de timeline ALE / ALE+CDL** : `resolve.EXPORT_ALE` et `resolve.EXPORT_ALE_CDL` pour `Timeline.Export(fileName, exportType, exportSubtype)` [V] G25 (absents de W23). Apparition en 19.0 bêta 2 [A] RS19b2.
- **Galerie** (19.1, « Create gallery albums », N191 [A]) [V] G25 : `Gallery.GetGalleryPowerGradeAlbums() --> [galleryStillAlbum]`, `CreateGalleryStillAlbum() --> galleryStillAlbum`, `CreateGalleryPowerGradeAlbum() --> galleryStillAlbum`.
- **Mode de keyframe** [V] G25 : `Resolve.GetKeyframeMode() --> keyframeMode`, `Resolve.SetKeyframeMode(keyframeMode) --> Bool`. Version exacte non sourcée (entre 18.5 et 20.0).
- **Cache de clip** (19.1, N191 [A]) [V] G25 : `TimelineItem.GetIsColorOutputCacheEnabled()`, `GetIsFusionOutputCacheEnabled()`, `SetColorOutputCache(cache_value) --> Bool`, `SetFusionOutputCache(cache_value) --> Bool` (valeurs auto/activé/désactivé pour Fusion).
- **Dolby Vision** [V] G25 : `Timeline.AnalyzeDolbyVision([timelineItems]=[], analysisType=NONE) --> Bool` (`resolve.DLB_BLEND_SHOTS`). Version exacte non sourcée.
- **20.2** [V] CL/R26 : `TimelineItem.ResetAllNodeColors() --> Bool`.

## 3. Montage, pool de médias, métadonnées
- **18.6.4** [V] G25 pour les signatures, version [A] N1864 : `Timeline.ConvertTimelineToStereo() --> Bool` · `MediaPool.CreateStereoClip(LeftMediaPoolItem, RightMediaPoolItem)`
  `ProjectManager.CreateCloudProject({cloudSettings}) --> Project`, `ImportCloudProject`, `RestoreCloudProject` · `Timeline.CreateSubtitlesFromAudio({autoCaptionSettings}) --> Bool` (dictionnaire de réglages ajouté)
- **19.0 bêta 2** : audio mapping, « query media audio track mapping » [A]. Signatures [V] G25 : `MediaPoolItem.GetAudioMapping() --> json formatted string`, `TimelineItem.GetSourceAudioChannelMapping() --> json formatted string`
- **19.0.2** (N1902 [A]), signatures [V] G25 :
  `MediaPoolItem.GetThirdPartyMetadata(metadataType=None) --> string|dict` · `SetThirdPartyMetadata(metadataType, metadataValue)` / `SetThirdPartyMetadata({metadata}) --> Bool`
  `TimelineItem.GetSourceStartFrame()/GetSourceEndFrame() --> int` · `GetSourceStartTime()/GetSourceEndTime() --> float`
  `MediaPool.GetSelectedClips() --> [MediaPoolItems]` · `MediaPool.SetSelectedClip(MediaPoolItem) --> Bool` ; position de clip et AppendToTimeline à la sous-image près (N1902 [A])
- **19.1** (N191 [A]), signatures [V] G25 :
  `ProjectManager.LoadCloudProject({cloudSettings}) --> Project`
  `MediaPoolItem.GetMarkInOut() --> {mark}` · `SetMarkInOut(in, out, type="all") --> Bool` · `ClearMarkInOut(type="all") --> Bool` (même trio sur Timeline)
  `MediaPool.AutoSyncAudio([MediaPoolItems], {audioSyncSettings}) --> Bool` (au moins une vidéo et un audio)
  `Project.DeleteRenderPreset(presetName) --> Bool` · `Project.GetQuickExportRenderPresets() --> [preset_name..]`
  `Project.RenderWithQuickExport(preset_name, {param_dict}) --> {status info}` (clés : TargetDir, CustomName, VideoQuality, EnableUpload)
- **Version non sourcée (entre 18.5 et 20.0)** [V] G25 : `TimelineItem.GetLinkedItems() --> [TimelineItems]` · `TimelineItem.GetTrackTypeAndIndex() --> [trackType, trackIndex]` · `Timeline.GetTrackSubType(trackType, trackIndex) --> string`
- **20.0** [V] CL : `MediaPoolItem.LinkFullResolutionMedia(fullResMediaPath) --> Bool` · `ReplaceClipPreserveSubClip(filePath) --> Bool` · `MonitorGrowingFile() --> Bool`.
  `TimelineItem.GetRightExtents` change de sens : il renvoie désormais l'écart entre le point de montage droit et la fin du média [V] CL.
- **20.1** [V] CL : `Timeline.GetVoiceIsolationState(trackIndex)` · `Timeline.SetVoiceIsolationState(trackIndex, {VoiceIsolationState})` ({isEnabled, amount}).
  Sur TimelineItem, R26 documente `GetVoiceIsolationState()` et `SetVoiceIsolationState({VoiceIsolationState})` [V], alors que CL écrit `EnableVoiceIsolationState`. Les deux textes officiels divergent, à vérifier.
- **20.2** [V] CL/R26 : `SetName(name) --> bool` sur MediaPoolItem et TimelineItem. Réglages de rendu `"ExportSubtitle": Bool` et `"SubtitleFormat"` (« BurnIn », « EmbeddedCaptions », « SeparateFile »).
- **20.2.2** [V] CL/R26 : `Resolve.GetFairlightPresets() --> [presetNames...]` · `Project.ApplyFairlightPresetToCurrentTimeline(name) --> Bool` · `ProjectManager.CreateProject(…, mediaLocationPath)` facultatif.

## 4. Resolve 21 (sortie ; 21.1 au 1er septembre 2026)
- **21.0** [V] CL/R26 :
  `Folder|MediaPoolItem.TranscribeAudio(useSpeakerDetection=None) --> Bool`
  `PerformAudioClassification() --> Bool` / `ClearAudioClassification`
  `RemoveMotionBlur({deblurOption})`
  `AnalyzeForIntellisearch(identifyFaces, isBetterMode) --> Bool`
  `AnalyzeForSlate(markerColor)`
  `Resolve.DisableBackgroundTasksForCurrentResolveSession() --> None`
  `Project.GenerateSpeech({speechGenerationSettings}, timecode) --> MediaPoolItem`
- **21.0.4** [V] CL/R26 : `Timeline.GetSelectedClips() --> [items...]` · `MediaPoolItem.GetTimeline()` · nouvelles options de `SetRenderSettings` (poignées, étendue complète, incrustation de données)
  Préréglages utilisateur : `GetLayoutPresetList`, `GetBurnInPresetList`/`DeleteBurnInPreset`, `Save|Load|Delete|Import|ExportUserPreferencesPreset` · `ProjectManager.GetProjectAttributesInCurrentFolder()`
- **21.1** [V] CL, signatures [V] PYI :
  `MediaPool.CreateMulticamClip(clips, multicamOptions) --> list[MediaPoolItem]` · `TimelineItem.FlattenMulticam`, `PerformMulticamSmartSwitch` · `Timeline.AutoAlignClips(timelineItems, autoAlignOptions=None) --> bool`
  `TimelineItem.AddTransition(transitionOptions) --> TimelineItem | None` · `TimelineItem.GetFades()/SetFades(fades)` · `TimelineItem.GetSpeed()/SetSpeed(speedOptions)` · `GetType`
  `Timeline.Get|SetOutputBlanking` · `Timeline.GetNormalizeAudioModes()` · `Timeline.NormalizeAudioLevel(timelineItems, normalizeAudioOptions=None) --> bool`
  `MediaPoolItem.GetTranscription(useNestedClipTranscription=False)` · `MediaPoolItem.SetAudioMapping` · `TimelineItem.SetSourceAudioChannelMapping`
  `resolve.ValidateDCTL(dctlSource) --> str | None` · `resolve.EncryptDCTL(inputPath, options=None) --> bool` · `resolve.GetCurrentProject/GetCurrentTimeline/GetMediaPool/GetGallery`
  `Resolve.IsStudio() --> bool` (dans PYI, absent de G25 et R26)
  Préréglages clavier et de projet, `Project.UpdateRenderPreset`, `SetQuickExportEnabledForRenderPreset`, `GetAudioRenderCodecs`, `GetAudioRenderFormats`, clonage dans MediaStorage (`StartCloneMedia`…)

## 5. Contraintes d'exécution (gratuit / Studio, local / réseau)
- [V] G25/R26 : par défaut, les scripts se lancent depuis la Console (page Fusion) ou en ligne de commande. Les préférences permettent de limiter à la Console seule ou d'ouvrir l'accès au réseau local, avec un avertissement de sécurité.
- [V] R26, section « Studio and AI Scripting APIs » : l'API est un sur-ensemble commun gratuit/Studio. Un appel renvoie False si la fonction est réservée à Studio, si la machine ne satisfait pas les prérequis, ou s'il manque le pack Extras correspondant (IntelliSearch, Slate ID, Speech Generator, modèles de transcription étendus).
- [V] BMD21 (21.1) : « Advanced scripting now requires DaVinci Resolve Studio. » « We have moved the ability to script in Python to the Studio version. »
- [A] DP211 : sur la version gratuite 21.1, l'API reste accessible depuis la Console. Workflow Integrations, UIManager natif et scripting externe sont réservés à Studio. La 21.1 ajoute un serveur MCP (Claude, Claude Code, Codex) et « 20 additional APIs ».
  Contradiction : Puget Systems (2026-09-10, connu seulement par un résumé de recherche, non lu) parle d'un retrait complet du scripting de la version gratuite 21.1.
- [A] Dépôt samuelgursky/davinci-resolve-mcp (README) : avant 21.1 déjà, la version gratuite refusait `scriptapp("Resolve")` à un processus externe, quelle que soit la préférence. Sur la version gratuite 21.1, le menu Scripts ne liste plus les `.py`, alors que Lua reste listé.
