# Examen n°8 — « Nuit Basse » : annonce de programmation d'un festival, Reel kinetic avec texte animé et rushes à stroboscope (session 15, 2026-10-10)

Réponse écrite **uniquement à partir des skills et des labos** (`montage-direction-artistique` étapes 0 à 5 et §double livrable, `montage-kinetic-editing` §1-4 dont R7 / R7b et §6 photosensibilité, `montage-rythme` §Ziak, `montage-motion-design-principes`, `montage-regard`, `montage-son-et-emotion`, `montage-loudness-livraison`, `montage-formats` §vertical, `culture/kinetic-edit-monteurs-reseaux-sources.md`, `culture/enter-the-void-generique-noe-tom-kan.md`, `labo/paroles/` (lisibilité OCR, ASS mot à mot, temps de lecture), `labo/photosensibilite/` dont `strobe-rushes/` fait ce matin), puis critiquée. Objectif fixé par le BACKLOG 78 : brief réseaux sociaux kinetic (goûts de l'utilisateur), texte incrusté animé, contrainte de photosensibilité ; mettre à l'épreuve la fiche monteurs d'edits et le labo ASS.

## Le brief (inventé)
Festival de musique électronique « Nuit Basse » (inventé), 3e édition, 2 nuits dans un hangar portuaire. Annonce de la programmation : **24 artistes**, dont **4 têtes d'affiche**.
Livrables :
1. un **Reel / TikTok 9:16 de 30 s** (sortie de l'annonce) ;
2. une **version 15 s** (publicité payante) ;
3. la même 30 s diffusée sur les **écrans urbains de la ville (DOOH)** : la régie exige une attestation de non-dangerosité photosensible (après une plainte l'an dernier).

Matière : **rushes de l'édition 2** (4 h de foule, scène, lasers, mains, vestiaire, lever de soleil sur le quai), tournés par des vidéastes bénévoles au téléphone et en hybride 25 i/s, **beaucoup de plans avec le stroboscope de scène à ~8 Hz** ; un morceau de la tête d'affiche (inventé, 128 BPM, droits accordés pour 30 s) ; le logo et une police de marque (une grotesque condensée, 3 graisses).
Demandes :
- Le directeur du festival : « Cuts rapides, **beaucoup de SFX**, que ça claque comme les edits qu'on voit partout. Et **tous les noms doivent être lisibles**. »
- La programmatrice : « Les 20 autres ne sont pas des seconds couteaux : pas de liste en tout petit à la fin. »
- La régie DOOH : « Rien qui clignote. »

## Étape 0 — Inventaire des rushes (le film est tourné)
1. **Les plans à strobe sont la matière la plus forte** (ce sont eux qui disent « on était là ») **et la plus dangereuse**. Labo `strobe-rushes` : un strobe de scène à 8 Hz donne **4 à 9 flashs/s dans le fichier** selon la rencontre avec l'obturateur ; inlivrable brut. Il faut **mesurer chaque plan candidat** avec `flash_check.py` avant de l'aimer.
2. **Téléphones, 25 i/s, bénévoles** : pas de haute cadence, donc pas de vrai ralenti ; ralentir = interpolation (artefacts sur les bras et les lasers, `montage-kinetic-editing` §velocity, BACKLOG 49) ou saccade.
3. **Pas de son direct exploitable** à part le grondement du système son : les SFX seront de bibliothèque (Sonniss, licence vérifiée) ou fabriqués.
4. **Le lever de soleil sur le quai** : la seule image calme et colorée de 4 h de rushes. À garder pour quelque chose.
5. **Le texte est le sujet réel** : 24 noms. Calcul avant toute idée (`labo/paroles/temps_lecture-resultats.md`, normes ATAA 14-15 car./s, Netflix FR 17) : un nom moyen fait ~11 caractères ; 24 noms ≈ 270 caractères ≈ **18 s de lecture à 15 car./s** si on les lit l'un après l'autre. Sur 30 s qui doivent aussi montrer la fête, **« tous lisibles » au sens d'une lecture linéaire est impossible**. Je l'écris au client avant de proposer (étape 5).

## Étape 1 — Intention
1. **Émotion** : le **manque** (« j'y étais / je veux y être ») et l'impatience, pas l'information.
2. **Message** : « Ils viennent. Tu viens ? » Les noms sont la promesse ; les images, la preuve.
3. **Public** : 20-35 ans, déjà clubbers, qui **cherchent leurs artistes** dans une liste : ils ne lisent pas une liste, ils la **balaient** (lecture de repérage, plus rapide que la lecture de phrases ; aucune norme ne la chiffre : hypothèse à vérifier en phase 2 avec de vrais regards).
4. **Diffusion** : Reels / TikTok (son activé chez les fans, muet dans le fil), DOOH **sans son**.
5. **Contraintes** : photosensibilité (DOOH, et je l'applique aussi aux réseaux : même fichier), 30 s de musique, rushes amateurs.
6. **Ne surtout pas être** : l'aftermovie de festival générique — ralentis de confettis, drone, coucher de soleil sur la foule, « teal & orange », un whoosh identique par coupe, la liste des noms qui défile en générique de fin.
7. **Contradictions** : (a) « tous lisibles » contre « cuts rapides » ; (b) « ça claque » (strobe, flashs) contre « rien qui clignote » ; (c) « beaucoup de SFX » contre un morceau électronique qui est déjà une machine à impacts : les SFX vont se battre avec la grosse caisse (`montage-kinetic-editing` §hiérarchie : musique varie comme un SFX).

**Idée propre au sujet** : **la lumière écrit les noms**. Dans un hangar plongé dans le noir, on ne voit les gens que quand la lumière les touche ; la programmation apparaît de la même façon : un nom n'existe que dans un coup de lumière. Le strobe, au lieu d'être un danger à effacer, devient l'outil qui **révèle** — à condition d'être retimé (≤ 2 coups par seconde, sur les temps).

## Étape 2 — Trois directions contrastées

### A — « La lumière écrit » (strobe retimé en métronome)
- **Parti pris** : tous les plans de foule à strobe sont **retirés au tirage par saccade** (une image tenue 6 à 12 images) en **choisissant à la main** les images allumées pour qu'elles tombent sur les noires du morceau (128 BPM = 2,13 temps/s, sous le seuil de 3 flashs/s ; labo : saccade = seul traitement qui garde le coup intact et passe toujours). Chaque coup de lumière révèle un corps **et** un nom. Entre les coups : noir, lasers lents (non saccadés, ils ne flashent pas), le grondement.
- **Références** : le principe Noé / Kan (rythme par la forme et la teinte quand la luminance doit rester stable) ; le step-printing de Wong Kar-wai et Doyle (*Chungking Express*, d'après les sources écrites, non vérifié image par image) pour le mouvement haché qui devient émotion.
- **Rythme** : une coupe par temps fort au plus ; les noms sur les temps ; **le geste qui manque entre deux images tenues est rempli par le son**.
- **Palette** : noir + le blanc-bleuté du strobe + le vert des lasers ; **une seule couleur chaude** : le lever de soleil, réservé à la fin (couleur forte mesurée et réservée, pièce 02).
- **Typo** : la grotesque condensée, blanc, **une graisse par rang** (Black pour les têtes d'affiche, Medium pour les 20 autres, jamais Thin : labo OCR) ; le nom apparaît sur l'image allumée et **reste** dans le noir suivant (persistance : c'est la rétine qui garde le nom).
- **Son** : la musique ; par-dessus, **un seul type de SFX** : le claquement électrique d'un relais de strobe (fabriqué : transitoire court + souffle), un par coup de lumière, varié en durée ; impact grave réservé aux 4 têtes d'affiche.
- **Risque** : la saccade sur 30 s fatigue ; un « look » qui peut sembler une erreur de lecture sur un téléphone lent.

### B — « Edit » (le goût de l'utilisateur, sans strobe)
- **Parti pris** : grammaire des velocity edits et du B-roll à SFX denses (fiche monteurs d'edits) : rampes de vitesse sur les temps, raccords de direction (mains levées → laser qui monte → logo), whoosh dont la durée = le mouvement, punch-in sur les têtes d'affiche. **Tous les plans à strobe sont exclus** au montage (ils ne passent pas), on ne garde que lasers, mains, foule en lumière continue.
- **Références** : Kolder (l'ordre de jugement : attention, émotion, technique) ; Schiffer (un son par mouvement) ; Scott Pilgrim (une règle par séquence).
- **Typo** : noms en cartons pleins plein cadre, fonds de teintes différentes **à luminance égale** (pièce 09, cartons ≥ 4 images) ; mot à mot pour les 20.
- **Son** : banque de 5 whooshs en rotation, risers sur les noms, impacts sur les 4 têtes d'affiche, la musique filtrée passe-bas pendant les montées.
- **Risque** : c'est l'aftermovie générique accéléré ; il sacrifie la meilleure matière (le strobe) et ressemble à tous les autres festivals.

### C — « Depuis le quai » (le retrait, l'usage Ziak)
- **Parti pris** : on est **dehors**. Plan tenu du hangar vu du quai au lever du soleil (le seul plan calme), son de la fête entendu à travers le mur (passe-bas, réverbération). Les 24 noms montent en **colonne lente**, à la vitesse de lecture, sur ce plan. À 22 s, coupe dans le hangar : **un seul plan** de foule (saccadé, livrable), le filtre s'ouvre, la tête d'affiche n°1 sur le drop. Montage sur l'arrangement, pas sur le beat.
- **Références** : Ziak (le montage qui retient) ; *Les Revenants* (la musique entendue de loin).
- **Risque** : 22 s de plan fixe dans un fil TikTok = défilement ; il contredit la demande « cuts rapides » et le goût de l'utilisateur pour cet usage précis.

## Étape 3 — Recommandation : **A « La lumière écrit »**, avec la grammaire de B dans la version 15 s
- **Pourquoi A** : c'est la seule direction où la contrainte (le strobe dangereux) devient l'idée ; elle garde la matière la plus vraie ; elle répond aux trois demandes à la fois (ça claque à chaque coup de lumière, chaque nom a son coup donc sa place, rien ne clignote au-delà de 2 coups/s). Elle respecte le goût de l'utilisateur : coupes nettes et beaucoup de SFX, mais **un SFX qui a une cause visible** (le relais du strobe), pas un whoosh générique.
- **Argument contre (règle « recommander ce que je sais faire »)** : A sort du labo que je viens de faire ce matin. Je recommande peut-être la technique fraîche, pas la direction juste. Test honnête : si le strobe n'existait pas dans les rushes, A n'existerait pas — c'est donc une idée **née de la matière**, ce qui la justifie ; mais la saccade sur 30 s n'est pas éprouvée à l'œil (BACKLOG 80).
- **Version 15 s** : grammaire de B (plus directe, publicité payante), avec **un seul** coup de strobe saccadé pour la tête d'affiche n°1 : la signature de A en une seconde.

## Traitement détaillé (A, 30 s = 16 mesures de 1,875 s à 128 BPM, 25 i/s)
| Mesures | Temps | Image | Texte | Son |
|---|---|---|---|---|
| 1 | 0-1,9 s | **Image 1 : un coup de strobe sur la foule bras levés** (image tenue 12 images), puis noir avec les lasers | « NUIT BASSE » + dates, apparus dans le coup | grosse caisse + relais ; le drop du morceau dès l'image 1 (hook R1) |
| 2-3 | 1,9-5,6 s | noir et lasers lents ; 4 coups saccadés (1 par blanche) : mains, nuque en sueur, verre, regard | rien : on installe la règle (la lumière révèle) | relais varié, grondement |
| 4-7 | 5,6-13,1 s | 16 coups (1 par noire), 4 par mesure ; chaque coup = un plan différent + **un nom** des 20, en Medium, à une place différente du cadre (rupture de forme, pièce 09), qui **reste** dans le noir jusqu'au coup suivant | 16 noms, un par temps : chaque nom est affiché ~0,47 s + reste visible en fondu sur le noir jusqu'à 0,9 s ; en balayage, ça suffit à repérer un nom connu ; en lecture, non (assumé : voir carton final) | un relais par nom, durées variées (variation de durée avant le timbre) |
| 8 | 13,1-15 s | **trou** : 1 mesure de noir total, lasers coupés | rien | la musique filtrée passe-bas, le relais seul sur le 4e temps (silence tactique avant le rang 1) |
| 9-12 | 15-22,5 s | les 4 têtes d'affiche : 1 par mesure ; coup de strobe tenu 12 images + plan de scène | nom en Black, 25-40 % de la largeur, **tenu toute la mesure (1,9 s)** : lisible au sens strict (11 car. / 15 car./s = 0,7 s, très au-dessus) | impact grave (rang 1) sur chaque nom, 4 en 7,5 s : **une seule par séquence de ~2 s, c'est trop** → impact plein sur les n°1 et n°4, impacts filtrés (moins de grave) sur 2 et 3 |
| 13-14 | 22,5-26,3 s | **le lever de soleil sur le quai**, plan continu, pas saccadé, la seule couleur chaude | les 4 noms restants (des 20) en ligne, puis **les 24 en carton** sur le ciel | la musique entendue à travers le mur (idée de C en 4 s) |
| 15-16 | 26,3-30 s | carton final : logo, dates, « billetterie » | **les 24 noms**, tenus 3,7 s, lecture de repérage ; la liste complète aussi en description du post | le drop revient sur la dernière mesure, coupé net sur le logo |

- **Photosensibilité** : au plus **un coup de lumière par noire** (2,13/s) ; un coup = une transition sombre → clair puis clair → sombre **sur l'image tenue suivante** : 1 flash par coup, 2,13 flashs/s < 3 (à mesurer : la persistance du nom en fondu adoucit la descente). **Interdit** : un coup par croche (4,3/s). Mesures 4-7 : mesurer **chaque seconde glissante** avec `flash_check.py` sur le fichier encodé, et un vrai test Harding pour la régie DOOH (`flash_check` n'en est pas un). Les noms apparaissant dans le coup ne créent pas de transition supplémentaire (même image).
- **Texte** : zone sûre 9:16 (hors 15 % du bas et colonne d'interface à droite) ; graisse ≥ Medium, ≥ 2,6 % de la hauteur pour les 20, boîte jamais nécessaire (fond noir) ; mot à mot exporté en ASS calé à l'image (`labo/paroles/ass_mot_a_mot.py`), **un événement par nom** (le pop dans une ligne fait glisser la ligne : 110 px au labo).
- **Couleur** : noir protégé (pas de noir relevé, `atelier/17`), blanc du strobe non coupé (on garde les hautes lumières brûlées : c'est la vérité du strobe), lasers saturés mais sous le rouge WCAG (les lasers rouges éventuels : vérifier le critère « rouge saturé »).
- **Son** : la musique fait le niveau ; les relais à -16 dB sous la grosse caisse, EQ creusée sur 50-100 Hz pour ne pas doubler le kick ; impacts sur les têtes d'affiche **à la place** d'une grosse caisse (on retire un kick du morceau à cet endroit, montage de la musique). -14 LUFS / ≤ -1 dBTP mesurés sur le MP4 (R6). DOOH : muet → l'image doit tenir seule ; c'est le cas de A (le coup de lumière se voit).
- **Outils** : sélection des plans à strobe et mesure : ffmpeg + `flash_check.py` ; saccade : Premiere (Frame Hold sur chaque image choisie, à vérifier en phase 2) ou script de sélection d'images (`strobe-rushes/strobe.py` donne la logique) ; texte : AE (animateurs de texte, persistance par opacité) ou ASS ; mix : Premiere / Fairlight.

## Critères de réussite
1. Muet, sur un téléphone : on comprend « une fête dans le noir » et « une liste d'artistes » avant 3 s.
2. Un fan qui cherche **son** artiste parmi les 20 le trouve au premier visionnage (test : 5 personnes, 5 noms demandés).
3. Les 4 têtes d'affiche sont lues par tous.
4. `flash_check.py` OK sur chaque seconde du fichier livré ; Harding OK pour le DOOH.
5. Le coup de lumière est reconnu comme un choix (pas une panne de lecture) : demander « qu'est-ce qui ne va pas avec cette vidéo ? » à 3 personnes ; si l'une parle de bug, allonger les images tenues ou réduire la saccade aux mesures 4-12.
6. Le lever de soleil arrive comme un soulagement (la seule couleur chaude, mesurée et réservée).

## Ce que je réponds au client (étape 5)
- « Tous les noms lisibles en 30 s avec des cuts rapides » : **non au sens d'une lecture de chaque nom** (18 s de lecture pure à 15 car./s) ; **oui au sens où chacun a son temps fort**, sa place à l'image et le carton final ; et la liste complète en légende du post. Je préfère ce chiffre maintenant à une plainte de la programmatrice après la sortie.
- « Beaucoup de SFX » : oui, mais un son **qui vient de la salle** (le relais du strobe) ; des whooshs génériques sur un morceau techno se battraient avec le morceau.
- « Ça claque » et « rien qui clignote » ne sont **pas contradictoires** si le claquement est retimé à 2 par seconde : c'est la seule promesse que je peux signer pour le DOOH.

## Autocritique (sans complaisance)
- **Ce qui tient** :
  1. **Les chiffres viennent avant les idées** : temps de lecture des 24 noms (18 s), flashs du strobe (4-9/s), seuil (3/s), tempo (2,13 temps/s). La contradiction « tous lisibles » est **démontrée** et non seulement sentie ; c'est la première fois qu'un « savoir dire non » s'appuie sur un calcul de lecture.
  2. **La contrainte devient l'idée** (le strobe dangereux = la lumière qui écrit), et la référence Noé / Kan sert la même logique qu'à l'atelier 09.
  3. Le goût de l'utilisateur est respecté sans être appliqué en réflexe : SFX denses, mais avec une cause visible (règle Scott Pilgrim / atelier 02).
  4. Le lever de soleil, seule image calme, reçoit un rôle (la couleur réservée) au lieu d'être jeté ou mis en « respiration » décorative.
- **Ce qui est faible** :
  1. **Recommander la technique du matin** : A est née du labo `strobe-rushes`, fait il y a une heure. L'argument « idée née de la matière » est honnête, mais **je n'ai jamais vu 30 s de saccade** : le risque « ça ressemble à un bug » est réel sur un téléphone, et je le découvre seulement en critère 5. Il faut une pièce d'atelier avant d'oser le proposer à un vrai client (BACKLOG 80).
  2. **Mesures 9-12 : la hiérarchie des impacts est violée** (4 rangs 1 en 7,5 s) ; je l'ai rattrapée dans le tableau (impacts filtrés), mais c'est une correction de dernière minute : la structure elle-même met 4 sommets à la suite. Mieux : n°1 seul au sommet (mesure 12, la dernière), les trois autres en montée (n°4 → n°2), ordre décidé avec la programmatrice.
  3. **Les 16 noms en 7,5 s (mesures 4-7)** : un nom par noire = 0,47 s, en dessous du plancher ATAA (16 images = 0,64 s) et de Netflix (5/6 s). La « lecture de repérage » est une **hypothèse sans source** que j'utilise pour justifier mon propre rythme. Il faut au moins une noire pointée par nom (0,7 s) ou des paires de noms par coup — ou assumer et tester (critère 2).
  4. **Le son du « relais de strobe »** : je ne sais pas ce que fait un vrai stroboscope de scène (le Martin Atomic historique à lampe xénon claque ; les strobes LED récents sont presque muets, à vérifier). Cause visible, oui ; cause sonore **plausible**, non vérifiée.
  5. **Rien sur le droit à l'image** des festivaliers filmés par des bénévoles (pub payante en 15 s) : ce n'est pas mon métier, mais un directeur artistique de post doit le signaler avant de monter des visages reconnaissables.
  6. **Fiche monteurs d'edits peu utilisée** : B l'emploie, A seulement pour « un son par mouvement ». L'examen devait l'éprouver ; elle a surtout servi de repoussoir (l'aftermovie générique).
- **Note : 15/20.** Contradictions chiffrées et dites au client, contrainte transformée en idée, goût de l'utilisateur servi avec une cause ; mais recommandation fondée sur une technique non vue en mouvement, hiérarchie des impacts rattrapée tard, et temps de lecture des 16 noms sous les planchers que je cite moi-même.

## Corrections versées
- `montage-direction-artistique` : (1) **un texte à lire est une durée** : avant de proposer, compter les caractères et convertir en secondes (14-15 car./s ATAA ; 17 Netflix) ; si la somme dépasse le tiers de la durée du film, c'est une contradiction à dire au client ; (2) une technique découverte au labo dans la même journée ne peut pas porter seule une recommandation sans une pièce d'atelier qui la montre en mouvement.
- `montage-kinetic-editing` §6 : rushes à strobe (labo `strobe-rushes`) : mesurer chaque plan ; saccade choisie à la main = seule façon de garder le coup ; la moyenne et `deflicker` effacent ou échouent.
- BACKLOG 80 (pièce « La lumière écrit » : 10 s de saccade sur foule Blender + noms, juger « choix ou bug ») ; 81 (vrai son d'un stroboscope LED / xénon, sources) ; 82 (lecture de repérage dans une liste : sources de psychologie de la lecture, temps de recherche d'un nom connu).

## Correction après l'atelier 20 (même session)
- **Erreur de l'examen** : « un coup par noire = 2,13 flashs/s < 3 » ; mesuré sur la pièce 20 : **pire seconde 3**, la limite exacte (fenêtre glissante). Le traitement A doit passer aux noires pointées dans les mesures 4-7 (ce qui règle aussi le plancher de lecture de 16 images : 17,6 images par nom) et garder les noires seulement pour 2 mesures maximum, mesurées.
- **Erreur de l'examen** : « le nom apparaît dans le coup » en blanc : **invisible**. Il doit être noir dans le coup et s'inverser en blanc dans le noir (pièce 20 v4).
- La saccade automatique est exclue (v1 : aucun coup retenu sur 2,4 s). Note maintenue à 15/20 : l'examen a produit les bonnes questions, et l'atelier y a répondu le jour même ; mais deux erreurs de traitement sur six lignes de tableau.
