# Fusion et Fairlight dans DaVinci Resolve 19 à 21 (consulté le 2026-10-10)

Complète `.claude/skills/montage-resolve/SKILL.md` et `sources/resolve-scripting-api-19-20.md` (étalonnage, RCM et API Python y sont déjà traités).
Balises : [DOC OFFICIELLE] = lu dans un texte Blackmagic, ou dans une copie fidèle du README livré avec le logiciel · [SOURCE SECONDAIRE] = presse, formateur, forum · [INCERTAIN] = pas lu directement, ou contradiction.
Aucun nom de fonction ne figure ici sans avoir été lu dans une source. Les autres sont marqués [INCERTAIN].

## Sources (toutes consultées le 2026-10-10)
- **FVE20** : Blackmagic, *DaVinci Resolve 20 Fusion Visual Effects* (guide de formation, 2025). https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Fusion-Visual-Effects.pdf
- **BG20** : Blackmagic, *DaVinci Resolve 20 Beginners Guide* (Fairlight leçon 8, Deliver leçon 10). https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Beginners-Guide.pdf
- **NF20 / NF201 / NF202** : *New Features Guide* 20, 20.1 (août 2025), 20.2 (sept. 2025). https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_20_New_Features_Guide.pdf (même chemin avec `20.1_` et `20.2_`)
- **FSG8** : *Fusion 8 Scripting Guide and Reference Manual* (févr. 2016, Lua et Python, FusionScript). https://documents.blackmagicdesign.com/UserManuals/Fusion8_Scripting_Guide.pdf
- **R26 / CL / PYI** : README de scripting Resolve (« Last Updated 24 Jul 2026 », 21.0.4), CHANGELOG (1 sept. 2026, 21.1) et stub `.pyi`, copies hébergées par un tiers. https://github.com/samuelgursky/davinci-resolve-mcp/tree/main/docs/reference
- **PVC18** : K. P. McAuliffe, « After Effects vs Fusion – Which one's right for the Resolve Editor? », ProVideo Coalition, 29/08/2018. https://www.provideocoalition.com/after-effects-vs-fusion-which-ones-right-for-the-resolve-editor/
- **PB** : PremiumBeat, « Fusion vs After Effects ». https://www.premiumbeat.com/blog/fusion-vs-after-effects/ (lu seulement à travers un résumé de recherche)
- **ML19** : Mixing Light, catégorie ACES (Resolve 19, « Managed Color Space View LUT »). https://mixinglight.com/tutorial-category/aces (lu seulement à travers un résumé de recherche)
- **FBM-LH** : forum Blackmagic, « Loudness History Standard? ». https://forum.blackmagicdesign.com/viewtopic.php?p=1144201 (lu seulement à travers un résumé de recherche)
- **DRC** : DaVinci Resolve Club, réglage des niveaux en LUFS. https://davinciresolveclub.com/davinci-resolve-audio-levels-lufs/ (lu seulement à travers un résumé de recherche)

## 1. Fusion : la logique des nodes
- Un clip ouvert dans la page Fusion arrive sous la forme d'un node **MediaIn** (le clip de la timeline Edit). Le node **MediaOut** renvoie l'image vers la timeline. Si on déconnecte MediaOut, le clip devient noir dans la page Edit. [DOC OFFICIELLE] FVE20 p. 13-16
- **Merge** compose deux images. L'entrée jaune reçoit l'arrière-plan (*background*), l'entrée verte le premier plan (*foreground*). Pour l'ajouter, on sélectionne d'abord le node d'arrière-plan. [DOC OFFICIELLE] FVE20
- Pour faire entrer plusieurs clips de la page Edit, il faut créer un **Fusion clip**. Resolve y place les couches dans des Merge, plus un node **Background** qui gère les écarts de résolution et de durée. [DOC OFFICIELLE] FVE20 « Using Layers from the Edit Page »
- **Ordre de traitement** : Edit/Cut → Fusion → Color. Les effets Resolve FX/OFX posés dans la page Edit ne sont pas visibles dans Fusion : ils s'appliquent après, et la seule exception est le redimensionnement et le repositionnement. Pour les voir dans Fusion, il faut d'abord faire un compound clip. [DOC OFFICIELLE] FVE20
- **Tracker** (suivi de points) et **Planar Tracker** (suivi d'une surface plane par polygone). Le Planar Tracker sert au corner pin, puis on garde un **Planar Transform** qui contient les données de suivi. [DOC OFFICIELLE] FVE20 leçon 3
- **Delta Keyer** : c'est l'outil principal pour le fond vert ou bleu. Il a une entrée Clean Plate, une entrée Garbage Matte et une entrée Solid (holdout), et ses réglages essentiels sont dans l'onglet Matte. [DOC OFFICIELLE] FVE20 leçon 4. L'**Ultra Keyer** n'apparaît pas dans les extraits lus. [INCERTAIN]
- **Magic Mask v2** est l'outil par défaut dans Fusion depuis la 20.1. Il fonctionne avec des points positifs et négatifs posés dans le viewer et a 4 entrées. Une case « Use Legacy Magic Mask » garde l'ancien comportement. [DOC OFFICIELLE] NF201
- La 20 ajoute à Fusion un jeu d'outils **Deep Image** (dCrop, dHoldout, dRecolor, dResize, dTransform, Image to Deep, Deep to Image ; MediaIn et Loader lisent l'EXR deep). Elle ajoute aussi l'outil **MultiText**, construit sur Text+, avec import CSV en colonnes (20.1) et de nouveaux contrôles d'alignement (20.2). [DOC OFFICIELLE] NF20, NF201, NF202

