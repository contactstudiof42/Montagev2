# État public des serveurs MCP / ponts IA pour la post-production (2026-10-10)

Recherche web uniquement. **Aucun serveur n'a été installé ni appelé.** Ce fichier complète `PLAN-TESTS-MCP.md` (noms d'outils Higgsfield observés) et `sources/ia-verif-2026-10-10.md` (plugins Higgsfield) sans les recopier.

Légende :
- **[V]** : vérifié sur la page source (README GitHub, page officielle, PyPI) le 2026-10-10. Cela veut dire « la page le dit », pas « ça marche ».
- **[A]** : annoncé par un agrégateur ou un tiers (glama, mcpservers, blogs), ou déduit. À confirmer.
- **[L]** : constaté localement, dans la liste d'outils de la session (cf. PLAN-TESTS-MCP.md).

Limite de méthode : l'API GitHub n'était pas accessible depuis la VM. Les dates de « dernier commit » ont été lues sur la page `/commits/main` via WebFetch et sont donc fiables seulement au jour près. Le nombre d'étoiles est celui que la page affichait.

---

## 1. Blender

### blender-mcp (« MCP for Blender »), ahujasid
- URL : https://github.com/ahujasid/blender-mcp · PyPI : https://pypi.org/project/blender-mcp/
- Activité : dernier commit le 2026-10-06 (« fix: resume generations after client timeouts ») [V]. Version PyPI 2.0.0 publiée le 2026-09-16 [V]. ~30 k étoiles [V].
- Licence : MIT [V]. Projet non affilié à la Blender Foundation [V].
- Mécanisme : un add-on (`addon.py`) ouvre un **socket TCP JSON dans Blender** (localhost:9876 par défaut, port configurable) ; le serveur MCP Python s'y connecte [V].
- Capacités (9 outils annoncés) : `execute_blender_code`, `look` (vues viewport, caméra, multi-angles, animation), `get_scene_info`, `generate_3d`, `search_assets` / `import_asset`, `get_addon_status`, `disable_telemetry`, `record_trajectory_feedback` [V]. Intégrations : Poly Haven (CC0, sans clé), Sketchfab et Poly Pizza (avec clé ; certains modèles sont en CC-BY, donc à créditer), génération 3D Hyper3D Rodin / Tripo / Hunyuan3D [V].
- Requis : Blender ≥ 3.0, Python ≥ 3.10 [V].
- Risques : `execute_blender_code` exécute du Python arbitraire ; le README dit « ALWAYS save your work » [V]. Mode sûr `BLENDER_MCP_SAFE_MODE=1` (bloque fichiers, programmes externes et réseau) [V]. Socket **sans authentification ni chiffrement** : à garder sur localhost [V]. **Télémétrie anonyme active par défaut** (`DISABLE_TELEMETRY=true` pour la couper) [V]. Les générations 3D par API tierce peuvent être payantes [A].

