Annexe de `SKILL.md` : décliner un montage Resolve dans un autre format (9:16 → 16:9, 16:9 → 9:16, 1:1, 4:5), par le MCP. Fusion, le 2026-10-29, du skill `resolve-adaptation-format` du cabinet (premier test réel : une pub 9:16 déclinée en 16:9 dans Resolve Studio 21.1), noms de marque et de client retirés. Leçon validée par Diego, `LECONS-A-REMONTER.md`. Les règles de genre (déclinaison verticale) sont dans `montage-formats` ; les sous-titres du studio aussi.

# Décliner un montage dans un autre format [TESTÉ EN CONDITIONS RÉELLES (2026-10)]

Le but : une déclinaison aboutie, pas une conversion technique. Chaque plan cadré comme un monteur l'aurait fait, les compositions repensées pour le nouveau format, et ce qui ne s'adapte pas signalé clairement.

## Principes
1. **Ne jamais toucher l'original** : `Timeline.DuplicateTimeline(nom)` (vérifier qu'aucune timeline ne porte déjà ce nom), puis travailler sur la copie seulement.
2. **Vérifier sur une image, jamais supposer** : les unités de position, de zoom et de recadrage changent selon le mode de mise à l'échelle, le zoom et le type de média (calibration ci-dessous).
3. **Rendus de contrôle légers**, supprimés après vérification, jobs retirés de la file ; rien écrit dans les dossiers du projet ou des rushes.
4. **Dire les limites tout de suite**, avec le contournement.

## Méthode
1. **État des lieux** (lecture seule) : timelines, réglages de la timeline source (résolution, cadence, `timelineInputResMismatchBehavior`) ; chaque piste vidéo (début, fin, résolution source, zoom, pan, tilt, crop, Fusion, clips désactivés) ; logos, packshots, transitions Fusion, clips d'ajustement, pistes de sous-titres ; **compositions multi-plans** (écrans partagés, triptyques : plans recadrés et décalés qui se chevauchent sur plusieurs pistes).
2. **Dupliquer et changer de format** : `SetSettings` avec `useCustomSettings` « 1 », résolution de timeline et de sortie ; remplissage `timelineInputResMismatchBehavior = "scaleToCrop"` (autres valeurs : `scaleToFit`, `centerCrop`, `stretch` ; `scaleToFill` n'existe pas). Resolve recalcule lui-même pan, tilt et crop : les relire, ils ne valent plus rien tels quels.
3. **Recadrer plan par plan** (Smart Reframe ne fait rien par script) :
   - exporter de Resolve une image du milieu de chaque plan, plan entier visible : timeline en `scaleToFit` le temps de l'export, tilt à 0, seule la piste du plan active ;
   - planches contact avec une grille tous les 10 % (`labo/outils/planche_contact.sh`), choisir le centre de la fenêtre en fraction de la source ;
   - **visages** : yeux vers le tiers haut, un peu d'air au-dessus de la tête (au premier test, remonter la fenêtre d'environ 2 % de plus que le premier choix) ; **produit** : centrer sur le produit, pas sur la main ; **ambiance** : garder l'action, pas de plafond ni de sol vides ;
   - revenir à `scaleToCrop`, restaurer l'état des pistes, contrôler par un rendu léger complet, corriger les plans ratés.
4. **Écrans partagés** : repenser la mise en page. En 9:16 → 16:9, des bandes empilées deviennent des colonnes côte à côte d'un tiers de largeur exactement, sans bordure ; la première bande apparue va à gauche. Crops à 0, position par zoom et pan ; vérifier sur image ni bordure ni chevauchement.
5. **Logo, packshot** : logo replacé selon les conventions du format (par exemple en haut à droite, environ 10 % de la largeur, marges de 120 à 150 px en UHD), calé par itération (un still n'a pas les unités d'une vidéo). Packshot ou carton de marque : gardé s'il passe (logo centré sur fond uni), sinon demander la version officielle du client dans le bon format. Les clips désactivés dans l'original le restent.
6. **Sous-titres** : l'API ne modifie ni le texte ni le style d'une piste de sous-titres. Deux voies : SRT corrigé réimporté (recettes, « Sous-titres ») ou conversion en Text+ (ci-dessous). Règles de découpe du studio : `montage-formats`. Ancienne piste **désactivée, pas supprimée** ; rappeler de ne pas les incruster à l'export.
7. **Compte rendu** : ce qui a été fait ; **ce qui ne s'adapte pas ou reste à vérifier** (définition : un 16:9 recadré dans un 9:16 UHD donne environ 1 215 lignes, livrer en 1080p ; packshots à remplacer ; plans graphiques trop serrés ; textes reformulés) ; ce qui est resté intact ; ce que l'API ne permet pas, avec le contournement.

