---
name: montage-regard
description: Juger un plan, une coupe, un montage, une animation ou un étalonnage — « est-ce que ça marche ? », « pourquoi ce montage ne fonctionne pas », critique d'une version, retour de DA, relecture avant livraison, autocritique d'une planche contact, choisir entre deux prises ou deux versions.
---

# Le regard : principes de jugement et grille d'autocritique

Version 1 (session 1, 2026-10-09). Ce skill dit **comment je juge**. Il évolue à chaque pièce d'atelier et chaque examen.

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

## Journal des leçons (alimenté par l'atelier)
- 2026-10-09, atelier 01 v1 : apparition par émission 0 → mot noir sur fond bleu (fausse ombre). Pulse symétrique ±10 % = mécanique. Italique FreeSerif : « ff » mal approché, illisible en titre.
- 2026-10-09, atelier 01 v2 : corriger un excès en réduisant l'amplitude du même paramètre donne un mouvement invisible. Il faut **déplacer** le mouvement vers le paramètre qui porte le sens.
- 2026-10-09, atelier 01 v3-v4 : une police système (« Times ») se voit comme une absence de choix ; une valeur d'interlettrage ne se transpose pas d'une police à l'autre ; un fond en dégradé dont l'intensité varie donne une profondeur qu'un aplat n'a pas.
- 2026-10-09, atelier 01 v4 : je me suis écarté de ma propre intention sonore (silence → grondement) sans le décider. **Relire l'intention avant chaque version.**
- Limite de l'atelier cloud : je ne vois pas la vidéo en mouvement ni n'entends le son. Les planches contact, les courbes de luminance (`signalstats`) et les formes d'onde sont des substituts ; noter ce qui reste à juger en temps réel.
- 2026-10-09, atelier 01 v6 : j'ai « corrigé » un bruit de rendu imaginaire (16 échantillons + débruitage, 3× plus long) ; la mesure a montré que les taches venaient de l'encodage H.264 du dégradé. **Mesurer avant de corriger** ; une planche réduite grossit les artefacts de compression.
- 2026-10-10, atelier 02 v1 : 7 plans sur 19 illisibles à leur 1re image (sujet hors cadre, dans le noir, trop petit). En montage rapide, **la planche « 1re image de chaque plan » est le premier test** ; elle a révélé plus de défauts que n'importe quelle autre lecture.
- 2026-10-10, atelier 02 v4 : une fois tout lisible, le défaut restant était de **conception** : une suite d'objets sans lien n'est pas une montée, même bien rythmée. Une coupe rapide ne crée de la tension que si les plans s'enchaînent par **cause et effet** (Honda « Cog »). Question à ajouter à la grille : *qu'est-ce qui relie ce plan au suivant, autre que le tempo ?*
- 2026-10-10, atelier 02 : un parti pris de couleur se **mesure** (% de pixels chauds par image), comme la loudness. Le dire avec un chiffre rend la critique opposable.
- 2026-10-10, atelier 04 v1 : le sujet a sa propre dramaturgie (la marée découvre lentement ce qui est haut, puis tout le sol d'un coup). **Chercher d'abord le rythme que le sujet impose** avant d'en plaquer un. Et mon système (« une seule chaleur ») est revenu par la matière (la rouille) alors que je l'avais chassé de la lumière : le constater, le décider, ne pas le subir.
- 2026-10-10, atelier 04 v2 : caméra sous l'eau pendant 97 images, invisible sur mon test d'une image (prise au milieu). **Tester la 1re et la dernière image** d'un plan animé et vérifier les contraintes géométriques avant un rendu long. L'accident a ouvert une direction (ironie dramatique : montrer l'objet sous l'eau d'abord).
- **Un effet a besoin de ce qu'il imite** (atelier 05, session 5) : une halation sans source ponctuelle ne fait que teinter le ciel ; un grain trop gros devient du bruit de surveillance. Avant d'ajouter un effet de support, vérifier que l'image contient ce que l'effet suppose (spéculaires, émulsion fine, lumière dure).
- **Une image fixe donne un registre, pas un sens** (atelier 05) : « menace » ou « constat » se lisent sur une image ; « souvenir » exige un regard (contrechamp, voix, son). Ne pas demander à l'étalonnage ce qui revient au montage.
- **Mesurer avant de corriger, encore** (atelier 05) : « neutre » se vérifie au biais R-B du ciel et du sol ; mon premier « constat » neutre était bleu à -19.
- **Contrôler chaque caméra à l'image du contact, pas au milieu du plan** (atelier 07, session 6) : deux caméras placées sous le plan de la table cachaient le contact domino → tasse ; une image fixe à l'image 64 l'a montré avant un rendu de 80 images. Une chaîne causale se vérifie aussi maillon par maillon avant de tourner (la tasse partait seule : 1 cm de jeu).
- **Le cadre doit contenir la conséquence** (atelier 07) : dans deux montages sur trois, l'impact final (le son le plus fort) avait lieu au bord du cadre ou hors champ. Je cadre d'abord la fin, puis je vérifie que la chaîne entre.
- **Une correction locale peut casser ailleurs** (atelier 07 v2) : en arrêtant la tasse au sol, j'ai empêché sa bascule, et elle tombait debout. Après chaque correction, **relire toute la planche**, pas seulement l'endroit corrigé.
