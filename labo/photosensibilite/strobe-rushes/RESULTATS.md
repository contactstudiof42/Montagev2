# Rushes à stroboscope : les rendre livrables (session 15, 2026-10-10) [TESTÉ EN LABO, rush synthétique]

Question (examen n°8) : un teaser de festival doit utiliser des rushes de la dernière édition, où le stroboscope de scène flashe à 8 Hz. Peut-on les livrer (WCAG 2.3.1 : au plus 3 flashs par seconde, fenêtre locale 1/3 × 1/3) et que coûte chaque traitement à l'image ?

Rush : `strobe.py` fabrique 8 s à 25 i/s, 360×640 : foule en silhouettes qui saute à 2,3 Hz (138 BPM), lasers lents, strobe blanc plein cadre. Deux cas : strobe **calé** (1 image sur 3, 8,3 Hz) et strobe **libre** à 7,7 Hz capté avec un obturateur 1/50 s (le cas réel : rien n'est synchronisé). Mesures : `flash_check.py` ; `pic` = luminance du 95e centile des images / médiane (ce qui reste du coup de strobe ; 1 = effacé, 20 = intact) ; `mouv` = variation moyenne d'image à image dans la foule (ce qui reste du mouvement).

| Traitement | Strobe calé 8,3 Hz | pic | mouv | Strobe libre 7,7 Hz | pic | mouv |
|---|---|---|---|---|---|---|
| brut | 9 flashs/s, **ÉCHEC** | 20 | 0,231 | 4/s, **ÉCHEC** | 20 | 0,112 |
| `tmix=frames=3` (moyenne de 3 images) | 0, OK | 1,0 | 0,008 | 2/s, OK limite | 4,2 | 0,022 |
| `tmix=frames=5` | 9/s, **ÉCHEC** | 1,0 | 0,047 | 2/s, OK limite | 2,1 | 0,024 |
| `deflicker=size=9` | 8/s, **ÉCHEC** | 1,1 | 0,037 | 0, OK | 1,6 | 0,022 |
| `deflicker=size=25` (1 s) | 4/s, **ÉCHEC** | 1,2 | 0,035 | 0, OK | 1,0 | 0,020 |
| **tirage par saccade** (1 image tenue 8 images, 3,1 /s) | 2/s, OK | **20** | 0,028 | 2/s, OK | **20** | 0,011 |
| moyenne 3 + saccade de 4 | 0, OK | 1,0 | 0,006 | 3/s, limite | 4,3 | 0,020 |

(Les lignes « tirage sombre / allumé » des tables brutes choisissent les images d'après la période 3 : valables seulement pour le strobe calé, où elles donnent 0 flash ; pour le strobe libre il faut choisir les images à la main.)

## Ce que ça apprend
1. **Ce que la caméra enregistre d'un strobe dépend de la rencontre entre sa fréquence et l'obturateur** (repliement) : le même 8 Hz de scène donne 9 ou 4 flashs/s dans le fichier. On ne sait pas d'avance : **mesurer chaque rush**, pas la fiche technique de la scène.
2. **Une moyenne temporelle ne marche que par coïncidence de période** : `tmix=3` efface un strobe de période 3 et échoue à 5 ; sur un strobe libre elle laisse un battement (pic 4) juste sous le seuil. `deflicker` d'ffmpeg (moyenne glissante) échoue sur le strobe calé même sur 1 s. Ces filtres sont des **gommes**, pas des solutions : quand ils passent, le strobe a disparu (pic ≈ 1) et la foule devient une bouillie traînante (mouv ÷ 10).
3. **Le seul traitement qui garde le coup de strobe intact et passe toujours : le tirage par saccade** (step-printing : une image tenue 8 images à 25 i/s, soit ≤ 3,1 changements/s). Le prix est le mouvement, devenu saccadé. C'est une **esthétique** (Wong Kar-wai / Christopher Doyle dans *Chungking Express*, d'après les sources écrites ; non vérifié ici), pas une rustine : à décider, pas à subir.
4. Variante de direction : **choisir à la main** quelles images allumées garder pour que les flashs tombent sur des temps du morceau (138 BPM = 2,3 temps/s, sous le seuil) : le strobe devient **le métronome du montage** au lieu d'un danger. À tester sur un vrai rush (phase 2 ou rush CC0).
5. Hors traitement : **couper avant le 4e flash** d'une seconde quelconque ne suffit pas si le plan dure plus d'une seconde ; un plan brut de strobe à 8 Hz n'est livrable qu'en dessous de ~0,4 s (3 flashs) — et encore, à mesurer avec le plan précédent et suivant dans la fenêtre glissante.

Limites : rush synthétique (strobe plein cadre, binaire) ; un vrai strobe a un déclin, un rolling shutter coupe le flash en bandes (flash partiel sur une partie du cadre : la fenêtre locale 1/3 peut alors échouer même si la moyenne passe). `flash_check.py` n'est pas un test Harding.

## Planche regardée (`planche-7_7hz.png`, images 25-40 : brut / `tmix=3` / saccade)
- **Brut** : deux flashs blancs à 2 images d'écart ; la foule devient grise pendant le flash : c'est là que le strobe « révèle » les corps.
- **Moyenne** : les deux flashs fondent en **un voile laiteux de 6 images** : ni noir ni coup, le contraste est tué. Visuellement le pire : ça ressemble à une erreur d'exposition, pas à un choix.
- **Saccade** : sur cette fenêtre, les images tenues sont toutes sombres : **aucun flash ne survit**. Le coup de strobe ne reste que là où une image tenue tombe sur un flash : en tirage automatique, c'est le hasard qui décide où tapent les flashs. D'où le point 4 : **choisir à la main** les images tenues (allumées sur les temps voulus).
