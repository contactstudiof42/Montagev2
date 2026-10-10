# Pièce 07 « Causalité » — intention (écrite avant de créer)

Session 6, 2026-10-10. BACKLOG 21 et 31, principe de Honda « Cog » (`culture/honda-cog.md`) : quand la preuve est l'argument, ne pas couper ; les sons des objets font la bande-son.

## Le sujet
Sur la table de la pièce 06 : une bille descend un livre incliné, heurte une rangée de dominos, le dernier domino pousse la tasse posée au bord, la tasse tombe. Une chaîne causale de 8 s, **simulée physiquement** (corps rigides Blender), pas animée à la main : la causalité doit être vraie dans le fichier, pour que la question ne porte que sur le montage.

## La question de montage
Le même événement, trois montages :
- **A, plan unique** (Cog) : un plan large fixe, rien n'est coupé. Hypothèse : c'est le plus crédible, mais les dominos et la bille sont petits dans le cadre.
- **B, découpé sur les contacts** : un plan serré par maillon, coupe au moment exact de chaque contact (cause dans un plan, effet dans le suivant). Hypothèse : plus lisible et plus nerveux, mais chaque coupe fait soupçonner la triche (« la bille a-t-elle vraiment touché ? »).
- **C, découpé mais avec les contacts dedans** : on coupe *entre* les contacts, chaque plan contient une cause **et** son effet. Hypothèse : on garde la lisibilité des plans serrés sans casser la preuve.

## Son
Aucune musique. Seulement les sons des objets, placés **à l'image près depuis les contacts calculés par la simulation** : roulement de la bille (bruit filtré), clics des dominos, choc de la tasse. Le silence après la chute.

## Critères de réussite
1. Chaque contact est visible dans au moins un plan (vérifié sur la planche « contacts »).
2. Dans C, aucun contact n'est à cheval sur une coupe (mesuré : distance coupe-contact ≥ 4 images).
3. Les sons tombent sur les contacts à 1 image près (mesuré).
4. A reste lisible à 480×270 : on distingue la bille et les dominos.
