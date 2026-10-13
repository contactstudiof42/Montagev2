# Expressions After Effects

## Durées types à 25 i/s (points de départ, à juger à l'œil)

| Usage | Durée | Remarque |
|---|---|---|
| Micro-interaction UI (bouton, toggle) | 4 à 8 i (160 à 320 ms) | Au-delà, l'UI paraît lente |
| Apparition d'un panneau / carte UI | 8 à 12 i | Sortie plus courte que l'entrée (≈ 70 %) |
| Lettre par lettre (décalage entre lettres) | 1 à 2 i | 3 i et plus : effet « machine à écrire » |
| Entrée d'un mot ou d'une ligne de titre | 10 à 18 i | Décaler les lignes de 3 à 5 i |
| Lower third (entrée) | 12 à 20 i, tenue ≥ 3 s | La tenue doit permettre deux lectures du nom |
| Révélation de logo | 30 à 75 i (1,2 à 3 s) | Plus le logo est « premium », plus l'arrivée est longue et sans overshoot |
| Anticipation | 2 à 4 i | Rarement plus de 15 % de l'amplitude |
| Overshoot / rebond qui se pose | 8 à 20 i | Au-delà, ça devient du cartoon |
| Transition plein cadre | 8 à 16 i | Sur le temps fort de la musique |

Ces chiffres sont des **conventions de métier**, pas des normes. Pour l'UI, ils rejoignent les guides de motion des systèmes de design (100 à 500 ms).

## 4. Recettes

Code complet et commentaires : [expressions.md](expressions.md). Fichiers : `labo/ae-expressions/NN-*.js`.

