# Journal Resolve — P3-sony-linkbuds-agent

_Base « TEST IA », Resolve Studio 21.1.1. Chaque appel MCP (`run_script` sauf mention), son résultat et son contrôle. Gestes déjà validés : `labo/mcp/journal-2026-10-11.md`._

| # | Heure | Geste | Appel | Résultat | Contrôle |
|---|---|---|---|---|---|
| 1 | 13:2x | Projet | `pm.CreateProject("P3-sony-linkbuds-agent")` ; `SetSetting` 1080 / 1920 / 25 | créé ; `timelinePlaybackFrameRate` refusé (sans effet ici) | `GetName()` |
| 2 | | Import | dossiers RUSH, SON, MUSIQUE, ASSET, SFX ; `ImportMedia([".../SONY copy/RUSH/"])` (dossier entier), musique, plan de fin, logo | 252 rushes, 1 musique, 2 assets ; sources non modifiées (import = référence) | comptes |
| 3 | | Timeline | `CreateEmptyTimeline("SONY_V1")`, `useCustomSettings` 1080/1920/25 | ok | — |
| 4 | | Musique, segment 1 | `AppendToTimeline` mp3 `startFrame 2253, endFrame 3096`, piste A1, `recordFrame 90000` (images à 25 i/s pour un fichier son) | 0-843 | positions relues |
| 5 | | Musique, segment 2 | idem `3143-3789` à `90843` ; `SetFades({"FadeOut":40})` | 843-1489 | relu |
| 6 | | Fondu enchaîné son | `items[0].AddTransition({"type":"Cross Fade +3 dB","category":"audio","position":"end","alignment":"center","duration":2})` | 842-844 ; **supprimé si l'on supprime un des deux plans** (à reposer) | relu |
| 7 | | Image V1 | 68 `AppendToTimeline` (rush 50p : `startFrame = s×50`, `endFrame = start + 2×durée`) | 68 plans, un seul trou (415-419, voulu) | positions relues |
| 8 | | Ralentis | `SetSpeed({"Percentage":50,"RippleTimeline":False})` sur 562, 1030, 1265 | durée gardée | relu |
| 9 | | LUT | `GetNodeGraph().SetLUT(1,"Sony/SLog3SGamut3.CineToLC-709TypeA.cube")` ×68 | 68/68 | images |
| 10 | | Plan de fin | asset ProRes 50p `0-84` en V1 à 1447 + son en A5 | 1447-1489 | image : noir puis SONY |
| 11 | | SFX ×19 + voix | `AppendToTimeline` (A2, A3, A6) avec `AudioVolume` ; voix = son de C6577 (`startFrame 715-859`, images 50p) en A4, fondus 2/3 | crêtes calées (crête mesurée du fichier → départ = image − crête×25) | positions relues |
| 12 | | Punch-ins | composition du plan : `Transform`, `AddModifier("Size","BezierSpline")`, `SetKeyFrames({0:{1:1.0,"RH":…},6:{1:1.25,"LH":{1:-3,2:0}}})` sur 368, 866, 1078 ; zoom lent 374 (0 → 80) | **réussi** | bandes d'images du rendu |
| 13 | | Secousse | `tr.Size=1.06` ; `tr.Center.SetExpression("Point(0.5+0.025*sin(time*2.4)*max(0,1-time/10), …)")` sur 468 | **réussi** | bande 464-476 |
| 14 | | Flashs | porteurs C6478 en V2 (1 ou 2 images) + `Background` blanc → `MediaOut1` à 140, 368, 374, 468, 1078 | **réussi** | bandes : blanc exactement aux bonnes images |
| 15 | | Texte | porteur en V3 1360-1447, `TextPlus` « LinkBuds Clip », SST Pro Medium, taille par clés 0,153 → 0,17 (8 images de composition) | réussi ; l'outil s'appelle `Text1` (et non `TextPlus1`) : le retrouver par `TOOLS_RegID` | image du rendu |
| 16 | | Transitions | `AddTransition` Push (70→94, 8), Glitch fusion (796→843, 6), Blur Dissolve (1018→1030, 8), Zoom In fusion (1335→1358, 8) | 4/4 | bandes |
| 17 | 13:45 | Rendu V0 | `SetRenderSettings` mp4 H264 1080x1920 25 AAC 48k ; 16 s | **son saturé** (+4,4 dBTP), texte trop petit | QC |
| 18 | | Niveaux | musique -8, SFX -6, logo Sony +6 ; texte 0,17 | | |
| 19 | | Rendu V1 | 18 s | -15,5 LUFS / -2,4 dBTP | QC, planches, luminance |
| 20 | | CDL | `SetCDL({"NodeIndex":"1","Slope":"1.25 1.25 1.25","Offset":"0.02 …"})` sur 6 plans sombres : **le CDL agit avec la LUT dans le même nœud** (28 → 45 de luminance moyenne mesurée) | **réussi** | image avant / après |
| 21 | | Remplacements | `DeleteClips` puis `AppendToTimeline` + LUT (0, 9, 1405) | transitions voisines conservées | relu |
| 22 | | Son +1 dB | `SetProperties({"AudioVolume": v+1})` toutes pistes | | |
| 23 | | Rendu V2 | 14 s ; projet enregistré | **-14,5 LUFS, -1,4 dBTP**, flash_check OK | QC |

