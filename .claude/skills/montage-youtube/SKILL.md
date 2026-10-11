---
name: montage-youtube
description: Monter et habiller une vidéo YouTube longue (5 à 60 min) ou une chaîne — « retention editing » (MrBeast), face caméra en jump cuts et punch-in, essai vidéo, doc explicatif (Vox, Johnny Harris), vulgarisation (Kurzgesagt, EGO), vlog, gaming, podcast filmé, live session ; titre, miniature, chapitres, écran de fin, specs d'envoi. Mots d'un YouTubeur : « ça décroche à 30 s », « la rétention chute à 3 min », « un montage à la MrBeast », « mes jump cuts sautent », « miniature qui claque », « habillage de chaîne ». Shorts, Reels : `montage-kinetic-editing`, `montage-formats`.
---

# YouTube : un spectateur qui a choisi, et qui peut partir à chaque seconde

Marqueurs : [SOURCÉ] lu dans une source citée · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu seulement sur maquette Blender / Pillow / ffmpeg, hypothèse à confirmer en phase 2 · [THÉORIQUE] déduit, non vérifié. Statut : sources secondaires, aucune vidéo regardée ; la grammaire FR du face caméra n'est pas sourcée (culture générale).

**Fait foi sur** : la vidéo longue (promesse, relances, courbe de rétention), le **face caméra** (jump cut, punch-in, micro-sauts), l'habillage de chaîne, la miniature et les specs d'envoi YouTube. Pour le format court vertical, les SFX, captions et transitions : `montage-kinetic-editing` ; Shorts narratifs : `montage-formats` ; principes EGO et tensions entre écoles : `montage-references`. Détail, chiffres et fiches : `details.md`.

## Ce qui change par rapport au cinéma et au clip
| | Cinéma | Clip | YouTube long |
|---|---|---|---|
| Unité de rythme | la scène | la musique | **l'idée** (phrase, preuve, relance) |
| Regard caméra | interdit ou rare | performance | **adresse directe** : le fil |
| Coupe | cachée | affichée, musicale | **jump cut assumé** |
| Son | diégèse + musique | la chanson | **la voix d'abord** |
| Motion | générique | effets | **un système réutilisable** |
| Structure | actes | couplets | **minutes** : promesse < 30 s, relances, fin nette |
| Avant le film | l'affiche après | la pochette | **titre + miniature avant le tournage** |
| Écran | salle | téléphone | téléphone **et téléviseur** (~45 % du visionnage, 2024) [SOURCÉ] |

