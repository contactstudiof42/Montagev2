# Comparaison — Sony LinkBuds Clip : agent (V2) contre Claude nu (V1)

_Étape 6, phase 3, 2026-10-11. Pas de version de Diego (brief fictif) : le juge, ce sont ses notes dans `RETOURS-DIEGO.md` (sections du 2026-10-11 « notes sur la V2 », « comparaison » et « ordre des plans »). Fichiers comparés : `rendus/sony_linkbuds_V2.mp4` et `rendus-nu/P3_sony_linkbuds_clip_9x16_v1.mp4`. Le dossier de Claude nu (`/Volumes/SSD FAST/Montage-IA/videos/archives/Test-Claude-nu/`, `NOTES.md` et `work/`) a été lu après la fin du test à l'aveugle, en lecture seule._

## Le verdict de Diego
| | Agent V2 | Claude nu V1 |
|---|---|---|
| Livrable à | **50 %** | **40 %** |
| Ce qui gagne | « plus globalement plus propre » | plus impressionnant, dynamique, « quasiment épileptique » ; effets « mieux posés » ; détourages audacieux ; étalonnage meilleur (« même si c'est pas pro ») |
| Communs aux deux | packshots de fin qui tremblent ; titre et transitions amateurs ; aucun look professionnel ; la série K-O-R-E du cadreur non lue ; un ordre des plans raté (lui trop chronologique, moi sans logique visible) |

## Mesures (rendus finaux)
| | Agent V2 | Claude nu V1 | Références réseaux de Diego (7) |
|---|---|---|---|
| Durée | 59,6 s | 54,9 s | 12 à 43 s |
| Plans | 68 | 83, dont environ 15 coupés en deux par un saut de zoom | — |
| Flashs blancs | 6 (dont un noir de silence) | **environ 60** (6 gros, 18 petits, un à chaque arrêt sur image) | — |
| SFX posés | 19 | **environ 55** sur 5 pistes | — |
| Mouvements animés | 4 punch-ins, 1 secousse, 1 zoom lent | **environ 30 plans** : impact de zoom 1,22 → 1 avec flou de bougé (`Transform.MotionBlur`), poussée lente, secousse | — |
| Vitesses | 3 ralentis à 50 % | ralentis à 50 % **et accélérés à 150-200 %** | — |
| Détourages | 0 (déclarés impossibles) | **3 arrêts sur image détourés** (contour blanc, fond orange ou noir et blanc) | — |
| Étalonnage | LUT Sony LC-709 TypeA (+ CDL qui **éclaircit** 6 plans sombres) | CST S-Log3 → 709, puis CDL pente 1,30, décalage −0,085, puissance 1,22, saturation 1,35 | — |
| Noirs (5e centile de luma, médiane) | 17 | 19 | **5 à 11** (60 pour lucasbosc, look laiteux voulu) |
| Saturation moyenne (HSV, 0-255) | 113 | 143 | 79 à 158 (médiane 115) |
| Loudness | −14,5 LUFS, −1,4 dBTP | −13,2 LUFS, −2,0 dBFS | — |
| Tremblement du dernier packshot (`labo/outils/tremblement.py`) | **4,3 px en moyenne, pic 11 px** | ≈ 1 px en moyenne, pic 3 px sur le plan mesuré, mais Diego le voit trembler aussi | plan fixe de référence : < 1,5 px |

Les chiffres de luma ne montrent pas ce que Diego voit : sur les noirs et le contraste, ma V2 n'est pas plus « claire » que celle de Claude nu. La différence est dans la **densité des couleurs et la courbe des tons moyens** (l'image LC-709 TypeA est douce et désaturée, celle de Claude nu est chaude, dense, saturée), et elle saute aux yeux sur six paires d'images en pleine résolution (`_travail/comparaison/paires_a.jpg`, `paires_b.jpg`). Leçon : on ne juge pas un look sur des statistiques, on le juge sur des images côte à côte.