Aucun usage de `run_script_unsafe`. Aucun projet hors `P3-*` ouvert. Sources lues seulement (import = référence).

## V3 (2026-10-11, 15:30-16:00) — timeline `SONY_V3`
_Tous les appels par `run_script` (bac à sable, sans accès disque), aucun `run_script_unsafe`. Aucun projet hors `P3-*` ouvert. Rushes en lecture seule. Contrôle après chaque geste : rendu d'une plage (`MarkIn` / `MarkOut`) puis images extraites._

| # | Geste | Appel | Résultat | Contrôle |
|---|---|---|---|---|
| 24 | Import SFX (19, copiés du dossier de Claude nu, licence Artlist de Diego) et éléments (blanc, grain) | `ImportMedia` | 33 SFX, GFX | comptes |
| 25 | Timeline 1080x1920 25 i/s, 6 pistes vidéo, 8 audio | `CreateEmptyTimeline("SONY_V3")`, `SetSetting`, `AddTrack` | ok | réglages relus |
| 26 | Musique en 2 segments | `AppendToTimeline` mp3 `2487-3143` puis `3331-3789` | 0-656, 656-1114 | positions |
| 27 | 90 plans + LUT de look | `AppendToTimeline` (rush 50p : `endFrame = start + 2 × durée`), `SetSpeed` 0 / 50 / 150 / 200, `SetLUT(1,"P3/P3_sony_look_film_D.cube")` | 90/90, un seul trou voulu (179-185) | relecture des positions ; brouillon V3a |
| 28 | Exposition par plan | `SetCDL` décalage sur le log (−0,065 à +0,05) | 27 plans | V3b |
| 29 | Impacts, poussées, punch-in, secousses | Fusion : `Transform` + `BezierSpline.SetKeyFrames` ; secousse par expression | 30 plans ; **poignées passées en absolu par erreur** → zooms à 1,9× | valeurs relues (`tr.Size[t]`) → geste 35 |
| 30 | Détourages | Fusion : `DepthMap` (aperçu de profondeur) → `BitmapMask` → `ErodeDilate` → fond → `Merge` ×2 | **dédoublés** : la composition d'un arrêt sur image n'est pas figée ; corrigé par `TimeSpeed` (vitesse 0) après `MediaIn` et sans flou de bougé | 3 rendus de plage par essai |
| 31 | Fond et contour à travers la LUT | valeurs S-Log3 calculées en inversant la LUT (orange 0,58/0,42/0,0 ; blanc 0,80) | couleurs justes | images |
| 32 | Flashs | **une image fixe (PNG) prend 125 images quoi qu'on demande** → courte vidéo blanche ProRes, 1 image, `Opacity`, `COMPOSITE_ADD` | 34 puis 28 | test de photosensibilité |
| 33 | Grain | ProRes 4 s de bruit, piste V5, `COMPOSITE_OVERLAY`, 35 % | ok | — |
| 34 | SFX | 64 `AppendToTimeline` audio, crête calée, répartis sur 6 pistes | 64 | loudness |
| 35 | Clés corrigées | poignées **relatives** (`RH {1: Δt, 2: Δv}`) | impacts 1,25 → 1,0 en 5 images | valeurs relues |
| 36 | Stabilisation Resolve | `TimelineItem.Stabilize()` | **recadrage énorme**, packshot illisible → plans reposés | image |
| 37 | Stabilisation par la trajectoire mesurée | `tremblement.py --json` sur le rush (50p), `Transform` « Stab » (taille 1,04) avec `Center` clé à chaque image = −reste | 5,5 → 2,7 px ; 1,7 → 0,7 ; 3,8 → 1,8 | `tremblement.py` sur le rendu |
| 38 | Titre | `TextPlus` SST Pro Roman 0,135, interlettrage 1,06 → 1,0, montée sous `RectangleMask`, flou de bougé, porteur sur V4 | lisible | 3 rendus d'essai |
| 39 | Niveaux | +1,3 dB partout, impacts −2,5 dB ; 6 flashs retirés | −14,1 LUFS, −1,1 dBTP, photosensibilité OK | `qc_livraison.sh`, `flash_check.py` |
| 40 | Look D2 | `SetLUT(1,"P3/P3_sony_look_film_D2.cube")` ×90 | saturation 89 → 100 | rendu final `sony_linkbuds_V3.mp4` ; projet enregistré |