## Principes
1. **La promesse d'abord** : titre et image clé écrits avant de tourner, tenus dans les 30 premières secondes (clic confirmé tout de suite, contexte vers 7 s, nouvelle accroche vers 30 s). [SOURCÉ] (guide MrBeast, Galloway)
2. **« Aucun temps mort », pas « couper vite »** : le retention editing 2019-2023 coupait toutes les 1,3-1,5 s ; MrBeast 2024 ralentit (38 → 23 coupes/min). Un plan long est juste s'il **fait** quelque chose ; le rythme suit l'écran (téléviseur = plus lent). [SOURCÉ]
3. **Penser en minutes** : une relance forte toutes les ~3 min sur 12-15 min (question, lieu, personnage nouveau) ; montrer l'enjeu avant la préparation ; un bloc sans voix après une récompense, jamais avant la promesse ; **finir net** (annoncer la fin fait partir). [SOURCÉ] ; placement du bloc sans voix [THÉORIQUE]
4. **Lire la courbe de rétention comme une critique** : un creux = la promesse n'est pas tenue ; un pic = passage revu (il plaît, **ou il n'est pas clair**). [SOURCÉ]
5. **Le regard caméra est un contrat (face caméra)** : couper dans le plan plutôt que cacher la coupe ; avec une caméra, le **punch-in** (110-130 % sur la chute), le bruitage et le carton remplacent le second plan ; le gag de montage **commente** la personne, il ne la couvre pas. [THÉORIQUE] Mis à l'épreuve sur marionnette 2D, seuils à confirmer sur un vrai visage [ÉPROUVÉ EN MAQUETTE] (pièce 24) :
   - un jump cut qui déplace le sujet de **moins de ~2 % de la largeur** se lit comme une panne ; ces micro-sauts naissent quand on coupe chaque respiration ; leur taille dépend de la **durée retirée** → ne couper que les ratés et les silences, sinon garder la respiration ; changer d'échelle seulement si la phrase mérite l'emphase (un punch-in n'est pas un cache-coupe). Seuil de durée minimale retirée : [À TRANCHER EN PHASE 2] ;
   - le punch-in est une **hiérarchie** : alterné mécaniquement 100/125 %, il donne l'emphase au hasard ; le réserver aux chutes ;
   - couper juste **après** un clignement ; un plan de coupe métaphorique se pose sur la phrase qui énonce la métaphore.
   Outil : `labo/micro-sauts/micro_sauts.py --video V.mp4 --coupes t1,t2…` (échelle, décalage, option `zone` : la mesure globale peut rater une tête qui saute devant une bibliothèque). [TESTÉ EN LABO] (synthétique)
6. **Montrer ET dire au même instant** (essai vidéo) ; jamais d'image papier peint ; **comparer plutôt qu'expliquer** (un split-screen vaut un paragraphe). [SOURCÉ]
7. **Le rythme vient de l'écriture** (doc explicatif) : une chaîne de questions ; **afficher la source** dès qu'un chiffre est avancé ; plus le sujet est grave, moins d'effets. [SOURCÉ]
8. **Une matière unique porte tout** (la carte de Johnny Harris, les formes de Kurzgesagt) ; matérialiser la donnée ; le zoom continu remplace le plan d'établissement. [SOURCÉ]
9. **Voix définitive avant l'animation** (Kurzgesagt) : l'image change quand l'idée change (~1 image / 3 s) ; aucun plan mort pendant une explication, un mouvement de repos sous le seuil de l'événement. [SOURCÉ]
10. **L'authenticité est un effet de montage** (vlog) : le raté gardé est dosé ; le plan vide où le sujet entre ; timelapse et drone = ponctuation. [SOURCÉ]
11. **Un effet violent est une ponctuation** (meme editing) : un par chute, sur un temps fort ; deux images à l'écran doivent avoir un rapport (contre le « sludge »). [SOURCÉ]
12. **Une série tient par une règle, un compteur et un palier par épisode** (Ryan Trahan). [SOURCÉ]
13. **Concevoir un système, pas une séquence** (habillage) : palette, rigs, cartons de chapitre, lower third maison ; partir d'un template, c'est choisir le cliché. [SOURCÉ]
14. **Gaming, podcast, live** : hiérarchie écran / visage à chaque instant ; **couper sur la réaction**, pas sur l'action ; chaque extrait tient seul, la phrase la plus forte d'abord, sans trahir son sens ; live session : **le son ne se coupe jamais**, couper vers ce qu'on entend, une contrainte visible jamais trahie. [SOURCÉ]
15. **Critique et animation** : le décor est un générique ; citer court et transformer (droits) ; la durée suit l'idée. [SOURCÉ]
16. **Goût de l'utilisateur : EGO est la référence par défaut** quand on confie une vidéo YouTube à ce studio (vulgarisation au rendu de cinéma, allégorie d'abord, voix posée, une couleur par film) ; Kurzgesagt ou face caméra seulement si le brief l'exige. Principes : `montage-references` § F. **Vu sur « Bibliothèque-Univers » (23 min)** [VU SUR IMAGES, mesuré] : densité en vagues de 3 à 29 coupes/min **commandée par le texte** (une image par élément quand la voix énumère : 36 coupes de 0,67 s en une minute ; plans d'une minute quand elle explique) ; **une minute d'ouverture sans voix** ; chapitres marqués par **le noir et 2 à 4 s de silence**, pas par des cartons ; sponsor isolé par la forme (captures blanches) et encadré de silences ; 24 s de silence après la dernière phrase ; mix à **-21 LUFS** (choix de dynamique, pas une erreur). (`analyses/youtube/ego-bibliotheque-univers.md`)
17. **Le contexte de visionnage est une forme** : une vidéo du soir, au lit, au casque peut baisser luminosité, volume et rythme avec le sujet. [THÉORIQUE] (examen n°10)
18. **Densité décroissante quand le sujet est un manque** (épreuve, privation) : le montage perd ses outils avec le sujet (captions → musique → bruitages → punch-ins), temps long après la 1re récompense, jamais plus de ~4 min sans relance. [THÉORIQUE] (examen n°11) Mis à l'épreuve [ÉPROUVÉ EN MAQUETTE] (pièce 26 ; courbe : `labo/youtube/densite.py`) :
   - **une relance est un coup qualitatif** (le dernier bruitage, un drop), **pas une rafale** : densifier 3 s n'ajoute qu'un événement ;
   - sans outil à retirer, la relance tardive passe par **un changement de régime d'image ou de son** (autre grain, timecode) ;
   - retirer les outils sans allonger les plans ne calme pas (chaque coupe restante choque plus) ; on ne coupe que vers ce que la lumière montre.
