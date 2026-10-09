# Pièce 01 « Respiration » — critiques successives

Grille : `montage-regard` (0 à 3, avec une preuve visuelle par critère).

## v1 — `v1-planche.png` (Blender 4.2, Cycles 16 échantillons, 640×360, 200 images, rendu 283 s)
| Critère | Note | Preuve visuelle |
|---|---|---|
| Intention | 1 | Rien d'apnée, rien d'inquiétant : un mot qui pulse. |
| Lisibilité | 1 | Image 0 : mot **noir** sur fond bleu (émission à 0 = noir, pas transparent). « souf fle » : trou entre les deux f (italique FreeSerif). |
| Rythme | 1 | 4 s / 4 s symétrique : une respiration réelle n'est pas symétrique. |
| Composition | 1 | Centré, aplat uniforme : carton générique. |
| Cohérence | 2 | Serif + bleu nuit : cohérent. |
| Couleur | 2 | Bleu nuit juste mais plus ardoise que profond (Standard view). |
| Mouvement | 0 | Échelle 0,9 → 1,1 (22 %) : se lit comme un « pulse » de logo. |
| Originalité | 0 | Cliché du carton-titre centré qui zoome. |
| Justesse | 2 | Sobre, mais vide plutôt que retenu. |
**Verdict : non livrable.** Le mouvement a une cause théorique (respirer) mais pas de forme juste.

## v2 — `v2-planche.png` (Cycles 4 échantillons, 200 images)
Changements : inspiration 3 s / rétention 3 s / expiration 2 s ; fondu par transparence ; Liberation Serif italique ; texte abaissé ; fond qui s'assombrit pendant la rétention ; amplitude 6 %.
Mesure (`signalstats`, luminance moyenne toutes les 20 images) : 52 → 55,8 (inspiration) → 36,3 (fin de rétention) → 45 (expiration).
| Critère | Note | Preuve |
|---|---|---|
| Intention | 2 | La descente pendant la rétention se voit (images 5→8). L'inquiétude ne vient pas encore. |
| Lisibilité | 3 | Fondu propre (image 1), « ff » correct. |
| Rythme | 2 | Asymétrie juste, mais la rétention de 3 s est trop courte pour inquiéter. |
| Composition | 2 | Mot bas = de l'eau au-dessus ; mais aplat plat. |
| Mouvement | 1 | 6 % d'échelle : imperceptible ; l'inspiration ne se lit pas (lum. +3,8 seulement). |
| Originalité | 1 | Encore très « carton ». |
| Justesse | 3 | Rien de trop. |
**Verdict : meilleure, pas livrable.** Leçon : j'ai corrigé l'excès de v1 par un manque. Réduire l'amplitude ne suffit pas : il faut **déplacer** le mouvement vers un paramètre qui porte le sens (ici, l'interlettrage = le corps qui se retient), plutôt que garder le même paramètre en plus petit.

## v3 — voir plus bas
