---
name: montage-rythme
description: Rythme et musicalité du montage — où couper, durée des plans, coupe sur le mouvement, coupe sur la musique et les temps forts, tension et respiration, ralenti, ellipse, montage rapide, plan-séquence, « le montage est mou », « ça traîne », « c'est trop haché », caler un clip ou une pub sur le beat.
---

# Rythme : tension, respiration, musicalité

Version 1 (session 1, 2026-10-09), tirée des fiches `culture/` (Murch, Schoonmaker, Edgar Wright). **Non encore éprouvée dans l'atelier** : exercice prévu (même matériau monté sur trois tempos).

## Ce que je crois du rythme
1. **Le rythme n'est pas la vitesse.** C'est la variation des durées. Un montage uniformément rapide est aussi monotone qu'un montage uniformément lent ; l'oreille et l'œil s'habituent en quelques plans.
2. **Le rythme suit l'état intérieur** (Schoonmaker, Raging Bull) : dilater l'instant qui compte (ralenti, plan long, silence), compresser le reste (ellipse, plans courts). Un seul ralenti bien placé au milieu de plans courts vaut plus que du ralenti partout.
3. **Couper à la fin d'une pensée** (Murch) : la coupe tombe là où le spectateur aurait cligné ou respiré — fin d'une phrase, d'un regard, d'un geste. Couper avant : on frustre ; couper après : on s'ennuie.
4. **La respiration est une décision.** Après un pic, un plan plus long et plus calme permet au spectateur de digérer. Sans respiration, l'intensité s'aplatit (montage « paranoïaque » de Goodfellas : il épuise volontairement — à réserver aux sujets où l'épuisement est le sens).
5. **Arbitrer par l'émotion** : un léger faux raccord sur le temps juste vaut mieux qu'un raccord parfait à contretemps.

## Couper sur le mouvement
- Couper **pendant** un geste (pas avant, pas après) cache la coupe : l'œil suit le mouvement d'un plan à l'autre. [THÉORIQUE, principe classique]
- Raccord de forme, de geste ou de son : la transition devient du contenu (Wright). Préférer à un fondu, qui dit seulement « le temps passe ».

## Couper sur la musique
- Toutes les coupes sur les temps forts = métronome. Varier : couper sur certains temps, laisser des plans enjamber la mesure, réserver les coupes « pile » aux accents qui comptent (attaque de refrain, impact).
- Un son peut porter le raccord : un son qui se transforme relie deux plans sans continuité visuelle (Murch, Apocalypse Now : ventilateur → rotor).
- **Retirer le son juste avant l'impact** (logo, révélation, chute) : le silence multiplie l'impact (Schoonmaker).
- Pour un clip ou une pub très synchronisée : verrouiller la musique **et ses droits** avant le tournage, et tourner sur playback (Wright, Baby Driver). La synchro se fabrique au tournage.

## Ordres de grandeur (à affiner par mesures et atelier)
| Usage | Durée de plan indicative | Remarque |
|---|---|---|
| Montage « hip-hop » d'une routine (Wright) | 6 à 12 images à 24/25 i/s | 5 à 8 plans, son amplifié ; 1 à 2 fois par film max |
| Texte à lire à l'écran | ≥ 2× le temps de lecture à voix haute | Plus long pour un public non captif |
| Respiration après un pic | nettement plus long que la moyenne des plans précédents | La différence compte plus que la valeur absolue |

## Pièges
- Le tic : un procédé (freeze frame + voix off, montage hip-hop, coupe sur chaque beat) répété devient un cliché.
- La synchro totale enferme : si la musique change (droits, version courte), tout est à refaire.
- Sur les réseaux sans son, le rythme doit aussi se lire visuellement.

## Mesurer le rythme (labo, à développer)
- Détection de coupes [TESTÉ EN LABO, session 1 — `labo/rythme/RESULTATS.md`] :
  `ffmpeg -i film.mp4 -vf "scdet=threshold=10,metadata=print:key=lavfi.scd.time:file=-" -f null - 2>/dev/null | grep -o "lavfi.scd.time=[0-9.]*" | cut -d= -f2`
  → temps des coupes → durées de plans → histogramme. Fiable sur coupes franches (8/8 au centième) ; **rate les fondus enchaînés** ; entre plans très proches, descendre le seuil à 3 (risque de faux positifs, à tester sur matériau réel).

## À faire
- Atelier : un même matériau monté sur trois tempos ; critique comparée.
- Fiches : Sally Menke (Tarantino), Kirk Baxter (Fincher), clips (Gondry, Jonze).
