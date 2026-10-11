# Yvnnis — « Gare du Nord »

_Fiche ouverte le 2026-10-11 (phase 2, session 4, clip n°7). **État : terminée (une passe, sans recherche documentaire).** Source : 1800×1080 (5:3), 25 i/s, 3 min 09, SDR. Planche commitée : `gdn-plans.png`. Réalisateur, monteur, date : non cherchés. Aucune fiche de phase 1._

**Lu avant l'analyse** : `montage-rythme`, `montage-motion-design-principes`, `montage-couleur-et-intention`, grille de `montage-regard`, `culture/clips-rap-francais-pnl-et-autres.md`. Aucun goût de Diego.

## Intention
Un portrait du quartier de la gare du Nord par ses **réseaux** : voies ferrées, trains qui passent, devantures, métro, plan des lignes, puis la voie vue du ciel jusqu'à la gare. L'artiste est un point sur ces lignes. [DÉDUIT]

## Forme [mesuré ; plans longs et passages truqués vérifiés]
- **3 min 09, 55 plans détectés (au moins 115 réels, dont environ 60 dans la rafale de 1:34, révision de session 10), ASL 3,4 s sur les plans détectés.** Densité par minute : 15, 27, 12 ; médiane 2,4 s, 1,3 s, 2,6 s. Le passage truqué de 2:10-2:35 contient au moins cinq coupes que le détecteur a fondues (`verif_plan.py`).
- **Ouverture de 15 s : l'image se construit par carreaux.** Sur le noir, de petites vignettes bleues apparaissent une à une dans une grille, de plus en plus nombreuses, jusqu'à former la première image (Yvnnis sur les voies, un RER qui passe). [VU SUR IMAGES, 1 image/s] Même idée que l'ouverture de Booba « 6G » (l'image qui grandit dans le noir), par un autre moyen : la mosaïque.
- **Les voies ferrées** (0:15-1:35) : rap entre les rails, trains en filé au premier plan, tours et grues de la Chapelle ; plans de 1 à 7 s.
- **Une rafale-inventaire** (1:33,7-1:41,8) : **environ 65 devantures du quartier en 8 s, presque toutes de 2 images** (boucherie, épicerie orientale, cosmétiques, cabine…), toutes cadrées de face, avec cinq ou six arrêts de 0,3 à 0,7 s (révisé en session 10 : j'avais écrit « huit devantures en 0,6 à 1,4 s », le détecteur ne voyait que les arrêts), puis **un plan tenu de 13,3 s** sous la structure métallique d'un pont (vérifié continu).
- **Le métro** (1:55-2:27) : vignettage rond, quai, foule, un gros plan d'yeux en collage ; l'image s'assombrit (luminance 83, 75, 61, 46 par minute).
- **Fin truquée** : 2:27-2:30, l'image se fragmente de nouveau en carreaux (rime avec l'ouverture) ; 2:30-2:35, **les lignes du plan de métro**, en blanc lumineux, se dessinent sur Yvnnis en noir et blanc ; 2:35-2:52, **une vue satellite suit une voie ferrée** à travers les champs, puis les faubourgs, jusqu'au faisceau de voies de la gare (une coupe vers 2:51) ; 2:52-3:09, logo sur noir. [VU SUR IMAGES, 1 image/s]
- **Son** : plateau de -10 à -13 LUFS (intégré -11,6), aucun trou avant la fin. [mesuré, pas écouté]
- **Couleur** : froide et désaturée, ciel gris-bleu, sarcelle (chaleur R-B par minute : -21, -9, -11). Aucune couleur chaude franche sauf les devantures. [mesuré]
- **Calage** : au niveau du hasard, sur le mixage (20 % sur un temps, hasard 28 %) comme sur la musique séparée de la voix (20 % contre 24 % ; attaques fortes 17 % contre 20 %). [mesuré]