Gyroflow : essai en ligne de commande refusé par le bac à sable de macOS (« Unable to read the video file », l'app ne lit que `~/Library/Application Support/Gyroflow/`). Diego a choisi de lui donner l'accès au dossier `SONY copy` ; marche à suivre donnée dans la conversation, test à refaire après.

## V4 (2026-10-11, session V4) — timeline `SONY_V4` (dupliquée de `SONY_V3`)
_Appels par `run_script` (bac à sable) ; aucun `run_script_unsafe`. Aucun projet hors `P3-*`. Rushes en lecture seule ; fichiers Gyroflow `_stabilized*` écrits à côté des originaux (accord de Diego). Contrôle de chaque geste par un rendu de plage._

| # | Geste | Appel / outil | Résultat | Contrôle |
|---|---|---|---|---|
| 41 | Gyroflow (CLI, version GitHub) | `-t _stabilized`, preset zoom fixe 115 %, ProRes HQ ; puis `do_autosync` sur plages courtes | 9 + 6 fichiers ; C6723 désynchronisé sans autosync (9,7 px), juste avec (1,9) | `tremblement.py --avant`, bandes |
| 42 | Timeline V4 | `DuplicateTimeline("SONY_V4")` | V3 intacte | — |
| 43 | LUT V4 salle / jour / rouge / rouge négatif | `look_sony_v4.py` ; `RefreshLUTList()` ; `SetLUT` | séparation des teintes | banc Python = Resolve à 1 % ; `ExportCurrentFrameAsStill` |
| 44 | Ouverture K-O-R-E + zoom infini | `stabiliser.py --mode fixe`, Cale (lettres à 720 px), SIFT E → KORE, V1 + V2, `MatteControl` + fondu d'alpha | lettres 0,2-0,3 px ; recul continu | rendus de plage ; **`comp.Lock()` empêchait le rendu des clés** |
| 45 | Flash cut des oreilles | 7 plans, `Transform` calé sur l'écouteur ; `AppendToTimeline` avec `"mediaType": 1` (sinon échec : conflit audio) | écouteur au même point | recadrages autour du point |
| 46 | Boîtiers et packshots | fichiers Gyroflow synchronisés + `stabiliser.py --mode rail` (clés toutes les 2 images) ; CDL −0,081 | 0,89 / 1,1 / 1,6 px ; ≤ 1,8 % de pixels ≥ 250 | `tremblement.py` sur le rendu |
| 47 | Rafale 1 (monte) | 9 plans, `SetSpeed` 300 %, glissement vertical | — | planche |
| 48 | Rafale 2 (step-print) | `TimeStretcher` `SourceTime` = `floor(time/4)*4` | images tenues par deux (écart 0,0 / saut) | écarts entre images |
| 49 | Rafale 3 (écran partagé) | 3 plans sur V1/V2/V3, `RectangleMask` + `MatteControl` par bande | bandes ouvertes sur les temps | images |
| 50 | Rafale 4 (inversions) | segments d'une image avec la LUT « rouge négatif » | 3 inversions en 0,92 s | `flash_check.py` |
| 51 | Collages ×3 | `TEST_GELS` : images figées + `ofx…DepthMap` rendus en PNG 16 bits ; `detourage.py` ; `collage.py` → ProRes 4444 | arrêt puis reprise du mouvement | aperçus pleine résolution |
| 52 | **Resolve figé** | boucle `GetInput` sur l'outil OFX DepthMap | roue qui tourne ; `kill` avec l'accord de Diego, relance, `LoadProject` : rien perdu | timeline relue |
| 53 | Doublons | `doublons_timeline.py` (+ table `DECALAGES` des plages Gyroflow) | 11 → 0 | — |
| 54 | Titre | 2 `TextPlus` (SST Pro Medium / Light) sur `Background` transparent, `Blur` + `Transform` + `Merge` Blend animés ; **`SetTrackEnable` ne tient que sur la page Montage** | — | comparé à la DA Sony |
| 55 | SFX | 64 retirés, 63 posés (`AppendToTimeline` `"mediaType": 2`, `SetProperty("AudioVolume", dB)`), crête calée | — | loudness |
| 56 | Rendu final | `H265`, `EncodingProfile` Main10, `MultiPassEncode`, `VideoQuality` 40000 | HEVC Main 10 10 bits 39 Mb/s ; −14,0 LUFS, −1,1 dBTP | `qc_livraison.sh`, `flash_check.py`, PSNR 40,7 dB |
