---
name: montage-resolve
description: DaVinci Resolve — étalonnage par nodes (série, parallèle, layer mixer), gestion des couleurs (RCM, DaVinci Wide Gamut, ACEScct), Deliver et rendus en lot, Fusion, Fairlight, saccade et retime, scripting Python (GetNodeGraph, AppendToTimeline, AddRenderJob, export EDL/XML/AAF). Mots d'un étalonneur ou d'un monteur : « on passe en étalo », « arbre de nodes », « monter un look », « recréer la colo de tel film », « reproduire le look de cette référence », « qualifier la peau », « power window », « rendu en lot », « automatiser l'export », « script Resolve », « je fais le plan dans Fusion ? ».
---

# DaVinci Resolve

Marqueurs : **[SOURCÉ]** lu dans une source datée · **[TESTÉ EN LABO]** fait technique mesuré (ffmpeg, scripts) · **[ÉPROUVÉ EN MAQUETTE]** principe tiré d'une maquette Blender/Pillow/numpy, hypothèse à confirmer sur de vraies images en phase 2 · **[THÉORIQUE]** doc ou pratique, jamais exécuté ; ici aussi [V] = lu dans le README officiel, [A] = relayé par des tiers.

Rôle : l'étape où l'image prend son **intention de couleur** (`montage-couleur-et-intention`) et où la chaîne technique est tenue propre (`montage-couleur-pipeline`). **Fait foi sur** : l'étalonnage dans Resolve, son API de scripting, Fusion, Fairlight et le retime dans Resolve. Pour les formats d'échange et la conformation (ce qui passe ou se perd en XML/EDL/AAF) : `montage-workflows` ; pour les cibles de loudness : `montage-loudness-livraison` ; Magic Mask et autres outils IA comparés : `montage-ia-generative`. Détail de l'API, Fusion, Fairlight et saccade : [details.md](details.md).

## 1. Quand et pourquoi Resolve
- **Étalonnage** : c'est l'outil de référence (nodes, qualifications, tracking de fenêtres, gestion des couleurs de bout en bout). Premiere Lumetri suffit pour un corporate homogène ; dès qu'il y a un **look** à construire, une peau à protéger dans une dominante « fausse » (goût de l'utilisateur : Joker), des fenêtres à suivre, c'est Resolve.
- **Conformation / round-trip** : monter dans Premiere, exporter XML/AAF, étalonner dans Resolve, rendre en master 10 bits (cf. `labo/encodage/` : le 10 bits évite les bandes dans les noirs).
- **Automatisation** : rendus en lot, import et assemblage d'une liste de plans, application d'une LUT ou d'un grade à toute une timeline. C'est la porte d'entrée d'un agent en phase 3 si aucun MCP Resolve n'est branché.

## 2. Arbre de nodes de référence [THÉORIQUE — à éprouver en phase 3]
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
- Vérifier le tag d'export (Gamma 2.4 contre Rec.709-A) avec ffprobe : test n° 9 de `PLAN-TESTS-MCP.md`.

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

**Méthode d'agent** (cf. `PLAN-TESTS-MCP.md`) : projet de test dédié, une action à la fois, `ExportCurrentFrameAsStill` après chaque étape d'étalonnage et regarder l'image, journaliser.

**Ce qui a changé de 19 à 21.1** (détail [details.md](details.md)) : classe **Graph** (`GetNodeGraph()` sur la timeline, le plan ou un ColorGroup ; LUT, DRX, activation des nodes) ; **on ne crée pas de node par script** : l'arbre se prépare dans un DRX ou une PowerGrade, le script l'applique. ColorGroups, `ExportLUT`, Quick Export, Voice Isolation et `NormalizeAudioLevel` scriptables, `TranscribeAudio`, `CreateMulticamClip`, `Get/SetSpeed`.

