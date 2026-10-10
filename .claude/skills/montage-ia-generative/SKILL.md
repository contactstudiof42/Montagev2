---
name: montage-ia-generative
description: Génération vidéo ou image par IA, choisir un modèle (Veo, Sora, Runway, Kling, Seedance, Higgsfield, Luma, Midjourney, Nano Banana, Flux…), plans impossibles, extension de plan (Generative Extend), upscaling (Topaz), interpolation, détourage/roto IA (Magic Mask, Object Mask, SAM), voix et musique IA (ElevenLabs, Suno, Udio), workflow hybride tournage + IA, éviter les clichés et le « look IA ». Mots d'un réalisateur ou monteur : « on n'a pas le plan », « il me manque deux secondes », « on peut le générer ? », « ça fait trop IA », « plan impossible », « rallonger la fin du plan », « faire parler », « musique libre de droits par IA », « mention IA obligatoire ? ».
---

# IA générative en post-production : le regard d'abord

Version 1 (2026-10-09), faits outils mis à jour le **2026-10-10**. Rédigé par un DA de post-prod, pas par un fan de technologie. **Rien ici n'a été testé** : tout ce qui touche aux outils vient de sources web 2025-2026 citées dans `etat-de-l-art-2026-10.md` et `/sources/ia-generative-2026-10-10.md`. Ce marché change chaque mois : **toute info outil de plus de 3 mois est à revérifier**.

## 1. Ce que l'IA permet vraiment, artistiquement

- **Le plan qu'on n'aurait jamais pu tourner** : l'échelle (cosmique, microscopique), le passé, l'intérieur d'un corps, un rêve. C'est sa seule vraie singularité. *Ancestra* (2025) mélange du tournage réel et des images générées de l'intérieur du corps et du cosmos.
- **Le raccord manquant** : deux secondes de plus en fin de plan, un plan de coupe, un fond étendu. C'est l'usage le plus sûr, car l'IA y comble un trou au lieu de porter le film.
- **L'idée visuelle qui EST le procédé** : *The Hardest Part* (Washed Out, 2024) fait de la dérive de l'IA un sujet, avec un zoom infini à travers une vie. *Total Pixel Space* (Grand Prix AIFF 2025) parle justement de l'espace de toutes les images possibles. Quand le médium et le propos se rejoignent, le spectateur pardonne les défauts.
- **La prévisualisation** : un moodboard animé ou une previz avant tournage, sans jamais être livrés.

## 2. Les clichés reconnaissables (le « look IA »)

À traquer image par image, comme on traque une faute d'étalonnage :

1. **Lissage plastique** : peau sans pores, tissus sans fibre, surfaces « cire ». Topaz vend même un modèle (Starlight) pour « réduire le look plastique », ce qui prouve que le défaut est bien connu.
2. **Caméra qui flotte** : travelling avant lent, sans opérateur, sans intention ni accident. Personne ne la tient.
3. **Mouvement sans poids** : les pieds glissent, les objets n'ont pas d'inertie, la physique est approximative. Runway reconnaît lui-même des limites de causalité et de permanence des objets (Gen-4.5).
4. **Morphing** : une main gagne un doigt, une voiture a des roues en trop (relevé sur la pub Coca-Cola 2025), un visage glisse vers un autre au fil du plan.
5. **Lumière dorée générique** : *golden hour* perpétuelle, contre-jour flatteur, halo sur tout.
6. **Visages parfaits** : symétriques, sans âge, sans expression vraie. La critique principale de la pub Coca-Cola, c'est justement des visages sans l'expression des acteurs de 1995.
7. **Fausse profondeur de champ** : un flou uniforme, sans optique réelle derrière, avec une mise au point qui ne « respire » pas.
8. **Plan « bande-annonce »** : tout est épique, chaque plan est un climax, ralenti, fumée, particules, sans plan neutre pour respirer.
9. **Composition centrée et symétrique** par défaut, sujet plein cadre.
10. **Texte et signalétique illisibles**, ou propres mais sans aucune patine.
11. **Son « stock »** : ambiance générique, voix trop propre, sans air de pièce ni respiration, musique sans accident.
12. **Durée de plan identique** (4-10 s, la durée de génération), qui donne un rythme mécanique au montage.

