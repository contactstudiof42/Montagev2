# Benefit — deux pubs réseau verticales (« You CAN Have It All »)

_Fiche ouverte le 2026-10-11 (phase 2, session 6, projet Studio F42 n°1 et 2). **État : complète** (deux films, vus en entier à 2 images/s, 16 images pleine définition, coupes recomptées avec `verif_plan.py`, loudness et true peak mesurés sur les fichiers livrés, calage contre le hasard). Sources : `BENEFIT PUB RESEAU.mov` (HEVC 2160×3840, 25 i/s, 23,2 s, PCM 24 bits) et `BENEFIT PUB RESEAU 2.mp4` (H.264 1080×1920, 25 i/s, 26,2 s, AAC). Pas de rushes : je ne peux pas savoir ce qui a été tourné et écarté ; quand une correction dépend des rushes, je le dis._

**Lu avant l'analyse** : `videos/projets-f42/A-LIRE.md`, `montage-regard` (grille), `montage-formats` (pub, vertical réseaux), `montage-kinetic-editing` (durées, SFX, checklist), `montage-loudness-livraison`, bilan des pubs de référence (`RAPPORT.md`). Aucun commentaire de Diego sur ces projets (`NOTES-DIEGO.md` ne donne que les titres).

## Intention et contraintes probables
- **Intention** : une campagne pour l'anti-cernes « The POREfessional » de Benefit, traitée comme une **comédie romantique en un plan de situation** : « You CAN Have It All » (le gâteau, le regard du serveur, les roses) et le produit au générique (« Starring The POREfessional Concealer »). Deux épisodes, deux femmes, deux décors.
- **Contraintes probables** [DÉDUIT] : une journée de tournage par décor ou moins (un seul lieu par film, 7 à 9 plans), une comédienne et un figurant, pas de voix, pas de texte à traduire hors du titre ; diffusion en Reels / TikTok, muet probable.

## Forme [mesuré]
| | Benefit 1 (café) | Benefit 2 (escalier, roses) |
|---|---|---|
| Durée | 23,2 s | 26,2 s |
| Plans | 9 (2,2 / 2,2 / 5,3 / 1,5 / 1,9 / 2,9 / 2,3 / 1,8 / 3,1 s) | 7 (6,1 / 2,4 / 1,9 / 1,8 / 2,2 / 6,0 / 5,7 s) |
| Titre sur flou | 0-4,4 s (deux plans) | 0-4,5 s (le plan 1, avant que le point arrive) |
| Produit lisible | jamais en gros plan : tube blanc et rose sur la table (13-19 s), petit dans le cadre | **insert de 2,2 s** (12,3-14,4 s) : tubes plantés dans le bouquet, carte « Mon chéri, You blur me away — XOXO, Benefit » |
| Logo « benefit » | 20,6-23,2 s, sur l'image qui se floute | 20,4-26,2 s, sur l'escalier qui se floute puis s'assombrit |
| Son | musique seule (aucune voix), 172 BPM | même tempo (même morceau probable) |
| LUFS intégré / LRA | -14,5 / 3,1 LU | -14,7 / 3,3 LU |
| True peak | **-0,6 dBTP** | **0,0 dBTP** |
| Calage sur la musique (contre le hasard) | attaques 25 % (hasard 14 %), temps 25 % (19 %) : hasard | attaques 17 % (19 %), temps 50 % (40 %) : hasard |

Le détecteur avait raté une coupe dans Benefit 2 (8,5 s, même décor, même lumière) ; `verif_plan.py` l'a trouvée. Le plan de 6,0 s (14,4-20,4) est bien un seul plan (tuile à 4 images/s : elle soulève le bouquet, la caméra suit).

