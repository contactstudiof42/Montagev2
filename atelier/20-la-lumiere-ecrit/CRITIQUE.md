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
