# Pièce 15 « Deux sonneries de trop » — critique (session 10)

Rendu : 120 images à 75 i/s (320×180, Cycles 8 éch., ~2 min) ; le 25 i/s = une image sur trois. Montages `montage.sh` (A, B, C, D) et `b2.sh` (B2). Son : sonnerie synthétisée (880 + 1320 Hz, trille 20 Hz, 1,2 s / 1,8 s), fond brun ; -20,8 LUFS (non normalisé : pièce d'étude).

## C (ralenti ×3 interpolé depuis 25 i/s) contre D (ralenti vrai, 75 i/s) — `v1-erreur-C-contre-D.png`, `v1-planche-C-D.png`
- Mesure (`mesure.py`, images inventées seulement, zones en mouvement = 30,7 % du cadre) : **43,0 dB en moyenne, 29,2 dB au pire** (image 83, pendant la levée).
- Ce que la planche montre et que la moyenne cache : sur la levée, **le combiné et la main se brisent en blocs** sur 2 images sur 3, le **cordon se dédouble** ; une image sur trois (l'originale) est nette. À 25 i/s cela donne une **pulsation nette / cassé / cassé à 8 Hz** sur l'objet même que le ralenti voulait honorer. La moyenne est bonne parce que 70 % du cadre (table, mur, téléphone immobile) est parfait : **une moyenne de PSNR flatte toujours un ralenti** ; juger la pire image et la zone du sujet.
- Confirme le labo et l'examen n°6 : main, objet fin (cordon), occlusion (la main passe devant le combiné) = interpolation refusée.

## B (5 sonneries, réel) contre A (3) — `v1-planche-A-B.png`
- Sur la planche, B = A avec 6 s de plus d'un téléphone immobile. **Sans personne, les deux sonneries de trop ne sont pas une hésitation : c'est du temps vide.** Mon alternative de l'examen était incomplète : le ralenti du temps a besoin **d'un signe de quelqu'un qui pourrait répondre et ne répond pas**.

## B2 — la main posée — `v2-planche-B2.png`
- 3 sonneries téléphone seul ; la main entre en temps réel (0,56 s) et **se pose sur le combiné** ; elle reste posée **deux sonneries** (image fixe + grain) ; puis elle décroche en temps réel.
- Ici l'attente a un sujet : la main est là, elle peut décrocher, elle ne le fait pas. C'est l'hésitation que le ralenti de C voulait montrer, **sans aucune image fabriquée** et avec un geste final à vitesse réelle (qui garde son poids, parce qu'il libère l'attente).
- Limite : une main-bloc immobile se lit comme une image figée ; un vrai rush aurait un micro-mouvement (doigts, respiration). Jugement en mouvement et au son : phase 2.

## Verdict
**B2 > D > A > B > C.** Le ralenti vrai (D) reste un bon outil si on a tourné en haute cadence ; le ralenti interpolé (C) depuis 25 i/s abîme précisément le sujet ; l'attente tenue n'a de sens qu'**habitée** (B2), vide elle ne vaut rien (B).

## Versé dans les skills
`montage-rythme` (dilater par la durée : l'attente doit être habitée) ; `montage-direction-artistique` (ralenti demandé sur rushes 25 i/s : proposer « la main posée qui ne décroche pas », vérifier qu'elle existe dans les rushes).
