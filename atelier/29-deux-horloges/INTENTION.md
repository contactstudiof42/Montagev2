# Pièce 29 « Deux horloges » — intention (session 24, 2026-10-10)

**Goût de l'utilisateur : *Interstellar*, pour son rythme.** Principe tiré de `culture/interstellar-rythme.md` :
deux horloges qui ne tournent pas à la même vitesse, et le montage alterné les fait se frotter. Jamais testé en atelier.

**Ce que la pièce doit faire ressentir** : l'angoisse du temps perdu ailleurs. Ici, une goutte met 12 s à se former
au bec d'un robinet ; là-bas, à chaque retour, des semaines puis des années ont passé. Le spectateur doit sentir
l'écart **à la coupe**, pas parce qu'on le lui dit (aucun texte, aucun compteur).

**Matériau** : 2D générée (numpy + Pillow), 480×270, 25 i/s, 12 s ; son synthétique (numpy). Aucun média tiers.
- Ici (A) : gros plan froid, un bec de robinet, une goutte qui grossit puis tombe à la fin.
- Là-bas (B) : une pièce chaude vue de face, une fenêtre, une plante, des bâtons comptés au mur, la tache de soleil au sol.
  Dans un plan B, le temps ne court presque pas (la lumière dérive à peine) : **l'ellipse est dans la coupe**.
  (Raison technique aussi : un jour/nuit accéléré dans le plan clignoterait, photosensibilité.)

**Versions prévues**
- v1 : alternance régulière (un plan toutes les 30 images), sauts de B constants. Hypothèse : mécanique, l'écart se lit mais ne monte pas.
- v2 : les plans raccourcissent vers la chute de la goutte, les sauts de B grandissent (semaines → années) ; fin : la goutte tombe, retour à B vide.
- v3 : v2 + le son. Un tic régulier (1,25 s, chiffre souvent cité pour *Interstellar* mais non confirmé, voir la fiche) est l'horloge d'ici et **reste audible sur les plans de là-bas** ; à la chute, le tic s'arrête et B est tenu 2 s en silence.

**Critères de réussite** : sans texte, un spectateur dit « là-bas le temps file » avant la moitié ; le dernier retour à B fait mal ; pas de clignotement (contrôle photosensibilité) ; la goutte reste lisible à 480 px.