## Ce qui marche (avec la preuve)
1. **Le flou est l'idée, et il ferme la boucle** (Benefit 2) : le titre apparaît sur l'escalier flou, **le point arrive et révèle la comédienne qui descend** (0-6,1 s), et le logo finit sur l'image qui se floute à nouveau (20,4-26,2 s). Le produit promet de « flouter » les pores, la carte du bouquet le dit (« You blur me away ») : **la forme dit le bénéfice**. C'est le meilleur moment des deux films. [VU SUR IMAGES]
2. **Le produit est dans le cadeau** (Benefit 2, 12,3-14,4 s) : les tubes sont des tiges du bouquet. Le principe des pubs de référence « le gag porte le bénéfice » est tenu : si on retire le produit, le bouquet n'est plus un message de la marque. [VU SUR IMAGES]
3. **La marque est un objet du décor dès les premières secondes** (Benefit 1 : « benefit » imprimé sur le plateau de la table, 2,2-4,4 s, et sur la tasse) ; le nom ne vient qu'à la fin. Exactement ce que font les sept pubs de référence de Diego (la marque comme lieu ou costume, le nom en signature). [VU SUR IMAGES]
4. **Une couleur par film, tirée de l'emballage** : rouge et blanc à carreaux, rose du gâteau (café) ; roses rouges, robe blanche, vert du jardin (escalier). Les deux films se reconnaissent comme une campagne : même titre en script blanc, même fin floue, même musique. C'est un **dispositif répétable** (principe Specsavers de `montage-formats`). [VU SUR IMAGES]
5. **Benefit 2 a un vrai dessin de durées** : long (révélation, 6,1 s) → court (2,4 / 1,9 / 1,8 / 2,2 s, l'arrivée du bouquet) → long (la réaction tenue, 6,0 s, puis la sortie, 5,7 s). Une transition tournée (le feuillage au premier plan qui balaie le cadre, 6,1-8,5 s) relie le large au gros plan. [VU SUR IMAGES]
6. **Le niveau est juste pour le réseau** : -14,5 et -14,7 LUFS intégrés (cible -14). [mesuré]

## Ce qui pourrait être meilleur, et comment
### Montage (corrigeable avec les mêmes rushes)
1. **Les 4,4 premières secondes sont floues, dans un format où les 2 premières décident** (`montage-formats` : « premier écran = tout » ; `montage-kinetic-editing` : « plan qui commence dans le noir ou vide » est un trait amateur). Dans Benefit 2, le flou est l'idée : garder la mise au point, mais **la faire arriver vers 1,5-2 s** (le titre peut rester sur l'image nette). Dans Benefit 1, deux plans flous de 2,2 s se suivent sans révélation : **ouvrir sur le café net** (le serveur qui arrive) et poser le titre dessus.
2. **Benefit 1 ne relie pas le produit à ce qui arrive** : l'ordre monté est service (4,4 s) → bouchée (9,7 s) → sourire du serveur (11,2 s) → **elle se met du produit** (13,1 s) → elle salue (18,3 s). Le regard du serveur arrive **avant** le produit : on ne peut pas lire « grâce à l'anti-cernes ». Le gâteau paraît intact à 14 s et à 19 s alors qu'elle y a mordu à 10,4 s (bouchée simulée ou plan tourné avant) : **l'ordre de tournage n'impose pas l'ordre monté**, on peut mettre le geste du produit avant l'arrivée du serveur. C'est la correction la plus importante des deux films (critère « liaison » de la grille : la cause manque).
3. **Benefit 1 a des durées presque uniformes** (huit plans sur neuf entre 1,5 et 3,1 s) : rien n'est tenu, ni la réaction du serveur (1,9 s) ni le clin d'œil final (1,8 s). Tenir **un** plan de réaction 3 à 4 s (le sourire du serveur, ou son regard à elle quand il se retourne), comme Benefit 2 tient la sienne.
4. **True peak à -0,6 et 0,0 dBTP** : au-dessus du -1 dBTP recommandé ; le ré-encodage AAC des plateformes peut écrêter. Un limiteur à -1 dBTP en fin de chaîne, sans toucher au niveau intégré (`montage-loudness-livraison`).
5. **Fin du son de Benefit 2** : la musique est encore à -19 LUFS momentané sur la dernière image (Benefit 1 descend de -14 à -27 en 0,8 s). Fin de morceau sèche ou coupe ? Je ne l'ai pas écouté ; si c'est une coupe, un fondu de 0,5 à 1 s sous le logo, ou couper sur un temps fort du morceau.
6. **Lisibilité du titre** : script blanc fin ; « Starring The POREfessional Concealer » passe sur le plateau clair de la table (contraste estimé à environ 3:1, mesure grossière sur une zone, sous le 4,5:1 des recommandations d'accessibilité). À la taille d'un téléphone, une ombre portée douce ou une zone plus sombre derrière le texte suffit ; garder la police (elle fait « générique de comédie romantique »).

### Tournage (à préparer autrement la prochaine fois)
1. **Aucun gros plan de peau dans les deux films** : le bénéfice (pores floutés, teint uniforme) n'est jamais montré. Un insert macro du geste sur la peau, 1 à 1,5 s, lumière rasante douce. Si cet insert existe dans les rushes, c'est une correction de montage.
2. **Benefit 1 n'a pas d'insert produit** : le tube est petit sur la table. Tourner le produit dans le décor en gros plan (comme le bouquet de Benefit 2) ; le café le permettait (le gâteau rose, la tasse marquée).
3. **Tourner la cause et l'effet séparément** (le geste du produit, puis le regard qu'il provoque) pour avoir le choix de l'ordre au montage.

