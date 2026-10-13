---
name: montage-ia-generative
description: Générer un plan ou une image par IA et l'intégrer au montage — choisir un modèle (Veo, Kling, Seedance, Runway, Luma, Higgsfield, Midjourney, Nano Banana, FLUX), plan impossible, raccord manquant, upscale (Topaz), roto IA, voix et musique IA (ElevenLabs, Suno), workflow hybride tournage + IA, éviter le « look IA », mention AI Act. Mots d'un réalisateur ou d'un client : « on n'a pas le plan », « on peut le générer ? », « ça fait trop IA », « plan impossible », « faire parler », « musique libre de droits par IA », « mention IA obligatoire ? ».
---

# IA générative en post-production : le regard d'abord

Marqueurs : **[SOURCÉ]** lu dans une source datée · **[TESTÉ EN LABO]** fait technique mesuré (ffmpeg, scripts) · **[ÉPROUVÉ EN MAQUETTE]** principe tiré d'une maquette Blender/Pillow/ffmpeg, hypothèse à confirmer sur de vraies images en phase 2 · **[THÉORIQUE]** doc ou pratique, jamais exécuté.

**Fait foi sur** : le choix d'un outil génératif, son usage artistique, les clichés « look IA », le juridique (AI Act, droits, consentement). **Pour** les réglages de Generative Extend et de l'Object Mask dans Premiere, voir `montage-premiere` ; Magic Mask et l'API Resolve, `montage-resolve` ; l'interpolation (RIFE, fondu, `minterpolate`), `montage-workflows` ; piloter Higgsfield par MCP, `montage-pilotage-mcp`.

