---
name: montage-ia-generative
description: Génération vidéo ou image par IA, choisir un modèle (Veo, Sora, Runway, Kling, Seedance, Higgsfield, Luma, Midjourney, Nano Banana, Flux…), plans impossibles, extension de plan (Generative Extend), upscaling (Topaz), interpolation, détourage/roto IA (Magic Mask, Object Mask, SAM), voix et musique IA (ElevenLabs, Suno, Udio), workflow hybride tournage + IA, éviter les clichés et le « look IA ». Mots d'un réalisateur ou monteur : « on n'a pas le plan », « il me manque deux secondes », « on peut le générer ? », « ça fait trop IA », « plan impossible », « rallonger la fin du plan », « faire parler », « musique libre de droits par IA », « mention IA obligatoire ? ».
---

# IA générative en post-production : le regard d'abord

Version 1 (2026-10-09). Rédigé par un DA de post-prod, pas par un fan de technologie. **Rien ici n'a été testé** : tout ce qui touche aux outils vient de sources web 2025-2026 citées dans `etat-de-l-art-2026-10.md` et `/sources/ia-generative-2026-10.md`. Ce marché change tous les trois mois : **toute info outil de plus de 6 mois est à revérifier**.

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
- **La cohérence de personnage** : partir d'images de référence (personnage, décor) et garder les mêmes d'un plan à l'autre. Les outils 2026 en font un argument (Veo 3.1 « Ingredients », Kling 3.0 multi-plans, Aleph 2.0 multi-shot selon les sources). C'est à vérifier plan par plan.
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

## 5. État de l'art (au 2026-10-09)

Détail, nuances et sources dans **`etat-de-l-art-2026-10.md`** (même dossier). « Secondaire » = blog ou agrégateur, sans confirmation officielle.

