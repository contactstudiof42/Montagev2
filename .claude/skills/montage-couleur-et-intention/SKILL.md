---
name: montage-couleur-et-intention
description: Couleur au service de l'émotion — choisir une palette et une intention d'étalonnage, un look, une ambiance de lumière ; doser contraste, saturation, température, peau ; décider si un teal & orange a un sens. Mots d'un réalisateur, d'un client ou d'un étalonneur : « quelle couleur pour ce film ? », « le look fait cheap », « c'est fade », « trop saturé », « je le veux plus chaud / plus froid / plus dense / laiteux / poisseux », « ça fait filtre ». Espaces couleur, log, LUT techniques : montage-couleur-pipeline.
---

# Couleur et intention

**Marqueurs** : [SOURCÉ] fiche ou source écrite · [THÉORIQUE] convention du métier non vérifiée ici · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette Blender / Pillow, hypothèse à confirmer sur de vraies images (phase 2).

**Fait foi sur** : le sens de la couleur et de la lumière (palette, look, teal & orange comme choix, peau, noir, blanc). **Ailleurs** : espaces, log, LUT, ordre des transformations, comment fabriquer un look → `montage-couleur-pipeline` ; capter la lumière au tournage (écrans, sources à éteindre, plaques allumée / éteinte) → `montage-preparation-tournage-vfx` ; nodes Resolve → `montage-resolve`.

Détail des maquettes et des fiches : [`details.md`](details.md). Sources : `culture/storaro-apocalypse-now-couleur.md`, `culture/christopher-doyle-wong-kar-wai.md`, `culture/roger-deakins-sicario-1917-blade-runner-2049.md`, Willis, Young / van Hoytema, Braier (`culture/`).

## Idée centrale
La couleur n'est pas une finition, c'est **un sens**. Avant de toucher une roue : « que doit ressentir le spectateur, et comment ça change du début à la fin ? ». Un look sans réponse est un filtre.

## Goût de l'utilisateur (`GOUTS.md` prime quand il s'applique) [SOURCÉ]
- **Joker** : garder la dominante « fausse » (fluos, sodium) qui raconte un lieu et un état, ne rendre juste que la peau ; faire **mériter** la couleur forte (une seule couleur lâchée à la bascule) ; lumières motivées.
- **Ziak** (mesuré sur le clip réel) : luminance médiane 8/255, quasi monochrome froid, une seule couleur chaude sur 0,16 % de l'image dans 24 s sur 229. Le noir est la matière, la couleur un événement compté.
- **Proposition par défaut** quand le brief laisse le choix (hypothèse de goût) : images basses et denses, environnement froid, peau protégée, une seule chaleur réservée à des événements comptés. Jamais une recette plaquée.

## Principes [SOURCÉ] (Storaro, Doyle / Wong, Deakins, Willis, Braier)
1. **Couleur = sens** : chaque dominante rattachée à un état ou un lieu (code personnel, pas universel) ; l'écrire dans la note d'intention.
2. **Palette réduite** : 1 dominante + 1 contrepoint + des neutres ; une palette se décide aussi **par exclusion** (nommer les couleurs interdites).
3. **Séparer par la teinte** autant que par la luminance (sujet / fond, réel / fantasme).
4. **La couleur évolue avec le récit** (or de l'enfance → gris de la prison).
5. **Retenue** : la couleur la plus forte est celle qu'on garde pour un moment ; laisser des noirs. Décider **quoi** garder dans le noir avant **combien** ; en post on ne crée pas ce noir, on le protège.
6. **Lumière motivée** : chaque couleur a une source plausible ; une source dans le champ n'est crédible que si elle **touche le visage et colore l'ombre**.
7. **La couleur dit ce que les personnages taisent** ; ne pas doubler ce que le texte dit.
8. **Décider avant de tourner** : décor, costume, gélatines, heure portent la palette ; l'étalonnage confirme, il ne sauve pas.

## Principes éprouvés en maquette [ÉPROUVÉ EN MAQUETTE]
- **Couleur d'accent = ressource rare** : une seule apparition au moment clé ; répétée, elle devient décor. (pièces 02, 03)
- **La chaleur se tourne, l'étalonnage la protège** : la matière au décor **et** une clé au grade ; ce que le décor porte, toutes les directions en héritent. **Neutre ≠ froid** : annuler la dominante, ne pas ajouter du bleu. (pièce 05)
- **Le souvenir passe par le support et le format** (4:3, texture caméscope, chaleur modérée) plus que par la couleur ; refuser la date incrustée. (pièce 08)
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
Les significations varient selon cultures et marques ; en format court, la courbe se réduit souvent à un seul basculement ; tous les principes « éprouvés en maquette » restent à voir sur de vrais rushes.
