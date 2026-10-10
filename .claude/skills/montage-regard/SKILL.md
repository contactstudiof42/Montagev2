---
name: montage-regard
description: Juger un plan, une coupe, un montage, une animation ou un étalonnage — « est-ce que ça marche ? », « pourquoi ce montage ne fonctionne pas », critique d'une version, retour de DA, relecture avant livraison, autocritique d'une planche contact, choisir entre deux prises ou deux versions.
---

# Le regard : principes de jugement et grille d'autocritique

Version 1 (session 1, 2026-10-09), journal déplacé dans `journal.md` et règles distillées en session 8. Ce skill dit **comment je juge**. Il évolue à chaque pièce d'atelier et chaque examen.

## Principes que je défends
1. **L'intention d'abord, l'effet ensuite.** Avant de juger un choix, je reformule en une phrase ce que le plan doit faire ressentir ou comprendre. Un choix est bon s'il sert cette phrase, quelle que soit sa difficulté technique.
2. **L'émotion gagne les arbitrages** (Murch, `culture/walter-murch-blink-of-an-eye.md`). Ordre des priorités quand deux coupes se disputent : émotion > histoire > rythme > trace du regard > plan 2D > espace 3D. Un faux raccord qui sert l'émotion vaut mieux qu'un raccord parfait qui l'éteint.
3. **Le rythme suit l'état intérieur, pas l'action** (Schoonmaker). On dilate l'instant décisif, on compresse le reste.
4. **Réduire.** Un concept, un signe (Saul Bass). Si je ne peux pas dire l'idée d'une pièce en une phrase, la pièce n'a pas d'idée. (Source et tensions : `montage-references` §C ; application au motion : `montage-motion-design-principes` §1.)
5. **Le mouvement doit avoir une cause.** Un objet qui bouge sans raison narrative ou physique est une « animation », pas un geste. Leçon de l'atelier 01 v1 : un pulse symétrique se lit comme un logo, pas comme une respiration.
6. **Le corps du spectateur est l'instrument.** Une bonne coupe tombe là où le spectateur aurait cligné ou respiré. Si je ne ressens rien en regardant, aucune justification théorique ne sauve la pièce.
7. **Faire moins quand c'est plus juste.** L'excès le plus courant n'est pas la vulgarité, c'est la redondance : l'effet qui dit la même chose que l'image, la musique qui surligne l'émotion déjà présente.

## Ce que j'évite (et pourquoi)
- L'effet de mode sans fonction (glitch, light leak, zoom de transition) : il date la pièce et signale un manque d'idée.
- Le centrage systématique et la symétrie par défaut : ils rendent l'image statique ; à utiliser comme choix (frontalité, solennité), pas comme réflexe.
- Les mouvements à amplitude excessive : au-delà de quelques pourcents d'échelle, un « respir » devient un zoom.
- L'apparition par « fondu au noir » d'un élément sur fond coloré : il passe par une ombre sale (atelier 01 v1). Fondre vers la transparence, ou depuis la couleur du fond.

## Grille d'autocritique (à appliquer à chaque planche contact)
- *Liaison* : qu'est-ce qui relie chaque plan au suivant, autre que le tempo (cause, regard, mouvement, son, idée) ? (ajout session 2)
Noter chaque critère de 0 à 3 et écrire **une phrase de preuve visuelle** (ce que je vois sur telle image), jamais une impression vague.

| Critère | Question | Piège à vérifier |
|---|---|---|
| Intention | La phrase d'intention est-elle perceptible sans explication ? | L'œuvre est « jolie » mais neutre |
| Lisibilité | L'information clé est-elle lue au premier regard, dans le temps imparti ? | Kerning, contraste, durée d'affichage (≥ 2× le temps de lecture) |
| Rythme | Les durées varient-elles avec une logique (tension, respiration) ? | Durées uniformes, symétrie mécanique |
| Composition | Le cadre guide-t-il l'œil ? L'espace négatif a-t-il un sens ? | Centrage par défaut |
| Cohérence | Typo, couleur, mouvement parlent-ils la même langue ? | Un élément « d'un autre film » |
| Couleur | La palette porte-t-elle l'émotion ? | Couleurs par défaut du logiciel |
| Mouvement | Chaque mouvement a-t-il une cause, une courbe juste, une fin ? | Easing par défaut, amplitude excessive |
| Originalité | Qu'est-ce qui distingue cette pièce de mille autres ? | Cliché du genre (carton centré, zoom lent, particules) |
| Justesse | En fait-on trop ? Que peut-on enlever ? | Redondance image/son/effet |

Verdict : une pièce n'est « livrable » que si **intention, lisibilité et justesse** sont à 3. Les autres critères peuvent être à 2.

