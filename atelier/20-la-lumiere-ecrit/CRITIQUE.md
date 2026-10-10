# Pièce 20 « La lumière écrit » — critique (session 15)

Planches : 20 vignettes, une image sur 3, 0-2,4 s. `flash_check.py` sur chaque fichier.

| Version | Dispositif | Photosensibilité | Verdict |
|---|---|---|---|
| v1 (`v1-planche.png`) | saccade automatique, 1 image sur 12, tout figé | 2 flashs en 10 s, OK | **Échec d'intention** : sur les 2,4 premières secondes, aucune image tenue ne tombe sur un coup : **pas un nom, pas un corps révélé**. Le noir et les lasers figés. Le tirage automatique laisse le hasard écrire, et le hasard n'écrit rien. |
| v2 (`v2-planche.png`) | coups choisis sur les noires (2,13/s), coup tenu 3 images, nom qui persiste en fondu, tout figé entre deux coups | 21 flashs, **pire seconde 3 = la limite** | **Défaut de lisibilité au moment clé** : le nom blanc apparaît **dans** le coup blanc, il est noyé (« NUIT BASSE », « LUNE VIVE » invisibles dans les vignettes allumées). On ne le lit qu'après, dans le noir, pendant le fondu. La lumière n'écrit pas, elle efface. |
| v3 (`v3-planche.png`) | v2 + lasers qui continuent de bouger pendant les images tenues | idem | même défaut de texte ; la différence (monde figé ou non) ne se juge pas sur une planche : voir plus bas |
| **v4** (`v4-planche.png`) | v3 + le nom **en noir dans le coup**, qui s'inverse en blanc dans le noir (image rémanente) | idem, pire seconde 3 | **Lisible du coup jusqu'au fondu** : le nom est lu sur 12 images d'affilée, l'inversion noir → blanc ressemble à ce que fait l'œil après un éclair (la rémanence en négatif). C'est la première version où le titre de la pièce est vrai. |

## Grille
- **Intention servie ?** v1 non, v2-v3 à moitié (le nom vient après la lumière), v4 oui.
- **Lisibilité** : v4 ; mais un nom tenu 12 images (0,48 s) reste **sous le plancher ATAA de 16 images** ; à 128 BPM, pour respecter 16 images, il faut un coup toutes les noires pointées (17,6 images) ou un nom pour deux coups.
- **Rythme** : régulier, une noire par nom : sur 10 s, déjà monotone sur la planche (même cycle blanc → noir → fondu × 4). L'examen avait prévu de la variation (trou à la mesure 8, têtes d'affiche tenues une mesure) : indispensable, la pièce le confirme.
- **Composition** : les corps en gris sur blanc lisent bien en silhouettes ; les noms à des places qui changent (rupture de forme) fonctionnent, sauf quand ils tombent sur les têtes (« DJ TARMAC » en v4, vignette 9).
- **Justesse** : la v4 n'ajoute rien qui ne soit déjà dans la lumière (pas de whoosh, pas de shake) : un seul geste, l'inversion.