| Outil | Usage fort | Limite | Date de l'info | Source |
|---|---|---|---|---|
| **Google Veo 3.1** (Flow, Gemini API, Vertex) | Généraliste, audio natif, « Ingredients to Video », extension de scène, 9:16 natif, upscale 1080p/4K | Outil « retirer un objet » annoncé, livraison non confirmée | janv. 2026 | 9to5google / yourstory (secondaire) |
| **OpenAI Sora 2** | — | **Arrêté** : appli et web le 26/04/2026, API annoncée pour le 24/09/2026 | 2026 | help.openai.com (officiel) |
| **Runway Gen-4.5** | Texte vers vidéo, physique améliorée | Runway liste lui-même des limites de causalité et de permanence des objets | annoncé 01/12/2025 ; revue juil. 2026 | CometAPI, Similar Labs (secondaire) |
| **Runway Aleph / Aleph 2.0** | Vidéo vers vidéo : ajouter/retirer un objet, ré-éclairer, nouvel angle, « plan suivant » | Aleph 2.0 (juin 2026) n'est connu que par un catalogue tiers | mars et juin 2026 | CometAPI, Runware (secondaire, **incertain**) |
| **Kling 3.0** (Kuaishou) | Multi-plans, contrôle « storyboard », audio multilingue, jusqu'à 15 s, 4K | Lent, coût difficile à prévoir | lancé 4-6/02/2026 | Bernama (communiqué) |
| **Seedance 2.0** (ByteDance) | Image vers vidéo, réalisme à partir de références | Comparatifs souvent écrits par le vendeur (Dreamina) | févr. 2026 | notegpt, Dreamina (biaisé) |
| **Hailuo 2.3** (MiniMax) | Volume rapide pour les réseaux sociaux | Pas de source 2026 sur une version suivante | 2026 | muapi.ai (secondaire) |
| **Wan 2.6** (Alibaba) | Disponible dans Higgsfield | Statut open source **non confirmé** pour 2.6 | 2026 | toolquestor (secondaire) |
| **Luma Ray3 Modify / Ray3.2** | Modifier une séquence réelle (costume, visage) en gardant le jeu et le timing ; Ray3.2 : 16 images clés, 20 s en 1080p | Ray3.2 n'est connu que par des sources secondaires | Ray3.2 : juin 2026 | jang.com.pk, veed (secondaire) |
| **Higgsfield** | Plateforme qui agrège plusieurs modèles (Kling, Seedance, Veo, Wan, Hailuo, Nano Banana) | Ce n'est pas un modèle en soi : la qualité dépend du modèle choisi | 2026 | toolquestor (secondaire) |
| **GPT Image 2** (OpenAI) | Image, tête de l'arène Artificial Analysis (1339 Elo) | Annoncé jusqu'à 2K | avril 2026 | tech-insider (secondaire) |
| **Nano Banana Pro** (Gemini 3 Pro Image) | Image jusqu'à 4K, texte dans l'image | Confusion entre « Nano Banana 2 » et « Pro » selon les sources | 2026 | tech-insider, laozhang (secondaire) |
| **Midjourney V8.1** | Esthétique, direction artistique | Pas d'API officielle, V7 encore par défaut | fin avril 2026 | tech-insider (secondaire) |
| **FLUX.2** (Black Forest Labs) | Poids téléchargeables, exécution locale (32 Md de paramètres) | Demande une machine solide | 2026 | tech-insider (secondaire) |
| **Topaz Astra 2 / Starlight** | Upscaling par diffusion, « dé-plastifier » les rushes IA | Versions contradictoires (2.5 ou 2.6) ; abonnement depuis oct. 2025 | Astra 2 : avril 2026 | invideo, fal.ai, unifab (secondaire) |
| **Premiere 26** (ex-Pro) | Object Mask en un clic (masque + suivi) ; Firefly Boards (Adobe, Google, OpenAI, Runway) | Object Mask peine sur une image bruitée ou peu contrastée | 20/01/2026 | PetaPixel, Digital Production |
| **Premiere Generative Extend** (Firefly Video) | +2 s de vidéo, +10 s d'audio, frames étiquetées | 12-30 i/s, 8 bits SDR seulement | janv. 2026 | community.adobe.com (officiel) |
| **DaVinci Resolve 21 / 21.1** | CineFocus (profondeur de champ synthétique), IntelliSearch local, Magic Mask (aussi sur la page Photo), Magic Mask 2.0 annoncé en 21.1 | La plupart des outils IA demandent Studio (payant) et un GPU d'au moins 4 Go | 02/06/2026 ; 21.1 le 09/09/2026 | Newsshooter, SVG |
| **Meta SAM 3** | Segmentation et suivi par texte ou boîte, image et vidéo, téléchargeable | Pas d'intégration Resolve/AE confirmée | 2025-2026 | ai.meta.com/sam3 (officiel) |
| **After Effects Roto Brush** | — | **Aucune source 2026 trouvée** | — | non vérifié |
| **Interpolation** (Topaz, Resolve Speed Warp…) | — | **Aucune source 2025-2026 trouvée** dans cette recherche | — | non vérifié |
| **ElevenLabs Eleven v3** | Voix expressive, balises d'émotion, dialogue à plusieurs voix, plus de 70 langues | Pas en temps réel ; clonage soumis à consentement vérifié | GA 02/02/2026 | coval.ai (secondaire) |
| **Suno** | Musique générée | Accord Warner (25/11/2025) : nouveaux modèles sous licence en 2026, pas d'usage commercial en gratuit ; impasse UMG/Sony (avril 2026, source unique) | 2025-2026 | Decrypt, MarketScreener, Opus (secondaire) |
| **Udio** | Remix de catalogues sous licence | Plateforme fermée : **pas d'export ni d'usage externe** | 2025-2026 | Decrypt |

### Vérification du 2026-10-10 (détail et sources : `sources/ia-verif-2026-10-10.md`)
- **Sora** : arrêt de l'API le 24/09/2026 inscrit dans les dépréciations *passées* d'OpenAI (page officielle), sans remplaçant ; désactivation effective très probable (presse), non vue directement.
- **AI Act art. 50** : confirmé applicable depuis le 02/08/2026, **non reporté** par l'Omnibus numérique (Règlement (UE) 2026/1744, JO du 24/07/2026) ; seul le marquage machine (50(2)) des systèmes déjà sur le marché a jusqu'au 02/12/2026 ; signalement des deepfakes (50(4)) sans délai. Code de pratique sur le marquage publié le 10/06/2026. Sources : cabinets d'avocats (secondaires), texte EUR-Lex non relu.
- **Modèles** : Veo reste en 3.1 ; Kling 3.0 (05/02/2026) ; Seedance 2.0 ; Runway Gen-4.5 sans successeur ; Luma Ray 3.2 (06/2026, à confirmer) ; MiniMax Hailuo 3.0 (31/07/2026, à confirmer). **Correction** : chez Wan, les poids ouverts s'arrêtent à 2.2 (Wan 3.0 = API fermée) ; open source vivant : **LTX-2 / 2.3** (Lightricks, 2026). Midjourney vidéo toujours V1.
- **Logiciels** : Premiere 26.2 confirmée ; panneau « Generative Media » en bêta (IBC 2026 : Firefly, Veo, Runway, Kling, Luma dans la timeline). Resolve 21.0 final le 02/06/2026 ; 21.1 (IntelliTrack, Magic Mask 2.0) annoncée en 09/2026 par une seule source.
- **Higgsfield** : agrégateur de modèles tiers + modèles maison (Soul, image) ; plugin Adobe AE + Premiere présenté le 21/07/2026 ; serveur MCP officiel (« bridge ») ; add-on Blender piloté par MCP. Les générations y sont **payantes (crédits)** : jamais sans accord explicite.

