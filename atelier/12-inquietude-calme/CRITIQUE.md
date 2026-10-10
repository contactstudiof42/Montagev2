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