## Grille (`montage-regard`, 0 à 3)
| Critère | Benefit 1 | Benefit 2 | Preuve |
|---|---|---|---|
| Intention | 1 | 3 | 2 : le flou et la carte disent « blur » ; 1 : le produit n'est pas la cause de la scène |
| Lisibilité | 1 | 2 | 4,4 s de flou au début des deux ; titre à environ 3:1 sur la table (1) |
| Liaison | 1 | 2 | 1 : regard avant produit ; 2 : feuillage qui balaie, bouquet qui arrive |
| Rythme | 1 | 3 | 1 : 1,5 à 3,1 s partout ; 2 : long / courts / long |
| Composition | 2 | 3 | sujet centré dans le 9:16, lisible ; 2 : escalier en perspective centrale |
| Cohérence | 3 | 3 | même titre, même fin floue, même musique, une couleur par décor |
| Couleur | 3 | 3 | rouge-rose-blanc tirés de l'emballage |
| Mouvement | 2 | 3 | 2 : mise au point qui révèle |
| Originalité | 2 | 2 | le générique de comédie romantique pour un produit est une idée ; le flou au début est un cliché beauté |
| Justesse | 2 | 2 | 4 s de titre de trop au début dans les deux |

**Verdict** : Benefit 2 est **presque livrable** (lisibilité à 2 : raccourcir le flou d'ouverture, limiter le true peak). Benefit 1 **ne l'est pas en l'état** : intention et liaison à 1, corrigeables au montage si l'ordre des plans est libre (indice : le gâteau intact).

## Confirme, contredit, complète
- **Confirme** sur un projet du studio le principe des sept pubs de référence : la marque est un objet du décor dès le début, le nom à la fin ; et « le gag porte le bénéfice » (`montage-formats`), tenu par Benefit 2, manqué par Benefit 1.
- **Confirme** « personne ne coupe sur les temps plus qu'au hasard » (le studio non plus).
- **Complète** `montage-formats` (vertical) : **un flou d'ouverture n'est permis que s'il est l'idée** (révélation par la mise au point, en moins de 2 s) ; sinon il retarde le premier écran.
- **Complète** `montage-loudness-livraison` : le niveau intégré était juste, le true peak non. Le contrôle QC doit mesurer les deux (le studio a livré deux fichiers à -0,6 et 0,0 dBTP).

## Principes transférables (pour le studio)
1. **Quand le produit promet un effet visuel, en faire la forme du film** (flou → net → flou pour un produit qui « floute »).
2. **Le produit dans l'objet du récit** (des tubes dans un bouquet) plutôt qu'à côté (un tube sur la table).
3. **La cause avant l'effet** : dans une pub sans voix, l'ordre des plans est la seule phrase ; le geste du produit doit précéder ce qu'il provoque.
4. **Une campagne est un dispositif** : titre, fin, musique et couleur répétés ; chaque épisode change le décor et le cadeau.
5. **QC de livraison** : intégré -14 LUFS **et** true peak ≤ -1 dBTP sur le fichier encodé.

## Ce que Diego en a dit
Rien sur ces deux projets (titres seulement dans `NOTES-DIEGO.md`).
