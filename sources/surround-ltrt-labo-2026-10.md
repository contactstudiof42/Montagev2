# Downmix 5.1 → stéréo : Lo/Ro ou Lt/Rt, et ce que devient l'arrière en mono (labo)

Labo du 10/10/2026 (BACKLOG 34), ffmpeg 6.1.1 + numpy/scipy, matériau 100 % synthétique. Scripts, commandes exactes et tableau complet : `labo/surround/` (`labo_surround.py`, `RESULTATS.md`, `resultats.json`). Contexte normatif (BS.775, RT 040, Tech 3344) : `sources/surround-hors-champ-2026-10.md`.
Statuts : **[TESTÉ EN LABO]** (mesuré ici), **[THÉORIQUE]** (raisonnement ou sources, pas mesuré).

## 1. Chiffres clés (5.1 synthétique à -23,5 LUFS : dialogue au C, musique en L/R, ambiance décorrélée en Ls/Rs 12 dB sous le front, LFE)

| Élément | 5.1 | Lo/Ro stéréo | Lo/Ro mono (L+R)/2 | Lt/Rt stéréo | Lt/Rt mono |
|---|---|---|---|---|---|
| Mix complet | -23,5 LUFS | -23,5 | -26,8 | -23,5 | -26,8 |
| Dialogue (C) | -24,6 | -24,6 | -27,6 (**-3,0 : référence**) | -24,6 | -27,6 |
| Ambiance arrière | -41,9 | -46,4 (-4,5) | **-52,4 (-10,5)** | -46,4 | **-70 = disparue** |
| LFE | exclu de la mesure | absent | absent | absent | absent |

[TESTÉ EN LABO]. Le résultat est identique avec un Lt/Rt `pan` simple et avec un vrai déphasage de 90° (Hilbert scipy ou `afir` ffmpeg).

## 2. Recettes

