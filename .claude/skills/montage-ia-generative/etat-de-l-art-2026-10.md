# État de l'art IA générative pour la post-production (annexe datée)

**À jour au 2026-10-10.** Recherche web du 2026-10-10 (WebSearch + WebFetch). **Rien n'a été testé ici**, sauf mention [LABO]. Ce marché bouge chaque mois : toute ligne de plus de 3 mois est à revérifier avant un devis.

Légende de chaque ligne :
- **[SOURCÉ]** : URL + date de publication de la source. « off. » = page de l'éditeur ; « sec. » = presse, blog, revendeur.
- **[À VÉRIFIER]** : source unique, contradiction ou vendeur juge et partie.
- **Inconnu** : aucune source trouvée. Aucun numéro de version n'est deviné.

Liens consultés : `/home/user/Montagev2/sources/ia-generative-2026-10-10.md`. Version précédente des sources : `sources/ia-generative-2026-10.md` et `sources/ia-verif-2026-10-10.md`.

---

## 0. Quel outil pour quel besoin (regard de DA)

| Besoin | Premier choix (oct. 2026) | Alternative | Quand NE PAS l'utiliser |
|---|---|---|---|
| **Plan impossible** (échelle, rêve, intérieur du corps) | Veo 3.1 (Flow) ou Kling 3.0 / 4.0 pour le réalisme ; Seedance 2.5 si plan long (30 s) | Luma Ray3.2 si l'étalonneur veut du HDR / EXR 16 bits | Quand le plan doit porter le jeu d'un acteur. Quand un insert tourné coûte moins que le tri (Trillo : 55 clips gardés sur 700). Quand le film promet du réel (doc, témoignage, produit). |
| **Raccord manquant** (plan de coupe, contrechamp absent) | Image vers vidéo depuis la dernière image réelle (Veo « Frames to Video », Kling, Seedance) | Runway Aleph 2.0 (vidéo vers vidéo, nouvel angle) | Si le raccord porte un regard ou une émotion : l'IA ne joue pas. Si le plan voisin est en 10 bits log et qu'on ne peut pas réunir les textures. |
| **Extension de plan** (+2 s) | Premiere Generative Extend (2 s vidéo, 10 s audio) | Veo « Scene extension » ; image vers vidéo + fondu | Sur un plan HDR ou 10 bits livré tel quel : les frames générées restent en 8 bits SDR selon la FAQ Adobe [À VÉRIFIER]. Sur un visage en gros plan qui parle. |
| **Upscale** | Topaz Starlight Precise 2.5 (rushes IA) ; Astra 2 (cloud) | Runway / Higgsfield upscale 4K | Sur une archive, un document ou un visage réel : la diffusion **invente** du détail. C'est une altération, à signaler. Souvent le grain seul suffit. |
| **Roto / détourage** | Outil intégré : Premiere Object Mask (Sharp/Smooth), AE Object Matte, Resolve Magic Mask | SAM 3.1 (Meta, local ou API) ; Runway SAM3 (export WebM transparent) | Cheveux en contre-jour, flou de bougé, fumée : repasser à la main. Ne jamais livrer un masque IA non vérifié image par image sur un plan héros. |
| **Interpolation / ralenti** | Tester d'abord le plan réel (labo : RIFE parfois **sous** un simple fondu) | Topaz Apollo / Chronos / Aion ; Resolve Speed Warp (Studio) ; Runway Enhance Frame Rate | Sur l'eau, le feuillage, une coupe dans le plan : artefacts. Un ralenti qui n'a pas été tourné se voit. Préférer un vrai haute cadence. |
| **Voix** | Voix témoin IA (ElevenLabs v4) pour caler le montage | Eleven v3 pour les balises d'émotion | En livraison sans comédien payé et sans accord écrit. Jamais la voix d'une personne réelle sans consentement. Le souffle et l'air de la pièce manquent toujours. |
| **Musique** | Musique composée ou banque sous licence | Suno v6 (payant, CGU à relire) ; Eleven Music (présenté « sous licence ») | Udio : pas de téléchargement. Suno gratuit : pas d'usage commercial (accord Warner). Jamais « dans le style de » un artiste. Pas de pub télé sans clause écrite. |

---

## 1. Vidéo générative

### Vue d'ensemble (oct. 2026)
- Trois tendances : **plans plus longs** (30 s chez Seedance 2.5 et Kling 4.0), **audio natif** partout, **agrégateurs** (Runway, Higgsfield, Adobe Firefly) qui revendent les modèles des autres.
- Les modèles chinois (Kling, Seedance, Hailuo, Wan) mènent sur la durée et le prix.
- OpenAI n'a plus de modèle vidéo public.

