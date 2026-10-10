# Pièce 13 « Le fond raccorde » — intention (écrite avant de créer)

Session 9, 2026-10-10. BACKLOG 47, leçon de la pièce 10 v6 : le plan serré se réchauffait **par son fond**, et ce réchauffement se lisait sur le personnage.

## Question
Dans un champ / contrechamp, peut-on faire « se refroidir » un personnage (il se ferme, il s'éloigne) **sans toucher à sa peau ni à sa lumière**, seulement par la couleur du mur derrière lui ? Et est-ce plus juste que de refroidir sa lumière ?

## Dispositif (Blender, deux têtes abstraites, plans fixes)
- A regarde à droite, B à gauche (180° respecté). Même lumière clé blanche pour les deux. 8 plans alternés A/B, ~1,2 s chacun.
- **v1 « le fond seul »** : le mur de A reste neutre ; le mur de B passe du neutre au bleu en 4 marches. La peau de B est identique d'un plan à l'autre (mesuré).
- **v2 « la lumière »** : murs neutres ; c'est la clé de B qui bleuit en 4 marches (la peau change).
- **v3 « deux mondes »** : le mur de A se réchauffe pendant que celui de B refroidit (la distance entre eux).

## Mesures possibles sans spectateur
- Lab de la peau (moyenne des pixels du visage) et du mur, par plan : ΔE de la peau entre plans (v1 doit donner ≈ 0).
- Estimation **modèle** du décalage perçu de la peau par contraste simultané : la teinte perçue s'écarte de celle du fond (induction chromatique opposée). Hypothèse simple et explicite : décalage ≈ −k × (a*, b* du fond), k = 0,1-0,3. C'est une hypothèse à confirmer en phase 2, pas une mesure de perception.

## Critères
1. v1 : peau constante (ΔE < 1), fond qui change franchement (ΔE > 15 en 4 marches).
2. La progression se lit sur la planche sans être un effet (pas de saut brutal, chaque marche visible).
3. Juger : laquelle dit « B se ferme » et laquelle dit « la lumière a changé » (faux raccord) ?