## 3. L'utiliser avec talent

- **Une contrainte d'abord** : une palette, une focale, un seul type de mouvement caméra (ou caméra fixe), un format. Moins on laisse de choix au modèle, moins ça fait IA.
- **Une intention par plan** : savoir ce que le plan doit faire ressentir avant de rédiger le prompt. « Beau » n'est pas une intention.
- **L'IA pour UN plan précis, pas pour tout** : le plan impossible, le raccord manquant. Le reste est tourné. Un film entièrement généré accumule les clichés.
- **La cohérence de personnage** : partir d'images de référence (personnage, décor) et garder les mêmes d'un plan à l'autre. Les outils 2026 en font un argument (Veo 3.1 « Ingredients », Kling 4.0 et ses références multiples, LTX-2.5 multi-plans en une passe, Aleph 2.0 qui propage une retouche). C'est à vérifier plan par plan.
- **Plans de 30 s possibles** (Seedance 2.5, Kling 4.0) : ce n'est pas une raison de les garder longs. La dérive grandit avec la durée.
- **Un montage qui cache les faiblesses** : couper AVANT que le morphing commence (les 2-3 premières secondes sont souvent les meilleures), garder des plans courts, couper sur le mouvement, placer le plan IA entre deux plans réels forts, éviter de le faire durer.
- **Un traitement unificateur** : même grain argentique sur tout, même LUT, même halation, même légère aberration. Remettre du défaut (flou de bougé, instabilité caméra réelle ajoutée en post) pour casser la perfection.
- **Le son réel** : du bruitage, une vraie ambiance et une voix humaine ancrent un plan généré mieux que n'importe quel upscale.
- **Assumer ou cacher, mais choisir** : soit l'IA devient le langage du film (rêve, mémoire, dérive), soit elle reste invisible (raccord). Le pire, c'est le milieu, quand on veut faire du réel et que ça se voit.

## 4. Quand NE PAS l'utiliser

- **Le client exige du réel**, avec un produit à montrer tel quel, un témoignage ou un documentaire : un plan généré y est une tromperie.
- **Les visages ou voix de personnes réelles sans consentement écrit** (deepfake), et toute personne publique. C'est illégal ou risqué, et une mention obligatoire s'applique dans l'UE depuis le 2 août 2026 (voir §7).
- **Des droits flous** : ne pas générer « à la manière de » un artiste vivant, une marque ou un personnage protégé, ni de musique « dans le style de ». Vérifier les CGU commerciales de l'outil.
- **Une émotion qui repose sur le jeu d'acteur** : l'IA ne joue pas. Garder la prise réelle.
- **Une marque dont l'image repose sur l'authenticité ou le « fait main »** : le contrecoup est réel (Coca-Cola 2024 puis 2025, 32 % de conversations négatives selon CARMA, via TechRadar).
- **Quand le temps de génération et de tri dépasse le tournage d'un insert.** Trillo a gardé 55 clips sur 700 générés (2024).

## 5. État de l'art (au 2026-10-10)

Détail, sources datées et liste de ce qui était faux dans la version précédente : **`etat-de-l-art-2026-10.md`** (même dossier), en tête le tableau « Quel outil pour quel besoin ». « Sec. » = presse ou revendeur ; « off. » = éditeur.