19. **Un traitement de divertissement liste ses gags** (5 à 10, placés à la minute ; répertoire : `culture/gags-de-montage.md`) : couper tôt sur la contradiction, tenir longtemps sur la réaction muette ; les gags **structurels** (plant & payoff, règle de trois) survivent à la perte des outils, les ponctuations non. [SOURCÉ]

## Méthode pour une vidéo longue confiée
1. Genre et contrat (divertissement, face caméra, essai, explicatif, vlog, motion) : il fixe l'unité de rythme.
2. Promesse : titre + miniature, au moins 2 variantes (Test & Compare : jusqu'à 3, juge par durée de visionnage par impression). [SOURCÉ]
3. Ouverture minutée (0-30 s), plan des relances, fin nette, écran de fin de 5-20 s prévu à l'image.
4. Pré-montage de la voix seule (radio edit), puis couverture : chaque phrase reçoit une preuve, une comparaison ou un visage ; supprimer les respirations mortes, garder les vivantes.
5. Ponctuation (punch-ins, inserts, bruitages, captions) **sur les chutes et les mots-clés seulement** (4-6 mots au plus). Mécanique fine des SFX et captions : `montage-kinetic-editing`.
6. Habillage lisible au téléphone et à 3 m d'un téléviseur.
7. Vérifier sans le son, puis sans l'image ; repérer ses tics.

## Clichés à refuser (sauf parti pris)
Le zoom sur chaque phrase ; le whoosh sur chaque coupe ; les mèmes qui couvrent la personne ; la caption qui répète la voix (sauf accessibilité : des sous-titres) ; le B-roll papier peint ; la carte 3D sans raison d'échelle ; l'intro « salut à tous » avant la promesse ; l'écran divisé sans rapport ; le template reconnaissable.

## Specs et zones (aide YouTube consultée le 2026-10-10) [SOURCÉ]
- **Envoi** : MP4 faststart, H.264 High, GOP fermé de la moitié de la cadence, 4:2:0, cadence d'origine, AAC-LC ou Opus 48 kHz, SDR BT.709 ; 1080p 8 Mb/s (12 en 50/60), 2160p 35-45. Détail : `details.md` ; recette : `labo/livraison/`, `montage-loudness-livraison`.
- **Chapitres** : premier à 00:00, au moins 3, 10 s minimum ; validateur `labo/youtube/chapitres.py`. [TESTÉ EN LABO]
- **Écran de fin** : vidéo ≥ 25 s, 5 à 20 dernières secondes, 4 éléments au plus.
- **Miniature** : 16:9, jusqu'à 3840×2160, ≥ 640 de large. Lisibilité à **168 px de large** : capitale ≥ 12 % de la hauteur sur image chargée, ≥ 9 % sur image calme, 2 à 4 mots, aplat sous le texte sur image chargée. [ÉPROUVÉ EN MAQUETTE] (jugé à l'œil sur fonds synthétiques, `labo/youtube/RESULTATS.md`)
- **Shorts** : vertical ou carré, jusqu'à 3 min (depuis le 15 octobre 2024).

## Liens
`montage-kinetic-editing`, `montage-formats`, `montage-references` (§ F-G), `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-rythme`, `montage-grammaire` (jump cut hors face caméra).
