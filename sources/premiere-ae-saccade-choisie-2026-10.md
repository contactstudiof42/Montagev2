# Saccade choisie (step-printing) dans Premiere Pro et After Effects

> BACKLOG 86 [TECH]. Recherche faite le 2026-10-10, pour Premiere Pro et After Effects 2026 (Premiere 26.x).
> **Tout ce document est [THÉORIQUE]** : rien n'a été testé dans les logiciels.
> Limite de la méthode : helpx.adobe.com renvoie une erreur 403 aux outils de lecture. Le contenu Adobe vient donc des extraits indexés par le moteur de recherche (pages helpx citées), puis il a été recoupé avec des forums et des pros (Adobe Community, ProVideo Coalition, Creative COW).
> Libellés : interface **anglaise**.

## 0. Définitions et usage artistique

- **Saccade régulière** (posterize, cadence fixe à 8, 12 ou 15 i/s) : c'est une *texture*. On l'applique à tout un plan ou une séquence, avec un effet stop-motion ou « undercrank ». C'est rapide, cohérent et sans décision image par image.
- **Saccade choisie** (step-printing à la Wong Kar-wai, *Chungking Express*, *Fallen Angels*) : c'est du *montage image par image*. Le monteur décide quelles images source tiennent et combien de temps. Le rythme peut s'accélérer et ralentir à l'intérieur du plan, souvent sur un sujet net dans une foule traînante. Sur le tournage d'origine, c'était de l'undercrank (environ 8 à 12 i/s) avec les images dupliquées au tirage, plus un obturateur ouvert qui donne la traînée ([cinematography.net](https://cinematography.net/edited-pages/StepPrinting-ExamplesInformation.htm), [indepthcine](https://indepthcine.com/videos/chungking-express)). Les cadences citées divergent selon les sources, donc il faut les traiter comme des ordres de grandeur.
- La traînée (le flou de mouvement long) fait partie du look. Une saccade *nette* sans traînée se lit plutôt « stop-motion / vidéo saccadée ».

## 1. Premiere Pro 2026

### 1.1 Frame Hold [THÉORIQUE]
- **Add Frame Hold** (clic droit sur le clip, ou menu Clip > Video Options) : coupe à la tête de lecture et fige tout le reste du clip sur cette image.
- **Insert Frame Hold Segment** (même menu) : coupe en 3 morceaux. Le morceau de gauche est normal, celui du milieu est figé (2 s par défaut selon les tutoriels) et celui de droite reprend la lecture ([softwarehow](https://www.softwarehow.com/?p=28408), [tourbox](https://www.tourboxtech.com/en/news/how-to-freeze-frame-in-premiere-pro.html)).
- **Frame Hold Options** (Clip > Video Options > Frame Hold Options) : fige le clip entier. Les paramètres sont la case **Hold On** avec le menu Source Timecode / Sequence Timecode / In Point / Out Point (une option Playhead apparaît aussi dans les versions récentes, à vérifier), et la case **Hold Filters**. Hold Filters fige aussi les effets animés ; sans elle, les effets continuent de s'animer sur l'image figée ([helpx Freeze frame](https://helpx.adobe.com/premiere-pro/using/freeze-frame.html), [KEM forum](https://forum.knightsoftheeditingtable.com/d/274-frame-hold-options)). Avec In Point ou Out Point, l'image figée suit le point d'entrée ou de sortie si on le trime.
- **Usage saccade choisie** : c'est la méthode la plus directe en montage. Pour chaque « tenue », on coupe (C, ou Ctrl/Cmd+K) puis on règle le segment avec **Frame Hold Options > Hold On : In Point**. Ensuite on trime chaque segment à 2, 3 ou 4 images. Chaque segment correspond à une image source choisie, et la timeline devient la partition.
- **Pièges** :
  - Un bug signale qu'Add Frame Hold ne fonctionnait plus après une mise à jour 2026 ([community 1547100](https://community.adobe.com/bug-reports-728/add-frame-hold-on-premiere-pro-2026-does-not-work-1547100)).
  - Un autre signale une image tenue différente de celle visée ([community 15133105](https://community.adobe.com/t5/premiere-pro-discussions/frame-hold-displays-wrong-frame/m-p/15133105/highlight/true)). Le conseil donné est de placer la tête de lecture sans pré-couper.
  - Des dizaines de micro-segments alourdissent la timeline. Il vaut mieux les imbriquer (nest) une fois validés.

### 1.2 Time Remapping avec paliers [THÉORIQUE]
- Clic droit sur l'icône fx du clip > **Time Remapping > Speed** (ou **Show Clip Keyframes**). On pose une clé de vitesse et on tire la bande à **0 %** pour obtenir un palier figé. Ctrl+Alt-glisser (Win) ou Opt+Cmd-glisser (Mac) sur la clé allonge le palier. On peut scinder une clé pour faire une rampe ([helpx freeze via Time Remapping](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/freeze-a-frame-for-a-portion-of-a-clip-using-time-remapping.html), [helpx Time Remapping](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/change-clip-speed-and-duration-using-time-remapping.html)).
- Adobe recommande Time Remapping, plutôt que Frame Hold, pour figer *une partie* d'un clip.
- **Piège** : les paliers sont faits pour des tenues longues. Pour des saccades de 2 à 4 images, l'édition à la souris est fastidieuse et imprécise, donc les coupes avec Frame Hold sont plus adaptées. Il faut aussi mettre les rampes en transition franche (pas de lissage de courbe), sinon le palier devient un ralenti.

### 1.3 Time Interpolation [THÉORIQUE]
- Clic droit sur le clip > **Time Interpolation** (aussi dans Clip > Video Options) : **Frame Sampling** (réglage par défaut, répète ou saute des images), **Frame Blending** (répète puis fond les images voisines), **Optical Flow** (fabrique des images intermédiaires) ([community, extrait helpx](https://community.adobe.com/t5/premiere-pro-discussions/time-interpolation-frame-sampling-and-opitcal-flow-in-ppro-then-again-in-media-encoder/m-p/12073975/highlight/true)).
- **Pour la saccade, garder Frame Sampling.** Frame Blending et Optical Flow lissent ou interpolent, ce qui *annule* la saccade (ou crée des fondus et des artefacts « morphing »). Le même réglage existe à l'export (Time Interpolation dans Export Settings) et s'applique à toute la séquence : il faut vérifier qu'il n'y réintroduit pas d'Optical Flow.

### 1.4 Effet Posterize Time (oui, il existe dans Premiere) [THÉORIQUE]
- Il se trouve dans Effects > Video Effects > **Time > Posterize Time**, avec un seul paramètre, **Frame Rate**. Il verrouille le clip à une cadence (l'exemple d'Adobe est 60 champs ramenés à 24 i/s). L'animation de Frame Rate n'accepte que l'interpolation **Hold**, et Adobe prévient que l'animer peut donner des résultats imprévisibles ([helpx Time effects Premiere](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/time-effects.html)).
- La liste des changements de Premiere 26.0 garde Posterize Time dans Time et classe **Echo en « Obsolete »** ([helpx liste 26.0](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/list-of-effects-and-transitions.html)). Pour la traînée, Echo est donc à éviter dans Premiere 2026 : il faut passer par After Effects ou par un autre effet.
- **Usage** : c'est la saccade *régulière* (texture). Des clés Hold sur Frame Rate (par ex. 12, puis 6, puis 24) donnent une saccade « semi-choisie » par zones, mais pas le choix image par image.

### 1.5 Comportement selon la cadence de séquence [THÉORIQUE, raisonnement arithmétique]
- Une tenue dure toujours un nombre entier d'images de *séquence*. À 24 ou 23,976 i/s, 12 i/s donne un motif 2-2-2 exact et 8 i/s donne 3-3-3. À 25 i/s, 12 i/s ne tombe pas juste : le motif devient irrégulier (2-2-2-…-3), ce qui peut être voulu, mais il faut le savoir. À 25, il vaut mieux viser 12,5, 8,33 ou 6,25.
- En 50/60 i/s, la saccade choisie offre plus de finesse (des tenues de 1/60 s), mais l'effet « film » se perd. Pour le look WKW, une séquence à 24 ou 25 est préférable.
- Côté After Effects, le bug Posterize Time sur les compositions à 23,976 (valeur arrondie dans l'interface, timing faux) est signalé jusqu'en 2025 ([community bug 1215887](https://community.adobe.com/bug-reports-528/issues-with-posterize-time-effect-when-using-a-frame-rate-of-23-976-1215887)). Le même risque est à vérifier dans Premiere.

## 2. After Effects 2026

### 2.1 Effet Posterize Time [THÉORIQUE]
- Il se trouve dans Effect > **Time > Posterize Time**, avec le paramètre **Frame Rate** (animation en Hold uniquement). Il fonctionne en 8, 16 et 32 bpc ([helpx Time effects AE](https://helpx.adobe.com/after-effects/using/time-effects.html)).
- Adobe propose une alternative plus efficace : précomposer, puis régler la cadence de la précomp dans Composition Settings. Il faut alors activer *Preserve frame rate when nested or in render queue* (Composition Settings > Advanced), libellé à vérifier.
- **Pièges** :
  - Désynchronisation (« time slip ») sur des précomps imbriquées ou sous un calque d'effets ([community 14809050](https://community.adobe.com/t5/after-effects-discussions/posterize-time-effect-breaking-the-integrity-of-a-pre-comp-causing-layers-to-quot-time-slip-quot/td-p/14809050)).
  - Collapse Transformations contourne Posterize Time et Preserve Framerate, d'après un ingénieur Adobe dans le même fil.
  - Mauvais comportement à 23,976 (voir 1.5).

### 2.2 Expression posterizeTime() [THÉORIQUE]
- Signature : `posterizeTime(updatesPerSecond)`. Elle fait évaluer la *propriété qui porte l'expression* moins souvent que la cadence de la comp ([docsforadobe, Global](https://ae-expressions.docsforadobe.dev/general/global/), [helpx Expression language](https://helpx.adobe.com/after-effects/using/expression-language-reference.html)). `posterizeTime(0)` fige la valeur à t=0 (depuis AE 16.0, d'après une citation sur [Creative COW](https://creativecow.net/?p=2429283)).
- **Piège principal** : la fonction n'agit que sur l'expression où elle est écrite. Les autres propriétés et la vidéo source continuent à la cadence de la comp. Pour saccader *l'image*, il faut l'écrire sur **Time Remap**. L'ingénieur Adobe le suggère : activer Time Remap sur la précomp puis écrire `posterizeTime(8); value;`, ce qui préserve aussi les modes de fusion ([même fil](https://community.adobe.com/t5/after-effects-discussions/posterize-time-effect-breaking-the-integrity-of-a-pre-comp-causing-layers-to-quot-time-slip-quot/m-p/14810001/highlight/true)).
- Autre bug : avec `posterizeTime(0)` et `sampleImage()`, l'interface affiche une valeur fausse alors que le rendu est correct ([bug 1216185](https://community.adobe.com/bug-reports-528/ui-fails-to-display-correct-values-for-expressions-combining-posterizetime-0-and-sampleimage-1216185)).

Expressions proposées, à coller sur **Time Remap** :

```js
// A. Saccade reguliere (texture) : 8 images/s
posterizeTime(8);
value;
```
```js
// B. Saccade choisie : une entree = l'image source affichee a chaque image de comp
var holds = [0,0,0,5,5,9,9,9,9,14,15,15,22]; // edite a la main (partition)
var f = timeToFrames(time);
framesToTime(holds[Math.min(f, holds.length - 1)]);
```
**Vérification** : seule la *syntaxe JavaScript* a été vérifiée, avec `node --check` et une exécution sous Node v22.22.0 où `posterizeTime`, `timeToFrames` et `framesToTime` sont simulés par des fonctions maison. Ni le moteur d'expressions d'AE ni le rendu n'ont été vérifiés. Avec le mock, A donne une sortie 0 / 0,125 / 0,25 s par paliers de 3 images (comp à 24 i/s), et B suit la liste comme prévu.

### 2.3 Time Remap avec clés Hold [THÉORIQUE]
- **Layer > Time > Enable Time Remapping** (Ctrl+Alt+T / Cmd+Opt+T). Des clés se créent au début et à la fin du calque. Pour chaque image choisie : poser une clé de Time Remap avec la valeur de l'image source voulue, puis passer la clé en Hold (clic droit > **Toggle Hold Keyframe**, ou Ctrl+Alt+H / Cmd+Opt+H, raccourci à vérifier). **Layer > Time > Freeze Frame** crée directement une clé Hold. Hold ne s'applique qu'à l'interpolation *sortante* ([helpx Time-stretching/remapping](https://helpx.adobe.com/after-effects/using/time-stretching-time-remapping.html)).
- C'est l'équivalent le plus fidèle du step-printing manuel : chaque clé Hold correspond à une image choisie, et l'écart entre les clés fixe la durée de la tenue. L'expression B ci-dessus fait la même chose sous forme de tableau.
- **Pièges** : une clé laissée en Linear crée un ralenti au lieu d'une tenue. Le motion blur du calque appliqué à un calque time-remappé dépend du Shutter Angle de la comp et de Collapse Transformations ([community motion blur/remap](https://community.adobe.com/t5/after-effects-discussions/time-remapping-changes-motion-blur/m-p/13644664)).

### 2.4 Frame Blending [THÉORIQUE]
- Il y a un interrupteur par calque (colonne Switches, icône pellicule) : **Frame Mix** (barre oblique inverse, fondu des images voisines, rapide) ou **Pixel Motion** (barre oblique, flux optique, meilleur et plus lent). L'interrupteur de comp **Enable Frame Blending** doit être actif pour que l'effet compte (menu Layer > Frame Blending) ([helpx](https://helpx.adobe.com/after-effects/using/time-stretching-time-remapping.html)).
- **Piège principal** : activer Frame Blending sur un calque saccadé fond les tenues entre elles et *annule* la saccade. Il faut le laisser **Off** sur le calque time-remappé. Exception artistique : Frame Mix sur une version dupliquée, mise en dessous, peut servir de traînée douce.

### 2.5 Traînée : CC Wide Time et Echo [THÉORIQUE]
- **Echo** (Effect > Time > Echo) : **Echo Time (seconds)**, avec une valeur négative pour les images passées ; **Number Of Echoes** ; **Starting Intensity** ; **Decay** ; **Echo Operator** (Add, Maximum, Minimum, Screen, Composite In Back/Front, Blend). Il ne fonctionne que si le *contenu* du calque bouge. Un calque fixe animé en position doit d'abord être précomposé. En mode Add, l'image sature vite vers le blanc ([helpx Time effects AE](https://helpx.adobe.com/after-effects/using/time-effects.html), [photofocus](https://photofocus.com/software/animate-your-motion-in-after-effects-with-the-echo-effect/)).
- **CC Wide Time** (Effect > Time, effet tiers fourni avec AE, listé par Adobe) : paramètres **Forward Steps**, **Backward Steps** et **Native Motion Blur**. Ces noms n'ont pas pu être confirmés par une source en ligne pendant cette recherche : il faut les vérifier dans l'interface.
- **Ordre conseillé** : la saccade (Time Remap) vient d'abord, la traînée ensuite. Il faut appliquer Echo ou Wide Time sur un calque ou une précomp *au-dessus* de la saccade, sinon la traînée lisse les tenues. Pour le look WKW, une traînée sur les images *passées* (valeurs négatives ou Backward Steps) pendant la tenue imite l'obturateur lent.

## 3. Choisir la méthode (résumé)

| Besoin | Premiere | After Effects |
|---|---|---|
| Texture régulière | Posterize Time (Frame Rate) | Posterize Time, cadence de précomp ou `posterizeTime(n)` sur Time Remap |
| Saccade choisie | Coupes + Frame Hold Options (Hold On : In Point), segments trimés | Clés Hold de Time Remap, ou expression-tableau (B) |
| Traînée | Echo obsolète en 26.0 : passer par AE | Echo, CC Wide Time, au-dessus de la saccade |
| À couper | Time Interpolation ≠ Frame Sampling | Frame Blending (Frame Mix / Pixel Motion) |

## 4. Tests phase 2 (dans le vrai logiciel)

1. **Premiere** : séquence 25 i/s et séquence 24 i/s, même clip, Posterize Time à 12. Exporter et compter les images répétées dans chaque cas, pour vérifier le motif 2-2-…-3 attendu à 25.
2. **Premiere** : saccade choisie de 3 s avec coupes + Frame Hold Options (Hold On : In Point, Hold Filters on/off). Trimer un point d'entrée et vérifier que l'image tenue suit, puis exporter avec Time Interpolation de séquence en Optical Flow, pour vérifier si la saccade survit.
3. **AE** : comparer l'expression A, l'effet Posterize Time et la cadence de précomp (avec et sans Preserve frame rate) sur une précomp imbriquée, pour détecter un décalage de synchronisation ou un problème avec Collapse Transformations.
4. **AE** : coller l'expression B sur Time Remap, vérifier que la liste est respectée image par image (Info panel ou export PNG séquence), puis activer Frame Blending (Frame Mix puis Pixel Motion) pour constater l'annulation.
5. **AE** : relever les noms exacts des paramètres de CC Wide Time et l'interaction de Native Motion Blur avec l'interrupteur Motion Blur, et comparer avec Echo (Echo Time négatif) posé au-dessus de la saccade.