## Ce que Claude nu a fait mieux que moi, et pourquoi je ne l'ai pas fait
1. **Il a obéi au brief plutôt qu'au goût moyen des références.** Le brief disait « kinetic, très rapide, beaucoup d'effets, beaucoup de SFX », et même « plus d'effets et de SFX que la plupart » des références. J'ai lu cette phrase et j'ai quand même pris les références comme norme (« pas de whoosh sur chaque coupe », « qui respire », SFX seulement aux événements). Ma formation m'a appris la retenue des références de Diego ; je l'ai appliquée à un brief qui demandait l'excès. **Le brief prime : quand il demande l'excès, j'ose comme un monteur kinetic, puis je rends propre.**
2. **Il a cherché un autre outil quand le premier était fermé.** Le Magic Mask ne se trace pas par script : j'en ai conclu « impossible, Diego tracera ». Lui a pris la carte de profondeur de Resolve (`DepthMap`, effet ResolveFX disponible comme outil Fusion), l'a seuillée en masque (`BitmapMask` sur la luminance, seuils réglés plan par plan), a dilaté ce masque pour faire un contour blanc (`ErodeDilate`), et a posé le sujet sur un aplat orange ou un fond en noir et blanc, le tout sur un **arrêt sur image** de 6 images avec un « pop » d'échelle. Sur un arrêt, un masque approximatif passe : rien ne bouge, et le rythme ne laisse pas le temps de voir les défauts. Je n'ai pas fait cette recherche : je me suis arrêté au nom de l'outil (Magic Mask) au lieu de chercher le résultat (un masque du sujet). **Quand un geste est bloqué, je liste les autres façons d'obtenir le même résultat (profondeur, luminance, couleur, IA de Resolve, image fixe) avant de déclarer l'impossibilité.**
3. **Ses effets ont du mouvement physique.** Ses impacts de zoom ont le flou de bougé de Fusion (`MotionBlur`, obturateur 180°) et retombent en 4 images ; ses secousses s'éteignent en 6 images ; il alterne ralentis et accélérés. Mes punch-ins étaient corrects, mais rares, et rien dans ma V2 ne secoue l'œil. Les rafales de flashs, qu'il pose à chaque phrase musicale, sont précisément ce que Diego a aimé dans ma V2 vers 15 s et voulait voir « revenir plus souvent ».
4. **Son étalonnage s'engage.** Un CDL simple mais décidé (pente forte, noirs abaissés, gamma plus dense, saturation +35 %) donne une image chaude et dense ; la mienne est restée une conversion technique, et j'ai même éclairci les plans sombres pour la « lisibilité ». Diego : aucun des deux n'est pro, mais le sien est meilleur. Je savais juger un look chez les autres (phase 2) ; je n'ai pas regardé le mien à côté d'eux.

## Ce que j'ai fait mieux que lui
- **Propreté d'ensemble** (le choix de Diego pour livrer) : packshot flou remplacé, première image lisible, aucun plan de l'après-cours en plein jour qui casse la séance (Claude nu revient au hall de jour, gens qui boivent et mangent, avant les packshots).
- **Respirations et calage** : noir de 4 images sur le silence numérique de la musique, coupes des drops 0,4 image avant l'attaque, plans tenus avant chaque drop ; le passage rapide à 15 s, que Diego a aimé, vient de là.
- **Le produit porté** : 13 plans d'oreilles, de boucles et de chouchous ; le produit comme un bijou, pas comme une démonstration.
- **Un dérush complet** (252 rushes décrits avec timecodes, transcriptions, prises écartées) et un plan avec des critères mesurables : c'est ce qui permet de reprendre la V3 sans tout revoir.
- Niveaux plus prudents en crête (−1,4 dBTP contre −2,0 dBFS d'échantillon, non mesuré en true peak chez lui).

## Ce que nous avons raté tous les deux
- **La série K-O-R-E** : le cadreur a filmé chaque lettre du logo puis le mot entier, pour épeler la marque en raccords. Claude nu ouvre sur le K puis passe au mur ; moi, j'ai vu « des lettres qui défilent » et conseillé d'en garder une ou deux. Un monteur humain l'aurait vu tout de suite. **Au dérush, je cherche les séries pensées pour être montées ensemble** (même cadre, éléments d'un même objet filmés un par un, mouvements qui se répondent, même geste sous plusieurs angles) et j'écris l'intention du cadreur et le montage qu'elle appelle.
- **Les packshots qui tremblent** : nous regardons tous les deux des images fixes. J'ai désormais un outil de mesure (`labo/outils/tremblement.py`) et Gyroflow.
- **Le titre et les transitions** : texte « LinkBuds Clip » posé et grossi comme une diapositive chez les deux ; glissements intégrés chez moi.
- **L'ordre des plans** : lui suit l'heure de tournage (on arrive, on s'échauffe, on travaille, on repart), moi je mélange sans raison visible. Il faut une progression qu'on comprend, bloc par bloc, sans être prisonnier de l'heure de tournage.

## Ce que ma formation a réellement apporté (honnêtement)
- **Apporté** : la méthode (dérush exhaustif, analyse musicale, calage mesuré, QC, loudness, photosensibilité), la sécurité (aucun projet touché hors `P3-*`, sources intactes), la propreté et la lisibilité, le sens des respirations. C'est ce qui fait les 10 points d'écart en faveur de ma version.
- **Pas apporté** : le goût en acte. J'ai appris à reconnaître une belle image chez les autres, pas à exiger la même de la mienne ; j'ai contrôlé des chiffres au lieu de comparer des images. Et j'ai pris le goût des références pour une règle, au point de désobéir au brief.
- **Coûté** : de l'audace. Un Claude sans formation, qui ne savait pas qu'il « fallait » respirer, a fait ce que le brief demandait. Ma formation doit servir à faire l'excès proprement, pas à l'éviter.

## Ce qui change pour la V3 (détails dans `plan.md` V3)
Brief d'abord (densité kinetic, rafales de flashs à chaque phrase, ~45 s) ; ouverture sur la série K-O-R-E ; ordre des blocs justifié un par un ; arrêts sur image détourés par carte de profondeur, repris en mieux (masque adouci, contour net, sujet choisi pour la profondeur) ; impacts de zoom avec flou de bougé et freinage ; look fabriqué et comparé aux références en pleine résolution avant le montage ; packshots mesurés et stabilisés par Gyroflow ; titre de niveau pro ou pas de titre ; aucune transition intégrée de type glissement.
