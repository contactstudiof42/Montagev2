# Pièce 11 « Dialogue » — critique (session 8)

Planches : `v1-planche.png`, `v2-planche.png`, `v3-planche.png` (une vignette par plan, temps de début) ; montage et voix : `montage.py`, `edl.json` ; mesures des regards : `mesures.json` (copie de `atelier/rendus/11/mesures.json`). Rendus : `atelier/rendus/11/v*.mp4` (15 s, 480×270). Plans fixes = une image Cycles chacun (~6 s), travelling = 50 images.

## Mesure : les sauts de regard à chaque coupe
Règle de `labo/grammaire` : quand on coupe d'un personnage à l'autre, leurs regards à l'écran doivent être opposés. Compté sur chaque coupe :
- **v1** (tout côté −Y) : 0 saut. A regarde toujours à droite, B à gauche.
- **v2** (coupe franche de l'autre côté à 7,6 s) : **1 seul saut**, exactement à la bascule (A1 avant : A → droite ; B2 après : B → **droite**). Ensuite A2 / B2 sont de nouveau opposés (A ← , B →) : **franchir l'axe pour tous les plans à la fois établit un nouvel axe** ; l'erreur n'existe qu'à la jointure.
- **v3** (travelling qui traverse l'axe en passant derrière B pendant qu'il se lève) : 0 saut par la coupe ; l'inversion se fait sous les yeux du spectateur.

C'est la découverte principale : **un franchissement n'est une « erreur » que s'il est partiel** (un plan de l'autre côté puis retour) ; complet, il devient une **rupture localisée** qu'on peut placer à l'image près, comme une coupe franche dans la musique.

## Critique DA
**v1 — classique.** Lisible, propre ; la bascule passe par les hauteurs (plongée sur B assis, B debout plus grand que A) et le son (A parle, puis B parle, A se tait). Ça suffit à comprendre, mais rien dans la **forme** ne bascule : la mise en scène reste celle de A jusqu'au bout. Correct, sans point de vue.

**v2 — franchi à la coupe.** Le saut de regard tombe sur l'image où B se lève : le spectateur ressent un **choc spatial** au moment du choc dramatique, puis se recale en un plan (le nouvel axe est cohérent). Effet secondaire non prévu et décisif : **le fond change**. Côté −Y, le mur éclairé ; côté +Y, le noir de la pièce. Le « monde de A » est clair, celui de B sombre : le décor dit que le rapport de force a changé de propriétaire. **C'est la meilleure version** : la règle est cassée une fois, au bon endroit, et le renversement a un contenu visuel.
Défaut : le premier plan après la bascule (B2) arrive sans plan large ; le spectateur peut croire un instant que B parle à quelqu'un d'autre. Un plan d'ensemble du nouveau côté (E2) placé **juste après** B2 et non à la fin réparerait la carte mentale plus tôt — à tester (v4).

**v3 — franchi en mouvement.** Le travelling passe derrière B qui se lève : à mi-course, **B éclipse A** (vignette 6,8 s) : image forte, littérale (B prend toute la place). Mais 2 s de mouvement de caméra dans une pièce de plans fixes, c'est un **effet** qui annonce l'événement au lieu de le subir ; le mouvement « explique » la bascule. Plus élégant, moins violent. À garder pour une bascule *lente* (une prise de conscience), pas pour un renversement brutal.

**Justesse** : la v2 fait le moins de choses (une coupe) pour le plus de sens. Cohérent avec mon principe « un signe fort plutôt que trois faibles ». Limite de l'exercice : des cylindres n'ont pas de visage ; la vraie épreuve (un regard humain qui « change de camp ») reste à faire en phase 2 ou avec un personnage articulé.

## Leçons (versées dans `montage-grammaire`)
1. **Franchir l'axe pour tous les plans à la fois = une seule rupture, placée à l'image près** ; le spectateur se recale au plan suivant. Partiel (aller-retour), c'est l'erreur qu'on connaît.
2. **Le franchissement change aussi le fond** : choisir de quel côté est la lumière, le mur, la fenêtre, c'est choisir à qui appartient le monde de la scène. Préparer au tournage : deux côtés de décor qui disent deux choses.
3. **Coupe franche pour un renversement brutal, travelling qui traverse pour une bascule lente** ; le mouvement explique, la coupe fait subir.
4. Le contrôle automatique des sauts de regard (signe par coupe) marche sur un montage entier : un outil possible pour un agent en phase 2.

## v4 (`v4-planche.png`) — le plan d'ensemble du nouveau côté juste après la bascule
B2 (1,4 s) → **E2** (1,4 s) → A2 → B2 → **A2 pour finir** (A muet, 1 s). La carte se recale dès le 2e plan après le saut (E2 montre B debout à gauche, A plus petit à droite, sur fond noir) ; et finir sur A qui se tait donne la conclusion au perdant, ce que v2 laissait au plan large neutre. **v4 = référence.** Ce que je retiens : après une rupture volontaire, **le plan qui re-situe vient tout de suite**, pas en conclusion ; la conclusion appartient au personnage qui a perdu la scène.