Faits outils à jour au **2026-10-10**, tirés de sources web (aucun modèle génératif n'a été testé ici). État détaillé et sources : [`etat-de-l-art-2026-10.md`](etat-de-l-art-2026-10.md) (prime sur le journal) ; journal historique des veilles, qui ne fait pas foi : [`veilles-2026-10.md`](veilles-2026-10.md). Ce marché change chaque mois : **toute info outil de plus de 3 mois est à revérifier avant un devis**.

## 1. Ce que l'IA permet vraiment, artistiquement [THÉORIQUE]

- **Le plan qu'on n'aurait jamais pu tourner** : l'échelle (cosmique, microscopique), le passé, l'intérieur d'un corps, un rêve. C'est sa seule vraie singularité (*Ancestra*, 2025).
- **Le raccord manquant** : deux secondes de plus, un plan de coupe, un fond étendu. Usage le plus sûr : l'IA comble un trou au lieu de porter le film.
- **L'idée visuelle qui EST le procédé** : *The Hardest Part* (Washed Out, 2024), *Total Pixel Space* (AIFF 2025). Quand le médium et le propos se rejoignent, le spectateur pardonne les défauts.
- **La prévisualisation** : moodboard animé ou previz, jamais livrés.

## 2. Les clichés reconnaissables (le « look IA »)

À traquer image par image, comme une faute d'étalonnage :
1. **Lissage plastique** (peau sans pores, surfaces « cire » ; Topaz vend un modèle pour le réduire, preuve que le défaut est connu).
2. **Caméra qui flotte** : travelling lent sans opérateur, sans accident.
3. **Mouvement sans poids** : pieds qui glissent, pas d'inertie (Runway reconnaît des limites de causalité sur Gen-4.5).
4. **Morphing** : doigt en plus, roues en trop (pub Coca-Cola 2025), visage qui glisse.
5. **Lumière dorée générique**, contre-jour flatteur, halo partout.
6. **Visages parfaits**, symétriques, sans âge ni vraie expression.
7. **Fausse profondeur de champ** : flou uniforme, mise au point qui ne respire pas.
8. **Plan « bande-annonce »** : chaque plan est un climax (ralenti, fumée, particules).
9. **Composition centrée et symétrique**, sujet plein cadre.
10. **Texte illisible**, ou propre mais sans patine.
11. **Son « stock »** : voix trop propre, sans air de pièce ; musique sans accident.
12. **Durée de plan identique** (celle de la génération) : rythme mécanique.

## 3. L'utiliser avec talent [THÉORIQUE]

- **Une contrainte d'abord** : une palette, une focale, un seul type de mouvement (ou caméra fixe). Moins on laisse de choix au modèle, moins ça fait IA.
- **Une intention par plan** avant le prompt. « Beau » n'est pas une intention.
- **L'IA pour UN plan précis**, pas pour tout : un film entièrement généré accumule les clichés.
- **Cohérence de personnage** : mêmes images de référence d'un plan à l'autre (Veo 3.1 « Ingredients », références multiples de Kling, Aleph 2.0 qui propage une retouche). À vérifier plan par plan.
- **Les plans de 30 s possibles** (Seedance 2.5) ne sont pas une raison de les garder longs : la dérive grandit avec la durée.
- **Un montage qui cache les faiblesses** : couper AVANT le morphing (les 2-3 premières secondes sont souvent les meilleures), plans courts, coupe sur le mouvement, plan IA entre deux plans réels forts.
- **Un traitement unificateur** : même grain, même LUT, même halation sur réel et IA ; remettre du défaut (bougé, instabilité).
- **Le son réel** (bruitage, ambiance, voix humaine) ancre un plan généré mieux qu'un upscale.
- **Assumer ou cacher, mais choisir** : langage du film (rêve, mémoire) ou raccord invisible. Le pire est le milieu.
- **Règle du studio (dictée le 2026-10-10)** : l'IA n'est **pas assumée** ; elle sert à **réduire les coûts ou aller plus vite** (plan manquant, extension, nettoyage), jamais à produire du « slop ». Par défaut : raccord invisible ; une IA visible seulement si le client la demande explicitement.

## 4. Quand NE PAS l'utiliser

- **Le client exige du réel** (produit montré tel quel, témoignage, documentaire) : un plan généré y est une tromperie.
- **Visage ou voix d'une personne réelle sans consentement écrit**, toute personne publique (mention obligatoire dans l'UE depuis le 2 août 2026, §7).
- **Droits flous** : jamais « à la manière de » un artiste vivant, une marque, un personnage protégé, ni de musique « dans le style de ».
- **Une émotion qui repose sur le jeu** : l'IA ne joue pas.
- **Une marque dont l'image est l'authenticité** : le contrecoup est réel (Coca-Cola 2024-2025, 32 % de conversations négatives selon CARMA, via TechRadar) [SOURCÉ].
- **Quand générer et trier coûte plus que tourner un insert** (Trillo : 55 clips gardés sur 700, 2024) [SOURCÉ].

## 5. État de l'art résumé (au 2026-10-10) [SOURCÉ, rien testé]

Dates, prix et sources : `etat-de-l-art-2026-10.md` (tableau « Quel outil pour quel besoin » en tête).

