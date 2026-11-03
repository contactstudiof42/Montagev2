Annexe de `SKILL.md` : mesures, sources et détail des maquettes de montage-preparation-tournage-vfx ; les principes ne sont pas répétés ici (le SKILL.md fait foi).

# Préparer un tournage pour les effets : détails

Les pièces numérotées (`atelier/NN-*/`) sont des maquettes Blender / Pillow / ffmpeg : à confirmer sur un vrai plateau et de vrais rushes (phase 2). Nuit infrarouge : `infrarouge.md`.

## §5 Effacer une source de lumière (examen n°7, session 12)
- Un lampadaire retiré laisse son halo sur le sol, les murs, les visages ; si quelqu'un passe dessous, c'est une relumière complète [THÉORIQUE]. Source contrôlée = faux lampadaire (un tube sur un mât, une lampe de chantier). Pour l'effacement : plan fixe sur pied + plaque propre longue.
- Courbe selon la technologie (corrigé session 12) [SOURCÉ] : à **l'extinction**, LED comme lampe à décharge s'éteignent presque instantanément (pour la décharge : déduit, l'arc cesse avec le courant) ; la différence est à **l'allumage** : le sodium haute pression change de couleur à mesure que le sodium se vaporise, et une lampe chaude coupée attend que le gaz refroidisse. En post, un rallumage « sodium » crédible est donc lent et change de teinte. Sources : PSU EGEE 102 https://courses.ems.psu.edu/egee102/node/2366 ; Maréchal https://marechal.com/en/p-hps-lamps-and-power-failure.html ; DIALux https://dialux4.support-en.dial.de/support/solutions/articles/9000078324-restriking.
- Pièce 18 (Blender) [ÉPROUVÉ EN MAQUETTE] : les sources lointaines partent sans qu'on le voie (−4 % de luminance). Part de chaque source mesurée depuis la caméra (les allumer une par une devant le moniteur, ou `atelier/18-soustraction/part.py` en 3D) : en cadrage serré, le lampadaire « proche » ne pesait que 2 %, son voisin 41 %.

## §5 ter Une lumière qui s'éteint à l'écran (pièce 18 v4-v5, `atelier/18-soustraction/anime.py`) [ÉPROUVÉ EN MAQUETTE] (rendu 3D ; au tournage : THÉORIQUE)
- Plaques : même diaphragme aussi ; linéariser = rush log → linéaire ; la lumière s'additionne, donc toute courbe (sèche, panne, rallumage lent avec virage de teinte) se compose sans refaire la prise. Seul le comédien peut bouger entre les plaques, s'il est détouré ; une partie saturée ne s'additionne plus.
- Cause de l'extinction : prévoir le plan ou le son qui la donne.
- Gestes (pièce 19) : en plan moyen, il faut un geste très ample (v7) ; serrer en gardant les mains dans le cadre est l'alternative probable (non démontrée, v8).

## §5 quater Coupe cachée par un cache (pièce 30, `atelier/30-coupe-cachee/`) [ÉPROUVÉ EN MAQUETTE] (maquette 2D ; THÉORIQUE au tournage)
- Si l'effet voulu est la comparaison (avant / après, humour), la coupe sèche dans le même cadre : à décider avant le tournage.
- L'objet d'arrivée est souvent plus grand (il dépasse par le haut). Marge de flou de bougé ≥ vitesse du cache × durée d'obturation (un torchon à 18 px/image en 180° : 9 px de bord semi-transparent ; mesuré, pièce 30 I).
- À figer ou retirer hors du cache : horloge, écran allumé, figurant, lumière du jour (préférer le studio ou des prises rapprochées) ; 6 % de variation de lumière suffisent à trahir la coupe (mesuré). Noter l'image exacte de couverture maximale.
- Contrôle : score de coupe ≈ bruit (scdet ≤ 1) **et** écart hors objet avant / après ≈ écart entre deux images d'une même prise (`mesure.py`). Un cache plein cadre trompe le détecteur mais pas l'œil si la lumière a bougé.
- Devis de rattrapage (pièce 30 G-H) : lumière qui bouge = un gain d'étalonnage, caméra qui bouge = une stabilisation (à elles deux −62 % de l'écart) ; élément vivant = une roto et une plaque propre, alors que le retirer au tournage ne coûte rien.

