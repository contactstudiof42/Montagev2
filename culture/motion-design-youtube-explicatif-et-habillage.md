# Le motion design de YouTube : explicatifs animés, documentaires de cartes, captions et habillage de chaîne

- **Objet** : la grammaire du motion propre aux chaînes YouTube, et non à la pub, au générique ou au clip. Quatre familles :
  1. les explicatifs animés (Vox, Kurzgesagt et ses suiveurs, Polymatter, RealLifeLore) ;
  2. le documentaire de cartes en 3D (Johnny Harris, ancien de Vox) ;
  3. le motion « talking head » à captions (MrBeast, Ali Abdaal, Hormozi) ;
  4. l'habillage imposé ou encouragé par la plateforme.
- **Complète** `kurzgesagt-motion-design.md` (le cas d'école) et `kinetic-edit-monteurs-reseaux-sources.md` (SFX, rampes de vitesse) sans les répéter.
- **Qualité des sources (consultées le 2026-10-10)** : bonne pour les règles de la plateforme (aide YouTube) et pour Vox (entretien du DA). Moyenne pour les cartes (pages d'aescripts, d'un éditeur de plugin). **Faible pour les captions** : uniquement des vendeurs d'outils de sous-titrage. Rien de solide sur Polymatter, RealLifeLore ni sur l'équipe vidéo du Monde. Je n'ai pu regarder aucune vidéo : les descriptions faites à l'œil sont marquées **[à vérifier à l'image]**.

## Ce que ça cherche à faire ressentir / comprendre

- **Explicatif** : « j'ai compris un sujet compliqué en 10 minutes, et c'était agréable ». La sensation d'intelligence gagnée, sans effort apparent.
- **Documentaire de cartes** : se sentir **situé** (où, à quelle échelle, qui contrôle quoi) et embarqué dans une enquête. La caméra qui plonge du globe à la rue transforme la géopolitique en voyage.
- **Talking head à captions** : ne jamais décrocher. Le mot est vu en même temps qu'entendu, tout se passe dans la seconde, et la promesse du titre doit être tenue dès la première minute.
- **Habillage** : reconnaître la chaîne en une seconde et savoir où l'on est dans la vidéo (chapitres), sans jamais retarder le contenu.

## Les choix qui produisent l'effet

**Explicatifs animés (Vox)**
- Le DA de l'équipe vidéo de Vox, Joey Sendaydiego, entre dans l'histoire « le plus tôt possible dans l'écriture du script ». Il esquisse et expérimente directement dans After Effects. Il cherche un style propre à chaque vidéo : du **papier découpé** coloré qui attire « quel que soit l'âge », ou une horloge en papier qui devient un camembert pour comparer des heures de travail. Une équipe à part vérifie l'exactitude des cartes. La cadence est d'**1 à 2 vidéos par semaine**, et « deux à trois semaines au plus » pour une vidéo (Storybench, 2024).
- Motifs repérés par les tutoriels (sources secondaires) : texture de papier animée derrière les images, **animation à 12 i/s** pour un aspect saccadé et artisanal (PremiumBeat), surlignage de documents, polices et couleurs récurrentes.
- **La transformation plutôt que la coupe** : l'objet (l'horloge) devient la donnée (le graphique). Le spectateur suit **une seule chose** qui change de rôle.

**Documentaire de cartes**
- L'outil dominant est **GEOlayers 3**, un plugin After Effects (aescripts). Il donne accès aux frontières, routes, rivières et bâtiments extrudés tirés d'OpenStreetMap / MapTiler, à des styles générés à partir d'une palette, à l'import de CSV pour colorer les données et à du relief 3D. aescripts affirme que « la plupart des animations de cartes vues en ligne » viennent de ce plugin, et publie un article où Johnny Harris explique comment il l'utilise (page inaccessible lors de ma consultation).
- **Google Earth Studio** (annoncé en décembre 2018) : un outil web à keyframes sur l'imagerie 3D de Google Earth (position, focale, heure du soleil, nuages). Les données caméra s'exportent vers After Effects pour y accrocher étiquettes et tracés. L'usage est libre à condition de **créditer Google**.
- [à vérifier à l'image] La grammaire : un zoom continu du globe au lieu ; une frontière qui se dessine ; une zone qui se remplit de couleur ; une étiquette qui suit le point ; une texture de papier ou de carte ancienne pour éviter le look « GPS ».
- **Arte, *Le Dessous des cartes*** : avec la nouvelle formule de septembre 2017 (Émilie Aubry), le magazine reste construit sur cartes et chiffres mais ajoute des images satellites en haute définition, plus de **survols 3D** et une meilleure lecture du relief (La Libre, 2017). Le dispositif ne change pas : la présentatrice introduit sur fond neutre, puis les cartes s'animent sous sa voix.

**Captions et talking head**
- Le style « Hormozi », tel que le décrivent les outils qui l'imitent : capitales grasses, **2 lignes et 4 à 6 mots au plus**, le mot prononcé surligné (souvent en jaune), une coupe entre plan moyen et plan serré toutes les **1 à 3 s**. L'argument : une **double entrée**, lire et entendre en même temps. Un article de 2026 note la saturation et une variante plus sobre : on garde les captions mot à mot et les zooms, on retire emojis, flashs et SFX.
- MrBeast : son guide interne (36 pages, divulgué en 2024 et authentifié par deux anciens producteurs selon Passionfruit) fixe trois mesures (taux de clic, durée moyenne de visionnage, pourcentage vu) et fait du titre et de la miniature des éléments « critiques ». Des reprises secondaires y lisent l'importance de la **première minute**, puis des minutes 3 à 6. Le motion y est un outil de rétention, pas une signature.

**Habillage imposé par YouTube**
- **Écran de fin** : il occupe les **5 à 20 dernières secondes**. La vidéo doit durer **au moins 25 s**, et on peut placer jusqu'à **4 éléments** en 16:9. Il n'est pas affiché sur le web mobile ni dans les vidéos pour enfants. Le motion de fin se compose donc **autour de zones vides** que YouTube remplira.
- **Chapitres** : une liste dans la description commençant à 00:00, au moins **3 horodatages**, chacun d'au moins **10 s**. D'où les **cartons de chapitre** à l'image : un titre court, de 1 à 2 s, qui reprend le libellé de la description.
- **Lower thirds, rappel d'abonnement, logo** : courts, placés en périphérie, souvent tirés de **templates** (Envato Elements, Motion Array, MOGRT Premiere). Les abonnements à téléchargement illimité proposent des milliers de packs de titres, transitions et « YouTube packs ». D'où la **standardisation** : les mêmes boutons d'abonnement animés, les mêmes glitchs, les mêmes lower thirds se retrouvent sur des milliers de chaînes.
- **France** : *DataGueule* (Henri Poulain, Julien Goetz, Sylvain Lapoix ; France 4 puis franceinfo, depuis 2014) fait du **data-journalisme en pictogrammes et chiffres animés**. Ses vidéos durent 3 à 5 min jusqu'à la saison 4, puis 4 à 12 min. La voix est rapide et ironique. Chaque épisode se clôt sur une **mosaïque** d'images et de textes qui compose une seule image : le motif de la chaîne.

## Ce qui distingue le motion YouTube du motion de pub, de générique et de clip

- **Le volume et le délai** : 1 à 2 vidéos par semaine chez Vox, contre 4 mois pour un spot de Buck. Le style doit donc être **un système réutilisable** (bibliothèque de formes, rigs, templates de chaîne), pas une exécution unique.
- **La durée** : 8 à 20 min à tenir, et non 30 s. Le motion sert la **compréhension continue** et la relance de l'attention, pas un « effet » unique.
- **La voix est la colonne vertébrale** : l'image suit la parole (cf. Kurzgesagt). En clip, l'image suit la musique ; en pub, souvent le concept visuel.
- **La lisibilité multi-écrans** : un texte assez gros pour un téléphone, mais aussi pour une télévision, qui est depuis décembre 2024 **le premier écran de YouTube en durée de visionnage aux États-Unis** (Neal Mohan, 2025). Il faut aussi éviter les zones couvertes par l'interface (barre de lecture, écran de fin).
- **Le son activé** par défaut sur YouTube long format, contrairement au feed social : la musique et la voix peuvent porter le sens, et les captions y deviennent du **rythme**, pas une nécessité.
- **Le succès se mesure** : courbe de rétention, taux de clic. Le motion est jugé à la seconde où les gens partent, pas au goût d'un jury.

## Pourquoi ça marche, et ce qui serait raté si on changeait ces choix

- Un explicatif en **pur générique** (typo animée chorégraphiée, rendu léché, transitions spectaculaires) épuiserait le budget sur 30 s et noierait l'information. Le motion YouTube **économise l'effet pour la compréhension**.
- Une carte sans **zoom continu** (plans de carte coupés sec) fait perdre l'échelle et l'orientation ; le zoom en est la grammaire.
- Des captions longues en bas d'écran façon sous-titres TV perdent l'effet « mot vu en même temps qu'entendu » et sont masquées par l'interface sur téléphone.
- Un écran de fin animé plein cadre, avec du texte là où YouTube pose ses vignettes, devient illisible : la plateforme décide de la composition des 20 dernières secondes.

## Principes transférables

1. **Concevoir un système, pas une séquence** : quand le volume est grand, investir dans les éléments réutilisables (palette, rigs, cartons de chapitre, lower third maison) et réserver l'effort sur mesure aux 2 ou 3 moments-clés de chaque vidéo.
2. **Faire suivre un seul objet qui change de rôle** (l'horloge devient un graphique, le globe devient la rue) plutôt que couper entre des illustrations : l'attention reste accrochée.
3. **Le zoom continu donne l'échelle** : en cartographie ou dans n'importe quel sujet multi-échelle, ne jamais couper entre deux échelles sans montrer le trajet au moins une fois.
4. **Composer avec les zones de la plateforme** : écran de fin (5 à 20 s, 4 éléments), barre de lecture, zones de sécurité en vertical. L'habillage commence par une **maquette des zones interdites**.
5. **Le texte à l'écran double la voix, il ne la répète pas** : 4 à 6 mots au plus, le mot-clé surligné, et seulement quand le mot est un **chiffre, un nom ou un concept** à retenir.
6. **Partir d'un template, c'est déjà choisir le cliché** : le personnaliser jusqu'à ce qu'il ne soit plus reconnaissable, ou le dessiner soi-même.

## Clichés à éviter

- Le bouton « Subscribe » animé avec main qui clique et cloche, tiré d'un pack ; le glitch RGB entre chaque section.
- La texture de papier froissé plaquée sur tout (« style Vox ») sans raison éditoriale.
- La carte en 3D qui tourne sans rien montrer, et le survol Google Earth gratuit au début de chaque vidéo.
- Les captions mot à mot avec emoji et SFX sur **chaque** mot (fatigue reconnue en 2026).
- Le zoom punch-in toutes les deux secondes sur un talking head calme : un rythme social appliqué à un format long.
- L'intro de chaîne animée de 10 s avant le contenu : elle tue la première minute.

## Faits incertains

- L'usage de GEOlayers par Johnny Harris est affirmé par aescripts, l'éditeur du plugin (source intéressée), et je n'ai pas pu lire l'article.
- Les spécifications du style Hormozi viennent de vendeurs d'outils, pas de son équipe.
- Les détails du guide MrBeast sur la première minute viennent de reprises secondaires.
- Polymatter, RealLifeLore, Ali Abdaal, la vidéo du Monde : aucune source sérieuse lue sur leurs choix de motion. Les citer comme exemples reste une hypothèse.
- Le nombre exact de templates chez Envato ou Motion Array n'a pas été vérifié.
- Les grammaires visuelles décrites (zoom du globe, frontière qui se dessine) ne sont pas vérifiées image par image.

## Sources (consultées le 2026-10-10)

- Aide YouTube, écrans de fin : https://support.google.com/youtube/answer/6388789
- Aide YouTube, chapitres : https://support.google.com/youtube/answer/9884579?hl=en
- Storybench, « How Vox uses animation… » (avril 2024) : https://www.storybench.org/?p=21229
- PremiumBeat, « Replicating Vox motion graphic » : https://www.premiumbeat.com/blog/replicating-vox-motion-graphic/
- aescripts, GEOlayers 3 : https://aescripts.com/geolayers/
- aescripts, « How Johnny Harris makes maps » (non lu, 403) : https://aescripts.com/learn/how-johnny-harris-makes-maps/
- MapTiler, GEOlayers dans After Effects : https://docs.maptiler.com/guides/maps-apis/maps-platform/maptiler-cloud-maps-for-adobe-after-effects-via-geolayers-3-plugin
- Cartoon Brew, Google Earth Studio : https://cartoonbrew.com/tools/google-earth-studio-is-a-new-animation-tool-for-google-earth-imagery-167674.html
- 9to5Google, Google Earth Studio (décembre 2018) : https://9to5google.com/2018/12/07/google-earth-studio-animation-app/
- Submagic, captions Hormozi : https://www.submagic.co/blog/how-to-make-alex-hormozi-captions
- Joyspace, le style Hormozi en 2026 : https://joyspace.ai/hormozi-editing-style-2026-analysis
- Tubefilter, le guide MrBeast (septembre 2024) : https://www.tubefilter.com/2024/09/17/mrbeast-internal-production-guide-leaked-key-points/
- Passionfruit, le guide MrBeast : https://passionfru.it/mrbeast-leaked-document-81151/
- 9to5Google, objectifs YouTube 2025 (la télévision devant le mobile) : https://9to5google.com/2025/02/11/youtube-2025-goals/
- Wikipedia, DataGueule : https://en.wikipedia.org/wiki/DataGueule
- La Libre, retour du *Dessous des cartes* (septembre 2017) : https://www.lalibre.be/culture/medias-tele/2017/09/02/la-nouveaute-du-samedi-le-retour-du-dessous-des-cartes-sur-arte-ARKMUDWWXRFVJAKFIU7JY7NAZA/
- Envato Tuts+, packs de titres et templates : https://photography.tutsplus.com/articles/top-motion-presets-after-effects--cms-40574
