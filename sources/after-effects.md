# Sources : After Effects (mouvement, easing, expressions)

Consultées le 2026-10-09. Les pages helpx.adobe.com ont répondu **403** au fetch direct : leur contenu est connu par les extraits du moteur de recherche (versions localisées de la même page), à relire en phase 2.

## Officiel Adobe

| URL | Ce qu'elle confirme | Lu ? |
|---|---|---|
| https://helpx.adobe.com/after-effects/using/legacy-and-extend-script-engine.html (miroirs localisés, par ex. https://helpx.adobe.com/at/after-effects/desktop/work-with-expressions/expression-basics/legacy-and-extend-script-engine.html) | Moteur JavaScript d'AE 16.0 basé sur ECMAScript 2018 ; ExtendScript hérité basé sur ECMAScript 3 (1999) ; choix dans Fichier > Paramètres du projet > Expressions ; les projets d'anciennes versions s'ouvrent en ExtendScript hérité ; différences de syntaxe (snake_case, `this()`, if/else). | Extraits de recherche (403 au fetch) |
| https://helpx.adobe.com/ca/after-effects/desktop/animate-in-after-effects/speed-between-keyframes/speed.html | Graphe de vitesse dans l'éditeur de graphiques : vitesse constante = ligne droite ; la vitesse dépend de l'écart de temps et de valeur entre les clés. | Extraits de recherche |
| https://helpx.adobe.com/after-effects/using/keyframe-interpolation.html | Page officielle de l'interpolation et de l'Easy Ease. **403, non lue** : la valeur 33,33 % n'est pas confirmée par une source officielle. | Non |
| https://helpx.adobe.com/at/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html | Référence officielle du langage d'expressions. | Titre seulement |

## Référence communautaire (docsforadobe)

| URL | Ce qu'elle confirme | Lu ? |
|---|---|---|
| https://ae-expressions.docsforadobe.dev/objects/property/ | Signatures : `loopOut([type="cycle"][, numKeyframes=0])`, types cycle / pingpong / offset / continue (continue sans argument de clés) ; `wiggle(freq, amp[, octaves=1][, amp_mult=0.5][, t=time])` ; `smooth`, `temporalWiggle`, `valueAtTime(t)`, `velocityAtTime(t)`, `nearestKey(t)`, `key(index)`, `numKeys`. | Oui |
| https://ae-expressions.docsforadobe.dev/general/global/ | `time` en secondes ; `thisComp` ; `posterizeTime(updatesPerSecond)` (fréquence de mise à jour plus basse que la comp), exemple avec `framesToTime`. | Oui |
| https://ae-expressions.docsforadobe.dev/general/interpolation/ | `linear`, `ease`, `easeIn`, `easeOut`. | Non lue en détail (sémantique tirée de la mémoire, à vérifier) |

## Praticiens

| URL | Ce qu'elle confirme | Lu ? |
|---|---|---|
| https://www.motionscript.com/articles/bounce-and-overshoot.html (Dan Ebberts) | Overshoot = oscillation à fréquence constante et amplitude décroissante (sin ÷ exp) ; rebond = perte d'énergie, rebonds de plus en plus rapprochés, impossible en sinus. Overshoot sur clés : `nearestKey`, vitesse lue **juste avant** la clé avec `velocityAtTime`, amplitude ÷ ω. Bounce back : élasticité `e`, gravité `g`, `nMax`. | Oui (résumé) |
| https://creativecow.net/?p=1853883 et fils voisins | Ebberts : `Math.exp(decay*t)` devient `Infinity` sur de longues durées, d'où la limite en temps. | Extraits de recherche |
| https://www.schoolofmotion.com/tutorials/graph-editor-after-effects | Différence graphe de vitesse / graphe de valeur ; exemple de rebond en Y dans le graphe de valeur ; graphe de vitesse pour régler un time remap. | Extraits de recherche |
| https://www.schoolofmotion.com/tutorials/intro-to-the-graph-editor-in-after-effects/ | Introduction à l'éditeur de graphiques (Joey Korenman). | Extraits de recherche |
| https://creativecow.net/?p=2412183 , https://community.adobe.com/t5/after-effects-discussions/ease-vs-eased-keyframes/td-p/7493370 | Easy Ease = vitesse 0, influence 33,33 (affichée), forum. Pratique courante de passer à 60 % pour un mouvement plus « snappy ». | Extraits de recherche (communauté, non officiel) |
| https://www.provideocoalition.com/ease_and_wizz/ | Ease and Wizz : courbes d'easing par expression (alternative aux clés). | Titre seulement |

## Non sourcé (convention de métier)

Durées types en images (tableau de la section 2 du skill), plages de wiggle, règles « départ vif / arrivée longue » : pratique de motion design, pas de source unique. À juger à l'œil.