### Higgsfield pour Blender (add-on + « Higgsfield Bridge »)
- URL : https://higgsfield.ai/plugins/blender · aide : https://higgsfield.ai/creator-hub/help-center/mcp-cli/external-integrations-higgsfield
- Mécanisme : Add-on `.zip` signé, installé par glisser-déposer, qui affiche une barre flottante dans la vue 3D [V]. L'agent passe par le connecteur MCP **distant** `https://bridge.higgsfield.ai/mcp` (nommé « Higgsfield Bridge »), qui relaie vers l'add-on local [V]. Le trajet réseau exact (cloud → add-on) n'est pas documenté [A].
- Capacités : 7 onglets (Scene builder, 3D Model, Character animation, Image, Video, Camera, Asset). Modèles annoncés : Nano Banana 2, GPT Image, Seedream 5.0 Pro, Seedance 2.5, Meshy 5 [V]. Côté MCP, outils `bl_*` dont `bl_execute` (bpy arbitraire), `bl_install_py_addon`, `bl_generate_3d` [L].
- Requis : **Blender ≥ 5.1**, Windows ou macOS, connexion internet, compte Higgsfield connecté [V].
- Licence : propriétaire. Les droits d'usage commercial des générations suivent les CGU du plan payant [V].
- Risques : Consomme les crédits du forfait Higgsfield, au même tarif que le web [V]. Les instructions du serveur disent qu'« une demande explicite de génération autorise l'envoi immédiat, sans seconde confirmation » [L]. Cela entre en conflit avec la règle 9 du skill. `bl_execute` permet d'exécuter du code arbitraire [L]. La page officielle contient des métadonnées incohérentes (FAQ décrivant le plugin Adobe) [V].
- Date : lancement le 25/08/2026 selon un tiers (https://creatify.ai/fr/blog/what-is-higgsfield-mcp-what-it-does-what-it-costs-and-how-to-use-it) [A].

## 2. DaVinci Resolve (API de scripting Python `DaVinciResolveScript`)

### davinci-resolve-mcp, Samuel Gursky
- URL : https://github.com/samuelgursky/davinci-resolve-mcp
- Activité : dernier commit le **2026-10-09**, version **v4.10.3** [V]. ~3,4 k étoiles, plus de 1 000 commits [V].
- Licence : MIT [V]. Les dépendances optionnelles (ffmpeg, Whisper, librosa…) et leurs poids de modèles ont leurs propres licences [V].
- Mécanisme : API de scripting officielle en **mode externe** : Resolve **Studio**, avec la préférence « External scripting using » réglée sur **Local** [V]. Pour la version gratuite : un pont lancé depuis Workspace ▸ Scripts ouvre un listener loopback authentifié [V]. L'auteur le dit « supported-until-it-is-not », et ce chemin n'est **pas confirmé sur Resolve 21.1** [V]. Un serveur Node optionnel lit et édite les `.drp`/`.drt`/`.drx` hors ligne [V].
- Capacités annoncées : 37 outils « compound » par défaut, ou 389 en mode granulaire [V]. Couverture : projets, media pool, montage, marqueurs, étalonnage, Fusion, Fairlight, rendu, extensions (Fuse, DCTL, scripts) [V]. L'auteur annonce 361/361 méthodes couvertes, dont 338 testées [A, auto-déclaré].
- Requis : Resolve ≥ 18.5 (base 19.1.3). Testé sur Studio 19.1.3, 20.3.2 et 21.0.2, et sur la version gratuite 21.0.3 via le pont. Python 3.10–3.12. Les fonctions de Resolve 21 demandent le pack « AI Extras » [V].
- Risques : L'installeur modifie les configurations des clients MCP et installe des scripts dans Resolve [V]. Le README ne parle pas d'exécution de code arbitraire. Les « extensions » (scripts, DCTL) en permettent probablement [A]. L'auteur déconseille de se fier à `rank_takes` pour choisir une prise [V].

### davinci-resolve-mcp, Tooflex
- URL : https://github.com/tooflex/davinci-resolve-mcp
- Activité : 16 commits, aucune release, aucune date visible ; ~19 étoiles [V].
- Licence : **non indiquée** sur la page [V], donc sans droit de réutilisation par défaut.
- Mécanisme : serveur MCP en stdio qui importe le module de scripting natif. Il vérifie d'abord ce module dans un sous-processus [V].
- Capacités : 32 outils (projets, médias, timelines, Fusion, couleur, audio, lecture, rendu) et 6 ressources en lecture seule [V].
- Requis : **Studio ≥ 18** (la version gratuite n'a pas de scripting externe), Python 64 bits **3.10 ou 3.11** (3.12+ cassé par `imp`) [V].
- Risques : `execute_lua` exécute du Lua arbitraire dans Fusion [V]. Plantage `0xC0000005` sous Windows si le mauvais runtime Python est chargé [V].
- Autre listing : https://glama.ai/mcp/servers/@hnethery/davinci-resolve-mcp, déjà cité dans `resolve-scripting.md` et non revu ici.

## 3. After Effects (ExtendScript)

### after-effects-mcp, Dakkshin
- URL : https://github.com/Dakkshin/after-effects-mcp
- Activité : dernier commit le **2026-04-01** [V]. ~720 étoiles, aucune release [V].
- Licence : MIT [V].
- Mécanisme : serveur Node/TS. Un script `mcp-bridge-auto.jsx` ouvert dans AE (menu Window) **interroge des fichiers de commandes toutes les quelques secondes** et les exécute en ExtendScript [V].
- Outils : create-composition, run-script, get-results, setLayerKeyframe, setLayerExpression, (batch)setLayerProperties, getLayerInfo, createCamera, createNullObject, duplicateLayer, deleteLayer, setLayerMask [V].
- Requis : AE 2022+, Node 14+ [V].
- Risques : `run-script` exécute du JS arbitraire [A, déduit du nom]. Un témoignage tiers rapporte qu'il ne prend pas les commandes sur macOS [A]. Fork documenté : `p10q/ae-mcp` (pont fichiers + panneau CEP, MIT selon https://mcpservers.org/servers/p10q/ae-mcp). Son dépôt GitHub renvoyait 404 le 2026-10-10 [V].

### mcp-aftereffects, kumo.productions
- URL : https://github.com/kumoproductions/mcp-aftereffects (npm `@kumoproductions/mcp-aftereffects`)
- Activité : 24 commits, date non visible ; ~100 étoiles [V].
- Licence : MIT (© 2026) [V].
- Mécanisme : un agent résident installe un script dans `Scripts/Startup` et lit une « mailbox » de fichiers dans le dossier temporaire (IPC par fichiers, ExtendScript) [V].
- Capacités : inspection projet / comps / calques, propriétés, clés, effets, masques, texte, formes, expressions, sauvegardes, rendu d'images. Outils `ae_context`, `ae_do`, `instance.*` (y compris la fermeture de dialogues) [V].
- Requis : AE 2024–2026, Windows ou macOS, Node 24+. Préférence « Allow Scripts to Write Files and Access Network » à activer. Sur macOS : autorisations Automatisation et Accessibilité [V].
- Risques : L'eval ExtendScript arbitraire est **désactivé par défaut** (`AE_MCP_ENABLE_EVAL=1`) ; la page dit qu'il « may permit actions that affect your entire computer » [V]. Les noms de calques, expressions et chemins partent vers le fournisseur d'IA : point d'attention pour les projets sous NDA [V].
- Autre : `Brandkick/after-effects-mcp` (panneau CEP + WebSocket, AE 2021+) n'est connu que par glama (https://glama.ai/mcp/servers/rqf9e57phr) [A].

## 4. Premiere Pro (CEP/ExtendScript et UXP)

### Adobe_Premiere_Pro_MCP, hetpatel-11 (site premiere-mcp.com)
- URL : https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP
- Activité : dernier commit le **2026-09-03** [V]. ~670 étoiles [V].
- Licence : MIT [V].
- Mécanisme : Le **pont CEP est le seul supporté** : Node génère de l'ExtendScript dans `/tmp/premiere-mcp-bridge`, et le panneau l'exécute par `CSInterface.evalScript()` [V]. Le plugin UXP est expérimental [V].
- Capacités : 283 outils au catalogue, dont 5 exposés par défaut (`PREMIERE_MCP_TOOLSET=full` les expose tous). Domaines : projet, import, séquences, montage, transitions, effets, clés, sous-titres, marqueurs, couleur, audio, export [V].
- Requis : Premiere 2020+ (testé sur 26.0), Node 20+, tout sur la même machine [V].
- Risques : `execute_extendscript` exécute du code arbitraire [V]. `ripple_delete` et les suppressions agissent **sans confirmation** [V]. Télémétrie anonyme **active par défaut** (`PREMIERE_MCP_TELEMETRY=0`) [V]. Panneau CEP auto-signé ; impossible de retirer un effet avec l'API de Premiere 26 [V].

### mcp_adobe_premiere, morim3
- URL : https://github.com/morim3/mcp_adobe_premiere
- Activité : 3 commits, ~5 étoiles, date non visible [V].
- Licence : MIT (le README cite aussi la MPL, ce qui est incohérent) [V].
- Mécanisme : Python fastmcp → **WebSocket** → plugin **UXP** (TypeScript) chargé par UXP Developer Tool [V].
- Capacités : séquences (création, suppression) et import de médias [V].
- Requis : Premiere **Beta 25.3+** [V].
- Statut : « not ready for production use » [V].
- Autres projets UXP connus seulement par agrégateurs [A] : `nguyenph88/Premiere-Pro-MCP` (dépôt en 404 le 2026-10-10) ; ; « Premiere Pro Full MCP », Windows, UXP + CEP + QE expérimental (https://glama.ai/mcp/servers/ops93ag140).

### Adobe « for creativity » (MCP distant officiel)
- URL : `https://adobe-creativity.adobe.io/mcp`, en Streamable HTTP (https://mcpservers.org/remote-mcp-servers/adobe-creativity) [A].
- Annoncé : disponible depuis le 28/04/2026, plus de 50 outils, couvre Photoshop, Lightroom, Illustrator, Firefly, **Premiere**, Express, InDesign et Stock [A]. Source : https://www.usecarly.com/blog/adobe-mcp/
- **Inconnu** : s'il agit sur le Premiere **desktop** ou seulement sur des services cloud. After Effects n'est pas cité.

## 5. Higgsfield, plugin Adobe (AE + Premiere) et MCP bridge
- URLs : https://higgsfield.ai/plugins/after-effects ; https://higgsfield.ai/plugins/premiere-pro ; https://higgsfield.ai/blog/higgsfield-after-effects (21/07/2026)
- Mécanisme : Panneau d'extension (Fenêtre → Extensions → Higgsfield). Installation par `.dmg` sur macOS, `.zxp` via ZXP Installer sur Windows ; un seul installeur pour AE et Premiere [V]. Le type CEP est probable (`.zxp`, menu Extensions) mais non confirmé [A]. Le même connecteur distant `bridge.higgsfield.ai/mcp` pilote AE et Premiere [V].
- Capacités : Panneau : Reframe, Remove BG, Upscale, Draw to Edit, Edit Video, génération image/vidéo [V]. Côté MCP : comps, calques, clés, effets, expressions [V]. Catalogue `ae_*` / `pr_*` / `bl_*` / `get_host_status`, plus un hôte `bs_*` (Blocking Studio, navigateur) découvert dynamiquement [L].
- Requis : AE / Premiere 2024 (24.0)+ selon le centre d'aide, 25.0 selon la page plugin. La contradiction est déjà notée dans ia-verif [V].
- Licence : propriétaire. Usage soumis au compte et aux crédits Higgsfield [V].
- Risques : Crédits payants au tarif web [V]. Pilotage via un **relais cloud tiers** : le contenu du projet transite probablement par les serveurs Higgsfield [A]. Les permissions de l'agent ne sont pas documentées publiquement [V]. Le serveur impose ses propres procédures (`ae-clean-rig`, `blender-scene`) [L].

## Synthèse comparative

| Logiciel | Projet | Mécanisme | Dernière activité | Licence | Code arbitraire |
|---|---|---|---|---|---|
| Blender | ahujasid/blender-mcp | socket TCP add-on | 2026-10-06 | MIT | oui (mode sûr optionnel) |
| Blender | Higgsfield Bridge | add-on + MCP distant | ? (lancement 08/2026 [A]) | propriétaire | oui (`bl_execute` [L]) |
| Resolve | samuelgursky | API Python externe (Studio) / pont in-app | 2026-10-09 | MIT | probable [A] |
| Resolve | Tooflex | API Python externe (Studio) | ? | non précisée | oui (`execute_lua`) |
| AE | Dakkshin | fichiers + .jsx en scrutation | 2026-04-01 | MIT | oui [A] |
| AE | kumoproductions | fichiers + script Startup | ? | MIT | off par défaut |
| Premiere | hetpatel-11 | CEP evalScript (UXP expérimental) | 2026-09-03 | MIT | oui |
| Premiere | morim3 | UXP + WebSocket (Beta 25.3+) | ? | MIT ? | non documenté |
| AE + Pr | Higgsfield | panneau Adobe + MCP distant | 21/07/2026 (annonce) | propriétaire | inconnu |

Constats transverses :
- Tous les ponts ont la même faiblesse : ce sont des canaux d'exécution locaux (socket, dossier temporaire, evalScript) **sans authentification forte**.
- Deux projets (blender-mcp, hetpatel-11) ont une **télémétrie activée par défaut**.
- La voie UXP reste expérimentale côté Premiere. Côté AE, aucun pont UXP public n'a été trouvé.
