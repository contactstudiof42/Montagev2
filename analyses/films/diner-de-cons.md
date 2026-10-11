# Le Dîner de cons (Francis Veber, 1998) — montage Georges Klotz

_Fiche ouverte le 2026-10-11 (phase 2, session 2, film vague 1 n°4). **État : terminée** (passe globale, 4 séquences, coupes contre la parole, trois chutes mesurées une à une). Source : Blu-ray 1080p (1920×822, SDR), VF d'origine AC3, aucun sous-titre texte : transcription Whisper (large-v3-turbo) dans `videos/_travail/diner/sous-titres.srt`. Planches commitées : `diner-de-cons-courbes.png`, `diner-de-cons-couleur.png`, puis une image par plan avec le volume momentané en dessous : `diner-de-cons-ouverture.png` (0:03:20-0:08), `diner-de-cons-leblanc.png` (0:30:20-0:35), `diner-de-cons-cheval.png` (0:53-0:58), `diner-de-cons-final.png` (1:12:50-1:17:40)._

**Lu avant l'analyse** : `culture/timing-comique-sitcom.md` (dont Kaamelott : dialogue frontal, deux caméras), `culture/gags-de-montage.md`, `montage-rythme` (timing comique), `montage-grammaire` (champ-contrechamp, couper sur la réaction), grille de `montage-regard`. Le film est une pièce de théâtre adaptée (Veber, 1993).

## Intention
Faire rire d'un piège qui se retourne : celui qui voulait se moquer d'un « con » se fait démolir par lui en une soirée, puis le film retourne la sympathie vers le con. [DÉDUIT]

## Forme [VU SUR IMAGES, mesures automatiques]
- **1 h 20 min, au moins 1 051 plans, ASL 4,6 s, médiane 3,0 s.** Histogramme : < 1 s : 38 · 1-2 s : 241 · 2-4 s : 384 · 4-8 s : 255 · 8-15 s : 96 · ≥ 15 s : 37. **Une pièce de théâtre en un décor, montée plus vite que Joker** (médiane 4,5 s), mais avec très peu de plans de moins d'une seconde (38, contre 226 dans Whiplash) : le rythme vient du dialogue, pas des inserts.
- **Densité de coupes plate** : 10 à 20 coupes/min du début à la fin, sans montée vers un climax. Le film avance au tempo des répliques.
- **Son très plat** : -24,8 LUFS intégrés, environ -32 LUFS momentané en médiane pendant tout le huis clos (0:10-1:17). La musique n'est que dans l'ouverture et le générique de fin (-19 à -21 LUFS).
- **Couleur constante** : un appartement beige et chaud, lumineux (luminance 84), peu saturé (0,37), presque sans vert. Aucune évolution sur le film : la couleur ne raconte rien, elle installe un salon bourgeois.

## Séquences analysées

