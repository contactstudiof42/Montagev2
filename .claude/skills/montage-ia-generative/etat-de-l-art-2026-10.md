# État de l'art IA générative pour la post-production (2026-10)

Annexe de `SKILL.md` : faits outils datés et sources derrière le tableau du § 5 (le SKILL.md fait foi ; sur les faits outils, cette annexe prime sur le journal des veilles).

**État unique au 2026-10-10** : il regroupe la recherche du 2026-10-10 et les sept passages de veille du même jour (sessions 19 à 25). Le journal de ces veilles, et la liste de ce qui était faux dans la version du 2026-10-09, sont archivés dans `archives/audit-2/skills/montage-ia-generative/veilles-2026-10.md` (ne fait pas foi). Recherche web (WebSearch + WebFetch). **Rien n'a été testé ici**, sauf mention [LABO]. Ce marché bouge chaque mois : toute ligne de plus de 3 mois est à revérifier avant un devis.

Légende de chaque ligne :
- **[SOURCÉ]** : URL + date de publication de la source. « off. » = page de l'éditeur ; « sec. » = presse, blog, revendeur.
- **[À VÉRIFIER]** : source unique, contradiction ou vendeur juge et partie.
- **Inconnu** : aucune source trouvée. Aucun numéro de version n'est deviné.

Liens consultés : `/home/user/Montagev2/sources/ia-generative-2026-10-10.md`. Version précédente des sources : `sources/ia-generative-2026-10.md` et `sources/ia-verif-2026-10-10.md`.

---

## 0. Quel outil pour quel besoin (regard de DA)

| Besoin | Premier choix (oct. 2026) | Alternative | Quand NE PAS l'utiliser |
|---|---|---|---|
| **Plan impossible** (échelle, rêve, intérieur du corps) | Veo 3.1 (Flow) ou Kling 3.0 pour le réalisme (Kling 4.0 complet non sorti au 10/10) ; Seedance 2.5 si plan long (30 s) | Luma Ray3.2 si l'étalonneur veut du HDR / EXR 16 bits | Quand le plan doit porter le jeu d'un acteur. Quand un insert tourné coûte moins que le tri (Trillo : 55 clips gardés sur 700). Quand le film promet du réel (doc, témoignage, produit). |
| **Raccord manquant** (plan de coupe, contrechamp absent) | Image vers vidéo depuis la dernière image réelle (Veo « Frames to Video », Kling, Seedance) | Runway Aleph 2.0 (vidéo vers vidéo, nouvel angle) | Si le raccord porte un regard ou une émotion : l'IA ne joue pas. Si le plan voisin est en 10 bits log et qu'on ne peut pas réunir les textures. |
| **Extension de plan** (+2 s) | Premiere Generative Extend (2 s vidéo, 10 s audio) | Veo « Scene extension » ; image vers vidéo + fondu | Sur un plan HDR, 10 bits ou 50p livré tel quel : les frames générées sortiraient en 8 bits SDR, 30 i/s au plus (FAQ Adobe et blog vendeur) [À VÉRIFIER DANS LE LOGICIEL]. Sur un visage en gros plan qui parle. |
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
- OpenAI n'a plus de modèle vidéo public ; aucun nouveau modèle image, vidéo ou audio à son DevDay (29/09/2026). Ses agents **Dots** permettent de commander des plans à Runway (01/10) et Higgsfield (29/09) depuis ChatGPT. [SOURCÉ] off. changelogs Runway et Higgsfield.
- Dernières entrées vérifiées le 10/10 au soir : Runway 02/10, Higgsfield 08/10, ElevenLabs 05/10 (agents seulement), Gemini API 08/10 (rien sur Veo, Omni, Lyria). Aucun nouveau modèle vidéo, voix ou musique entre le 03 et le 10/10, sauf Vidu Q4 Preview (07/10).

