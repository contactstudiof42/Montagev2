# Pièce 05 « Trois étalonnages » — intention (écrite avant de créer)

Session 5, 2026-10-10. BACKLOG 3 (« même plan, trois étalonnages ») et 8 (arbre de nodes).

## Le matériau
Le même plan de la pièce 04 (configuration `v6-surface.json` : la chaise de bistrot rouillée que la marée découvre), trois instants : f70 (eau haute, la chaise à peine visible), f160 (l'eau se retire), f230 (estran découvert). Rendu Blender Cycles, AgX « Base Contrast », 640×360. On étalonne **l'image rendue** (référée à l'affichage, 8 bits), comme on étalonnerait un rush Rec.709 : c'est une limite assumée, notée en critique.

## Ce que je veux prouver
Qu'un étalonnage n'est pas un filtre mais **une lecture du plan** : le même plan doit raconter trois histoires différentes, et chacune doit pouvoir s'écrire en une phrase avant de toucher un curseur. Si deux versions disent la même chose, l'exercice a échoué.

## Les trois directions (une phrase chacune)
- **A « Constat »** (documentaire, Morris) : *on regarde une pièce à conviction.* Neutre et un peu froid, saturation basse mais pas grise, contraste moyen, noirs posés, la rouille lisible comme matière et non comme émotion. Rien n'est souligné.
- **B « Souvenir »** (deuil, Varda) : *quelqu'un s'est assis là, il y a longtemps.* Laiteux : noirs relevés, hautes lumières compressées, légère dominante chaude dans les hautes lumières, saturation basse. Doux, sans sépia de carte postale.
- **C « Menace »** (vos goûts : Joker, Ziak) : *l'eau rend quelque chose qu'on n'aurait pas dû voir.* Bas et dense (médiane de luminance très basse), environnement vert-froid, **une seule chaleur : la rouille de la chaise**, isolée par sa teinte et poussée, tout le reste désaturé.

## Critères de réussite (mesurables autant que possible)
1. Trois phrases différentes : un spectateur décrirait trois sentiments (jugé sur la planche).
2. C : la chaleur limitée à la chaise (pixels chauds < 2 % de l'image, et absents du sable et du ciel).
3. B : noir minimal ≥ 20/255 (laiteux réel), pas de dominante orange dans les ombres (sinon carte postale).
4. A : écart de teinte moyen du sable et du ciel proche du neutre (pas de « look »).
5. La chaise reste lisible dans les trois (la lecture du plan n'est pas sacrifiée au look).
