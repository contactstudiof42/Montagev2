# État de l'art IA générative pour la post-production (annexe datée)

Établi le **2026-10-09** par recherche web (WebSearch). **Rien n'a été testé.** Légende :
- **[OFFICIEL]** : page de l'éditeur ou communiqué.
- **[SECONDAIRE]** : presse spécialisée, blog, agrégateur.
- **[INCERTAIN]** : source unique, contradiction entre sources, ou vendeur juge et partie.
- **[NON TROUVÉ]** : pas de source 2025-2026 dans cette recherche.

Liste complète des URL : `/home/user/Montagev2/sources/ia-generative-2026-10.md`.

## 1. Vidéo générative

### Tendance générale (juillet 2026)
Plusieurs comparatifs de 2026 placent **Veo 3.1** et **Kling 3.0** en tête (audio natif, sortie 4K), avec **Seedance 2.0** pour l'image vers vidéo et **Runway Gen-4.5** comme modèle phare de Runway. Sora n'en fait plus partie. [SECONDAIRE] provimedia.de, flowhunt.io, dupple.com. Les classements varient selon les testeurs.

### Google Veo 3.1 / Flow
- Au lancement (oct. 2025), Flow ajoute le son généré dans « Ingredients to Video », « Frames to Video » et « Scene Extension ». La fonction « Insert » ajoute un élément en ajustant ombres et lumière. Le « Remove » a été annoncé « bientôt », **livraison non confirmée**. [SECONDAIRE] yourstory, chromeunboxed.
- Mise à jour de **janvier 2026** : « Ingredients to Video » amélioré, 9:16 natif, upscaling 1080p/4K (Flow, Gemini API, Vertex AI). [SECONDAIRE] 9to5google, androidauthority.
- Runway propose aussi Veo 3 et 3.1 sur sa plateforme. [SECONDAIRE] laozhang.

### OpenAI Sora 2 : arrêté
- Appli et web **arrêtés le 26 avril 2026** ; API annoncée pour l'arrêt le **24 septembre 2026** ; données supprimées après la fenêtre d'export. [OFFICIEL] help.openai.com/en/articles/20001152.
- Les développeurs ont été prévenus le 24/03/2026, et les alias sora-2 et sora-2-pro ont été retirés le 24/09/2026. [SECONDAIRE] techjacksolutions. **Retrait effectif non vérifié sur une page officielle postérieure.**
- Aucun successeur annoncé. Conséquence métier : un rush généré peut devenir introuvable et non régénérable, d'où l'obligation d'archiver.

### Runway
- **Gen-4.5** annoncé le **1er décembre 2025**. Une revue de juillet 2026 indique que la page Gen-4.5 de Runway liste elle-même des limites en raisonnement causal, en permanence des objets et en « biais de réussite de l'action ». [SECONDAIRE] CometAPI, similarlabs.
- **Aleph** (gen4_aleph, API listée le 19/03/2026) : vidéo vers vidéo pour ajouter, retirer ou remplacer un objet, ré-éclairer, générer un nouvel angle ou un « plan suivant ». [SECONDAIRE] CometAPI.
- **Aleph 2.0** (juin 2026) : guidage par une image et cohérence multi-plans. [INCERTAIN] catalogue Runware seul, aucune annonce officielle trouvée.
- Partenariat pluriannuel Adobe × Runway. [SECONDAIRE] Digital Production, janv. 2026.

### Kling 3.0 (Kuaishou)
- Annonce les **4-6 février 2026** (Video 3.0, Video 3.0 Omni, Image 3.0, Image 3.0 Omni), d'abord réservée aux abonnés Ultra. [OFFICIEL] communiqué via Bernama.
- Jusqu'à 15 s, audio natif multilingue ; 4K/HDR selon une source secondaire (cinevva, déploiement mondial le 25/03/2026).
- Points forts cités : contrôle de type storyboard, multi-plans, dialogue. Points faibles : lenteur et coût difficile à prévoir. Environ 0,10 $/s selon un comparatif. [SECONDAIRE] notegpt, techsy.

