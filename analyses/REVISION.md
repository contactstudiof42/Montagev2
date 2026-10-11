# Passe de révision (étape 7 de `PROMPT-PHASE-2.md`)

_Ouverte le 2026-10-11 (session 9). Une ligne par vidéo à revoir : ce que les outils et leçons apparus après son analyse peuvent changer. On mesure d'abord, on relit la fiche ensuite. Chaque fiche révisée reçoit une section « Révision »._

## 1. Outils et leçons, par session d'apparition
| Session | Outil ou leçon | Ce qu'il peut changer |
|---|---|---|
| 1 | coupes fusionnées dans le sombre ; fausses coupes de lumière | nombres de plans, plans longs, pics |
| 2 | `verif_plan.py` ; `HDR=1` ; `calage.py` (contre le hasard) ; `coupes_parole.py` | plans longs, couleur des sources HDR, calage, parole |
| 3 | demucs pour confirmer un calage ; copie éclaircie (vidéo très sombre) ; `verif_plan.py` lit la fréquence ; action accélérée | calages, comptes dans le noir |
| 4 | calage sur musique séparée ; Whisper invente et boucle | calages sur mixage, transcriptions |
| 5 | `whisper -mc 0` ; parole sous musique → voix séparée ; générique monté ; cartons sur noir | transcriptions longues, parole, densité de fin |
| 6 | `qc_livraison.sh` ; amorce au premier plan sur tuile | livrables, alternances |
| 7 | `verif_plan.py` sur tout plan de nuit > 60 s ; voix séparée contre mixage | comptes de nuit, parole |
| 8 | `SEUIL=haut`, `spectro_coupes.py` ; « pendant la parole » ne distingue pas un style, l'air oui | tous les pourcentages de parole |
| 9 | séries de « plans » à la durée minimale = détecteur saturé ; retirer logos et générique | médianes, pics |

## 2. Vidéos à revoir et mesure à relancer
| Vidéo (session d'analyse) | À relancer | État |
|---|---|---|
| Le Dîner de cons (2) | parole : voix séparée `SEUIL=haut` + spectrogramme | **fait (session 9)** : 1 corrigée, 2 confirmées |
| Interstellar (1) | `verif_plan.py` sur les plans longs sombres ; séries saturées ; générique | **fait (session 9)** : 3 confirmées |
| Joker (1-2) | séries saturées : aucune (0 sur 1 101) ; calage des escaliers : 13 coupes seulement, mesure trop petite pour être refaite utilement | **vérifié (session 9)**, rien à changer |
| Whiplash (2) | plans longs (`verif_plan.py` + tuile) ; séries saturées ; calage sur musique séparée (fait sur mixage) | **fait (session 9)** : 3 confirmées, 1 corrigée, 1 nouvelle |
| Mad Max: Fury Road (3) | séries saturées : une seule (5 plans, 27:45) ; générique à 1:52:58, après le final cité | **vérifié (session 9)**, rien à changer |
| adidas « Backyard Legends » (4) | parole : `SEUIL=haut` + spectrogramme (la mesure de session 4 était déjà sur voix séparée) | **fait (session 9)** : 1 confirmée, 1 corrigée |
| Qui est l'imposteur (5) | parole : `SEUIL=haut` + spectrogramme | **fait (session 9)** : 1 confirmée, 1 corrigée |
| POPCORN (5) | parole : `SEUIL=haut` + spectrogramme | **fait (session 9)** : 1 confirmée, 1 corrigée |
| Boxho (5) | parole : spectrogramme (pas de fond musical) | **fait (session 9)** : 1 confirmée, 1 corrigée |
| Toutes les transcriptions (27) | boucles et phrases fantômes (`uniq -c`, « Sous-titrage… ») | **fait (session 9)** : boucles dans adidas (×22, 4:44-5:02), Crunch Creator (×18, 1:31-1:59), YggTorrent (générique, déjà noté), KAIZEN (×19, 1:55:19-1:55:41, malgré `-mc 0`) ; **aucune fiche ne cite ces lignes**, aucune conclusion touchée |
| Clips (3-4) | séries saturées (Ziak éclairci) ; parole sans objet | à vérifier vite |
| Hirsingen (6) | parole : voix séparée + spectrogramme | **fait (session 9)** : 1 confirmée, 1 corrigée |
| Fou rire (6) | série saturée signalée à 1:59-2:02 : tuile à 10 i/s + bandes à 25 i/s | **fait (session 9)** : 1 confirmée, 1 corrigée (la « rafale de panique » est un seul plan porté de 4,8 s) |
| La Haine, Avengers, Forrest Gump (7) | parole si citée ; générique de fin | à vérifier vite |

## 3. Bilan chiffré (mis à jour à chaque vidéo révisée)
| Vidéo | Conclusions vérifiées | Confirmées | Corrigées | Nouvelles |
|---|---|---|---|---|
| Le Dîner de cons | 3 | 2 | 1 | 0 |
| Interstellar | 3 | 3 | 0 | 0 |
| Whiplash | 5 | 3 | 1 | 1 |
| adidas « Backyard Legends » | 2 | 1 | 1 | 0 |
| Qui est l'imposteur | 2 | 1 | 1 | 0 |
| POPCORN | 2 | 1 | 1 | 0 |
| Boxho | 2 | 1 | 1 | 0 |
| Hirsingen | 2 | 1 | 1 | 0 |
| Fou rire | 2 | 1 | 1 | 0 |
| **Total** | 23 | 14 | 8 | 1 |

**Lecture provisoire (session 9)** : une correction sur les images (Fou rire : fausse rafale sur un plan porté flou, trouvée par le comptage des séries saturées). Sur les mesures de parole, **tous les pourcentages de l'outil étaient faux** (7 sur 7, toujours trop hauts, de 6 à 36 points), **toutes les conclusions qualitatives tiennent** (qui coupe au milieu des phrases, qui attend la fin). Plans longs et calage : 8 conclusions sur 9 confirmées. Le regard « à l'œil » sur images tient ; le chiffre automatique sur la parole ne tient pas sans spectrogramme.