| Outil | Usage fort | Limite | Date | Source |
|---|---|---|---|---|
| **Veo 3.1** (Flow, Gemini API) | Généraliste, audio natif, références, extension, insertion/retrait d'objet, 4K | 8 s par clip ; 0,40 $/s en 1080p. **Pas de Veo 4** | page consultée 10/2026 | deepmind.google, ai.google.dev (off.) |
| **Gemini Omni Flash** | Montage conversationnel, entrées texte/image/vidéo/audio | 3-10 s, 720p (sec.) | I/O 19/05/2026 | ai.google.dev (off.), invideo (sec.) |
| **Sora** | — | **Fermé** : appli 26/04/2026, API 24/09/2026, sans successeur | 2026 | help.openai.com (off.) |
| **Kling 4.0** | 30 s, 10 images clés, nombreuses références ; 4K HDR 10 bits annoncés | 4.0 Flash en accès anticipé, version complète « en octobre », prix non publié | 28/09/2026 | briefs.co, Bloomberg, X Kling |
| **Seedance 2.5** | 30 s en une passe, audio | Mises en demeure Disney/MPA sur la 2.0 (droits) | dispo 11/08/2026 | runway.com/changelog (off.) |
| **Runway Gen-4.5 / Aleph 2.0** | Aleph 2.0 : retoucher une image, propager sur le plan ; export ProRes 4444 ; plugins Premiere, AE, Resolve | Pas de Gen-5. Gen-4.5 : limites de causalité reconnues | Aleph 2.0 : 21/05/2026 | runway.com/changelog (off.) |
| **Hailuo 3.0 / H3** (MiniMax) | 15 s, 2K, son stéréo, multi-entrées | Poids ouverts contradictoires | 31/07/2026 | runway.com/changelog (off.), sec. |
| **Luma Ray3.2** | 20 s 1080p, 16 images clés, **HDR natif, EXR 16 bits**, suivi du jeu | Audio non mentionné | 09/06/2026 | lumalabs.ai (off.) |
| **Wan 3.0** (Alibaba) | Vidéo + audio jusqu'en 1080p | **Fermé** ; poids ouverts seulement jusqu'à Wan 2.2 | 24/08/2026 | runway.com/changelog (off.) |
| **LTX-2.5** (Lightricks) | Poids ouverts, 4K, audio, multi-plans en une passe, local | Licence communautaire (< 10 M$ de CA), pas OSI | 11/08/2026 | venturebeat, ltx.io |
| **Higgsfield** | Agrégateur (Seedance 2.5, Wan 3.0, H3, Nano Banana 2.1…), API (16/09), plugins AE/Premiere/Blender, MCP | Pas un modèle ; crédits payants | changelog 10/2026 | higgsfield.ai (off.) |
| **Firefly / Premiere 26.5** | Generative Media Tool (vidéo et SFX dans la timeline), Object Mask Sharp/Smooth, Paper Edit | Pas de nouveau modèle Firefly Video trouvé ; MAX le 10-12/11/2026 | 10/09/2026 | community.adobe.com (off.) |
| **Generative Extend** | +2 s vidéo, +10 s audio ; sources 360p-4K, 12-60 i/s, 8-16 bits, SDR/HDR | Frames générées en 8 bits SDR, 30 i/s max (à vérifier) | 26.5, 09/2026 | Adobe (off.), atlascloud (sec.) |
| **Midjourney V8.2** | Esthétique, direction artistique | Pas d'API ; vidéo = image vers vidéo seulement | défaut 24/07/2026 | sec. citant docs.midjourney |
| **Nano Banana 2 / 2.1 / Pro** | Image jusqu'en 4K, texte, 14 références ; 2.1 ≈ 0,11 $ l'image 4K | — | 2.1 : 10/2026 | ai.google.dev (off.) |
| **GPT Image 2.5** | Édition précise (Sunburst), rapide (Flare) | Texte dense encore fragile (sec.) | 08/09/2026 | axios (sec.) |
| **FLUX 3** (BFL) | Image + vidéo 20 s avec son | Poids ouverts promis, pas sortis | 23/07/2026 | marktechpost (sec.) |
| **Topaz Starlight Precise 2.5 / Astra 2 / Hyperion 2** | « Dé-plastifier » les rushes IA en 4K ; SDR vers HDR ; panneau Premiere | Invente du détail ; abonnement | 03 à 05/2026 | topazlabs.com (off.) |
| **AE Object Matte** | Roto IA en un clic ; Roto Brush devient Quick Selection | Rendu lent, propagation fragile (bêta) | 02-04/2026 | community.adobe.com (off.) |
| **Resolve 21 / 21.1** | 21 : CineFocus, IntelliSearch, Magic Mask ; 21.1 : pilotage par Claude / ChatGPT (MCP, Studio) | IntelliTrack / Magic Mask 2.0 en 21.1 **non confirmés** | 02/06 et 08/09/2026 | blackmagicdesign.com (off.) |
| **SAM 3.1** (Meta) | Segmentation par texte ou boîte, vidéo, local | Pas de plugin AE/Nuke confirmé | 27/03/2026 | learnopencv (sec.) |
| **Interpolation** | RIFE 4.25 (libre), Topaz Apollo/Chronos/Aion, Runway Enhance Frame Rate (25-120 i/s) | **[TESTÉ EN LABO]** RIFE sous un simple fondu sur eau et feuillage (`labo/interpolation-reel/`) | 2026 | Topaz (off.), runway (off.) |
| **ElevenLabs v4 / v4 Turbo** | Voix expressive, 90+ langues, temps réel (≈ 100 ms) | Clonage soumis à consentement vérifié | 28/09/2026 | elevenlabs.io (off.) |
| **Suno v6** | Musique jusqu'à 8 min, modèles faits avec Warner, BMG, Believe | v6 payant ; UMG et Sony attaquent encore (2e plainte 18/09/2026) | 09/09/2026 | routenote, MBW (sec.) |
| **Udio** | — | **Téléchargements coupés** depuis 10/2025, toujours fin 09/2026 ; Sony attaque | 2026 | sec. |

