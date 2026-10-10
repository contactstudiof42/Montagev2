# Labo paroles incrustées : temps de lecture d'un vers (session 15, 2026-10-10) [TESTÉ EN LABO pour le calcul ; normes THÉORIQUES]

Question (BACKLOG 79) : quand un vers apparaît mot à mot sur la voix, combien d'images faut-il le **tenir après le dernier mot** pour qu'il soit lisible en entier ?

**Méthode** (`temps_lecture.py`, bibliothèque standard) : nombre de caractères espaces et ponctuation compris (règle Netflix) → durée requise selon chaque norme (avec son plancher) → images à 24 et 25 i/s, arrondies au-dessus. Mot à mot : 0,3 s par mot (≈ 3 syllabes/s, approximation), le dernier mot arrive à (mots − 1) × 0,3 s ; **tenue = max(0, durée requise − ce délai)**. Les normes et leur statut (vérifié / non vérifié) sont dans `sources/sous-titres-vitesse-lecture-2026-10.md`, section Session 15.

Normes utilisées : Netflix FR 17 c/s adultes, 20 c/s en sous-titrage SME, 13 c/s enfants, plancher 5/6 s, plafond 7 s ; ATAA 14-15 c/s, plancher 16 images, plafond 5 s ; barème de la charte CSA 2011 (12 car. = 1 s, 20 = 2 s, 36 = 3 s, 60 = 4 s, interpolé linéairement par le labo) ; CSA belge 12 c/s (bas de sa fourchette 12-15).

## Sortie brute
La colonne « requis s » est à 25 i/s (à 24 i/s, seul le plancher ATAA de 16 images change).

```
Débit mot à mot supposé : 0.3 s par mot (≈ 3 syllabes/s). Tenue = images à garder après l'apparition du dernier mot.

« On danse sous la pluie » : 22 car., 5 mots, apparition mot à mot 1.2 s
  norme                           requis s  24 i/s  25 i/s | tenue s  24 i/s  25 i/s
  Netflix FR adultes 17 c/s           1.29      32      33 |    0.09       3       3
  Netflix FR SME adultes 20 c/s       1.10      27      28 |    0.00       0       0
  Netflix FR enfants 13 c/s           1.69      41      43 |    0.49      12      13
  ATAA 15 c/s (haut)                  1.47      36      37 |    0.27       7       7
  ATAA 14 c/s (bas)                   1.57      38      40 |    0.37       9      10
  CSA FR 2011 (SME, barème)           2.12      51      54 |    0.93      23      24
  CSA Belgique 12 c/s (strict)        1.83      44      46 |    0.63      16      16

« Demain on brûlera les cartes » : 28 car., 5 mots, apparition mot à mot 1.2 s
  norme                           requis s  24 i/s  25 i/s | tenue s  24 i/s  25 i/s
  Netflix FR adultes 17 c/s           1.65      40      42 |    0.45      11      12
  Netflix FR SME adultes 20 c/s       1.40      34      35 |    0.20       5       5
  Netflix FR enfants 13 c/s           2.15      52      54 |    0.95      23      24
  ATAA 15 c/s (haut)                  1.87      45      47 |    0.67      16      17
  ATAA 14 c/s (bas)                   2.00      48      50 |    0.80      20      20
  CSA FR 2011 (SME, barème)           2.50      60      63 |    1.30      32      33
  CSA Belgique 12 c/s (strict)        2.33      56      59 |    1.13      28      29

« Les néons coulent sur le bitume mouillé » : 39 car., 7 mots, apparition mot à mot 1.8 s
  norme                           requis s  24 i/s  25 i/s | tenue s  24 i/s  25 i/s
  Netflix FR adultes 17 c/s           2.29      56      58 |    0.49      12      13
  Netflix FR SME adultes 20 c/s       1.95      47      49 |    0.15       4       4
  Netflix FR enfants 13 c/s           3.00      72      75 |    1.20      29      30
  ATAA 15 c/s (haut)                  2.60      63      65 |    0.80      20      20
  ATAA 14 c/s (bas)                   2.79      67      70 |    0.99      24      25
  CSA FR 2011 (SME, barème)           3.12      75      79 |    1.33      32      34
  CSA Belgique 12 c/s (strict)        3.25      78      82 |    1.45      35      37

« J'ai gardé ta voix dans la poche de mon manteau » : 47 car., 10 mots, apparition mot à mot 2.7 s
  norme                           requis s  24 i/s  25 i/s | tenue s  24 i/s  25 i/s
  Netflix FR adultes 17 c/s           2.76      67      70 |    0.06       2       2
  Netflix FR SME adultes 20 c/s       2.35      57      59 |    0.00       0       0
  Netflix FR enfants 13 c/s           3.62      87      91 |    0.92      22      23
  ATAA 15 c/s (haut)                  3.13      76      79 |    0.43      11      11
  ATAA 14 c/s (bas)                   3.36      81      84 |    0.66      16      17
  CSA FR 2011 (SME, barème)           3.46      83      87 |    0.76      19      19
  CSA Belgique 12 c/s (strict)        3.92      94      98 |    1.22      30      31

« Tout le quartier dort, moi je compte encore les fenêtres » : 56 car., 10 mots, apparition mot à mot 2.7 s
  norme                           requis s  24 i/s  25 i/s | tenue s  24 i/s  25 i/s
  Netflix FR adultes 17 c/s           3.29      80      83 |    0.59      15      15
  Netflix FR SME adultes 20 c/s       2.80      68      70 |    0.10       3       3
  Netflix FR enfants 13 c/s           4.31     104     108 |    1.61      39      41
  ATAA 15 c/s (haut)                  3.73      90      94 |    1.03      25      26
  ATAA 14 c/s (bas)                   4.00      96     100 |    1.30      32      33
  CSA FR 2011 (SME, barème)           3.83      92      96 |    1.13      28      29
  CSA Belgique 12 c/s (strict)        4.67     112     117 |    1.97      48      50

« Les vitrines me rendent un type que je connais pas » (référence pièce 19) : 50 car., 10 mots, apparition mot à mot 2.7 s
  norme                           requis s  24 i/s  25 i/s | tenue s  24 i/s  25 i/s
  Netflix FR adultes 17 c/s           2.94      71      74 |    0.24       6       7
  Netflix FR SME adultes 20 c/s       2.50      60      63 |    0.00       0       0
  Netflix FR enfants 13 c/s           3.85      93      97 |    1.15      28      29
  ATAA 15 c/s (haut)                  3.33      80      84 |    0.63      16      16
  ATAA 14 c/s (bas)                   3.57      86      90 |    0.87      21      22
  CSA FR 2011 (SME, barème)           3.58      86      90 |    0.88      22      23
  CSA Belgique 12 c/s (strict)        4.17     100     105 |    1.47      36      37

```

