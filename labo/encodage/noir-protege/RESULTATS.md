# Noir protégé sur une vraie scène (BACKLOG 65, session 12, 2026-10-10)

Suite de `labo/encodage/` (session 2, dégradé synthétique plein cadre). Ici : **une image 16 bits de la pièce 17** (« 3 h 12, dans le noir », v3 : écran tenu bas, caméra de côté ; Blender 4.2.3, Cycles 96 échantillons, AgX, 960×540, `scene16.py` = `atelier/17-dans-le-noir/scene.py` avec résolution, échantillons et PNG 16 bits ; rendu 52 s). Image typée « Willis » : ~90 % de noir pur, un îlot éclairé, des pénombres **courtes et raides**.

Script : `mesure.py` (≈ 15 s ; `PANO=1` = panoramique simulé de 2 px/image). Mesures : `resultats.json` (image fixe), `resultats_pano.json` (panoramique). Planches : `planche.png`, `planche_pano.png` (pénombre ×20, Y 16 → 28,75).

**Mesure** : pénombre lisse de la référence (Y 16,3-30 en plage limitée, noir pur exclu, gradient < 1 niveau/px) ; image n°12 ; *part de marche visible* = part des pixels où l'image lissée (σ 3 px) s'écarte de plus d'un demi-niveau 8 bits de la référence lissée. Indicatif : le masque est petit (≈ 2 500 px) et la valeur varie avec lui ; **les conclusions ci-dessous sont celles qui restent vraies pour les quatre masques essayés** (session 12 : premier masque sur le mur éclairé — erreur de zone ; puis Y > 2 en oubliant que la plage limitée met le noir à 16 — erreur corrigée).

| Variante | Fixe : marche visible | Pano : marche visible | Ko (1 s) fixe / pano |
|---|---|---|---|
| A master 8 bits CRF 18 | 0,000 | **0,027** | 23 / 40 |
| B master 10 bits CRF 18 | 0,000 | **0,004** | 14 / 27 |
| A → plateforme CRF 23 (8 bits) | 0,015 | 0,117 | 14 / 24 |
| B → plateforme CRF 23 | 0,018 | 0,146 | 12 / 22 |
| A → plateforme 2 Mb/s | 0,000 | 0,037 | 61 / 141 |
| B → plateforme 2 Mb/s | 0,000 | **0,007** | 72 / 166 |
| G grain σ 2 niveaux (sans perte, référence du grain seul) | 0,033 | 0,059 | — |
| G → plateforme CRF 23 | 0,147 | 0,083 | 15 / 32 |
| G → plateforme 2 Mb/s | 0,172 | 0,158 | 267 / 255 |
| M grain dosé (nul dans le noir pur) → CRF 23 | 0,212 | 0,164 | 14 / 27 |
| M → 2 Mb/s | 0,115 | 0,096 | 200 / 202 |

## Ce que ça apprend
1. **Une image fixe ment** : immobile, l'encodeur garde tout (8 et 10 bits identiques). Dès que le cadre bouge de 2 px/image, le master 8 bits fait des marches dans la pénombre (visibles sur `planche_pano.png`, coin bas-gauche) et le 10 bits non (0,027 contre 0,004). **Tester l'encodage d'un plan sombre en mouvement**, jamais sur un plan fixe.
2. **Le master 10 bits reste la règle**, et il survit à un ré-encodage 8 bits **à débit correct** (2 Mb/s pour du 540p : 0,007, quasi intact ; la conversion 10 → 8 bits de ffmpeg tramant légèrement). Il ne survit pas à un ré-encodage serré (CRF 23 : blocs dans la pénombre, A comme B).
3. **Le grain n'est pas une protection universelle** (corrige la recette de la session 2) : sur une image majoritairement noire, le grain σ 2 **consomme le débit** (267 Ko contre 72 à 2 Mb/s) et l'encodeur rend des blocs : à débit plafonné, il fait **pire** que rien (0,16-0,17 contre 0,007). Il n'aide un peu qu'au ré-encodage serré **en mouvement** (0,083 contre 0,12-0,15), c'est-à-dire le cas de la session 2. Le doser par la luminance (M) ne règle rien.
4. **Le noir dur protège mieux que le noir doux** : sur cette image (pénombres courtes, noir pur), il y a peu de zones à risque. C'est le **dégradé long et doux** (ciel de nuit, mur éclairé par rebond, brume) qui fabrique des bandes. Décision artistique d'abord : un noir « à la Willis » (on décide quoi garder dans le noir, le reste est noir) encaisse mieux la plateforme qu'un clair-obscur laiteux.

## Recette mise à jour [TESTÉ EN LABO, 2 scènes : dégradé synthétique (s2), rendu Blender fixe et en panoramique (s12)]
- Master et échanges : 10 bits, toujours.
- Livraison plateforme : envoyer le 10 bits (ou un 8 bits à débit généreux) **sans grain ajouté par défaut** ; ajouter un grain fin seulement si (a) le plan contient un **dégradé long et doux** et (b) un essai en mouvement, ré-encodé à la qualité de la plateforme, montre qu'il aide. Le grain reste un choix de matière (Joker, Ziak), pas une assurance.
- Limites : ré-encodage plateforme **simulé** (x264 CRF 23 ou 2 Mb/s ABR), pas les vrais encodeurs YouTube / Instagram ; un seul rendu ; mouvement simulé par recadrage (interpolation bicubique, qui lisse un peu). À vérifier en phase 2 : téléverser A, B, G en non répertorié et mesurer le fichier rendu (PLAN-TESTS 52).
