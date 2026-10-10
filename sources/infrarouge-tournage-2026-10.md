# Tournage de nuit en infrarouge proche (NIR) : sources

Recherche du 10/10/2026 (BACKLOG Y15, suite de l'examen n°10 et de l'atelier 23). Faits reformulés, chacun avec sa source. Statut : **lu** (page ou PDF ouvert et lu), **via recherche** (résumé de moteur ou source secondaire non ouverte), **[CALCUL]** (fait par moi, non sourcé). Rien n'a été testé sur une vraie caméra : toute recette qui en découle est **[THÉORIQUE]**.

## 1. Caméra : pourquoi et comment elle voit l'IR

| Fait | Source | Statut |
|---|---|---|
| Les capteurs numériques enregistrent d'environ 300 à 1200 nm ; un filtre bloque d'origine presque tout ce qui sort du visible. Pour un vrai tournage IR, il faut modifier le capteur (retrait de ce filtre) | RED, « Infrared cinematography » (RED 101) : https://www.reddigitalcinema.com/red-101/infrared-cinema (l'ancienne URL red.com redirige) | lu |
| Sans filtre devant l'objectif, l'image mélange visible et IR : saturation des couleurs en baisse (l'IR passe dans les trois canaux). Gain d'au moins un diaph sans filtre ; perte d'un diaph ou plus avec un filtre passe-IR « agressif » | RED 101, même URL | lu |
| Filtres passe-IR : standards (Hoya R72, B+W 092, Wratten 89b) coupent sous ~700-720 nm ; agressifs (Hoya RM90, Wratten 87/87c, B+W 093) coupent sous ~800 nm ou plus | RED 101 | lu |
| L'IR fait le point à une distance légèrement différente du visible ; fermer le diaph aide à garder les deux nets ; la diffraction arrive plus tôt (douceur vers f/11 au lieu de f/22) | RED 101 | lu |
| Le décalage de point vient de la dispersion du verre de l'objectif, pas du filtre : retirer le filtre IR-cut ne le corrige pas. Un objectif « IR-corrigé » est nécessaire seulement si visible et NIR doivent être nets au même réglage ; en NIR seul, on fait le point en NIR | Commonlands (Max Henkart, mis à jour 06/2026) : https://commonlands.com/blogs/technical/nir-imaging-machine-vision | lu (fabricant d'optiques machine vision) |
| Balance des blancs : image rougeâtre avant balance ; convention courante = balance sur le feuillage ; après balance, image quasi bichrome | RED 101 | lu |
| Peau : rendu « plus lisse et blanc fantomatique », veines proches de la surface plus sombres et plus visibles. Vêtements : une teinte peut s'inverser (le rouge plus clair que le blanc) | RED 101 | lu |
| Explication physique : le NIR pénètre la peau de quelques millimètres et y diffuse (aspect laiteux, cireux) ; le sang (hémoglobine désoxygénée) l'absorbe, d'où les veines sombres, seulement si elles sont superficielles | Public Lab, note de recherche : https://publiclab.org/n/13700 ; Infrared100 : https://www.infrared100.org/2014/ | via recherche |
| Location « full spectrum » : Sony FX3 converti, sensible ~250 à >1000 nm ; fourni avec un hot mirror 82 mm (retour au visible) et un filtre IR au choix 715 nm, 850 nm ou Aerochrome ; l'autofocus peut peiner en IR ; certains objectifs font un point chaud (hotspot) en IR ; torche 850 nm 5 W disponible | Wild Films (loueur UK) : https://www.wildfilms.co.uk/full-spectrum-camera-hire-sony-fx3 | lu |
| Kolari (convertisseur) : un appareil full spectrum sans filtre gagne « 2 diaphs » par rapport à un appareil d'origine | Kolari Vision, 22/09/2023 : https://kolarivision.com/full-spectrum-for-low-light-photography | lu (chiffre commercial) |
| RED a vendu un OLPF « full spectrum » interchangeable : il faut alors filtrer devant l'objectif pour choisir sa bande | ProAV (revendeur) : https://proav.co.uk/cameras-lenses/kippertie-full-spectrum-false-colour-olpf | via recherche |
| **Sony, Canon, ARRI : aucune fiche officielle trouvée** décrivant une caméra cinéma IR ou une procédure de conversion. ARRI Rental mentionne seulement des ALEXA Monochrome natives sensibles à l'IR (voir §4) | — | lacune |

## 2. 850 nm contre 940 nm

