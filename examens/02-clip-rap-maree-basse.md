# Examen créatif n°2 — clip de rap (session 2, 2026-10-10)

## Le brief (inventé)
Artiste : « SEL », rappeur d'un port de Bretagne sud (fictif). Titre : « Marée basse », 3:10, drill lente à 138 BPM, couplets sombres sur l'attente (d'un frère en mer, d'une sortie de prison : le texte laisse le doute). Budget : 12 k€, 2 jours de tournage, en hiver. Livrables : le clip YouTube 16:9, plus 3 extraits verticaux de 15 à 30 s pour TikTok et Reels. Le label : « il faut que ça claque sur TikTok », l'artiste : « je veux un vrai film, pas un clip de plus avec des cagoules ».

Réponse rédigée uniquement à partir de mes skills (`montage-direction-artistique`, `montage-rythme`, `montage-references`, `montage-couleur-et-intention`, `montage-kinetic-editing`, `montage-son-et-emotion`, `montage-blender`), sans recherche.

## 1. Intention (7 lignes)
1. **Émotion** : l'attente, avec une menace contenue.
2. **Message** : le temps de l'attente se compte en marées.
3. **Public** : fans de drill française, 16-30 ans, sur téléphone, son activé ; le clip YouTube a un public plus captif (fans venus exprès).
4. **Diffusion** : YouTube 16:9 (public captif) et extraits 9:16 (public pressé, 1 à 2 s pour accrocher).
5. **Contraintes** : 2 jours, hiver, nuit tôt (avantage), port en activité : autorisations, fumigènes réglementés, marées à caler sur l'horaire (coefficients).
6. **Ne surtout pas être** : le clip de drill générique (cagoules, gestes vers l'objectif, voitures, drone de nuit sur la cité).
7. **Contradiction** : le label veut du kinetic, l'artiste veut un film. → C'est exactement la distinction de vos goûts : **deux usages, deux montages, un seul tournage**.

## 2. Trois directions
**A — « Le coefficient » (montage macro à la Ziak)**
- Parti pris : le montage suit l'arrangement, pas le beat. Plans longs et immobiles dans les creux, densité de coupes quand la basse entre. La seconde horloge, c'est la marée (un plan fixe du quai repris toutes les 30 s, où l'eau a baissé à chaque retour : la règle du temps à la Interstellar).
- Références : Ziak (arrangement, seconde horloge, 0,16 % de chaleur), Interstellar (règle du temps rendue visible), Glazer *Surfer* (faire réellement attendre).
- Rythme : médiane de 1,7 s dans les couplets, plans de 6 à 10 s dans les creux ; une seule bascule.
- Palette : nuit cyan-vert du port (sodium et LED des quais gardés « faux », comme dans Joker) ; une seule chaleur, la fusée de détresse ou les feux d'un chalutier qui rentre, à la fin.
- Typo : aucune dans le clip, sauf le titre à la fin, petit et fixe.
- Son : aucun SFX surligné ; le ressac et les drisses mixés sous la prod dans les creux.
- Effets : retouche du niveau d'eau entre les retours du plan fixe si la marée ne suffit pas (plaque propre du quai à chaque heure).
- Risque : un clip « beau et lent » qui perd les fans. Faisabilité : bonne (2 nuits, peu de figuration). Version muette : se comprend (l'eau qui baisse). Cliché : nuit et noir sont courants en drill ; ce qui différencie, c'est l'horloge-marée et l'absence de posture.

**B — « Tables des marées » (registre graphique)**
- Parti pris : les paroles et les chiffres des tables des marées en typographie cinétique sur des plans très sobres ; le texte est l'image.
- Références : Saul Bass (un signe), Patrick Clair (le décor devient le contenu du personnage), kinetic (captions calées à la syllabe).
- Rythme : calé sur les temps (micro). Palette : noir et un seul jaune de balise. Son : clicks et impacts typographiques.
- Risque : un lyric video de luxe ; le film voulu par l'artiste disparaît. Cliché : la typo cinétique sur du rap est très courante.

**C — « Le quai » (plan continu à la Murai)**
- Parti pris : un plan-séquence à la Steadicam sur 200 m de quai. SEL marche et rappe au premier plan ; derrière lui, la vie du port bascule (une barque qu'on hisse vide, des gens qui attendent, puis un attroupement). Le choc n'est jamais monté.
- Références : Murai « This Is America » (le sens à l'arrière-plan), Honda « Cog » (un raccord caché dans une sortie de champ si nécessaire).
- Risque : 2 jours, c'est très court pour régler un plan-séquence avec de la figuration ; la météo. Version muette : forte. Cliché : peu vu en drill française.

## 3. Recommandation
**A pour le clip, et des extraits verticaux montés en kinetic à partir des mêmes rushes.** Je reprends à C son idée la plus forte (un attroupement à l'arrière-plan, jamais commenté) dans un seul plan de A.
- Pourquoi pas B : il sert le label et trahit l'artiste.
- Pourquoi pas C entier : trop risqué en 2 jours d'hiver.
- Ce que je perds : la radicalité de C.
- Vos goûts : A applique Ziak et Interstellar, les extraits appliquent le kinetic. C'est la répartition que vous avez confirmée.

## 4. Critères de réussite
1. Le plan-horloge revient au moins 5 fois et l'eau a visiblement baissé à chaque retour : lisible sur une planche des 5 retours.
2. Aucune coupe calée sur le beat dans les couplets (vérifiable avec `labo/analyse-clip`).
3. Chaleur ≤ 0,5 % des pixels avant la bascule (mesure de l'atelier 02).
4. Extraits verticaux : sujet lisible à l'image 1, hook avant 2 s, -14 LUFS mesuré sur le MP4.
5. L'attroupement de l'arrière-plan n'est pas vu au premier visionnage par la moitié des spectateurs-tests : il est découvert au deuxième.

## 5. Préparation du tournage (effets et double livrable)
- Tourner en 4K (ou en open gate) pour recadrer les extraits 9:16 dans le 16:9 ; composer avec une zone verticale sûre au centre pour les plans clés.
- Plan-horloge : trépied ancré, objectif et focale notés, repères au sol, une plaque propre à chaque passage (pour l'éventuelle retouche de niveau d'eau). Consulter l'horaire et le coefficient des marées : marée basse en fin de 2e nuit.
- Log 10 bits (les noirs du port font des bandes en 8 bits : `labo/encodage/`), shutter à 180°, et quelques plans à 90° pour l'image sèche des extraits kinetic.
- Son seul (« wild ») : ressac, drisses, treuil, pas sur le ponton. Ce seront les SFX des extraits kinetic, avec une cause visible et filmée.
- Fusée ou fumigène : autorisation de la capitainerie et des pompiers ; sinon une lampe orange en pratique et un compositing de la fumée.

## 6. Autocritique (sans complaisance)
- **J'ai plaqué vos goûts comme une recette.** A, c'est Ziak transposé au bord de la mer : noir, une chaleur, montage sur l'arrangement. Je n'ai pas cherché ce que *ce* texte et *ce* port demandaient de différent. Exemple manqué : la marée basse découvre ce qui était caché (épaves, chaînes, objets). C'était une image-concept propre à ce titre (« ce que l'attente met à nu ») et je ne l'ai pas vue. **C'est le cliché le plus dangereux pour moi : mon propre système.**
- B est une direction de paille, construite pour être écartée. Une vraie direction graphique aurait été, par exemple, le texte gravé ou peint sur les coques, filmé : graphique, mais physique.
- La faisabilité de A est sous-estimée : le plan fixe sur 2 nuits n'a qu'un seul cycle de marée par nuit visible de jour comme de nuit. Il faut vérifier que l'amplitude couvre bien la durée de tournage.
- La préparation du tournage est bonne : double livrable, log 10 bits, son seul, autorisations. C'est le progrès net depuis l'examen n°1.
- Rien n'est dit de l'étalonnage de la peau sous le sodium, ni du traitement de la voix du rappeur (intelligibilité sur le ressac).
**Note : 14/20** (13 à l'examen n°1). Le double usage est bien résolu et la préparation du tournage est solide. Mais j'ai fait preuve de paresse conceptuelle : j'ai appliqué un goût au lieu de chercher l'idée propre au sujet.

## 7. Corrections apportées
- `montage-direction-artistique` : ajout du test « mon propre système » et de la question « qu'est-ce que *ce* sujet a que les autres n'ont pas ? » avant de choisir une référence ; règle du double livrable (un tournage, deux montages).
- BACKLOG : atelier « ce que la marée découvre » (image-concept propre au sujet), et `montage-preparation-tournage-vfx` passe en priorité.
