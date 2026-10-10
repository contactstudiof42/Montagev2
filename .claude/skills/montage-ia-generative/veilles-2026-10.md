# Journal des veilles IA générative (octobre 2026) — HISTORIQUE

Annexe de `SKILL.md` : **journal historique**, conservé tel quel pour retrouver quand et d'où vient une info ; **il ne fait pas foi** (le SKILL.md fait foi, puis `etat-de-l-art-2026-10.md` pour les faits outils).

Contenu : la liste de ce qui était faux dans la version du 2026-10-09, puis les sept passages de veille du 2026-10-10 (sessions 19 à 25), déplacés depuis `etat-de-l-art-2026-10.md` le même jour. Tout ce qui y est utile a été repris dans l'état de l'art. Chaque statut ci-dessous est celui **du moment du passage** ; quand un statut a changé depuis, une note *[État au 10/10 au soir : …]* le signale.

---

## Ce qui était faux ou périmé dans la version du 2026-10-09

1. **Generative Extend « 12-30 i/s, 8 bits SDR seulement »** : périmé. Les sources acceptées vont désormais de 12 à 60 i/s, 8 à 16 bits, SDR ou HDR, 360p à 4K. La **sortie** resterait en 8 bits SDR, 30 i/s au plus : **[À TRANCHER EN PHASE 2]**.
2. **« Midjourney V7 reste par défaut »** : faux. V8.2 est le défaut depuis le 24/07/2026.
3. **« Aleph 2.0 connu seulement par un catalogue tiers »** : faux. Officiel chez Runway le 21/05/2026.
4. **« Hailuo 2.3, pas de version suivante »** : périmé. Hailuo 3.0 / H3 le 31/07/2026.
5. **« Wan 2.6, open source non confirmé »** : périmé. Wan 3.0 le 24/08/2026, fermé. Poids ouverts jusqu'à 2.2 seulement.
6. **Kling 3.0 en tête** : périmé. Kling 4.0 annoncé le 28/09/2026 (30 s), en déploiement. *[État au 10/10 au soir : seule la Flash est ouverte, version complète non sortie ; ne pas la promettre.]*
7. **Seedance 2.0** : périmé. Seedance 2.5 (30 s, audio) disponible depuis août 2026.
8. **FLUX.2, GPT Image 2, Nano Banana Pro comme références** : périmés. FLUX 3 (23/07), GPT Image 2.5 (08/09), Nano Banana 2 et 2.1 (février et octobre 2026).
9. **Eleven v3 comme dernier modèle** : périmé. Eleven v4 le 28/09/2026.
10. **Suno « nouveaux modèles sous licence en 2026 »** : réalisé. Suno v6 le 09/09/2026, anciens modèles retirés. UMG et Sony ont **relancé** une plainte le 18/09/2026.
11. **Resolve 21.1 = IntelliTrack + Magic Mask 2.0** : non confirmé, à écarter (source unique). Le communiqué officiel ne parle que des assistants IA (Claude, ChatGPT Codex).
12. **« After Effects Roto Brush : non trouvé »** : corrigé. Object Matte ; Roto Brush devient Quick Selection.
13. **« Interpolation : non trouvé »** : corrigé (Topaz Apollo / Chronos / Aion, Runway Enhance Frame Rate) ; labo maison ajouté.
14. **Starlight « version 2.5 ou 2.6 »** : c'est **Precise 2.5** (officiel, 31/03/2026).
15. **Veo « retrait d'objet non confirmé »** : la page DeepMind liste désormais insertion **et retrait** d'objet.
16. **Luma Ray3.2 « sources secondaires seulement »** : confirmé par Luma (09/06/2026), avec HDR et EXR 16 bits.
17. **« Seule Sora n'est plus dans les classements »** : à compléter, OpenAI n'a **plus aucune** offre vidéo publique.


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
- **Premiere 26.5** *[numéro non confirmé, À TRANCHER EN PHASE 2]*, **Generative Media Tool** : le choix de modèle inclut nommément **Firefly, Veo, Kling, Runway, Luma** ; **Generate Music** et **Generate Soundscape** (analyse jusqu'à 15 s d'image) restent en bêta. **AI Assistant d'After Effects** en bêta publique (écrit le JavaScript et monte un rig à curseurs). [SOURCÉ] off. blog.adobe.com (08/09/2026) ; sec. postmagazine, provideocoalition (09/2026).
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

## Veille du 2026-10-10 (session 22)

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

---

## Veille du 2026-10-10 (session 23)

Fenêtre : 03/10 → 10/10/2026, cinquième passage du jour (WebSearch standard et étendu, WebFetch). Rien testé. Sources : `sources/ia-generative-2026-10-10.md`, « Session 23 ».