| Fait | Source | Statut |
|---|---|---|
| 850 nm : faible lueur rouge visible ; 940 nm : pas de lueur en conditions normales. À fort courant, la lueur du 850 nm se voit dans le noir | Commonlands (même URL) ; LDP/MaxMax : https://maxmax.com/light-sources/infrared-light-sources/professional-infrared-illuminators | lu |
| Sur beaucoup de capteurs silicium, le rendement quantique à 940 nm est « près de la moitié » de celui à 850 nm, parfois moins ; il faut plus de puissance ou de pose pour le même rapport signal/bruit | Commonlands | lu (pas de courbe constructeur ; à vérifier sur la fiche du capteur de la caméra louée) |
| LDP/MaxMax : ses LED 940 nm ont environ la moitié de la puissance des 850 nm. Portées annoncées : 850 nm 150 m (25°) / 60 m (70°) ; 940 nm 80 m (25°) / 45 m (70°). L'œil peut apercevoir la source en la regardant, pas l'IR réfléchi par un objet | LDP/MaxMax, même URL | lu (données commerciales) |
| Fabricants de capteurs : Sony annonçait pour le STARVIS IMX290 une sensibilité NIR (850 nm) ≥ 3× celle d'un capteur éclairé par l'avant de même pixel | asmag (reprise de Sony) : https://www.asmag.com/showpost/19626.aspx | via recherche (page Sony non ouverte) |
| Bande d'absorption de la vapeur d'eau ~930-970 nm (pertes à distance en extérieur à 940 nm) | Commonlands | lu |
| Liens morts : syronoptics.com (2 articles 850/940) → 404 | — | lien mort |

## 3. Illuminateurs et sécurité oculaire (IEC 62471)

| Fait | Source | Statut |
|---|---|---|
| IEC 62471 / EN 62471 (« Photobiological Safety of Lamps and Lamp Systems ») s'applique aux LED et aux diodes IR (IRED) ; elle a remplacé l'IEC 60825-1 (lasers) pour les LED | Vishay, « Eye Safety Risk Assessment of Infrared Emitting Diodes According IEC 62471 », doc. 81935 rév. 2.1, 15/11/2021 : https://www.vishay.com/docs/81935/eyesafe.pdf | lu |
| La plupart des IRED émettent entre 800 et 960 nm. Risques dans cette bande : **risque thermique rétinien**, **lésion thermique de la cornée** et effets différés possibles sur le **cristallin** (cataracte). Les limites cornée/cristallin ne figurent que dans l'IEC 62471 et la directive européenne 2006/25/CE | Vishay 81935 | lu |
| Vishay : toutes ses IRED unitaires sont « exempt » ; « seulement avec des matrices (arrays), il faut veiller à ne pas dépasser les limites cornée/cristallin ». La classification vaut pour le **produit final**, pas pour la LED seule | Vishay 81935 | lu |
| Quatre groupes de risque : exempt (RG0), faible (RG1), modéré (RG2), élevé (RG3) ; plus le groupe est haut, plus la durée d'exposition de référence est courte. Évaluation à 200 mm, hypothèse pire cas | ams OSRAM, AN002 « Details on photobiological safety of LED light sources », 16/09/2025 : https://look.ams-osram.com/m/1d720a7b18ab3fce/original/Details-on-photobiological-safety-of-LED-light-sources.pdf | lu |
| RG2 = « pas de danger grâce à la réaction d'aversion à la lumière très vive ou à l'inconfort thermique » | ams OSRAM AN002, tableau 1 | lu |
| Le danger « IR pour l'œil » couvre 780-3000 nm (clause 9 de l'IEC 62471-7 pour les luminaires) | Table des matières IEC 62471-7, VDE : https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec62471-7{ed1.0}b.pdf | via recherche |
| **Déduction (non citée telle quelle)** : l'IR proche ne provoque pas d'éblouissement ; la réaction d'aversion sur laquelle repose le RG2 ne joue donc pas pour un illuminateur IR. Ne pas compter sur le réflexe du sujet | ams OSRAM AN002 (définition RG2) + nature invisible de l'IR | [DÉDUIT] |
| **Seuils numériques IR (W/m²) : non trouvés dans une source lue** ; texte de la norme payant. Ne rien chiffrer : demander le groupe de risque IEC 62471 de l'illuminateur au loueur ou au fabricant | — | lacune |

## 4. Œuvres tournées en IR proche (sourcées)