- **Lo/Ro ITU** [TESTÉ EN LABO] : `-af "pan=stereo|FL=FL+0.7071*FC+0.7071*BL|FR=FR+0.7071*FC+0.7071*BR"` (fichier en `5.1(side)` : SL/SR au lieu de BL/BR).
- **Lt/Rt simple** [TESTÉ EN LABO] : `-af "pan=stereo|FL=FL+0.7071*FC-0.5*BL-0.5*BR|FR=FR+0.7071*FC+0.5*BL+0.5*BR"`. Suffisant pour **vérifier** la compatibilité (mono, phase). Ce n'est pas un encodeur Dolby.
- **Lt/Rt avec déphasage de 90°, ffmpeg seul** [TESTÉ EN LABO] : FIR de Hilbert de 2047 points en wav et `afir=gtype=none` sur S, fronts retardés de 1023 échantillons par `adelay`. Le graphe complet est dans `labo/surround/RESULTATS.md`. Il colle à `scipy.signal.hilbert` à -81 dB au-dessus de 50 Hz, mais devient faux en dessous (FIR trop court). Il ajoute 21,3 ms de latence, à recaler.
- **Lt/Rt Hilbert via `aiir`** (paires d'all-pass) : [THÉORIQUE], pas tenté.
- **Contrôle mono** [TESTÉ EN LABO] : `-af "pan=mono|c0=0.5*c0+0.5*c1,ebur128=peak=true"`. Phase : `aphasemeter=video=0,ametadata=print:key=lavfi.aphasemeter.phase:file=-`, puis moyenne.

## 3. Quand préférer Lo/Ro ou Lt/Rt

- **Lo/Ro** quand la stéréo sera écoutée telle quelle ou risque d'être repliée en mono (téléphone, enceinte unique, TV bas de gamme, web). C'est le seul des deux qui garde une trace des arrières en mono (-10,5 LU, mais présente) [TESTÉ EN LABO].
- **Lt/Rt** seulement si la chaîne aval décode du Pro Logic ou si la spec l'exige. La RT 040 met « Preferred Stereo Downmix = Lt/Rt » dans les métadonnées Dolby par défaut du PAD français, et exige que la compatibilité mono soit vérifiée (voir la source surround-hors-champ). Dans ce cas, **vérifier le repliement mono** : tout ce qui n'existe qu'à l'arrière y disparaît [TESTÉ EN LABO].
- Le décodeur du téléspectateur choisit souvent tout seul (Tech 3344 : box et téléviseurs ignorent la métadonnée). Il faut donc que le mix **survive aux deux** [THÉORIQUE, d'après la source précédente].

## 4. Pièges

1. **Le chiffre global ment** [TESTÉ EN LABO] : le mix complet garde -23,5 LUFS dans les 4 downmix alors que l'ambiance arrière a disparu en Lt/Rt mono. Une ambiance pèse trop peu en LUFS pour bouger le chiffre. Il faut écouter ou mesurer les **stems**.
2. **Le 90° ne sauve pas le mono** [TESTÉ EN LABO] : S est en ±S dans Lt/Rt, quel que soit son déphasage par rapport aux fronts, donc Lt+Rt l'annule toujours. Seul du contenu arrière **aussi présent à l'avant** survit.
3. **Le `pan` simple peut vider un canal** [TESTÉ EN LABO] : le même signal à l'avant et à l'arrière (réverbe ou room tone étalés sur 4 canaux) donne L - S = 0, donc Lt muet et toute l'ambiance dans Rt. Le Hilbert remet Lt et Rt au même niveau (-40,0 dBFS RMS chacun) et les décorrèle. C'est le vrai intérêt du 90° : la stabilité de l'image stéréo, pas le mono.
4. **Ambiance identique Ls = Rs** [TESTÉ EN LABO] : en Lt/Rt, elle perd moins en stéréo (-1,5 LU au lieu de -4,5) mais part entièrement en antiphase (corr. -1,00, phase moyenne -1,00). C'est mauvais à la fois sur un phasemètre de chaîne et en mono.
5. Latence de l'`afir` (1023 échantillons) et LFE omis partout : déjà vu en session 6 [TESTÉ EN LABO].
6. `-ac 2` normalise les coefficients et rend le downmix 7,6 dB trop bas (session 6) [TESTÉ EN LABO].

## 5. Pour le monteur son et pour l'intention artistique

- **Dialogue** : au centre, il est stable dans tous les cas (perte de 3 LU en mono, comme le reste du front centré) [TESTÉ EN LABO]. Pas d'inquiétude tant qu'il reste au C.
- **L'arrière est un luxe qui s'évapore** : une présence hors champ construite seulement dans Ls/Rs recule de 7,5 LU par rapport au dialogue en Lo/Ro mono et **n'existe plus** en Lt/Rt mono [TESTÉ EN LABO]. Si l'ambiance arrière porte du **sens** (menace hors champ, foule qui gronde, lieu qui respire), elle doit avoir un **pied à l'avant** : une version plus discrète de l'ambiance dans L/R, décorrélée de l'arrière (pas une copie, sinon le piège 3 s'applique en Lt/Rt simple) [THÉORIQUE, conséquence directe des mesures].
- Accepter qu'en mono et sur un smartphone, l'enveloppement soit perdu, mais pas l'**information**. Faire la passe d'écoute « mono Lt/Rt » comme on fait une passe d'écoute sur petit haut-parleur.
- À l'inverse, un élément qu'on **veut** voir disparaître hors du 5.1 (un détail d'immersion qui encombrerait la stéréo) peut rester seulement à l'arrière. C'est un choix, pas un accident [THÉORIQUE].
- Toujours écouter les deux downmix, plus le mono, avant de valider. Dans la fiche de livraison, noter quel downmix la spec impose.

## Incertain / à vérifier

- Pas de décodeur Pro Logic dans ffmpeg : la séparation C/S au décodage n'est pas vérifiée.
- Un vrai encodeur Dolby Surround filtre S (environ 100 Hz-7 kHz) et applique souvent un réducteur de bruit. Non modélisé ici [THÉORIQUE].
- Les chiffres viennent de signaux synthétiques : ce sont des ordres de grandeur, à confirmer sur un vrai mix 5.1 (stems séparés).