| # | Recette | Usage motion | Statut |
|---|---|---|---|
| 01 | `wiggle(freq, amp)` piloté par deux sliders | Caméra à l'épaule, tremblement, flottement | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** (bornes vérifiées avec un faux wiggle) |
| 02 | `loopOut("cycle")` | Boucle de fond, rotation infinie, GIF | **[TESTÉ EN LABO, syntaxe uniquement]** (le comportement testé est celui du mock) |
| 03 | `loopOut("pingpong")` | Balancier, respiration simple | **[TESTÉ EN LABO, syntaxe uniquement]** |
| 04 | Boucle manuelle `valueAtTime(t0 + (time - t1) % d)` | Boucler une portion choisie | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 05 | Overshoot inertiel (principe Dan Ebberts) | Arrivée élastique sur n'importe quelle propriété | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** : pic à 107 pour une cible de 100, posé en 3 s |
| 06 | Écho / suiveur `valueAtTime(time - retard)` | Traînées, cascades, essaims | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 07 | `ease(p, 20, 60, 0, 100)` | Piloter une propriété par une autre (« progression ») | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** (courbe exacte d'`ease` non reproduite) |
| 08 | Time remap à vitesse constante | Ralenti/accéléré propre d'un clip | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 09 | Compteur de texte avec séparateur de milliers | Chiffres clés, data, infographie | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 10 | `posterizeTime(8)` + wiggle | Effet stop motion, image par image dessinée | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 11 | Rig respiration asymétrique (inspiration/rétention/expiration/pause) | Logo vivant, attente, ambiance | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 12 | Rebond avec gravité (bounce back, Ebberts) | Objet qui tombe et rebondit | **[THÉORIQUE]** |
| 13 | `loopOut("offset")` / `("continue")` | Escalier qui monte, mouvement qui continue sur sa lancée | **[THÉORIQUE]** |
| 14 | Animateur de texte + sélecteur de plage « Expression » | Décalage lettre par lettre piloté | **[THÉORIQUE]** |

### Réglages qui comptent

- **Overshoot (05)** : `freq` règle la raideur, `decay` la rapidité de stabilisation. L'amplitude n'est pas un réglage : elle vient de **la vitesse d'arrivée** (vitesse ÷ 2π·freq). Pour plus de rebond, on arrive plus vite ou on baisse `freq`. Les clés doivent arriver **avec de la vitesse** (sortie linéaire ou peu amortie) : une clé en Easy Ease arrive à vitesse nulle, donc il n'y a pas d'overshoot.
- **Wiggle (01)** : fréquence 0,5 à 2 pour un flottement, 3 à 8 pour une caméra à l'épaule, au-delà c'est une vibration. Amplitude caméra : 2 à 8 px en HD. Sur une seule dimension : séparer les dimensions, ou ne garder qu'un axe du résultat.
- **pingpong (03)** : au retour, l'easing est inversé. Une arrivée longue devient un départ long. Si l'asymétrie compte, faire un cycle complet et utiliser `cycle`.
- **cycle (02)** : la dernière clé doit avoir la même valeur que la première, avec des tangentes compatibles, sinon un « hoquet » apparaît à chaque tour.

- **Saccade (step-printing)** : régulière = `posterizeTime(8);` sur le Time Remap d'une précomp [THÉORIQUE] ; **choisie** = Time Remap en clés maintenues (Hold) sur les images voulues, Frame Blending coupé. La saccade régulière laisse le hasard choisir les images et rate le coup de lumière [ÉPROUVÉ EN MAQUETTE] (pièce 20 v1). Recette tableau, pièges et traînée : [expressions.md](expressions.md#saccade).

## Pièges (résumé de l'ancien SKILL.md ; détail plus bas)

- **Moteur** : écrire pour le moteur JavaScript (accolades, points-virgules, `thisLayer`, `thisComp`) et fixer le moteur dans le cahier des charges ; un poste en ExtendScript hérité affiche des erreurs en série.
- **Expressions lentes** (`sampleImage`, `valueAtTime` en boucle, échos sur 50 calques) : convertir en images clés une fois figé, `posterizeTime` pour ce qui n'a pas besoin de 25 i/s.
- **Vitesse d'arrivée nulle = pas d'overshoot** : cause n° 1 de « mon expression ne fait rien ». `exp()` explose sans coupure (`t < 3`).
- **Bézier spatial non voulu** : le calque boucle ou dépasse dans l'espace ; Interpolation spatiale > Linéaire.
- **Overshoot trop rapide** (freq > 6) : tombe entre les images à 25 i/s ; juger à 25, pas à 50.
- **Période qui varie dans un `sin`** (ou `wiggle` à `freq` animée) : le geste hésite et repart au lieu de s'apaiser ; intégrer la phase [TESTÉ EN LABO] (sous Node, `labo/ae-expressions/bercement/test.js`).
- **Wiggle et duplication** : tirages différents d'un calque à l'autre ; `seedRandom()` pour figer (à vérifier en phase 3).

Annexe de `SKILL.md` : code complet des recettes, durées types, table des recettes et réglages, saccade, pièges (le SKILL.md fait foi). Durées, table et pièges déplacés du SKILL.md à l'audit 2 (2026-10-13).

Chaque bloc est copié depuis `labo/ae-expressions/`. Écrit pour le **moteur JavaScript** (par défaut depuis AE 16.0). Statut : **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** veut dire que le code a passé `node --check` et des évaluations dans `mock.js`, **pas** qu'il a tourné dans AE. Résultats : `labo/ae-expressions/RESULTATS.md`.

Rappel : dans AE on peut écrire `value + [10, 0]` ; le labo utilise `add(value, [10, 0])` et `mul(value, k)` (fonctions AE documentées) pour pouvoir tester sous Node. Les deux sont équivalents dans AE.

Mise en place des sliders : Effet > Paramètres pour expressions > Paramètre glissière, puis renommer (Entrée). Le nom dans l'expression doit être identique, accents compris.

## 01-wiggle-sliders  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Wiggle piloté par deux Sliders sur le calque (Effet > Paramètres pour expressions > Paramètre glissière).
// Renommer les sliders exactement "Fréquence" et "Amplitude".
// Fréquence en oscillations/seconde, Amplitude en unités de la propriété (px, degrés…).
var freq = effect("Fréquence")("Slider");
var amp = effect("Amplitude")("Slider");
wiggle(freq, amp);
```

## 02-loopout-cycle  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Boucle simple : rejoue de la 1re à la dernière clé, à l'infini.
// La dernière clé doit avoir la même valeur que la première, sinon saut visible.
loopOut("cycle");
```

## 03-loopout-pingpong  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Aller-retour : rejoue les clés à l'endroit puis à l'envers.
// Attention : l'easing de sortie devient l'easing d'entrée au retour (asymétrie inversée).
loopOut("pingpong");
```

## 04-boucle-manuelle  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Boucle "cycle" écrite à la main avec valueAtTime : utile pour comprendre,
// ou pour boucler seulement entre deux clés choisies (ici la 1re et la dernière).
var t0 = key(1).time;
var t1 = key(numKeys).time;
var d = t1 - t0;
(numKeys > 1 && time > t1) ? valueAtTime(t0 + ((time - t1) % d)) : value;
```

## 05-overshoot-inertiel  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Overshoot inertiel après la dernière clé atteinte (principe décrit par Dan Ebberts, motionscript.com,
// réécrit ici). Le calque arrive avec une vitesse, dépasse sa cible, oscille et se pose.
// Mettre des clés LINÉAIRES (ou une sortie peu amortie) : l'overshoot récupère la vitesse d'arrivée.
var freq = 2.5;   // oscillations par seconde : plus haut = matière plus rigide
var decay = 6;    // amortissement : plus haut = se pose plus vite
var n = 0;
if (numKeys > 0) {
  n = nearestKey(time).index;
  if (key(n).time > time) n--;          // on veut la dernière clé DÉJÀ passée
}
var t = (n > 0) ? time - key(n).time : 0;
if (n > 0 && n == numKeys && t < 3) {   // seulement après la dernière clé ; coupe à 3 s (évite exp() énorme)
  var vIn = velocityAtTime(key(n).time - thisComp.frameDuration / 10); // vitesse JUSTE AVANT la clé
  var w = 2 * Math.PI * freq;
  add(value, mul(vIn, Math.sin(t * w) / Math.exp(decay * t) / w));
} else {
  value;
}
```

## 06-echo-decalage  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Suiveur / écho : ce calque reprend la position du calque juste au-dessus avec un retard en images.
// Dupliquer le calque N fois : chaque copie suit la précédente -> traînée en cascade.
var retardImages = effect("Retard (images)")("Slider");
var leader = thisComp.layer(index - 1);
leader.transform.position.valueAtTime(time - retardImages * thisComp.frameDuration);
```

## 07-mapping-linear-ease  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Mapper une plage sur une autre. Ex. : opacité pilotée par un slider "Progression" 0..100,
// visible seulement entre 20 et 60 % de la progression, avec un fondu doux.
var p = effect("Progression")("Slider");
ease(p, 20, 60, 0, 100);
```

## 08-time-remap-vitesse  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Remappage temporel (Time Remap) piloté par un slider "Vitesse %" (100 = normal, 50 = ralenti x2).
// Vitesse CONSTANTE uniquement : si le slider est animé, ce calcul ne l'intègre pas (voir RESULTATS).
var v = effect("Vitesse %")("Slider") / 100;
clamp((time - inPoint) * v, 0, source.duration - thisComp.frameDuration);
```

## 09-compteur-texte  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Texte source : compteur 0 -> cible, avec ralenti à l'arrivée et séparateur de milliers français.
// Sliders : "Cible", "Début (s)", "Durée (s)".
var cible = effect("Cible")("Slider");
var t0 = effect("Début (s)")("Slider");
var d = effect("Durée (s)")("Slider");
var n = Math.round(easeOut(time, t0, t0 + d, 0, cible));
var s = String(Math.abs(n));
var out = "";
for (var i = 0; i < s.length; i++) {
  if (i > 0 && (s.length - i) % 3 === 0) out += " ";  // espace fine insécable
  out += s.charAt(i);
}
(n < 0 ? "-" : "") + out;
```

## 10-posterize-wiggle  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Tremblement "stop motion" : wiggle recalculé seulement 8 fois/seconde (tenues de 3 images à 24/25 i/s).
posterizeTime(8);
wiggle(3, 6);
```

## 11-respiration  [TESTÉ EN LABO, syntaxe/logique Node uniquement]

```js
// Respiration asymétrique sur l'Échelle : inspiration (montée) / rétention (tenue) / expiration (descente plus longue) / pause.
// Sliders en IMAGES : "Inspiration", "Rétention", "Expiration", "Pause" ; "Amplitude %" (ex. 4).
var f = thisComp.frameDuration;
var tIn = effect("Inspiration")("Slider") * f;
var tHold = effect("Rétention")("Slider") * f;
var tOut = effect("Expiration")("Slider") * f;
var tRest = effect("Pause")("Slider") * f;
var amp = effect("Amplitude %")("Slider") / 100;
var cycle = tIn + tHold + tOut + tRest;
var t = ((time - inPoint) % cycle + cycle) % cycle;
var k;
if (t < tIn) k = ease(t, 0, tIn, 0, 1);                                   // on gonfle, doux aux deux bouts
else if (t < tIn + tHold) k = 1;                                          // poumons pleins
else if (t < tIn + tHold + tOut) k = easeOut(t, tIn + tHold, tIn + tHold + tOut, 1, 0); // relâche vite puis se pose
else k = 0;                                                               // vide
mul(value, 1 + amp * k);
```

## 12-rebond-gravite  [THÉORIQUE]

Principe du « bounce back » de Dan Ebberts (motionscript.com), réécrit : après la dernière clé, l'objet repart dans le sens inverse avec sa vitesse d'arrivée × élasticité, retombe sous une gravité, et chaque rebond perd de l'énergie (les rebonds raccourcissent, contrairement à l'overshoot dont la fréquence reste constante). Non testé.