## 2. Fusion : espace de travail et couleur
- Avec la gestion des couleurs de Resolve (RCM), l'espace d'entrée de chaque MediaIn serait détecté puis converti en **gamma linéaire**. Les réglages ACES du projet s'appliqueraient aux pages Edit, Fusion et Color. Source : manuel 18.6, connu seulement par un résumé de recherche, et le miroir est en 404. [INCERTAIN] Le principe est cohérent avec la pratique, mais il faut le vérifier dans le manuel 20.
- Resolve 19 aurait ajouté une « Managed Color Space View LUT » pour juger une image linéaire dans le viewer Fusion en ACES ou OCIO. [SOURCE SECONDAIRE] ML19, non lu en entier.
- La 20 gère ACES 2.0 et propose des effets OCIO (OCIO Color Space, OCIO Display, OCIO File Transform, OCIO CDL Transform). [DOC OFFICIELLE] NF20. En 20.1 et 20.2, plusieurs outils ont des contrôles de gamma et d'espace d'entrée, réglés par défaut sur « Use timeline ». [DOC OFFICIELLE] NF201/NF202
- Conséquence pratique : un Merge ou un flou travaille sur des valeurs linéaires, alors que les titres et les couleurs choisis « à l'œil » le sont dans l'espace d'affichage. Un mauvais réglage du viewer produit le classique « ça ne ressemble pas à la page Edit ». [SOURCE SECONDAIRE] fil ACES Central https://community.acescentral.com/t/davinci-15-and-fusion-page/1967

## 3. Macros et templates (.setting) utilisés comme titres
- Méthode : sélectionner les nodes, puis clic droit > **Macro > Create Macro**. Dans le Macro Editor, on coche les paramètres à exposer (par exemple StyledText) et on peut les renommer. [DOC OFFICIELLE] FVE20 p. 163-165
- Pour que le titre apparaisse dans l'Effects Library de la page Edit (Titles), on enregistre dans `.../Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit/Titles/` (macOS : Library/Application Support, Windows : AppData/Roaming), puis on relance Resolve. L'emplacement par défaut ne le rend visible que dans la page Fusion. [DOC OFFICIELLE] FVE20
- Le fichier enregistré est un `.setting`. [SOURCE SECONDAIRE] pratique courante ; l'extension n'est pas écrite dans l'extrait lu.

## 4. Fusion par script
- Dans le moteur Fusion, on obtient l'objet par `resolve.Fusion()`. C'est le point d'entrée de « toute la fonctionnalité de scripting Fusion ». Les scripts placés dans `Fusion/Scripts/Comp` ou `/Tool` sont listés dans la page Fusion, ceux placés dans `Utility` sur toutes les pages. [DOC OFFICIELLE] R26
- Fonctions de l'objet `comp` (FusionScript, Lua `comp:` / Python `comp.`) [DOC OFFICIELLE] FSG8 :
  `Composition.AddTool(id[, defsettings][, xpos][, ypos])`. Avec x = y = -32768, l'outil est placé comme si on avait cliqué dans la barre d'outils, et il est connecté automatiquement si c'est possible. Exemples tirés du guide : `comp.AddTool("Background", 1, 1)`, `comp.AddTool("Merge", -32768, -32768)`.
  `Operator.ConnectInput(input, target)`, par exemple `Merge1.ConnectInput("Foreground", ldr)` ; `Input.ConnectTo(output)` (sans argument, déconnecte) ; `GetConnectedOutput()`.
  `tool:SetInput("Nom", valeur, [temps])` et `GetInput("Nom", temps)` ; écriture directe `Merge1.Angle[5] = 20` ; `SetAttrs({TOOLS_Name=…})`.
  `comp:Lock()` (bloque le rendu pendant le script), `StartUndo("…")` / `EndUndo`, `FindTool(name)`, `FindToolByID(id)`, `GetToolList([selected][, regid])`.
  Limite : ce guide date de Fusion 8 (2016). Je n'ai pas trouvé de guide de scripting Fusion plus récent. [INCERTAIN] Il reste à vérifier que ces signatures sont inchangées dans Resolve 20/21.
