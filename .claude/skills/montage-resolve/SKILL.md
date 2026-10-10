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

## 5. À vérifier en phase 2
- README livré avec la version installée sur le Mac : objets ajoutés depuis la 19 (graphe de nodes par script ? groupes de couleur ?), différences gratuite/Studio pour le scripting externe.
- Les codes exacts de `SetCurrentRenderFormatAndCodec` (lister avec `GetRenderFormats()`, `GetRenderCodecs()`).
- `ApplyGradeFromDRX` sur une timeline de test ; `SetLUT` : index de node à partir de 1 ?
- L'arbre de nodes du § 2 sur un vrai rush log, comparé à une LUT unique (temps, rendu de la peau).
