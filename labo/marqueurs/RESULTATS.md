# Labo marqueurs de temps (session 4, 2026-10-10)

**Question** : peut-on fabriquer, hors logiciel, une grille de marqueurs de temps importable dans Premiere ou Resolve, pour monter sur la musique (kinetic) ou au contraire *contre* elle (macro, façon Ziak) en voyant la grille ?

**Outil** : `beats_xml.py musique.wav sortie [fps] [temps_par_mesure]` → `sortie.xml` (FCP7 xmeml v4 : une séquence vide portant un marqueur par temps, les premiers temps de mesure nommés M1, M2…) et `sortie.csv` (contrôle).

## Test [TESTÉ EN LABO pour la détection ; import dans Premiere/Resolve THÉORIQUE]
Vérité terrain synthétique : grosse caisse à 128 BPM, 1er temps à 0,350 s, charleston à contretemps, bruit de fond, 20 s.

| Version | BPM trouvé | Écart aux vrais temps |
|---|---|---|
| v1 : flux spectral plein spectre pour le tempo et la phase | 128,24 | **jusqu'à 292 ms : grille à contretemps** (le charleston, riche en aigus, gagne la phase) |
| v2 : phase sur le flux grave (< 200 Hz) + correction du retard de fenêtre | 128,24 | −30 à +6 ms (dérive du tempo arrondi) |
| v3 : chaque temps recalé sur le pic grave voisin (±40 ms) puis régression linéaire | **127,99** | **−10 à −9 ms constants** (biais de la fenêtre, < ¼ d'image à 25 i/s) |

## Ce que j'apprends
1. **Le tempo est facile, la phase est le piège** : une grille juste en BPM mais décalée d'un demi-temps met toutes les coupes à contretemps. Toujours vérifier le premier marqueur à l'oreille ou sur la forme d'onde avant de monter.
2. Les instruments aigus réguliers (charleston, shaker) attirent la phase : les temps forts se lisent dans les graves.
3. Limites : tempo fixe uniquement (pas de musique jouée sans clic, pas de rubato, pas de changement de tempo) ; musique sans grosse caisse (piano, cordes) non testée.
4. À vérifier en phase 2 (`PLAN-TESTS-MCP.md`) : import du XML dans Premiere (les marqueurs de séquence arrivent-ils ? noms et commentaires ?), dans Resolve ; comparer avec l'outil `pr_detect_beats` du MCP Higgsfield sur la même musique.
