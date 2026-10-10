---
name: montage-rythme
description: Rythme et musicalité du montage — où et quand couper, durée des plans, tension et respiration, couper sur la musique (beat ou arrangement), tempo et cadence, dilater ou compresser le temps, ralenti, montage rapide ou plan long, timing comique. Mots entendus : « le montage est mou », « ça traîne », « c'est trop haché », « ça manque de respiration », « cale-le sur le beat », « la chute tombe à plat », « le plan dure trop / pas assez ».
---

# Rythme : tension, respiration, musicalité

**Marqueurs** : [SOURCÉ] fiche ou source écrite · [THÉORIQUE] convention du métier non vérifiée ici · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette Blender / Pillow / ffmpeg, hypothèse à confirmer sur de vraies images (phase 2).

**Fait foi sur** : où et quand couper, durées de plans, tension / respiration, calage sur la musique et la cadence. **Ailleurs** : raccords (dont raccord mouvement), J/L-cut, définition de l'ellipse → `montage-grammaire` ; silence, sound design, musique avec ou contre l'image → `montage-son-et-emotion` ; cuts kinetic réseaux → `montage-kinetic-editing`.

Détail des mesures, des pièces et des références : [`details.md`](details.md).

## Ce que je crois du rythme [SOURCÉ] (Murch, Schoonmaker, Wright, fiches `culture/`)
1. **Le rythme n'est pas la vitesse**, c'est la variation des durées. Uniformément rapide = aussi monotone qu'uniformément lent.
2. **Le rythme suit l'état intérieur** (Schoonmaker) : dilater l'instant qui compte, compresser le reste. Un seul ralenti bien placé vaut mieux que du ralenti partout.
3. **Couper à la fin d'une pensée** (Murch) : là où le spectateur aurait cligné ou respiré. Avant : on frustre ; après : on s'ennuie.
4. **La respiration est une décision** : après un pic, un plan nettement plus long et plus calme. Sans respiration, l'intensité s'aplatit (Goodfellas épuise volontairement : à réserver aux sujets où l'épuisement est le sens).
5. **Arbitrer par l'émotion** : un léger faux raccord sur le temps juste vaut mieux qu'un raccord parfait à contretemps.

## Couper sur la musique
- Toutes les coupes sur les temps forts = métronome. Couper sur certains temps, laisser des plans enjamber la mesure, réserver les coupes « pile » aux accents (attaque de refrain, impact). [THÉORIQUE]
- **Micro ou macro, à choisir** [SOURCÉ] (Ziak, mesuré sur le clip réel : coupes non calées sur le beat, mais 26 coupes/min avec la basse, 13,4 sans) : **micro** (sur les temps : énergie, réseaux) ou **macro** (densité selon l'arrangement : gravité, clip, film de marque). Les deux sont dans les goûts de l'utilisateur.
- **Le calage sur les temps est une texture ; la densité par section est la forme. Hybride = défaut pub et réseaux** : intro tenue, calage là où la musique pousse, accélération avant la coupure, image d'exception sur la coupure. [ÉPROUVÉ EN MAQUETTE] (pièce 03)
- **Un accent ne vaut que par sa rareté** : 1 fois sur la coupure = l'événement ; 4 fois à intervalle régulier = papier peint. [ÉPROUVÉ EN MAQUETTE] (pièce 03)
- Un son peut porter le raccord (Murch : ventilateur → rotor). Retirer le son juste avant l'impact (Schoonmaker) : le détail du silence est dans `montage-son-et-emotion`. [SOURCÉ]
- Clip ou pub très synchronisés : verrouiller la musique **et ses droits** avant le tournage, tourner sur playback (Wright, *Baby Driver*). [SOURCÉ]
- **Tempo et cadence** [TESTÉ EN LABO] : à 25 i/s, seuls 60, 75, 100, 125, 150 BPM tombent en images entières ; à 24 i/s : 60, 72, 80, 90, 96, 120, 144, 160, 180. Ne jamais couper « toutes les N images » : poser les marqueurs de temps et couper sur l'image la plus proche, en numéro d'image absolu (`round(t*fps)`), jamais en additionnant des durées arrondies (dérive mesurée : −460 ms sur 24 s).

## Interstellar, référence de l'utilisateur (`GOUTS.md` prime) [SOURCÉ]
Poser une règle du temps puis la faire entendre (un tic devient un compteur) ; le son de la scène suivante arrache la fin d'une scène émotionnelle ; compresser le temps raconté pendant qu'un visage reste sans coupe ; raccourcir les segments du montage parallèle à l'approche du climax (8 / 4 / 2 / 1 s) ; retirer les plans de respiration pendant la tension. Mise à l'épreuve (pièce 29) [ÉPROUVÉ EN MAQUETTE] : l'ellipse est **dans la coupe** ; pulsation sur les retours = causalité ; enseigner la règle puis la rompre ; écran partagé pour expliquer, alternance pour émouvoir. Détail : `details.md`.

## Où couper : principes éprouvés en maquette
- **Le sujet impose souvent son rythme** : lent puis brusque est la forme naturelle de la révélation (marée, bougie) ; la laisser se poser (≥ 1 s), ne pas la remplacer par une accélération de montage. [ÉPROUVÉ EN MAQUETTE] (pièce 04)
- **Chaîne causale** (démo produit, réaction en chaîne) : la mécanique décide où couper ; couper dans les respirations entre deux contacts (≥ 4 images), jamais sur le contact quand la preuve est l'argument ; ouvrir avant la cause, cadrer la conséquence. [ÉPROUVÉ EN MAQUETTE] (pièce 07)
- **Tempo propre du sujet** (pendule, respiration, danse) : couper sur ses points morts ; si ce tempo change, tenir le cadre pour qu'on le compare à lui-même. [ÉPROUVÉ EN MAQUETTE] (pièce 14)
- **Plan de retour** (même cadre, quelque chose a changé) : plus long que le plan de départ (4 s puis 6 s). [ÉPROUVÉ EN MAQUETTE] (pièce 12)
- **Dilater par la durée plutôt que par la vitesse** : tenir au-delà de l'attente, mais une attente **habitée** (quelqu'un qui pourrait agir et n'agit pas). Ralenti d'image seulement sur rushes haute cadence ; jamais d'interpolation sur mains, fils, occlusions ; juger la pire image du sujet, pas la moyenne. [ÉPROUVÉ EN MAQUETTE] (pièce 15)
- **Une forme qui ralentit** : une direction lente commune à tous les canaux (débit, durée des plans, son, lumière) ; une relance y est **un coup** (un pic qualitatif), pas une rafale ; retirer des ponctuations sans allonger les plans ne calme rien ; peu de coupes = chacune pèse (un fondu long peut la remplacer). [ÉPROUVÉ EN MAQUETTE] (pièces 25, 26)
- **Timing comique** : un plan d'arrivée lisible en < 0,5 s ; écart après le mot-clé ~2 images (0 rogne, 8 = temps mort) ; règle de trois ; réaction muette finie par un **bouton**, coupe ~0,6 s après ; pas de pré-lap sur une contradiction. [ÉPROUVÉ EN MAQUETTE] (pièce 27) La réplique suivante tombe sur la fin du rire ; couper sur celui qui écoute. [SOURCÉ] (fiche sitcom)
- **Réaction tenue** : pas de durée normée ; elle tient si l'enjeu est posé juste avant et si le plan change encore ; couper après le dernier geste. [SOURCÉ]
- **Silence vu de loin** : de près, un silence est une réaction ; de loin, un trou. Lui donner un support visible qui soit un acte des personnages, à la taille de lecture. [ÉPROUVÉ EN MAQUETTE] (pièce 34)

## Ordres de grandeur
| Usage | Durée indicative | Remarque |
|---|---|---|
| Montage « hip-hop » d'une routine (Wright) | 6 à 12 images | 5 à 8 plans ; 1 à 2 fois par film max |
| Texte à lire | ≥ 2× le temps de lecture à voix haute | fait foi : `montage-motion-design-principes` |
| Respiration après un pic | nettement plus long que la moyenne précédente | la différence compte plus que la valeur |

## Pièges
- Un procédé répété (freeze frame + voix off, coupe sur chaque beat) devient un tic.
- La synchro totale enferme : si la musique change (droits, version courte), tout est à refaire.
- Sans son (réseaux), le rythme doit aussi se lire visuellement ; mixer le dialogue sous les effets est à proscrire en pub et réseaux.

## Mesurer [TESTÉ EN LABO]
`labo/analyse-clip/analyse_clip.py` (coupes, flashs, tempo, calage sur le beat, lumière) ; `scdet` pour les coupes franches (rate les fondus, sous-détecte dans le noir) ; méthode « écart au milieu » pour les fondus ; marqueurs de temps XML (`labo/marqueurs/beats_xml.py`, vérifier la phase). Commandes et chiffres : `details.md`.

## Reste à faire
Fiches Sally Menke, Kirk Baxter, clips (Gondry, Jonze). Phase 2 : confirmer sur de vrais montages les durées éprouvées en maquette.
