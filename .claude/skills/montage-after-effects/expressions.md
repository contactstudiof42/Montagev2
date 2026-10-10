# Annexe : expressions After Effects

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


## Bercement qui ralentit après un événement (session 11) — [TESTÉ EN LABO : logique et syntaxe sous Node ; AE en phase 2]
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
## Saccade (step-printing) régulière ou choisie (déplacé de SKILL.md)

[THÉORIQUE, forums Adobe Community consultés le 2026-10-10] : régulière = effet Posterize Time, ou mieux l'expression `posterizeTime(8);` sur le **Time Remap** d'une pré-composition (Posterize Time n'agit que sur le calque où il est posé ; signalés : décalages dans des pré-compos imbriquées, cadences fractionnaires arrondies, l'interrupteur « Réduire les transformations » contourne Posterize Time et « Conserver la fréquence d'images »). **Choisie** (rushes à strobe, `labo/photosensibilite/strobe-rushes/`) : Time Remap avec des **clés maintenues** (Hold) posées sur les images sources voulues ; la saccade régulière laisse le hasard choisir les images ([ÉPROUVÉ EN MAQUETTE] pièce 20 v1 : aucun coup retenu). Pour la traînée façon Wong Kar-wai : CC Force Motion Blur ou Pixel Motion Blur **avant** le maintien. Version tableau de la saccade choisie (sur Time Remap) : `var holds=[0,0,0,5,5,9]; framesToTime(holds[Math.min(timeToFrames(time),holds.length-1)]);` [TESTÉ EN LABO] (syntaxe sous Node, fonctions simulées). **Frame Blending Off** sur le calque saccadé (Frame Mix / Pixel Motion fondent les tenues) ; traînée (Echo à Echo Time négatif, CC Wide Time) sur une précomp **au-dessus**. Détail et Premiere : `sources/premiere-ae-saccade-choisie-2026-10.md`, `montage-premiere`.

<a id="phase-2"></a>
## À vérifier en phase 2, dans After Effects (déplacé de SKILL.md)

1. Les 11 expressions du labo collées sur de vrais calques (moteur JavaScript **et** ExtendScript hérité) : aucune erreur, valeurs proches de celles du labo.
2. Overshoot 05 : sur des clés linéaires 0 → 100 en 12 i, le pic doit être d'environ 107 vers 1 à 2 images après la clé. Vérifier aussi sur Position 2D non séparée, Rotation et Échelle.
3. La courbe exacte d'`ease()`, d'`easeIn()` et d'`easeOut()` dans AE (le mock utilise des cosinus/sinus) : comparer les valeurs à mi-course (07, 09, 11).
4. Easy Ease (F9) : lire dans « Vitesse de l'image clé » l'influence réelle (33 % ou 33,33 %) et la vitesse (0), en entrée et en sortie.
5. `loopOut("pingpong")` : confirmer l'inversion de l'easing au retour.
6. `posterizeTime(8)` à 25 i/s : relever le nombre d'images de chaque tenue (3 ou 4 i, puisque 25/8 n'est pas entier).
7. Compteur 09 : l'espace fine insécable ` ` s'affiche-t-elle dans la police choisie ? Sinon, utiliser ` `.
8. Time remap 08 : comportement avec un clip plus court que le calque, et avec un slider animé (non intégré par la recette).
9. Coût en aperçu : 30 calques d'écho (06) et un `sampleImage` ; noter le temps de rendu par image.
10. Le comportement de `wiggle` sur des calques dupliqués (tirages différents ou identiques) et l'effet de `seedRandom`.
11. Le message d'erreur exact d'AE quand un slider référencé est renommé (diagnostic courant chez les clients).

