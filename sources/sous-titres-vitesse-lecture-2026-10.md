# Vitesse de lecture des sous-titres : ce qui est vérifié (session 14, consulté le 2026-10-10)

Pour BACKLOG 79 (temps de lecture d'un vers incrusté). Chiffres lus sur les pages Netflix Partner Help, en vérifiant le **titre** de chaque page.

| Source | Valeur |
|---|---|
| Netflix, *Timed Text Style Guide: General Requirements* (https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617) | durée minimale d'un sous-titre : **5/6 s** (20 images à 24 i/s) ; durée maximale : **7 s** ; les sections sur les intervalles entre sous-titres ont été retirées le 2020-07-24 (journal des modifications) |
| Netflix, guides russe, roumain, indonésien (résultats de recherche, pages non ouvertes une par une) | adultes **17 caractères/s**, enfants **13** |
| Netflix, guide chinois traditionnel / simplifié | adultes 9 car./s, enfants 7 ; 16 caractères par ligne |
| Netflix, *How is reading speed measured* (https://backlothelp.netflix.com/hc/en-us/articles/115001352212) | les espaces et la ponctuation comptent dans le nombre de caractères |

**Piège rencontré** : l'URL connue « 215986007-French-Timed-Text-Style-Guide » renvoie aujourd'hui le guide **chinois simplifié** (le résumé automatique m'a d'abord donné « 9 car./s, 16 car./ligne » pour le français). **La valeur française n'est donc pas vérifiée** : 17 car./s est probable (même valeur que les autres langues à alphabet latin), mais à confirmer sur le guide français lui-même.

**Pour un vers incrusté en clip** (déduction, pas une norme) : « Les vitrines me rendent un type que je connais pas » = 51 caractères → à 17 car./s, **3 s** de présence à l'écran, au-delà du plancher de 5/6 s. Mot à mot, le décompte commence au premier mot ; laisser le vers complet affiché au moins le temps que la vitesse de lecture demande après le dernier mot (à mesurer, BACKLOG 79). Les normes de sous-titrage visent la compréhension d'un dialogue ; un clip peut choisir d'être moins lisible, mais il doit le décider.

## Session 15 (consulté le 2026-10-10) : la valeur française, vérifiée

Le guide français a été retrouvé par l'API de recherche du centre d'aide Netflix (`/api/v2/help_center/articles/search.json`), puis lu en entier via l'API article ; **titre vérifié** à chaque fois. « Vérifié » = chiffre lu par moi sur la page ou le PDF ; « non vérifié » = vu seulement dans un résultat ou un résumé de recherche.

| Source (URL) | Valeur | Statut |
|---|---|---|
| Netflix, *French (France) Timed Text Style Guide* (https://partnerhelp.netflixstudios.com/hc/en-us/articles/217351577-French-France-Timed-Text-Style-Guide, mis à jour le 2025-12-19, rédigé en anglais, exemples en français) | adultes **17 car./s**, enfants **13** ; **42 car./ligne** ; en sous-titrage SME (section II), limites relevables à **20** (adultes) et **17** (enfants) | vérifié |
| Netflix, *French (Canada) Timed Text Style Guide* (https://partnerhelp.netflixstudios.com/hc/en-us/articles/42738240066835-French-Canada-Timed-Text-Style-Guide) | mêmes valeurs : 17 / 13, 42 car./ligne, SME 20 / 17 | vérifié |
| Netflix, *Timed Text Style Guide: General Requirements* (https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617, mis à jour le 2026-07-06) | durée min **5/6 s** (20 images à 24 i/s), max **7 s** ; le guide français ne donne pas d'autre durée | vérifié (relu) |
| ATAA, *French Subtitling Standards* (https://www.ataa.fr/documents/NORMES_SOUS-TITRAGE_FRANCAIS_ANGLAIS_EN-TETE.pdf, PDF du 2022-04-24, en anglais) | lecture moyenne **14-15 car./s** ; 16-17 jugés trop rapides (fatigue en quelques minutes) ; durée min **16 images** (un ou deux mots), max **5 s** hors chansons ; intervalle min 4 images ; car./ligne : cinéma 40-41, streaming 40-42, vidéo 38-40, télévision 36-37 | vérifié |
| CSA (aujourd'hui Arcom), *Charte relative à la qualité du sous-titrage à destination des personnes sourdes ou malentendantes*, 12 décembre 2011 (copie PDF lue : https://help.peach.me/hc/en-us/article_attachments/28687281538193 ; non retrouvée sur le site de l'Arcom dans le temps imparti) | critère 6, programmes de stock : **12 car. pour 1 s, 20 pour 2 s, 36 pour 3 s, 60 pour 4 s** (secondes de 25 images), tolérance **20 %** | vérifié (sur une copie tierce) |
| CSA Belgique (Fédération Wallonie-Bruxelles), *Charte relative à la qualité des mesures d'accessibilité* (https://www.csa.be/wp-content/uploads/documents-csa/20191015-Charte-accessibilité.pdf) | vitesse des sous-titres SME **entre 12 et 15 car./s** | vérifié |
| Europe 1, article sur le sous-titrage cinéma (https://www.europe1.fr/node/384992) | 12 à 15 car./s ; « 1 s et 8 images = 19 caractères » | non vérifié (résumé de recherche) |
| ATAA, « Code des bonnes pratiques » / SNAC | non trouvé dans le temps imparti : seule la fiche technique ATAA ci-dessus a été lue | inaccessible / non trouvé |

**Conclusion** : la valeur de session 14 (17 car./s adultes pour le français chez Netflix) est **confirmée**. Les normes professionnelles françaises sont plus lentes : **14-15 car./s** (ATAA), **~12 car./s** et plus pour les vers courts (charte CSA 2011). Le calcul du temps de tenue après le dernier mot est dans `labo/paroles/temps_lecture.py` et `labo/paroles/temps_lecture-resultats.md`. Correction : le vers de la pièce 19 compte **50** caractères, pas 51.