## Méthode de visionnage (sans vidéo : planche contact)
1. Planche à intervalle régulier (ex. 1 image sur 20) avec le numéro d'image : lire l'**arc** d'un coup d'œil.
2. Planche des images de transition (avant/après chaque coupe ou clé).
3. Mesures objectives quand c'est possible : luminance moyenne par image (`signalstats`), durées de plans (`scdet`), loudness (`ebur128`).
4. Commande type [TESTÉ EN LABO, session 1] :
   `ffmpeg -i v.mp4 -vf "select='not(mod(n\,20))',scale=320:-1,drawtext=text='%{n}':x=4:y=4:fontsize=12:fontcolor=yellow,tile=5x2" -frames:v 1 planche.png`

## Règles tirées de l'atelier (distillées en session 8 ; détail daté et preuves : `journal.md`)
1. **Mesurer avant de corriger**, et vérifier l'outil de mesure contre la norme quand il me donne raison trop facilement (01 v6, 05, contrôle de flashs session 7).
2. **Une explication ne va dans un skill qu'après un essai qui isole la variable** (10 v4 : « AgX » réfuté par un seul rendu en Standard).
3. **Premier test d'un montage rapide : la planche « 1re image de chaque plan »** ; pour un plan animé, la 1re, la dernière et l'image de l'événement, pas le milieu (02 v1, 04 v2, 07).
4. **Ce qui relie un plan au suivant doit être autre chose que le tempo** : cause, regard, mouvement, son, idée (02 v4, Honda « Cog »).
5. **Chercher d'abord le rythme que le sujet impose** avant d'en plaquer un (04).
6. **Déplacer le mouvement vers le paramètre qui porte le sens** plutôt que réduire l'amplitude du mauvais (01 v2).
7. **Un effet a besoin de ce qu'il imite** ; une image fixe donne un registre, pas un sens : le sens vient du montage (05).
8. **Le cadre contient la conséquence** ; la lisibilité dépend de la part du cadre, pas de la résolution (07).
9. **Le sens en retard a besoin d'un retour** (reprise d'une image déjà vue) ; chercher la trace avant le flash-back (08).
10. **Une correction locale peut casser ailleurs** : relire toute la planche après chaque correction (07 v2).
11. **Casser une règle complètement, une fois, au bon endroit** : à moitié, c'est une erreur (11, 180°).
12. **Mon œil se trompe sur la saillance ; la mesure la vérifie** : le plus clair et le plus contrasté du cadre gagne le regard (une fenêtre dans le champ vole l'attention à tout le reste). Avant de croire qu'on guide le regard, mesurer (`atelier/12-inquietude-calme/mesure.py`) (12 v4 : j'étais satisfait, la mesure a placé l'attention à 34 % de la diagonale de l'anomalie ; confirmé par un modèle publié, `labo/saillance/`). Nuance : **éclairer une zone y attire l'œil mais peut éteindre le contraste du détail** (tasse blanche sur table au soleil) ; désigner la zone, et garder le détail contrasté dedans.
13. **Vérifier un raccord ou un détail depuis la caméra**, pas sur le plan de la scène : deux objets alignés dans l'axe se lisent comme un seul (12 v2).
14. **Compter les sources chaudes sur chaque planche** (atelier 16, session 10) : mon tic « une seule chaleur méritée » revient même quand la pièce a pour but de l'éviter. Les compter **à la taille de lecture** : une chaleur de 2 px n'existe pas (16 v4).
15. **Pour tuer une lecture parasite d'échelle (ballon, jouet, maquette), changer l'échelle par rapport au cadre** plutôt que la forme : un objet coupé par le bord est plus grand que l'image, donc ni tenu ni manipulable (16 v4). **Une ligne qui traverse une surface se lit fissure, une ligne qui la touche au bord se lit lien** : juger les raccords de lignes dans le plan de l'image.
16. **Relire chaque planche comme un inconnu** : « qu'est-ce que c'est ? » avant « est-ce que ça se voit ? » ; un signe rendu lisible peut devenir un autre signe (16 v3 : la Terre au bout d'un fil = un ballon).
17. **Une source dans le champ** (écran, lampe) : **centrée dans un cadre symétrique, elle fait une icône** ; trop forte, elle **tue le noir** ; décentrée et basse, elle éclaire ce qu'on tient et laisse le visage dans l'ombre (17 v1 → v3). Et la cause d'un apaisement doit **précéder** l'apaisement, au son comme à l'image (17, son).
15. Limite assumée : je juge sur planches, mesures et formes d'onde ; le jugement en temps réel (fluidité, son) reste à confirmer en phase 2.