- **07/10/2026 : Vidu Q4 Preview** (ShengShu), absent des sessions précédentes. Image vers vidéo et **référence vers vidéo** seulement (pas de texte seul) ; 3 à 16 s ; de 540p à **4K**, 10 bits annoncés ; son généré par défaut ; jusqu'à **15 images et 3 sons de référence** (MP3 de 3 à 12 s). Web et API (`viduq4-preview`). Prix d'appel : 0,014 $/s ; 4K ≈ 0,39 $/s ; −30 % jusqu'au 30/11. [SOURCÉ] off. docs platform.vidu.com (consultées le 10/10) ; sec. unite.ai (07/10), alphasignal (08/10), chinatechnews (08/10). Classement Artificial Analysis image vers vidéo : 3e (Elo 1 179), selon alphasignal seulement ; à reconfirmer.
- **Non retenu** : « Grok Imagine Video 1.5 Lite » (1 à 15 s, jusqu'à 1080p) ; il n'apparaît que dans des annuaires, sans annonce xAI, et ceux-ci le datent tantôt du 01/10, tantôt du 08/10.
- **Rien de neuf vérifié** : Veo, Sora, Kling (4.0 complet toujours pas sorti ; Higgsfield sans entrée les 09 et 10/10), Runway, Luma (Ray3.2), Pika, Seedance, Hailuo (H3), Wan (poids : 2.2 max), LTX (2.5, 11/08), Midjourney, upscale et interpolation (Topaz, FLUX Video Upscale du 19/08), Resolve (21.1, 08/09), Premiere / AE, Blender, voix et musique (au-delà de Suno Speech / Studio).
- **Pour le monteur** : la référence audio de Vidu Q4 sert à imposer **une voix ou une ambiance** sur un plan généré ; mais le son sort « cuit » dans la vidéo, donc il faut un export séparé ou le refaire au mixage. Le 4K à 16 s maximum convient à des plans d'insert, pas à des plans-séquences. Pas de texte seul : il faut une image de départ, ce qui oblige à préparer une vraie DA image avant de générer (c'est plutôt une bonne contrainte).

## Veille du 2026-10-10 (session 24)

Fenêtre : 03/10 → 10/10/2026, sixième passage du jour (~19h35 UTC ; 7 WebSearch standard, 3 WebFetch). Rien testé. Sources : `sources/ia-generative-2026-10-10.md`, « Session 24 ».

- **Rien de neuf depuis la session 23.** Higgsfield : dernière entrée toujours le 08/10, ni Kling 4.0 complet ni Vidu Q4. Runway : dernière entrée le 02/10. ElevenLabs : dernière entrée le 05/10 (agents seulement). [SOURCÉ] off. changelogs Higgsfield, Runway, ElevenLabs (consultés le 10/10 vers 19h40 UTC).
- **Non retenu** : « Kling 4.0 arrive en octobre » (Atlas Cloud, fal.ai, gradually.ai : toujours sans jour ni annonce Kuaishou) ; « Seedance 2.5 pourrait sortir cette semaine » (you.com, non daté, modèle déjà sorti) ; récaps d'agrégateurs (af.net, frameo, segmind) qui recyclent des infos de mars à juillet.
- **Rien de neuf vérifié** : Veo / Flow (pas de Veo 4), Sora (fermé), Luma, Seedance, Hailuo, Wan, LTX, Vidu (au-delà de Q4 Preview), Midjourney (pas de vidéo V2), Topaz, Firefly / Premiere / AE (rien depuis l'annonce « Premiere 26.5 », numéro non confirmé, et IBC ; MAX le 10-12/11), Resolve (21.1), ElevenLabs, Suno (au-delà de Speech et Studio).
- **Pour le monteur** : rien à changer dans les devis ni dans le choix d'outils de la session 23. Ne pas planifier de plans de 30 s Kling 4.0 tant que le modèle n'est pas listé chez Kling ou Higgsfield.

## Veille du 2026-10-10 soir (session 25)

Fenêtre : 03/10 → 10/10/2026, septième passage du jour (6 WebSearch, 2 WebFetch). Rien testé.

- **Aucun nouveau modèle vidéo, voix, musique, upscale, interpolation ou détourage depuis la session 24.** Higgsfield : dernière entrée le 08/10 (Katana, vote du festival). Runway : dernière entrée le 02/10. Kling 4.0 complet : toujours « octobre », sans jour. [SOURCÉ] off. higgsfield.ai changelog et runway.com/changelog (consultés le 10/10 au soir) ; sec. atlascloud.ai/blog/tips/kling-4-flash-vs-full.
- **Rattrapage image : Tencent HY Image 3.5 Preview** (22/09/2026 ; listé sur OpenRouter le 05/10). Génération et retouche d'image, retouche conversationnelle sur plusieurs tours, jusqu'à 20 références ; 2K annoncé par Tencent (4K selon OpenRouter : (non confirmé)) ; environ 0,024 $ l'image ; **pas de poids publiés**, deux nœuds partenaires dans ComfyUI. Le « +30 % face à HY Image 3.0 » vient des tests internes de Tencent (non confirmé). [SOURCÉ] sec. comfyui-wiki.com/en/news/2026-09-22-tencent-hy-image-3-5-preview (22/09/2026) ; openrouter.ai/tencent/hy-image-v3.5-preview (05/10/2026) ; runtimewire.com (09/2026).
  - **Pour le monteur / motion designer** : une option de plus pour décliner des plaques ou des key visuals dans ComfyUI par retouches successives. Elle n'apporte rien que FLUX 3 ou Nano Banana 2.1 ne fassent déjà, et il n'y a pas de poids pour un usage en local. À tester seulement si le coût par image compte.
- **AI Act art. 50** : rien de neuf depuis l'avis de la Commission du 08/07/2026 sur le code de bonnes pratiques (obligations applicables depuis le 02/08/2026). *[Les lignes directrices finales C(2026) 5054 du 20/07/2026 sont postérieures à cet avis : voir l'état de l'art § 5.]* [SOURCÉ] off. digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content.
- **Non retenu** : « Grok Imagine Video 1.5 Lite le 08/10 » (llmgateway.io seulement, déjà écarté en session 23) ; « ElevenLabs v3 » (voxbooster, récap Q4 daté en partie dans le futur).
- **Rien de neuf vérifié** : Veo, Sora, Luma, Pika, Hailuo, Seedance, Wan, LTX, Vidu (au-delà de Q4 Preview), Midjourney, Firefly / Premiere / AE / Resolve / Blender, ElevenLabs, Suno, Udio.
