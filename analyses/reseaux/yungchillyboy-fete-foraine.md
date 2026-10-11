# yungchillyboy — fête foraine de nuit (réseaux, 13 s)

_Fiche du 2026-10-11 (session 12, référence ajoutée par Diego dans `videos/reseaux/`). Source : `video-by-yungchillyboy-jxaexg.mp4`, 1276x718, 30 i/s, VP9, 13,0 s. Toutes les images vues (390), spectrogramme, calage, écarts signés. Rien écouté._

## Intention
Faire sentir l'ivresse lumineuse d'une fête foraine la nuit : manèges, grande roue, néons violets et bleus, foule. [VU SUR IMAGES]

## Forme [mesuré, chaque image]
- **28 coupes en 13 s, médiane 0,47 s.** Trois régimes :
  1. **0-0,47 s : sept éclats de 1 à 3 images** (foule, enseigne « ACADA' », manège bleu, balancier, traînée violette) ; ce sont **des plans du film lui-même, qu'on reverra plus loin** (ACADA' à 6,4 s, balancier à 7,07 s, manège bleu à 7,80 s) : une bande-annonce du film en un demi-temps.
  2. 0,5-6,4 s : plans de 0,5 à 1,8 s reliés par des **transitions-masques** : titre rose posé sur la grande roue (0,5-1,6 s), volet horizontal qui révèle le plan suivant par une bande (1,63-1,97 s), filé (2,1-2,3 s), **petits rectangles qui découvrent le plan suivant par morceaux** (4,53-4,87 s), éclats en négatif (6,30-6,43 s).
  3. **7,07-12,1 s : huit plans d'exactement 21 à 22 images (0,72 s)**, coupés secs, un par temps à 83 BPM ; dernier plan large tenu 0,83 s.
- Pas de texte hors du titre ; pas de voix (Whisper : une phrase, sans doute des paroles de la chanson).

## Choix par domaine
- **Rythme** : l'ouverture la plus dense, puis des transitions, puis une cadence métronomique ; trois régimes en 13 s. [VU SUR IMAGES]
- **Couleur** : nuit noire, néons violets, bleus, verts ; une seule matière (néon sur noir) pour tous les plans, ce qui rend lisibles les plans de 0,7 s.
- **Effets** : négatif, traînée de lumière, volet, masques rectangulaires ; la mise en lumière des silhouettes de la foule (5,4-6,0 s) en blanc brûlé.
- **Son** : chanson lente (83 BPM détectés, cohérent avec la cadence des plans). Intégré -14,1 LUFS, LRA 3,8 LU, crête -1,5 dBFS.
- **Calage** (28 coupes vues) : à ±1 image d'une attaque forte 9 % (hasard 17 %), **à ±2 images 74 % (hasard 33 %, 95e centile 61 %)** ; sur les temps à ±2 images 52 % (hasard 17 %). L'écart signé explique ce paradoxe : **à partir de 3,4 s, 17 coupes sur 17 tombent 1 à 2 images AVANT l'attaque** (écart médian +1,1 à +1,9 image, signe constant). Le monteur coupe **juste avant** le temps. [mesuré]

## Confirme, contredit, complète
- **Contredit** « personne ne coupe sur les temps plus qu'au hasard » (synthèse de phase 2) : calage net, avec une avance constante de 1 à 2 images (33 à 66 ms).
- **Corrige** la table SFX de `montage-kinetic-editing` dans son esprit : la règle « crête sur la coupe » vaut pour un son posé sur l'image ; quand c'est la coupe qu'on pose sur la musique, ce monteur la met **1 à 2 images avant** l'attaque, jamais après. À confronter avec pasalu (0 image) et l'équipe de France (+0,3 image).
- **Complète** R1 « hook 0-3 s » : **ouvrir par un éclat de 0,5 s fait des plans du film à venir** (promesse visuelle), puis ralentir.
- **Confirme** « une matière par univers » (`montage-couleur-et-intention`) : néon sur noir partout.

## Principes transférables
1. **Ouvrir par une bande-annonce de 0,5 s** : 5 à 7 éclats de 1 à 3 images tirés de la suite.
2. **Finir par une cadence fixe** (un plan par temps) après un passage plus libre : la régularité arrive comme une résolution.
3. **Couper 1 à 2 images avant l'attaque** quand la coupe suit la musique.
4. **Transitions-masques** (bande, rectangles) qui découvrent le plan suivant par morceaux.

## Ce que Diego en a dit
Retour du 2026-10-11 sur le dossier : « beaucoup de kinétique, mais pas que ».

## Doutes
- L'avance de 1 à 2 images pourrait venir du décalage audio de l'encodage (AAC) ; mais pasalu, traité par la même chaîne, donne +0,1 image : l'avance est donc dans le montage. [mesuré, non écouté]
- `flash_check.py` : ÉCHEC (23 flashs, pire seconde 6), surtout dans l'ouverture (éclats de luminances très différentes) et aux négatifs de 6,3 s.
