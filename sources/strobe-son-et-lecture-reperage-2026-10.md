# Son d'un strobe de scène ; temps de lecture de repérage d'une liste de noms

Recherche du 10/10/2026 (BACKLOG 81 et 82), pour l'examen n°8 (`examens/08-festival-strobe-lineup.md`, autocritique 3-4) et la pièce 20 (`atelier/20-la-lumiere-ecrit/CRITIQUE.md`).
Statuts : **vérifié** = lu sur la page ou dans le PDF (consulté le 2026-10-10) ; **non vérifié** = vu seulement dans un résultat de recherche ou déduit ; **calcul** = mon raisonnement à partir des valeurs.

---

## 1. Quel son fait un stroboscope de scène ? (BACKLOG 81)

### Mécanisme
- **Xénon** (Martin Atomic 3000 d'origine et équivalents) : un condensateur chargé à plusieurs centaines de volts se décharge dans un tube de xénon, amorcé par une impulsion de plusieurs kilovolts. L'arc crée une **onde de choc** dans le gaz qui frappe la paroi du tube. Sur un flash photo, la même physique donne un **« pop » à la décharge** puis un **sifflement aigu de recharge** (convertisseur élévateur).
- **LED** (Atomic 3000 LED, etc.) : semi-conducteurs en basse tension, pas d'arc ni de haute tension. Le seul bruit documenté est celui du **ventilateur** (refroidissement forcé). Une alimentation à découpage peut aussi siffler, mais aucune source ne le confirme pour un strobe de scène.

| Point | Valeur / constat | Statut | Source |
|---|---|---|---|
| Le tube xénon produit une onde de choc supersonique à chaque arc ; à basse énergie on n'entend qu'« un petit coup contre le verre » ; le pré-pulse sert notamment à faire moins de bruit | qualitatif | vérifié | Wikipédia, « Flashtube », https://en.wikipedia.org/wiki/Flashtube |
| Durée d'une décharge de flashtube : de 0,1 µs à quelques dizaines de ms | 0,1 µs - dizaines de ms | vérifié | idem |
| Flash photo : « pop » dû à l'expansion brutale du gaz, puis sifflement de recharge du convertisseur (> 1 000 V) qui cesse quand le condensateur est plein | qualitatif | vérifié | Improve Photography, « Why does a camera flash make noise? », https://improvephotography.com/54300/why-does-a-camera-flash-make-noise/ |
| Flash de studio : le claquement du tube est plus faible quand la puissance baisse | qualitatif | non vérifié | forum FredMiranda (résultat de recherche) |
| Strobe xénon : condensateur de quelques centaines de volts, amorçage à quelques kV ; strobe LED en basse tension, sans circuit haute tension | ordres de grandeur | non vérifié | brevets US8773276 / US9355535 « Dual mode LED strobe » (résultat de recherche) |
| Atomic 3000 LED : « refroidissement forcé, régulé en température, faible bruit, réglages de ventilateur » ; mode « LED and Xenon » (émulation du xénon) par menu ou DMX | qualitatif, **aucun dBA publié** | vérifié | fiche Martin Atomic 3000 LED, https://proadv.com/content/Atomic-3000-LED.pdf |
| Forum d'éclairagistes xénon/LED : on y parle de spectre, de luminosité et d'usure du tube, **jamais du bruit** | aucun témoignage sur le son | vérifié | ControlBooth, « Strobe theory -- xenon vs. LED », https://www.controlbooth.com/threads/strobe-theory-xenon-vs-led.38925/latest |
| Pack SFX « High Voltage » : plus de 950 sons enregistrés à partir de décharges réelles (3 500 V) dans un tube xénon | catalogue | non vérifié | itch.io, https://giga-softworks.itch.io/high-voltage-sound-of-electricity |
| Banques en ligne : catégories « flash », « flickering light / strobe malfunction » (souvent un « pulse » électrique ou un bourdonnement de néon) | catalogue | non vérifié | ElevenLabs sound-effects (résultat de recherche) |

### Conclusions pour un monteur
1. **Dans un festival, un strobe ne s'entend pas.** Un xénon claque bien un peu (onde de choc, relais ou amorçage), mais c'est un petit « tic » à 1 m, écrasé par un système son à plus de 100 dB. Un strobe LED est muet, à part son ventilateur. Aucune fiche ne donne de niveau sonore. **Un SFX de « relais » ou de « décharge » sur un coup de strobe est donc un son inventé**, plausible physiquement (xénon) mais jamais entendu par le public. C'est légitime (règle « son causé par l'image »), à condition de le savoir : on sonorise **l'idée de décharge**, pas un son de salle. L'examen n°8 disait « un son qui vient de la salle » : c'est faux au sens littéral.
2. **Ce que font les sound designers (non vérifié, pratique courante plus catalogues)** : ils empruntent au **flash photo** (pop puis sifflement de recharge), à l'**électricité** (arc, étincelle, relais, interrupteur de projecteur, « clunk » de gros projecteur de stade), ou à un son **synthétique** (pulse, transitoire de bruit blanc filtré). Pour une matière signée, le principe Ben Burtt s'applique : partir d'un vrai déclic (relais, interrupteur, flash d'appareil photo enregistré de près) et le déformer.
3. **Sur un morceau techno, le meilleur choix est souvent un transitoire très court et aigu** (clic, sans queue grave) **calé sur le coup** : il ne se bat ni avec la grosse caisse ni avec la basse. Un « boom » sur chaque flash doublerait le kick.