## 4 ter. Piloter Resolve par son MCP natif [TESTÉ EN CONDITIONS RÉELLES] (2026-10-11, Resolve Studio 21.1.1)
Détail appel par appel : `labo/mcp/journal-2026-10-11.md` ; capacités du serveur : `labo/mcp/resolve-mcp.md`.
- **Tout passe par `run_script`** (Python sandboxé, `resolve` et `project` injectés, `result = …`). Pas de fichiers depuis Python, mais Resolve écrit où on lui dit.
- **Œil** : `tl.SetCurrentTimecode(tc)` puis `project.ExportCurrentFrameAsStill(png)`, **depuis la page Edit** (sur la page Color, l'export prend l'image d'avant). Se fier à l'image, pas à `GetCurrentVideoItem()` (renvoie parfois le plan précédent).
- **Poser** : `AppendToTimeline` avec `startFrame`/`endFrame` en images **de la source** (un rush 50p compte en images 50p), `endFrame` **exclusif**, `recordFrame` absolu (timeline à 90000 = 01:00:00:00). Monter = reconstruire : pas de lame ni de trim, on supprime (`DeleteClips`) et on repose.
- **Ne jamais utiliser `InsertFusionTitleIntoTimeline` / `Insert…Generator…`** sur une timeline montée : montage par insertion sur la piste active, qui coupe et pousse tout, son compris. Texte, flash, aplat : **plan porteur** posé par `AppendToTimeline` sur une piste haute, puis `AddFusionComp()` et `TextPlus` / `Background` branché sur `MediaOut1` ; zoomer le porteur s'il n'a pas le format de la timeline.
- **Vertical depuis UHD** : `tl.SetSetting("useCustomSettings","1")` puis 1080 / 1920 / 25 ; remplir = `ZoomX = ZoomY = 3,1605` ; `Pan` en pixels de timeline (+ = vers la droite, ±1166 px avant le bord).
- **Vitesse** : `SetSpeed({"Percentage": 50, "RippleTimeline": False})` garde la durée et prend moitié moins de source ; un rush 50p à 50 % dans une timeline 25p donne un vrai ralenti image par image. Pas de courbe de vitesse dans l'API : **rampe en paliers** (segments à 100 / 85 / 70 / 60 / 50 %) ou rampe lisse faite à la main.
- **Animer (zoom, punch-in, texte qui entre, rotation)** [TESTÉ EN CONDITIONS RÉELLES] (2026-10-11, session 1) : dans la composition du plan, `tool.AddModifier("Size", "BezierSpline")`, `sp = tool.Size.GetConnectedOutput().GetTool()`, `sp.SetKeyFrames({0: {1: 1.0, "RH": {1: 3, 2: 0}}, 10: {1: 1.3, "LH": {1: -3, 2: 0}}}, True)` : poignées **relatives** à la clé, plates = easing ; une clé de plus au-dessus de la valeur finale = dépassement. Ou une expression sans clé : `tool.Size.SetExpression("1 + 0.5*(time-comp.RenderStart)/(comp.RenderEnd-comp.RenderStart)")`. Le temps de la composition est en **images de la source** (rush 50p : image de timeline n = temps 2n). `GetInput(…, t)` relit mal les clés : **contrôler sur le rendu**, pas sur l'export d'image (souvent noir juste après un changement Fusion). `spline[t] = v` ne marche pas.
- **Transitions intégrées** [TESTÉ EN CONDITIONS RÉELLES] (2026-10-11) : `AddTransition({"type", "category", "position":"end", "alignment":"center", "duration"})` : `Push`, `Slide`, `Blur Dissolve`, `Smooth Cut` (simple) ; `Brightness Flash`, `Camera Shake`, `Zoom In`, `Glitch` (fusion).
- **Son** : `SetProperties({"AudioVolume": dB})`, `SetFades({"FadeIn": n, "FadeOut": n})` (exacts au rendu) ; synchro double système `MediaPool.AutoSyncAudio([vidéo, wav], {"syncMode": resolve.AUDIO_SYNC_WAVEFORM})`, décalage lu dans `GetAudioMapping()`.
- **Couleur** : `SetCDL` (nœud 1) ; LUT seulement depuis le dossier de LUT de Resolve, en chemin relatif (mes LUT : sous-dossier `P3/`, accord de Diego du 2026-10-11) ; une LUT de tirage (Kodak 2383, Fuji 3513) attend du **Cineon log** : sur du Rec.709 elle éclaircit et bleuit. Pas de création de nœud ni de Magic Mask par script (`CreateMagicMask` ne fait que suivre des traits déjà tracés à la main).
- **Rendu** : `SetCurrentRenderFormatAndCodec("mp4","H264")` (codes : `GetRenderFormats()`, `GetRenderCodecs("mp4")`), `SetRenderSettings({"SelectAllFrames", "TargetDir", "CustomName", "AudioCodec": "aac", "AudioSampleRate": 48000})`, `AddRenderJob`, `StartRendering`, attendre dans le même script ; puis ffprobe et `qc_livraison.sh`.

## 4 bis. Fusion, Fairlight, saccade [THÉORIQUE ; détail : [details.md](details.md)]
- **Fusion plutôt qu'After Effects** pour un effet plan par plan dans un montage qui vit dans Resolve (effacement, incrustation d'écran, keying, titre lié à un plan) : pas d'aller-retour, l'étalonnage passe après Fusion. **AE reste devant** pour le motion design et la typo animée (`montage-after-effects`). Piège : les Resolve FX posés dans Edit ne sont pas vus dans Fusion (faire un compound clip).
- **Fairlight** : normalisation au rendu dans Deliver > Audio (EBU R128, ATSC A/85, préréglages) ; compteur, bus et stems non scriptables. Mesurer soi-même la sortie (`montage-loudness-livraison`).
- **Saccade choisie** (garder quelques images d'un rush à strobe et les tenir 2-4 images) : **tenir, jamais fondre**. D'abord **Retime Process = Nearest** sur chaque clip (le réglage du clip l'emporte sur le projet), puis couper et **Freeze Frame (Shift-R)** image par image ; version la plus fidèle : Fusion **Time Stretcher** en Nearest, clés en Step. Les Freeze Frames ne passent **pas** en XML FCP7 vers Premiere : construire la saccade dans l'application qui finalise, ou la rendre en média avant l'échange.

## 4 quater. Recettes du premier projet monté (Sony, 2026-10-11) [TESTÉ EN CONDITIONS RÉELLES]
- **Rushes verticaux** (métadonnée `rotation=90`, Sony ZV-E1) : Resolve applique la rotation à l'import (2160x3840) ; dans une timeline 1080x1920, plein cadre à zoom 1 et 2× de marge pour les punch-ins.
- **S-Log3 sans gestion des couleurs** : `GetNodeGraph().SetLUT(1, "Sony/SLog3SGamut3.CineToLC-709TypeA.cube")` sur chaque plan ; puis `SetCDL` sur le nœud 1 pour corriger : **le CDL et la LUT du même nœud se combinent** (pente 1,25 + décalage 0,02 : luminance moyenne 28 → 45 sur un plan sombre).
- **Fichier son** dans `AppendToTimeline` : `startFrame`/`endFrame` en images de la **timeline** (25 i/s), quel que soit l'échantillonnage ; le son d'un **rush 50p** se compte en images 50p.
- **Fondu enchaîné son** : `AddTransition({"type":"Cross Fade +3 dB","category":"audio",…})` ; il disparaît si l'on supprime l'un des deux plans (le reposer).
- **Composition d'un plan** : temps de 0 à 2×(durée−1) pour un rush 50p à 100 % (`COMPN_RenderStart` = 0). Un `TextPlus` ajouté s'appelle `Text1` : le retrouver par `GetAttrs()["TOOLS_RegID"]`.
- **Secousse amortie sans clés** : `Transform.Size = 1.06` et `Center.SetExpression("Point(0.5+0.025*sin(time*2.4)*max(0,1-time/10), 0.5+0.02*cos(time*3.1)*max(0,1-time/10))")`.
- **Musique masterisée fort** (MP3 de banque) : posée à 0 dB elle sature le mix ; partir de -8 dB, mesurer le rendu (`qc_livraison.sh`), ajuster par pas de 1 dB.
- Un rendu H.264 de 60 s en 1080x1920 depuis des rushes UHD HEVC 4:2:2 10 bits avec 68 compositions Fusion : **14 à 18 s**.

## 4 quinquies. Recettes de la V3 Sony (2026-10-11) [TESTÉ EN CONDITIONS RÉELLES]
- **Poignées de courbe Fusion : RELATIVES à la clé.** `SetKeyFrames({t0: {1: v0, "RH": {1: Δt, 2: Δv}}, t1: {1: v1, "LH": {1: -Δt, 2: Δv}}}, True)`. En absolu, un impact 1,25 → 1 montait à 1,9× et une poussée 1 → 1,1 à 1,86×. **Toujours relire les valeurs** (`tool.Size[t]` sur quelques images) après avoir posé des clés. Impact juste : `{s0: {1: A, "RH": {1: 0.6r, 2: -(A-1)*0.75}}, s0+5r: {1: 1, "LH": {1: -2.5r, 2: 0}}}` (r = images de composition par image de timeline : 2 pour un rush 50p à 100 %).
- **Flou de bougé** : `Transform.MotionBlur = 1`, `Quality = 8`, `ShutterAngle = 180`. Ne pas l'activer en aval d'un outil IA (carte de profondeur) : il le recalcule à des instants intermédiaires (halos dédoublés).
- **Détourage sans Magic Mask** (idée de Claude nu, corrigée) : `ofx.com.blackmagicdesign.resolvefx.DepthMap` (`isPreviewDepth = 1`) → `BitmapMask` (luminance, `Low` 0,34, `High` 0,40, `SoftEdge` 0,0012) pour le sujet ; `ErodeDilate` (`XAmount` 0,007) → second `BitmapMask` pour le contour ; fond = `BrightnessContrast` (gain 0) + `ColorCorrector` (sortie basse = couleur), ou le plan en noir et blanc assombri ; deux `Merge` avec `EffectMask`. Juger d'abord la carte de profondeur rendue : le sujet doit être le plus proche (un néon au premier plan ruine le masque, C6581). Faible sur des cheveux éclairés (halo).
- **Arrêt sur image + Fusion** : `SetSpeed(0)` fige la timeline, **pas la composition** (elle lit toujours 12 images différentes). Mettre un `TimeSpeed` (`Speed = 0`) juste après `MediaIn` et y rebrancher tous les outils.
- **Fusion passe AVANT le nœud de couleur** : une couleur posée dans Fusion (fond, contour, texte sur un plan qui porte la LUT) traverse la LUT de look. Calculer la valeur d'entrée en inversant la LUT (`labo/couleur/look_sony.py`, recherche sur grille) : orange voulu (0,84 ; 0,41 ; 0,09) = S-Log3 (0,58 ; 0,42 ; 0,0) ; blanc = 0,80. Un texte sur une piste à part, sans LUT, n'a pas ce problème.
- **Image fixe dans `AppendToTimeline`** : un PNG prend sa durée par défaut (125 images) quoi qu'on demande dans `endFrame`. Pour un flash d'une image : une courte vidéo (ProRes blanc de 2 s) coupée à `endFrame = 1`, `Opacity`, `CompositeMode = resolve.COMPOSITE_ADD`.
- **Grain** sans alourdir : un ProRes de 4 s de bruit gris (ffmpeg `noise=alls=22:allf=t`) sur une piste haute, `COMPOSITE_OVERLAY`, 35 %, désactivable.
- **Look en un seul nœud** : LUT `.cube` qui fait conversion S-Log3 + tirage 2383 + pied de courbe (`labo/couleur/look_sony.py`) ; exposition par plan avec le décalage CDL du même nœud (le CDL agit avant la LUT : 1 diaph = 0,077 en S-Log3). Après `RefreshLUTList()`, `SetLUT(1, "P3/…cube")`.
- **Stabilisation** : `TimelineItem.Stabilize()` marche par l'API mais recadre énormément (packshot illisible) : à éviter sans réglage. Ce qui marche : mesurer la trajectoire sur le rush (`labo/outils/tremblement.py RUSH t0 t1 --json reste.json`, 50p), puis un `Transform` « Stab » (taille 1,04) dont le `Center` est clé à chaque image de composition à `(0,5 − rx/1080 ; 0,5 + ry/1920)`. Résultat mesuré : 5,5 → 2,7 px, 3,8 → 1,8 px, 1,7 → 0,7 px.
- **Gyroflow** (1.6.3) en ligne de commande [TESTÉ EN LABO 2026-10-11] : la version **Mac App Store** (`/Applications/Gyroflow.app`, contient `_MASReceipt`) est en « bac à sable » : sur un disque externe, « Unable to read the video file » puis blocage, même après avoir ouvert le fichier dans l'app. **Utiliser la version GitHub** (gratuite, notarisée, sans bac à sable), installée dans `~/Applications/Gyroflow-GitHub.app` : `~/Applications/Gyroflow-GitHub.app/Contents/MacOS/gyroflow`. Test sans rendu : `--export-metadata "3:<chemin>.json"` (une entrée par image : `org_quat`, `stab_quat`, `fov_scale`, `minimal_fov_scale`…) ; lit le SSD en 0,5 s. Les deux versions partagent `~/Library/Application Support/Gyroflow/settings.json`. [TESTÉ EN CONDITIONS RÉELLES 2026-10-11, projet Sony]
  - **Gyroflow d'abord, quand le rush porte des données gyroscopiques et tremble au-delà du seuil** (Diego : plus précis que toute stabilisation interne), que l'intention soit un fixe ou un mouvement ; puis **mesure du rendu** : le brut ou le rail l'emportent s'ils mesurent mieux (voir « Mesurer le résultat, pas la preuve » ci-dessous). Un rush sans données gyro, ou un plan sur pied, n'en a pas besoin ; **10 essais au plus, puis on remplace le plan** (`montage-regard`, point 3). Rendu : `gyroflow RUSH.MP4 -t _stabilized -p "{ 'codec': 'ProRes', 'codec_options': 'HQ', 'use_gpu': true, 'audio': false }" --preset "{ 'version': 2, 'stabilization': { 'adaptive_zoom_window': -1.0, 'max_zoom': 115.0 } }"` : lissage par défaut (modéré), **zoom fixe** (`adaptive_zoom_window` -1 ; le zoom dynamique fait « respirer » le cadre) plafonné à 115 %, ProRes 422 HQ 10 bits, sortie à côté de l'original (accord de Diego). Plage seule : `'trim_ranges_ms': [[24000.0, 30000.0]]` dans le preset. Objectif et rotation du ZV-E1 lus seuls (profil Sony, 70 mm, rotation 90 : sortie 2160x3840). 2,4 s rendues en 10-15 s. `--export-project 1` écrit un `.gyroflow` À CÔTÉ DU RUSH : le déplacer aussitôt dans `_travail/`.
  - **Toujours la synchronisation automatique, sur une plage courte** : `'synchronization': { 'do_autosync': true, 'search_size': 3, 'max_sync_points': 4 }` dans le preset. Sans elle, le packshot C6723 passait de 1,96 px (original) à **9,66 px** (gyroscope décalé de l'image) ; avec elle sur 4 s autour du moment utilisé : 1,91 px. Sur 20 s rendues d'un coup, la synchro retombe mal (7,9 px) : rendre une plage courte par moment utilisé (`trim_ranges_ms`). Toujours mesurer avant / après sur la plage utilisée : si Gyroflow n'améliore pas, le rush était déjà stable. Sortie hors du dossier source pour un essai : `'output_folder': 'file:///…/'` dans `-p`.
  - **Une sortie Gyroflow rendue sur une plage garde le timecode de DÉBUT du rush** (pas celui de la plage) : pour retrouver le vrai moment, ajouter le début de la plage (table `DECALAGES` de `labo/outils/doublons_timeline.py`).
  - Rushes avec son : `AppendToTimeline` échoue (`None`) si l'audio entre en conflit avec la piste A1 : ajouter `"mediaType": 1` (vidéo seule).
  - Lissage plus fort (`smoothness` 3) : presque aucun gain sur le tremblement, mais le geste ralentit (vitesse gardée 0,85) : à éviter.
  - **Gyroflow ne voit que la rotation** : le va-et-vient de la main (translation, avant / arrière) reste. Ensuite : `labo/outils/stabiliser.py STAB.mov DEBUT FIN --mode fixe|rail --json cles.json` (intention du cadreur, voir `montage-regard` point 3), contrôle hors Resolve avec `labo/outils/appliquer_stab.py`, puis clés dans un `Transform` de la composition du plan (image 0 = point d'entrée, une image de composition = une image source à 50 i/s). Mesure sur le packshot C6725 (même plage) : original 6,8 px (fenêtre 0,4 s) / 13,9 px d'écart au rail (1 s) ; Gyroflow seul 4,1 / 8,8 ; **Gyroflow + rail 0,55 / 3,1**, vitesse du geste gardée à 97 %, zoom ajouté ×1,03. Bande d'images : glissement régulier, aucun contour dédoublé.
  - **Mesurer le résultat, pas la preuve** [TESTÉ EN CONDITIONS RÉELLES 2026-10-11, V5 Sony] : une synchronisation gyroscope / image prouvée (résiduel 4 ms) n'empêche pas un rendu Gyroflow de trembler **plus** que le rush (C6507 à 39 s : 8,6 px contre 1,15 brut) ; et Gyroflow seul laisse la translation (packshots : 2,5-4,2 px, puis 0,7-0,8 avec le rail). Toujours mesurer le plan stabilisé lui-même sur le rendu, garder le brut s'il est meilleur. Sur le tapis en carbone (motif répétitif), `tremblement.py` se trompe : recouper par le centre des objets clairs, **à exposition égale seulement** (le centre d'une zone brûlée paraît stable).
  - **Clés d'un rail dans la composition d'un plan 50p** : l'image 0 de la composition n'est pas toujours le point d'entrée : `comp.GetAttrs()["COMPN_GlobalStart"]` donne l'image source de la composition 0 (−44 pour un point d'entrée à 43) ; décaler les clés de `GetSourceStartFrame() + COMPN_GlobalStart` (une image de retard suffit à doubler le tremblement). Clés : `tr.AddModifier("Size", "BezierSpline")`, `AddModifier("Center", "XYPath")`, puis `tr.SetInput("Center", {1: x, 2: y}, t)`. `DeleteFusionCompByName` échoue sur la composition active : `LoadFusionCompByName` l'autre d'abord.
- **Ne jamais lire les entrées d'un effet IA OpenFX par script** (ex. `AIDepthMap1`, RegID `ofx.com.blackmagicdesign.resolvefx.DepthMap` : boucle `GetInput` sur `GetInputList()`) [TESTÉ EN CONDITIONS RÉELLES 2026-10-11] : Resolve s'est figé (roue qui tourne, 10 % de processeur, plus aucun appel ne répond). Seule issue : forcer à quitter (avec l'accord de l'utilisateur), relancer, `LoadProject`. Enregistrer le projet (`SaveProject`) avant toute exploration risquée.
- **Ne jamais `comp.Lock()` pendant la pose des clés** [TESTÉ EN CONDITIONS RÉELLES 2026-10-11] : les valeurs relues sont justes (`GetInput("Size", t)`), mais le rendu lit l'animation comme figée (première valeur, puis la dernière d'un coup) ; les valeurs fixes, elles, passent. Sans `Lock`, `SetInput(v, t)` comme `SetKeyFrames` sont rendus. Toujours contrôler une animation par un **rendu de plage**, pas par la relecture des valeurs.
- **Zoom infini réel** (V4 Sony, E → KORE) [TESTÉ EN CONDITIONS RÉELLES 2026-10-11] : (1) vérifier la matière : même objet aux deux échelles ; alignement mesuré par SIFT (`cv2.SIFT_create`, `estimateAffinePartial2D` RANSAC) entre le gros plan et le plan large, contrôle par incrustation (aucun dédoublement) ; (2) plan large sur V1, gros plan sur V2, les deux animés par la **même** échelle exponentielle (`z = Z0^(1-e(u))`, `e` = smoothstep : vitesse perçue régulière, départ et arrivée freinés) autour du point d'accroche qui glisse de sa place à l'écran vers sa place dans le plan large ; (3) bord du gros plan fondu (`RectangleMask` SoftEdge 0,16 + `MatteControl` `Garbage.Matte` inversé) et **fondu d'alpha** pendant le recul (`BrightnessContrast` `Alpha`=1, `Gain` 1 → 0) : aligné, le fondu ne se voit pas ; (4) **même luminosité** des deux plans (décalage CDL mesuré sur le béton) ; (5) flou de bougé sur les `Transform` (`MotionBlur` 1, `Quality` 8, `ShutterAngle` 180). 7 images de timeline suffisent ; Fusion compose l'alpha de V2 sur V1.
- **Recettes V5 Sony** [TESTÉ EN CONDITIONS RÉELLES 2026-10-11] :
  - **Inversion sans couper un plan animé** : poser au-dessus (V3) le même rush, mêmes images source (`GetSourceStartFrame`), sur 1-2 images ; `ExportFusionComp` du plan dessous → `ImportFusionComp` sur le calque (même punch-in, même flou) ; LUT négative (`…_negatif.cube`) et CDL du plan dessous. Le contrôle des doublons ignore un calque du même plan.
  - **Changer de moment en gardant la vitesse** : `AppendToTimeline` de la durée voulue en images source à 100 %, puis `SetSpeed({"Percentage": 300})` : la durée dans la timeline reste, la source s'allonge (12 → 36 images à 50p).
  - **Recaler un son** : pas de déplacement par l'API ; `DeleteClips` puis `AppendToTimeline` `"mediaType": 2` avec `startFrame` = `GetLeftOffset()` et le même volume. Position du point de synchro = début + attaque (ou crête) mesurée × 25 − décalage d'entrée.
- **Recettes V4 Sony** [TESTÉ EN CONDITIONS RÉELLES 2026-10-11] :
  - **Step-print** : `TimeStretcher` entre `MediaIn` et la sortie, `ts.SourceTime.SetExpression("floor(time/4)*4")` (rush 50p : chaque image tenue 2 images de timeline, au vrai tempo). Contrôle : écart entre images consécutives alternativement nul.
  - **Écran partagé** : un plan par piste (V1, V2, V3), chacun `Transform` (sujet au centre de sa bande) → `MatteControl` (`Garbage.Matte` = `RectangleMask` de la bande, `Garbage.MaskInverted` 1) ; `Width`/`Height` du masque en unités normalisées de l'image (hauteur 632/1920).
  - **Inversion d'une image APRÈS l'étalonnage** : Fusion passe avant la LUT ; fabriquer une LUT « négative » (1 − sortie de la LUT de look) et la poser sur un segment d'une image découpé dans le plan (source continue : pas un doublon).
  - **Titre en deux graisses** : deux `TextPlus` (`Font` « SST Pro », `Style` « Medium » / « Light », `UseFrameFormatSettings` 0, 1080x1920) sur un `Background` transparent ; positions calculées avec les largeurs PIL des mots (taille Fusion 0,1 = 64 px par em en 1080 de large). Apparition : `Blur.XBlurSize`, `Transform.Center` et `Merge.Blend` animés.
  - **Pistes** : `SetTrackEnable` peut répondre `True` sans tenir si Resolve n'est pas sur la page Montage (`resolve.OpenPage("edit")`) ; après un plantage, une piste désactivée pendant un rendu de contrôle peut le rester : relire `GetIsTrackEnabled` avant le rendu final.
  - **Son** : `AppendToTimeline` avec `"mediaType": 2` et `trackIndex` = piste audio (`startFrame`/`endFrame` en images de timeline) ; volume `SetProperty("AudioVolume", dB)` ; hauteur `AudioPitchSemiTones`.
  - `ExportCurrentFrameAsStill` exporte l'image du plan **du dessus** (le grain en V5 masquait tout) : pour une image de contrôle, rendre une image en PNG 16 bits (`SetCurrentRenderFormatAndCodec("png", "RGB16")`).
  - **Collage / détourage soigné** : timeline jetable avec l'image figée (LUT) et la même image passée dans un `ofx.com.blackmagicdesign.resolvefx.DepthMap` neuf (sans lire ses réglages !), rendues en PNG 16 bits ; `labo/outils/phase3/v4/detourage.py` (Otsu sur la profondeur, GrabCut, filtre guidé, indices manuels pour les cheveux sombres sur fond sombre) puis `collage.py` (ProRes 4444) ; posé sans LUT.
- **Recettes du mariage-jo (2026-10-12)** [TESTÉ EN CONDITIONS RÉELLES] :
  - **Ralenti au-delà de ×2** : `SetSpeed({"Percentage": 25})` puis `SetProperty("RetimeProcess", resolve.RETIME_OPTICAL_FLOW)` et `SetProperty("MotionEstimation", resolve.MOTION_EST_SPEED_WARP_BETTER)` : relus justes, rendus. Comparaison à 200 % sur un plan 50p à ×4 : fondu d'images = membres dédoublés ; flux optique « Enhanced Better » et Speed Warp = nets, léger étirement au bout des doigts.
  - **Voix** : `TimelineItem.SetVoiceIsolationState({"isEnabled": True, "amount": 35})` sur chaque clip de la piste voix (timeline active seulement) ; le nivellement de dialogue existe aussi en propriétés (`AudioDialogueLeveler*`). Le compresseur et le limiteur de Fairlight ne sont pas scriptables : précompresser la source (ffmpeg `acompressor` + `alimiter`) et finir le master son hors de Resolve (rendu « Audio Only » WAV 24 bits, limiteur, remultiplexage `-c:v copy`).
  - **Rendu** : dans un conteneur mp4, `AudioCodec` « lpcm » est refusé (AAC seulement) ; `LoadRenderPreset("Audio Only")` + `ExportVideo: False` rend un WAV 24 bits en 15 s pour 5 min 30.
  - **Média réécrit sur disque** (titre refait) : `MediaPoolItem.ReplaceClip(chemin)` force Resolve à relire le fichier.
  - **Lire des données** (un montage de 125 plans en JSON) : `run_script` ne lit pas les fichiers ; `run_script_unsafe` en lecture seule, chaque usage au journal.
  - **CDL avant LUT pour remonter le contraste d'un plan laiteux** (jour blanc couvert, S-Log3) : pente 1,18-1,28 et décalage 0,55 × (1 − pente) : pivot vers 0,55 en log, les ombres descendent, les blancs restent.
- **Rendre une plage pour contrôler** : `SetRenderSettings({"SelectAllFrames": False, "MarkIn": T0+f, "MarkOut": T0+f+5, …})`, puis attendre le fichier (une composition avec carte de profondeur rend en plusieurs secondes par image).

## 4 sexies. Garder Resolve léger pendant le montage (consigne de Diego, 2026-10-11 ; déplacée de `PROMPT-PHASE-3.md` à l'audit du 2026-10-12) [universel]
Le look et les effets Fusion alourdissent Resolve : lecture saccadée pour Diego, rendus lents. Ordre de travail :
- **Proxies** : relier à chaque rush une copie légère (`LinkProxyMedia` dans l'API, si elle est disponible ; sinon les proxies de Resolve), et rendre le final depuis les originaux. Sony : `LinkProxyMedia` non éprouvé [NON VÉRIFIÉ] ; lire rotation et gamma avant de fabriquer un proxy (`montage-pilotage-mcp`).
- **Le look se décide tôt, s'applique tard** : réglé sur 6 images avant le montage, enregistré en LUT (`LUT/P3/`) ou DRX ; pendant le montage, les plans ne portent que la conversion technique ; le look est posé sur tous les plans à la finition [TESTÉ EN CONDITIONS RÉELLES, Sony : look en un seul nœud].
- **Les effets sur des pistes à eux** : flashs, textes, grain et compositions Fusion sur des pistes hautes dédiées, désactivées pendant le montage et réactivées pour vérifier ou rendre (`SetTrackEnable`, sur la page Montage seulement ; relire `GetIsTrackEnabled` avant le rendu final). Les effets posés sur les plans eux-mêmes (zoom, secousse) viennent en dernier, bloc par bloc.
- **Vérifier un passage sans tout rendre** : rendu de plage (`MarkIn` / `MarkOut`), en basse définition si l'on ne juge que le rythme.

## 5. À vérifier en phase 3
- README livré avec la version installée sur le Mac : ce qui reste scriptable en version gratuite.
- Les codes exacts de `SetCurrentRenderFormatAndCodec` (lister avec `GetRenderFormats()`, `GetRenderCodecs()`).
- `GetNodeGraph().ApplyGradeFromDRX` et `GetNodeGraph().SetLUT` sur une timeline de test (index de node à partir de 1).
- Retime Frame avec clés Step In / Step Out (équivalent des clés Hold d'AE ?), et Freeze Frame de Retime Controls « automatically eased » sur des tenues de 2-4 images.
- L'arbre de nodes du § 2 sur un vrai rush log, comparé à une LUT unique (temps, rendu de la peau).