```js
var e = 0.6;     // élasticité : part de la vitesse conservée à chaque rebond
var g = 5000;    // gravité en unités/s² : plus haut = rebonds plus courts
var nMax = 6;    // nombre max de rebonds
var n = 0;
if (numKeys > 0) { n = nearestKey(time).index; if (key(n).time > time) n--; }
if (n > 0 && n == numKeys) {
  var t = time - key(n).time;
  var v = -velocityAtTime(key(n).time - 0.001) * e;   // vitesse renvoyée
  var vl = length(v);
  var vu = (v instanceof Array) ? (vl > 0 ? normalize(v) : v) : (v < 0 ? -1 : 1);
  var tCur = 0, segDur = 2 * vl / g, tNext = segDur, nb = 1;
  while (tNext < t && nb <= nMax) { vl *= e; segDur *= e; tCur = tNext; tNext += segDur; nb++; }
  if (nb <= nMax) { var d = t - tCur; add(value, mul(vu, d * (vl - g * d / 2))); } else { value; }
} else { value; }
```

## 13-loopout-offset-continue  [THÉORIQUE]

```js
loopOut("offset");    // chaque cycle repart de la valeur d'arrivée : escalier, compteur, rotation qui s'additionne
// loopOut("continue"); // prolonge sur la vitesse de la dernière clé : un objet qui file hors champ
```