### Seedance 2.0 (ByteDance)
- Sorti en **février 2026**. Réalisme guidé par références, réputé fort en image vers vidéo. [SECONDAIRE / INCERTAIN] notegpt, et Dreamina (CapCut) qui est la plateforme de ByteDance, donc juge et partie.

### MiniMax Hailuo 2.3
- Présenté comme le choix de la vitesse pour du volume réseaux sociaux. [SECONDAIRE] muapi.ai. Aucune info 2026 sur une version suivante.

### Alibaba Wan 2.6 / HappyHorse-1.0
- Wan 2.6 est proposé dans Higgsfield. [SECONDAIRE] toolquestor. **Open source non confirmé pour 2.6.**
- HappyHorse-1.0 (Alibaba) apparaît dans les classements d'avril 2026. [INCERTAIN] frameo.ai seul.

### Luma
- **Ray3 Modify** : modifie une séquence existante (costume, traits du visage) en conservant le mouvement, le timing et le jeu. [SECONDAIRE] jang.com.pk.
- **Ray3.2** (juin 2026) : jusqu'à 16 images clés, transformations vidéo de 20 s en 1080p. [SECONDAIRE] veed.

### Higgsfield
- Studio qui agrège des modèles tiers (Seedance 2.0, Kling 3.0, Veo 3, Wan 2.6, Hailuo, Nano Banana ; Sora 2 encore listé, sans doute obsolète). [SECONDAIRE] toolquestor. Le choix porte donc sur le modèle, pas sur la plateforme.

## 2. Image

- **GPT Image 2** (OpenAI) : lancé en **avril 2026**, en tête de l'arène Artificial Analysis Text-to-Image (1339 Elo), 2K max. [SECONDAIRE] tech-insider.org/fr.
- **Nano Banana Pro** (= Gemini 3 Pro Image) : 4K max, réputé pour le texte et les mains. Disponibilité générale en « juin » selon une source. [INCERTAIN] confusion avec « Nano Banana 2 » selon les comparatifs.
- **Midjourney V8.1** : fin avril 2026 ; V7 reste par défaut pour la plupart des utilisateurs (juillet 2026) ; pas d'API officielle. [SECONDAIRE]
- **FLUX.2** (Black Forest Labs) : 32 Md de paramètres, poids téléchargeables, utile pour un pipeline local et confidentiel. [SECONDAIRE]
- **Imagen** : **[NON TROUVÉ]** pas de source 2026 spécifique ; Google semble mettre en avant Nano Banana.

## 3. Upscaling, restauration, interpolation

- **Topaz Astra 2** : lancé en **avril 2026**, upscaling par diffusion guidé par prompt, curseurs Creativity et Sharpness. [SECONDAIRE] invideo, photoworkout.
- **Starlight (Precise 2.5 ou 2.6)** : régénère la texture (peau, cheveux, tissu) pour réduire le « look plastique » des rushes IA. Environ 1,20 $ par 10 s jusqu'à 1080p via fal.ai. [INCERTAIN] numéro de version contradictoire.
- Topaz Video AI : fin de la licence perpétuelle en **octobre 2025**, environ 299 $/an. [SECONDAIRE] unifab.
- Attention, un upscaler par diffusion **invente** du détail. Sur un document, une archive ou un visage réel, c'est une altération à signaler.
- **Interpolation** (ralenti, conversion de cadence) : **[NON TROUVÉ]** aucune source 2025-2026 consultée. Ne rien affirmer sur l'état actuel de Topaz Apollo/Chronos ou de Resolve Speed Warp sans revérifier.

## 4. Détourage et roto

