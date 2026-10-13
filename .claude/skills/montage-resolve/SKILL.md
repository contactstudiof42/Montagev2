---
name: montage-resolve
description: DaVinci Resolve — étalonnage par nodes (série, parallèle, layer mixer), gestion des couleurs (RCM, DaVinci Wide Gamut, ACEScct), Deliver et rendus en lot, Fusion, Fairlight, saccade et retime, ralentis Speed Warp, stabilisation et Gyroflow, scripting Python et pilotage par le serveur MCP natif (GetNodeGraph, AppendToTimeline, AddRenderJob, export EDL/XML/AAF). Mots d'un étalonneur ou d'un monteur : « on passe en étalo », « arbre de nodes », « monter un look », « recréer la colo de tel film », « reproduire le look de cette référence », « qualifier la peau », « power window », « rendu en lot », « automatiser l'export », « script Resolve », « je fais le plan dans Fusion ? », « ça rame ».
---

# DaVinci Resolve

_Réécrit le 2026-10-13 (audit 2) : chaque règle cite l'erreur qui l'a gagnée ou le mot de Diego qu'elle porte. Recettes éprouvées en conditions réelles (gestes par l'API, Fusion, couleur, son, stabilisation, Gyroflow, détourage, rendu) : [recettes.md](recettes.md) ; savoir et API (arbre de nodes, reproduire un look, RCM, squelette Python, Fusion, Fairlight, saccade, évolutions 19 → 21.1) : [details.md](details.md). Capacités du serveur : `labo/mcp/resolve-mcp.md`. Version d'avant : `archives/audit-2/skills/montage-resolve/`._

**Fait foi sur** : l'étalonnage dans Resolve, son API et son serveur MCP, Fusion, Fairlight, le retime et la stabilisation dans Resolve. Formats d'échange : `montage-workflows` ; sens et chaîne de la couleur : `montage-couleur` ; cibles de loudness : `montage-loudness-livraison` ; méthode de pilotage : `montage-pilotage-mcp`.

## 1. Quand Resolve
L'outil de référence pour l'étalonnage (nodes, qualifications, fenêtres suivies, gestion des couleurs de bout en bout), la conformation d'un montage venu d'ailleurs, et l'automatisation (rendus en lot, assemblage d'une liste de plans, look posé sur toute une timeline). Sur ce Mac : Resolve Studio 21.1.1, piloté par son serveur MCP natif (`run_script`).

## 2. Les pièges qui ont coûté cher [TESTÉ EN CONDITIONS RÉELLES]
- **Projets `P3-<projet>-agent` seulement** ; `SaveProject` avant tout geste risqué ; `run_script` est un bac à sable (ni fichiers ni `os`) : `run_script_unsafe` seulement pour lire un fichier quand aucun outil dédié ne le permet, jamais pour supprimer, chaque usage au journal (`PROMPT-PHASE-3.md`).
- **Jamais `InsertFusionTitleIntoTimeline` ni `Insert…Generator…`** sur une timeline montée : montage par insertion qui coupe et pousse tout, son compris. Texte, flash, aplat : un plan porteur posé par `AppendToTimeline` sur une piste haute, puis une composition Fusion.
- **L'œil, c'est le rendu** : `ExportCurrentFrameAsStill` peut exporter l'image d'avant, le plan du dessus ou la dernière image du film ; `GetCurrentVideoItem()` peut renvoyer le plan précédent. Pour juger : un rendu de plage (PNG 16 bits si besoin). (Gagnée sur les deux projets.)
- **Un média remplacé sur disque sous le même nom devient illisible au rendu** : toujours un nouveau nom (ou `MediaPoolItem.ReplaceClip`). (Gagnée : V4 du film de mariage.)
- **Jamais `comp.Lock()` pendant la pose des clés** : les valeurs relues sont justes, le rendu lit l'animation figée. Toujours contrôler une animation par un rendu de plage, pas par la relecture des valeurs.
- **Ne jamais lire les entrées d'un effet IA OpenFX par script** (carte de profondeur…) : Resolve s'est figé, il a fallu le forcer à quitter (avec l'accord de Diego, à redemander chaque fois).
- **Fusion passe avant le nœud de couleur** : une couleur posée dans Fusion traverse la LUT de look ; **le CDL du nœud 1 agit avant sa LUT**.
- **Une LUT se pose seulement depuis le dossier de LUT de Resolve** (les miennes dans `P3/`), après `RefreshLUTList()` quand elle vient d'être écrite.
- **`SetSpeed(0)` ne tient pas la bonne image** dans une composition : un plan fixe fabriqué depuis l'image exacte du rush, ou un `TimeSpeed` à 0 juste après `MediaIn`.
- **Monter = reconstruire** : pas de lame ni de trim dans l'API ; on supprime (`DeleteClips`) et on repose (`AppendToTimeline`, `startFrame` / `endFrame` en images de la source, `endFrame` exclusif, `recordFrame` absolu).

## 3. Garder Resolve léger pendant le montage [universel] (consigne de Diego, 2026-10-11)
Le look et les effets Fusion alourdissent Resolve (lecture saccadée pour Diego, rendus lents) :
- proxies reliés aux rushes, rendu final depuis les originaux (lire rotation et gamma avant de fabriquer un proxy) ;
- le look se décide tôt et s'applique tard : réglé sur 6 images avant le montage, enregistré en LUT ou en DRX, posé sur tous les plans à la finition ;
- les effets sur des pistes à eux (flashs, textes, grain, compositions), désactivées pendant le montage (`SetTrackEnable` sur la page Montage seulement ; relire `GetIsTrackEnabled` avant le rendu final) ;
- vérifier un passage sans tout rendre : rendu de plage (`MarkIn` / `MarkOut`), en basse définition si l'on ne juge que le rythme.