## Flou optique, reflet, ombres (pièce 28, `atelier/28-flou-net/CRITIQUE.md`) [ÉPROUVÉ EN MAQUETTE] (rendus Blender Cycles)
- Choisir disques ou tache grise selon l'émotion (rêverie contre malaise). Le flou optique dépend de la distance (près et loin échangent leur netteté) : il garde la profondeur et le point de vue ; le gaussien aplatit.
- Plage perceptive mesurée : en 50 mm f/1.4 sur un sujet à 30-60 m, silhouette → lisible entre ~1,5 et 15 m ; faire le point sur le premier plan efface complètement le sujet. v2 (40 rendus) : presque tout le changement visible tient en 1,5 → 5-8 m ; une course linéaire de 15 s laisse 8 s de temps mort, le geste naturel du pointeur (rapide puis pose) 12 s ; programmer ~80 % de la durée sur la plage silhouette → lisible.
- Mesure : la variance du laplacien ne dit rien de la lisibilité d'une forme (elle sature à 2 px).
- Reflet (v3) : visage éclairé côté vitre ; à −5 diaph et plus, le paysage s'éteint. Point simultané visage-reflet (~0,9 m) et paysage (30 m+) : impossible en 50 mm (f/48), possible en 24 mm f/11.
- Ombres qui défilent (v4, `flash_check.py`) : lisière de forêt vue d'un train à 100 km/h (troncs tous les 5 m ≈ 5,6 Hz) = échec photosensibilité même avec une ombre douce ; à 40 km/h, limite.
- Flou par support (v5) : régler la courbe de mise au point par support, ou tourner une prise plus floue pour la déclinaison mobile.