### L'ouverture (0:03:14-0:08) [VU SUR IMAGES, `diner-de-cons-ouverture.png`]
- Le « con » du train (le maquettiste en allumettes) : champ-contrechamp dans le compartiment, 0,7 à 6 s, inserts du TGV et des photos des maquettes. Le gag est dans la répétition (« Vous en avez d'autres ? »).
- Le générique est **dessiné** (des assiettes, des verres, des visages dans les assiettes), monté sur une chanson connue sur la bêtise dont les paroles posent le thème. Un plan de 22,4 s sur le titre.

### Le coup de fil à Juste Leblanc (0:30:20-0:35) [VU SUR IMAGES, `diner-de-cons-leblanc.png`]
- 68 plans, durée moyenne 4,2 s. Trois sortes de plans : Pignon au téléphone (plan rapproché), Brochant qui écoute (gros plan de réaction), et **le plan à deux sur le canapé**. Leblanc, chez lui, n'a que trois plans de coupe (2 à 4,5 s).
- **Les gaffes se jouent en plan à deux tenu** : 12,3 s (« C'est quoi son numéro ? »), 14,6 s (le début de l'appel), **15,4 s sur la gaffe** (0:33:57, « Ah oui, j'ai fait la boulette » ; vérifié, continu). Le gaffeur et sa victime sont dans le même cadre : on voit la cause et l'effet en même temps.
- Les réactions de Brochant sont isolées en gros plans courts (1 à 3 s) **après** la gaffe, jamais pendant.

### Cheval, le contrôleur fiscal (0:53-0:58) [VU SUR IMAGES, `diner-de-cons-cheval.png`]
- 55 plans, durée moyenne 5,5 s.
- **Le gag du vin tient dans un plan fixe frontal de 37,5 s** (0:54:36, vérifié : continu) : Cheval à gauche, Brochant au centre, Pignon à droite, alignés face à la caméra comme sur une scène. Puis 20,8 s (« Lucien, à cheval ») et 16 s : les gags de situation sont tenus en plans à trois.
- Les échanges verbaux rapides passent en champ-contrechamp (1 à 4 s).

### Le coup de fil final de Pignon à Christine (1:12:50-1:17:40) [VU SUR IMAGES, `diner-de-cons-final.png`]
- 50 plans, **durée moyenne 6,2 s, deux fois la médiane du film**. La tirade sincère de Pignon est tenue en gros plans de **32,7 s** (1:14:41) et **28,2 s** (1:16:03), vérifiés : continus. Christine à l'hôpital en contrechamp (4 à 14 s).
- Le film se termine par un plan large de 28,5 s (1:17:32) : la dernière gaffe et la réaction en un seul cadre.

## Où tombent les coupes par rapport à la parole [mesuré, `labo/outils/coupes_parole.py`, énergie de la voix par 20 ms]
| Passage | Coupes | Pendant la parole | Air depuis la fin de la réplique (quartiles) | Jusqu'à la reprise (quartiles) |
|---|---|---|---|---|
| huis clos 0:10-0:30 | 279 | **40 %** | 0,15 / 0,34 / 0,57 s | 0,20 / 0,42 / 0,83 s |
| coup de fil à Leblanc | 67 | **43 %** | 0,21 / 0,37 / 0,61 s | 0,24 / 0,34 / 0,76 s |
| Cheval | 54 | **44 %** | 0,21 / 0,43 / 0,73 s | 0,17 / 0,37 / 1,12 s |
| coup de fil final (sincère) | 47 | **21 %** | 0,28 / 0,48 / 0,94 s | 0,28 / 0,76 / 1,80 s |
- **Dans les scènes comiques, quatre coupes sur dix tombent pendant que quelqu'un parle** (réaction prise sur la réplique, chevauchement). Les autres tombent dans des silences très courts : environ **0,35 s après la fin de la réplique**, à peu près au milieu d'un trou de 0,8 s. Il n'y a presque jamais d'air.
- **Dans la scène sincère, deux fois moins de coupes sur la parole**, et plus d'air autour (la reprise vient 0,76 s après la coupe en médiane, 1,8 s au troisième quartile).
- **Trois chutes mesurées une à une** (énergie de la voix par 100 ms, une image toutes les 0,5 s) [VU SUR IMAGES, mesuré] :
  - « il n'a pas de prénom » (0:31:07) : la chute est dite **dans le plan à deux**, la coupe vers le gros plan de réaction de Brochant tombe environ 0,5 s après la fin de la réplique ;
  - « Cheval en vin ? Ah oui, il s'y connaît » (0:54:14) : pendant la chute, on est **sur Cheval, la victime**, et son visage reste environ **2,5 s en silence** avant la coupe (0:54:19) ;
  - « C'est le con de votre mari » (1:14:01) : la chute est dite **sur le visage de Pignon** (on voit les yeux de celui qui la dit), coupe 0,4 s après vers Brochant debout (1,5 s), puis retour.
- **Nuance l'estimation de phase 1** (`culture/timing-comique-sitcom.md`, « 1 à 3 s après la chute ») : elle est juste **pour les chutes**, à condition que l'air soit sur un visage qui encaisse ; elle est fausse pour le dialogue courant, où le film ne laisse presque aucun air (0,35 s en médiane).

## Confirme, contredit, complète
- **Confirme** `culture/timing-comique-sitcom.md` (Kaamelott) : dialogue frontal, peu de valeurs de plan, un plan à deux pour situer. **Complète** : les **gags de situation** (la gaffe, le vin) sont tenus en plan à deux ou à trois (12 à 37 s), les **échanges verbaux** en champ-contrechamp rapide (1 à 4 s), et la réaction isolée vient **après** la chute.
- **Confirme**, sur un quatrième film et dans un autre genre, la règle des plans longs : **quand le personnage est sincère** (la tirade de Pignon), le plan tient (28 à 33 s) alors que le film coupe toutes les 3 s.
- **Complète** `montage-rythme` : une comédie de dialogue peut avoir une densité de coupes **plate du début à la fin** ; le rythme est celui des répliques, pas une forme qui monte.
- Ne dit rien sur la couleur : elle ne raconte rien ici, et c'est juste pour une comédie de huis clos.

## Principes transférables
1. **La gaffe en plan à deux** : cause et effet dans le même cadre ; la réaction isolée après, pas pendant.
2. **Le gag de situation en plan fixe frontal à plusieurs** : quand le public en sait plus que les personnages, on lui laisse tout le monde dans le cadre.
3. **Couper vite la parole, tenir la sincérité** : dans une comédie, le moment vrai se reconnaît à la durée du plan.
4. **Pas d'air dans le dialogue, de l'air sur la chute** : couper environ 0,35 s après une réplique courante (ou pendant, sur la réaction) ; après une chute, couper vers la réaction 0,4 à 0,5 s après et la tenir 1,5 à 3 s en silence.

## Ce que Diego en a dit
Rien pour l'instant (`GOUTS.md`, `NOTES-DIEGO.md`, `RETOURS-DIEGO.md`).

## Pas fait
- L'arrivée de Pignon (vers 0:14-0:20) et la chute de « la boulette » mesurée image par image.

## Doutes
- La transcription Whisper n'est pas vérifiée ligne à ligne ; elle a transcrit aussi les paroles de la chanson du générique.
- Un plan fixe de 37 s peut cacher une coupe de raccord dans l'axe ; `verif_plan.py` et une tuile toutes les 3 s n'en montrent pas.