### Limites
Aucune mesure acoustique (dB) d'un strobe de scène trouvée, ni xénon ni LED. Le forum ControlBooth ne parle pas du son. Le « tic » audible d'un xénon de scène reste une déduction (physique du flashtube plus expérience photo), à vérifier à l'oreille si un jour on a accès à un Atomic.

---

## 2. Combien de temps pour trouver un nom connu dans une liste affichée ? (BACKLOG 82)

| Mesure | Valeur | Statut | Source |
|---|---|---|---|
| Recherche hybride de mots (cible mémorisée parmi des mots affichés) : le temps de réponse **augmente linéairement avec le nombre de mots affichés** (2 à 16) et logarithmiquement avec le nombre de cibles en mémoire | qualitatif | vérifié | Boettcher & Wolfe 2015, *Atten Percept Psychophys* 77:1132-1142, https://search.bwh.harvard.edu/new/pubs/HybridWordBoettcherWolfeAPP2015.pdf |
| **16 mots affichés, 16 cibles possibles en mémoire : ~3 500 ms** pour trouver la cible (contre ~2 700 ms pour des objets photographiés) | 3,5 s | vérifié | idem (discussion générale) |
| Les auteurs attribuent l'écart mots/objets au fait que **lire un mot demande probablement de fixer chaque élément** | qualitatif | vérifié | idem |
| Recherche dans un menu déroulant (3, 6 ou 9 éléments, cible connue) : pente observée d'**environ 100 ms par élément** ; le modèle qui colle aux données traite **~3 éléments par fixation** (85 % des essais), contre 380 ms/élément prédit pour une lecture strictement un par un | ~100 ms/élément | vérifié | Hornof & Kieras, CHI 97, « Cognitive Modeling Reveals Menu Search is Both Random and Systematic », https://chi1997.acm.org/proceedings/paper/ajh.html |
| Fixation en lecture : **200-300 ms** en général (plage 50-500) ; saccade 20-35 ms ; 7-9 caractères par saccade | 200-300 ms | vérifié | Pitt (Perfetti), « Eye Movements During Reading », https://sites.pitt.edu/~perfetti/Eye%20Movements%20During%20Reading.htm |
| Fixation en lecture : ~225-250 ms (Rayner) | 225-250 ms | non vérifié | UMSL, résultat de recherche |
| Pentes de recherche visuelle : de ~0 (trait saillant, « pop-out ») à ~10 ms/élément (conjonction) et 30 ms/élément ou plus (configuration spatiale) ; la plupart des tâches vont de 0 à 150 ms/élément ; les pentes forment un continuum | 0-150 ms/élément | non vérifié | Wolfe 1998, *Psychological Science* (PDF NYU indisponible : erreur 503) ; Wolfe 2016, *i-Perception*, confirme seulement le « continuum » (vérifié) |
| Recherche d'un mot parmi des distracteurs : estimation ancienne d'environ 83 ms par caractère (recherche en mémoire, autre mesure) | 83 ms/car. | non vérifié | Springer, BF03198632 (résultat de recherche) |