## Ce que la pièce a appris (et corrige l'examen n°8)
1. **Un texte clair qui apparaît dans un flash est invisible** : dans un coup de lumière, le texte doit être **sombre**, puis s'inverser dans le noir. Règle générale : le texte prend **la valeur opposée** à celle de l'image au moment où il apparaît, pas une couleur fixe.
2. **« Un coup par noire à 128 BPM » n'est pas 2,13 flashs/s avec de la marge** : la fenêtre glissante d'une seconde (25 images) attrape **3 coups** (25 / 11,7 = 2,13 → 3 débuts de coups possibles dans une seconde). `flash_check.py` : pire seconde 3, la limite exacte. Pour une marge : coups sur les noires pointées ou alterner coup de luminance et coup de teinte à luminance égale. L'examen n°8 se trompait en annonçant 2,13 « sous le seuil ».
3. **La saccade automatique ne peut pas porter une direction** (v1) : elle doit être montée image par image, comme un montage.
4. **Non jugé** : « choix ou bug » (l'hypothèse « si quelque chose continue de bouger, la saccade se lit comme un choix ») ne se voit pas sur une planche d'images fixes. À juger en mouvement en phase 2 sur les fichiers `atelier/rendus/20/v2.mp4` contre `v3.mp4` (régénérables par `piece.py`), ou par un regard humain.

Médias : tout est synthétique (numpy, police DejaVu Sans Bold, licence libre DejaVu / Bitstream Vera). Noms d'artistes inventés.

## v5-v6 : la structure de l'examen n°8 corrigée, avec le son (`v5.py`, `v5-planche.png`, `v6-planche.png`, `v5-onde.png`)
Structure (10 s, 128 BPM) : coup-titre (image 0) → 6 noms sur **noires pointées** (17,6 images) → **trou** d'une mesure (noir total, lasers coupés, le relais seul sur le 4e temps) → tête d'affiche. Son synthétique : kick 128 BPM (coupé dans le trou), un « relais » de 12-25 ms par coup (durées variées), impact sub 40 Hz sur la tête d'affiche.

| | v5 | v6 |
|---|---|---|
| Photosensibilité | 7 flashs, **pire seconde 2** (marge gagnée sur v2-v4 : 3) | idem, 2 |
| Loudness (MP4 AAC) | `loudnorm` seul : **-17,9 LUFS** (il n'atteint pas -14 sous contrainte de true peak avec des kicks impulsifs) ; boucle gain + limiteur 192 kHz (R6) : -21,5 → -16,0 → -15,1 → -14,7 → **-14,5 LUFS / -2,5 dBTP** en 5 passes | -14,5 / -2,5 en 1 passe (gain repris de v5) |
| Planche | **bug** : « OKAPI SOUND » apparaît comme nom secondaire **et** comme tête d'affiche (indice 0 de la liste réutilisé) : le sommet est déjà vu ; le coup de la tête d'affiche (3 images) **plus faible** que les secondaires, le sommet n'en est pas un | doublon retiré ; coup de la tête d'affiche **tenu 8 images** (un seul flash, mesuré) : 0,32 s de blanc, nom en noir énorme, puis inversion : c'est enfin le sommet |

Grille (v6) :
- **Intention** : servie : chaque nom a son coup, et le trou rend le dernier coup attendu.
- **Rythme** : les 6 noms sur noires pointées tombent à cheval sur les temps : **contre** le kick une fois sur deux (syncope). Sur la planche, rien ne le montre ; à l'oreille, c'est soit un groove, soit un décalage : à juger en phase 2. Hypothèse : la syncope sert les secondaires (ça avance) et le retour sur le temps (tête d'affiche sur le 1er temps de la mesure 5) fait arriver.
- **Justesse** : le trou de 1,9 s de noir total risque de faire croire à une fin ou à un bug sur un fil ; la v6 garde le relais seul sur le 4e temps pour dire « ça continue ». Non vérifiable sans regard humain.
- **Faiblesse qui reste** : les noms secondaires sont tous traités pareil (même taille, même cycle) : monotone sur 6, ce serait insupportable sur 20 ; varier taille et position selon la mesure (rupture de forme de la pièce 09), et la foule toujours la même (un seul rush synthétique).

Leçons :
1. **Le sommet doit être plus long, pas plus fort** : un seul flash tenu 8 images reste un seul flash pour WCAG (montée + descente) et pèse plus qu'un coup de 3 images, sans ajouter de risque. La durée de l'état clair est un levier libre ; le nombre de transitions ne l'est pas.
2. **Vérifier la liste des textes contre les doublons** avant tout rendu (la v5 a montré deux fois le sommet).
3. `loudnorm` en une passe sur un montage de 10 s à kicks impulsifs reste à -18 LUFS : confirmer la boucle R6 (`montage-kinetic-editing`), qui converge en ~5 passes.

## Après la fiche step-printing (`culture/step-printing-wong-kar-wai-et-autres.md`)
Chez Wong Kar-wai et Doyle, la saccade se combine à un **obturateur lent** : les images tenues portent des traînées. Mes images tenues sont nettes : c'est probablement ce qui ferait lire la v2 comme un bug. v7 à faire : flou de bougé accumulé dans chaque image tenue (moyenne des images de la noire précédente sur la foule seulement), contre v3 (lasers continus), à juger en phase 2.

## v7 / v7b : la traînée (`v4-v7-detail.png` : v4 nette / v7 8 poses à 1/25 s / v7b 32 sous-poses)
- **v7** (moyenne de 8 poses entières) : des **poses fantômes discrètes**, un écho façon chronophotographie, pas un flou. Ce n'est pas un raté : c'est une autre esthétique (fiche McLaren : quelques images d'écart = écho, corps multiplié).
- **v7b** (4 sous-poses par image) : la traînée devient presque continue, le flou d'un obturateur lent : la tête qui sautait laisse un sillage vers le bas. Photosensibilité inchangée (pire seconde 3, comme v2-v4 : coups sur les noires).
- Choix pour « la lumière écrit » : **l'écho (v7)** sert mieux un festival (la foule de soi, chaque corps multiplié par le coup) ; la traînée (v7b) dit seulement « vitesse ». À juger en mouvement (PLAN-TESTS 59) ; v8 : écho + noires pointées + 20 noms variés (BACKLOG 80).
- Coût : rendu numpy à 32 sous-poses par image ≈ 5-6 min pour 10 s (ne recalculer qu'une fois par noire la prochaine fois).

## v8 (session 16) : écho + 20 noms hiérarchisés, contre un témoin uniforme (`v8.py`, `v8-planche.png`, `v8-uniforme-planche.png`)
Planches : une image sur 6 (0,24 s), 14 × 6. Les deux versions gardent l'écho de la v7 (moyenne de 8 poses entières, calculée une fois par coup : rendu 40 s au lieu de 5 min) et les lasers continus.

| | v8 hiérarchisée | v8-uniforme (témoin) |
|---|---|---|
| Structure | titre → 7 noms « niveau 2 » un par coup, taille 30-46 px et place qui changent → 12 noms « niveau 3 » en 4 paquets de 3 (colonne, 20 px, gauche/droite alternés) → trou d'une mesure → tête d'affiche tenue 8 images → carton-liste 4 s | titre → 19 noms un par coup, même taille, même place → trou → tête d'affiche (pas de carton) |
| Photosensibilité (`flash_check.py`) | **12 flashs, pire seconde 2** | 20 flashs, pire seconde 2 |
| Durée pour les 19 noms | 5,6 s (images 47 → 187 + 4 paquets) | **13,3 s** |

Ce que montrent les planches :
- **Le témoin uniforme est un papier peint** : 19 fois le même cycle blanc → nom → fondu, toujours au même endroit ; le nom suivant tombe là où le précédent s'éteint, ce qui se lit comme un **compteur** ou un générique qui défile, pas comme une programmation. Sur la planche, l'œil cesse de lire vers le 6e nom (rangée 3). La tête d'affiche, malgré ses 54 px, arrive après 13 s de même chose : elle est moins attendue que dans la v8.
- **La hiérarchie raccourcit et respire** : 11 coups au lieu de 19 pour les mêmes noms, donc 40 % de flashs en moins **sans rien retirer** ; trois tailles = trois rangs lisibles d'un coup d'œil (seul / en paquet / énorme), c'est la règle d'affiche appliquée au temps.
- **Les paquets de 3 ne se lisent pas, ils se repèrent** : 0,7 s pour 3 noms courts. C'est acceptable seulement parce que le carton-liste suit (lecture de repérage, BACKLOG 82) : le défilé donne l'énergie, le carton donne l'information. Sans carton, les 12 noms du niveau 3 seraient sacrifiés : il faut le dire au client avec ce chiffre.
- **Défauts** : (1) après le 7e nom, 0,7 s de « HALOGÈNE » mourant en gris sombre avant le premier paquet (le dernier coup de la section tombe à l'image 170, la mesure suivante à 188) : un trou involontaire qui affaiblit le vrai trou de la mesure 7. Il faut caler la fin de section sur la barre (6 noires pointées + 1 noire, ou une noire pointée de plus). (2) Le carton-liste dure 4 s ; d'après la recherche de la session 15, trouver un nom dans 20 prend 3-4 s, conclure qu'il manque 6-7 s : **le carton doit durer 6 s** (film de 22 s) ou être doublé d'une sortie en carrousel. (3) Le « noir » du trou est un brun très sombre (couleur de base de la salle) : à vérifier sur un téléphone en luminosité basse, il peut lire « image » et non « noir ».

Grille : **intention** servie (la lumière écrit, chaque rang a sa forme) ; **lisibilité** : niveau 2 et tête d'affiche oui, niveau 3 en repérage seulement ; **rythme** : la v8 a une forme (seul, paquets, silence, sommet, liste), le témoin n'en a pas ; **justesse** : aucun effet ajouté, la hiérarchie fait le travail que le volume ne fait pas ; **originalité** : le carton-liste final est un passage obligé, assumé comme tel.

Leçons :
1. **Hiérarchiser une liste, c'est économiser des coups** : grouper le bas de l'affiche en paquets divise le nombre d'événements (et de flashs) sans retirer un nom. Une liste longue montée « un nom = un coup » est un compteur.
2. **Une section doit finir sur la barre** : un reste de 0,7 s entre la fin d'une section et la suivante fait un trou involontaire qui use le vrai silence.
3. Coût : calculer l'écho une fois par coup (cache) et non par image : 40 s pour 20 s de film.

À faire (v9) : fin de section calée, carton 6 s, son (kick + relais + impact, boucle R6), un « moment Muybridge » (la tête d'affiche en 4 phases côte à côte, fiche `culture/chronophotographie-marey-muybridge.md`) contre la trace superposée.
