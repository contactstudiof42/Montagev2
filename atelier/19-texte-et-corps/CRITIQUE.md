# Pièce 19 « Le texte et le corps » — critique (session 13)

Fichiers : `scene.py` (7 plans Blender, 21 images à 12 i/s chacun), `monte.py` (un vers par plan, texte incrusté, planche = image 14 de chaque plan). Rendus dans `atelier/rendus/19/` (non versionnés).

## v1 — les plans bruts (`v1-plans-bruts.png`)
- `large` : le personnage fait **2 % du cadre**, la marche ne se voit pas. `mains` : illisible (une boule devant un cylindre, la caméra presque dans le torse). `vitrine` : **le reflet n'existe pas** (vitre diélectrique sombre : 4 % de réflexion, rien ne revient). `face` (regard caméra), `porte` (de dos, applique froide), `escalier` (la fenêtre s'allume à l'image 10), `rue-vide` : lisibles.
- Corrigé en v2 : plan large rapproché (personnage à ~20 % de la hauteur), vitrine en miroir métallique (le double apparaît), mains de profil en contre-jour. **Les mains restent le point faible** : avec des primitives, un geste de main ne se lit pas ; je l'ai noté comme limite de l'atelier, pas comme leçon.

## v2-A — texte illustré (`v2-A-illustre-planche.png`)
mains, large, face, mains, vitrine, vitrine, porte, escalier.
- **Intention servie ?** Lisible, oui ; servie, non. Chaque plan répète le vers : le spectateur n'a rien à relier, le texte se lit deux fois.
- **Découverte** : illustrer oblige à **répéter des plans** dès que le texte revient sur un motif (mains aux vers 1 et 4, vitrine aux vers 5 et 6) : la structure du texte impose la sienne à l'image, et la répétition se lit comme une pauvreté de rushes, pas comme une rime.
- Et l'illustration échoue même à illustrer : « je parle avec les mains » sur le visage (pas de plan de mains qui parlent) ; il faudrait **tourner pour le texte**, ce qui est exactement ce qu'un clip illustratif coûte.
- L'absente (« tes clés ») n'existe nulle part : A raconte un homme qui marche, pas un homme quitté.

## v2-B — contrepoint (`v2-B-contrepoint-planche.png`)
rue-vide, large, porte, mains, face, vitrine, rue-vide, escalier.
- **Gagne** : la rue vide sur « tes clés » fait de l'**absente** le sujet dès le premier vers ; le **regard caméra sur « un type que je connais pas »** fait du spectateur la vitrine (l'accord le plus fort des trois montages) ; la **reprise** de la rue vide au vers 7 relit le vers 1.
- **Perd** : la porte au vers 3 puis la rue au vers 5 **casse le trajet** (il arrive chez lui, puis il est de nouveau dehors). Le contrepoint de sens a été payé par une incohérence d'espace, et l'œil le sent plus que le sens.

## v3-B2 — contrepoint sur un trajet continu (`v3-B2-contrepoint-trajet-planche.png`) — RÉFÉRENCE
rue-vide, large, vitrine, mains, face, porte, rue-vide, escalier.
- L'espace avance (rue, vitrine, poche, face, porte, rue déserte, lumière dans l'escalier) ; **le sens est en contrepoint, l'espace en continuité**.
- « Je lui fais signe, il me fait signe » **sur la porte de dos** : personne ne répond ; le « il » devient ambigu (le reflet ? la porte ?) : ambiguïté productive.
- « Personne attend en bas de chez moi » sur la rue vide : la même image qu'au vers 1, mais il vient d'entrer ; **le texte change le sens d'une image reprise** (leçon de la pièce 08, vérifiée dans l'autre sens : ici c'est le mot qui relit l'image).
- Fin : la fenêtre qui s'allume **sans lui** : la présence par la trace.
- Reste faible : le vers 3 (« ma mère… les mains ») sur la vitrine est presque arbitraire ; il faudrait un plan de mains **qui bougent** (le corps qui contredit le vers 4 avant qu'il soit dit). Et le plan `mains` est illisible.

## Comptes
| Montage | Vers illustrés | Plans répétés | Regards caméra | Trajet cohérent |
|---|---|---|---|---|
| A | 8/8 visés (6 réussis) | 2 | 1 (vers 3, sans raison) | oui |
| B | 2/8 (ancrage, geste) | 1 (reprise voulue) | 1 (vers 5) | **non** |
| B2 | 2/8 (ancrage, geste) | 1 (reprise voulue) | 1 (vers 5) | oui |

## Leçons (versées dans `montage-direction-artistique` et `montage-regard`)
1. **Illustrer l'ancrage et le geste, contredire le reste** : le vers qui pose qui et où (2) et le seul geste physique (4) sont illustrés ; ailleurs, l'image dit ce que le texte tait.
2. **Contrepoint de sens, continuité d'espace** : le spectateur pardonne un décalage de sens, pas un trajet qui recule.
3. **Un regard caméra, sur le vers où le « je » parle de la façon dont on le voit** : le spectateur devient le regard dont parle le texte.
4. **Le texte relit une image reprise** : le même plan vide sur deux vers fait le récit à lui seul.
5. Illustrer oblige à tourner pour le texte et fait répéter les plans : à budget égal, le contrepoint demande **moins** de plans.
Limite : jugé sur planches, sans musique ni voix ; la scansion (où tombe le vers dans le plan) n'est pas testée : un vers par plan est une simplification.
