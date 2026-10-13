Annexe de `SKILL.md` : le savoir et l'API de Resolve (arbre de nodes de référence, reproduire un look d'après une référence, gestion des couleurs, squelette Python, Fusion, Fairlight, saccade, évolutions 19 → 21.1) ; en grande partie [THÉORIQUE] (doc lue), sauf mention. Sections du SKILL.md déplacées à l'audit 2 (2026-10-13). Le SKILL.md fait foi ; les gestes éprouvés sont dans `recettes.md`.

# montage-resolve — savoir et API

Marqueurs : **[SOURCÉ]** lu dans une source datée · **[TESTÉ EN LABO]** fait technique mesuré (ffmpeg, scripts) · **[ÉPROUVÉ EN MAQUETTE]** principe tiré d'une maquette Blender/Pillow/numpy, hypothèse à confirmer sur de vraies images en phase 2 · **[THÉORIQUE]** doc ou pratique, jamais exécuté ; ici aussi [V] = lu dans le README officiel, [A] = relayé par des tiers.

## 2. Arbre de nodes de référence [THÉORIQUE — à éprouver en phase 3]
Ordre défendu (une idée par node, lisible par un autre étalonneur) :
1. **Entrée / normalisation** (si pas de RCM) : CST log caméra → espace de travail.
2. **Balance / exposition primaire** (Offset d'abord en log, puis Lift/Gamma/Gain).
3. **Contraste et courbe** (pivot réglé sur la valeur moyenne du sujet).
4. **Correction secondaire de peau** (qualifieur + fenêtre suivie) : c'est elle qui permet de garder un environnement vert sodium sans rendre le visage malade.
5. **Fenêtres de relief** (vignettage motivé, ramener l'œil sur le sujet).
6. **Look** (node parallèle ou LUT créative à opacité réglée par la clé du node).
7. **Grain / texture** en dernier (après le look, avant la sortie).
8. **Sortie** : CST ou ODT de l'espace de travail vers Rec.709 Gamma 2.4 (ou 2.2 pour le web, à décider : voir `montage-couleur`).
Pourquoi cet ordre : corriger avant de styliser ; un look appliqué sur une image non balancée réagit différemment d'un plan à l'autre.

**Leçons d'un étalonnage simulé en numpy** [ÉPROUVÉ EN MAQUETTE] (atelier 05, `atelier/05-trois-etalonnages/grade.py`, hors Resolve) :
- Une secondaire qui doit faire vivre une couleur ne se place **ni avant** un node qui écrase (elle est écrasée avec le reste) **ni après** (la couleur à qualifier n'existe plus) : on prend la **clé sur l'entrée** (node parallèle ou clé externe branchée sur la source) et on mélange en sortie. Mesuré : 0 % → 1,7 % de pixels chauds, 0 % hors de l'objet.
- Des gammas un peu différents par canal sur une image grise (0,75 / 0,80 / 0,78) fabriquent une dominante forte : préférer le gamma maître + une balance séparée.
- Qualifier un objet fin et sombre (pieds de chaise rouillés à v ≈ 0,15) ne prend que ses **bords** : liseré coloré. Remèdes : remonter la matière au tournage, clean black / blur de la clé, ou fenêtre + qualifieur.

## 2 bis. Reproduire un look d'après une image de référence : une méthode simple parmi d'autres
Vue chez David Foxprod (« recréer la colo de *Seven* », fiche `analyses/methodes/david-foxprod-look-seven.md`). Arbre et ordre [VU SUR IMAGES], rôle de chaque nœud [THÉORIQUE] (outils illisibles à l'écran).
1. **Retourner le plan comme la référence** (cadre, amorce, contre-jour, valeur du ciel) : la moitié du look se fait au tournage.
2. **CST IN** → en série **EXPO** → **WB** → **CON / SAT** (une idée par nœud, nommé).
3. En parallèle, depuis la source : **DENSITÉ** → correction localisée (fenêtres : jaunit le ciel sans toucher le visage) → **QUALIFIER** (visage). Mélangeur.
4. **MASK** puis **OVERLAY** (texture), encore dans l'espace de travail.
5. **CST OUT**, puis **deux looks en parallèle** (FUJI, K…), un seul actif : A / B immédiat.
6. Juger : activer les nœuds un à un, puis tout désactiver d'un coup (avant / après), la référence à côté.

Différence avec le § 2 : **le look vient après la sortie** (look écrit pour du Rec.709). Plus simple, mais à refaire pour une sortie HDR ou cinéma.

**Quand elle ne suffit pas** [mesuré sur la vidéo, sinon THÉORIQUE] :
- **La densité ne se rattrape pas** si le tournage l'a perdue : sur sa propre démonstration, la teinte est proche mais l'image finale reste bien plus claire (ciel 249 / 234 / 175 contre 184 / 167 / 106 pour *Seven*) ; un ciel brûlé ne redevient pas ocre.
- **Une séquence** : elle règle un plan ; il faut ensuite apparier les autres (stills en galerie, split screen, parade RVB et vectorscope : aucun de ces outils n'est montré).
- **Plans qui bougent** : fenêtres et qualifieur à suivre plan par plan.
- **Référence = copie web compressée** : on copie aussi ses défauts ; chercher la meilleure source, juger sur les scopes plutôt qu'à l'œil sur un écran non calibré.
- **Look qui vient du tirage ou de la lumière** (rétention d'argent, brume, décor) : aucun nœud primaire ne l'imite ; il faut un outil dédié (émulation de pellicule, Halation, grain) ou le tournage.

## 3. Gestion des couleurs (RCM) [THÉORIQUE]
- Projet en **DaVinci YRGB Color Managed**, espace de traitement **DaVinci Wide Gamut / DaVinci Intermediate**, sortie Rec.709 Gamma 2.4 ; ou ACEScct pour un échange VFX ACES.
- Vérifier le tag d'export (Gamma 2.4 contre Rec.709-A) avec ffprobe (ancien test n° 9, `archives/phase-3/PLAN-TESTS-MCP.md` ; exercice E5 de `PLAN-TESTS.md`).

## 4. API de scripting Python [THÉORIQUE pour le squelette ci-dessous ; les gestes vérifiés sont au § 4 ter]
Source : README de scripting livré avec Resolve (Aide > Documentation > Developer) ; copies lues de 2022-2023 (Resolve 18), puis README et CHANGELOG 19 à 21.1 (`sources/resolve-scripting-api-19-20.md`). Lire le README de la version installée en phase 3.

Prérequis : Resolve lancé (ou `-nogui`) ; Python 3 64 bits (Python 2 abandonné en 21). **« Advanced scripting now requires DaVinci Resolve Studio »** (page officielle 21.1 [V]) ; ce qui reste possible depuis la Console (Workspace > Console) en version gratuite est contradictoire selon les sources [A]. **Avant tout projet scripté : `resolve.IsStudio()` et `GetVersionString()`.** Depuis 21.1, Resolve Studio se pilote aussi par des assistants externes via un serveur MCP natif qui passe par cette API [SOURCÉ, 08/09/2026].

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
proj = pm.CreateProject("P3-exemple-agent") or pm.LoadProject("P3-exemple-agent")   # convention : P3-<projet>-agent ; jamais un projet client
mp = proj.GetMediaPool()
clips = mp.ImportMedia(["/chemin/plan01.mov", "/chemin/plan02.mov"])
tl = mp.CreateEmptyTimeline("assemblage")
mp.AppendToTimeline([{"mediaPoolItem": clips[0], "startFrame": 10, "endFrame": 24},
                     {"mediaPoolItem": clips[1], "startFrame": 0, "endFrame": 14}])
tl.AddMarker(0, "Blue", "hook", "impact image 1", 1, "")
for it in tl.GetItemListInTrack("video", 1):
    it.GetNodeGraph().SetLUT(1, "/chemin/look.cube")   # node 1 (index dès 1) ; TimelineItem.SetLUT est déprécié depuis 2025
resolve.OpenPage("deliver")
proj.SetCurrentRenderFormatAndCodec("mov", "ProRes422HQ")   # valeurs exactes : GetRenderFormats() / GetRenderCodecs("mov")
proj.SetRenderSettings({"SelectAllFrames": True, "TargetDir": "/chemin/rendus", "CustomName": "assemblage_v1"})
job = proj.AddRenderJob(); proj.StartRendering([job])
while proj.IsRenderingInProgress(): pass        # puis GetRenderJobStatus(job)
```
Autres méthodes (export `Timeline.Export` en EDL / XML FCP7 / FCPXML / AAF, `ImportTimelineFromFile`, `ApplyGradeFromDRX` via le graphe, `SetCDL`, `DetectSceneCuts`, `ExportCurrentFrameAsStill`, paramètres de `SetRenderSettings`, pièges du README) : [details.md](details.md).

**Méthode d'agent** (cf. `montage-pilotage-mcp`) : projet de test dédié, une action à la fois, `ExportCurrentFrameAsStill` après chaque étape d'étalonnage et regarder l'image, journaliser.

**Ce qui a changé de 19 à 21.1** (détail [details.md](details.md)) : classe **Graph** (`GetNodeGraph()` sur la timeline, le plan ou un ColorGroup ; LUT, DRX, activation des nodes) ; **on ne crée pas de node par script** : l'arbre se prépare dans un DRX ou une PowerGrade, le script l'applique. ColorGroups, `ExportLUT`, Quick Export, Voice Isolation et `NormalizeAudioLevel` scriptables, `TranscribeAudio`, `CreateMulticamClip`, `Get/SetSpeed`.

## 4 bis. Fusion, Fairlight, saccade [THÉORIQUE ; détail : [details.md](details.md)]
- **Fusion plutôt qu'After Effects** pour un effet plan par plan dans un montage qui vit dans Resolve (effacement, incrustation d'écran, keying, titre lié à un plan) : pas d'aller-retour, l'étalonnage passe après Fusion. **AE reste devant** pour le motion design et la typo animée (`montage-after-effects`). Piège : les Resolve FX posés dans Edit ne sont pas vus dans Fusion (faire un compound clip).
- **Fairlight** : normalisation au rendu dans Deliver > Audio (EBU R128, ATSC A/85, préréglages) ; compteur, bus et stems non scriptables. Mesurer soi-même la sortie (`montage-loudness-livraison`).
- **Saccade choisie** (garder quelques images d'un rush à strobe et les tenir 2-4 images) : **tenir, jamais fondre**. D'abord **Retime Process = Nearest** sur chaque clip (le réglage du clip l'emporte sur le projet), puis couper et **Freeze Frame (Shift-R)** image par image ; version la plus fidèle : Fusion **Time Stretcher** en Nearest, clés en Step. Les Freeze Frames ne passent **pas** en XML FCP7 vers Premiere : construire la saccade dans l'application qui finalise, ou la rendre en média avant l'échange.


Annexe de `SKILL.md` : méthodes d'API, évolutions 19 → 21.1, Fusion, Fairlight et saccade dans le détail (le SKILL.md fait foi ; seules les précisions absentes du SKILL.md sont ici). Tout est **[THÉORIQUE]** (doc lue, rien exécuté : Resolve n'est pas installable dans la VM), sauf mention [SOURCÉ] ; [V] = lu dans le README/CHANGELOG officiel (copies datées), [A] = notes de version relayées par des tiers.

### API : méthodes utiles (README 2022-2023, corrigées par les versions 19-21)
- `Timeline.Export(chemin, resolve.EXPORT_EDL, resolve.EXPORT_CDL)` ; aussi `EXPORT_FCP_7_XML`, `EXPORT_FCPXML_1_10`, `EXPORT_AAF` (+ sous-type `EXPORT_AAF_NEW`), CSV.
- `MediaPool.ImportTimelineFromFile(chemin, {"timelineName": ..., "importSourceClips": True})` : conformation d'un XML/AAF Premiere.
- Appliquer un grade de référence à toute une scène : `item.GetNodeGraph().ApplyGradeFromDRX(drx, mode)` (mode 0 sans clés, 1 aligné sur le timecode source, 2 sur le début). L'ancienne forme directe `Timeline.ApplyGradeFromDRX(chemin, gradeMode, [items])` (README 2022-2023) n'est plus documentée depuis 2025 : ne pas l'utiliser.
- `TimelineItem.SetCDL([{"NodeIndex": "1", "Slope": "...", "Offset": "...", "Power": "...", "Saturation": "..."}])` (reste actif [V]), `SetProperty("ZoomX", 1.2)`, `CopyGrades([...])`, `AddFusionComp()`.
- `Timeline.DetectSceneCuts()`, `Timeline.CreateSubtitlesFromAudio()`, `Project.ExportCurrentFrameAsStill(chemin)` (README 2023).
- Paramètres de `SetRenderSettings` : SelectAllFrames, MarkIn, MarkOut, TargetDir, CustomName, UniqueFilenameStyle, ExportVideo, ExportAudio, FormatWidth, FormatHeight, FrameRate, PixelAspectRatio, VideoQuality, AudioCodec, AudioBitDepth, AudioSampleRate, ColorSpaceTag, GammaTag, ExportAlpha, EncodingProfile, MultiPassEncode, AlphaMode, NetworkOptimization.
- Pièges notés dans le README : les appels de rendu par index sont dépréciés (utiliser les identifiants de job) ; `GetItemsInTrack` déprécié au profit de `GetItemListInTrack`.

### Mise à jour 19 → 21.1 (recherche du 2026-10-10, `sources/resolve-scripting-api-19-20.md`)
- **Dépréciés** [V, README mai 2025] : `TimelineItem.SetLUT`, `GetLUT`, `GetNumNodes`, `GetNodeLabel` appelés directement sur le plan. Tout passe par le graphe : `g = item.GetNodeGraph(); g.SetLUT(1, lut)`.
- **Classe Graph** (19.0 [A], signatures [V]) : `Timeline.GetNodeGraph()`, `TimelineItem.GetNodeGraph(layerIdx)`, `ColorGroup.GetPreClipNodeGraph() / GetPostClipNodeGraph()` ; méthodes `GetNumNodes()`, `SetLUT(i, path)`, `GetLUT(i)`, `GetNodeLabel(i)`, `GetToolsInNode(i)`, `SetNodeEnabled(i, bool)`, `ApplyGradeFromDRX(path, mode)` (19.1), `ApplyArriCdlLut()`, `ResetAllGrades()`. Nodes indexés à partir de 1.
- **ColorGroup** (19.0 [A]) : `Project.GetColorGroupsList() / AddColorGroup(nom) / DeleteColorGroup(g)`, `TimelineItem.AssignToColorGroup(g) / GetColorGroup() / RemoveFromColorGroup()` ; utile pour poser un look commun (post-clip) par scène.
- `TimelineItem.ExportLUT(resolve.EXPORT_LUT_33PTCUBE, path)` (19.0 [A]) : exporter le grade d'un plan en LUT pour l'appliquer ailleurs (moniteur de plateau, Premiere).
- Rendu : `Project.RenderWithQuickExport(preset, {...})`, `GetQuickExportRenderPresets()` (19.1 [A]) ; sous-titres de rendu `ExportSubtitle` / `SubtitleFormat` (20.2 [V]).
- Audio : `Timeline.Get/SetVoiceIsolationState(track, {...})` (20.1 [V], nom incertain : `Enable…` dans le CHANGELOG), `Resolve.GetFairlightPresets()`, `Project.ApplyFairlightPresetToCurrentTimeline(nom)` (20.2.2 [V]), `Timeline.NormalizeAudioLevel()` (21 [V]).
- 21.0 / 21.1 [V] : `TranscribeAudio`, `GenerateSpeech`, `MediaPool.CreateMulticamClip()`, `TimelineItem.AddTransition`, `Get/SetFades`, `Get/SetSpeed`, `Timeline.GetSelectedClips()`, `resolve.IsStudio()`.
- 21.1 : le serveur MCP natif (Studio) est annoncé pour des assistants externes nommés (Claude, ChatGPT Codex) [SOURCÉ, communiqué Blackmagic du 08/09/2026]. « Magic Mask 2.0 » et « IntelliTrack » en 21.1 : **non confirmés, à écarter** (une seule source, sportsvideo.org ; absents du communiqué officiel). Magic Mask lui-même existe depuis les versions antérieures.

### Fusion et Fairlight (doc officielle lue par un sous-agent, rien exécuté ; sources : `sources/resolve-fusion-fairlight-2026-10.md`)
- Ordre des pages : Edit → Fusion → Color. AE reste aussi devant pour les plugins et les projets à beaucoup d'éléments graphiques (source secondaire ancienne : ProVideo Coalition 2018).
- Nodes : MediaIn = le clip de la timeline, MediaOut = ce qui retourne au montage (déconnecté : le plan devient noir) ; Merge : entrée **jaune = arrière-plan**, **verte = premier plan**. Plusieurs plans : Fusion clip (ajoute Merge et Background).
- Resolve FX / OFX posés dans Edit : seuls le recadrage et la position sont vus dans Fusion.
- **Titres maison** : Macro > Create Macro, exposer les réglages utiles, enregistrer dans `Fusion/Templates/Edit/Titles`, relancer : le titre apparaît dans la page Edit (l'équivalent des MOGRT de Premiere). Pourquoi : un carton reproductible et modifiable par le monteur, sans retour au motion designer.
- Script : l'API Resolve atteint la comp d'un plan (`GetFusionCompByIndex`, `AddFusionComp`, `ImportFusionComp`, `ExportFusionComp`, `CreateFusionClip`, `InsertFusionTitleIntoTimeline`, README 21.0.4) ; dans la comp, `AddTool`, `ConnectInput`, `SetInput` (guide de scripting Fusion 8, **2016**, rien de plus récent trouvé : signatures à vérifier).
- Fairlight, précisions : la normalisation de Deliver suit BS.1770-4 et propose des préréglages de plateformes ; AI Dialogue Leveler (effet de piste) ; Voice Isolation par piste scriptable (20.1) ; `NormalizeAudioLevel` avec cible LKFS (21.1). Faders non scriptables non plus : tout ce qui n'est pas scriptable passe par un préréglage de rendu.

### Saccade choisie et retime (manuels de référence 19.1 / 20 / 21 lus ; pages et tests : `sources/resolve-saccade-choisie-2026-10.md` ; version Premiere/AE : `sources/premiere-ae-saccade-choisie-2026-10.md`)
- **Pourquoi tenir** : une image tenue se lit comme une pensée (le regard s'arrête avec le personnage) ; un mélange de deux images se lit comme une panne (fondu sale, morphing). La saccade choisie sert un moment intérieur, un sujet net dans une foule qui traîne ; pour une texture régulière, on prend un effet (Stop Motion, ci-dessous), pas une partition.
- **Où se règle le verrou** : Inspector > Retime and Scaling > Retime Process ; le défaut du clip est « Project Settings » (Project Settings > Master Settings > Frame Interpolation). Le même verrou vaut pour les rushes 50/60p posés sur une timeline à 24/25 : Frame Blend et Optical Flow y fondent ou inventent des images. Motion Estimation (Standard / Enhanced / Speed Warp) n'agit qu'en Optical Flow.
- **Freeze Frame image par image** : couper le clip à chaque frontière de tenue, poser la tête de lecture sur l'image choisie, Shift-R (le segment entier fige cette image), puis trimer à N images. La timeline devient la partition, comme avec le Frame Hold de Premiere.
- **Retime Controls (Cmd-R) > Clip Speed > Freeze Frame** : pose deux speed points autour de la tenue ; le manuel dit les changements de vitesse « automatically eased » : bien pour une tenue longue, suspect pour 2 à 4 images.
- **Retime Frame** (graphe image source / image timeline ; segment plat = tenue) : clic droit > Retime Curve en 19/20, onglet Keyframes > Keyframe Curves en 21. Le manuel 21 documente des clés **Step In / Step Out** sans dire qu'elles s'appliquent à Retime Frame (équivalent des clés Hold d'AE, **à tester**).
- **Fusion Time Stretcher** : une clé de **Source Time** par image choisie, clés en Step avec I / O. **Time Speed** ne convient pas (sa Speed n'est pas animable).
- **Texture régulière** : Resolve FX Temporal > **Stop Motion** (Frame Repeat 1-10, Sampling Variation ; trouvé seulement dans le manuel 21).
- **Traînée (obturateur lent)** : Fusion **Trails** (gratuit ; Gain = longueur ; Reset entre deux prévisualisations) ; Resolve FX **Motion Trails** (Studio : Trail Length, Dropoff) ; Motion Blur **From Previous Frame** (Studio). La traînée se pose **après** la saccade (après le Time Stretcher dans Fusion, ou sur un compound clip). **Smear** et Frame Blend fondent les tenues : à proscrire.
- **Échange avec Premiere**, précisions : les Freeze Frames passent seulement en AAF Media Composer et reviennent en « N/A » vers Premiere ; les vitesses variables, elles, passent. Rendre en média = rendu « Single clip ».