## 14-texte-selecteur-expression  [THÉORIQUE]

Animateur de texte > Ajouter > Sélecteur > Expression. Dans « Quantité », `textIndex` (rang du caractère), `textTotal`. Décalage de 2 images par lettre et montée en 8 images :

```js
var d = 2 * thisComp.frameDuration;           // décalage entre lettres
var dur = 8 * thisComp.frameDuration;         // durée de la montée d'une lettre
var t0 = inPoint + (textIndex - 1) * d;
easeOut(time, t0, t0 + dur, 100, 0);          // 100 % = propriété de l'animateur appliquée, 0 % = au repos
```


## Bercement qui ralentit après un événement — [TESTÉ EN LABO] (logique et syntaxe sous Node ; AE en phase 3)
**Quand** : un geste répété qui doit s'apaiser à cause de quelque chose (un appel, une voix, une note) : bercement, respiration, balancier. **Pourquoi** : le calme se lit dans **l'allongement de la période** plus que dans la baisse d'amplitude ; les deux ensemble, sans à-coup de phase. Marqueur n°1 du calque = l'événement.
```js
var amp0 = 5, amp1 = 1.2, P0 = 1.6, P1 = 3.2, d = 4;   // degrés, secondes ; d = durée de l'apaisement
var t0 = (marker.numKeys > 0) ? marker.key(1).time : 1e9;
var k = clamp((time - t0) / d, 0, 1), a = (P1 - P0) / d, ph;
if (time <= t0) ph = time / P0;                       // phase intégrée : ∫ dt / P(t)
else ph = t0 / P0 + Math.log((P0 + a * Math.min(time - t0, d)) / P0) / a + Math.max(0, time - t0 - d) / P1;
value + ease(k, 0, 1, amp0, amp1) * Math.sin(2 * Math.PI * ph);
```
Ne jamais écrire `Math.sin(2*Math.PI*time/P)` avec `P` qui varie (voir Pièges). Si P0 = P1, remplacer le terme en log par `(Math.min(time - t0, d)) / P0`.

