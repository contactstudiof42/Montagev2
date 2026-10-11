---
name: montage-couleur-et-intention
description: Couleur au service de l'émotion — choisir une palette et une intention d'étalonnage, un look, une ambiance de lumière ; doser contraste, saturation, température, peau ; décider si un teal & orange a un sens. Mots d'un réalisateur, d'un client ou d'un étalonneur : « quelle couleur pour ce film ? », « le look fait cheap », « c'est fade », « trop saturé », « je le veux plus chaud / plus froid / plus dense / laiteux / poisseux », « ça fait filtre ». Espaces couleur, log, LUT techniques : montage-couleur-pipeline.
---

# Couleur et intention

**Marqueurs** : [VU SUR IMAGES] mesuré ou vérifié sur de vraies vidéos (phase 2, `analyses/`) · [SOURCÉ] fiche ou source écrite · [THÉORIQUE] convention du métier non vérifiée ici · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette Blender / Pillow, hypothèse à confirmer sur de vraies images (phase 2).

**Fait foi sur** : le sens de la couleur et de la lumière (palette, look, teal & orange comme choix, peau, noir, blanc). **Ailleurs** : espaces, log, LUT, ordre des transformations, comment fabriquer un look → `montage-couleur-pipeline` ; capter la lumière au tournage (écrans, sources à éteindre, plaques allumée / éteinte) → `montage-preparation-tournage-vfx` ; nodes Resolve → `montage-resolve`.

Détail des maquettes et des fiches : [`details.md`](details.md). Sources : `culture/storaro-apocalypse-now-couleur.md`, `culture/christopher-doyle-wong-kar-wai.md`, `culture/roger-deakins-sicario-1917-blade-runner-2049.md`, Willis, Young / van Hoytema, Braier (`culture/`).

## Idée centrale
La couleur n'est pas une finition, c'est **un sens**. Avant de toucher une roue : « que doit ressentir le spectateur, et comment ça change du début à la fin ? ». Un look sans réponse est un filtre.

