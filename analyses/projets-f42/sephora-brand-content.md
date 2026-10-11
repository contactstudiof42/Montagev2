# Sephora × Laneige — brand content vertical « The Bounce Lab »

_Fiche ouverte le 2026-10-11 (phase 2, session 6, projet Studio F42 n°5). **État : complète** (vue en entier à 1 image / 2 s, six images pleine définition, coupes par deux outils, loudness et true peak sur le fichier livré, transcription Whisper lue). Source : `SEPHORA BRAND CONTENT.mov`, HEVC 1080×1920, 25 i/s, 2 min 45,9, AAC stéréo. Les prénoms viennent des cartons et de la transcription ; je ne cherche rien sur les personnes. Pas de rushes._

**Lu avant l'analyse** : `A-LIRE.md`, `montage-regard` (grille), `montage-formats` (vertical), `montage-kinetic-editing` (captions, hook), `montage-youtube` 16 ter et 16 quinquies (plateau de jeu, talk-show : le système de série, couper sur la réaction), fiches « Qui est l'imposteur » et « POPCORN ». Aucun commentaire de Diego.

## Intention et contraintes probables
- **Intention** : présenter le nouveau sérum « Bouncy & Firm » de Laneige, vendu chez Sephora, par **un jeu entre créateurs** : deux duos (une créatrice et son abonnée, un créateur et son abonnée) en blouses de labo dans un décor rose (« The Bounce Lab »), deux manches de vrai / faux sur les ingrédients, des gagnants qui repartent avec la gamme. Le jeu fait passer l'information produit (peptides, niacinamide, capsules, cinq produits).
- **Contraintes probables** [DÉDUIT] : un décor de marque fourni ou construit pour l'événement, quatre personnes non comédiennes, plusieurs caméras ou une caméra mobile, un tournage court, des messages produit imposés, une diffusion sur les comptes des créateurs et de la marque (vertical).

## Forme [mesuré, VU SUR IMAGES]
- **2 min 46, 73 plans (PySceneDetect) à 82 changements (`verif_plan.py`, qui compte aussi les cartons et la transition tournoyante) ; médiane 2,0 s ; 14 plans de moins de 1 s.** Densité **décroissante** : 33, puis 24, puis 15 coupes/min.
- **Structure** : accroche (0:00-0:09, « On peut tricher ? … le visage du non-fair-play ») → produit et logo bulle « THE BOUNCE LAB — LANEIGE × SEPHORA » (0:08-0:12) → présentations (0:10-0:27) → règles (0:27-0:45) → **manche 1** (carton « MANCHE 1 — ANNA & TIPHAINE », 0:45-1:20) → **manche 2** (transition tournoyante, 1:22-1:58) avec l'accusation de triche (1:46-1:52) → « LE GAGNANT EST… » (1:58) → **le lot** : sac Sephora « Click & Collect », puis les quatre produits en packshots doux (2:06-2:30) → applaudissements, noir.
- **Habillage** : score en pastilles et points d'interrogation au néon en haut du cadre ; cartons de manche sur le décor flouté ; **sous-titres fins, blancs, sans contour**.
- **Son** : -17,1 LUFS intégrés, LRA 7,0 LU, **true peak -0,1 dBTP**.

## Ce qui marche (avec la preuve)
1. **L'accroche est un conflit pris plus loin dans le film** : « On peut tricher ? », puis « le visage du non-fair-play » (0:00-0:09), qui annonce l'accusation de triche de 1:46. C'est le « ouvrir par la fin » des docs YouTube (Ygg, CIA) appliqué au jeu, et ça tient le spectateur jusqu'à la manche 2. [VU SUR IMAGES, transcription]
2. **Le jeu porte l'information produit** : chaque question est un argument de vente (« Les peptides aident à raffermir la peau ? », « environ 24 000 capsules »). On apprend le produit en jouant ; c'est le principe « le gag porte le bénéfice » transposé au brand content. [transcription]
3. **Un décor de marque cohérent** : rose, blanc, néons, flacons, logo « The Bounce Lab » dans l'arche, blouses de labo ; la marque est un lieu, comme dans les pubs de référence. [VU SUR IMAGES]
4. **Les manches sont marquées par des cartons et une transition** (« MANCHE 1 — ANNA & TIPHAINE » sur le décor flouté ; tourbillon avant la manche 2 ; « LE GAGNANT EST… ») : la structure du jeu se lit sans le son. Même système que les formats de plateau YouTube (`montage-youtube` 16 ter). [VU SUR IMAGES]
5. **La densité baisse vers le lot** (33 → 24 → 15 coupes/min) : les produits finissent en packshots tenus, lumière douce (2:10-2:30). Le film se pose sur ce qu'il vend. [mesuré]