- **Adobe Premiere 26** (le « Pro » disparaît) : sortie le **20 janvier 2026**. Object Mask (survol, clic, masque et suivi), masques de forme jusqu'à 20× plus rapides selon Adobe, mode d'édition « Frame track ». Les tests le trouvent bon sur un sujet net, plus fragile sur une image bruitée ou peu contrastée. Certaines fonctions encore en bêta au lancement. [SECONDAIRE] PetaPixel, Digital Production, ProVideo Coalition ; [OFFICIEL] community.adobe.com (26.0).
- **DaVinci Resolve 21** : version finale le **2 juin 2026**. CineFocus (profondeur de champ synthétique par carte de profondeur IA), IntelliSearch (recherche de contenu en local), Magic Mask aussi sur la nouvelle page Photo. **21.1** à l'IBC le **9 septembre 2026** : IntelliTrack, Magic Mask 2.0 (meilleure détection des bords). [SECONDAIRE] Newsshooter, SVG, CineD. [INCERTAIN] la date d'arrivée d'IntelliTrack (déjà présent depuis la v19 selon une autre source). Outils IA surtout dans la version Studio ; 16 Go de RAM minimum (32 avec Fusion), GPU d'au moins 4 Go.
- **Meta SAM 3** : segmentation et suivi par texte ou par boîte, image et vidéo, téléchargeable, avec playground. [OFFICIEL] ai.meta.com/sam3. Aucune intégration Resolve ou After Effects confirmée.
- **After Effects Roto Brush** : **[NON TROUVÉ]** pas de source 2026 consultée.
- **CineFocus = fausse profondeur de champ** (cliché n° 7 du SKILL) : à doser.

## 5. Outils intégrés Adobe

- **Generative Extend** (Premiere, Firefly Video) : allonge la vidéo de 2 s max et l'audio de 10 s ; 12-30 i/s, 8 bits SDR ; frames générées étiquetées. [OFFICIEL] community.adobe.com (annonce, janv. 2026).
- **Firefly Boards** relié à Premiere 26 : planche collaborative avec des modèles Adobe, Google, OpenAI et Runway. [SECONDAIRE]
- Firefly Video présenté comme entraîné sur du contenu sous licence et du domaine public. [SECONDAIRE] TVBEurope (2024, à revérifier).
- **Aucune note de version officielle 2026 d'un nouveau modèle Firefly Video n'a été trouvée.**

## 6. Voix et musique

- **ElevenLabs Eleven v3** : disponibilité générale le **2 février 2026**. Balises audio (émotion), dialogue à plusieurs voix, plus de 70 langues, pas en temps réel. [SECONDAIRE] coval.ai.
- Clonage : consentement explicite, vérification technologique pour le clonage professionnel (phrase de consentement prononcée dans la voix clonée), voix de célébrités bloquées, classifieur de détection. [SECONDAIRE]
- **Eleven Music v2** (mai 2026, « entraîné uniquement sur des données sous licence ») : [INCERTAIN] affirmation d'un site tiers.
- **Suno** : accord avec Warner le **25 novembre 2025** (fin du procès, nouveaux modèles sous licence en 2026, retrait des anciens modèles, téléchargement réservé aux comptes payants, pas d'usage commercial en gratuit). [SECONDAIRE] Decrypt, MarketScreener. Discussions avec UMG et Sony **dans l'impasse** en avril 2026. [INCERTAIN] Opus, source unique.
- **Udio** : accord avec UMG (oct. 2025) puis Warner. Devient une plateforme fermée de remix sous licence : **pas de téléchargement, de streaming ni d'usage externe**. [SECONDAIRE] Decrypt. Donc inutilisable pour une bande-son livrée.

## 7. Cadre juridique

- **AI Act UE, article 50** : obligations de transparence applicables depuis le **2 août 2026** (étiquetage des deepfakes, information en cas d'interaction directe avec une IA). Le **Digital Omnibus** n'a pas reporté l'article 50. Il accorde seulement jusqu'au **2 décembre 2026** pour le marquage lisible par machine des systèmes génératifs déjà sur le marché. Il reporte en revanche les obligations « haut risque » (annexe III) au 2 décembre 2027. Lignes directrices de la Commission publiées le 20 juillet 2026. [SECONDAIRE] CSA Labs (29/07/2026), ictrecht.nl. **À confirmer sur EUR-Lex avant tout usage contractuel.**
- États-Unis : l'ELVIS Act (Tennessee) est cité à propos du clonage de voix. [INCERTAIN] non vérifié en source primaire.

## 8. Ce que cette recherche n'a pas couvert (à faire)

Interpolation, After Effects 2026, Imagen, le statut exact de Wan open source, Hailuo 03, une confirmation officielle de Runway Aleph 2.0, le texte EUR-Lex de l'article 50 et la position française (CNC, SACD, ARCOM) sur la mention IA.