## 6. Workflows hybrides types [THÉORIQUE]

Aucun de ces workflows n'a été testé ici. Ce sont des schémas à valider sur un vrai projet.

**A. Le plan manquant (raccord)** [THÉORIQUE]
1. Exporter la dernière image du plan réel, étalonnée neutre.
2. Image vers vidéo (Veo « Frames to Video », Kling, Seedance) avec un prompt court sur le mouvement, et la consigne « caméra fixe » ou le mouvement exact du plan précédent.
3. Garder 1-3 s, couper avant la dérive.
4. Appliquer le même grain et la même LUT que le réel, puis un upscale seulement si nécessaire.
5. Ajouter un son réel (ambiance du tournage).

**B. Rallonger un plan de 2 s** [THÉORIQUE]
Premiere Generative Extend (2 s max). Depuis 26.5, il accepte des sources 360p-4K, 12-60 i/s, 8-16 bits, SDR ou HDR ; mais les frames générées sortiraient en 8 bits SDR, à 30 i/s au plus (à vérifier). Pour un master 10 bits, HDR ou 50p, comparer avec une autre voie (par exemple un vidéo vers vidéo Aleph, ou l'image vers vidéo du workflow A). Vérifier le raccord de lumière à l'image près.

**C. Le plan impossible porteur de sens** [THÉORIQUE]
1. Planche de références : 5 à 10 images (Midjourney V8.2, Nano Banana 2.1, FLUX.2 ou FLUX 3) validées avec le réalisateur, dans le même univers de couleur que le tournage.
2. Génération de 3 à 5 variantes par plan avec les mêmes références (personnage, décor).
3. Montage serré, plans IA courts et entourés de réel.
4. Passe Topaz Starlight ou Astra pour la texture (à tester contre le grain seul : le grain suffit parfois).
5. Étalonnage commun et grain commun.

**D. Modifier une prise réelle** (costume, décor, époque) [THÉORIQUE]
Luma Ray3 Modify / Ray3.2 ou Runway Aleph 2.0 (on retouche une image, il propage) : le jeu de l'acteur et le timing sont conservés, seul l'habillage change. Vérifier les yeux, les mains et les bords à chaque image. Le consentement de l'acteur est requis.

**E. Détourage** [THÉORIQUE]
D'abord l'outil intégré (Premiere Object Mask en mode Sharp ou Smooth, AE Object Matte, Resolve Magic Mask), puis SAM 3.1 si le cas est difficile et qu'un pipeline local existe. Repasser à la main les cheveux et le flou de bougé : c'est là que les masques IA cèdent.

**F. Voix et musique** [THÉORIQUE]
Voix témoin IA pour caler le montage, puis **comédien réel** pour la livraison, sauf accord explicite. Musique : vérifier la licence commerciale du plan d'abonnement (Suno v6 : réservé aux abonnés payants, gratuit = pas d'usage commercial ; Udio = pas de téléchargement). Une musique composée ou une banque sous licence reste plus sûre pour la diffusion. Pour une voix témoin rapide en français : ElevenLabs v4 (28/09/2026).

