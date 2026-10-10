---
name: montage-resolve
description: DaVinci Resolve — étalonnage par nodes (série, parallèle, layer mixer), gestion des couleurs (RCM, DaVinci Wide Gamut / Intermediate, ACEScct), page Deliver et rendus, Fusion, Fairlight, et automatisation par l'API de scripting Python (resolve.GetProjectManager, MediaPool.AppendToTimeline, SetRenderSettings, AddRenderJob, SetLUT, ApplyGradeFromDRX, export EDL/XML/AAF). Mots d'un étalonneur ou d'un monteur : « on passe en étalo », « arbre de nodes », « monter un look », « node de correction primaire », « qualifier la peau », « power window », « rendu en lot », « automatiser l'export », « script Resolve », « conformation », « faire un round-trip Premiere-Resolve ».
---

# DaVinci Resolve

Rôle : l'étape où l'image prend son **intention de couleur** (`montage-couleur-et-intention`) et où la chaîne technique est tenue propre (`montage-couleur-pipeline`). Ce skill dit comment l'organiser et l'automatiser.

## 1. Quand et pourquoi Resolve
- **Étalonnage** : c'est l'outil de référence (nodes, qualifications, tracking de fenêtres, gestion des couleurs de bout en bout). Premiere Lumetri suffit pour un corporate homogène ; dès qu'il y a un **look** à construire, une peau à protéger dans une dominante « fausse » (goût de l'utilisateur : Joker), des fenêtres à suivre, c'est Resolve.
- **Conformation / round-trip** : monter dans Premiere, exporter XML/AAF, étalonner dans Resolve, rendre en master 10 bits (cf. `labo/encodage/` : le 10 bits évite les bandes dans les noirs).
- **Automatisation** : rendus en lot, import et assemblage d'une liste de plans, application d'une LUT ou d'un grade à toute une timeline. C'est la porte d'entrée d'un agent en phase 2 si aucun MCP Resolve n'est branché.