## Goût de l'utilisateur (`GOUTS.md` prime quand il s'applique) [SOURCÉ]
- **Look film par défaut (dicté le 2026-10-11)** : grain et look film quand ils racontent quelque chose, mais aussi **le choix par défaut de Diego quand il n'a pas d'idée ou doit livrer vite**. Sans demande de look du client et sans intention plus forte, un look film léger est donc le bon point de départ, pas un filtre à éviter.
- **Préférences dictées le 2026-10-10** : grain et **look film** par goût personnel (le client décide) ; la nuit, **visages sombres mais un minimum de lumière sur l'info à voir** ; Joker se juge comme **un ensemble** (couleur, lumière, corps, caméra) : ne jamais pousser un seul levier.
- **Joker** : garder la dominante « fausse » (fluos, sodium) qui raconte un lieu et un état, ne rendre juste que la peau ; faire **mériter** la couleur forte (une seule couleur lâchée à la bascule) ; lumières motivées. [VU SUR IMAGES] (mesuré sur le film, `analyses/films/joker.md`) : vert dominant pendant 95 min (maximum dans le métro), rouge saturé presque nul jusqu'au plateau de Murray (1:35) ; les seules touches rouges avant appartiennent à **des lieux de spectacle** (scène du club, théâtre) : la couleur méritée s'annonce par petites touches attachées à un lieu symbolique, puis le personnage la porte. L'image ne s'assombrit pas au fil du film ; la fin est claire et désaturée. La première vraie plage rouge est **un passage** : la lumière des coulisses de Pogo's (0:42:42), sur le chemin de la scène. À la fin, le vert n'est pas remplacé : il **passe du personnage au décor** (fumée bleu-vert de l'émeute) et le rouge prend le corps ; la couleur dominante change de place plutôt que de disparaître.
- **Whiplash** (sélection de la phase 2, pas un goût cité par Diego) : **deux mondes codés par la couleur**, l'ambre de la musique (tungstène, bois, cuivres) et le vert ou le neutre de la vie (dehors, famille, route). La chaleur monte avec l'obsession et le final est le passage le plus chaud et le plus saturé du film, **sans vert** (part de vert 0,06 contre 0,41 au début). [VU SUR IMAGES] (`analyses/films/whiplash.md`)
- **Spider-Man: Across the Spider-Verse** (sélection de la phase 2) : **une matière graphique par monde** (aquarelle rose et bleu pour Gwen, chaleur maximale pour Mumbattan, rouge et noir pour la Terre sans Spider-Man), ce qui rend lisibles des plans de 0,5 s dans le film le plus rapide du corpus (médiane 1,96 s) ; et **dans un seul monde, la couleur suit l'émotion plan par plan** (Gwen face à son père : rose pendant l'aveu, cyan quand il pointe son arme, les deux mélangés quand elle s'enfuit). Le monde du héros (Brooklyn) est le moins saturé. [VU SUR IMAGES, mesuré] (`analyses/films/spider-man-across-the-spider-verse.md`) Variante mémoire dans *Aftersun* : une texture par temps (MiniDV neutre à chaud, 35 mm des vacances, rave noire, présent de l'adulte le plus froid, rouge - bleu -17 à -25). [mesuré] (`analyses/films/aftersun.md`)
- **Ziak** (mesuré sur le clip réel) : luminance médiane 8/255, quasi monochrome froid, une seule couleur chaude sur 0,16 % de l'image dans 24 s sur 229. Le noir est la matière, la couleur un événement compté.
- **Projet Sony (2026-10-11) : la conversion technique n'est pas un look** [TESTÉ EN CONDITIONS RÉELLES]. Ma V2 (LUT Sony LC-709 TypeA seule, et des plans sombres **éclaircis** pour la lisibilité) : « catastrophique », « lumineuse, plate, sans contraste, c'est pas beau ». Claude nu, avec un simple CDL décidé (pente 1,30, noirs abaissés, gamma plus dense, saturation +35 %), a été jugé meilleur, « même si c'est pas pro ». Règles : un projet vendu comme « pro » porte un vrai look (contraste, noirs denses, palette choisie, même look sur tous les plans) ; il se fabrique sur 6 images avant le montage et se juge **en pleine résolution à côté des références** (`montage-regard`, « Juger sa propre version ») ; la lisibilité d'un plan sombre se règle sur l'info à voir (le visage, l'écouteur), pas en relevant tout le plan. Mesures des sept références réseaux de Diego : noirs (5e centile de luma) **5 à 11 sur 255** (60 pour un look laiteux voulu), contre 17 pour ma V2.
- **Proposition par défaut** quand le brief laisse le choix (hypothèse de goût) : images basses et denses, environnement froid, peau protégée, une seule chaleur réservée à des événements comptés. Jamais une recette plaquée.

