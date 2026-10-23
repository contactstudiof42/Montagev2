# « L'Air » — prompts d'images GPT

_2026-10-24. Modèle : **GPT Image 2.5 Sunburst** (choix de Diego). C'est la version lente et précise de GPT Image 2.5, sortie en septembre 2026 ; Flare est la version rapide. Dans l'API, le modèle s'appelle `gpt-image-2.5-sunburst`. Dans ChatGPT, rien ne dit clairement quelle version tourne par défaut ; un test indépendant penche pour Flare [SOURCÉ] (mindstudio.ai, morphic.com). Les prompts sont en anglais. Un résumé en français suit chaque prompt._

## Les fiches personnage

### Ce qu'on attend des fiches
- **Elles servent de référence d'identité à Seedance** (visage, corps, costume), pas d'image de film. La lumière et la couleur du film viennent des prompts de plan et de la bible de look (`da.md`). (méthode des pros, `montage-ia-generative/prompts-seedance-pros.md`)
- **Lumière de studio neutre sur un fond gris moyen.** La chemise blanche de lui disparaîtrait sur le fond blanc qu'utilisent les pros. (moi)
- **Deux images par personnage**, une en pied (quatre vues) et une du visage (trois vues), puis **une image des deux ensemble** pour l'écart de taille (1,95 m contre 1,50 m). Sur deux fiches séparées, cet écart ne se lit pas. (moi)
- **Aucune entrave, aucune menotte, aucun uniforme, aucun tatouage** (`script.md`, tableau des personnages). Les entraves n'apparaîtront que dans le prompt du plan 7b.
- **Les visages** (Diego, 2026-10-24) : « pour le personnage grand, un visage type Pedro Pascal ; pour la nonne, un visage type Rosemary Harris ». **Les prompts décrivent ce type de visage sans jamais nommer les acteurs.** Deux raisons : GPT refuse la ressemblance avec une personne réelle, et un sosie relève de l'article 50 de l'AI Act (deepfake à signaler). Le contrôle vérifie qu'on retrouve le type sans obtenir un sosie. Ce type de visage éloigne aussi le personnage de John Coffey (`script.md`). Le corps de colosse vient du scénario, pas de l'acteur.
- **Format 3:2 horizontal** (1536 × 1024) : quatre silhouettes en pied tiennent mieux qu'en 16:9.

### F1 — Lui, en pied

> Character reference sheet, live-action photograph. The same man shown four times side by side, full body, standing, neutral pose, arms relaxed: front view, three-quarter view, side profile, back view. Evenly spaced, same scale, same height in frame, feet visible.
> The man: about 30 years old, a giant, 1.95 m tall, very heavy and broad, shoulders like a furniture mover, a thick neck, enormous hands. A Latin American man with warm olive skin. Short dark brown hair, slightly wavy, a little tousled. Thick dark eyebrows, warm dark brown eyes with deep laugh lines at the corners, a strong straight nose, a short trimmed dark beard shadow. A calm, slightly ironic face, a hint of melancholy, not threatening.
> Wardrobe: his own clothes, dressed as for an occasion. A clean white cotton shirt with every button fastened, including the top collar button: the collar is closed tight around his thick neck in all views, no open neck, no visible throat skin below the collar. No tie, sleeves down and buttoned at the cuffs, slightly tight on his shoulders. Plain dark charcoal trousers, black leather shoes, worn but polished.
> No tattoos, no scars, no jewelry, no handcuffs, no shackles, no restraints, no uniform.
> Plain mid-grey seamless studio background, soft even studio lighting, neutral white balance, true colors. Natural skin texture with pores, real fabric creases. 50mm lens, sharp focus on all four figures. Not CGI, not a 3D render, not an illustration. No text, no labels, no numbers.

_Résumé : le même homme quatre fois (face, trois-quarts, profil, dos), en pied, sur fond gris. Colosse de 30 ans, latino-américain, peau olive, cheveux bruns courts un peu ondulés, sourcils épais, yeux bruns rieurs, barbe de quelques jours, chemise blanche fermée jusqu'au col, pantalon sombre, chaussures noires cirées mais usées. Ni tatouage, ni entrave, ni uniforme._

### F2 — Lui, le visage

> Character reference sheet, live-action photograph. The exact same man as in @Image1, same face, same hair, same beard: his head and shoulders shown three times side by side: front view, three-quarter view, side profile. Same scale, eyes at the same height.
> About 30 years old, a giant with a thick neck and very broad shoulders. A Latin American man with warm olive skin. Short dark brown hair, slightly wavy, a little tousled. Thick dark eyebrows, warm dark brown eyes with deep laugh lines at the corners, a strong straight nose, a short trimmed dark beard shadow. A calm, slightly ironic face, a hint of melancholy, not threatening. White shirt buttoned to the collar.
> Neutral expression, mouth closed, looking straight ahead in each view.
> Plain mid-grey seamless studio background, soft even studio lighting, neutral white balance. Natural skin texture with pores, real skin, no retouching. 85mm lens. Not CGI, not a 3D render, not an illustration. No text, no labels.

