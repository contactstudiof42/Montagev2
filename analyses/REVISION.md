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
| Joker (1-2) | calage des escaliers sur musique séparée ; séries saturées | à faire |
| Whiplash (2) | plans longs (`verif_plan.py` + tuile) ; séries saturées ; calage sur musique séparée (fait sur mixage) | **fait (session 9)** : 3 confirmées, 1 corrigée, 1 nouvelle |
| Mad Max: Fury Road (3) | séries saturées ; générique | à faire |
| adidas « Backyard Legends » (4) | parole : `SEUIL=haut` + spectrogramme (la mesure de session 4 était déjà sur voix séparée) | **fait (session 9)** : 1 confirmée, 1 corrigée |
| Qui est l'imposteur (5) | parole : `SEUIL=haut` + spectrogramme | **fait (session 9)** : 1 confirmée, 1 corrigée |
| POPCORN (5) | parole : `SEUIL=haut` + spectrogramme | **fait (session 9)** : 1 confirmée, 1 corrigée |
| Boxho (5) | parole : spectrogramme (pas de fond musical) | **fait (session 9)** : 1 confirmée, 1 corrigée |
| YggTorrent, EGO, B-roll (4-5) | transcription : boucles et phrases fantômes | à faire |
| Clips (3-4) | séries saturées (Ziak éclairci) ; parole sans objet | à vérifier vite |
| Projets F42 (6) | parole (Fou rire, Hirsingen) sur voix séparée | à faire |
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
| **Total** | 19 | 12 | 6 | 1 |