| Outil | Usage fort | Limite |
|---|---|---|
| **Veo 3.1** (Flow, Gemini API) | Généraliste, audio natif, références, extension, insertion/retrait d'objet, 4K | 8 s par clip ; 0,40 $/s en 1080p. **Pas de Veo 4** |
| **Gemini Omni 1.1 Flash** | Montage conversationnel (texte, image, vidéo, audio) | 3-10 s, 720p (sec.) |
| **Sora** | — | **Fermé** : appli 26/04/2026, API 24/09/2026, sans successeur |
| **Kling 3.0 / 4.0** | 4.0 : 30 s, 10 images clés, 4K HDR annoncés | **4.0 complet non sorti au 10/10** (Flash seule, accès anticipé) : ne pas le promettre |
| **Seedance 2.5** | 30 s en une passe, audio | Mises en demeure Disney/MPA sur la 2.0 |
| **Runway Gen-4.5 / Aleph 2.0** | Retoucher une image, propager sur le plan ; ProRes 4444 ; plugins Premiere, AE, Resolve | Pas de Gen-5 |
| **Hailuo H3** (MiniMax) | 15 s, 2K, son stéréo | Poids ouverts contradictoires |
| **Luma Ray3.2** | 20 s 1080p, **HDR natif, EXR 16 bits** | Audio non mentionné |
| **Wan 3.0** (Alibaba) | Vidéo + audio jusqu'en 1080p | **Fermé** ; poids ouverts seulement jusqu'à **Wan 2.2** |
| **LTX-2.5** | Poids ouverts, 4K, audio, multi-plans, local | Licence communautaire (< 10 M$), pas OSI |
| **Vidu Q4 Preview** (07/10) | Références vers vidéo, 4K, 3-16 s | Pas de texte seul ; son mélangé à l'image |
| **Higgsfield** | Agrégateur, API, plugins AE/Premiere/Blender, MCP | Pas un modèle ; crédits payants |
| **Premiere : Generative Media Tool, Paper Edit, Generative Extend** | Vidéo et SFX dans la timeline ; +2 s vidéo / +10 s audio | Annoncés pour **26.5 [NON CONFIRMÉ — À TRANCHER EN PHASE 3]** ; détail : `montage-premiere` |
| **Midjourney V8.2** | Esthétique, DA (défaut depuis le 24/07/2026) | Pas d'API ; vidéo = image vers vidéo |
| **Nano Banana 2.1** (06/10) | Image 4K, texte, 14 références, formats 8:1 à 1:8 | NB2 déprécié |
| **FLUX 3 Image** (01/10) | Composition par boîtes de placement, retouches locales | Poids ouverts promis, pas sortis |
| **GPT Image 2.5** | Édition précise | Texte dense fragile (sec.) |
| **Topaz Starlight / Astra / Hyperion** | « Dé-plastifier » en 4K, SDR vers HDR ; Topaz racheté par Adobe (23/09) | Invente du détail |
| **AE Object Matte** | Roto IA ; Roto Brush devient Quick Selection | Rendu lent, propagation fragile |
| **Resolve 21 / 21.1** | 21 : CineFocus, IntelliSearch, Magic Mask ; **21.1 : pilotage par assistants externes (MCP, Studio)** | Pas de « Magic Mask 2.0 » ni d'« IntelliTrack » en 21.1 (source unique, absent du communiqué) |
| **SAM 3.1** (Meta) | Segmentation par texte ou boîte, local | Pas de plugin AE/Nuke confirmé |
| **ElevenLabs v4 / Music v2.5** | Voix 90+ langues ; régénérer un passage de musique | Clonage soumis à consentement vérifié |
| **Suno v6 / Speech / Studio** | Musique jusqu'à 8 min | Payant pour l'usage commercial ; Speech mélange voix et musique sur une piste ; UMG et Sony attaquent |
| **Udio** | — | Téléchargements coupés depuis 10/2025 |
| **Stable Audio 3.0** | Poids ouverts (Small, Medium) : musique en local | Licence à relire |

## 6. Workflows hybrides types [THÉORIQUE, à valider sur un vrai projet]

**A. Le plan manquant (raccord)** : exporter la dernière image du plan réel, étalonnée neutre → image vers vidéo (Veo « Frames to Video », Kling, Seedance), prompt court sur le mouvement, « caméra fixe » ou le mouvement du plan précédent → garder 1-3 s, couper avant la dérive → même grain, même LUT que le réel, upscale seulement si nécessaire → son réel (ambiance du tournage).

**B. Rallonger un plan de 2 s** : Generative Extend de Premiere (réglages et limites : `montage-premiere`). Les frames générées sortiraient en 8 bits SDR, 30 i/s au plus [À TRANCHER EN PHASE 3] : pour un master 10 bits, HDR ou 50p, comparer avec une autre voie (vidéo vers vidéo Aleph, ou le workflow A). Vérifier le raccord de lumière à l'image près.