_Résumé : son visage en trois vues (face, trois-quarts, profil), expression neutre, même fond gris et même lumière._

### F3 — Elle, en pied

> Character reference sheet, live-action photograph. The same woman shown four times side by side, full body, standing, neutral pose: front view, three-quarter view, side profile, back view. Evenly spaced, same scale, feet visible.
> The woman: a Catholic nun about 75 years old, tiny, 1.50 m tall, thin, slightly hunched. A deeply wrinkled face, thin bony hands. An English woman with very fair, thin, papery skin. A fine, delicate bone structure, high cheekbones, a small straight nose, thin lips. Pale grey-blue eyes, sharp and attentive, with a gentle warmth behind them. A dignified, quietly kind face.
> Wardrobe: a classic traditional habit, ankle-length, in very dark navy wool, and a matching dark veil over a white coif framing the face. A simple wooden rosary hanging from a cord at her waist. A small old wristwatch with a leather strap and a round dial with hands on her left wrist. Plain black flat shoes.
> No jewelry other than the rosary and the watch, no glasses, no modern clothing.
> Plain mid-grey seamless studio background, soft even studio lighting, neutral white balance, true colors. Natural skin texture, real wool texture and folds. 50mm lens, sharp focus on all four figures. Not CGI, not a 3D render, not an illustration. No text, no labels, no numbers.

_Résumé : la même religieuse quatre fois, en pied. 75 ans, anglaise, minuscule, voûtée, très ridée, peau très claire et fine, traits délicats, pommettes hautes, yeux gris-bleu vifs et doux. Habit et voile classiques bleu nuit très sombre, guimpe blanche, chapelet de bois à la ceinture, petite montre à aiguilles au poignet gauche._

### F4 — Elle, le visage

> Character reference sheet, live-action photograph. The exact same woman as in @Image1, same face, same habit: her head and shoulders shown three times side by side: front view, three-quarter view, side profile. Same scale, eyes at the same height.
> A Catholic nun about 75 years old, tiny, thin, slightly hunched. A deeply wrinkled face. An English woman with very fair, thin, papery skin. A fine, delicate bone structure, high cheekbones, a small straight nose, thin lips. Pale grey-blue eyes, sharp and attentive, with a gentle warmth behind them. A dignified, quietly kind face. Very dark navy veil over a white coif framing the face.
> Neutral expression, lips pressed together, looking straight ahead in each view.
> Plain mid-grey seamless studio background, soft even studio lighting, neutral white balance. Natural skin texture, every wrinkle visible, no retouching. 85mm lens. Not CGI, not a 3D render, not an illustration. No text, no labels.

_Résumé : son visage en trois vues, lèvres pincées, même fond gris et même lumière._

### F5 — Les deux, pour l'échelle

> Live-action photograph, scale reference. The man from @Image1 and the woman from @Image2, exact same faces, standing side by side, full body, both facing the camera, on a plain mid-grey seamless studio background. He is 1.95 m tall, she is 1.50 m: the top of her veil reaches the middle of his chest. Same wardrobe as the reference sheets. Soft even studio lighting, neutral white balance, 35mm lens at chest height, both fully in frame with feet visible. Not CGI, no text.

_Résumé : les deux côte à côte, en pied ; le haut de son voile arrive au milieu de la poitrine de lui. Se génère après F1 à F4, en joignant F1 et F3 comme références._

## Ordre de travail
1. F1, puis F2 à partir de F1 jointe : le même visage d'une fiche à l'autre.
2. F3, puis F4 à partir de F3 jointe.
3. F5 avec F1 et F3 jointes.
4. Contrôle à l'œil, en pleine résolution, avant de passer aux décors : même visage entre les vues ; ni tatouage, ni menotte ; montre à aiguilles visible ; chemise boutonnée jusqu'au col ; le type de visage demandé par Diego, sans en faire un sosie ; écart de taille juste sur F5.

## Les décors

### Ce qu'on attend des décors
- **D1 est la plaque maîtresse** : le plan large du plan 1, éclairé avec le look complet de `da.md`. Elle sert d'« autorité » pour la couleur et la matière des plaques suivantes (méthode des pros, `prompts-seedance-pros.md`) : chaque autre plaque se fera avec le rendu Blender de sa caméra (`@Image1`, pour la géométrie) et D1 (`@Image2`, pour le look). Diego juge D1 avant qu'on fasse les autres.
- **Le rendu Blender ne donne que la géométrie** : place de la caméra, cadrage, emplacement des objets. Ses couleurs roses et ses matières lisses sont celles d'une previz ; le prompt dit de ne pas les reprendre.
- **Pièce vide**, chaises vides, dôme éteint (sa lumière rouge se pose en post, `generation.md`).
- **16:9** (le format de génération ; recadrage 2,39 au montage, `da.md`).

### D1 — La pièce, plan large (plan 1)