## Ce que ça dit
- **Mot à mot, la parole fait déjà l'essentiel du temps de lecture** : à 0,3 s par mot, un vers de 10 mots met 2,7 s à s'afficher, soit à peu près ce que demande Netflix à 17 c/s pour 45-50 caractères. La tenue après le dernier mot reste donc courte : **0 à 15 images à 17 c/s, 7 à 26 images à 15 c/s (ATAA)**.
- **Ce qui allonge la tenue, ce sont les mots longs** (beaucoup de caractères par mot), pas la longueur du vers : « Demain on brûlera les cartes » (28 car., 5 mots) demande plus de tenue que « J'ai gardé ta voix dans la poche de mon manteau » (47 car., 10 mots).
- Le barème CSA 2011 est plus généreux pour les **vers courts** (20 car. = 2 s, soit 10 c/s) : c'est la norme la plus exigeante sous 30 caractères.
- Le vers de la pièce 19 compte **50** caractères (et non 51 comme écrit en session 14).

## Règle pratique pour un monteur de clip
**Tenir le vers complet 1/2 s à 1 s après le dernier mot (12 à 25 images à 24-25 i/s)** ; calcul rapide : tenue (s) ≈ caractères / 15 − (mots − 1) × 0,3, minimum 0. Pour un public enfant, ou un vers à mots longs (moins de 5 mots pour 25 caractères ou plus), viser 1 s et plus. En dessous de ces valeurs, le vers est lu par une partie du public seulement : c'est un choix possible (le clip n'est pas un sous-titre de dialogue), mais il doit être décidé, par exemple quand le texte est une texture ou un écho de la voix que l'oreille comprend déjà.

## Limites
- 0,3 s par mot est une approximation : mesurer le débit réel sur la voix (alignement mot à mot) avant de caler.
- Les normes visent un sous-titre lu d'un bloc ; le mot à mot permet de lire au fil de la voix, ce qui rend probablement le calcul **prudent**. Non mesuré sur des lecteurs (phase 2).
- L'interpolation du barème CSA entre ses quatre points et son prolongement au-delà de 60 caractères sont des hypothèses du labo.
