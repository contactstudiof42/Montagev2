# Pièce 09 « Générique de l'équipe » — intention (écrite avant de créer)

Session 7, 2026-10-10. BACKLOG 36. Principe tiré de `culture/enter-the-void-generique-noe-tom-kan.md` (Noé / Tom Kan), relié à votre goût pour le kinetic editing (`GOUTS.md`).

## Le sujet
Un générique de 10 s pour une équipe fictive (noms inventés), sur une boucle électronique à 128 BPM que je fabrique. Aucun média tiers ; polices libres installées dans la VM (licences notées dans `fonts.md`).

## Ce que je veux faire ressentir
Un **sas** : on entre dans un état (l'énergie d'un club, une montée) avant d'entrer dans l'histoire. Pas une liste de noms qu'on lit, une **vague** qui monte et se pose sur un titre.

## Principes à mettre à l'épreuve
1. **Une coupe = une rupture de forme** : chaque carton change au moins police, teinte et échelle. Règle de génération : une police par « personnalité » de métier (le monteur en chasse fixe, le chef op en italique fine, le son en bitmap…).
2. **Son verrouillé d'abord** : la boucle et ses temps sont fixés ; les durées des cartons en découlent (1 temps, puis ½, puis ¼ de temps en croches), jamais l'inverse.
3. **Le chaos a besoin d'une courbe** : accélération vers un sommet, puis un titre tenu 1,5 s en silence relatif.
4. **Photosensibilité** : la v1 « naïve » (fonds noir / blanc alternés) devrait échouer au contrôle `labo/photosensibilite/flash_check.py` ; la v2 obtient l'effet stroboscopique **à luminance constante** (teinte, forme). Question : garde-t-elle l'énergie ?
5. Contrôle : v3 avec **une seule police** (Inter) et les mêmes durées. Si v3 frappe autant, le principe 1 est faux.

## Critères de réussite
- La courbe se lit sur la planche (cartons de plus en plus courts, puis un titre qui respire).
- Chaque coupe change au moins deux paramètres forts (mesuré : police, teinte du fond, échelle).
- `flash_check.py` : OK sur la version livrable.
- Les noms restent lisibles au moins au début (au sommet, on accepte de ne plus lire : c'est l'effet).