## Buée sur les vitres (pièce 34) [THÉORIQUE] (plateau) ; [ÉPROUVÉ EN MAQUETTE] (effet, Blender)
- Intention : une buée qui monte est un compteur (le temps passé, le souffle) et un rideau (pudeur) ; elle doit croître de façon lisible et rester raccord.
- Au plateau : vitres refroidies, moteur coupé, vaporisateur entre les prises ; photo du pare-brise à chaque prise. En post : plaque embuée « à fond » (la maquette fait de même avec deux rendus).
- La buée diffuse la lumière intérieure : une liseuse allumée dans une voiture embuée en fait une lanterne (prévoir une source chaude réglable dans l'habitacle).

## Axe de lecture d'un corps (pièce 31 v4) [ÉPROUVÉ EN MAQUETTE]
Solutions de repérage dans un lieu étroit : escalier ouvert d'un côté, mur démontable en studio, focale longue depuis un palier ; sans elles, la posture voulue est illisible et aucun montage ne la rattrape. Voir `montage-regard` (31).

## §5 bis Écrans dans le champ : sources
Consultées le 2026-10-10, par résumés de recherche : https://www.premiumbeat.com/blog/5-tips-for-shooting-digital-screens ; https://www.zerovfx.com/tips/how-to-shoot-monitor-composites ; https://forum.logik.tv/t/screen-replacement-advice-for-producers/1773

## Stabiliser au tournage ou en post : matériel et pratique au 2026-11-03 [SOURCÉ] (veille, aucun essai ici)
Question de Diego : faut-il un gimbal, ou Gyroflow à main levée suffit-il ? Sources datées ; rien n'est éprouvé sur images.
- **Gimbals pour un hybride d'environ 1,2 kg** (ZV-E1 + zoom 24-70 GM II) : DJI RS 4 Mini (890 g, 2 kg de charge, 02/2025), Hohem iSteady MT3 Pro (1 070 g, 2,5 kg, caméra de suivi intégrée), Zhiyun Weebill 5 (1 080 g, 3 kg, 09/2026), DJI RS 5 (1 193 g sans poignée, 3 kg, 01/2026 ; molettes de réglage fin sur les trois axes, indicateur d'équilibre à l'écran). Sources : dji.com/rs-5/specs, newsshooter.com 2026-01-29, dpreview.com (RS 4 Mini), camerajabber.com (Weebill 5, RS 5), fstoppers.com 2026-03-24 (MT3 Pro).
- **Aucun gimbal à main ne s'équilibre seul par moteurs** (DJI, Zhiyun, Hohem, Feiyu ; recherche du 2026-11-03, absence de preuve). Ce qui existe : auto-tune (raideur des moteurs), verrous d'axes automatiques, indicateurs d'équilibre, molettes de réglage fin. Pour ne pas rééquilibrer : plateaux laissés sur la caméra, mêmes accessoires, une seule optique ; un zoom qui s'allonge déplace le centre de gravité.
- **Suivi de sujet** : module magnétique DJI (19 g, 0,5-10 m), caméra intégrée du MT3 Pro (champ plus large que l'objectif : cadrage décalé au-delà de 35 mm). Ne pilote pas la mise au point. **Le naturel du suivi n'est évalué par aucun test** : à juger à l'œil.
- **Gimbal contre Gyroflow** : aucun comparatif contrôlé publié. Le gimbal ne recadre pas et permet le 180° (flou de bougé juste) ; Gyroflow recadre et demande 90° ou 45° (doc Gyroflow). Aucun des deux ne corrige la translation (le rebond de la marche) : le gimbal la guide par l'indicateur d'axe Z du RS 5, la main et le pas la corrigent.
- **Au cinéma** [THÉORIQUE] (pratique de plateau connue, non vérifiée ici) : on stabilise au tournage, par une équipe dédiée (machinistes, opérateur Steadicam, technicien de tête stabilisée) qui monte et équilibre pendant que le reste du plateau se prépare ; rigs tout faits (Steadicam, Trinity, tête stabilisée sur bras ou grue, Ronin 4D, Easyrig sous un gimbal). En post, la stabilisation est un plan VFX : correction de la distorsion de l'objectif (grille tournée sur le plateau), suivi d'une zone fixe du décor (Nuke, Mocha, SynthEyes), lissage partiel et pas un verrouillage, recadrage dans la marge (open gate, surcadrage), contrôle du flou de bougé ; le monteur pose une stabilisation provisoire (Warp, Resolve) que l'équipe VFX refait.

### Comparatif des gimbals au 2026-11-03 : ce qui est prouvé [SOURCÉ]
- **Aucun test mesuré de la stabilisation elle-même** (banc, même parcours chiffré) n'existe en 2025-2026, toutes marques ; les « best gimbals tested » sont des pages d'affiliation. Mesures réelles trouvées : charges pesées et tenues observées (Digital Camera World), équilibrages chronométrés à la louche (Camera Jabber, Fstoppers), poids de rig. Les tests du DJI RS 5 chez CineD et Fstoppers sont payés par DJI ; la plupart des autres sont des prêts.
- **ZV-E1, listes officielles** (lues le 2026-11-03) : DJI RS 5 et RS 4 Mini (page dji.com/fr/support/compatibility/<modèle>/zve1, lue dans le navigateur) : câble USB-C = photo, REC, AF, mise au point électronique, diaph, vitesse, ISO, pas de zoom ; Bluetooth = photo, REC, AF, zoom. **Note DJI pour le RS 5 : « may experience stabilization issues when used with the Sony FE 24-70mm f/2.8 GM lens »** (GM ou GM II, non précisé). Zhiyun Crane 4 et Weebill 3S : ZV-E1 listé (câble et Bluetooth) ; Crane-M3S : câble seul ; Weebill 5, Crane 4E, Weebill 3E : aucune liste publiée. Hohem et Feiyu : non vérifié.
- **Charges annoncées contre tenue réelle** (DCW, 2026) : Hohem MT3 (1,4 kg annoncé) ne tient pas un reflex avec 24-105 ; MT3 Pro (2,5 kg) peine en roulis avec 1,05 kg ; Feiyu SCORP-C2 tient 1,05 kg sans peine.
- **Équilibrage chronométré** : Zhiyun Crane 4E, A7 IV + 24-70 + cage, un peu moins de 5 min (Camera Jabber, prêt) ; 10 min avec un 35-150 (Fstoppers). Feiyu : 5 à 10 min (estimé).
- **SAV Zhiyun** : plusieurs plaintes indépendantes (réponse arrêtée, renvoi en Chine, pas de garantie internationale). **DJI RS 5** : activation par compte DJI obligatoire (deux testeurs).
- Reddit, B&H et Amateur Photographer n'ont pas pu être lus (outil bloqué) : les avis d'acheteurs y restent à lire.
- **Test que je peux mesurer** : un même trajet tourné sur chaque gimbal essayé avec le ZV-E1 ; Gyroflow lit le gyroscope du rush et donne la rotation résiduelle (méthode du banc Gyroflow du 2026-11-03, `montage-resolve/recettes.md`).