- Depuis l'API Resolve vers une comp d'un TimelineItem [DOC OFFICIELLE] R26 :
  `GetFusionCompCount()`, `GetFusionCompByIndex(i)` (1 ≤ i ≤ count), `GetFusionCompNameList()`, `GetFusionCompByName(n)`, `AddFusionComp()`, `ImportFusionComp(path)`, `ExportFusionComp(path, i)`, `DeleteFusionCompByName`, `LoadFusionCompByName`, `RenameFusionCompByName`.
  Côté Timeline : `CreateFusionClip([items])`, `InsertFusionGeneratorIntoTimeline(name)`, `InsertFusionCompositionIntoTimeline()`, `InsertFusionTitleIntoTimeline(name)`, `InsertTitleIntoTimeline(name)`.
  Le CHANGELOG mentionne un correctif : « AddFusionComp sometimes showing incorrect composition ». [DOC OFFICIELLE] CL
- Le nom de RegID des nodes de texte (`TextPlus` ?) et de MediaIn/MediaOut dans `AddTool` n'a pas été lu. [INCERTAIN]

## 5. Fairlight : bus, pistes, loudness, dialogue
- La timeline Fairlight affiche une « piste » **Bus 1**, qui correspond à la sortie stéréo de la timeline. On change son format dans **Fairlight > Bus Format**. [DOC OFFICIELLE] BG20. En 20.1, on peut supprimer un bus depuis l'en-tête de piste, et un bus **ASAF Master** (Apple Spatial Audio, Studio) est disponible. [DOC OFFICIELLE] NF201
- En 20.2, le montage préserve l'automation des bus. Une nouvelle option de projet (Fairlight > General) gère les fondus doux et le « Ramp Up on Play » ; le fondu automatique de 1,5 ms (72 échantillons) existe depuis la v14. [DOC OFFICIELLE] NF202
- **Normalize Audio Levels** sur des clips : modes Sample Peak, True Peak et normes de loudness. « Set Level » vaut Relative (le niveau le plus haut sert de référence) ou Independent (chaque clip est traité seul). La cible par défaut est -9 dBFS en crête. Le guide insiste : la normalisation ne « règle » pas le mixage. [DOC OFFICIELLE] BG20 leçon 3
- **Normalisation au rendu** (page Deliver > Audio > Normalize Audio > Optimize to Standard) : ITU-R BS.1770-4 (cible de crête et de loudness réglables), ATSC A/85, EBU R128, OP-59, TR-B32, AGCOM 219, et des préréglages Netflix, YouTube et Disney. Le préréglage YouTube impose -14 LKFS et -1 dBTP. L'option **Output Track** permet de rendre des pistes précises ou toutes les pistes, ce qui sert de base pour les stems. [DOC OFFICIELLE] BG20 leçon 10
- **Loudness History** : le graphe du bus principal suit la norme choisie pour le compteur (échelle et cible). Si « Lock Metering to Transport » est actif, déplacer la tête de lecture remet la mesure à zéro. [SOURCE SECONDAIRE] FBM-LH (modérateur), DRC
- **AI Dialogue Leveler** : un Track FX dans le mixeur, avec des modes comme « Optimize moderate levels », souvent suivi d'un Ducker. Repère du guide pour le dialogue : entre -18 et -9 dBFS au mixeur, autour de -12 dBFS en moyenne. [DOC OFFICIELLE] BG20 leçon 8
- **Voice Isolation** et **Dialog Leveler** peuvent être activés pendant l'enregistrement de voix off (outil Record de la 20). L'**AI Audio Assistant** (Studio) range les pistes, nivelle le dialogue, applique Voice Isolation et de-essing, fait le ducking et règle le mastering selon une norme de livraison (Timeline > AI Tools > Audio Assistant > Auto Mix). [DOC OFFICIELLE] NF20
- **Export de stems** : le flux exact (une sortie par bus, « Render as individual tracks ») n'a pas été lu dans le guide Fairlight 20, qui n'a pas été trouvé en PDF. [INCERTAIN]

