# Pièce 12 « Inquiétude calme » — critiques successives

Mesures : `mesures.txt` (script `mesure.py` : aire du changement entre plan 1 et plan 3, distance à la zone la plus saillante du plan 1 — luminance × contraste local —, distance au centre). Rendus : `atelier/rendus/12/` (ignorés par git). Médias : tout est généré dans Blender, aucun média externe. Son : bruit rose généré par ffmpeg (`anoisesrc`).

## v1 — `v1-planche.png` : raté technique
- Le mur gauche bouchait la fenêtre (segment avant trop long) : la pièce est noire, seule une fente de lumière. Rien n'est lisible.
- La chaise au premier plan masque la table. La tasse fait 9 × 13 px (0,07 % de l'image) : **un détail que personne ne verra changer**.
- Le plan fenêtre est un rectangle noir : il ne dit pas « on regarde ailleurs », il dit « erreur ».

## v2 — `v2-planche.png` : lisible, mais clinique, et l'anomalie se cache derrière elle-même
- Le ciel trop fort aplatit tout : lumière de laboratoire, pas d'après-midi.
- Placée « en face de la chaise », la seconde tasse tombe **dans l'axe exact** de la première vue de la caméra (pentes 0,623 et 0,627) : on lit une tasse empilée, pas deux tasses. Leçon : vérifier l'anomalie **depuis la caméra**, pas sur le plan de la scène.
- Plan fenêtre : un carré gris. Abstrait, sans lumière.

## v3 — `v3-planche.png`
- La seconde tasse est maintenant devant la chaise vide : elle raconte « quelqu'un s'est assis » sans personne. C'est le bon détail.
- Le soleil tombe sur le sol à l'avant, pas sur la table : la zone chaude attire le regard **loin** de la tasse.

## v4 — `v4-planche.png` : à l'œil c'est réussi, la mesure dit le contraire
- Le soleil (rotation Z +8°) tombe sur la table ; la tasse est dans la flaque. J'étais satisfait.
- **Mesure** : la zone la plus saillante du plan 1 est la **fenêtre** (le coin clair en haut à gauche), à 34 % de la diagonale de l'anomalie. Le regard d'un spectateur qui découvre le plan va d'abord au plus clair et au plus contrasté ; l'anomalie n'a pour elle que le biais central (1,7 % du centre).
- Le plan fenêtre montrait encore le bord de la table (v4) puis un coin de table (v5) : tricherie de raccord (on verrait si les tasses y sont ou non) et cadre maladroit. Corrigé en v6 (cible plus à gauche) : mur, fenêtre, sol, rien d'autre.

## v6 — montages A (3/2/3 s), B (5/3/5 s), C (8/4/8 s) — `v6-B-planche.png`
- Grain temporel (`noise=alls=7:allf=t`) : les plans fixes respirent sans bouger. Sans lui, le plan 1 se lit comme une photo.
- Air de pièce : mesuré à **−60,2 LUFS**, inaudible : il ne sert à rien. Corrigé en v7 par mesure + gain (−42,2 LUFS).
- Durées (jugement, pas mesure de spectateur) : A trop court, le plan 3 dure 3 s, le temps de reconnaître le lieu mais pas de le *relire* ; C : à 8 s le plan 1 devient décor, l'inquiétude se dilue avant même l'anomalie. B tient.

## v7 — `v7-planche.png`, `v7-montage-planche.png` (4 / 3 / 6 s) : référence
- Focale 32 → 45 mm : la fenêtre sort presque du cadre (reste un liseré à gauche, à corriger) ; la table au soleil devient la zone la plus saillante, **à 9 % de la diagonale** de l'anomalie (contre 34 %) ; l'anomalie double de surface (0,45 % de l'image).
- Plans 1 et 3 identiques hors anomalie (écart max hors zone 0,039, bruit du rendu).
- Plan 3 plus long que le plan 1 (6 s contre 4) : le spectateur reconnaît le cadre en 1 s, puis a le temps de **comparer**. C'est l'asymétrie qui fait le travail, pas la longueur totale.
- Rien ne désigne l'anomalie : pas de zoom, pas de son, pas de musique. **Critère 3 tenu.**
- Limites : la scène est trop propre (pas de matière, pas d'objets du quotidien) : un lieu ordinaire doit être *encombré* pour que l'anomalie ait de quoi se cacher et de quoi être trouvée. La cécité au changement n'est pas mesurée sur un vrai spectateur (phase 2, test humain). Le liseré de fenêtre gauche.

## Ce que j'en retiens (versé dans `montage-regard` et `montage-grammaire`)
1. **Une anomalie à travers une coupe est invisible par défaut** (cécité au changement) : elle doit se trouver dans la zone que le plan 1 a déjà désignée (lumière, contraste, centre), sans que le plan 3 la désigne.
2. **Le plus clair gagne** : mesurer la saillance du plan avant de croire qu'on guide le regard ; une fenêtre dans le cadre vole l'attention à tout ce qui est dedans.
3. **Vérifier un raccord depuis la caméra** (deux objets alignés dans l'axe = un seul objet).
4. **Le plan de retour plus long que le plan de départ** : l'asymétrie donne le temps de comparer.
5. **Un plan fixe n'est pas une image figée** : grain temporel et air de pièce mesurés (un fond à −60 LUFS n'existe pas).

## Contre-expertise (session 9, `labo/saillance/`)
Un modèle publié (résidu spectral, Hou et Zhang 2007) confirme que la v4 est la pire (zone de l'anomalie au 63e centile), mais préfère la v3 (89e) à la v7 (75e) : la tasse blanche se détache mieux sur une table sombre que sur une table au soleil. **Éclairer la zone attire l'œil mais peut éteindre le contraste du détail.** v8 (BACKLOG 50) : flaque de lumière voisine, tasse à la lisière, sur fond plus sombre.

## v8 — lieu encombré (session 10, BACKLOG 50) — `v8-planche.png` (haut : v8a, v8b ; bas : v8c plan 1, plan 3), `v8-montage-planche.png` (4 / 3 / 6 s)
**Intention (écrite avant)** : un lieu ordinaire est encombré ; l'anomalie (la seconde tasse devant la chaise vide) doit **se cacher parmi des objets semblables** (un pot à sucre blanc, un verre) et **rester trouvable**. Hypothèse de la session 9 : flaque de lumière **à côté** de la tasse, tasse sur fond sombre.
Script : `scene_v8.py` (copie de `scene.py` + `"encombre": true` : journal, coupe de fruits, livres, pot à sucre leurre, verre, clés, étagère et bocaux, calendrier, cabas, gilet sur la chaise vide, radio). Rendu Cycles 480×270, 24 éch. : ~5 s par image.

| version | changement | maison : zone saillante → anomalie (% diag.) | résidu spectral : centile de la zone | pic du résidu → anomalie |
|---|---|---|---|---|
| v7 (réf. session 9) | pièce nue, 45 mm | 9,0 | 74,7 | — |
| v8a | encombré ; gilet caché derrière le dossier ; verre clair | 10,4 | 85,0 | 20,1 |
| v8b soleil 0° / 8° / 16° | gilet rouge **devant** le dossier, verre sombre, étagère et calendrier dans le cadre, radio | 10,2-10,4 | 88,0 / 87,9 / 84,2 | 14-16 |
| v8c (réf.) | v8b 8° + radio sombre | 10,3 | 86,6 | 15,7 |

- **v8a** : le verre clair se lisait comme une troisième tasse : trois cylindres blancs avant même l'anomalie. Un leurre, c'est bien ; trois, l'anomalie devient un objet parmi d'autres sans raison d'être cherchée. Le gilet caché derrière le dossier ne servait à rien.
- **v8b** : le gilet **rouge** sur la chaise vide est devenu la couleur la plus saturée du cadre : il désigne la place vide dès le plan 1, et dans le plan 3 la tasse blanche se détache **sur lui**. Le résidu spectral passe de 74,7 (v7) à 88 : au niveau de la v3, sans perdre la désignation de la v7. **Ce n'est pas la lumière qui a fait le travail, c'est un fond coloré derrière l'anomalie.**
- **Hypothèse de la session 9 non vérifiée** : faire tourner le soleil de 0 à 16° ne déplace presque pas la flaque (elle reste au sol, devant la table) ; écart de saillance faible (84-88). Dans cette géométrie, la lumière n'est pas le bon levier : je ne l'ai pas isolée, je n'en tire rien.
- **v8c** : assombrir la radio ne déplace pas le pic du résidu : il est sur la pile de livres (couverture blanche) — un pic secondaire, à 15 % de la diagonale, acceptable (il est dans la même moitié de table).
- **Encombrement** : il n'a pas noyé l'anomalie dans les mesures ; il a baissé la saillance de tout le reste (beaucoup de petits objets moyens). Ce qui la **cache** pour un humain, c'est le leurre de même forme (le pot à sucre à 6 cm) — et cela, aucune de mes deux mesures ne le voit : elles mesurent où va l'œil, pas si l'œil **distingue** la nouveauté. Test spectateur (PLAN-TESTS 44) indispensable.
- **Ce qui reste raté** : la pièce est encore une maquette (cubes, pas de matière, pas d'usure) ; sans soleil sur la table l'après-midi est gris, l'inquiétude devient tristesse ; le gilet est un bloc.

### Leçon (versée dans `montage-grammaire`)
Pour qu'une anomalie à travers une coupe reste trouvable dans un décor chargé : **désigner la zone par une couleur saturée dans le plan 1** (un vêtement, un objet) et **poser l'anomalie devant elle** dans le plan 3 ; un seul leurre de même forme à proximité, pas plusieurs. La couleur désigne et détache à la fois, là où la lumière désigne mais peut éteindre le contraste du détail (session 9).
