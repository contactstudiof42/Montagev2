# *La Haine* (Mathieu Kassovitz, 1995)

_Fiche ouverte le 2026-10-11 (phase 2, session 6), complétée en session 7. **État : terminée** (passe globale + 5 séquences + vérification de 9 plans longs). Source : WEB 1080p H.265 (1920×1040, SDR), VOF stéréo, sous-titres SDH français (1 288 répliques). **Noir et blanc** : pas de mesure de couleur ; luminance et contraste mesurés à la place. Aucune fiche de phase 1 sur ce film ni sur Kassovitz dans `culture/`. Planches commitées : `haine-courbes.png` (densité et volume du film entier), `haine-ouverture.png` (0:00-5:00), `haine-grunwalski.png` (50:30-54:10), `haine-mort-abdel.png` (84:40-87:40), `haine-fin.png` (89:40-93:37), `haine-coupe-escalier.png` (coupe cachée dans le noir, 14:18,5-14:21). Fichiers de travail : `videos/_travail/haine/` (tuiles dans `v/`)._

Skills relus avant l'analyse : `montage-rythme`, `montage-grammaire`, `montage-son-et-emotion`, `montage-couleur-et-intention`, grille de `montage-regard`.

## Intention
Une journée de 24 heures avec trois amis d'une cité, le lendemain d'une émeute, jusqu'au coup de feu final. Le film fait sentir **le temps qui passe sans que rien n'arrive, puis tout arrive en une minute**. Le montage le dit par deux moyens : des plans longs qui laissent traîner la journée, et une horloge affichée sur noir qui compte à rebours sans le dire.