| Œuvre | Ce qui est sourcé | Source | Statut |
|---|---|---|---|
| *Planet Earth II* (BBC, 2016) | Projecteurs IR + RED Dragon sensibles à l'IR pour des images monochromes de nuit « qui ne dérangent pas les animaux » ; caméra thermique quand on ne peut pas éclairer ; Sony a7S pour la couleur en basse lumière. Épisode « Cities » : léopards de Mumbai la nuit (IR **et/ou thermique** selon les sources, pas tranché) | The Credits (MPA), C. Viollet, 09/03/2017 : https://www.motionpictures.org/2017/03/cutting-edge-technology-lets-planet-earth-ii-shoot-dark/ ; CineD : https://www.cined.com/bbc-planet-earth-ii-cinematography-explained/ ; PetaPixel 07/03/2017 (403) | lu (MPA) ; via recherche (CineD) |
| *Dune : Deuxième partie* (2024), Greig Fraser | Extérieurs de Giedi Prime (« soleil noir ») : ALEXA dont on a retiré le filtre IR (pas assez d'ALEXA Monochrome natives), filtre devant l'objectif bloquant le visible ; un noir à l'œil peut sortir blanc : costumes doublés. **De jour, pas de nuit** | ARRI Rental, interview Fraser : https://www.arrirental.com/en/about/overview/news/interview-on-dune-part-two-with-greig-fraser-acs-asc ; ASC (page vide au fetch) : https://theasc.com/articles/expanding-view-dune-part-two ; filtre 87c : Slashfilm https://slashfilm.com/1598368/dune-2-unreal-engine-video-game-tech-infrared-cameras-harkonnen-arena-fight | via recherche (ARRI) |
| *Rogue One* (2016) | ALEXA 65 modifiées IR par ARRI Rental, utilisées comme caméras VFX éclairées en IR | ARRI Rental (même interview) | via recherche |
| *Nope* (2022), Hoyte van Hoytema | Nuit américaine : ALEXA 65 convertie IR + caméra film Panavision System 65 sur rig miroir, images superposées (IR = luminance de nuit, film = couleur). **De jour** | YMCinema 03/08/2022 (cite une interview Kodak) : https://ymcinema.com/2022/08/03/nope-was-shot-on-a-unique-day-for-night-rig-of-alexa-65-infrared-and-panavision-system-65/ ; No Film School : https://nofilmschool.com/dp-hoyte-van-hoytema-night-shots-on-nope | lu (YMCinema) |
| *Zero Dark Thirty* (2012), Fraser | Raid final : éclairage IR de nuit + vrais intensificateurs de lumière montés en PL sur l'ALEXA (look « vision nocturne » verte). L'interview MPA ne parle pas de l'IR ; les détails viennent de No Film School / HitFix | MPA Q&A 10/01/2013 : https://www.motionpictures.org/2013/01/a-qa-with-greig-fraser-cinematographer-on-zero-dark-thirty/ ; No Film School : https://nofilmschool.com/2012/12/cinematography-sound-design-zero-dark-thirty-arri-alexa | via recherche |
| Historique | Article *American Cinematographer* 1940 (Hatto Tappenbeck) sur la pellicule infrarouge à Hollywood | Lantern : https://lantern.mediahist.org/catalog/american21asch_0521 | via recherche |

Pas trouvé (donc pas cité) : un film de fiction tourné en IR proche **de nuit sur un dormeur** ; un article *American Cinematographer* récent sur la nuit en IR. Les films « found footage » en mode NightShot ne sont pas cités faute de source lue.

## 5. Les yeux sous IR

| Fait | Source | Statut |
|---|---|---|
| Illuminateur coaxial (dans l'axe de l'objectif) : la rétine renvoie la lumière vers le capteur, **pupille brillante** (même effet que les yeux rouges au flash). Illuminateur décalé : **pupille sombre** | Brevets d'oculométrie, ex. US10984236B2 : https://patents.google.com/patent/US10984236B2/en | via recherche (brevets, pas d'article revu par des pairs) |

## 6. Chiffre de l'examen n°10 : « 2 milliards de dormeurs au même instant »

- **Aucune source** trouvée qui donne le nombre de personnes endormies simultanément. Le seul outil trouvé est une simulation (« What The Hell Are People Doing? », humans.maxcomperatore.com, signalée par beSpacific 29/05/2025 : https://www.bespacific.com/?p=113561), qui se décrit elle-même comme « une impression, pas un flux réel ». Statut : **invérifiable**.
- Population : ~8,2 milliards mi-2024 (ONU, World Population Prospects 2024 : https://www.un.org/sustainabledevelopment/blog/2024/07/press-release-wpp2024/). Lu via recherche.
- **[CALCUL]** 8,2 G × 7/24 à 8/24 ≈ **2,4 à 2,7 milliards en moyenne** ; le chiffre réel varie selon l'heure UTC, car la population est concentrée en Asie (≈ UTC+5:30 à +8) : plus haut pendant la nuit asiatique. « 2 milliards » est donc un ordre de grandeur plausible mais **non sourcé** ; le dire en voix off comme une estimation (« environ un tiers de l'humanité », « plus de deux milliards ») ou retirer.
- « 8 milliards de dormeurs » (direction C) = la population totale, pas des dormeurs simultanés : juste si on dit « chaque nuit », faux sous l'image d'un globe avec la ligne de nuit.

## 7. Liens en échec
- 403 : https://petapixel.com/2017/03/07/camera-tech-used-film-animals-pitch-dark-planet-earth-ii/ ; https://britishcinematographer.co.uk/greig-fraser-asc-acs-dune-part-two/
- 404 : https://syronoptics.com/blogs/technical-article/is-940nm-better-than-850nm ; https://syronoptics.com/blogs/technical-article/what-is-better-850nm-or-940nm
- 503 : https://diglloyd.com/blog/2006/20060107_2-InfraredWithHumanBody.html
- Page vide au fetch : https://theasc.com/articles/expanding-view-dune-part-two