### Google Veo et Gemini Omni
| Fait | Statut |
|---|---|
| Veo 3.1 reste la dernière version. Déclinaisons Fast et Lite. **Pas de Veo 4 officiel** au 2026-10-10. | [SOURCÉ] off. deepmind.google/models/veo (consulté 2026-10-10) ; sec. evolink.ai (avril 2026), aireiter.com (août 2026). Un article MSN annonce un « Veo 4 » : [À VÉRIFIER], contredit par tout le reste. |
| Veo 3.1 : 1080p et 4K, audio natif, « Ingredients to video » (références de personnage, d'objet, de style), extension de scène, première et dernière image, **insertion et retrait d'objet**, contrôle caméra. | [SOURCÉ] off. deepmind.google/models/veo (consulté 2026-10-10). Date de livraison du retrait d'objet : inconnue. |
| Clip de base : 8 s, extensible. 9:16 natif depuis janvier 2026. | [SOURCÉ] off. deepmind.google ; sec. 9to5google (janv. 2026). |
| Prix API Gemini (avec audio) : Veo 3.1 = 0,40 $/s en 1080p, 0,60 $/s en 4K ; Fast = 0,12 $/s en 1080p ; Lite = 0,08 $/s en 1080p (pas de 4K). | [SOURCÉ] off. ai.google.dev/gemini-api/docs/pricing (consulté 2026-10-10). |
| **Gemini Omni Flash** : annoncé à l'I/O le 19/05/2026. Texte, image, vidéo et audio en entrée. Montage conversationnel. Clips de 3 à 10 s en 720p, audio natif. API en preview le 30/06/2026. Environ 0,10 $/s. | [SOURCÉ] off. ai.google.dev/gemini-api/docs/pricing (prix) ; sec. invideo.io, buildfastwithai (2026). Durée et résolution : [À VÉRIFIER] (sources secondaires). |
| Gemini Omni **1.1 Flash** (`gemini-omni-1.1-flash`) : version **GA** du 27/08/2026 ; l'ancien point d'accès `gemini-omni-flash-preview` est déprécié depuis le 30/09/2026. *(Corrigé le 2026-10-10, session 19 : n'est plus [À VÉRIFIER].)* | [SOURCÉ] off. ai.google.dev/gemini-api/docs/changelog (27/08/2026) ; off. changelog Higgsfield (28/08/2026). |

### OpenAI Sora : fermé
| Fait | Statut |
|---|---|
| Appli et sora.com fermés le 26/04/2026. API (sora-2, sora-2-pro) arrêtée le 24/09/2026, sans remplaçant. | [SOURCÉ] off. help.openai.com/en/articles/20001152 (24/03/2026) ; off. developers.openai.com/api/docs/deprecations (consulté 2026-10-10). |
| Aucun successeur annoncé (« Sora 3 », « Spud » = rumeurs). | [SOURCÉ] sec. opus.pro, spheron.network (2026). |
| Un guide (wavespeed) date Sora 2 du 30/09/2026 : **faux**, Sora 2 date de septembre 2025. | Signalé pour éviter la confusion. |

### Runway
| Fait | Statut |
|---|---|
| **Gen-4.5** (déc. 2025) reste le modèle de génération maison. **Pas de « Gen-5 »** trouvé. | [SOURCÉ] sec. en.wikipedia.org/wiki/Runway_(company) ; off. runway.com/changelog (aucune entrée Gen-5, consulté 2026-10-10). |
| **Aleph 2.0 + Edit Studio** : 21/05/2026. On retouche une image, Aleph 2.0 propage la retouche sur toute la vidéo. API le 02/06/2026. | [SOURCÉ] off. runway.com/changelog (21/05/2026) ; off. docs.dev.runwayml.com api_changelog. |
| Aleph 2.0 : clips jusqu'à 30 s en 1080p ; Gen-4 Aleph retiré le 30/07/2026. | [À VÉRIFIER] sec. pexo.ai, picsart (2026). |
| Export **ProRes 4444 ou séquence PNG** pour Gen-4.5 et Aleph 2 (plans Pro et plus). | [SOURCÉ] off. runway.com/changelog (10/08/2026). |
| **Plugins Adobe** (Premiere et After Effects, restyle Aleph 2) le 08/09/2026 ; **plugin DaVinci Resolve** le 23/09/2026. | [SOURCÉ] off. runway.com/changelog. |
| **Runway Ruby** : étalonnage HDR d'une vidéo SDR (20/08/2026) ; conversion HDR10 / HLG / ProRes HDR (28/08/2026). | [SOURCÉ] off. runway.com/changelog. |
| **Enhance Frame Rate** : conversion de 25 à 120 i/s, jusqu'en 4K et 5 min (plan Max+). | [SOURCÉ] off. runway.com/changelog (17/09/2026). |
| Runway revend aussi Seedance 2.0 / 2.5, Kling 3.0 / O3, Wan 3.0, Hailuo 3.0, Gemini Omni Flash, Grok Imagine 1.5, Nano Banana 2, Seedream 5.0, Ideogram 4.5, ElevenLabs v4. | [SOURCÉ] off. runway.com/changelog (avril à oct. 2026). |
| **Act-Two** (capture de jeu) : sorti le 21/07/2025. Aucun successeur trouvé. | [SOURCÉ] off. runway.com/changelog. Successeur : inconnu. |

### Kling (Kuaishou)
| Fait | Statut |
|---|---|
| Kling 3.0 / 3.0 Omni : 05/02/2026, 15 s, audio natif. Turbo et mise à jour Omni en juin 2026. | [SOURCÉ] sec. communiqué via Bernama (02/2026) ; Turbo [À VÉRIFIER] atlascloud (06/2026). |
| **Kling 4.0** : présenté le 28/09/2026. **4.0 Flash** en accès anticipé (abonnés Ultra annuels). Version complète annoncée « en octobre ». Clips jusqu'à **30 s**, plus d'une douzaine de types de références (texte, image, vidéo), jusqu'à 10 images clés. | [SOURCÉ] sec. briefs.co (28/09/2026) ; Bloomberg (28/09/2026) ; off. x.com/Kling_ai (fin sept. 2026). |
| Kling 4.0 annoncé en 4K, **HDR 10 bits**, audio stéréo, lip-sync amélioré. Flash : 20 s, 720p selon un comparatif. Prix 4.0 non publié. API : pas encore. | [À VÉRIFIER] annonce Kling sur X + blogs ; non testé, sortie complète non constatée au 2026-10-10. |
| Abonnement Ultra : environ 1 430 $/an. | [À VÉRIFIER] sec. aitoolanalysis, eesel.ai (2026). |

### Seedance (ByteDance)
| Fait | Statut |
|---|---|
| Seedance 2.0 : février 2026. Lettres de mise en demeure de Disney, Paramount et de la MPA (février 2026). ByteDance promet des garde-fous, sans détail. | [SOURCÉ] sec. axios.com (20/02/2026), au.variety.com (02/2026). |
| **Seedance 2.5** : présenté le 23/06/2026 (Volcano Engine FORCE). Jusqu'à **30 s en une passe** avec audio. Dans Runway le 11/08/2026, 1080p le 15/08/2026. Mode brouillon 480p le 02/10/2026. | [SOURCÉ] off. runway.com/changelog (11/08, 15/08, 02/10/2026) ; sec. digitalapplied, runtimewire (06/2026). |
| Seedance 2.5 en 4K, « 50 références » | [À VÉRIFIER] annonces de revendeurs avant sortie. |
| Seedance 2.0 en 4K dans Runway (22/07/2026). | [SOURCÉ] off. runway.com/changelog. |

### MiniMax Hailuo
| Fait | Statut |
|---|---|
| **H3 / Hailuo 3.0** : 31/07/2026 (dévoilé à la WAIC le 17/07). Texte, image, vidéo et audio en entrée. Jusqu'à 15 s en **2K**, son stéréo. Dans Runway le 05/08/2026. « H3 Max » chez Higgsfield le 31/08/2026. | [SOURCÉ] off. runway.com/changelog (05/08/2026) ; sec. huggingface.co blog, novoads.ai (08/2026). |
| Poids ouverts d'une version de base 768p (module 2K retenu) | [À VÉRIFIER] sources contradictoires (03/08 ou 05/08/2026, ou rien). |
| Environ 0,78 $ pour 6 s en 2K avec audio | [À VÉRIFIER] blog tiers. |

### Luma
| Fait | Statut |
|---|---|
| **Ray3.2** : 09/06/2026. Clips jusqu'à **20 s en 1080p**, jusqu'à 16 images clés, **génération HDR native, export EXR 16 bits**, suivi du jeu (posture et visage, jusqu'à 8 visages), recadrage et changement de fond. Première API Luma. | [SOURCÉ] off. lumalabs.ai/news/introducing-ray-3-2 (09/06/2026). Audio : non mentionné. |
| Ray3.14 : 26/01/2026, 1080p natif, plus rapide et moins cher que Ray3. | [SOURCÉ] off. businesswire (26/01/2026). |
| Luma Agents distribue aussi Hailuo 3.0 (06/08/2026). | [À VÉRIFIER] sec. runtimewire. |

### Alibaba Wan
| Fait | Statut |
|---|---|
| **Wan 3.0** : en test sur invitation le 06/08/2026, dans Runway et Higgsfield le 24/08/2026. Vidéo avec audio en 480p, 720p ou 1080p. **API fermée**. | [SOURCÉ] off. runway.com/changelog (24/08/2026) ; sec. orcarouter, evolink (08-09/2026). |
| Dernière version à **poids ouverts : Wan 2.2** (Apache 2.0, 2025). Wan 2.5 à 3.0 sont fermés. | [SOURCÉ] sec. howaiworks.ai (2026), kingy.ai (09/2026). Des pages annoncent des poids Wan 3.0 en avril 2026 : **faux** selon les sources récentes. |

### LTX (Lightricks) : l'open source vivant
| Fait | Statut |
|---|---|
| **LTX-2.5** : 11/08/2026. Poids sur Hugging Face, ComfyUI, API. 22 Md de paramètres, jusqu'en 4K, audio et vidéo, **plusieurs plans liés en une passe**. | [SOURCÉ] sec. venturebeat.com (08/2026) ; off. ltx.io/model/open-source. |
| **Licence** : « LTX-2.x Community License », gratuite sous 10 M$ de revenu annuel récurrent. **Pas une licence open source au sens OSI.** | [SOURCÉ] sec. innfactory.ai, medium (2026). Relire la licence avant usage client. |
| LTX-2.3 (05/03/2026) avec éditeur local. | [SOURCÉ] sec. en.wikipedia.org/wiki/LTX-2. |

### Higgsfield (agrégateur, pas un modèle)
| Fait | Statut |
|---|---|
| Série B de **400 M$** (valorisation 5,4 Md$), 17/08/2026, menée par DST Global. 700 M$ de revenu annualisé. | [SOURCÉ] off. prnewswire (17/08/2026). |
| Produits maison : Cinema Studio 4.0 (12/08), Relight et palette (20/08), Genjutsu (01/09), Ads Studio (30/09), AI Influencer (02/10), Ad Multiplier (06/10), skill « Katana » pour Claude (08/10/2026). **API publique** le 16/09/2026 (50+ modèles, paiement à la génération). | [SOURCÉ] off. higgsfield.ai/creator-hub/changelog (consulté 2026-10-10). |
| Plugins After Effects / Premiere (21/07/2026), Blender (21/08/2026), serveur MCP. | [SOURCÉ] off. higgsfield.ai/blog/higgsfield-after-effects (21/07/2026) ; changelog. |
| Modèles tiers ajoutés : Seedance 2.5 (03/08), Wan 3.0 (24/08), Gemini Omni 1.1 Flash (28/08), MiniMax H3 Max (31/08), GPT Image 2.5 (22/09), Eleven v4 (28/09), FLUX 3 Image (01/10), Nano Banana 2.1 (06/10/2026). **Kling 4.0 absent** du changelog au 10/10. | [SOURCÉ] off. changelog Higgsfield. |
| Outil de « similarity scoring » (ressemblance avec des œuvres protégées) pour les équipes, mars 2026. | [SOURCÉ] off. prnewswire (03/2026). |
| Générations **payantes en crédits** : jamais sans accord explicite du client. | Règle maison. |

### Pika, Moonvalley, Midjourney vidéo, autres
| Fait | Statut |
|---|---|
| **Pika** : se repositionne en plateforme multi-modèles (« Welcome to the New Pika », 17/09/2026) ; Pika Music, SFX, Speech, Soundtrack (18/08/2026). Modèle maison : 2.5 (date inconnue). | [À VÉRIFIER] off. pika.art (dates lues via recherche, page non ouverte). |
| **Moonvalley / Marey** : modèle entraîné sur données sous licence (sortie générale juillet 2025). **Aucune annonce 2026 trouvée.** Prix actuel : inconnu. | [SOURCÉ] sec. cined.com (07/2025). 2026 : inconnu. |
| **Midjourney vidéo** : toujours image vers vidéo (clips de 5 s, extensibles par 4 s jusqu'à 21 s). Pas de modèle vidéo V2 trouvé. | [À VÉRIFIER] sec. (2026). |
| **Grok Imagine 1.5** (xAI) : 1 à 15 s, 1080p, audio. | [SOURCÉ] off. runway.com/changelog (13/08/2026). |
| **FLUX 3** fait aussi de la vidéo (voir §2). | |

### Adobe Firefly Video
| Fait | Statut |
|---|---|
| Firefly agrège plus de 30 modèles (dont Veo 3.1, Gen-4.5, Kling 3.0 / Omni, Nano Banana 2). | [SOURCÉ] off. blog.adobe.com (15/04/2026). |
| Firefly AI Assistant (27/04/2026), puis agent créatif dans Premiere, Photoshop, etc. (18/06/2026, bêta publique ; bêta privée dans AE). | [SOURCÉ] off. news.adobe.com (06/2026). |
| **Nouveau modèle Firefly Video maison en 2026 : aucune note officielle trouvée.** | Inconnu. |
| **Adobe MAX 2026 : 10-12 novembre (Miami Beach).** Les annonces ne sont pas encore faites. | [SOURCÉ] sec. creativebloq (2026). |

---

## 2. Image

| Fait | Statut |
|---|---|
| **Midjourney V8.2** : modèle par défaut depuis le 24/07/2026. V8 alpha en mars, V8.1 le 14/04/2026. Pas d'API officielle. | [SOURCÉ] sec. tech-insider, pixmind, javisreview (2026) qui citent la page Version de Midjourney (docs.midjourney.com, 403 à la lecture). |
| **Nano Banana 2** (Gemini 3.1 Flash Image) : 26/02/2026, défaut dans l'appli Gemini. **Nano Banana Pro** (Gemini 3 Pro Image, nov. 2025) toujours proposé. Disponibilité générale entreprise le 28/05/2026. | [SOURCÉ] sec. techcrunch.com (26/02/2026) ; off. cloud.google.com blog (05/2026). |
| **Nano Banana 2.1** (`gemini-nano-banana-2.1`) : **GA le 06/10/2026** *(date précisée, session 19)*. Nano Banana 2 (`gemini-3.1-flash-image`) déprécié, sans date d'arrêt officielle. Jusqu'en 4K, 14 images de référence, meilleur rendu du texte. Prix API : 0,034 $ (1K) à 0,113 $ (4K) par image. | [SOURCÉ] off. ai.google.dev (modèle et prix, consulté 2026-10-10) ; sec. seroundtable (10/2026). |
| **GPT Image 2** (ChatGPT Images 2.0) : 21/04/2026, raisonnement avant génération, 2K. | [SOURCÉ] sec. thenewstack, neurohive (04/2026). |
| **GPT Image 2.5** (ChatGPT Images 2.5) : 08/09/2026. Deux variantes API : Flare (défaut) et Sunburst (précis). Jusqu'à 50 % plus rapide. | [SOURCÉ] sec. axios.com (08/09/2026). Résolution 3840×2160 et 16 références : [À VÉRIFIER]. |
| **FLUX 3** (Black Forest Labs) : 23/07/2026. Modèle multimodal (image, vidéo jusqu'à 20 s avec son). Vidéo par API en août ; **FLUX 3 Image le 01/10/2026** (notes de version BFL, voir session 19). Poids ouverts « Dev » promis, pas encore sortis. FLUX.2 reste le modèle image conseillé par la doc BFL. | [SOURCÉ] sec. marktechpost (26/07/2026), winbuzzer (28/07/2026). Dates de déploiement : [À VÉRIFIER]. |
| **Seedream 5.0** (ByteDance) : 10/02/2026 ; Pro en juin-juillet 2026. Jusqu'à 14 références. | [SOURCÉ] sec. newsquawk (13/02/2026) ; off. runway.com/changelog (15/07/2026). |
| **Ideogram 4.0** : 03/06/2026, 2K natif, mise en page par boîtes. Poids non commerciaux. **Ideogram 4.5** : listé chez Higgsfield (30/09) et Runway (02/10/2026). Détails 4.5 : inconnus. | [SOURCÉ] sec. en.wikipedia.org/wiki/Ideogram (4.0) ; off. runway.com/changelog (4.5). |

---

## 3. Outils de post intégrés

### Adobe Premiere (le « Pro » a disparu en version 26)
| Fait | Statut |
|---|---|
| **Premiere 26.5** (annonce du 10/09/2026) : **Generative Media Tool** (vidéo et effets sonores générés dans la timeline, « Firefly et modèles partenaires », images existantes comme référence) ; **Paper Edit** (premier montage depuis la transcription) ; Object Mask avec modes **Sharp** et **Smooth** (cheveux, tissu). | [SOURCÉ] off. community.adobe.com, « What's new in Adobe Premiere 26.5 » (10/09/2026). |
| **Generative Extend** : sources acceptées de 360p à 4K UHD, tous formats, entrelacé et pixels non carrés (26.5). Notes de version : sources de 12 à 60 i/s, 8 à 16 bits, SDR ou HDR. | [SOURCÉ] off. community.adobe.com (10/09/2026) ; off. helpx.adobe.com release notes (extrait de recherche, page en 403). |
| Generative Extend : extension toujours de **2 s vidéo / 10 s audio**. Les frames générées sortent en 8 bits SDR si la séquence l'est ; au-delà de 30 i/s, extension à 30 i/s. | [À VÉRIFIER] FAQ Adobe (extrait de recherche) et atlascloud (blog vendeur). |
| Color Mode (bêta) annoncé à la NAB, 15/04/2026. | [SOURCÉ] off. blog.adobe.com (15/04/2026). |

### After Effects
| Fait | Statut |
|---|---|
| **Object Matte** : quatre outils (Object Selection, Quick Selection, Selection Brush, Refine Edge). Même IA que l'Object Mask de Premiere. **Roto Brush est renommé Quick Selection**, il n'est pas supprimé. | [SOURCÉ] off. community.adobe.com, « New in Beta: Object Matte » (19/02/2026). |
| Sortie en version finale avec AE 26.2 (15/04/2026). | [À VÉRIFIER] sec. creativeainews (2026). |
| Retours de bêta : rendu lent, crénelage, propagation qui casse en cours de plan. | [SOURCÉ] off. même fil (réponses jusqu'au 13/05/2026). |

### DaVinci Resolve
| Fait | Statut |
|---|---|
| Resolve 21.0 final le 02/06/2026 : page Photo, IntelliSearch, CineFocus, Speech Generator, Face Age / Reshaper, UltraSharpen. | [SOURCÉ] sec. newsshooter (02/06/2026). |
| **Resolve 21.1** : 08/09/2026 (IBC). Nouveauté IA officielle : **assistants externes** (Claude, Claude Code, ChatGPT Codex) qui analysent le projet, rangent les médias, règlent et lancent les rendus ; préférence de décodage pour les outils IA. | [SOURCÉ] off. blackmagicdesign.com/media/partial/release/20260908-03 (08/09/2026). |
| Pilotage par **serveur MCP natif**, réservé à Studio (passe par l'API de script). | [SOURCÉ] sec. ymcinema (09/09/2026), notebookcheck. |
| IntelliTrack, Magic Mask 2.0, remplacement de dialogue IA en 21.1 | [À VÉRIFIER] une seule source (sportsvideo.org, 09/09/2026) ; **absents du communiqué officiel**. |
| Studio : licence perpétuelle 295 $. | [SOURCÉ] sec. kompozy (2026). |

### Topaz Labs
| Fait | Statut |
|---|---|
| **Starlight Precise 2.5** : 31/03/2026, pour amener des rushes IA en 4K. Disponible en local le 28/04/2026. | [SOURCÉ] off. topazlabs.com/news (03/2026 et 04/2026). |
| **Astra 2** (upscale cloud) : 28/04/2026. **Hyperion 2** (conversion SDR vers HDR) et **panneau Topaz pour Premiere** : 07/05/2026. NeuroStream (jusqu'à −95 % de VRAM). | [SOURCÉ] off. topazlabs.com/news, prnewswire (28/04 et 07/05/2026). |
| **Topaz appartient à Adobe** : accord le 25/06/2026, rachat finalisé le **23/09/2026**. Topaz reste une marque et des applis autonomes ; intégration prévue dans Firefly et Photoshop d'abord, puis vidéo (upscale, restauration d'archives, basse lumière). Aucune nouvelle version de modèle Topaz trouvée de juillet à octobre 2026. *(Corrigé session 19 : la ligne disait « aucune sortie ».)* | [SOURCÉ] off. blog.adobe.com (23/09/2026) ; sec. petapixel (23/09/2026), newsshooter (25/06/2026). |
| Interpolation : Apollo (ralenti), Chronos (changement de cadence, ex. 24 vers 60), Aion (jusqu'à 16×). Accessible depuis Resolve. | [SOURCÉ] off. developer.topazlabs.com/video-models/frame-interpolation (consulté via recherche). |

### Détourage IA hors suites
| Fait | Statut |
|---|---|
| **SAM 3** (19/11/2025) puis **SAM 3.1** (27/03/2026, « Object Multiplex », environ 7× plus rapide à 128 objets). API Meta hébergée annoncée le 18/09/2026. Pas de « SAM 3.5 ». | [SOURCÉ] sec. learnopencv.com (2026), arxiv 2511.16719. API Meta : [À VÉRIFIER]. |
| Runway : SAM3 Video Segmentation, export WebM transparent (28/07/2026). | [SOURCÉ] off. runway.com/changelog. |
| Plugins SAM pour AE ou Nuke | [À VÉRIFIER] seul un site peu fiable l'affirme. |

### Interpolation
- Labo maison [LABO] : RIFE 4.25 bat `minterpolate` sur image lisse, mais reste **sous un simple fondu** sur de l'eau et du feuillage (`labo/interpolation/`, `labo/interpolation-reel/`).
- Nouvelles offres : Runway Enhance Frame Rate (17/09/2026), Topaz Aion (16×). Non testées.

---

## 4. Voix et musique

| Fait | Statut |
|---|---|
| **Eleven v4 et v4 Turbo** (ElevenLabs) : 28/09/2026. Plus de 90 langues, clonage amélioré. Turbo : environ 100 ms de latence (temps réel). | [SOURCÉ] off. elevenlabs.io/docs/changelog/2026/9/28 et elevenlabs.io/blog/eleven-v4. |
| Eleven v3 : disponibilité générale le 02/02/2026 (balises d'émotion, dialogue). | [SOURCÉ] sec. coval.ai (2026). |
| **Eleven Music** : présenté par ElevenLabs comme « fully licensed », construit avec artistes, labels et éditeurs. Plateforme ElevenMusic (découverte, remix, revenus). | [SOURCÉ] off. elevenlabs.io/music, elevenlabs.io/blog/introducing-elevenmusic (2026). La portée exacte des licences : [À VÉRIFIER] dans les CGU. |
| **Suno v6** (v6, v6-wild, v6-mini) : 09/09/2026. Construit avec Warner, BMG et Believe. v6 et v6-wild réservés aux abonnés Pro et Premier ; v6-mini pour tous. Morceaux jusqu'à 8 min. Anciens modèles retirés. | [SOURCÉ] sec. routenote.com (20/09/2026), aimusicpreneur (09/2026). |
| Suno : accord Warner (25/11/2025). **UMG et Sony poursuivent toujours**, avec une seconde plainte le 18/09/2026 (environ 60 000 enregistrements). Jugement sur le fond pas avant 2027. Enquête en Italie sur les CGU. | [SOURCÉ] sec. billboard (11/2025), lawcommentary, musicbusinessworldwide (2026). |
| **Udio** : accords UMG (29/10/2025) et Warner (19/11/2025). **Sony poursuit.** Téléchargements coupés depuis le 29/10/2025, toujours coupés fin septembre 2026. Plateforme sous licence promise en 2026, pas de date. | [SOURCÉ] sec. billboard (10/2025), chatgptiseatingtheworld (19/11/2025), aitools-directory (2026). |
| Seed Audio 1.0 (ByteDance) : jusqu'à 120 s de voix, sound design et musique. | [SOURCÉ] off. runway.com/changelog (29/06/2026). |

---

## 5. Régulation et usages

### AI Act (UE), article 50
| Fait | Statut |
|---|---|
| Article 50 applicable depuis le **02/08/2026**. Non reporté par l'Omnibus numérique (Règl. (UE) 2026/1744, JO du 24/07/2026). | [SOURCÉ] off. eur-lex.europa.eu (Règl. 2024/1689) ; sec. lewissilkin (27/07/2026). |
| Seul délai : marquage lisible par machine (50(2)) des systèmes déjà sur le marché → **02/12/2026**. Le signalement des deepfakes par le déployeur (50(4)) n'a **aucun délai**. | [SOURCÉ] sec. lewissilkin, compliancehub (2026). |
| **Lignes directrices finales** de la Commission : C(2026) 5054, adoptées le **20/07/2026** (projet le 08/05/2026). Non contraignantes, mais les autorités les suivront. | [SOURCÉ] sec. twobirds.com, gtlaw.com (06-07/2026). |
| Points utiles au monteur : un contenu qui ressemble à une personne réelle se signale **même sans intention de tromper**. Œuvre manifestement artistique ou fictionnelle : mention due, mais **sans gêner l'œuvre**. **Pas de rétroactivité** : compte la date de génération (avant le 02/08/2026 = pas d'obligation). | [SOURCÉ] sec. gtlaw.com (06/2026), ipglobalguard (2026). |
| Code de pratique sur le marquage : 10/06/2026, volontaire, marquage multicouche (métadonnées + filigrane) et icône UE. | [SOURCÉ] off. digital-strategy.ec.europa.eu (10/06/2026). |
| Amendes : jusqu'à 15 M€ ou 3 % du CA mondial. | [SOURCÉ] sec. fedil.lu (2026). |
| **France** : pas de loi spécifique. Projet de loi d'adaptation adopté au Sénat le 18/02/2026, en attente à l'Assemblée au 16/09/2026. Rôle prévu de l'Arcom pour l'audiovisuel et les deepfakes, non acté. | [À VÉRIFIER] sec. blogs juridiques (2026). |

### C2PA / Content Credentials
| Fait | Statut |
|---|---|
| Spécification 2.3 (signature du direct, segments CMAF) ; une 2.4 serait en usage en mai 2026. | [À VÉRIFIER] sec. irdeto, wikipedia (2026). |
| Pixel 10 : Content Credentials sur chaque photo (sept. 2025). Leica M11-P, caméra pro Sony. | [SOURCÉ] off. blog.google (09/2025). |
| Faille de falsification sur Android (août 2026) | [À VÉRIFIER] source unique. |

### Plateformes
| Fait | Statut |
|---|---|
| **YouTube** : depuis le 27/05/2026, **étiquette automatique** si un contenu photoréaliste IA n'est pas déclaré. Étiquette sous le lecteur (vidéos longues), en surimpression (Shorts). Étiquette permanente si C2PA indique une génération complète ou si l'outil est YouTube (Veo, Dream Screen). | [SOURCÉ] off. blog.youtube « Improving AI labels » (27/05/2026) ; sec. macrumors (27/05/2026). |
| YouTube : la monétisation vise le contenu « inauthentique » (produit en masse), pas l'IA en soi. | [À VÉRIFIER] blogs (2026), règle de juillet 2025. |
| **TikTok** : étiquette visible pour les visuels et sons réalistes IA, lecture des métadonnées C2PA. Plus de 3 milliards de vidéos étiquetées. | [À VÉRIFIER] blogs ; chiffres non retrouvés chez TikTok. |
| **Meta** : étiquetage IA sur FB, IG, Threads ; pub : l'annonceur est responsable des variantes générées (avril 2026). | [À VÉRIFIER] blogs (2026). |

### Syndicats, académies, festivals
| Fait | Statut |
|---|---|
| **SAG-AFTRA** : accord avec l'AMPTP le 03/05/2026. Pas de « taxe Tilly » ; les studios n'utilisent un interprète synthétique que s'il apporte une « valeur additionnelle significative » ; arbitrage dédié. | [SOURCÉ] sec. variety.com (2026), fortune (28/03/2026). |
| **Oscars (99e cérémonie)** : règles du 01/05/2026. Jeu et scénario doivent être humains pour concourir ; l'Académie peut demander quel usage de l'IA a été fait. | [SOURCÉ] sec. npr/vpm.org (02/05/2026), gigazine (07/05/2026). Texte officiel non relu. |
| **Cannes 2026** : Frémaux affiche sa méfiance ; une œuvre conçue par IA ou avec comédiens virtuels « n'a pas sa place ». **Aucun règlement écrit cité.** Deux films hors compétition ont utilisé des outils IA (Jaoui, Soderbergh). | [SOURCÉ] sec. franceinfo.fr (12/05/2026). « Interdiction gravée au règlement » : [À VÉRIFIER], blogs seulement. |
| **SACD, SCAM, SACEM, SNE** : tribune commune, plus de 21 000 signatures fin avril 2026. César : pas de règle formelle trouvée. | [À VÉRIFIER] source secondaire unique. |

---

## 6. Ce qui était faux ou périmé dans la version du 2026-10-09

1. **Generative Extend « 12-30 i/s, 8 bits SDR seulement »** : périmé. Les sources acceptées vont désormais de 12 à 60 i/s, 8 à 16 bits, SDR ou HDR, 360p à 4K. La **sortie** resterait en 8 bits SDR (à vérifier).
2. **« Midjourney V7 reste par défaut »** : faux. V8.2 est le défaut depuis le 24/07/2026.
3. **« Aleph 2.0 connu seulement par un catalogue tiers »** : faux. Officiel chez Runway le 21/05/2026.
4. **« Hailuo 2.3, pas de version suivante »** : périmé. Hailuo 3.0 / H3 le 31/07/2026.
5. **« Wan 2.6, open source non confirmé »** : périmé. Wan 3.0 le 24/08/2026, fermé. Poids ouverts jusqu'à 2.2 seulement.
6. **Kling 3.0 en tête** : périmé. Kling 4.0 annoncé le 28/09/2026 (30 s), en déploiement.
7. **Seedance 2.0** : périmé. Seedance 2.5 (30 s, audio) disponible depuis août 2026.
8. **FLUX.2, GPT Image 2, Nano Banana Pro comme références** : périmés. FLUX 3 (23/07), GPT Image 2.5 (08/09), Nano Banana 2 et 2.1 (février et octobre 2026).
9. **Eleven v3 comme dernier modèle** : périmé. Eleven v4 le 28/09/2026.
10. **Suno « nouveaux modèles sous licence en 2026 »** : réalisé. Suno v6 le 09/09/2026, anciens modèles retirés. UMG et Sony ont **relancé** une plainte le 18/09/2026.
11. **Resolve 21.1 = IntelliTrack + Magic Mask 2.0** : non confirmé. Le communiqué officiel ne parle que des assistants IA (Claude, ChatGPT Codex).
12. **« After Effects Roto Brush : non trouvé »** : corrigé. Object Matte ; Roto Brush devient Quick Selection.
13. **« Interpolation : non trouvé »** : corrigé (Topaz Apollo / Chronos / Aion, Runway Enhance Frame Rate) ; labo maison ajouté.
14. **Starlight « version 2.5 ou 2.6 »** : c'est **Precise 2.5** (officiel, 31/03/2026).
15. **Veo « retrait d'objet non confirmé »** : la page DeepMind liste désormais insertion **et retrait** d'objet.
16. **Luma Ray3.2 « sources secondaires seulement »** : confirmé par Luma (09/06/2026), avec HDR et EXR 16 bits.
17. **« Seule Sora n'est plus dans les classements »** : à compléter, OpenAI n'a **plus aucune** offre vidéo publique.

## 7. Ce que cette recherche n'a pas couvert

- Le texte EUR-Lex des lignes directrices C(2026) 5054 (lu via cabinets d'avocats seulement).
- Les CGU commerciales en vigueur de Suno v6, Eleven Music, Kling 4.0, Seedance 2.5.
- Les annonces d'Adobe MAX (10-12 novembre 2026), à reprendre après l'événement.
- La sortie complète de Kling 4.0 (« octobre »), à constater.
- Les règlements officiels de Cannes, des César et des Oscars (non relus en source primaire).

---

## Veille du 2026-10-10 (session 19)

Fenêtre visée : 30/09 → 10/10/2026. WebSearch (standard puis étendu) + WebFetch des changelogs officiels. Rien testé. Sources : `sources/ia-generative-2026-10-10.md`, section « Veille session 19 ».

### Nouveautés datées
| Date | Nouveauté | Statut |
|---|---|---|
| 01/10/2026 | **FLUX 3 Image** (Black Forest Labs) : un seul point d'API pour générer, retoucher et composer ; **boîtes de placement** en JSON dans le prompt ; retouches locales multiples (recolorer, déplacer, retirer) sans toucher au reste ; 10 références ; de 768 px à 4K (~16 Mpx), 15 formats. Prix : 0,048 $ (1K) à 0,607 $ (4K) par image. Poids : non publiés. | [SOURCÉ] off. docs.bfl.ai/release-notes (01/10/2026) ; off. changelog Higgsfield (01/10/2026). |
| 06/10/2026 | **Nano Banana 2.1** GA : meilleure cohérence de personnage sur plusieurs tours, texte, et **formats extrêmes** 1:4, 4:1, 1:8, 8:1 en 1K/2K/4K. Déployé dans Gemini, Flow, AI Studio. Nano Banana 2 déprécié. Arrêt de NB2 au 29/10 : [À VÉRIFIER] (blogs seulement). | [SOURCÉ] off. ai.google.dev changelog (06/10/2026) ; sec. jetstream.blog, cellcog (10/2026). |
| 28/09 → 10/10/2026 | **Kling 4.0** : seule la version **Flash** est ouverte (accès anticipé limité, abonnés Ultra annuels). Version complète toujours annoncée « en octobre », **sans jour**, et **non sortie au 10/10**. Specs rapportées (3-30 s, 4K, 10 images clés, stéréo, prompt 8 000 tokens, 21:9 à 9:16) ; HDR 10 bits et extension 2 min « à venir ». | [À VÉRIFIER] sec. atlascloud, blog.mean.ceo (05/10/2026), qui citent la note de version Kling (page vide à la lecture). |
| 06/10/2026 | **Kling AI** prépare une IPO à Hong Kong (≥ 1 Md$, banques CICC, Goldman, UBS ; cotation visée 2027). Contexte : levée de 2,8 Md$ en juillet. | [SOURCÉ] sec. Bloomberg via technode.com (08/10/2026) ; aiweekly. Non commenté par Kling. |
| 29/09/2026 | **OpenAI Dots** (DevDay) : agents ChatGPT permanents. **Runway** (01/10) et **Higgsfield** (29/09) s'y branchent : on peut commander des plans vidéo depuis ChatGPT. **Aucun nouveau modèle image, vidéo ou audio OpenAI** trouvé à DevDay 2026. | [SOURCÉ] off. runway.com/changelog (01/10) ; off. changelog Higgsfield (29/09) ; sec. siliconangle (29/09/2026). |
| 30/09 → 08/10/2026 | **Higgsfield** : Genjutsu **Restyle** (re-dessine une vidéo en gardant le mouvement, 30/09), Ideogram 4.5 (30/09), Grok Imagine Video 1.5 (01/10), extension ChatGPT (30/09). Autres entrées déjà listées au §1. | [SOURCÉ] off. changelog Higgsfield (consulté 2026-10-10). |
| 02/10/2026 | **Runway** : Seedance 2.5 brouillon 480p dans Agent, Ideogram 4.5 dans le MCP Runway. **Aucune entrée du 03 au 10/10.** | [SOURCÉ] off. runway.com/changelog. |
| 05/10/2026 | **ElevenLabs** : rien de neuf côté voix ou musique depuis Eleven v4 (28/09) ; le 05/10 ne touche que les agents et SDK. Speech to Text : correction de transcription en langage naturel (28/09). | [SOURCÉ] off. elevenlabs.io/docs/changelog. |

### Rattrapages (antérieurs à la fenêtre, absents du fichier)
- **Adobe rachète Topaz Labs** : finalisé le 23/09/2026 (voir §3, ligne corrigée). Topaz reste vendu à part. [SOURCÉ] off. blog.adobe.com ; sec. petapixel.
- **Premiere 26.5, Generative Media Tool** : le choix de modèle inclut nommément **Firefly, Veo, Kling, Runway, Luma** ; **Generate Music** et **Generate Soundscape** (analyse jusqu'à 15 s d'image) restent en bêta. **AI Assistant d'After Effects** en bêta publique (écrit le JavaScript et monte un rig à curseurs). [SOURCÉ] off. blog.adobe.com (08/09/2026) ; sec. postmagazine, provideocoalition (09/2026).
- **Lyria 3.5** (musique Google) GA le 03/09/2026 ; **TTS Gemini 3.8 Flash** GA le 22/09/2026. CGU commerciales non lues. [SOURCÉ] off. ai.google.dev changelog.

### Rien de neuf trouvé (30/09 → 10/10)
Veo (toujours 3.1), Sora (fermé), Luma (Ray3.2), MiniMax Hailuo (H3), Wan (3.0 fermé, poids : 2.2 max), LTX (2.5), Pika, Midjourney (V8.2), Seedance (2.5 ; pas de 3.0), Suno, Udio, Resolve (21.1), Topaz (aucun modèle), Blender. Procès : Sony a relancé une 2e plainte contre Udio le 20/07/2026 (30 117 enregistrements) ; pas de jugement sur le fond trouvé. [SOURCÉ] sec. musicbusinessworldwide, variety (07/2026).

### Ce que ça change pour le monteur / motion designer
- **FLUX 3 Image, boîtes de placement** : enfin une image fixe **composée** (où va le produit, où va le titre) plutôt que tirée au sort. À utiliser pour les cartons, key visuals, plaques de fond pour AE, où la place réservée au texte compte. Cliché à éviter : l'image « parfaite » centrée, lumière de pub, sans grain ; réintroduire grain, défauts, et laisser la typo faite dans AE (plus nette et modifiable). Retouches locales = utile pour décliner un fond sans régénérer.
- **Nano Banana 2.1, formats 8:1 / 1:8** : plaques panoramiques pour un **travelling latéral** ou un parallaxe 2,5D dans AE, bannières, fonds de générique défilant. Piège : à 4K sur 8:1, chaque tranche reste basse définition une fois recadrée en 16:9 ; vérifier au zoom 100 %. Cliché : le panorama « fantasy » sans perspective cohérente, qui casse dès que la caméra bouge.
- **Kling 4.0** : **ne pas le promettre au client** tant que la version complète n'est pas sortie et testée ; Flash (720p, 20 s selon blogs) suffit pour une prévisu, pas pour une livraison. Les 30 s d'un tenant tentent de faire des plans-séquences IA : un plan long expose plus longtemps les dérives (mains, textes, physique). Couper plus tôt reste souvent le meilleur choix de montage.
- **Genjutsu Restyle / restyle vidéo** (comme Aleph 2) : utile pour un **passage onirique** ou une transition de style motivée par le récit. Cliché : le filtre « anime » ou « peinture » plaqué sur tout un clip sans raison dramaturgique ; limiter à un moment, et garder le plan réel avant et après comme point d'ancrage.
- **Agents (Dots, Claude, MCP)** qui commandent des plans : gain pour les déclinaisons pub, risque de générations payantes non validées. Règle maison inchangée : pas de génération en crédits sans accord écrit, et le DA choisit les plans, pas l'agent.
- **Topaz chez Adobe** : à terme l'upscale Topaz dans Premiere. Rien ne change pour l'éthique : sur archive ou visage réel, un upscale par diffusion **invente** du détail, à signaler (AI Act art. 50 si la personne est reconnaissable).

### Corrections faites en place (session 19)
1. §1 Google : **Gemini Omni 1.1 Flash** n'est plus [À VÉRIFIER] : GA officielle le 27/08/2026 ; point d'accès preview déprécié le 30/09/2026.
2. §2 Image : **Nano Banana 2.1** daté au **06/10/2026** (au lieu de « début octobre ») ; NB2 déprécié.
3. §2 Image : **FLUX 3 Image** daté au **01/10/2026** par les notes de version BFL (n'est plus « Higgsfield seulement »).
4. §3 Topaz : « aucune sortie entre juillet et octobre » remplacé par le **rachat par Adobe** (23/09/2026).
5. §7 reste valable : Kling 4.0 complet et Adobe MAX (10-12/11) toujours à constater.

---

## Veille du 2026-10-10 (session 20)

Fenêtre : 03/10 → 10/10/2026, refaite le même jour que la session 19 (WebSearch standard et étendu, WebFetch des changelogs Higgsfield, Runway, Gemini API, ElevenLabs). Rien testé. Sources : `sources/ia-generative-2026-10-10.md`, section « Veille session 20 ».

**Bilan : presque rien de neuf depuis la session 19.** Aucun nouveau modèle vidéo, image, voix, musique, upscale, interpolation ou détourage n'a été publié entre la session 19 et le 10/10 au soir.

### Constats datés (confirmés par source officielle)
| Date | Fait | Statut |
|---|---|---|
| 10/10/2026 | **Kling 4.0 complet : toujours pas sorti.** Seule la Flash est ouverte ; absent des changelogs Higgsfield et Runway. | [SOURCÉ] off. changelogs Higgsfield et Runway (consultés 2026-10-10) ; sec. atlascloud (seule source sur le « octobre », sans jour). |
| 08/10/2026 | Gemini API : seules des dépréciations de modèles texte (3.5 / 3.7 Flash, Deep Research). **Rien sur Veo, Omni, Lyria, TTS.** Arrêt de Nano Banana 2 : **toujours sans date officielle** (le « 29/10 » des blogs reste [À VÉRIFIER]). | [SOURCÉ] off. ai.google.dev changelog (08/10/2026). |
| 05 → 08/10/2026 | **Higgsfield Global Film Festival** : vote du public ouvert le 08/10 (jusqu'au 15/10), jury du 09 au 14/10, palmarès « dernière semaine d'octobre ». Dotation totale 1 M$ ; films faits **uniquement** dans Cinema Studio. | [SOURCÉ] off. changelog Higgsfield (05 et 08/10) ; off. higgsfield.ai/blog. Règle d'exclusion des plans Veo / Kling : [À VÉRIFIER] (guide tiers). |
| 03/10/2026 | Higgsfield : pannes Seedance réglées, générations remboursées. | [SOURCÉ] off. changelog Higgsfield. |

### Rattrapages (antérieurs à la fenêtre, absents du fichier)
- **Meta Muse Image** (sorti) et **Muse Video** (aperçu, avec son) : 07/07/2026. Muse Video est annoncé « bientôt » dans Meta AI, **toujours non disponible** au 10/10, pas d'API. Durée, résolution, prix : inconnus. [SOURCÉ] off. ai.meta.com/blog/introducing-muse-image-muse-video-msl ; sec. gigazine (08/07/2026), aireiter (08/2026).
- **ElevenLabs** : Seedance 1.5 Pro retiré de ses Flows le **11/11/2026** (annonce du 23/09). [SOURCÉ] off. elevenlabs.io/docs/changelog.
- **Suno** : un juge a autorisé UMG et Sony à ajouter l'accusation de **« stream ripping »** (entraînement sur des téléchargements YouTube), plainte modifiée le 25/08/2026 ; l'ajout de 61 026 titres a été refusé (18/08). [SOURCÉ] sec. musicbusinessworldwide (08/2026).

### Rapporté par la presse, non retenu
- « Grok Imagine 2 » vidéo (4K, 30 s) : un seul annuaire tiers ; xAI en reste à Video 1.5. « Suno v5 » ou « ElevenLabs v3 » présentés comme nouveautés d'octobre (voxbooster) : **faux**, dépassés par v6 et v4. Seedance 2.5 « 50 références » : toujours [À VÉRIFIER].

### Rien de neuf (03 → 10/10)
Veo / Flow, Omni, Runway (dernière entrée 02/10), Luma, Hailuo, Wan, LTX, HunyuanVideo, Pika, Midjourney (V8.2, pas de vidéo V2), Firefly (rien avant MAX, 10-12/11), Topaz, SAM, ElevenLabs (rien après le 05/10, agents seulement), Suno, Udio.

### Ce que ça change pour le monteur / motion designer
- **Kling 4.0 en attente** : rien ne bouge ; garder Veo 3.1, Kling 3.0 ou Seedance 2.5 pour tout devis d'octobre, et ne pas bâtir un découpage sur des plans de 30 s promis mais non livrés.
- **Muse Video (Meta)** : à surveiller pour le social (génération directement dans Instagram / Meta AI). Artistiquement, attendre : Meta reconnaît des décalages son-image et des mouvements rapides peu crédibles, soit précisément ce qui casse un raccord dans le rythme.
- **Festival Higgsfield** : bon baromètre de l'esthétique « tout IA » de 2026. Le regarder comme on regarde une banque d'images, pour repérer les **clichés** à fuir (travellings flottants, visages lisses, lumière de pub). L'exclusivité d'un outil dit aussi qu'un film primé là n'est pas une preuve de fiabilité en production.
- **Seedance 1.5 Pro retiré le 11/11** : un projet qui doit être regénéré à l'identique (retouche client) ne pourra plus l'être. Archiver les rushes IA bruts et noter modèle, version et prompt dans le dossier projet.
- **Suno, accusation de « stream ripping »** : renforce la règle maison : pas de Suno sur une pub ou une diffusion TV sans clause écrite.

---

## Veille du 2026-10-10 soir (session 21)

Fenêtre : 08/10 → 10/10/2026 (~17h30 UTC), troisième passage du jour. WebSearch standard et étendu, WebFetch des changelogs Higgsfield, Runway, Gemini API, ElevenLabs. Rien testé. Sources : `sources/ia-generative-2026-10-10.md`, section « Veille session 21 ».

**Bilan : rien de neuf depuis la session 20.** Aucun nouveau modèle vidéo, image, voix, musique, upscale, interpolation ou détourage trouvé. Deux rattrapages audio (antérieurs) seulement.

### Constats datés
| Date | Fait | Statut |
|---|---|---|
| 10/10/2026 | **Kling 4.0 complet : toujours pas sorti** ; toujours « octobre », sans jour, une seule source tierce. | [SOURCÉ] off. changelogs Higgsfield et Runway (consultés 10/10 soir) ; sec. atlascloud. |
| 08/10/2026 | Higgsfield : dernière entrée = Katana + vote du festival. **Aucune entrée les 09 et 10/10.** | [SOURCÉ] off. changelog Higgsfield. |
| 02/10/2026 | Runway : dernière entrée toujours le 02/10. | [SOURCÉ] off. runway.com/changelog. |
| 08/10/2026 | Gemini API : page mise à jour le 09/10 **sans nouvelle entrée** ; Veo reste en 3.1 ; NB2 toujours sans date d'arrêt. | [SOURCÉ] off. ai.google.dev changelog. |
| 05/10/2026 | ElevenLabs : rien après le 05/10. | [SOURCÉ] off. elevenlabs.io/docs/changelog. |

### Rattrapages (antérieurs, absents du fichier)
- **ElevenLabs Music v2** (27/05/2026) : changement de genre en cours de morceau, composition section par section, **régénération d'un passage** (inpainting) ; accords Believe, Kobalt, Merlin. **Music v2.5** dans l'API le 14/09/2026. [SOURCÉ] sec. decrypt.co (27/05/2026) ; off. elevenlabs.io/docs/changelog (14/09).
- **Stable Audio 3.0** (Stability AI, 05/2026) : 4 modèles, jusqu'à ~6 min 20 s (Medium) ; **poids ouverts** pour Small et Medium (Hugging Face) ; Large en API réservé aux structures > 1 M$ de CA ; présenté comme entraîné sous licence (UMG, Warner). [SOURCÉ] sec. decrypt.co (27/05/2026). CGU non lues : [À VÉRIFIER].

### Rapporté, non retenu
- « MiniMax a publié des poids ouverts solides » : un seul récapitulatif de blog, sans modèle nommé. Pollo AI (09/10) : cas client OpenAI, pas un modèle.

### Rien de neuf (08 → 10/10)
Veo / Flow, Omni, Sora (fermé), Runway, Luma, Hailuo, Wan, LTX, Seedance, Pika, Midjourney (pas de vidéo V2), Firefly / Topaz (rien avant MAX), Meta Muse Video (toujours non disponible), ElevenLabs, Suno, Udio, Higgsfield (modèles).

### Ce que ça change pour le monteur / motion designer
- **Rien à changer dans les devis** : mêmes recommandations que la session 20 ; Kling 4.0 reste une promesse.
- **Music v2 / v2.5, régénérer un passage** : utile pour **caler une musique sur le montage** (refaire seulement les 8 mesures qui tombent mal sur une coupe) au lieu de régénérer tout le morceau. Cliché à éviter : la musique « générique bande-annonce » qui monte à chaque plan ; garder des respirations.
- **Stable Audio 3.0, poids ouverts** : seule piste musique **en local** (pas de crédits, pas d'envoi de rushes). Mais relire la licence avant toute diffusion commerciale ; le label « entraîné sous licence » ne vaut pas licence d'usage.

---

## Mise à jour du 2026-10-10 (session 22)

Fenêtre : 03/10 → 10/10/2026, quatrième passage du jour. WebSearch standard, WebFetch des changelogs Higgsfield, Runway et des notes de version Suno. Rien testé. Sources : `sources/ia-generative-2026-10-10.md`, section « Veille session 22 ».

**Bilan : aucun nouveau modèle vidéo, image, upscale ou voix.** Seule nouveauté vérifiée : côté **Suno**, deux entrées absentes des sessions précédentes.

| Date | Fait | Statut |
|---|---|---|
| 08/10/2026 | **Suno Studio** : détection des temps forts plus précise, étirement de clip (shift-clic), fondus à courbe, fenêtres détachables. | [SOURCÉ] off. suno.com/release-notes. |
| 01/10/2026 | **Suno Speech (bêta)** : voix parlée et musique générées ensemble, sur une seule piste (texte, puis choix de la voix et du style). Ouvert à tous, web et mobile. Suno reconnaît des accents qui dérivent et des pauses trop dramatiques. Formules concernées, droits commerciaux, durée : non précisés. | [SOURCÉ] off. suno.com/blog/introducing-speech-beta ; sec. letsdatascience (02/10). |
| 10/10/2026 | Kling 4.0 complet : toujours pas sorti. Higgsfield : dernière entrée le 08/10. Runway : dernière entrée le 02/10. | [SOURCÉ] off. changelogs Higgsfield et Runway (consultés le 10/10 au soir). |

**Non retenu** : « Seedance 2.5 pourrait sortir cette semaine » (agrégateur sans date, et le modèle est déjà sorti) ; « ElevenLabs v3 le 14/10 » (date future, source peu fiable).
**Rien de neuf** : Veo / Flow, Omni, Luma, Hailuo, Wan, Moonvalley, Midjourney, Firefly, Topaz, ElevenLabs.

### Ce que ça change pour le monteur / motion designer
- **Suno Speech** : la voix et la musique sortent mélangées sur une seule piste, donc **impossible de baisser la musique sous la voix**, de couper une respiration ou de recaler une phrase au montage. Bon pour une maquette, pas pour un master. Pour un livrable, garder voix (TTS) et musique sur des pistes séparées.
- **Suno Studio, fondus et temps forts** : utile pour caler une musique Suno sur les coupes, mais le mixage final reste dans Premiere ou Resolve. Même règle de droits qu'avant : pas de Suno en pub ou en TV sans clause écrite.
