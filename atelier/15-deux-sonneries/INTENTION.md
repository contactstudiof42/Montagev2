# Pièce 15 « Deux sonneries de trop » (session 10, 2026-10-10)

**Origine** : examen n°6. Le réalisateur voulait un ralenti sur la main qui décroche (rushes à 25 i/s) ; j'ai refusé au nom du labo d'interpolation et proposé le **ralenti du temps** (laisser sonner deux fois de plus). Cette pièce met ma réponse à l'épreuve au lieu de la croire.

**Intention** : « le moment où elle se décide à répondre » doit peser. Le spectateur doit sentir l'hésitation, pas admirer un effet.

**Dispositif** : un téléphone fixe sur une table, une main (bloc simple) qui entre, saisit le combiné et le soulève ; un cordon fin (objet fin = cas hostile pour l'interpolation). Quatre versions du même instant :
- **A** : 3 sonneries, décroché à vitesse réelle (25 i/s).
- **B** : 5 sonneries (deux de trop), décroché à vitesse réelle.
- **C** : 3 sonneries, décroché ralenti ×3 **interpolé** depuis le 25 i/s (`minterpolate mci`) — ce que donnerait le rush de l'examen.
- **D** : 3 sonneries, décroché ralenti ×3 **vrai** (rendu à 75 i/s, lu à 25) — ce que donnerait un tournage en haute cadence.

**Critères** : (1) C contre D : erreurs d'interpolation mesurées sur la main, le combiné, le cordon (PSNR zones en mouvement, planche d'erreur) ; (2) B contre D : lequel dilate le moment sans le surligner ? (jugement sur planche et chronologie, perception réelle en phase 2) ; (3) aucun son sur-désigné : les sonneries sont le seul son.
Médias : tout est fabriqué (Blender, sons synthétisés par ffmpeg) : aucune licence tierce.