## Ce qui pourrait être meilleur, et comment
### Montage et finition (corrigeable avec les mêmes rushes)
1. **Les sous-titres sont presque illisibles** : police fine, blanche, sans contour, sur un décor rose clair et des blouses blanches (« On peut tricher ? » à 0:00 ; « Mouais ! » sur le comptoir à 2:43) ; contraste estimé à 2,5:1 au mieux (mesure grossière sur une zone), loin du 4,5:1. En vertical, muet par défaut, **l'accroche est perdue sans le son**. C'est le défaut principal du film. Correction : police grasse, contour ou ombre, ou pavé coloré derrière le mot (`montage-kinetic-editing` : plancher de lisibilité après ré-encodage).
2. **45 s avant la première question** (présentations 0:10-0:27, règles 0:27-0:45). En vertical, c'est le passage où l'on perd le plus de spectateurs. Les présentations peuvent passer en cartons-noms sur les plans d'entrée, les règles en une phrase (« vrai ou faux, deux catégories ») : première question vers 0:20-0:25.
3. **True peak -0,1 dBTP** et **-17,1 LUFS** : trop bas pour le réseau (Instagram ne remonte pas un son faible) et crêtes trop hautes. Normaliser à -14 LUFS avec un limiteur à -1 dBTP. **Les cinq fichiers du studio vus jusqu'ici sont tous au-dessus de -1 dBTP** (Benefit -0,6 et 0,0 ; Oney +3,1 ; Swile -0,8 ; Sephora -0,1).
4. **2 min 46 pour un Reels** : la manche 1 (35 s) et la manche 2 (36 s) ont la même forme. Une version courte (45-60 s : accroche, une manche, la triche, le lot) servirait les comptes des créateurs ; la version longue peut rester pour la marque [DÉDUIT : je ne connais pas le plan de diffusion].

### Tournage (à préparer autrement la prochaine fois)
1. **Quatre blouses blanches sur fond rose** : les deux équipes ne se distinguent que par les visages. Un détail de couleur par équipe (badge, lunettes, brassard, côté du comptoir tenu) rend le jeu lisible en un coup d'œil, comme le costume unique des candidats d'« Imposteur ».
2. **Le rose partout** (décor, produits, cartons) écrase la hiérarchie : le packshot du sérum (rose pâle sur rose) ressort peu. Prévoir un fond plus sombre ou plus neutre pour les inserts produit.

## Grille (`montage-regard`, 0 à 3)
| Critère | Note | Preuve |
|---|---|---|
| Intention | 3 | jeu compris, produit appris par les questions |
| Lisibilité | 1 | sous-titres fins à ~2,5:1 ; équipes indistinctes |
| Liaison | 2 | cartons de manche, tourbillon ; présentations sans lien |
| Rythme | 2 | 45 s avant le jeu ; densité qui se pose bien sur le lot |
| Composition | 2 | plans à deux centrés, lisibles ; packshots rose sur rose |
| Cohérence | 3 | décor, blouses, néons, cartons dans la même langue |
| Couleur | 2 | rose monochrome : marque forte, hiérarchie faible |
| Mouvement | 2 | transition tournoyante, pastilles de score |
| Originalité | 2 | le jeu entre créateurs et abonnés est un bon dispositif ; habillage courant |
| Justesse | 2 | deux manches identiques ; règles longues |

**Verdict** : **pas livrable en l'état pour un usage muet** (lisibilité à 1, à cause des sous-titres) ; corrigeable au montage en une passe (sous-titres, son, ouverture raccourcie).

## Confirme, contredit, complète
- **Confirme** sur un projet du studio la règle des formats de plateau YouTube (`montage-youtube` 16 ter : un système, des cartons de manche, couper sur la réaction) et l'accroche par un conflit pris plus loin (Ygg, CIA).
- **Confirme** `montage-formats` (vertical, muet par défaut) **en négatif** : sous-titres illisibles = accroche perdue.
- **Complète** : dans un jeu de marque, **les questions sont le message produit** ; c'est la forme la plus naturelle du brand content d'information.

## Principes transférables (pour le studio)
1. **Ouvrir un jeu par son conflit** (la triche), pas par ses règles.
2. **Faire du message produit la matière du jeu** (questions vrai / faux sur la formule).
3. **Un signe de couleur par équipe**, dès le tournage.
4. **Sous-titres de réseau : gras, contour, contraste mesuré** ; jamais fins et blancs sur fond clair.
5. **Une version courte par compte de créateur**, la longue pour la marque.

## Ce que Diego en a dit
Rien sur ce projet (titre seulement dans `NOTES-DIEGO.md`).
