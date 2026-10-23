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
> Wardrobe: his own clothes, dressed as for an occasion. A clean white cotton shirt, buttoned all the way up to the collar, no tie, sleeves down, slightly tight on his shoulders. Plain dark charcoal trousers, black leather shoes, worn but polished.
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
