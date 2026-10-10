# Pièce 04 « Ce que la marée découvre » — critiques

Planches : `v1-planche.png` (1 vignette toutes les 20 images, numéro d'image incrusté).

## v1 — plan fixe large, eau qui baisse linéairement (0,85 → −0,30 m en 250 images)
| Critère | Note | Preuve visuelle |
|---|---|---|
| Intention | 2 | La 1re image est vide (bien) et, à l'image 20, deux points noirs sur l'eau (les montants du dossier) créent la question. Mais la chaise est identifiée vers 100-120 (40-48 %), puis **cinq vignettes (120-180) n'apportent rien** : la gêne retombe. |
| Lisibilité | 2 | Chaise ≈ 6 % de la hauteur de l'image : lisible sur grand écran, perdue sur téléphone. |
| Rythme | 1 | L'eau descend à vitesse constante : la chaise émerge comme un métronome, puis **le sable et la chaîne surgissent d'un coup** (vignettes 180 → 200 : l'estran est presque plat, il se découvre en 20 images). Le vrai événement arrive à 80 % et la pièce finit sur un changement, pas sur une tenue : critère 3 raté. |
| Composition | 1 | Chaise au centre, horizon au tiers haut : carte postale. Le centrage n'est pas un choix ici. |
| Cohérence | 3 | Ciel, eau et sable dans le même gris. |
| Couleur | 2 | Je m'étais interdit « une seule chaleur »… et la **rouille de la chaîne** devient exactement cela à la fin. Elle est motivée (matière) et porte la révélation : je la garde, mais je note que mon système revient par la matière quand je le chasse par la lumière. |
| Mouvement | 1 | Linéaire = mécanique. |
| Originalité | 2 | Une chaise dans la mer : image surréaliste connue (Magritte, photos de plage), sauvée par la chaîne qui suggère une histoire. |
| Justesse | 3 | Rien de trop : pas de musique, pas d'effet. |

**Découverte de la v1, plus importante que ses défauts** : sur un estran plat, la marée découvre lentement ce qui est haut (la chaise), puis **tout le sol d'un coup**. C'est la dramaturgie naturelle du sujet : lent, puis brusque. Je n'ai pas à l'inventer, il faut la cadrer et lui laisser le temps de se poser.

**Corrections pour v2** : caméra basse (0,55 m) et focale 45 mm, chaise décalée à droite et 3× plus grande ; l'eau au ras de l'objectif devient la matière de l'image ; courbe d'eau lente au début (la question), qui accélère, puis **tenue de 28 images** sur l'estran découvert ; horizon remonté vers le tiers haut. Constat du test d'une image : en caméra basse, l'eau est un miroir (Fresnel rasant) : impossible de laisser deviner la chaîne sous la surface ; la révélation sera purement par émersion.

## v2 — caméra basse (0,55 m), 45 mm, courbe d'eau lente puis rapide, tenue finale : **erreur de géométrie**
Image de contrôle : `v2-erreur-sous-eau.png` (images 1, 60, 110 / 140, 170, 188).
- **La caméra est sous l'eau** de l'image 1 à l'image ~97 : l'eau démarre à 0,80 m, l'objectif est à 0,55 m. Les deux premières vignettes montrent la chaise et la chaîne *sous* la surface, vue d'en dessous. Mon test d'une seule image (image 160) ne pouvait pas le voir. **Leçon de méthode : tester la 1re et la dernière image d'un plan animé, et vérifier les contraintes géométriques (caméra au-dessus de l'eau à toute image) avant de lancer 250 images.**
- **Accident à garder** : la vue sous-marine montre l'objet au spectateur *avant* que la surface ne le découvre. C'est l'autre façon de faire monter la gêne : l'ironie dramatique (Hitchcock : le spectateur sait qu'il y a une bombe sous la table). Direction alternative notée : ouvrir sous l'eau sur la chaise, couper au-dessus de la surface lisse, et laisser le spectateur attendre ce qu'il sait déjà.
- À partir de l'image 110 (caméra hors de l'eau) : la chaise décalée à droite est 2× plus grande qu'en v1, l'eau occupe la moitié basse ; à l'image 170, **la chaîne affleure en pointillés** avant que le sable n'apparaisse : un détail d'attente juste, que la v1 n'avait pas.
→ v2b : même cadrage, caméra à 0,95 m (au-dessus de l'eau à toute image), inclinaison 84,5°.

## v2b — plan unique corrigé (caméra 0,95 m, 45 mm, chaise au tiers droit) — `v2b-planche.png`
| Critère | Note | Preuve visuelle |
|---|---|---|
| Intention | 3 | 0-40 : eau vide ; **60 : un trait fin** à la surface (le haut du dossier), impossible à nommer ; 120 : un cadre ; **140 : l'assise sort, c'est une chaise (56 %)** ; 200 : la chaîne affleure puis l'estran se découvre d'un coup ; 222-250 : tenue. Les trois critères de l'intention sont tenus. |
| Lisibilité | 2 | Chaise ≈ 12 % de la hauteur (v1 : 6 %). Encore petite sur téléphone : en 9:16, il faudrait la placer bien plus près. |
| Rythme | 3 | Lent (60 images sans rien, puis émergence), brusque (estran découvert en ~20 images), tenue de 28 images. |
| Composition | 2 | Tiers droit, la chaîne entre par la gauche et guide vers la chaise : juste. Horizon un peu haut. |
| Couleur | 2 | Toujours la rouille comme seule chaleur (assumé, cf. v1). |
| Mouvement | 2 | Rien ne bouge que l'eau : juste pour le sujet. |
| Originalité | 2 | — |
| Justesse | 3 | — |
Défaut technique : la frontière eau/sable est **polygonale** (images 200-220 : bords à facettes) : résolution du déplacement trop faible ; trahit l'image de synthèse. → subdiviser la zone proche ou utiliser un déplacement au shader.

## v3 — trois plans (plan unique 1-175, insert anneau 176-215, plan large 216-250) — `v3-planche.png`
- L'insert (image 200 : l'anneau et la chaîne qui mène au pied de la chaise) est **la plus belle image de la pièce** : une ligne de cause (quelqu'un l'a attachée).
- Mais **couper libère la tension** : l'insert commence sur de l'eau vide avec un pied de chaise au bord (image 180 : « où suis-je ? »), et le plan large final *explique* (tout le dispositif est montré, la question est close). On passe de la gêne à la démonstration. Confirme Honda « Cog » et Murai : **quand l'attente est l'argument, ne pas couper**.
- Usage : v3 serait juste pour une pub (il faut une image-signe, l'insert) ; pour l'intention écrite, non.

## v4 — ironie dramatique : ouverture sous l'eau (1-60), puis le plan unique (61-250) — `v4-planche.png`
- Images 0-40 : chaise et chaîne vues sous la surface, la surface en miroir au-dessus. **À l'image 60, le trait à la surface n'est plus un mystère : on sait ce qui va sortir.** Les 6 s suivantes deviennent une attente de ce qu'on sait (suspense) au lieu d'une énigme (mystère).
- Cela sert peut-être **mieux** l'intention (« depuis combien de temps c'était là ? ») : on a vu l'objet installé au fond, immobile.
- Défaut : le sous-marin n'est pas crédible (aucune turbidité, bande claire de l'horizon). À refaire avec un volume (absorption vert-gris, particules, rayons).

## Bilan provisoire (session 4)
- **Référence : v2b** pour le mystère ; **v4 à développer** pour le suspense. Le montage en 3 plans (v3) ne sert pas l'intention.
- Son (v3, v4) : ressac qui s'éloigne et s'efface à l'image 222, puis **quatre gouttes** tombant de la chaise : le seul son de la fin. Mesuré à -18,4 LUFS / -1,0 dBTP (limité par le true peak du bruit rose : cible -18 non tout à fait atteinte, assumé). Non écouté (pas d'oreille dans la VM).
- Prochaines versions : v5 = v4 avec eau sous-marine crédible et frontière eau/sable lissée ; variante 9:16.

## v5 — v4 + volume sous-marin (densité 0,07) + sable plus fin (60 m, subdivision 9) — `v5-planche.png`
- Sous l'eau (0-40) : la turbidité et les rides du fond donnent enfin une matière ; la bande claire (fenêtre de Snell : le ciel vu à travers la surface au-delà de l'angle critique) est physiquement plausible. Encore trop sombre et pas assez vert pour qu'on lise « sous l'eau » sans hésiter.
- Surface (200-220) : la frontière eau/sable est **organique** (défaut de v2b corrigé), mais les rides sont devenues **trop fortes et trop régulières** (tôle ondulée) : la chaîne se perd dedans à l'image 220. Ce que j'ai gagné en crédibilité de la grève, je l'ai perdu en lisibilité du sujet. → v6 : déplacement 0,015 au lieu de 0,04, rides moins régulières (bruit à deux échelles).
- Volume à 0,35 : image noire (absorption totale) ; à 0,07 : juste. Un volume sous l'eau se règle à l'échelle de la scène (ici quelques mètres de visée).
- **Référence actuelle : v2b (mystère)** ; v5 est la meilleure version « suspense » mais pas encore livrable (lisibilité de la chaîne à la fin).