Aucune source trouvée sur la lecture d'affiches ou de génériques de festival en particulier.

### Déduction pour un carton de 20-24 noms (calcul, [THÉORIQUE])
- **Recherche auto-terminée** : le fan s'arrête quand il trouve son nom, donc en moyenne vers la moitié de la liste. S'il ne le trouve pas, il doit tout parcourir. Le fan qui vérifie « mon artiste est-il là ? » doit donc parfois tout lire.
- **Hypothèse haute (un nom par fixation, ~250-300 ms par nom, ce que suggère Boettcher & Wolfe pour les mots)** : 24 noms ≈ **3,5 s en moyenne, ~7 s pour tout parcourir**, plus ~0,5 s pour s'orienter dans le carton.
- **Hypothèse basse (menu, ~100 ms par élément, plusieurs éléments par fixation)** : 24 noms ≈ **1,2 s en moyenne, ~2,5 s pour tout parcourir**, plus le temps d'orientation. Mais ce sont des étudiants devant un menu court et serré, à 8-20 pouces d'un écran. Les noms d'artistes sont plus longs, et ils sont lus sur téléphone pendant que la vidéo bouge.
- Recoupement : Boettcher & Wolfe donnent 3,5 s pour 16 mots, avec 16 cibles en mémoire (le pire cas). Un fan qui cherche 1 à 3 artistes est plus rapide par mot, et 24 noms coûtent plus de mots à balayer. Les deux effets se compensent à peu près, d'où **environ 3 à 4 s pour la moyenne**.
- **Règle de travail proposée** : tenir un carton de 20-24 noms **immobile au moins 4 s (plancher : la plupart des fans ont trouvé leur nom), 6-7 s pour qu'un fan puisse conclure « il n'y est pas » ou en repérer plusieurs**. Pour comparaison, la lecture linéaire de tous les noms prend 18 s à 15 caractères par seconde (examen n°8, étape 0) : le repérage est donc 3 à 5 fois plus rapide que la lecture, mais **ne descend pas sous ~3 s pour 24 noms**.
- Ce qui raccourcit la recherche (déduit des pentes, non mesuré ici) : un ordre connu (alphabétique ou par jour), des groupes visuels de 4-6 noms, les têtes d'affiche hors de la liste (pop-out par la taille). Ce qui l'allonge : texte en mouvement, petite taille sur téléphone, fond chargé, noms qui changent de place.
- Conséquence pour la pièce 20 (un nom par coup, 12-16 images) : le problème n'est pas le repérage mais la **lecture d'un seul nom** (plancher ATAA de 16 images). Le carton-liste final (24 noms) doit tenir au moins 4 s, idéalement 6 s, **sans aucune animation pendant la tenue**.

### Limites
Les études portent sur des listes courtes (≤ 16 mots, ≤ 9 éléments de menu), en laboratoire, avec des mots courants. Aucune ne porte sur des noms d'artistes, sur la vidéo, ni sur le DOOH (distance, angle). Les chiffres pour 24 noms sont une **extrapolation linéaire**. Pour valider : test regard réel (5 personnes, carton de 24 noms, chronomètre « dis stop quand tu as trouvé X »), à faire en phase 2.
