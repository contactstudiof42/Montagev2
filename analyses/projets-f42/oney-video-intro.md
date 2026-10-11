# Oney — vidéo d'intro « rentrée » (version mobile)

_Fiche ouverte le 2026-10-11 (phase 2, session 6, projet Studio F42 n°3). **État : complète** (vue en entier à 2 images/s, 12-21 s à 4 images/s, images pleine définition, sauts recomptés, loudness, true peak et crêtes mesurés sur le fichier livré, transcription Whisper). Source : `ONEY_VIDEOINTRO_169_V3_MOBILE.mov`, HEVC **1080×1080** (le nom dit « 169 » : la version mobile est carrée), 25 i/s, 37,1 s, AAC stéréo. Pas de rushes._

**Lu avant l'analyse** : `A-LIRE.md`, `montage-regard` (grille), `montage-formats` (vertical / réseaux), `montage-kinetic-editing` (captions, punch-in, checklist), `montage-youtube` §5 (face caméra, jump cuts), `montage-loudness-livraison`. Aucun commentaire de Diego.

## Intention et contraintes probables
- **Intention** : présenter aux clients Oney un jeu-concours d'août (« 20 000 euros de cadeaux », un quiz par semaine) sur le ton de la blague de rentrée : un comédien en transat, lunettes de soleil, qui parle au spectateur. La dernière phrase (« Allez, on se lance ? ») et le nom du fichier disent que la vidéo **ouvre le quiz** (dans l'application ou une page mobile) [DÉDUIT].
- **Contraintes probables** [DÉDUIT] : une demi-journée de studio, un décor construit (mur turquoise, ombres de palmes, transat rouge, desserte jaune), une caméra, un texte écrit par le client avec des obligations (montant, lots, principe), une V3 (des allers-retours).

