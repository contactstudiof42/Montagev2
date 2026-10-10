# Pièce 31 « Le même escalier » — intention (session 24, 2026-10-10)

**Goût de l'utilisateur : *Joker*, pour sa couleur et son image.** Principe n°3 de `culture/joker-couleur-image.md` :
**inverser un même décor** — on revient au même lieu en changeant la lumière (froid de face → chaud en contre-jour),
la hauteur de caméra (haute → basse) et le corps (voûté → ouvert). Dans le film : l'escalier monté au crépuscule, redescendu en dansant.

**Question** : combien de paramètres faut-il inverser pour que le retour se lise comme une **transformation** du personnage,
sans que le lieu cesse d'être **reconnu** ? Hypothèse : la lumière seule change l'heure, pas l'homme ; il faut au moins
lumière + hauteur ; le corps finit la phrase.

**Matériau** : Blender 4.2 (Cycles CPU, 480×270), un escalier urbain entre deux murs, un réverbère, une silhouette simple.
Images fixes (le mouvement de caméra, 3e levier du film, n'est pas testé ici : limite notée).
- R1 aller : crépuscule froid, lumière de face, caméra haute plongeante, corps voûté.
- R2 : seule la lumière s'inverse (soleil bas chaud en contre-jour en haut des marches).
- R3 : lumière + caméra basse en contre-plongée.
- R4 : lumière + caméra + corps ouvert (bras écartés, buste droit).
- R5 (contrôle) : seule la caméra s'inverse, lumière froide.

**Mesures** : reconnaissance du lieu = corrélation des contours (Sobel) avec R1 sur la zone du décor ; transformation =
écart moyen de chrominance (a*, b*) et de luminance. **Puis le jugement sur la planche, qui prime.**
