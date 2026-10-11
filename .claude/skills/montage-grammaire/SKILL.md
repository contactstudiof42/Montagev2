---
name: montage-grammaire
description: Grammaire du montage — raccords (regard, mouvement, direction, axe, forme, son), règle des 180°, champ / contrechamp, jump cut, insert, plan de coupe, ellipse, J-cut et L-cut, montage parallèle, faux raccord, monter une interview ou un dialogue. Mots entendus : « ça saute », « on est perdu dans l'espace », « ils ne se regardent pas », « le dialogue ne coule pas », « comment je cache cette coupe dans l'interview ? », « on a franchi l'axe », « personne ne verra le faux raccord ? ».
---

# Grammaire du montage

**Marqueurs** : [SOURCÉ] fiche ou source écrite · [THÉORIQUE] convention du métier non vérifiée ici · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette Blender / Pillow / ffmpeg, hypothèse à confirmer sur de vraies images (phase 2). Sans marqueur dans une section : celui de son titre.

**Fait foi sur** : raccords (dont le raccord mouvement), axe et 180°, J/L-cut, ellipse, montage parallèle, interview, faux raccord. **Ailleurs** : où et combien de temps tenir un plan → `montage-rythme` ; silence et sound design → `montage-son-et-emotion` ; niveaux → `montage-loudness-livraison` ; l'émotion gagne les arbitrages → `montage-regard`.

## Pourquoi une grammaire (et quand la casser)
Elle sert à ce que le spectateur **ne se pose pas de question involontaire** (où sont-ils ? qui regarde qui ? combien de temps a passé ?). On la casse quand **la question est voulue** : désorientation (*Se7en*, *Goodfellas*), urgence (*À bout de souffle*), subjectivité. Casser par ignorance se voit ; casser par choix se sent, et alors **franchement et avec constance**.

## Les raccords [THÉORIQUE]
| Raccord | Ce qu'il fait | Piège |
|---|---|---|
| **Regard** | Regard → ce qui est regardé : point de vue (effet Koulechov) | direction du regard incohérente avec la position de l'objet |
| **Mouvement** | Couper **pendant** un geste, le finir dans le plan suivant : la coupe disparaît | couper au début ou à l'arrêt du geste : la coupe se voit |
| **Direction** | Sortie à droite → entrée par la gauche | inverser = demi-tour (sauf intention) |
| **Dans l'axe** | Rapprochement dans le même axe : accent, choc | variation de valeur trop faible (< ~30 %, chiffre à vérifier) = saut |
| **Forme** | Une forme en appelle une autre (os → vaisseau, *2001*) | gratuit sans lien de sens |
| **Son** | Son du plan suivant en avance (J-cut) ou du précédent qui continue (L-cut) | dialogue monté « au carré » = haché |