## 7. Juridique et éthique (au 2026-10-10)

- **AI Act européen, article 50** (transparence) : applicable depuis le **2 août 2026**. Un deepfake (image, son ou vidéo qui ressemble à des personnes, lieux ou événements réels) doit être signalé comme généré ou manipulé par IA. Une exception allégée existe pour une œuvre manifestement artistique ou fictionnelle : la mention reste due, mais sans gêner l'œuvre (à vérifier dans le texte officiel). Le **marquage lisible par machine** (filigrane, métadonnées) imposé aux fournisseurs bénéficie d'un délai jusqu'au **2 décembre 2026** pour les systèmes déjà sur le marché (Digital Omnibus). Lignes directrices finales de la Commission C(2026) 5054, adoptées le 20/07/2026 : une ressemblance avec une personne réelle se signale **même sans intention de tromper** ; **pas de rétroactivité** (compte la date de génération). Plateformes : YouTube étiquette d'office le photoréaliste IA non déclaré depuis le 27/05/2026 (blog YouTube). **Ce n'est pas un avis juridique** : faire valider par un juriste pour toute diffusion.
- **Mention au client** : écrire dans le devis et le bon de livraison quels plans sont générés et par quel outil. Garder les prompts et les sources.
- **Consentement** : visage et voix d'une personne réelle = accord écrit et spécifique. ElevenLabs exige une vérification du titulaire de la voix pour le clonage professionnel (secondaire).
- **Droits sur la musique** : le terrain est en recomposition (accords Warner/Suno, UMG et Warner/Udio ; UMG et Sony ont relancé une plainte contre Suno le 18/09/2026 ; Sony poursuit Udio). Lire les CGU au moment de la livraison.
- **Entraînement « sûr »** : Adobe présente Firefly Video comme entraîné sur du contenu sous licence et du domaine public. C'est un argument pour un client prudent, à vérifier dans les CGU en vigueur.
- **Pérennité** : Sora a fermé avec suppression des données. Archiver localement tout rush généré, ses prompts et la version du modèle.
- **Éthique de métier** : ne pas présenter un plan généré comme tourné, ne pas l'utiliser pour éviter de payer un comédien ou un musicien sans le dire au client.

## 8. Checklist avant livraison d'un plan IA

- [ ] Le plan a-t-il une intention écrite ?
- [ ] Quels clichés du §2 y sont présents (vérifier aux mains, aux yeux, aux bords et au texte) ?
- [ ] Coupé avant la dérive ?
- [ ] Grain et LUT communs avec le réel ?
- [ ] Son réel ?
- [ ] Droits, consentement et mention (AI Act) en règle ?
- [ ] Prompts, modèle et date archivés ?

Voir aussi : `montage-regard` (grille de jugement), `/culture/ia-oeuvres-remarquables.md`.
- (2026-10-10, session 10) RIFE 4.25 sur vrais plans d'eau et de feuillage à petit mouvement : **1 à 3,6 dB sous un simple fondu** (`labo/interpolation-reel/`). L'interpolation par IA n'est pas un gain par défaut : la tester sur le plan réel.

