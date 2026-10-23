# « L'Air » — les plans et leurs raccords (J-cut, L-cut), V2

_Session de génération, 2026-10-23, d'après `script.md` V4 (commit 842184c), corrigé par Diego le même jour : « pas assez la caméra sur lui ; sur le "Later" la caméra doit être sur lui ; son départ avec les entraves, la caméra doit être sur lui et il doit sortir du cadre ». Écrit en liste, pas en tableau (Diego). J-cut : on entend le plan suivant avant de le voir. L-cut : le son du plan continue sur l'image du suivant. Le découpage de `script.md` est à aligner sur cette version (conversation d'écriture)._

## Le principe
- Une réplique dite **hors champ**, ou un son fait **en post** (sifflements, serrure, cliquetis, chaîne, couloir), se pose où l'on veut : c'est ce qui permet les J-cut et L-cut.
- Une réplique dite **à l'écran** est liée aux lèvres de sa prise.
- Pour avoir de quoi couper, les échanges se tournent **comme un vrai champ-contrechamp** : une prise continue sur lui, une prise continue sur elle, chacun joue ses répliques à l'écran et **écoute** pendant celles de l'autre (dites hors champ, avec les voix de référence). Au montage, chaque réplique prend le son de la prise où l'on voit la bouche ; l'écoute de l'autre se taille librement autour.

## Les plans (13, environ 46 s, durée souple)
**1 — 0:00 à 0:05 — plan large, fixe, à hauteur de table**
Face à face, de profil ; le dôme couvert au plafond. Il siffle la première phrase de l'air (post).
→ **L-cut** : sa dernière note tient sur le plan d'elle.

**2a — 0:05 à 0:08 — rapproché sur elle**
Elle pince les lèvres, souffle ; la flamme se couche.
→ **J-cut** : son « No. » à lui tombe sur la flamme couchée, avant qu'on le voie.

**2b — 0:08 à 0:11 — sur lui**
« No. That's how you blow out a candle. » (à l'écran).
→ **coupe franche** : il arrondit la bouche, exagérément.

**3 — 0:11 à 0:16 — sur lui, par-dessus l'épaule d'elle** (son voile en amorce, flou)
Il lui montre la bouche ronde. Elle, hors champ : « Nuns don't whistle. » Il tapote la table : « Nobody'll hear. » (à l'écran).
→ **J-cut** : on entend son inspiration à elle sur la fin du plan, puis on coupe sur elle au moment de la note.

**4a — 0:16 à 0:19 — rapproché sur elle**
La note grêle, cassée (post) ; ses sourcils se lèvent.
→ **coupe franche** sur son regard à lui vers la croix.

**4b — 0:19 à 0:22 — sur lui**
Un coup d'œil vers la croix : « See? He didn't strike you down. » (à l'écran).
→ **L-cut** : la fin de sa phrase tient sur elle, qui ne sourit pas.

**5a — 0:22 à 0:25 — rapproché sur elle**
Elle regarde sa montre : « There's something I have to tell you… » (à l'écran).
→ **L-cut** : la fin de sa phrase tient sur lui, qui écoute.

**5b — 0:25 à 0:28 — sur lui**
Il l'écoute, pose sa grosse main sur la table, vers elle (la main peut sortir du cadre par le bas). Doucement : « Later. » (à l'écran, choix de Diego).
→ **J-cut** : le bourdonnement de la serrure commence sur son visage, juste après « Later. » ; on coupe sur le plan à deux au claquement du pêne.

**6 — 0:28 à 0:31 — plan à deux**
Ils se figent ; elle regarde la porte, lui ne regarde qu'elle. Sous le linge, la lumière rouge s'allume (post).
→ **raccord dans le mouvement** : il commence à se lever dans les 4 dernières images du 6, on coupe pendant le lever ; au 7a la caméra l'accompagne en remontant jusqu'au cadre à la taille (corrigé le 2026-10-24 : un cadre fixe à la taille coupait leurs têtes assises en bas de l'image). Le cliquetis du métal tombe sur son lever.

**7a — 0:31 à 0:34 — plan à deux, cadré à la taille**
Il se lève et la domine ; elle se lève à son tour : « I'll pray for you. » (à l'écran).
→ **coupe franche** sur lui, qui la regarde.

**7b — 0:34 à 0:39 — sur lui, en pied, fixe**
Il siffle trois notes, tout bas (post). La porte s'ouvre à côté de lui, le bruit du couloir entre d'un coup (post). Il se tourne et **sort du cadre** à petits pas ; on voit les entraves et la chaîne qui traîne pendant qu'il marche. Le cadre reste vide un instant, la lumière froide du couloir sur le sol.
→ **coupe sèche, son compris** : la porte se referme (hors champ), tout le bruit se coupe net sur la coupe. Pas de L-cut : le silence est le coup.

**8a — 0:39 à 0:41 — gros plan sur ses mains à elle**
Elles cherchent le chapelet, commencent à se joindre, s'arrêtent. La ventilation, très loin.
→ **J-cut** : sa première note sifflée (post) commence sur ses mains arrêtées.

**8b — 0:41 à 0:46 — elle, de profil, devant la chaise vide**
Elle siffle l'air jusqu'au bout ; la lumière du dôme est éteinte.
→ **L-cut** : la dernière note résonne une seconde sur le noir, puis le titre.

Répartition : sur lui 2b, 3, 4b, 5b, 7b (environ 19 s) ; sur elle 2a, 4a, 5a, 8a, 8b (environ 15 s) ; à deux 1, 6, 7a (environ 11 s).

## Ce que ça demande à la génération
- **Prise continue sur lui** (2b, 3, 4b, 5b, environ 18 s, même axe, fixe) : il dit ses répliques à l'écran et écoute les siennes à elle, dites hors champ. **Prise continue sur elle** (2a, 4a, 5a, environ 14 s) : l'inverse. Voix de référence pour les deux.
- Plans seuls, avec 1 s de marge : 1, 6, 7a, 7b (6 s : sortie complète et cadre vide), 8a, 8b.
- Les entraves n'apparaissent que dans la prise du 7b ; avant, aucun cadre ne montre le sol ni ses jambes (le 7a est cadré à la taille).
- « Later. » est à l'écran : c'est la prise de la prise continue sur lui qui décide du film ; en générer plusieurs, et garder le plan B (réplique faite dans ElevenLabs, puis synchronisée sur les lèvres).
