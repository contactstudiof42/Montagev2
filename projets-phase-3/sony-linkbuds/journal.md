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
