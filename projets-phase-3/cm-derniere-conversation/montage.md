# « L'Air » — les plans et leurs raccords (J-cut, L-cut)

_Session de génération, 2026-10-23, d'après `script.md` V4 (commit 842184c). Écrit en liste, pas en tableau (Diego). J-cut : on entend le plan suivant avant de le voir. L-cut : le son du plan continue sur l'image du suivant._

## Le principe qui rend les J-cut et L-cut possibles en IA
- Une réplique dite **hors champ**, ou un son fait **en post** (sifflement, serrure, chaîne, couloir), n'est attachée à aucune image : on la pose où l'on veut, on la prend dans n'importe quelle prise, même une prise en 480p dont on ne garde pas l'image, ou dans ElevenLabs.
- Une réplique dite **à l'écran** est liée aux lèvres de sa prise : elle ne peut pas déborder sur un autre plan sans que la bouche se voie.
- Donc : chaque plan généré seul, avec **une seconde de marge avant et après** (on y demande l'écoute, bouche fermée), et une voix de référence par personnage. Une génération qui regroupe plusieurs plans ne laisse aucun chevauchement entre deux axes, donc aucun J-cut ni L-cut au montage. Cela remplace le regroupement en deux générations de `generation.md`.

## Les plans
**Plan 1 — 0:00 à 0:05 — plan large, fixe, à hauteur de table**
Ils sont face à face, de profil ; le dôme couvert dans l'angle du plafond. Il siffle la première phrase de l'air (en post).
Vers le plan 2 : **L-cut**. La dernière note de son sifflement tient sur le gros plan d'elle qui pince les lèvres.

**Plan 2 — 0:05 à 0:09 — plan rapproché sur elle**
Elle souffle, la flamme se couche. Lui, hors champ : « No. That's how you blow out a candle. »
Sa réplique est hors champ : elle vient de la meilleure prise, où qu'elle soit.
Vers le plan 3 : **coupe franche sur l'action**, quand il arrondit la bouche pour lui montrer.

**Plan 3 — 0:09 à 0:15 — plan à deux, serré, au-dessus de la table**
Il lui montre, elle le regarde, raide. Elle : « Nuns don't whistle. » Lui : « Nobody'll hear. » (les deux à l'écran). Il tapote la table.
Vers le plan 4 : **J-cut**. On entend son inspiration à elle sur la fin du plan 3 (lui qui tapote), puis on coupe sur elle au moment où sort la note grêle (en post).

**Plan 4 — 0:15 à 0:20 — rapproché sur elle, puis raccord sur lui**
La note cassée, ses sourcils qui se lèvent. Lui, un coup d'œil vers la croix : « See? He didn't strike you down. » (à l'écran).
Vers le plan 5 : **L-cut**. La fin de sa réplique tient sur le gros plan d'elle qui ne sourit pas.

**Plan 5 — 0:20 à 0:25 — rapproché sur elle**
Elle regarde sa montre : « There's something I have to tell you… » (à l'écran). Sa grosse main entre dans le cadre et se pose près de la sienne. Lui, hors champ : « Later. »
**« Later. » reste hors champ** : on voit la réplique arriver sur elle, et on choisit la meilleure des prises, ou une voix ElevenLabs, sans contrainte de lèvres. La réplique dont tout dépend devient la plus libre du film.
Vers le plan 6 : **J-cut**. Le bourdonnement de la serrure commence sur son visage, juste après « Later. » ; on coupe sur le plan à deux au claquement du pêne.

**Plan 6 — 0:25 à 0:28 — plan à deux**
Ils se figent ; elle regarde la porte, lui ne regarde qu'elle. Sous le linge, la lumière rouge s'allume (en post).
Vers le plan 7a : **coupe franche sur le mouvement**, quand il commence à se lever ; le cliquetis du métal tombe sur son lever.

**Plan 7a — 0:28 à 0:31 — plan à deux, cadré à la taille**
Il se lève et la domine ; elle se lève à son tour. Elle : « I'll pray for you. » (à l'écran).
Vers le plan 7b : **L-cut court**. Le silence qui suit sa réplique tient sur le plan large ; ses trois notes sifflées (en post) sont sa réponse, dans le plan large.

**Plan 7b — 0:31 à 0:35 — plan large, fixe**
Les trois notes ; la porte s'ouvre, le bruit du couloir entre d'un coup (en post) ; il sort à petits pas, la chaîne traîne.
Vers le plan 8a : **coupe sèche, son compris**. La porte se referme et tout le bruit du dehors se coupe net, sur la coupe même. Pas de L-cut ici : le silence est le coup.

**Plan 8a — 0:35 à 0:38 — gros plan sur ses mains**
Elles cherchent le chapelet, commencent à se joindre, s'arrêtent. La ventilation, très loin.
Vers le plan 8b : **J-cut**. La première note de son sifflement (en post) commence sur ses mains arrêtées ; on comprend son choix à l'oreille avant de la voir, puis on coupe sur son profil.

**Plan 8b — 0:38 à 0:43 — elle, de profil, devant la chaise vide**
Elle siffle l'air jusqu'au bout ; la lumière du dôme est éteinte.
Vers le noir : **L-cut**. La dernière note résonne une seconde sur le noir, puis le titre.

## Ce que ça demande à la génération
- Chaque plan généré seul, 1 s de marge avant et après, écoute bouche fermée dans les marges.
- Répliques à l'écran (dans leur prise) : plans 3, 4, 5 (la sienne à elle) et 7a.
- Répliques hors champ (à prendre dans n'importe quelle prise ou dans ElevenLabs) : plan 2 et « Later. » au plan 5. Les générer en 480p suffit, puisqu'on n'en garde que le son.
- Tous les sifflements et les sons de la révélation : en post.
- Une nappe d'ambiance continue sous tout le film, coupée seulement au plan 7b → 8a.
