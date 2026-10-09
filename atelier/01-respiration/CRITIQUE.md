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

## v3 — `v3-planche.png` (10 s, 250 images, planche 1 image sur 25)
Changements : fond = plan en dégradé vertical (lumière de surface en haut) dont l'intensité porte la profondeur ; rétention allongée à 4,5 s ; **le mot se resserre** (interlettrage 1,0 → 0,90) pendant la rétention puis se relâche (1,07) en s'affaissant.
Mesure luminance : 55,6 → 71,5 (inspiration, enfin lisible) → 44,0 (fin de rétention) → 55,0.
| Critère | Note | Preuve |
|---|---|---|
| Intention | 2 | Images 6-8 : le mot se comprime, les lettres se touchent presque — une constriction. Mais sans son, l'inquiétude reste discrète. |
| Lisibilité | 2 | Au maximum de compression (image 8) « ffl » se tasse : limite, assumé, mais à surveiller. |
| Rythme | 3 | 3 s / 4,5 s / 2,5 s : la rétention dure plus que l'inspiration — c'est l'inconfort voulu. |
| Composition | 2 | Le dégradé donne une profondeur ; cadrage toujours frontal, centré horizontalement (acceptable : sobriété). |
| Cohérence | 3 | Lumière, interlettrage et position racontent la même descente. |
| Couleur | 2 | Gris-bleu ardoise : évoque un fond d'écran plus que l'eau. |
| Mouvement | 3 | Le mouvement est sur le paramètre qui porte le sens. |
| Originalité | 2 | L'idée du mot qui retient son souffle est propre à la pièce ; la typo (Liberation Serif = « Times ») fait défaut. |
| Justesse | 3 | Rien à enlever. |
**Verdict : presque.** Il manque le son (prévu dans l'intention) et une police choisie plutôt que subie.

## v4 — police EB Garamond Italic (OFL, téléchargée via jsDelivr : `https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/ebgaramond/EBGaramond-Italic%5Bwght%5D.ttf`), fond plus profond/plus « eau », design sonore synthétique (`souffle_son.py`, aucun média externe)
Son : bruit coloré filtré, enveloppes calées sur l'image (inspiration crescendo coupée net à 3 s ; rétention : pression grave qui monte ; expiration à 7,52 s : attaque brève, longue décroissance). Forme d'onde : `v4-onde.png`. Mesure : -19,9 LUFS intégré, LRA 5,4 LU, crête -6 dBFS (laissé sous le niveau d'un dialogue web à -16/-14 : un souffle est intime, il ne doit pas « sonner fort »).
**Autocritique du son :** l'intention disait « silence total pendant la rétention » ; j'ai ajouté un grondement qui monte. C'est efficace sur le papier mais c'est le cliché du *drone de tension*. Je ne peux pas écouter : je juge par la forme d'onde et les mesures. → Faire une variante v4b avec un vrai silence (simple souffle d'ambiance très bas) et trancher en phase 2 à l'écoute.

### Critique v4 — `v4-planche.png`
Mesure luminance : 51,0 → 65,7 (inspiration) → 40,8 (fin de rétention) → 50,6.
| Critère | Note | Preuve |
|---|---|---|
| Intention | 3 (sous réserve d'écoute) | Image et son racontent la même apnée : inspiration en crescendo coupée net, constriction, relâchement. |
| Lisibilité | 2 | Images 7-8 : avec EB Garamond, plus étroite, l'interlettrage 0,90 écrase « ffl ». Le réglage dépend de la police. |
| Rythme | 3 | Inchangé (3 / 4,5 / 2,5 s). |
| Composition | 2 | Inchangée. |
| Cohérence | 3 | Typo littéraire, eau, souffle : un seul monde. |
| Couleur | 3 | Bleu-vert profond : on lit l'eau. |
| Mouvement | 3 | |
| Originalité | 2 | L'idée tient ; la mise en page reste classique. |
| Justesse | 2 | Le grondement de rétention (cliché possible). Inspiration moins lumineuse qu'en v3 (amplitude 15 contre 16 en luminance, sur un fond plus sombre). |
**Verdict : livrable sous réserve.** Corrections : interlettrage minimum 0,93 pour cette police, inspiration plus lumineuse (v5), et choisir à l'écoute entre grondement (v5a) et silence (v5b).
**Leçon générale :** une valeur d'animation typographique (interlettrage, approche) **ne se transpose pas d'une police à l'autre** : la retester à chaque changement de police.