---

<a id="saccade"></a>
## Saccade (step-printing) : précisions

[THÉORIQUE, forums Adobe Community consultés le 2026-10-10 ; détail et Premiere : `sources/premiere-ae-saccade-choisie-2026-10.md`, `montage-premiere`]
- **Régulière** : préférer l'expression sur le Time Remap d'une précomp à l'effet Posterize Time, qui n'agit que sur le calque où il est posé. Signalés : décalages dans des pré-compos imbriquées, cadences fractionnaires arrondies ; l'interrupteur « Réduire les transformations » contourne Posterize Time et « Conserver la fréquence d'images ».
- **Choisie, version tableau** (sur Time Remap ; `holds` = image source à montrer à chaque image de la comp) [TESTÉ EN LABO] (syntaxe sous Node, fonctions simulées) :
  `var holds=[0,0,0,5,5,9]; framesToTime(holds[Math.min(timeToFrames(time),holds.length-1)]);`
  Matériau de test : rushes à strobe, `labo/photosensibilite/strobe-rushes/`.
- **Ce qui fond les tenues** : Frame Mix et Pixel Motion (Frame Blending à couper sur le calque saccadé).
- **Traînée façon Wong Kar-wai** : CC Force Motion Blur ou Pixel Motion Blur **avant** le maintien ; ou Echo (Echo Time négatif), CC Wide Time sur une précomp **au-dessus** du calque saccadé.

## À vérifier dans After Effects
La liste des onze vérifications est devenue les exercices E0 à E2 de `PLAN-TESTS.md` (audit 2, 2026-10-13) ; texte d'origine : `archives/audit-2/skills/montage-after-effects/expressions.md`.

<a id="pieges"></a>
## Pièges : précisions (les règles sont dans `SKILL.md` § 6)

- **Moteur JavaScript vs ExtendScript hérité.** Depuis AE 16.0 (CC 2019), le moteur par défaut est **JavaScript** (ECMAScript 2018), plus rapide ; l'ancien **ExtendScript hérité** suit ECMAScript 3. Choix par projet : Fichier > Paramètres du projet > onglet Expressions. Les projets enregistrés dans d'anciennes versions s'ouvrent en ExtendScript hérité. Erreurs classiques en passant à JavaScript : `if/else` sur une ligne sans accolades, raccourci `this()` (utiliser `thisLayer`), syntaxe en snake_case (`this_comp`, à remplacer par `thisComp`), `sourceText` qui doit parfois être lu en `.value`, « dernière valeur » d'un `if` sans `else`.
- **Expressions lentes.** Toute expression est réévaluée à chaque image. `sampleImage()` (lire la couleur d'un calque) est la plus coûteuse : un pixel ou une petite zone, sur peu de calques. Les boucles `for` sur `numKeys` coûtent aussi. Conversion : Animation > Assistant d'images clés > Convertir l'expression en images clés. Pour travailler l'animation, la vue « Expressions désactivées » (raccourci d'aperçu).
- **`exp()` qui explose.** `Math.exp(decay * t)` devient `Infinity` après quelques minutes, d'où la coupure `t < 3` de la recette 05 (point signalé par Dan Ebberts).
- **Séparer les dimensions** change ce que montre le graphe de vitesse (vitesse par axe et non le long du chemin). L'overshoot sur Position 2D non séparée dépasse sur les deux axes à la fois, proportionnellement à leurs vitesses (vérifié en labo).
- **Période qui varie dans un `sin`** : avec `P` animé, la fréquence réelle de `Math.sin(2*Math.PI*time/P)` est 1/P − t·P'/P² et tombe presque à zéro (mesuré : 0,02 Hz au lieu de 0,31 à 0,63 Hz, `labo/ae-expressions/bercement/test.js`). Remède : la recette « Bercement qui ralentit » ci-dessus. [TESTÉ EN LABO] (sous Node ; AE en phase 3)