## 6. Fairlight par script : ce qui existe et ce qui manque
- Ce qui existe [DOC OFFICIELLE] R26/CL/PYI :
  `Timeline.GetVoiceIsolationState(trackIndex)` / `SetVoiceIsolationState(trackIndex, {isEnabled, amount 0-100})` (20.1). Au niveau du clip, le CHANGELOG nomme `TimelineItem.GetVoiceIsolationState` et `TimelineItem.EnableVoiceIsolationState(...)`.
  `Resolve.GetFairlightPresets()`, `Project.ApplyFairlightPresetToCurrentTimeline(name)` (20.2.2) ; `Project.InsertAudioToCurrentTrackAtPlayhead(...)` (page Fairlight).
  `Timeline.AddTrack("audio", {audioType, index})`, `GetTrackSubType`, `Get/SetTrackName`.
  En 21.1 : `Timeline.GetNormalizeAudioModes()` et `NormalizeAudioLevel(items, {normalizationMode, targetLevel dBFS, targetLoudness LKFS, setLevelMode})`, avec les constantes `resolve.NORMALIZE_AUDIO_SET_LEVEL_RELATIVE` / `_INDEPENDENT`. Le mode par défaut est « Sample Peak Program ».
  `SetRenderSettings` connaît les clés `ExportAudio`, `AudioCodec`, `AudioBitDepth`, `AudioSampleRate` ; la 21.1 ajoute `GetAudioRenderCodecs` / `GetAudioRenderFormats`.
- Ce que le README ne mentionne pas : il n'y a pas de clé de normalisation de loudness au rendu dans `SetRenderSettings`, pas de lecture du compteur de loudness ou de la Loudness History, pas de routage de bus, pas de réglage de fader, d'EQ ou de plugin, ni d'Output Track pour les stems. [DOC OFFICIELLE par absence dans R26] Le contournement serait un préréglage de rendu ou un préréglage Fairlight préparé à la main, puis appliqué par script. [INCERTAIN, à tester]

## 7. Fusion ou After Effects : quand un monteur choisit Fusion
- Fusion fait mieux : il est intégré à la timeline, donc pas d'export ni de réimport, pas de problème de codec ni de disque gaspillé. Il est gratuit. Ses nodes rendent le flux lisible et partageable, et il est fort en compositing 3D et en VFX plan par plan (keying, tracking, Magic Mask, Deep). [SOURCE SECONDAIRE] PVC18 (2018, ancien), PB
- Fusion fait moins bien : c'est d'abord un compositeur « un plan à la fois », alors qu'AE gère des projets de dizaines de plans. L'écosystème de plugins (OFX) est plus petit et il y a beaucoup moins de formation et de templates. La courbe d'apprentissage des nodes est raide pour qui pense en calques. AE reste devant pour le motion design et la typographie animée. [SOURCE SECONDAIRE] PVC18, PB
- En pratique : on reste dans Fusion pour l'incrustation, la retouche, le stabilisé, le suivi d'un logo ou un titre maison sauvegardé en macro Edit/Titles. On passe dans AE pour de l'habillage typographique, des templates Mogrt ou des plugins propres à AE. MultiText (20) réduit un peu l'écart pour les titres. [SOURCE SECONDAIRE] synthèse ; l'apport de MultiText s'appuie sur NF20

## 8. À tester en phase 2 dans un vrai Resolve (20.x ou 21.x)
1. `item.GetFusionCompByIndex(1)` puis `comp.AddTool("Merge", -32768, -32768)`, `ConnectInput`, `SetInput` en Python : vérifier que les signatures de FSG8 fonctionnent toujours, et relever le RegID de Text+, MediaIn et MediaOut avec `GetAttrs()`.
2. Comparer les valeurs de pixel d'un MediaIn avec RCM ou ACES et sans (linéaire ou non) ; repérer le réglage de LUT du viewer.
3. Créer une macro, l'enregistrer dans `Templates/Edit/Titles` et l'insérer avec `InsertFusionTitleIntoTimeline(nom)`.
4. Appeler `NormalizeAudioLevel` (21.1) avec une cible en LKFS, puis mesurer le résultat au compteur ; comparer avec Deliver > Normalize Audio.
5. Chercher un moyen scripté de rendre des stems : préréglage de rendu avec Output Track, puis `LoadRenderPreset`.
6. Vérifier `SetVoiceIsolationState` (piste) et `EnableVoiceIsolationState` (clip) sur la version gratuite et sur Studio.