> Live-action film still, 16:9, wide shot of an empty room, no people. Use @Image1 only for the geometry: camera position, framing, perspective and the placement of every object. Do not copy its flat pink colors or its smooth 3D materials.
> The room: a tiny prison chaplaincy, about 3 by 3.5 meters, timeless and analog. Cinder block walls painted a dirty beige, the paint chipped and stained, scuffed at chair height. A plain wooden cross, worn and patinated, on the back wall. High on the back wall, a narrow vertical window of frosted glass in a metal frame.
> In the middle, a scratched old wooden table and two simple wooden chairs facing each other across it, both empty. On the table, at the center, a single candle burning inside a short glass. At the near edge of the table, a plastic meal tray, untouched: a full plate of meat, vegetables and bread, a plastic cup, a paper napkin, cutlery.
> In the top left corner of the ceiling, a small security camera dome, entirely covered by a folded white cloth, small but readable. Its light is off.
> Light, the only two sources: a soft, diffuse, static magenta glow (#C2185B) from a city neon sign somewhere behind the frosted window, spilling down the back wall and catching a light haze in the air; and the warm amber light of the candle (#FF9F43), a small pool on the table with a soft halo. Deep blacks (#0B0A10) in the corners, under the table and along the floor, still holding texture. No other light, no ceiling lamp.
> Shot on 35mm film, 24mm lens at table height, fine film grain, gentle halation around the window and the flame. Not a video game render, not CGI, live-action cinema. No people, no text, no logos, no screens, no holograms, no rainbow neon.

_Résumé : la pièce vide, cadrée comme le plan large Blender. Parpaing beige sali, croix de bois patinée, fenêtre haute en verre dépoli. Table abîmée, deux chaises vides, bougie dans un verre, plateau-repas intact. Dôme couvert du linge blanc, éteint, dans l'angle du plafond. Seules lumières : le magenta doux et immobile du néon de la ville à travers la fenêtre, avec une légère brume, et l'ambre de la bougie. Noirs profonds qui gardent de la matière. Pellicule 35 mm, grain fin, halos._

## Résultats des fiches (2026-10-24)
_Images dans `CM TEST /04_gpt/fiches/`, chacune avec ses réglages en JSON ; dépenses dans `journal-oxen.csv` (6 images Oxen, 0,31 $)._
- **F1 retenue : `F1_chatgpt.png`**, générée dans ChatGPT (choix de Diego). Les deux versions Oxen sont écartées : v1 au col ouvert ; v2 au col fermé, mais avec un visage plus lourd, moins proche du type demandé.
- **F2 : `F2_v1.png`**, faite avec F1 jointe. Même visage, col fermé. [VU SUR IMAGES]
- **F3 : `F3_v1.png`**. Même visage dans les quatre vues ; montre à aiguilles et bracelet de cuir au poignet gauche ; chapelet de bois. [VU SUR IMAGES]
- **F4 : `F4_v1.png`**, faite avec F3 jointe. Même visage. Écart : elle sourit un peu au lieu de pincer les lèvres. [VU SUR IMAGES]
- **F5 : `F5_v1.png`**, faite avec F1 et F3 jointes. Écarts notés, sans reprise faute d'accord de Diego : elle mesure 0,70 fois sa taille à lui, soit 1,37 m s'il fait 1,95 m (cible : 0,77, soit 1,50 m) ; il est moins massif que sur F1. Correction possible : « the top of her veil reaches his collarbone; he is as broad and heavy as in @Image1 ». [mesure faite à l'œil sur les pixels, à ± 10 px]

## Résultat de D1 (2026-10-24)
_`CM TEST /04_gpt/decors/D1_v1.png`, 1920 × 1088, 0,05 $._
- **Ce qui tient** [VU SUR IMAGES] : la géométrie du rendu Blender (croix, fenêtre, table, chaises, dôme en haut à gauche, bord de la porte) ; le parpaing beige sali et écaillé ; la croix patinée ; le plateau intact ; la bougie ambrée ; une vraie photo, pas un rendu 3D.
- **Écarts notés, sans reprise faute d'accord de Diego** :
  - Le magenta est trop faible. Il ne fait que 6,6 % des pixels saturés, contre 84 % pour le brun et l'ambre. L'image se lit brun chaud, alors que la bible demande deux couleurs, magenta et ambre (`da.md`). [mesure : teintes HSV des pixels saturés]
  - Les noirs sont un peu levés : 19,5 % de l'image sous 0,06 de luminance. Les captures de référence en avaient 24 à 76 % sous le seuil du noir, et ce seuil n'avait pas été noté. [mesure ; comparaison approximative]
  - La brume dans la lumière de la fenêtre n'apparaît pas.
  - L'objectif du dôme dépasse sous le linge, alors que le linge doit le couvrir entièrement.
- **Correction proposée** : « The magenta neon through the window is the key light of the room: it washes the back wall and the ceiling from above, the beige paint reads dusty magenta where the light falls and drops into black elsewhere; no warm brown fill light; the candle is the only warm source. A visible soft haze in the air catches the window glow. The white cloth hangs over the whole camera dome, the lens is completely hidden. »