## Calibrer les unités (à refaire à chaque nouveau cas)
Poser une valeur test (tilt 0, −400, −800), exporter une image à chaque fois, mesurer le déplacement réel en pixels, en tirer le facteur, l'appliquer aux plans du même type, contrôler. Mesures d'un cas (sources 2160x3840 dans une timeline 3840x2160 en `scaleToCrop`), des indices, pas des lois :
- changer la résolution recalcule pan, tilt et crop proportionnellement ; changer le mode de mise à l'échelle recalcule encore les crops (×1,78 ici) ;
- **tilt**, vidéo 9:16, zoom 1 : 1 unité ≈ 3,16 px (le carré de 16/9) ; `Tilt = (c − 0,5) × hauteur_timeline` (c = centre voulu de la fenêtre dans la source, 0 en haut) ; limite environ ±738 en UHD ; tilt positif monte l'image, pan positif la décale à droite ;
- **pan à zoom 1/3** (colonnes de triptyque) : 1 unité ≈ 1 px ; trois colonnes de 1 280 px en UHD : pan −1280 / 0 / +1280 (±1215 laissait 64 px de noir de chaque côté) ;
- **still (logo PNG)** : pan ≈ 3,16 px par unité ; zoom d'une autre logique (0,031 ≈ 380 px de large pour un PNG 1663x294) ;
- `GetIsTrackEnabled` n'est fiable que sur la timeline courante ; une timeline créée par `CreateEmptyTimeline` prend la cadence par défaut du projet : régler `useCustomSettings` et `timelineFrameRate` avant d'y poser quoi que ce soit ;
- **export d'images** : `SetCurrentTimecode` sur l'image précédente puis sur l'image visée, pause de 0,5 à 0,8 s, puis `ExportCurrentFrameAsStill` (pas d'alpha). Ici il a marché depuis la page Color ; sur les projets de 2026-10-11, la page Color exportait l'image d'avant : se fier à l'image, pas à la page ;
- les sous-titres ne se voient pas dans une image exportée : rendu avec `ExportSubtitle: True`, `SubtitleFormat: "BurnIn"` ;
- `InsertFusionTitleIntoTimeline` écrit toujours sur V1, en écrasement, 125 images (5 s à 25 i/s) ; verrouiller les autres pistes le fait échouer. Pas de fonction pour régler la durée d'un clip : un titre « bouche-trou » inséré à l'image de fin écrase la queue du précédent, puis on le supprime. **Seulement dans une timeline dédiée** (`SKILL.md` § 2) ;
- les réglages de la page Deliver changés par script restent dans le projet : le dire au monteur.

## Sous-titres en Text+ (timeline imbriquée)
On lit les sous-titres (`GetItemListInTrack("subtitle", 1)`, `GetName()`, `GetStart()`, `GetEnd()`) et on les reconstruit en Text+ dans une timeline dédiée, imbriquée ensuite.
1. Regrouper selon les règles du studio, écrire la liste `(début, fin, texte)` dans un fichier, la relire à froid.
2. Timeline `ST <format>` : `CreateEmptyTimeline`, puis aussitôt `useCustomSettings` « 1 », même cadence et même résolution que le montage, même timecode de départ.
3. Par lots d'environ 12 (sous la limite de 60 s par appel) : tête de lecture au début, `InsertFusionTitleIntoTimeline("Text+")`, texte et style, `SetName` (début de la phrase), noter `GetUniqueId()` ; tête de lecture à la fin, Text+ bouche-trou. Liste des ID dans un JSON entre les appels.
4. Supprimer tout clip dont l'ID n'est pas dans la liste (`DeleteClips(items, False)`) ; contrôler début et fin de chaque clip.
5. Imbriquer : `AppendToTimeline([{"mediaPoolItem": st.GetMediaPoolItem(), "startFrame": 0, "endFrame": duree, "trackIndex": <piste vide>, "recordFrame": debut, "mediaType": 1}])`, renommer la piste (`SetTrackName`) ; la transparence est gardée.
6. `SetTrackEnable("subtitle", 1, False)` sur l'ancienne piste ; rendu léger, une image au milieu de chaque sous-titre, surtout sur fond clair.
Style validé en UHD 16:9 : `Font` « Helvetica Neue », `Style` « Medium », `Size` 0,036, `HorizontalJustificationNew` 1, `VerticalJustificationNew` 3, `Center` (0,5 ; 0,07), ombre `Enabled3` 1, noir, `Alpha3` 0,75, `Softness3` 3, `Offset3` (0,002 ; −0,003). À dire au monteur : où modifier (timeline `ST …`, clips nommés par le début de phrase), l'export SRT natif perdu (garder l'ancienne piste à jour à part si le client en veut un), les passages reformulés à relire. Au-delà d'environ 1 000 Text+ posés dans une session, Resolve ralentit : `SKILL.md` § 2.

## Rendu de contrôle léger
`SetCurrentRenderFormatAndCodec("mp4", "H264")`, puis `SetRenderSettings({"SelectAllFrames": True, "TargetDir": <dossier temporaire>, "CustomName": "check", "ExportVideo": True, "ExportAudio": False, "FormatWidth": 960, "FormatHeight": 540, "VideoQuality": 1500, "MultiPassEncode": False, "ExportSubtitle": False})`, `AddRenderJob`, `StartRendering([jid])`, attendre avec `IsRenderingInProgress()` par boucles de moins de 60 s, puis `DeleteRenderJob(jid)` et le fichier. 93 s de montage : environ 17 Mo, 50 s de rendu. Planche à 1 image/s ou une image au milieu de chaque plan.
