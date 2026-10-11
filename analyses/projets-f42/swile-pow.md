# Swile — « POW » (Perfect Office Wallet), 16:9, V5 sous-titres jaunes

_Fiche ouverte le 2026-10-11 (phase 2, session 6, projet Studio F42 n°4). **État : complète** (vue en entier à 1 image/s, six images pleine définition, coupes par deux outils, loudness et true peak des deux pistes, transcription Whisper). Source : `SWILE_POW_169_V5_STJAUNE.mov`, H.264 3840×2160, 25 i/s, 1 min 19,5, **deux pistes AAC mono identiques**. « STJAUNE » = sous-titres jaunes incrustés [DÉDUIT de l'image]. Pas de rushes._

**Lu avant l'analyse** : `A-LIRE.md`, `montage-regard` (grille), `montage-formats` (pub ; principes de campagne : « installer un genre pour le casser », « le gag porte le bénéfice »), bilan des pubs de référence (iPhone 17 : gag de genre), `montage-kinetic-editing` (SFX, captions), `montage-loudness-livraison`. Aucun commentaire de Diego.

## Intention et contraintes probables
- **Intention** : vendre la carte Swile (avantages salariés : restos, culture, cadeaux, mobilité, vacances) en **parodiant le téléachat** : la chaîne « Office Shopping TV », un présentateur en costume bleu et cravate rose, le « Perfect Office Wallet » (P.O.W.), qui n'est qu'une carte, puis **la vraie marque** sur noir.
- **Contraintes probables** [DÉDUIT] : un décor de plateau construit (magenta, comptoir rayé, arche jaune), un présentateur comédien, trois mini-sketchs de cas d'usage avec un second comédien, un faux témoignage tourné ailleurs (mur de briques), un packshot 3D fourni ou fait par le studio ; cinq versions (V5).

## Forme [mesuré, VU SUR IMAGES]
- **1 min 19,5 ; 26 plans (PySceneDetect) à 38 changements (`verif_plan.py`, qui compte aussi les « POW » plein cadre) ; médiane 2,6 s.**
- **Deux parties** : la parodie (0:00-1:03), puis **la rupture** : la lumière du plateau baisse (1:03-1:05), un trou de son (-26,9 LUFS momentané à 1:04), la voix change de ton (« Sérieusement ? … ça existe vraiment ? — Oui, oui, ça existe »), et **le packshot Swile sur noir** (1:08-1:19,5 : carte noire puis téléphone en 3D, « Une seule carte, tous vos avantages. », les cinq catégories qui s'inscrivent une à une sur la voix, logo).
- **Dans la parodie** : l'appel du présentateur (« Vous n'en avez pas marre des portefeuilles XXL ? »), la révélation du produit (0:10-0:25), **trois cas d'usage en sketch** (déjeuner bloqué, cadeau pour « Brenda de la compta » en chariot de cartons, voyage à Miami), chacun clos par **un « POW ! » plein cadre** en lettres 3D magenta (environ toutes les 6 à 7 s), le bandeau « POW au 1 800 800 800 », un faux témoignage avec titre incrusté (« Elle revient sur son expérience POW »).
- **Son** : -11,1 LUFS intégrés, LRA 5,0 LU, true peak -0,8 dBTP, deux pistes mono identiques.

## Ce qui marche (avec la preuve)
1. **La parodie est lisible à la première image** : logo de chaîne « OFFICE SHOPPING TV » en coin dès 0:00, présentateur face caméra qui pointe le spectateur, comptoir, bibelots. Chaque code vient du vrai téléachat (bandeau du numéro, témoignage en incrustation, « Wow ! ») : le genre est installé en une seconde. [VU SUR IMAGES]
2. **Le gag porte le bénéfice** : le « portefeuille parfait » est une seule carte. Si on retire le produit, la blague disparaît (règle de `montage-formats`, tenue). Les trois sketchs sont **une image par cas d'usage**, comme une liste dite (déjeuner, cadeau, voyage). [VU SUR IMAGES]
3. **Le « POW ! » est à la fois la ponctuation et le nom de la campagne** : il clôt chaque sketch, revient en bandeau (« POW au 1 800 800 800 »), et donne son nom au produit fictif (P.O.W.). Un running gag qui fait marque. [VU SUR IMAGES]
4. **La rupture est faite par la lumière et le silence** (1:03-1:05) : le plateau s'éteint, le son tombe, puis le monde réel de Swile arrive (noir, sobre, typographie fine). C'est le même geste que les pubs et clips de référence (**le silence ouvre le changement de régime** : Lacoste, Conte de Noël, Stress) et que « installer un genre pour le casser ». Le contraste de couleur (magenta saturé → noir) dit le passage de la blague à la marque. [VU SUR IMAGES, son mesuré pas écouté]
5. **Le packshot synchronise le texte sur la voix** : « resto », « culture », « cadeaux », « mobilité », « vacances » s'inscrivent au moment où ils sont dits (1:13-1:17). [VU SUR IMAGES]
6. **Le faux témoignage change de décor** (mur de briques, lumière du jour, 0:52-0:55) : on lit tout de suite « autre lieu, autre source », comme les docs YouTube qui changent de cadre pour changer de régime. [VU SUR IMAGES]

## Ce qui pourrait être meilleur, et comment
### Montage et finition (corrigeable avec les mêmes rushes)
1. **Quatre couches de texte sur le packshot** : slogan (« Une seule carte, tous vos avantages. »), catégories qui s'inscrivent, sous-titres jaunes de la voix (« Avec votre carte SWILE, »), logo. Le sous-titre répète ce que les catégories disent déjà (1:13-1:17). Sur le packshot, **retirer les sous-titres** quand le texte à l'écran dit la même chose (ou réduire le slogan), pour que l'œil n'ait qu'une chose à lire.
2. **Les sous-titres jaunes passent sur le comptoir rayé rose et blanc** (0:03 : « Vous n'en avez pas marre ») : fond chargé, contraste variable. Une ombre portée ou un léger bandeau sombre ; ou les remonter d'un cran sur les plans larges.
3. **-11,1 LUFS** : trop fort pour toute diffusion normée (TV -23, cinéma), et les plateformes le baisseront de 3 dB (YouTube, -14) en écrasant sa dynamique pour rien (LRA 5 LU). Le true peak (-0,8 dBTP) dépasse aussi le -1 recommandé, comme les quatre autres fichiers du studio vus. Livrer une version par usage : -14 LUFS / -1 dBTP pour le web, -23 / -1 pour la TV (`montage-loudness-livraison`).
4. **Deux pistes mono au lieu d'une piste stéréo** : la plupart des lecteurs ne jouent que la première piste. Ici elles sont identiques, donc rien ne se perd, mais c'est une source d'erreur à la livraison (et un diffuseur peut refuser le fichier). Une seule piste stéréo (ou mono) déclarée.
5. **La parodie dure 63 s pour 16 s de marque** : les deux gags tardifs (numéro de téléphone, 0:48 ; témoignage, 0:52-0:58) viennent après le troisième cas d'usage, quand la blague est comprise. Pour une version courte (30 s), garder la révélation, deux cas d'usage et la rupture ; c'est la version qui manque probablement à la déclinaison [DÉDUIT, je ne connais pas le plan de diffusion].

### Tournage (à préparer autrement la prochaine fois)
1. Rien de bloquant : le décor, le costume et le faux témoignage servent tous la parodie. Une seule remarque : **la carte P.O.W. du plateau et la vraie carte Swile du packshot** pourraient être le même objet (même noir, même format), pour que la rupture soit un raccord d'objet (la carte de la blague devient la vraie). Si le packshot est en 3D, un insert de la vraie carte au plateau aurait suffi.

## Grille (`montage-regard`, 0 à 3)
| Critère | Note | Preuve |
|---|---|---|
| Intention | 3 | parodie comprise en 1 s ; bénéfice porté par le gag |
| Lisibilité | 2 | quatre couches de texte au packshot ; sous-titres sur fond rayé |
| Liaison | 3 | chaque sketch clos par un POW ; rupture par la lumière et le silence |
| Rythme | 3 | sketchs de 1 à 3 s, POW toutes les 6-7 s, silence avant la marque |
| Composition | 2 | présentateur centré (genre oblige) ; sous-titres en zone chargée |
| Cohérence | 3 | codes du téléachat tenus ; le monde Swile séparé par le noir |
| Couleur | 3 | magenta saturé pour la blague, noir pour la marque : la couleur dit le passage |
| Mouvement | 2 | POW en 3D efficaces ; pas plus |
| Originalité | 2 | la parodie de téléachat est un classique de la pub ; le POW la rend propre à la marque |
| Justesse | 2 | 15 s de gags après que la blague est comprise ; sous-titres redondants au packshot |

**Verdict** : **livrable** en l'état pour le web (après un passage à -14 LUFS et une piste stéréo) ; c'est le plus abouti des projets vus jusqu'ici.

## Confirme, contredit, complète
- **Confirme** sur un projet du studio trois principes de `montage-formats` et du bilan des pubs : installer un genre pour le casser, le gag porte le bénéfice, le silence ouvre le changement de régime.
- **Confirme** « personne ne coupe sur les temps » en creux : le rythme est donné par la blague (un POW par chute), pas par la musique.
- **Complète** `montage-kinetic-editing` (SFX, rang 5 « mème / rupture comique ») : **l'onomatopée graphique plein cadre comme running gag de campagne**, une par chute, qui donne aussi son nom au produit.

## Principes transférables (pour le studio)
1. **Parodier un genre par ses codes graphiques** (logo de chaîne, bandeau du numéro, incrustation de témoignage), dès la première image.
2. **Une onomatopée par chute**, qui devient le nom de la campagne.
3. **Passer de la blague à la marque par la lumière et le silence**, puis par la couleur (saturé → noir).
4. **Au packshot, une seule chose à lire à la fois** : le texte qui s'inscrit sur la voix remplace le sous-titre.
5. **Une version de loudness par diffusion**, et une seule piste son déclarée.

## Ce que Diego en a dit
Rien sur ce projet (titre seulement dans `NOTES-DIEGO.md`).