## Ce que 45 vraies vidéos confirment (phase 2) [VU SUR IMAGES]
Mesuré sur une vignette toutes les 10 s par film (luminance, saturation, chaleur rouge - bleu), puis vérifié sur images extraites. Bilans : `archives/phase-2/RAPPORT-bilans-detailles-phase-2.md` (synthèse : `RAPPORT.md`).
1. **Une matière par monde est le principe de couleur le plus répandu du corpus** : dans au moins douze œuvres de toutes familles (*Interstellar*, *Whiplash*, *Mad Max*, *Spider-Verse*, *Aftersun*, *OSS 117*, *Forrest Gump*, HOUDI, Gare du Nord, adidas, « Conte de Noël », KAIZEN). Elle **rend lisibles des plans de 0,5 à 2 s** : on sait où l'on est avant de savoir ce qu'on voit. Le levier n'est pas que la teinte : **format d'image, support et texture** comptent autant (adidas : 4:3 chaud pour la légende, large et froid pour le présent ; *Aftersun* : MiniDV, 35 mm, rave noire, présent froid ; *OSS 117* : N&B pour 1945, nuit américaine bleue).
2. **La couleur forte se mérite et change de place** (*Joker* : rouge presque absent 95 min, annoncé par des lieux de spectacle, puis porté par le corps ; le vert passe au décor). Variantes : la couleur **voyage** sur toute la durée (6G du froid au chaud, STORM se refroidit) ; dans un seul monde, elle **suit l'émotion plan par plan** (*Spider-Verse*, Gwen et son père). Confirme « couleur d'accent = ressource rare » (maquette).
3. **Le monde de référence est le moins coloré** : Brooklyn, monde du héros de *Spider-Verse*, est le moins saturé ; *Spotlight* (saturation 0,26, la plus basse des films en couleur) efface l'image pour rendre l'enquête crédible. Le neutre est un choix, pas une absence.
4. **Une couleur peut ne rien raconter** : *Le Dîner de cons* garde un beige constant ; la comédie de dialogue mise tout sur le jeu. Ne pas exiger une courbe de couleur de chaque film.
5. **La nuit baisse plus qu'elle ne contraste** (*La Haine* : le noir est atteint partout, la nuit descend sans durcir ; *Mad Max* et *OSS 117* : la nuit est un bloc bleu, un monde de plus). Dans les trois, la lumière va à ce qu'il faut voir, ce qui rejoint la règle de nuit de l'utilisateur (rapprochement de ma part).
6. **La marque est une couleur ou un costume dès la première image**, son nom à la fin (sept pubs sur sept) ; un événement à plusieurs équipes se lit par **paquets de couleur** (GP Explorer 3), ce qui manquait à une commande du studio (Sephora : un signe de couleur par équipe, à prévoir au tournage).
7. **Une rafale tient en une seule couleur** (KAIZEN : l'entraînement en bleu ; Gare du Nord : 65 devantures de face à luminance voisine, conforme au contrôle de photosensibilité).
8. **Le souvenir passe par le support et le format** (maquette, pièce 08) : confirmé par *Aftersun*, adidas et les archives de *Forrest Gump*.
Pièges de mesure : une source HDR lue en SDR donne une image grise et des mesures fausses (vérifier `color_transfer`) ; une planche réduite en palette postérise les aplats saturés : juger la couleur fine sur une image extraite.

## Principes [SOURCÉ] (Storaro, Doyle / Wong, Deakins, Willis, Braier)
1. **Couleur = sens** : chaque dominante rattachée à un état ou un lieu (code personnel, pas universel) ; l'écrire dans la note d'intention.
2. **Palette réduite** : 1 dominante + 1 contrepoint + des neutres ; une palette se décide aussi **par exclusion** (nommer les couleurs interdites).
3. **Séparer par la teinte** autant que par la luminance (sujet / fond, réel / fantasme).
4. **La couleur évolue avec le récit** (or de l'enfance → gris de la prison).
5. **Retenue** : la couleur la plus forte est celle qu'on garde pour un moment ; laisser des noirs. Décider **quoi** garder dans le noir avant **combien** ; en post on ne crée pas ce noir, on le protège (10 bits au master ; le grain n'est pas une protection à l'encodage : `details.md`).
6. **Lumière motivée** : chaque couleur a une source plausible ; une source dans le champ n'est crédible que si elle **touche le visage et colore l'ombre**.
7. **La couleur dit ce que les personnages taisent** ; ne pas doubler ce que le texte dit.
8. **Décider avant de tourner** : décor, costume, gélatines, heure portent la palette ; l'étalonnage confirme, il ne sauve pas.

## Principes éprouvés en maquette [ÉPROUVÉ EN MAQUETTE]
- **Couleur d'accent = ressource rare** : une seule apparition au moment clé ; répétée, elle devient décor. (pièces 02, 03) **[VU SUR IMAGES]** : *Joker*, Ziak (une seule chaleur sur 0,16 % de l'image, 24 s sur 229).
- **La chaleur se tourne, l'étalonnage la protège** : la matière au décor **et** une clé au grade ; ce que le décor porte, toutes les directions en héritent. **Neutre ≠ froid** : annuler la dominante, ne pas ajouter du bleu. (pièce 05)
- **Le souvenir passe par le support et le format** (4:3, texture caméscope, chaleur modérée) plus que par la couleur ; refuser la date incrustée. (pièce 08) **[VU SUR IMAGES]** : *Aftersun* (MiniDV), adidas (4:3 chaud).
- **Chaleur partout** = « intime » si elle a une source et un dégradé, « filtre » si uniforme. **Un événement froid dans un monde chaud** : gélatiner la source plus bleue que nature ou une clé secondaire, sur une surface neutre ou habitée (main, visage) ; la saillance vient de la luminance. (pièce 10 v4 ; l'hypothèse « AgX blanchit le froid » est réfutée)
- **Le fond est attribué au monde, la lumière au corps** : refroidir le mur isole le personnage, refroidir sa lumière change son corps. Un fond froid réchauffe la peau perçue (logique et piège du teal & orange : pour une peau plus chaude, refroidir le fond). (pièce 13)
- **La température d'une source pratique change la matière** de ce qu'elle touche (peau → plâtre), plus que l'angoisse. (pièce 17)
- **Une lumière qui s'éteint** se lit par la lumière portée qui disparaît ; une courbe qui a une forme, pas un escalier ; un virage de teinte part d'au moins ~25 % de l'intensité finale. (pièce 18 ; capture : `montage-preparation-tournage-vfx`)
- **Blanc ou noir est un ton, pas un style** (tendre → blanc clinique ; funèbre → noir à lumière froide) ; dans le noir, le sujet devient la lumière ; le blanc pur se pose au grade (point blanc), pas au plateau. (pièce 22)
- **Infrarouge** : vert + bruit coloré = surveillance ; monochrome neutre, grain fin, noir ~3 % = intime. (pièce 23)
- **Descente de lumière** : ordonner les plans par leur luminance avant de graduer ; plancher au-dessus du noir, un dernier point vivant. (pièce 25)
- **Lumière, hauteur de caméra, corps** disent chacun une chose ; la transformation se lit quand les trois vont dans le même sens. (pièce 31)

## Méthode : du brief à l'intention couleur
1. **Émotion cible** en 2-3 mots ; sinon demander « à la fin, le spectateur doit se sentir comment ? ».
2. **Courbe** : état de départ → état d'arrivée (sans changement, la retenue compte double).
3. **Couleurs pivots** : une dominante par état ou lieu + un contrepoint, justifiés par le récit.
4. **Curseurs par état** : contraste, saturation, température, place de la peau.
5. **Contraintes** : charte, produit fidèle, diffusion, matière tournée.
6. **Intention** en une demi-page : 2-3 références **précises** (un plan), ce qu'on refuse.
7. **Tester sur 3 plans clés** (début, pic, fin), en mouvement et dans le montage.
8. **Si le client montre un plan de référence** (« je veux la colo de *Seven* ») : le look d'une référence vient d'abord de sa **prise de vue** (contre-jour, valeur du ciel, cadre) ; l'étalonnage rattrape la teinte, pas une densité perdue au tournage [VU SUR IMAGES, David Foxprod, `analyses/methodes/david-foxprod-look-seven.md`]. Le dire avant le tournage ; la méthode d'arbre est dans `montage-resolve` § 2 bis.

### Traduire les mots entendus [THÉORIQUE]
| Mot | Piste |
|---|---|
| « chaud », « humain » | ambre, peaux protégées, noirs légèrement relevés |
| « froid », « clinique » | blancs neutres à bleutés, saturation basse, contraste net |
| « dense », « riche » | noirs profonds, saturation localisée sur la dominante |
| « laiteux », « nostalgique » | noirs relevés, hautes lumières compressées, légère chaleur |
| « poisseux », « malade » | dominante vert-jaune, peaux tirées vers la teinte |
| « ça fait cheap » | trop de teintes, peaux incohérentes, saturation uniforme, lumière sans source |
| « c'est fade » | pas de contrepoint, plutôt qu'un manque de saturation |

## Clichés à refuser (sauf intention explicite)
- **Teal & orange par défaut** : ne dit rien et date l'image ; seulement si chaud / froid porte un sens (dosage et vectorscope : `montage-couleur-pipeline`).
- LUT « cinématique » plaquée ; désaturer pour faire « sérieux » ; saturer pour faire « joyeux » ; néons rose / cyan sans raison ; noirs relevés « vintage » partout ; une couleur par plan ; étalonner pour sauver un plan sans source crédible.

## Format de sortie (« quelle couleur pour ce film ? »)
1. Émotion et courbe (2 lignes) ; 2. palette avec la raison de chaque couleur ; 3. curseurs par état ; 4. 2-3 références précises ; 5. ce qu'on refuse ; 6. un risque et son test (3 plans).

## Limites
Les significations varient selon cultures et marques ; en format court, la courbe se réduit souvent à un seul basculement ; les principes « éprouvés en maquette » sur la lumière (source, gélatine, descente, infrarouge) restent à voir sur de vrais rushes : la phase 2 a mesuré des films finis, pas des tournages ; la peau n'a pas été mesurée.