### Google Veo et Gemini Omni
| Fait | Statut |
|---|---|
| Veo 3.1 reste la dernière version. Déclinaisons Fast et Lite. **Pas de Veo 4 officiel** au 2026-10-10. | [SOURCÉ] off. deepmind.google/models/veo (consulté 2026-10-10) ; sec. evolink.ai (avril 2026), aireiter.com (août 2026). Un article MSN annonce un « Veo 4 » : [À VÉRIFIER], contredit par tout le reste. |
| Veo 3.1 : 1080p et 4K, audio natif, « Ingredients to video » (références de personnage, d'objet, de style), extension de scène, première et dernière image, **insertion et retrait d'objet**, contrôle caméra. | [SOURCÉ] off. deepmind.google/models/veo (consulté 2026-10-10). Date de livraison du retrait d'objet : inconnue. |
| Clip de base : 8 s, extensible. 9:16 natif depuis janvier 2026. | [SOURCÉ] off. deepmind.google ; sec. 9to5google (janv. 2026). |
| Prix API Gemini (avec audio) : Veo 3.1 = 0,40 $/s en 1080p, 0,60 $/s en 4K ; Fast = 0,12 $/s en 1080p ; Lite = 0,08 $/s en 1080p (pas de 4K). | [SOURCÉ] off. ai.google.dev/gemini-api/docs/pricing (consulté 2026-10-10). |
| **Gemini Omni Flash** : annoncé à l'I/O le 19/05/2026. Texte, image, vidéo et audio en entrée. Montage conversationnel. Clips de 3 à 10 s en 720p, audio natif. API en preview le 30/06/2026. Environ 0,10 $/s. | [SOURCÉ] off. ai.google.dev/gemini-api/docs/pricing (prix) ; sec. invideo.io, buildfastwithai (2026). Durée et résolution : [À VÉRIFIER] (sources secondaires). |
| Gemini Omni **1.1 Flash** (`gemini-omni-1.1-flash`) : version **GA** du 27/08/2026 ; l'ancien point d'accès `gemini-omni-flash-preview` est déprécié depuis le 30/09/2026.  | [SOURCÉ] off. ai.google.dev/gemini-api/docs/changelog (27/08/2026) ; off. changelog Higgsfield (28/08/2026). |

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
| Kling 4.0 annoncé en 4K, **HDR 10 bits**, audio stéréo, lip-sync amélioré, 3-30 s, 21:9 à 9:16. Flash : 20 s, 720p selon un comparatif. Prix 4.0 non publié. API : pas encore. | [À VÉRIFIER] annonce Kling sur X + blogs (atlascloud, mean.ceo, 05/10). |
| **Au 10/10/2026 au soir, Kling 4.0 complet n'est pas sorti** (seule la Flash, accès anticipé) ; absent des changelogs Higgsfield et Runway. **Ne pas le promettre dans un devis.** Kling AI prépare une IPO à Hong Kong (cotation visée 2027). | [SOURCÉ] off. changelogs Higgsfield, Runway (10/10) ; sec. Bloomberg via technode (08/10/2026). |
| Abonnement Ultra : environ 1 430 $/an. | [À VÉRIFIER] sec. aitoolanalysis, eesel.ai (2026). |

### Seedance (ByteDance)
| Fait | Statut |
|---|---|
| Seedance 2.0 : février 2026. Lettres de mise en demeure de Disney, Paramount et de la MPA (février 2026). ByteDance promet des garde-fous, sans détail. | [SOURCÉ] sec. axios.com (20/02/2026), au.variety.com (02/2026). |
| Seedance 1.5 Pro retiré des Flows ElevenLabs le **11/11/2026** : un plan généré avec ne pourra plus être regénéré à l'identique. | [SOURCÉ] off. elevenlabs.io/docs/changelog (23/09/2026). |
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
| Produits maison : Cinema Studio 4.0 (12/08), Relight et palette (20/08), Genjutsu (01/09), Genjutsu **Restyle** (re-dessine une vidéo en gardant le mouvement, 30/09), extension ChatGPT (30/09), Ads Studio (30/09), AI Influencer (02/10), Ad Multiplier (06/10), skill « Katana » pour Claude (08/10/2026). **API publique** le 16/09/2026 (50+ modèles, paiement à la génération). | [SOURCÉ] off. higgsfield.ai/creator-hub/changelog (consulté 2026-10-10). |
| Plugins After Effects / Premiere (21/07/2026), Blender (21/08/2026), serveur MCP. | [SOURCÉ] off. higgsfield.ai/blog/higgsfield-after-effects (21/07/2026) ; changelog. |
| Modèles tiers ajoutés : Seedance 2.5 (03/08), Wan 3.0 (24/08), Gemini Omni 1.1 Flash (28/08), MiniMax H3 Max (31/08), GPT Image 2.5 (22/09), Eleven v4 (28/09), FLUX 3 Image (01/10), Nano Banana 2.1 (06/10/2026). **Kling 4.0 absent** du changelog au 10/10. | [SOURCÉ] off. changelog Higgsfield. |
| **Higgsfield Global Film Festival** : films faits uniquement dans Cinema Studio ; vote du public 08-15/10, palmarès fin octobre 2026, 1 M$ de dotation. À regarder comme un catalogue des clichés « tout IA » de 2026, pas comme une preuve de fiabilité. | [SOURCÉ] off. changelog et blog Higgsfield (05 et 08/10/2026). |
| Outil de « similarity scoring » (ressemblance avec des œuvres protégées) pour les équipes, mars 2026. | [SOURCÉ] off. prnewswire (03/2026). |

### Pika, Moonvalley, Midjourney vidéo, autres
| Fait | Statut |
|---|---|
| **Pika** : se repositionne en plateforme multi-modèles (« Welcome to the New Pika », 17/09/2026) ; Pika Music, SFX, Speech, Soundtrack (18/08/2026). Modèle maison : 2.5 (date inconnue). | [À VÉRIFIER] off. pika.art (dates lues via recherche, page non ouverte). |
| **Moonvalley / Marey** : modèle entraîné sur données sous licence (sortie générale juillet 2025). **Aucune annonce 2026 trouvée.** Prix actuel : inconnu. | [SOURCÉ] sec. cined.com (07/2025). 2026 : inconnu. |
| **Midjourney vidéo** : toujours image vers vidéo (clips de 5 s, extensibles par 4 s jusqu'à 21 s). Pas de modèle vidéo V2 trouvé. | [À VÉRIFIER] sec. (2026). |
| **Grok Imagine 1.5** (xAI) : 1 à 15 s, 1080p, audio. « Grok Imagine 2 » et « 1.5 Lite » : annuaires seulement, non retenus. | [SOURCÉ] off. runway.com/changelog (13/08/2026). |
| **Vidu Q4 Preview** (ShengShu) : 07/10/2026. Image ou références vers vidéo (pas de texte seul), 3 à 16 s, 540p à **4K**, 10 bits annoncés, son par défaut, jusqu'à 15 images et 3 sons de référence. API `viduq4-preview`, environ 0,014 $/s (4K ≈ 0,39 $/s). Le son sort mélangé à l'image : le refaire au mixage. | [SOURCÉ] off. docs platform.vidu.com (10/10) ; sec. unite.ai (07/10). Classement Artificial Analysis : [À VÉRIFIER]. |
| **Meta Muse Video** (aperçu, avec son) : annoncé le 07/07/2026, **toujours non disponible** au 10/10, pas d'API. Muse Image : sorti. | [SOURCÉ] off. ai.meta.com/blog (07/2026). |
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
| **Nano Banana 2.1** (`gemini-nano-banana-2.1`) : **GA le 06/10/2026**. Nano Banana 2 (`gemini-3.1-flash-image`) déprécié, sans date d'arrêt officielle (le « 29/10 » des blogs : [À VÉRIFIER]). Jusqu'en 4K, 14 images de référence, meilleur rendu du texte, meilleure cohérence de personnage, **formats extrêmes 1:4, 4:1, 1:8, 8:1** (plaques panoramiques pour un travelling ou un parallaxe dans AE ; vérifier la définition au zoom 100 %). Prix API : 0,034 $ (1K) à 0,113 $ (4K) par image. | [SOURCÉ] off. ai.google.dev (modèle et prix, consulté 2026-10-10) ; sec. seroundtable (10/2026). |
| **GPT Image 2** (ChatGPT Images 2.0) : 21/04/2026, raisonnement avant génération, 2K. | [SOURCÉ] sec. thenewstack, neurohive (04/2026). |
| **GPT Image 2.5** (ChatGPT Images 2.5) : 08/09/2026. Deux variantes API : Flare (défaut) et Sunburst (précis). Jusqu'à 50 % plus rapide. | [SOURCÉ] sec. axios.com (08/09/2026). Résolution 3840×2160 et 16 références : [À VÉRIFIER]. |
| **FLUX 3** (Black Forest Labs) : 23/07/2026. Modèle multimodal (image, vidéo jusqu'à 20 s avec son). Vidéo par API en août ; **FLUX 3 Image le 01/10/2026** : un seul point d'API pour générer, retoucher et composer, **boîtes de placement** en JSON (où va le produit, où va le titre), retouches locales, 10 références, 768 px à 4K, 0,048 $ à 0,607 $ l'image. Poids ouverts « Dev » promis, pas encore sortis. | [SOURCÉ] off. docs.bfl.ai/release-notes (01/10/2026) ; sec. marktechpost (26/07/2026). |
| **Tencent HY Image 3.5 Preview** : 22/09/2026, retouche conversationnelle, 20 références, 2K (4K non confirmé), ≈ 0,024 $ l'image, pas de poids. N'apporte rien que FLUX 3 ou Nano Banana 2.1 ne fassent. | [SOURCÉ] sec. comfyui-wiki (22/09), openrouter (05/10/2026). |
| **Seedream 5.0** (ByteDance) : 10/02/2026 ; Pro en juin-juillet 2026. Jusqu'à 14 références. | [SOURCÉ] sec. newsquawk (13/02/2026) ; off. runway.com/changelog (15/07/2026). |
| **Ideogram 4.0** : 03/06/2026, 2K natif, mise en page par boîtes. Poids non commerciaux. **Ideogram 4.5** : listé chez Higgsfield (30/09) et Runway (02/10/2026). Détails 4.5 : inconnus. | [SOURCÉ] sec. en.wikipedia.org/wiki/Ideogram (4.0) ; off. runway.com/changelog (4.5). |

---

## 3. Outils de post intégrés

### Adobe Premiere (le « Pro » a disparu en version 26)
| Fait | Statut |
|---|---|
| **Premiere 26.5 [NON CONFIRMÉ — À TRANCHER EN PHASE 3]** : une seule annonce lue (page communauté Adobe) et des notes de version en 403 ; d'autres pages du dépôt s'arrêtent à 26.2 / 26.3. Vérifier le numéro dans la version installée. Annonce du 10/09/2026 : **Generative Media Tool** (vidéo et effets sonores générés dans la timeline, « Firefly et modèles partenaires », images existantes comme référence) ; **Paper Edit** (premier montage depuis la transcription) ; Object Mask avec modes **Sharp** et **Smooth** (cheveux, tissu). | [SOURCÉ] off. community.adobe.com, « What's new in Adobe Premiere 26.5 » (10/09/2026). |
| **Generative Extend** : sources acceptées de 360p à 4K UHD, tous formats, entrelacé et pixels non carrés (annonce « 26.5 », numéro non confirmé). Notes de version : sources de 12 à 60 i/s, 8 à 16 bits, SDR ou HDR. | [SOURCÉ] off. community.adobe.com (10/09/2026) ; off. helpx.adobe.com release notes (extrait de recherche, page en 403). |
| Generative Extend : extension toujours de **2 s vidéo / 10 s audio**. Sortie générée en 8 bits SDR (la FAQ dit « si la séquence l'est », sans préciser le cas d'une séquence 10 bits ou HDR) ; au-delà de 30 i/s, extension à 30 i/s. | **[À VÉRIFIER DANS LE LOGICIEL]** FAQ Adobe (extrait de recherche) et atlascloud (blog vendeur). |
| Generative Media Tool : choix de modèle nommé (Firefly, Veo, Kling, Runway, Luma) ; **Generate Music** et **Generate Soundscape** (analyse jusqu'à 15 s d'image) en bêta. | [SOURCÉ] off. blog.adobe.com (08/09/2026) ; sec. postmagazine. |
| Color Mode (bêta) annoncé à la NAB, 15/04/2026. | [SOURCÉ] off. blog.adobe.com (15/04/2026). |

### After Effects
| Fait | Statut |
|---|---|
| **Object Matte** : quatre outils (Object Selection, Quick Selection, Selection Brush, Refine Edge). Même IA que l'Object Mask de Premiere. **Roto Brush est renommé Quick Selection**, il n'est pas supprimé. | [SOURCÉ] off. community.adobe.com, « New in Beta: Object Matte » (19/02/2026). |
| Sortie en version finale avec AE 26.2 (15/04/2026). | [À VÉRIFIER] sec. creativeainews (2026). |
| Retours de bêta : rendu lent, crénelage, propagation qui casse en cours de plan. | [SOURCÉ] off. même fil (réponses jusqu'au 13/05/2026). |
| **AI Assistant d'After Effects** en bêta publique : écrit le JavaScript des expressions et monte un rig à curseurs. | [SOURCÉ] off. blog.adobe.com (08/09/2026). |

### DaVinci Resolve
| Fait | Statut |
|---|---|
| Resolve 21.0 final le 02/06/2026 : page Photo, IntelliSearch, CineFocus, Speech Generator, Face Age / Reshaper, UltraSharpen. | [SOURCÉ] sec. newsshooter (02/06/2026). |
| **Resolve 21.1** : 08/09/2026 (IBC). Nouveauté IA officielle : **assistants externes** (Claude, Claude Code, ChatGPT Codex) qui analysent le projet, rangent les médias, règlent et lancent les rendus ; préférence de décodage pour les outils IA. | [SOURCÉ] off. blackmagicdesign.com/media/partial/release/20260908-03 (08/09/2026). |
| Pilotage par **serveur MCP natif**, réservé à Studio (passe par l'API de script). | [SOURCÉ] sec. ymcinema (09/09/2026), notebookcheck. |
| « IntelliTrack, Magic Mask 2.0 en 21.1 » : **à écarter**. Une seule source (sportsvideo.org, 09/09/2026) ; absents du communiqué officiel. La nouveauté IA de 21.1 est le pilotage par assistants externes (MCP). Magic Mask existe depuis les versions antérieures. | Corrigé le 2026-10-10. |
| Studio : licence perpétuelle 295 $. | [SOURCÉ] sec. kompozy (2026). |

### Topaz Labs
| Fait | Statut |
|---|---|
| **Starlight Precise 2.5** : 31/03/2026, pour amener des rushes IA en 4K. Disponible en local le 28/04/2026. | [SOURCÉ] off. topazlabs.com/news (03/2026 et 04/2026). |
| **Astra 2** (upscale cloud) : 28/04/2026. **Hyperion 2** (conversion SDR vers HDR) et **panneau Topaz pour Premiere** : 07/05/2026. NeuroStream (jusqu'à −95 % de VRAM). | [SOURCÉ] off. topazlabs.com/news, prnewswire (28/04 et 07/05/2026). |
| **Topaz appartient à Adobe** : accord le 25/06/2026, rachat finalisé le **23/09/2026**. Topaz reste une marque et des applis autonomes ; intégration prévue dans Firefly et Photoshop d'abord, puis vidéo (upscale, restauration d'archives, basse lumière). Aucune nouvelle version de modèle Topaz trouvée de juillet à octobre 2026. | [SOURCÉ] off. blog.adobe.com (23/09/2026) ; sec. petapixel (23/09/2026), newsshooter (25/06/2026). |
| Interpolation : Apollo (ralenti), Chronos (changement de cadence, ex. 24 vers 60), Aion (jusqu'à 16×). Accessible depuis Resolve. | [SOURCÉ] off. developer.topazlabs.com/video-models/frame-interpolation (consulté via recherche). |

### Détourage IA hors suites
| Fait | Statut |
|---|---|
| **SAM 3** (19/11/2025) puis **SAM 3.1** (27/03/2026, « Object Multiplex », environ 7× plus rapide à 128 objets). API Meta hébergée annoncée le 18/09/2026. Pas de « SAM 3.5 ». | [SOURCÉ] sec. learnopencv.com (2026), arxiv 2511.16719. API Meta : [À VÉRIFIER]. |
| Runway : SAM3 Video Segmentation, export WebM transparent (28/07/2026). | [SOURCÉ] off. runway.com/changelog. |
| Plugins SAM pour AE ou Nuke | [À VÉRIFIER] seul un site peu fiable l'affirme. |

### Interpolation
- Labo maison [LABO] : résultat dans `SKILL.md` § 6, mesures dans `montage-workflows` (`details.md`).
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
| **Udio** : accords UMG (29/10/2025) et Warner (19/11/2025). **Sony poursuit** (2e plainte le 20/07/2026). Téléchargements coupés depuis le 29/10/2025, toujours coupés fin septembre 2026. Plateforme sous licence promise en 2026, pas de date. | [SOURCÉ] sec. billboard (10/2025), chatgptiseatingtheworld (19/11/2025), aitools-directory (2026). |
| **Eleven Music v2** (27/05/2026) : composition par sections, **régénération d'un passage** (refaire 8 mesures qui tombent mal sur une coupe) ; v2.5 dans l'API le 14/09/2026. | [SOURCÉ] sec. decrypt.co ; off. elevenlabs.io/docs/changelog. |
| **Suno Speech** (bêta, 01/10/2026) : voix parlée et musique générées **sur une seule piste**, donc impossible de baisser la musique sous la voix : maquette seulement. **Suno Studio** (08/10/2026) : détection des temps forts, étirement de clip, fondus. | [SOURCÉ] off. suno.com/blog, suno.com/release-notes. |
| Suno : plainte UMG/Sony modifiée le 25/08/2026 pour ajouter le « stream ripping » (entraînement sur des téléchargements YouTube). | [SOURCÉ] sec. musicbusinessworldwide (08/2026). |
| **Stable Audio 3.0** (Stability AI, 05/2026) : jusqu'à ~6 min, **poids ouverts** Small et Medium (seule piste musique en local), Large en API ; présenté comme entraîné sous licence. CGU non lues. | [SOURCÉ] sec. decrypt.co (27/05/2026). Licence : [À VÉRIFIER]. |
| **Lyria 3.5** (musique Google) GA le 03/09/2026 ; TTS Gemini 3.8 Flash GA le 22/09/2026. CGU commerciales non lues. | [SOURCÉ] off. ai.google.dev changelog. |
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

## 6. Mise à jour du 2026-10-23 : modèles sortis et workflows de court métrage

Recherche web + catalogue Higgsfield lu par le MCP (`models_explore`, lecture seule) + catalogue Oxen lu dans le navigateur. Rien généré.

### Ce qui a bougé depuis le 10/10
| Fait | Statut |
|---|---|
| **Kling 4.0 sorti** pour tous le 15/10/2026 (communiqué du 16/10) : 3-30 s, 720p à 4K, jusqu'à 15 références (10 images, 5 vidéos ≤ 30 s cumulées, voix, 7 « elements »), 10 images clés, montage d'une vidéo existante (expression, caméra, décor, style). **HDR 10 bits et 4K en 21:9 « bientôt »** ; API en accès anticipé, sans prix. Chez Higgsfield le 21/10 (modes texte, image, références, `video-edit` ; 720p/1080p seulement dans le catalogue). | [SOURCÉ] sec. globenewswire (16/10), orcarouter (22/10) ; off. changelog Higgsfield (21/10) ; catalogue MCP (23/10). |
| **Seedance 2.5 4K** annoncé le 23/10/2026 (Volcano Engine) : 4K, 10 bits, mode brouillon 480p ; réservé à des entreprises en essai. | [SOURCÉ] sec. technode (23/10/2026). Ne pas le promettre. |
| Seedance 2.5 chez Higgsfield : modes `t2v`, `omni_reference` (image, vidéo, son), `video_edit`, `video_extension` ; 4-30 s ; 480p-1080p ; **`draft` 480p puis `draft_job_id` pour finaliser la même prise en 1080p sous 7 jours**. Cinema Studio 4.0 expose exactement les mêmes paramètres, plus caméra, objectif, ouverture, époque, rythme, lumière et palette. | [SOURCÉ] catalogue MCP Higgsfield (23/10). « Cinema Studio 4.0 = Seedance 2.5 habillé » : [NON VÉRIFIÉ], déduit des paramètres identiques. |
| **Genjutsu** (Higgsfield) : transfert de mouvement (`hf_mult_motion_control`) et remplacement d'objet (`hf_mult_replace_object`) ; vidéo de 4 à 30 s + jusqu'à 30 images de référence ; sortie ≤ 1080p ; 15 s = 40 crédits en 480p, 104 en 720p, 144 en 1080p (≈ 7,20 $). **Genjutsu Lite** (19/10) : moins cher, ≤ 15 s, sur Wan 3.0. **Genjutsu Styles** : redessine chaque image d'une vidéo dans un look, mouvement et cadrage gardés. | [SOURCÉ] off. higgsfield.ai/blog/higgsfield-genjutsu (31/08, prix « vérifiés en septembre ») ; changelog (19/10) ; catalogue MCP. |
| Higgsfield : **Draw To Video** (une vidéo + références), **3D Angles** (19/10), **3D Jutsu** (scène Blender hébergée, `bpy` 5.2, rendu → Seedance 2.5 en image de départ). Compte connecté au MCP : **0 crédit, plan gratuit** (23/10). | [SOURCÉ] catalogue et instructions MCP (23/10). |
| **Oxen.ai** (compte de Diego, 46 $ au 23/10) : Seedance 2.5 réf. vers vidéo **0,12 $/s en 480p, 0,26 $/s en 720p, 0,65 $/s en 1080p, 1,34 $/s en 4K** (le prix du catalogue est celui du 480p ; 1080p et 4K en 10 bits H.265 ; jusqu'à 30 images, 10 vidéos et 10 sons de référence ; 4-30 s ; brouillon 480p finalisable en 1080p sous 7 jours ; pas de graine ni d'image de départ documentées), image ou texte vers vidéo 0,11 $/s (480p) ; Gemini Omni 1.1 Flash 0,04 $/s ; Wan 3.0 0,06 $/s ; MiniMax H3 Max 0,06-0,09 $/s ; Luma Ray 3.2 vidéo vers vidéo 0,10 $/s ; Kling O3 Omni 0,11 $/s ; Kling 3.0 Motion Control 0,17 $/s ; LTX 2.5 0,17 $/s ; Depth Anything Video 0,05 $/s ; LTX-2.3 IC-LoRA Union Control (profondeur, contours, pose) affiché 0,0028 $/s ; FLUX 3 Image 0,06 $ ; Topaz Starlight Precise 2.6 dès 0,10 $/s. **Ni Kling 4.0 ni Genjutsu.** | [SOURCÉ] off. oxen.ai/ai/models (lu le 23/10). Le 0,0028 $/s : [À VÉRIFIER] (unité douteuse). |
| Runway (03-23/10) : rien de neuf en génération vidéo (SFX, voix, détourage, plafonds de crédits). | [SOURCÉ] off. runway.com/changelog. |

### Les familles de workflows d'un court métrage IA (oct. 2026) [THÉORIQUE sauf mention]
1. **Images clés puis image vers vidéo** : bible de look en images fixes (Nano Banana 2.1, FLUX 3, Seedream 5, Midjourney), puis première et dernière image vers vidéo (Kling 4.0, Seedance 2.5, Veo 3.1). Le plus rapide ; caméra approximative, cohérence fragile d'un plan à l'autre.
2. **Brouillon bon marché, rendu cher** : deux variantes. (a) Même modèle : brouillon 480p de Seedance 2.5 puis finalisation de la même prise en 1080p (paramètre documenté, voir plus haut). (b) Modèle bon marché (Omni Flash, Wan 3.0) pour l'animatique, puis le brouillon sert de référence vidéo au modèle cher : le mouvement passe à peu près, le look change.
3. **Prévisualisation Blender vers vidéo** : décor en volumes gris et caméra animée dans Blender, rendu passé en référence vidéo (Seedance 2.5 `omni_reference`, Kling 4.0) avec une image de départ pour le look ; variante libre : passe de profondeur vers LTX IC-LoRA. Sources : billets de créateurs et de vendeurs (dev.to, invideo, X) ; « suit la caméra image par image » n'est mesuré nulle part.
4. **Prise de vue « croquis » vers vidéo à vidéo** (performance filmée, monde remplacé) : Genjutsu, Kling 4.0 `video-edit`, Seedance 2.5 `video_edit`, Luma Ray 3.2, Runway Aleph 2.0. [VU SUR IMAGES] juice.ext (réalisateur IA, Amsterdam, partenaire Higgsfield), reel « Drivers License » (16/10/2026) : trois bandes superposées, rush tourné dans un salon (acteurs assis sur un canapé, lampe, plantes), sortie Genjutsu (même jeu, même cadrage, devenus une voiture dans la campagne irlandaise, puis un bar vu dans un rétroviseur), puis « final : colour & grain » (contraste et densité plus forts, grain, sous-titres). Le jeu, les regards et le rythme viennent du rush. Un commentateur relève que la scène du rétroviseur est inversée. tseily (partenaire Higgsfield, 22/10) : elle se filme chez elle, crée le décor (un wagon de train de luxe) en image fixe avec Seedream 5 Pro, puis Genjutsu Motion Transfer (rush + planche du personnage + image du décor).
5. **Vrai tournage + décor IA** (VFX classique) : acteur filmé proprement (log, 10 bits, lumière de couleur réelle), décor généré en plaques, compositing ; Beeble SwitchLight 3 pour relighter. La plus chère en travail, la seule dont le visage reste une vraie image.
6. **En local** : sur le Mac du studio (M1 Max, 32 Go), les modèles ouverts récents (LTX 2.5 : 22 Md de paramètres + encodeur 12 Md) sont hors de portée [THÉORIQUE, déduit des tailles] ; passer par Oxen ou une API.

Sources : globenewswire.com (16/10), orcarouter.ai/blog/kling-4-0-general-availability, technode.com (23/10), higgsfield.ai/blog/higgsfield-genjutsu, higgsfield.ai/creator-hub/changelog, runway.com/changelog, oxen.ai/ai/models, dev.to/glglgl (Blender vers Seedance 2.5, billet promotionnel), docs.ltx.io (Union Control IC-LoRA), cgchannel (SwitchLight 3.0, 11/2025), instagram.com/juice.ext et instagram.com/p/DezKr6EoKSc (vus le 23/10).

---

## 7. Ce que cette recherche n'a pas couvert

- Le texte EUR-Lex des lignes directrices C(2026) 5054 (lu via cabinets d'avocats seulement).
- Les CGU commerciales en vigueur de Suno v6, Eleven Music, Kling 4.0, Seedance 2.5.
- Les annonces d'Adobe MAX (10-12 novembre 2026), à reprendre après l'événement.
- La sortie complète de Kling 4.0 (« octobre », sans jour ; non sortie au 10/10 au soir), à constater.
- Le numéro de version réel de Premiere (26.5 non confirmé) dans le logiciel installé.
- Les règlements officiels de Cannes, des César et des Oscars (non relus en source primaire).

---
