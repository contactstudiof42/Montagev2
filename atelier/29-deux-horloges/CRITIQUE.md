# Pièce 29 « Deux horloges » — critiques (session 24, 2026-10-10)

Rendus (ignorés par git) : `atelier/rendus/29/v1..v5.mp4`. Commande : `python3 piece.py vN atelier/rendus/29` (2-3 s par version).
Mesure : `python3 labo/outils/coupes.py atelier/rendus/29/v4.mp4 --edl atelier/rendus/29/v4.edl --scdet 10 --avant 4 --apres 4 --sortie …`
(11/11 coupes, 0 fausse alerte : premier usage de l'outil général sur une vraie pièce). Photosensibilité v4 : OK (4 flashs généraux sur 14 s, pire seconde 1).
Limite : je ne peux pas écouter ; le son est jugé sur l'enveloppe et la position des tics dans la bande-film (`v4-bande-coupes.png`, `v5-bande-coupes.png`).

## v1 — alternance régulière (planche `v1-planche.png`, une colonne de 3 = un plan)
- Intention servie à moitié : l'écart se lit (bâtons au mur, plante qui pousse puis se fane, lumière qui saute d'heure), sans un mot. Le principe d'*Interstellar* tient même en 2D pauvre : **l'ellipse est dans la coupe**, pas dans le plan.
- Mais c'est un métronome : 10 plans de 30 images, sauts égaux. On comprend dès le 2e retour, puis on attend la fin. Rien ne monte.
- Ici est illisible : la goutte fait 4 à 8 px dans un cadre de 480. L'horloge lente doit être **vue** pour être comptée.

## v2 — accélération (planche `v2-planche.png`)
- Les plans d'ici raccourcissent (62 → 14 images), les sauts de là-bas grandissent (puissance 2,2 : semaines puis années). La tension monte, c'est mieux.
- Fin ratée : le dernier retour dure 16 images (0,6 s). Le coup de grâce passe avant qu'on l'ait regardé.
- Ici toujours trop petit.

## v3 — v2 + son (tic de 1,25 s entendu partout, silence au dernier retour)
- Même image que v2. Le tic, indépendant des coupes, donne une pression continue. Mesuré −33,6 LUFS intégré (maquette, non normalisée).

## v4 — corrections (planche `v4-planche.png`)
- Ici en macro (recadrage ×3 sur le bec) : la goutte se lit dès la 1re image, et sa croissance se voit d'un plan d'ici au suivant. **Chaque ligne a besoin d'un indicateur lisible de son temps** : la goutte ici, les bâtons là-bas.
- Dernier retour tenu 66 images (2,6 s) qui s'assombrit ; la plante est morte ; **les bâtons n'ont pas bougé depuis le retour précédent** : plus personne ne compte. C'est l'idée la plus forte de la pièce (l'absence dite par ce qui n'a *pas* changé), mais elle est fragile : le retour précédent ne dure que 14 images, le spectateur n'a peut-être pas mémorisé le nombre de bâtons. À tester sur quelqu'un (phase 2). Renfort possible : un bâton commencé, inachevé.
- Le tic tombe n'importe où par rapport aux coupes (écart 0 à 8 images, `v4-bande-coupes.png`) : pression d'ambiance, sans sens.

## v5 — chaque retour à là-bas tombe sur un tic (planche `v5-planche.png`) → **référence**
- Les 6 retours sont sur un tic (écart 0). Le tic **devient la cause** : à chaque tic, on voit ce qui a été perdu là-bas. C'est le contrat qu'on prête au tic d'*Interstellar* (« chaque tic = un jour sur Terre », souvent cité, non confirmé) que v4 ne faisait qu'évoquer.
- Et la règle apprise rend la fin plus forte : le tic s'arrête à la chute de la goutte, le dernier retour arrive **sans tic**. La règle enseignée cinq fois puis rompue fait entendre l'absence ; dans v4, le même silence n'était qu'un silence.
- Prix payé : les derniers retours tombent tous les 31 images, c'est mécanique sur la fin ; les plans d'ici ne raccourcissent plus régulièrement (41, 43, 13, 17, 19). Acceptable : la mécanique est le sujet (une horloge).
- Piège technique trouvé : un tic de 1,25 s à 25 i/s tombe toutes les **31,25 images**, donc à ±1 image de la coupe selon l'arrondi (visible dans la bande : le tic précède parfois la coupe d'une image). À 24 i/s, 1,25 s = 30 images pile. **Si l'on coupe sur une pulsation, choisir un tempo qui tombe sur des images entières à la cadence du projet** (à 25 i/s : 1,24 s = 31 images, 1,28 s = 32).