## Confirme, contredit, complète
- **Confirme** (septième clip sur sept) : pas de coupe sur les temps plus qu'au hasard.
- **Confirme** « une seule rafale » (6G) et « rafale puis plan tenu » : environ 65 devantures en 8 s, puis 13 s sous le pont.
- **Confirme** « une matière par monde » (vague 1) à petite échelle : rails de jour, métro sombre, ciel satellite, trois matières pour trois réseaux.
- **Complète** `montage-motion-design-principes` : un **motif graphique tiré du sujet** (la grille de carreaux, les lignes de métro, la voie vue du ciel) qui revient au début et à la fin, au lieu d'un habillage plaqué. La typographie est absente ; c'est le **plan de réseau** qui sert d'habillage.
- **Complète** `montage-grammaire` (ellipse) : la vue satellite qui suit la voie jusqu'à la gare résume un trajet entier en 17 s, et donne enfin la géographie que le clip a tenue cachée.

## Principes transférables
1. **Construire la première image** (mosaïque, cadre qui grandit) : une ouverture qui dit « regarde comment c'est fait » avant de montrer l'artiste.
2. **L'inventaire en rafale** : présenter un lieu par des dizaines de façades de face, à 2 images chacune (un clignotement, pas une lecture), ponctué de quelques arrêts de 0,3 à 0,7 s qui seuls se lisent, puis tenir un plan long. Utile pour un portrait de ville, de marque ou d'entreprise (les lieux, les métiers).
3. **Finir par la carte** : un plan d'ensemble graphique (satellite, plan de lignes) qui situe tout ce qu'on a vu en morceaux.

## Ce que Diego en a dit
Rien (`GOUTS.md`, `NOTES-DIEGO.md`, `RETOURS-DIEGO.md`).

## Pas fait, doutes
- Recherche documentaire (réalisateur, origine des images satellite).
- Le passage truqué (2:10-2:35) n'a pas été recompté plan par plan ; le nombre de plans est un minimum.
- Je suppose que la vue satellite suit la ligne de Paris-Nord ; je ne l'ai pas identifiée sur une carte.

## Révision (2026-10-11, session 10 de la phase 2)
Mesuré avant relecture : chaque image de 1:33 à 1:42 (25 i/s), différence image à image (écart net : 33 à 87 aux coupes, 1 à 2 ailleurs) et deux tuiles à pleine cadence. Planche commitée : `gdn-revision-pleine-cadence.png` (1:35,5-1:37,5, les 50 images dans l'ordre, de gauche à droite).
- **Corrigée — la rafale-inventaire.** Ce n'est pas « huit devantures en 0,6 à 1,4 s » : c'est **environ 65 devantures en 8 s (1:33,7-1:41,8), presque toutes de 2 images (0,08 s)**, avec cinq ou six arrêts de 8 à 18 images (0,3 à 0,7 s : les bouchers en blouse, une façade verte, une enseigne Ria qu'un cycliste traverse), un filé et un noir d'une image, et des retours (Ria, KTC, rideau baissé, Ria). PySceneDetect ne garde aucun plan de moins de 0,6 s (réglage par défaut) : il n'a vu que les arrêts. [VU SUR IMAGES, chaque image]
- **Confirmée** : rafale puis plan tenu (13,3 s sous le pont, 1:41,8) ; une seule rafale de ce type dans le clip.
- **Nouvelle** : c'est un **clignotement** (12,5 changements par seconde), pas une suite de plans lisibles : on ne lit aucune enseigne, on reçoit une matière (couleurs chaudes des devantures, toutes de face, même cadre). Les arrêts donnent seuls quelque chose à lire. **Photosensibilité mesurée** (`labo/photosensibilite/flash_check.py` sur 1:33-1:42,5) : 7 flashs en 9,5 s, **pire seconde 2**, aucun flash rouge : **conforme** (limite : 3 par seconde). Les façades changent à 12,5 Hz, mais leur luminance moyenne varie peu : c'est le « strobe sûr » de `montage-kinetic-editing` (changer teinte et forme à luminance égale) vu sur une vraie vidéo. [mesuré]
- Le nombre de plans du clip devient **au moins 115** (55 détectés + environ 60 dans la rafale), et l'histogramme « < 1 s » est faux pour ce passage.
- Calage : non refait ; à 12,5 coupes par seconde, la question ne se pose plus dans la rafale (plus rapide que tout temps).