## 2. Arbre de nodes de référence [THÉORIQUE — à éprouver en phase 2]
Ordre défendu (une idée par node, lisible par un autre étalonneur) :
1. **Entrée / normalisation** (si pas de RCM) : CST log caméra → espace de travail.
2. **Balance / exposition primaire** (Offset d'abord en log, puis Lift/Gamma/Gain).
3. **Contraste et courbe** (pivot réglé sur la valeur moyenne du sujet).
4. **Correction secondaire de peau** (qualifieur + fenêtre suivie) : c'est elle qui permet de garder un environnement vert sodium sans rendre le visage malade.
5. **Fenêtres de relief** (vignettage motivé, ramener l'œil sur le sujet).
6. **Look** (node parallèle ou LUT créative à opacité réglée par la clé du node).
7. **Grain / texture** en dernier (après le look, avant la sortie).
8. **Sortie** : CST ou ODT de l'espace de travail vers Rec.709 Gamma 2.4 (ou 2.2 pour le web, à décider : voir `montage-couleur-pipeline`).
Pourquoi cet ordre : corriger avant de styliser ; un look appliqué sur une image non balancée réagit différemment d'un plan à l'autre.

**Leçons de l'atelier 05 (étalonnage simulé en numpy, `atelier/05-trois-etalonnages/grade.py`)** [TESTÉ EN ATELIER, hors Resolve] :
- Une secondaire qui doit faire vivre une couleur ne se place **ni avant** un node qui écrase (elle est écrasée avec le reste) **ni après** (la couleur à qualifier n'existe plus) : on prend la **clé sur l'entrée** (node parallèle ou clé externe branchée sur la source) et on mélange en sortie. Mesuré : 0 % → 1,7 % de pixels chauds, 0 % hors de l'objet.
- Des gammas un peu différents par canal sur une image grise (0,75 / 0,80 / 0,78) fabriquent une dominante forte : préférer le gamma maître + une balance séparée.
- Qualifier un objet fin et sombre (pieds de chaise rouillés à v ≈ 0,15) ne prend que ses **bords** : liseré coloré. Remèdes : remonter la matière au tournage, clean black / blur de la clé, ou fenêtre + qualifieur.

## 3. Gestion des couleurs (RCM) [THÉORIQUE]
- Projet en **DaVinci YRGB Color Managed**, espace de traitement **DaVinci Wide Gamut / DaVinci Intermediate**, sortie Rec.709 Gamma 2.4 ; ou ACEScct pour un échange VFX ACES.
- Vérifier le tag d'export (Gamma 2.4 contre Rec.709-A) avec ffprobe : test n° 9 de `PLAN-TESTS-MCP.md`.

## 4. API de scripting Python [THÉORIQUE — doc officielle lue, rien exécuté : Resolve n'est pas installable dans la VM]
Source : README de scripting livré avec Resolve (Aide > Documentation > Developer) ; copies lues : version du 29/03/2022 (resolvedevdoc.readthedocs.io) et du 18/07/2023, Resolve 18.x. **Les ajouts des versions 19-20 ne sont pas vérifiés** : lire le README du Mac en phase 2.

Prérequis : Resolve lancé (ou `-nogui`) ; Python 3.6+ 64 bits. Le scripting **externe** serait réservé à la version Studio sur les versions récentes (à vérifier) ; la console interne (Workspace > Console) fonctionne dans la version gratuite.

```bash
# macOS
export RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
export RESOLVE_SCRIPT_LIB="/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
export PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"
```

Chaîne d'objets : `Resolve → ProjectManager → Project → MediaPool / Timeline → TimelineItem`.

Recette type « assembler une liste de plans et rendre » (squelette, noms de méthodes tirés du README) :
```python
import DaVinciResolveScript as dvr
resolve = dvr.scriptapp("Resolve")
pm = resolve.GetProjectManager()
proj = pm.CreateProject("TEST_SCRIPT_2026") or pm.LoadProject("TEST_SCRIPT_2026")   # jamais un projet client
mp = proj.GetMediaPool()
clips = mp.ImportMedia(["/chemin/plan01.mov", "/chemin/plan02.mov"])
tl = mp.CreateEmptyTimeline("assemblage")
mp.AppendToTimeline([{"mediaPoolItem": clips[0], "startFrame": 10, "endFrame": 24},
                     {"mediaPoolItem": clips[1], "startFrame": 0, "endFrame": 14}])
tl.AddMarker(0, "Blue", "hook", "impact image 1", 1, "")
for it in tl.GetItemListInTrack("video", 1):
    it.SetLUT(1, "/chemin/look.cube")            # node 1 ; voir montage-couleur-pipeline pour la LUT
resolve.OpenPage("deliver")
proj.SetCurrentRenderFormatAndCodec("mov", "ProRes422HQ")   # valeurs exactes : GetRenderFormats() / GetRenderCodecs("mov")
proj.SetRenderSettings({"SelectAllFrames": True, "TargetDir": "/chemin/rendus", "CustomName": "assemblage_v1"})
job = proj.AddRenderJob(); proj.StartRendering([job])
while proj.IsRenderingInProgress(): pass        # puis GetRenderJobStatus(job)
```
Autres méthodes utiles (README 2022-2023) :
- `Timeline.Export(chemin, resolve.EXPORT_EDL, resolve.EXPORT_CDL)` ; aussi `EXPORT_FCP_7_XML`, `EXPORT_FCPXML_1_10`, `EXPORT_AAF` (+ sous-type `EXPORT_AAF_NEW`), CSV.
- `MediaPool.ImportTimelineFromFile(chemin, {"timelineName": ..., "importSourceClips": True})` : conformation d'un XML/AAF Premiere.
- `Timeline.ApplyGradeFromDRX(chemin, gradeMode, [items])` (0 sans clés, 1 aligné sur le timecode source, 2 sur le début) : appliquer un grade de référence à toute une scène.
- `TimelineItem.SetCDL([{"NodeIndex": "1", "Slope": "...", "Offset": "...", "Power": "...", "Saturation": "..."}])`, `SetProperty("ZoomX", 1.2)`, `CopyGrades([...])`, `AddFusionComp()`.
- `Timeline.DetectSceneCuts()`, `Timeline.CreateSubtitlesFromAudio()`, `Project.ExportCurrentFrameAsStill(chemin)` (README 2023).
- Paramètres de `SetRenderSettings` : SelectAllFrames, MarkIn, MarkOut, TargetDir, CustomName, UniqueFilenameStyle, ExportVideo, ExportAudio, FormatWidth, FormatHeight, FrameRate, PixelAspectRatio, VideoQuality, AudioCodec, AudioBitDepth, AudioSampleRate, ColorSpaceTag, GammaTag, ExportAlpha, EncodingProfile, MultiPassEncode, AlphaMode, NetworkOptimization.
- Pièges notés dans le README : les appels de rendu par index sont dépréciés (utiliser les identifiants de job) ; `GetItemsInTrack` déprécié au profit de `GetItemListInTrack`.

**Méthode d'agent** (cf. `PLAN-TESTS-MCP.md`) : projet de test dédié, une action à la fois, `ExportCurrentFrameAsStill` après chaque étape d'étalonnage et regarder l'image, journaliser.

### Mise à jour 19 → 21.1 (recherche du 2026-10-10, `sources/resolve-scripting-api-19-20.md`) [THÉORIQUE]
[V] = lu dans le README/CHANGELOG officiel (copies datées) ; [A] = notes de version relayées par des tiers.
- **Corrige la recette ci-dessus** : `TimelineItem.SetLUT / GetLUT / GetNumNodes / GetNodeLabel` sont **dépréciés** [V, README mai 2025] → `g = item.GetNodeGraph(); g.SetLUT(1, lut)`. `Timeline.ApplyGradeFromDRX` n'est plus documenté depuis 2025 → `item.GetNodeGraph().ApplyGradeFromDRX(drx, 0)`.
- **Classe Graph** (19.0 [A], signatures [V]) : `Timeline.GetNodeGraph()`, `TimelineItem.GetNodeGraph(layerIdx)`, `ColorGroup.GetPreClipNodeGraph() / GetPostClipNodeGraph()` ; méthodes `GetNumNodes()`, `SetLUT(i, path)`, `GetLUT(i)`, `GetNodeLabel(i)`, `GetToolsInNode(i)`, `SetNodeEnabled(i, bool)`, `ApplyGradeFromDRX(path, mode)` (19.1), `ApplyArriCdlLut()`, `ResetAllGrades()`. Nodes indexés à partir de 1. **On ne crée pas de node par script** : l'arbre se prépare dans un DRX ou une PowerGrade, le script l'applique.
- **ColorGroup** (19.0 [A]) : `Project.GetColorGroupsList() / AddColorGroup(nom) / DeleteColorGroup(g)`, `TimelineItem.AssignToColorGroup(g) / GetColorGroup() / RemoveFromColorGroup()` ; utile pour poser un look commun (post-clip) par scène.
- `TimelineItem.SetCDL({...})` reste actif [V] ; `TimelineItem.ExportLUT(resolve.EXPORT_LUT_33PTCUBE, path)` (19.0 [A]) : exporter le grade d'un plan en LUT pour l'appliquer ailleurs (moniteur de plateau, Premiere).
- Rendu : `Project.RenderWithQuickExport(preset, {...})`, `GetQuickExportRenderPresets()` (19.1 [A]) ; sous-titres de rendu `ExportSubtitle` / `SubtitleFormat` (20.2 [V]).
- Audio : `Timeline.Get/SetVoiceIsolationState(track, {...})` (20.1 [V], nom incertain : `Enable…` dans le CHANGELOG), `Resolve.GetFairlightPresets()`, `Project.ApplyFairlightPresetToCurrentTimeline(nom)` (20.2.2 [V]), `Timeline.NormalizeAudioLevel()` (21 [V]).
- 21.0 / 21.1 [V] : `TranscribeAudio`, `GenerateSpeech`, `MediaPool.CreateMulticamClip()`, `TimelineItem.AddTransition`, `Get/SetFades`, `Get/SetSpeed`, `Timeline.GetSelectedClips()`, `resolve.IsStudio()` ; Python 2 abandonné.
- **Gratuit / Studio** : « Advanced scripting now requires DaVinci Resolve Studio » (page officielle 21.1 [V]) ; ce qui reste possible depuis la Console en version gratuite est contradictoire selon les sources [A]. **Avant tout projet scripté : `resolve.IsStudio()` et `GetVersionString()`.**

## 5. À vérifier en phase 2
- (en partie levé en session 5 : Graph et ColorGroup existent depuis la 19) README livré avec la version installée sur le Mac : différences gratuite/Studio pour le scripting externe.
- Les codes exacts de `SetCurrentRenderFormatAndCodec` (lister avec `GetRenderFormats()`, `GetRenderCodecs()`).
- `ApplyGradeFromDRX` sur une timeline de test ; `SetLUT` : index de node à partir de 1 ?
- L'arbre de nodes du § 2 sur un vrai rush log, comparé à une LUT unique (temps, rendu de la peau).