## v6 — v5 + un bâton commencé, jamais fini (`v6-detail-baton.png` : avant / dernier retour, recadré ×2)
- L'idée est juste (la phrase de l'histoire tient dans un trait de 7 px), mais **illisible au cadre** : à 480 px, le demi-bâton fait 7 px dans un plan large qui s'assombrit. Le détail qui porte la fin ne peut pas rester un détail.

## v7 — v6 + poussée lente vers le mur pendant le dernier retour (`v7-fin.png`) → **nouvelle référence**
- Poussée de ×1 à ×2,6 en 2,4 s (cosinus), centrée sur les bâtons : l'œil est conduit au trait inachevé **sans coupe**, la tenue est préservée. Fin lisible : plante morte + un bâton à moitié tracé.
- 1er essai raté : la poussée dérivait et coupait le bâton au bord du cadre. Un mouvement de caméra qui désigne un détail se cadre sur la position **finale** du détail, pas sur sa trajectoire.
- Photosensibilité OK. Prix : la poussée est un geste d'auteur qui « appuie ». Une coupe vers un insert serait plus sèche ; la poussée garde la tenue. J'assume la poussée, lente, une seule fois dans la pièce.

## v8 — vertical 9:16, les deux horloges empilées (écran partagé, sans alternance ; `v8-planche-vertical.png`, une image par seconde)
- 1er essai raté : recadrages déformés (goutte étirée) et bâtons hors cadre ; refait en recadrant sans redimensionner.
- On voit tout en permanence : la goutte grossit en continu en haut, la pièce saute en bas. L'écart se **comprend** mieux (c'est un schéma, presque une vulgarisation), mais il ne se **sent** plus : on ne quitte jamais une ligne, donc on ne revient jamais découvrir ce qu'on a perdu. Les sauts du bas se lisent comme des jump cuts d'un accéléré.
- Règle : **l'alternance fait sentir la perte (on s'absente), l'écran partagé fait comprendre l'écart (on compare)**. En vertical, choisir selon l'intention : écran partagé pour un Short explicatif, alternance plein cadre pour l'émotion (le 9:16 coupé en deux donne deux bandes de 270×238 : chaque compteur doit y rester lisible).

## Confrontation avec les grandes références (`culture/montage-alterne-grandes-references.md`, sous-agent, session 24)
- **Confirmé** : compteur par ligne, tic indépendant = pression, accélération des segments, règle apprise puis rompue.
- **Contredit** : (1) ma fin régulière (retours toutes les 31 images) : Griffith, *Le Parrain*, *Dunkirk* accélèrent jusqu'au bout ; (2) ma « fin tenue » n'a pas d'appui chez eux : leurs alternances finissent par **une rencontre des lignes** (le sauvetage, les meurtres qui convergent vers Michael). Ma pièce n'a pas de jonction : c'est un parti pris (les lignes ne se rejoignent jamais = la perte définitive), à défendre comme tel, pas à citer comme Interstellar ; (3) chez eux la causalité vient de la jonction ou d'un point d'ancrage, pas d'un tic sur la coupe ; (4) **l'ironie** (le son d'une ligne posé sur l'autre, le baptême sur les meurtres) manque : piste v9, faire entendre la goutte sur le mur aux bâtons.

## Ce que la pièce m'apprend (versé dans `montage-rythme` et `montage-references`)
1. Montage alterné à deux vitesses : l'ellipse est dans la coupe ; dans le plan, le temps des deux lignes doit presque s'arrêter (sinon on lit un accéléré, pas un écart, et un jour/nuit accéléré clignote).
2. Chaque ligne a besoin de son **compteur visible** (goutte, bâtons, plante) ; sans compteur, l'écart n'est qu'une affirmation.
3. Une pulsation sonore indépendante des coupes = pression. La même pulsation **sur** les coupes = causalité. Choisir selon qu'on veut l'angoisse diffuse ou la perte comptée.
4. Pour un final par l'absence : enseigner une règle (tic = perte), puis la rompre au dernier retour.
5. La fin d'un montage qui accélère doit être **tenue** (≥ 2 s) : l'accélération prépare, la tenue fait mal.
6. Le détail qui porte la fin doit être **amené à la taille de lecture** (poussée lente ou insert) : une idée de 7 px n'existe pas.

## Reste (BACKLOG Y39)
Tester v4 / v5 sur un spectateur (phase 2) ; version 9:16 ; vraie matière (Blender, lumière de fenêtre physique).