**C. Le plan impossible porteur de sens** : planche de 5 à 10 références (Midjourney V8.2, Nano Banana 2.1, FLUX 3) validée avec le réalisateur dans l'univers couleur du tournage → 3 à 5 variantes par plan avec les mêmes références → montage serré, plans IA courts entourés de réel → Topaz Starlight ou Astra pour la texture (à comparer au grain seul, qui suffit parfois) → étalonnage et grain communs.

**D. Modifier une prise réelle** (costume, décor, époque) : Luma Ray3.2 Modify ou Runway Aleph 2.0 ; le jeu et le timing sont conservés. Vérifier yeux, mains, bords à chaque image. Consentement de l'acteur requis.

**E. Détourage** : d'abord l'outil intégré (Premiere Object Mask Sharp/Smooth, AE Object Matte, Resolve Magic Mask), puis SAM 3.1 si un pipeline local existe. Repasser à la main cheveux et flou de bougé.

**F. Voix et musique** : voix témoin IA pour caler le montage, **comédien réel** pour la livraison sauf accord explicite. Musique : licence commerciale du plan d'abonnement ; voix et musique toujours sur **pistes séparées** pour un master. Une musique composée ou une banque sous licence reste plus sûre pour la diffusion.

**Interpolation** : jamais un gain par défaut. Sur de vrais plans d'eau et de feuillage, RIFE 4.25 reste 1 à 3,6 dB **sous un simple fondu** [TESTÉ EN LABO] (`labo/interpolation-reel/`). Choix et réglages : `montage-workflows`.

## 7. Juridique et éthique (au 2026-10-10) [SOURCÉ, pas un avis juridique]

- **AI Act, article 50**, applicable depuis le **2 août 2026** : un deepfake (ressemblance avec des personnes, lieux ou événements réels) se signale comme généré ou manipulé, **même sans intention de tromper** ; œuvre manifestement artistique : mention due mais sans gêner l'œuvre ; **pas de rétroactivité** (compte la date de génération). Marquage machine des systèmes déjà sur le marché : délai au **2 décembre 2026**. Lignes directrices C(2026) 5054 du 20/07/2026. YouTube étiquette d'office le photoréaliste IA non déclaré depuis le 27/05/2026. Faire valider par un juriste toute diffusion.
- **Mention au client** : devis et bon de livraison disent quels plans sont générés, par quel outil. Garder prompts et sources.
- **Consentement** : visage et voix d'une personne réelle = accord écrit et spécifique.
- **Musique** : terrain en recomposition (accords Warner/Suno, UMG et Warner/Udio ; procès UMG et Sony contre Suno, Sony contre Udio). Pas de Suno en pub ou TV sans clause écrite. Relire les CGU à la livraison.
- **Entraînement « sûr »** : Adobe présente Firefly Video comme entraîné sous licence ; à vérifier dans les CGU en vigueur.
- **Pérennité** : Sora a fermé avec suppression des données ; Seedance 1.5 Pro quitte ElevenLabs le 11/11/2026. Archiver localement chaque rush généré, ses prompts, le modèle et sa version.
- **Éthique de métier** : ne pas présenter un plan généré comme tourné ; ne pas remplacer un comédien ou un musicien sans le dire au client. Générations payantes : jamais sans accord explicite.

## 8. Checklist avant livraison d'un plan IA

- [ ] Intention écrite pour ce plan ?
- [ ] Clichés du §2 présents (mains, yeux, bords, texte) ?
- [ ] Coupé avant la dérive ?
- [ ] Grain et LUT communs avec le réel ?
- [ ] Son réel ?
- [ ] Droits, consentement et mention (AI Act) en règle ?
- [ ] Prompts, modèle, version et date archivés ?

Voir aussi : `montage-regard` (grille de jugement), `/culture/ia-oeuvres-remarquables.md`.