## Forme [mesuré, VU SUR IMAGES]
- **37,1 s : 34,6 s de face caméra, puis 2,5 s de noir** (34,6-37,1 s ; le son s'éteint de -28 à -88 LUFS).
- **Un seul décor, une caméra, des sauts d'échelle** (large / plan taille / plan rapproché) environ toutes les 2,5 à 5 s : 10 sauts détectés (5,0 ; 8,2 ; 10,8 ; 12,2 ; 19,7 ; 24,4 ; 27,3 ; 29,6 ; 32,9 ; 34,6 s), et au moins un raté par le détecteur (vers 14,8 s, vu sur la tuile à 4 images/s) : **au moins 12 plans**.
- **Sous-titres mot à mot** en bas du cadre (blanc, le mot dit surligné dans un pavé vert) ; **autocollants verts** pour les phrases-clés (« Ça fait pas rêver ! », « Vous méritez une rentrée sereine ! », « Un quiz toutes les semaines ») ; **compteur animé** qui monte jusqu'à « 20 000 € » (14,8-17,5 s) ; **pictogrammes des lots collés sur sa chemise**, un par mot (montre, téléphone, friteuse, carte cadeau, 19,4-23 s) ; la voiture dans une pastille verte.
- **Son** : la voix seule, -13,5 LUFS intégrés, LRA 5,4 LU. **True peak +3,1 dBTP ; crêtes décodées à +2,7 et +3,1 dBFS** (L / R, `astats`).
- **Rythme du texte** : environ 70 mots en 33 s ; un trou de voix à 8 s (-24 LUFS) après la première chute.

## Ce qui marche (avec la preuve)
1. **La situation est lisible à la première image** : homme en transat, lunettes, mains derrière la tête, sous-titre « Ah là là… » (0,0 s). Le premier écran est tenu, sans le son (`montage-formats`). [VU SUR IMAGES]
2. **La liste reçoit une image par élément, sans couper** : pendant « montre connectée, téléphone portable, friteuse, carte cadeau », chaque lot vient se coller sur sa chemise au moment où il est dit (19,4-23 s), dans un seul plan. C'est la règle « densité selon le type de phrase » des docs YouTube, faite par le graphisme plutôt que par la coupe : bonne solution quand on n'a qu'une caméra. [VU SUR IMAGES]
3. **Le saut d'échelle tombe sur l'emphase** : on passe au plan rapproché pour « 20 000 € », avec le compteur qui monte (14,8 s). C'est l'usage juste du punch-in (`montage-youtube` §5 : changer d'échelle là où l'on veut l'emphase). [VU SUR IMAGES]
4. **Le vert de la marque est le code de l'information** : chaque mot surligné, chaque autocollant, chaque chiffre est vert ; tout le reste du décor est turquoise, rouge, jaune. L'œil apprend en 3 s que vert = à retenir. [VU SUR IMAGES]
5. **Le nom de la marque est dit tôt (8 s), et c'est juste ici** : la vidéo parle à des clients déjà acquis (« vous êtes client chez Oney ») ; la règle « nom à la fin » des pubs de référence vaut pour la conquête, pas pour un message de fidélité. [DÉDUIT]

## Ce qui pourrait être meilleur, et comment
### Montage et finition (corrigeable avec les mêmes rushes)
1. **Le son sature** : true peak +3,1 dBTP, crêtes décodées au-dessus de 0 dBFS. Lu sur un téléphone en virgule fixe, les plosives et les rires peuvent craquer. C'est le défaut le plus grave du fichier, et le plus simple à corriger : limiteur à -1 dBTP, puis vérifier **sur le fichier encodé** (`ebur128=peak=true`). Les cinq fichiers du studio vus en session 6 dépassent tous -1 dBTP (Benefit -0,6 et 0,0 ; Swile -0,8 ; Sephora -0,1) : **c'est une habitude de chaîne, pas un accident** [mesuré].
2. **2,5 s de noir à la fin** (34,6-37,1 s) après « Allez, on se lance ? », sans logo ni bouton. Si l'application enchaîne sur le quiz, ce noir est un temps mort (le spectateur croit que c'est fini) ; s'il est demandé pour l'intégration, le remplacer par un carton « Jouer » ou par le dernier plan tenu. **À vérifier auprès du client** : je ne connais pas l'intégration.
3. **Redondance des autocollants** : « Vous méritez une rentrée sereine ! » s'affiche pendant qu'il le dit, avec le sous-titre mot à mot en dessous : trois fois la même phrase (voix, autocollant, sous-titre). Garder l'autocollant pour les **informations** (20 000 €, un quiz par semaine) et le retirer des phrases de ton.
4. **Sous-titres sur les jambes** : en 1:1, la ligne de sous-titres tombe sur ses genoux et son short (0,2 s : « la la… » blanc sur la peau claire). Un contour ou une ombre portée, ou remonter la ligne au niveau du torse sur les plans larges.

5. **Codec du fichier : HEVC 10 bits (`yuv420p10le`)** (`labo/outils/qc_livraison.sh`). Si la vidéo est lue telle quelle dans une page web ou une application (et non ré-encodée par un réseau social), une partie des navigateurs et des Android ne lit pas le HEVC 10 bits. Pour une intégration, livrer aussi un H.264 8 bits `yuv420p` avec `faststart` (`montage-loudness-livraison`, specs). [DÉDUIT : compatibilité non testée sur appareils]

### Tournage (à préparer autrement la prochaine fois)
1. **Penser le carré au tournage** : le nom du fichier suggère un master 16:9 recadré en 1:1 [DÉDUIT, non vérifié] ; dans le carré, la plante et la desserte sont coupées au bord et le comédien est à gauche sur les larges (0,2 s), ce qui peut être voulu (lui + la desserte) mais laisse peu d'air. Tourner en open gate ou cadrer large avec une zone 1:1 marquée au moniteur (`montage-preparation-tournage-vfx`).
2. **La marque absente du décor** : le vert Oney n'existe que dans le graphisme. Un accessoire vert (serviette, bouteille, coussin) aurait fait du décor un lieu de la marque, comme les pubs de référence (la marque comme lieu ou costume).
3. **Une prise de réaction muette** (le comédien qui découvre la voiture, sans texte) aurait donné au montage un temps tenu ; tout le film est parlé, sans air sauf à 8 s.

## Grille (`montage-regard`, 0 à 3)
| Critère | Note | Preuve |
|---|---|---|
| Intention | 3 | ton de rentrée, jeu, lots et principe compris sans le son |
| Lisibilité | 2 | code vert clair ; sous-titres sur les jambes en plan large |
| Liaison | 2 | les sauts suivent les phrases ; aucun lien visuel au-delà |
| Rythme | 2 | sauts réguliers de 2,5 à 5 s ; une seule respiration (8 s) |
| Composition | 2 | sujet décentré à gauche en large dans le carré |
| Cohérence | 3 | un vert, une police, un décor |
| Couleur | 2 | décor saturé à quatre couleurs, vert seulement dans le graphisme |
| Mouvement | 2 | compteur et pictos qui arrivent sur le mot ; animations par défaut |
| Originalité | 1 | format « comédien face caméra + sous-titres verts » très courant |
| Justesse | 2 | autocollants redondants ; 2,5 s de noir |

**Verdict** : le montage est **livrable** sur le fond ; le **fichier ne l'est pas** tant que le son dépasse 0 dBFS.

## Confirme, contredit, complète
- **Confirme** `montage-youtube` §5 (le punch-in sur l'emphase) et la règle des docs « une image par élément de liste », ici en graphisme.
- **Nuance** la règle des pubs de référence « le nom de la marque à la fin » : elle vaut pour la conquête ; pour un message à des clients, le nom vient tôt.
- **Complète** `montage-loudness-livraison` : les cinq livraisons du studio vues dépassent -1 dBTP (celle-ci au-dessus de 0 dBFS) ; le QC doit être une étape fixe de la chaîne.

## Principes transférables (pour le studio)
1. **Une caméra, une liste : la liste se fait en graphisme sur le mot**, pas en coupes.
2. **Une couleur = l'information** : réserver la couleur de la marque à ce qu'il faut retenir.
3. **Un autocollant pour une information, jamais pour une phrase de ton.**
4. **QC automatique avant tout envoi** : intégré, true peak, crêtes décodées, durée du noir de fin.

## Ce que Diego en a dit
Rien sur ce projet (titre seulement dans `NOTES-DIEGO.md`).