## Règle des 180°
Une ligne imaginaire relie les deux personnages (ou un personnage et ce qu'il regarde, ou un mouvement). Caméra d'un même côté : les regards se répondent. Franchie : ils semblent regarder dans la même direction. [THÉORIQUE]
- **Constaté en maquette** (deux personnages Blender, `labo/grammaire/RESULTATS.md`) : axe franchi, A regarde aussi à gauche, comme s'ils parlaient à un tiers ; en amorce, l'épaule de l'autre saute de bord. Contrôle automatisable : signes de direction de regard opposés en champ / contrechamp (`labo/grammaire/sauts_regard.py` : franchissement complet = 1 saut, partiel = 2). [ÉPROUVÉ EN MAQUETTE]
- **La franchir proprement** : plan dans l'axe, mouvement de caméra qui la traverse, personnage qui se déplace, ou plan large qui redéfinit l'espace. [THÉORIQUE]
- **La casser avec un sens** (pièce 11, v4) [ÉPROUVÉ EN MAQUETTE] : franchir pour **tous les plans à la fois** (un seul saut, à la jointure), sur l'image où le rapport de force bascule ; **un plan large du nouveau côté tout de suite** ; **le fond change** (choisir le côté = choisir à qui appartient le monde, à préparer au tournage). Coupe franche pour un renversement brutal, travelling qui traverse pour une bascule lente. Finir sur celui qui a perdu la scène. Kubrick s'en sert pour le malaise ; Ozu l'ignore systématiquement : la constance en fait un style. [THÉORIQUE]

## Dialogue et interview
- **Champ / contrechamp** : couper sur la **réaction** autant que sur la réplique ; le plus fort est souvent celui qui écoute. [THÉORIQUE]
- **Séparer par la coupe, réunir par le filé** : *Whiplash* tient un champ-contrechamp strict entre l'élève et le maître pendant 1 h 35 (mêmes cadres à chaque retour), puis, au final, les relie par des filés aller-retour dans un même plan (environ toutes les 2 s, 1:36:14). Le mouvement de caméra dit qu'ils sont enfin accordés. Attention en analyse : un détecteur voit ces filés comme un seul plan long, et une coupe peut s'y cacher. [VU SUR IMAGES] (`analyses/films/whiplash.md`)
- **J-cut / L-cut** : décaler image et son de quelques images à quelques secondes ; le dialogue coule. [THÉORIQUE]
  - **J-cut de mémoire** : le son du souvenir arrive ~12 images avant son image ; au retour, **pas de L-cut** : couper le son net, le silence du présent est le coup. [ÉPROUVÉ EN MAQUETTE] (pièce 08)
  - **Raccord dans l'axe du temps** (même cadre, deux époques) : aligné au pixel (magique) ou franchement décalé (mémoire qui flotte) ; à moitié aligné, il paraît raté. [ÉPROUVÉ EN MAQUETTE] (pièce 08)
- **Interview** : couper à la fin d'une pensée. Masquer une coupe dans une phrase par un plan de coupe (insert, archive, mains) ou **assumer le jump cut** ; un changement d'échelle (recadrage de 10-20 % si on a de la marge en 4K) seulement là où l'on veut l'emphase, jamais alterné mécaniquement : un punch-in n'est pas un cache-coupe (face caméra : `montage-youtube` §5) ; jamais de fondu au milieu d'une phrase. Seuil sous lequel un jump cut se voit trop (souvent cité : ~0,5 s retirée) [À TRANCHER EN PHASE 2]. [THÉORIQUE]
- **Conversation multicaméra : distinguer la coupe de contenu et le changement d'angle.** « Couper à la fin d'une pensée » vaut pour ce qu'on retire ; le changement de caméra, lui, tombe **au milieu des phrases** : 71 à 88 % des coupes pendant la parole pour 77-82 % du temps parlé (Boxho, « POPCORN »). Quand il tombe dans un trou, c'est **0,1-0,2 s avant la reprise**, sur celui qui va parler. Un récit d'invité se tient en gros plan 5 à 16 s ; un échange se coupe en plans de 1 à 4 s. Contre-exemple voulu : la comédie de dialogue (*Le Dîner de cons*, 40-44 % pendant la parole, coupe au milieu d’un trou de 0,8 s ; 21 % dans la scène sincère) cherche l’air pour ses chutes. [VU SUR IMAGES, mesuré] (`analyses/youtube/popcorn-anyme-lena-etoiles.md`)
- **Plans de coupe** : les tourner en abondance (mains, détails, lieu) ; ce sont les jokers du montage.

## Changement à travers une coupe (cécité au changement)
- Un détail qui change entre deux plans **n'est pas vu par défaut** : la coupe masque le signal de mouvement qui attirerait l'œil (Rensink, O'Regan et Clark, 1997 ; Levin et Simons, 1997). C'est ce qui sauve les faux raccords ordinaires, et ce qui tue une anomalie voulue. [SOURCÉ]
- **Anomalie voulue** (inquiétude, indice) : la placer dans la zone que le plan précédent a déjà désignée (lumière, contraste, centre, regard), sans la désigner dans le plan où elle apparaît (pas de zoom, pas de son). Plan de retour plus long que le plan de départ (voir `montage-rythme`). [ÉPROUVÉ EN MAQUETTE] (pièce 12, mesures de saillance, pas de spectateur)
- **Décor chargé** : désigner la zone par une couleur saturée au plan 1 et poser l'anomalie devant elle ; un seul leurre de même forme à proximité, pas trois. [ÉPROUVÉ EN MAQUETTE] (pièce 12 v8)
- **Faux raccord à cacher** : l'inverse, hors de la zone saillante, ou couper sur un mouvement qui capte l'œil. [THÉORIQUE]
- **Raccorder deux plans suivis dans le noir** pour faire un seul trajet : *La Haine* (12:26-15:17) suit les trois amis 113 s dans la cité, laisse Saïd disparaître derrière une vitre noire de cage d'escalier, et coupe sur lui sortant d'une trappe sur le toit, filmé d'au-dessus (14:19,9). Le noir efface la coupe, le geste continu (monter) fait le raccord : on croit à un plan de 171 s. Utile pour un faux plan-séquence. [VU SUR IMAGES] (`analyses/films/la-haine.md`)
- Outil : `atelier/12-inquietude-calme/mesure.py` (aire du changement, distance à la zone saillante).

## Temps [THÉORIQUE]
- **Ellipse** : enlever ce que le spectateur peut reconstruire ; il préfère compléter que subir. (Dilater / compresser au service de l'émotion : `montage-rythme`.)
- **Montage parallèle** : deux actions alternées créent une relation ; accélérer l'alternance fait monter la tension (détail et pièce 29 : `montage-rythme`). Donner à chaque ligne sa matière (couleur, lumière) pour qu'un insert de 2 s se lise sans contexte ; suspendre l'alternance sur l'action la plus tendue. [VU SUR IMAGES] (*Interstellar*, 1:50-2:27)
- **Montage-séquence** : une durée longue en quelques plans, souvent sur musique ; cliché de la « préparation » si mal utilisé (montage « hip-hop » de Wright).

## Montage son (bases) [THÉORIQUE]
- Trois couches : voix (l'ancre), ambiances et bruitages, musique ; monter les ambiances **en continu sous les coupes image** (une ambiance qui coupe avec l'image fait sauter).
- Fondus audio de quelques images sur chaque coupe son. Intention sonore : `montage-son-et-emotion`.

## Reste à faire
Aire de regard et règle des 30 % sur un vrai visage (phase 2) ; vérifier les chiffres (30 %, durées de J-cut, seuil du jump cut) par des sources de monteurs.
