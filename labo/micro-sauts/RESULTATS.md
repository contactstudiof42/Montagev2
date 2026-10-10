# Labo micro-sauts (BACKLOG Y17) — session 25, 2026-10-10 [TESTÉ EN LABO, vérité terrain synthétique]

**Question** : à une coupe dans une même prise (jump cut face caméra, punch-in), de combien l'image saute-t-elle ? Un jump cut qui saute de moins d'environ 1-2 % de la largeur sans changer d'échelle se lit comme une **erreur** (le « micro-saut »), pas comme une ellipse assumée. Il faut un chiffre pour le repérer dans un montage de 20 min.

**Méthode** (`micro_sauts.py`) : image juste avant / juste après la coupe, réduites à 320 px de large, en niveaux de gris, fenêtre de Hann ; recherche d'échelle 1/1,5 → 1,5 par pas de 0,01 (punch-in ou punch-out), puis translation par **corrélation de phase** ; on garde l'échelle au pic le plus haut. Sortie : échelle, décalage en % de largeur, pic (confiance). 4 s par coupe (CPU).

**Vérité terrain** (`verite.py`, image Blender de la pièce 34 recadrée, bruit σ = 4) :
| vrai (échelle, dx %) | mesuré | pic |
|---|---|---|
| 1,00 / 0 | 1,00 / 0 | 0,90 |
| 1,00 / +0,5 | 1,00 / +0,62 | 0,66 |
| 1,00 / +1,5 | 1,00 / +1,56 | 0,83 |
| 1,00 / +3,0 | 1,00 / +3,12 | 0,65 |
| 1,00 / -0,3 | 1,00 / -0,31 | 0,90 |
| 1,10 / 0 | 1,10 / 0 | 0,67 |
| 1,20 / +1,0 | 1,20 / +0,94 | 0,57 |
| 1,35 / -2,0 | 1,35 / -1,88 | 0,43 |
| plan différent | (1,39 / 4,4 / -7,8) | **0,048** |

- Échelle exacte au centième ; décalage à ±0,12 % de largeur (1 px d'analyse = 0,31 %).
- **Séparation nette** : même prise ≥ 0,43, plans différents 0,05. Seuil proposé : pic < 0,15 = vraie coupe entre plans (ignorer) ; pic ≥ 0,15 = même prise, lire échelle et décalage.

**Limites** : translation globale seulement. Sur un vrai face caméra, la tête bouge et pas le fond : la corrélation de phase prend le mouvement dominant (souvent le fond, s'il est texturé). En phase 2 : mesurer sur une zone (le visage) et sur le fond séparément ; confronter le seuil « micro-saut » à mon jugement sur de vrais rushes (PLAN-TESTS 75). Rotation non gérée.

**Règle à tester (hypothèse de travail)** : dans une même prise, échelle 1,00 et décalage < ~2 % → micro-saut (paraît une erreur) : soit le cacher (plan de coupe, punch-in ≥ 1,10-1,15 qui se lit comme un choix), soit l'assumer franchement (enchaîner plusieurs jump cuts au même rythme).

## Par zones (BACKLOG Y50, session 25) [TESTÉ EN LABO, synthétique]
`mesurer(avant, après, zone=(x, y, l, h))` (fractions de l'image) ; `verite_zones.py` : une « tête » texturée (disque de 220 px) déplacée de dx % sur un fond fixe.
| dx tête (%) | fond lisse : global | fond lisse : zone | fond texturé : global | fond texturé : zone |
|---|---|---|---|---|
| 0,5 | 0,31 | 0,44 | **0,00** | 0,44 |
| 1,0 | 0,94 | 0,98 | **0,00** | 0,98 |
| 2,0 | 1,88 | 1,97 | **0,00** | 1,97 |
| 4,0 | 4,06 | 3,94 | **0,00** | 3,94 |
- **La mesure globale suit la région la plus texturée**, pas le sujet : sur un fond lisse (mur), elle voit la tête ; sur un fond texturé (bibliothèque, feuillage), elle dit « aucun saut » même quand la tête saute de 4 %. Mesurer **toujours par zone** sur le sujet (boîte autour du visage, avec une marge ≥ au saut attendu), et à part sur le fond.
- Zone : erreur ≤ 0,06 % de la largeur totale. Lecture combinée : tête qui saute + fond immobile = la personne a bougé entre les deux morceaux (micro-saut de jeu) ; les deux sautent ensemble = recadrage ou caméra qui a bougé.
- Reste : boîte du visage automatique (détecteur de visage, phase 2 sur vrais rushes), rotation.

## Échelle jusqu'à ×3 (session 25)
Recherche étendue (pas de 0,01 jusqu'à 1,5, puis 0,02 jusqu'à 3). Vérité terrain : ×2,4 → 2,42 (pic 0,20) ; ×2,9 / +1 % → 2,86 / 0,62 (pic 0,16) ; plan différent pic 0,066. **Le pic baisse avec l'échelle** (moins de détail commun) : pour une coupe dans l'axe forte, le seuil de 0,15 devient limite ; abaisser à ~0,12 au-delà de ×2. Sur une vraie coupe dans l'axe avec déplacement de caméra (pièce 34 v7, large → plan de v6), la mesure globale donne ×1,6 : elle suit les fenêtres de l'hôpital, lointaines, qui grossissent moins que la voiture (parallaxe). Même leçon qu'en zones : **mesurer sur le sujet**.