## Forme [mesuré]
- **1 h 33 min 37 ; au moins 347 plans** (313 détectés par PySceneDetect, plus au moins 34 retrouvés à la vérification dans trois scènes sombres, voir plus bas). **ASL environ 16 s** ; la médiane des 313 plans détectés est 8,2 s, et **101 plans durent 15 s ou plus**. C'est le film le plus lent mesuré en phase 2 (Joker : médiane 4,5 s).
- **Densité presque toujours sous 10 coupes/min, souvent 0 à 4.** Deux crêtes seulement : **minute 3 (16/min)**, qui est le **générique monté sur des images d'archives d'émeutes** (Bob Marley, noms incrustés, plans de 2 à 14 s : leçon « un générique monté gonfle la densité ») ; et **minutes 85-86 (12 et 16/min)**, l'annonce de la mort d'Abdel puis la recherche de Vinz. La seule rafale de la fiction est donc **la mauvaise nouvelle**, pas le climax.
- **-19,9 LUFS intégrés.**
- **Treize cartons-horloge** (heure blanche au centre d'un noir, environ 3,8 s chacun) : 10:38 (5:15), 12:43, 14:12, 15:47, 17:04, 18:22, 20:17, 22:08, 00:33, 02:57, 04:27, 06:00, **06:01** (1:32:24). Entre deux cartons, l'histoire avance de 1 h 17 à 2 h 25 ; **le dernier n'avance que d'une minute**. En temps de film, les intervalles sont de 3 à 15 min pendant 80 minutes, puis 4,5, 4,6 et **1,7 min** : l'horloge se resserre à la fin sans que les plans raccourcissent. [VU SUR IMAGES, mesuré]

## Plans longs vérifiés (`verif_plan.py` + tuiles de 1 à 12 images/s)
| Début | Durée détectée | Résultat |
|---|---|---|
| 12:26 | 171,6 s | **deux plans** : coupe cachée à **14:19,9** dans la cage d'escalier. La caméra reste sur une vitre armée noire où Saïd disparaît, puis on coupe sur Saïd vu d'au-dessus, sortant d'une trappe sur le toit (`haine-coupe-escalier.png`). Donc **113,5 s** (la traversée de la cité) puis **57,7 s** (le toit). Le filé vers 15:09 n'en cache pas (vérifié image par image). Un tronc d'arbre passe devant l'objectif à 13:04 : coupe possible, **non tranchée** sur l'image (décor raccord des deux côtés). |
| 7:57 | 80,7 s | deux plans (coupe à 8:43). |
| 49:25 | 93,1 s | un plan (aucun pic) : Vinz et Hubert face à face dans les toilettes. |
| 51:06 / 51:55 | 49,2 / 34,7 s | un plan chacun : le vieil homme raconte Grunwalski. |
| 78:35 | 172,8 s | **au moins 27 plans** : le vol de voiture, de nuit, dans l'habitacle sombre (champ-contrechamp entre les trois). |
| 81:28 | 194,9 s | **9 plans** : un plan fixe de dos d'environ 91 s sur le toit face à Paris, deux gros plans, la tour Eiffel, l'affiche « Le monde est à vous », les escalators. |
| 1:29:53 | 50,4 s | 6 plans (gros plan du skinhead, plan large de nuit, deux plans du RER, carton). |
| 1:32:27,6 | 30,4 s | **un plan de 25,6 s** puis le noir (les « coupes » suivantes sont du bruit sur le noir). |

**Leçon** : le piège des scènes sombres est massif ici (un « plan » de 173 s en contenait 27). Dans un film noir et blanc de nuit, la médiane et le nombre de plans de PySceneDetect sont faux : passer `verif_plan.py` sur **tout** plan de plus de 60 s de nuit avant de citer un chiffre. Inscrit dans `PROMPT-PHASE-2.md`.

## Choix par domaine

### Rythme : le plan long est la norme, la coupe est l'événement
- Dans les cinq films de la vague 1, les plans longs étaient **réservés** à ce qui compte. Ici c'est l'inverse : **le plan long est la règle** (101 plans de 15 s ou plus) et **la rafale est l'exception qui signale**. Les deux seules rafales sont le réel d'archives (générique) et la mort d'Abdel apprise sur un mur d'écrans (1:24:58-1:26:03 : plans de 1,6 à 5 s, vignettes de télé en mosaïque, le visage d'Abdel en gros), puis la recherche de Vinz dans la gare (1:26:19-1:26:33 : sept plans de 0,8 à 2,3 s). Puis on revient à un plan de 68 s. [VU SUR IMAGES]
- **Le récit tenu, la réaction brève** (Grunwalski, 51:06-53:21) : le vieil homme raconte en plans de 49, 35 et 14 s ; les trois amis n'ont droit qu'à des contrechamps de 7 à 11 s. La chute de l'histoire (« il est mort de froid », 53:06) tombe dans un plan sur lui, la réaction (« pourquoi il nous raconte ça ? ») dans le plan suivant. Le montage refuse de couper pendant la parole de celui qui raconte. [VU SUR IMAGES]
- **Le plan suivi pour faire exister un lieu** (12:26-14:20) : 113 s de Steadicam pour traverser la cité avec les trois personnages, croiser d'autres jeunes, des policiers, et monter vers le toit. La coupe cachée dans le noir de la cage d'escalier relie deux plans suivis pour en faire un seul trajet : du sol au toit sans rupture visible. [VU SUR IMAGES]
- **Le climax n'est pas plus rapide** (comme 4 films sur 5 de la vague 1) : la fin (89:40-93:37) a une durée moyenne de plan de 16 s ; la dernière scène est un plan de 25,6 s.

### Son [mesuré, pas écouté]
- **Chaque carton-horloge est un trou de son** : -36 à -58 LUFS momentanés pendant le carton, contre -17 à -36 dans les 5 s avant. Treize fois sur treize. Le noir et le silence vont ensemble, comme une respiration forcée entre deux blocs de journée.
- **Le dernier carton (06:01) est précédé de silence** (-54 LUFS dans les 5 s avant, juste après le coup de feu qui tue Vinz) : c'est le seul carton où le silence commence avant le noir.
- **La fin est un crescendo continu de 30 LU en 25 s** : de -48 LUFS sur le carton à -17 au moment de la détonation (sous-titre « Détonation » à 1:32:53,7), qui tombe **sur le noir** ; on ne voit pas qui tire ni qui tombe. Le dernier plan avance lentement de l'affrontement Hubert / policier vers le visage de Saïd, qui ferme les yeux. La voix d'Hubert répète l'histoire de l'homme qui tombe (« jusqu'ici tout va bien »), entendue à l'ouverture sur noir (0:29-1:17) et au milieu sur le toit de Paris (82:53). La fable encadre le film.

### Image (noir et blanc) [mesuré]
- **Le noir est atteint dans tous les plans** (5e centile de luminance proche de 0 pendant tout le film) : la gamme est complète, le film n'est jamais laiteux.
- **La nuit n'est pas plus contrastée, elle est plus basse** : le jour de la cité (minutes 5 à 61) a une luminance moyenne de 30 à 50 et des hautes lumières à 70-100 ; la nuit de Paris (62 à 71) descend à 11-30 ; **le toit face à Paris (81-83) tombe à 0,4-5**, avec des hautes lumières à 12-27. Pendant les 91 s du plan fixe de dos, les quatre visages sont des silhouettes noires ; ce qui est éclairé, c'est la ville.
- Comparé au goût de Diego pour la nuit (« des visages sombres, mais avec un minimum de lumière sur l'info à voir », GOUTS.md) : ici, l'info est la ville et les voix, pas les visages. Kassovitz va plus loin que Diego, mais avec la même règle : la lumière va à ce qu'il faut voir. Ce rapprochement est mon interprétation, pas une parole de Diego.

### Typographie
- Un seul habillage, et il est structurel : l'heure en chasse fixe, petite, blanche, centrée sur noir, sans animation. Elle sert de métronome au film et de compte à rebours caché. Aucun carton décoratif. Ça confirme le constat des clips : **l'habillage vient du sujet** (ici, le temps).

## Ce qui confirme, contredit ou complète mes skills
- **Confirme** « le climax n'est pas plus rapide » et « l'après est tenu » (`montage-rythme`, bilan de la vague 1) : après la mort de Vinz, le silence, le carton, puis un plan de 25,6 s.
- **Complète** « les plans longs sont réservés à ce qui compte » : quand le plan long est la norme d'un film, **c'est la rafale qui devient le signal**. Le principe est le contraste, pas la longueur : ce qui compte, c'est ce qui sort de la règle que le film a installée. → `montage-rythme`.
- **Confirme** « le silence n'a de sens que s'il remplace un son appris » (`montage-son-et-emotion`, principe 3) : les treize cartons installent un silence régulier ; le dernier le déplace (le silence commence avant le noir).
- **Complète** « le silence ouvre ou clôt le sommet » : ici le sommet est **un crescendo continu qui finit sur le noir**, et le coup de feu est hors champ. → `montage-son-et-emotion`.
- **Confirme** la leçon des coupes cachées par le noir et l'occlusion (SDM, Interstellar) : coupe dans la cage d'escalier à 14:19,9. → `montage-grammaire` (la coupe dans le noir comme raccord de trajet).
- **Confirme** la leçon des scènes sombres, en plus grave (27 plans dans un « plan » de 173 s).

## Principes transférables
1. **Installer une norme, puis s'en écarter une fois** : un film en plans longs n'a besoin que d'une rafale pour frapper, et inversement. Pour Studio F42 (projets souvent énergiques) : dans un film rapide, un plan tenu fait le même effet que la rafale de *La Haine*.
2. **L'horloge sur noir comme structure** : un carton récurrent, sobre, accompagné d'un trou de son, découpe une durée et prépare la fin ; le resserrer à la fin (ici une minute) suffit à faire monter la tension sans accélérer le montage. Utilisable dans un film de marque ou un documentaire sur une journée.
3. **Raccorder deux plans suivis dans le noir** (une porte, une cage d'escalier, un dos) pour faire un trajet continu : utile pour un faux plan-séquence en corporate ou en clip.
4. **Le coup de feu sur le noir** : la montée continue du son, puis l'événement hors champ. Moins on montre le choc, plus le spectateur le fabrique.

## Ce que Diego en a dit
Rien sur ce film (aucune note dans `NOTES-DIEGO.md`).

## Reste incertain
- Le tronc d'arbre à 13:04 : coupe ou non (le plan suivi de la cité ferait alors 38 + 75 s).
- `coupes_parole.py` n'a pas été lancé : les scènes coupées dans le dialogue sont sombres (voiture) et leurs coupes ne sont pas dans `coupes.json`. À faire en passe de révision si utile.

## Révision (2026-10-11, session 10 de la phase 2)
- **Vérifiée, rien à changer** : aucun pourcentage de parole n'est cité (`coupes_parole.py` n'avait pas été lancé) ; aucune série de « plans » à la durée minimale (plus court plan détecté : 0,76 s) ; les deux crêtes de densité (générique d'archives, mort d'Abdel) avaient été regardées sur planche en session 7, et les plans longs de nuit recomptés avec `verif_plan.py`. La passe de révision n'apporte pas d'instrument nouveau à ce film.
