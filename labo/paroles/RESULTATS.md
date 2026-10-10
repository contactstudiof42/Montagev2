# Labo paroles incrustées : lisibilité au téléphone (session 13, 2026-10-10) — [TESTÉ EN LABO, proxy OCR]

Question (BACKLOG 75, suite de la pièce 19) : quelle taille, quelle graisse et quel traitement (nu, ombre, boîte) pour qu'un vers incrusté en 9:16 survive à la ré-encode d'une plateforme et se lise sur un téléphone ?

**Méthode** (`lisibilite.py`) : fond agrandi et recadré en 1080×1920 ; deux lignes de texte (« Les vitrines me rendent / un type que je connais pas ») en Inter (OFL), centrées à 62 % de la hauteur (au-dessus de la zone d'interface basse) ; `drawtext` → H.264 **2,5 Mb/s** (ordre de grandeur supposé d'une ré-encode plateforme, non vérifié) → réduction à **360 px de large** (convention « téléphone à bout de bras » de l'atelier) → recadrage sur la bande du texte → **OCR tesseract (fra)** → **part des mots retrouvés**. Quatre fonds : `face` et `porte` (pièce 19 : nuit, sombre, flou), une **texture claire à haute fréquence** (automate cellulaire, pire cas : feuillage, foule, gravier au soleil) et un **uni clair** (mur, ciel). Durée : ~1,5 min pour 80 cas.

**Résultats** (`tableau.txt`, brut : `resultats.tsv`) — part des mots retrouvés, par taille de police en % de la hauteur :

| fond | traitement | 1,2 % | 1,6 % | 2,0 % | 2,6 % | 3,5 % |
|---|---|---|---|---|---|---|
| nuit (face) | Medium nu / ombre / boîte | 0 | 0,7-0,8 | **1** | 1 | 1 |
| nuit (face) | **Thin** nu | 0 | 0 | **0** | 1 | 1 |
| nuit (porte) | Medium, tous | 0,2 | 0,9-1 | 0,9-1 | 1 | 1 |
| texture claire | Medium nu / ombre | ≤ 0,1 | ≤ 0,1 | ≤ 0,1 | ≤ 0,1 | ≤ 0,1 |
| texture claire | boîte noire 55 % | 0 | 0,1 | 0,7 | 0,4 | 0,5 |
| texture claire | **boîte noire 85 %** | 0 | 0,1 | 0,7 | **1** | **1** |
| uni clair | Medium nu | 0,2 | 1 | 1 | 1 | 1 (**faux positif**, voir limites) |
| uni clair | ombre | 0 | 0,7 | 0,9 | 0,5 | 0,7 |

## Ce que ça dit
1. **Plancher : 2 % de la hauteur** (≈ 38 px en 1920, ≈ 13 px une fois vu à 360 px de large) en graisse Medium sur fond sombre. À 1,2 % (23 px), rien ne survit. **Les sous-titres « fins et élégants » ne passent pas** : l'Inter Thin disparaît jusqu'à 2 % compris (les fûts d'1 px sont mangés par la compression puis la réduction) et ne revient qu'à 2,6 %.
2. **Sur une texture claire et fine, ni le blanc nu ni l'ombre portée ne lisent, à aucune taille.** Seule une **boîte opaque (≈ 85 %) à partir de 2,6 %** garantit la lecture ; à 55 %, la texture traverse la boîte et casse les lettres.
3. **L'ombre portée n'aide jamais ici, et nuit sur fond clair uni** (0,5-0,9) : elle épaissit le contour en un halo gris que la compression barbouille. Contour net (`borderw`) à tester (non fait).
4. Sur fond de nuit, le traitement n'a pas d'importance : **c'est la taille et la graisse qui décident**.

## Limites (à ne pas oublier)
- **L'OCR n'est pas un œil.** Blanc sur uni clair (#E8E4DA, contraste ≈ 1,2:1) : l'OCR lit tout (binarisation adaptative), un humain ne lit rien (WCAG demande 4,5:1). Le proxy **surestime** la lisibilité des contrastes faibles et **sous-estime** sans doute celle d'un texte connu (on reconnaît un mot familier qu'on ne lirait pas lettre à lettre).
- Le score global (difflib) était faux sur fond texturé : l'OCR lit la texture comme des lettres (« LAPS AAA ») et noie le vers pourtant bien lu ; d'où le rappel de mots et le recadrage.
- Débit de plateforme supposé ; une seule police (Inter) ; images fixes (en mouvement, un texte se lit moins : temps de lecture à mesurer).

## Leçon artistique
Le texte incrusté est une **image**, et il se décide avec le plan : sur une nuit de clip, du Medium à 2-2,6 % de la hauteur suffit et reste discret ; sur un plan clair et chargé, **soit on change de plan** pour le vers qui compte, **soit on assume une boîte** (qui devient un parti pris graphique, pas une rustine). Le Thin « élégant » est un choix de bureau qui meurt au téléphone.

## Complément : contour net (`borderw=3`, noir) — même protocole (`STYLES=contour`, `resultats-contour.tsv`)
| fond | 1,2 % | 1,6 % | 2,0 % | 2,6 % | 3,5 % |
|---|---|---|---|---|---|
| nuit (face) | 0 | 0,3 | 1 | 1 | 1 |
| nuit (porte) | 0,3 | 1 | 0,9 | 1 | 1 |
| texture claire | 0 | 0,1 | 0 | 0,1 | 0,1 |
| uni clair | 0 | 0,3 | 0,6 | 0,9 | 0,9 |

**Non concluant, et je le dis** : le contour de 3 px ne sauve pas la texture claire selon l'OCR, mais tesseract est connu pour mal lire les lettres détourées (il est entraîné sur du texte imprimé plein). Les captions détourées des réseaux (style Hormozi) sont faites pour l'œil, pas pour l'OCR. **Le proxy n'est valable que pour comparer des traitements « pleins » (nu, boîte)** ; contour et ombre se jugent à l'œil, en phase 2 (PLAN-TESTS 56).

## Session 14 — paroles animées mot à mot en ASS (libass dans ffmpeg 6.1.1) [TESTÉ EN LABO]
**1. Le mot tombe-t-il à l'image voulue ?** (`ass_mot_a_mot.py`) Un vers de 8 mots, karaoké `\k` avec `SecondaryColour` transparente (le mot est invisible avant son temps, plein après), temps volontairement hors grille (0,63 s = 15,75 images à 25 i/s). Mots comptés image par image (projection des colonnes, mots séparés par leurs blancs).
- **24/24 à l'image attendue** à 25, 29,97 et 23,976 i/s : le mot apparaît sur la **première image dont l'instant est ≥ à son temps** (`ceil(t × cadence)`), jamais avant. La résolution de l'ASS est le **centième de seconde**, plus fine que l'image : la limite est la cadence, pas le format.
- Conséquence : un mot calé « sur la syllabe » apparaît **0 à 1 image après** elle (jusqu'à 40 ms à 25 i/s). Pour un mot qui doit frapper avec la voix (kinetic, accent), **anticiper d'une demi-image à une image** dans le fichier ; le seuil de perception d'un retard de l'image sur le son est de l'ordre de quelques dizaines de ms (valeur de mémoire, ITU-R BT.1359 : à vérifier avant de la citer).
- La mise en page du `\k` est **fixe** : les mots invisibles occupent déjà leur place, rien ne bouge quand ils apparaissent.

**2. Le « pop » (échelle 70 → 100 % en 120 ms à chaque mot) fait-il glisser la ligne ?** (`ass_pop.py`)
| mode | bord gauche du 1er mot pendant le vers |
|---|---|
| `ligne` : un seul événement, `\t` d'échelle par mot | **110 px d'amplitude, 28 positions** : chaque mot qui grandit élargit la ligne, libass la recentre, **toute la ligne glisse à chaque mot** |
| `calques` : un événement par mot, `\an2\pos` calculé une fois sur la ligne finale (largeurs par Pillow, même police) | **8 px** : le seul grossissement du mot autour de son centre ; les autres mots ne bougent pas |
- Leçon : **dans un vers animé, l'échelle d'un mot ne doit jamais changer la mise en page des autres.** En ASS : un événement par mot, positions figées sur la ligne finale. La ligne qui « respire » se lit comme un défaut (le regard perd sa place à chaque mot), sauf si on la veut ivre.
- En After Effects, les animateurs de texte transforment les glyphes **sans recalculer la mise en page** (de mémoire, [THÉORIQUE] : PLAN-TESTS 57) ; un MOGRT ou un sous-titre Premiere animé par mot est à vérifier.
- Reste : temps de lecture minimal d'un vers apparu mot à mot (dernier mot → coupe) ; contour à l'œil ; rendu sur un vrai débit plateforme.
