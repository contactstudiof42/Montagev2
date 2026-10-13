---
name: montage-couleur
description: La couleur du rush log au look — gestion des couleurs (Rec.709, Rec.2020, sRGB, P3, ACES, ACEScct, log caméra S-Log3, LogC, V-Log, LUT techniques et de look, OCIO, CST, RCM, tags, gamma 2.4 ou 2.2) et intention (palette, look, contraste, densité, peau, blancs, noirs, teal & orange, changer de look en cours de film). Mots d'un réalisateur, d'un client ou d'un étalonneur : « quelle couleur pour ce film ? », « le look fait cheap », « c'est fade », « c'est laiteux », « les blancs sont brûlés », « trop saturé », « plus chaud / plus froid / plus dense », « ça fait filtre », « l'image est délavée », « c'est grisâtre », « mes couleurs changent à l'export », « la LUT ne rend pas pareil », « on étalonne dans quel espace ? ».
---

# Couleur : du rush log au look

_Créé le 2026-10-13 (audit 2) en fusionnant `montage-couleur-et-intention` et `montage-couleur-pipeline` : l'erreur du film de mariage est née entre les deux (une conversion qui tassait les blancs, jugée comme un look). Chaque règle cite l'erreur qui l'a gagnée ou le mot de Diego qu'elle porte. Savoir de l'intention (films mesurés, maquettes, méthode, mots entendus, clichés) : [intention.md](intention.md) ; savoir du pipeline (choisir son pipeline, recettes, écarts entre logiciels) : [pipeline.md](pipeline.md). Versions d'avant : `archives/audit-2/skills/montage-couleur-et-intention/` et `montage-couleur-pipeline/`._

**Fait foi sur** : la chaîne de couleur (espace, log, conversion, LUT, tags) et le sens de la couleur (palette, look, peau, noirs, blancs). Nœuds et API de Resolve : `montage-resolve` ; capter la lumière au tournage : `montage-preparation-tournage-vfx` ; tags et contrôle à l'export : `montage-loudness-livraison` ; jugement côte à côte : `montage-regard`.

## 1. Une conversion n'est pas un look
Une conversion log → Rec.709 n'est qu'un point de départ. Un look choisit le contraste, la densité des noirs, la palette, et sépare les teintes ; il est le même sur tous les plans, se règle sur 6 images avant le montage et se juge côte à côte avec la référence (`montage-regard`). La lisibilité d'un plan sombre se règle sur l'info à voir (le visage, l'objet), pas en relevant tout le plan. (Gagnée : V2 du film de marque kinetic, LUT technique seule et plans éclaircis, « catastrophique », « lumineuse, plate, sans contraste » ; récidive au mariage : V3b laiteuse, dominantes posées, « rien n'est séparé » selon le DA.)

## 2. Garder les hautes lumières en convertissant
La latitude du log se perd dans une conversion mal choisie : une LUT de tirage ou une épaule trop basse tasse la robe, le ciel ou le produit en un blanc sans matière, même quand aucun pixel n'atteint 250. Ce qui a tenu sur du S-Log3 : une conversion à épaule longue (ni la LUT de la carte, ni une émulation de tirage), l'exposition par plan en CDL sur le même nœud (le CDL agit avant la LUT : 1 diaph ≈ 0,077 en S-Log3), vérifiée dans Resolve à 0,5/255 de la prévision (`labo/couleur/look_mariage_v4.py`). [TESTÉ EN CONDITIONS RÉELLES 2026-10-12, validé par le directeur artistique, pas encore par Diego] (Gagnée : V3b du film de mariage, ma LUT maison, passage Cineon et tirage, épaule à 0,62.)

## 3. Séparer les teintes, mesurer ce qui compte
- **Des points témoins** (peau, objet blanc, accessoire coloré, fond) mesurés en OkLCh avant de juger : une peau, un blanc et un décor qui tombent dans la même teinte font « une bouillie », même avec de bons noirs. Corriger la balance avant le look (une lumière tungstène peut être chaude **et** magenta : refroidir seul rend la peau plus rose) ; puis désaturer les ombres et les hautes lumières, plafonner la chroma de la peau, réduire la dominante du décor. (Gagnée : « une bouillie de pixels », « trop pâté de couleurs », V3 du film de marque.)
- **La couleur des noirs** se vérifie amplifiée (×6), pas seulement leur luminance : deux refroidissements cumulés donnent des noirs bleu canard invisibles en vignette.
- **Un blanc** : la part de pixels ≥ 250 n'est qu'un indice ; le jugement se fait côte à côte avec la référence, en pleine résolution (`montage-regard`, liste maître, point 7). (Gagnée : au mariage, 0 % à 250 sur une robe sans matière.)
- **Les couleurs clés** (peaux, blancs réels, couleur de la marque) restent constantes d'un plan à l'autre : liste maître de `montage-regard`, point 6 (Diego, V5 du film de marque).

## 4. Changer de look en cours de film
Par séquence ou même entrelacé : « pourquoi pas, tout est possible, mais il faut que ça ait un sens, que ce soit justifié. Et pas justifié de manière bullshit comme une analyse filmique : il faut qu'on ressente pourquoi il se passe ça. » (Diego, 2026-10-12.) Test : le changement se sent-il sans explication (un souvenir, une émotion qui monte, un autre temps) ? S'il faut l'écrire pour qu'on le comprenne, c'est un filtre.

## 5. Quand le brief ne dit rien
La hiérarchie du goût (`CLAUDE.md`) s'applique : d'abord le look par défaut de Diego (`GOUTS.md` : « quand je n'ai pas d'idée ou que je dois livrer une vidéo rapidement, je mets du film look ») ; ma proposition (images basses et denses, environnement froid, peau protégée, une seule chaleur méritée) seulement comme variante : c'est mon goût.

## 6. Les pièges de la chaîne (chacun a mordu, au labo ou en projet ; détail dans [pipeline.md](pipeline.md))
- Une seule transformation d'entrée : Resolve en RCM convertit déjà ; une LUT log → 709 en plus surcontraste.
- Une LUT attend une entrée précise : une LUT de tirage (Kodak 2383, Fuji 3513) attend du Cineon log, et sur du Rec.709 elle éclaircit et bleuit ; une LUT LogC3 sur du S-Log3, ou une LUT 709 sur du log, donne un contraste et une saturation faux. Une LUT 3D est bornée à 0-1 : jamais sur du linéaire.
- Tags : un fichier sans `color_primaries / transfer / matrix` est lu au hasard ; toujours taguer et vérifier (`ffprobe`) ; plage vidéo ou pleine : vérifier `color_range`.
- Gamma 2.4 contre 2.2 : étalonné en 2.4 et vu en 2.2, l'image paraît délavée dans les ombres ; choisir la cible et l'écrire.
- Un look qui sort la peau de la ligne chair au vectorscope est trop poussé.
- Dans Resolve, Fusion passe avant le nœud de couleur (une couleur posée dans Fusion traverse la LUT de look) ; une LUT se pose seulement depuis le dossier de LUT de Resolve (`montage-resolve`).