## 6. Workflows hybrides types [THÉORIQUE]

Aucun de ces workflows n'a été testé ici. Ce sont des schémas à valider sur un vrai projet.

**A. Le plan manquant (raccord)** [THÉORIQUE]
1. Exporter la dernière image du plan réel, étalonnée neutre.
2. Image vers vidéo (Veo « Frames to Video », Kling, Seedance) avec un prompt court sur le mouvement, et la consigne « caméra fixe » ou le mouvement exact du plan précédent.
3. Garder 1-3 s, couper avant la dérive.
4. Appliquer le même grain et la même LUT que le réel, puis un upscale seulement si nécessaire.
5. Ajouter un son réel (ambiance du tournage).

**B. Rallonger un plan de 2 s** [THÉORIQUE]
Premiere Generative Extend (2 s max, 8 bits SDR, 12-30 i/s). Pour du 10 bits, du HDR ou du 50p, chercher une autre voie (par exemple un vidéo vers vidéo Aleph, ou l'image vers vidéo du workflow A). Vérifier le raccord de lumière à l'image près.

**C. Le plan impossible porteur de sens** [THÉORIQUE]
1. Planche de références : 5 à 10 images (Midjourney, Nano Banana, FLUX.2) validées avec le réalisateur, dans le même univers de couleur que le tournage.
2. Génération de 3 à 5 variantes par plan avec les mêmes références (personnage, décor).
3. Montage serré, plans IA courts et entourés de réel.
4. Passe Topaz Starlight ou Astra pour la texture (à tester contre le grain seul : le grain suffit parfois).
5. Étalonnage commun et grain commun.

**D. Modifier une prise réelle** (costume, décor, époque) [THÉORIQUE]
Luma Ray3 Modify ou Runway Aleph : le jeu de l'acteur et le timing sont conservés, seul l'habillage change. Vérifier les yeux, les mains et les bords à chaque image. Le consentement de l'acteur est requis.

**E. Détourage** [THÉORIQUE]
D'abord l'outil intégré (Premiere Object Mask, Resolve Magic Mask), puis SAM 3 si le cas est difficile et qu'un pipeline local existe. Repasser à la main les cheveux et le flou de bougé : c'est là que les masques IA cèdent.

**F. Voix et musique** [THÉORIQUE]
Voix témoin IA pour caler le montage, puis **comédien réel** pour la livraison, sauf accord explicite. Musique : vérifier la licence commerciale du plan d'abonnement (Suno gratuit = pas d'usage commercial ; Udio = pas d'export). Une musique composée ou une banque sous licence reste plus sûre pour la diffusion.

## 7. Juridique et éthique (au 2026-10-09)

- **AI Act européen, article 50** (transparence) : applicable depuis le **2 août 2026**. Un deepfake (image, son ou vidéo qui ressemble à des personnes, lieux ou événements réels) doit être signalé comme généré ou manipulé par IA. Une exception allégée existe pour une œuvre manifestement artistique ou fictionnelle : la mention reste due, mais sans gêner l'œuvre (à vérifier dans le texte officiel). Le **marquage lisible par machine** (filigrane, métadonnées) imposé aux fournisseurs bénéficie d'un délai jusqu'au **2 décembre 2026** pour les systèmes déjà sur le marché (Digital Omnibus). Lignes directrices de la Commission publiées le 20 juillet 2026 (CSA, 29/07/2026, secondaire). **Ce n'est pas un avis juridique** : faire valider par un juriste pour toute diffusion.
- **Mention au client** : écrire dans le devis et le bon de livraison quels plans sont générés et par quel outil. Garder les prompts et les sources.
- **Consentement** : visage et voix d'une personne réelle = accord écrit et spécifique. ElevenLabs exige une vérification du titulaire de la voix pour le clonage professionnel (secondaire).
- **Droits sur la musique** : le terrain est en recomposition (accords Warner/Suno, UMG/Udio ; procès Suno contre UMG/Sony non réglé en avril 2026). Lire les CGU au moment de la livraison.
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
