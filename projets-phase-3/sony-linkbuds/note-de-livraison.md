# Note de livraison — Sony LinkBuds Clip, V5

_2026-10-11. Fichier : `videos/phase-3/sony-linkbuds/rendus/sony_linkbuds_V5.mp4` (1080x1920, 25 i/s, **HEVC Main 10, 39 Mb/s**, AAC 48 kHz, 44,6 s, **−13,9 LUFS, −1,1 dBTP**). Resolve : projet `P3-sony-linkbuds-agent`, timeline **`SONY_V5`** (la V4 reste intacte dans `SONY_V4`). Note V4 : `archives/phase-3/sony-linkbuds/V4/note-de-livraison.md`._

## Ce que j'ai fait (tes notes sur la V4, une par une)
| Ta note | Dans la V5 |
|---|---|
| Un son sur chaque transition | Chaque transition (effet ou changement de bloc) a son son, calé à l'image sur l'attaque ou la crête mesurée du fichier : 16 sons recalés (certains tombaient 2 à 12 images à côté), 5 retirés, 13 posés. Les coupes franches à l'intérieur d'un bloc n'ont pas de son à elles : c'est ma lecture de « transition », à confirmer. Tableau : `sfx.md` § V5. Aucun nouveau téléchargement |
| Preuve Gyroflow plan par plan | Tableau ci-dessous |
| Bruit, noirs relevés | Noirs à 0 sur les plans de salle, grain 35 → 20 %, ombres vérifiées amplifiées ×4 |
| Étalonner plan par plan | Rendu entier mesuré plan par plan (noirs, médiane, hautes lumières, blanc brûlé) et chaque plan regardé ; 19 corrigés (`journal.md` geste 64) |
| Large KORE surexposé, ouverture plus rapide | Ouverture plus rapide (zoom en 7 images) ; lettres et comptoir au même béton, large sans blanc brûlé |
| Plan de 16-17 s surexposé | C6581 : −1 diaph (médiane 0,35 → 0,15) |
| Écouteurs de fin surexposés | −2 diaph environ (C6725 −0,15, C6723 −0,17) : de 13-27 % de blanc brûlé à 0 % hors flash ; le lavande, le menthe et le crème se lisent |
| Visages | Tous les plans contrôlés image par image ; « tête bizarre » retirée ; C6627 (7,96 s) remplacé par un autre moment du même rush |
| Collages | A1 (11,2 s) : ta piste (le plan suivant glisse derrière elle, elle disparaît par balayage) ; C1 (27,1 s) : la tête positive, le monde en négatif ; B supprimé. Tout vient de `da.md` |
| Inversions : un peu plus | Les flashs blancs des drops (9,3 s et 27,6 s) sont devenus des inversions ; deux de plus dans le pic |
| Plan de remplissage, flous | Tapis et panoramique flou retirés ; chaque flou classé volontaire ou raté |
| Fin trop longue : dernier pic | **Pic de 4,7 s (33,2-37,9 s)** d'après ta référence foebusdelapaz : révélation par seuil, rafale récapitulative, respiration en noir et blanc, stroboscope dans le rouge, crash zoom sur le mot KORE, balayage, blanc, packshots sobres |

## Stabilisation : méthode et preuve, plan par plan
Méthode : Gyroflow (données gyroscopiques du ZV-E1, zoom fixe 115 %, lissage par défaut) rendu sur une plage courte avec un **décalage gyroscope / image imposé** puis remesuré (`labo/outils/gyro_rendu.py`, preuve `*_preuve.json`) ; puis, pour les plans où le cadreur voulait un mouvement, correction « rail » de la translation que les gyroscopes ne voient pas (`stabiliser.py`, clés dans un `Transform` « Rail » de la composition du plan). Tremblement mesuré sur le rendu final (`tremblement.py`, px d'une image de 1080).
| Plan | Fichier | Synchronisation | Après | Tremblement final |
|---|---|---|---|---|
| K-O-R-E, large KORE (0-2,4 s) | `C6491`…`C6495_stabilized.mov` (V4) | autosynchronisation de la ligne de commande (V4) : **ne laisse aucune trace, non prouvable** ; mouvement trop faible pour la mesurer (0,2 px par image) | épinglage « fixe » (V4) | 0,2-0,3 px (V4) |
| Boîtiers (4,7 s) | rush brut C6507 | — | aucun | 1,15 px (mesuré par le centre des boîtiers : `tremblement.py` ne lit pas le tapis en carbone) : déjà stable. Le rendu Gyroflow synchronisé de ce passage tremblait 7 fois plus : écarté |
| Gros plan boîtier (5,2 s) | `C6507_gf_s24.mov` | mesuré −34 ms, imposé +34 ms, **résiduel 4 ms** | aucun (flash blanc, gros plan) | — |
| Packshot lavande (37,9 s) | `C6725_gf_s0.mov` | **non mesurable** (corrélation trop faible) : imposé 0 | rail, lissage 1 s | **0,66 px** |
| Packshot menthe (38,9 s) | `C6723_gf_s12.mov` | imposé +10 ms, **résiduel −2 ms** | rail, lissage 1 s | **0,68 px** |
| Les trois boîtiers + titre (39,8 s) | `C6723_gf_s27.mov` | imposé +10 ms, **résiduel 6 ms** (corrélation de rotation 0,91) | rail, lissage 0,6 s | **0,84 px** |
Le travelling du cadreur est gardé (45, 34 et 47 px/s) : ce n'est jamais un plan fixe.

## À vérifier par toi
**À l'oreille (rien n'a été écouté) :**
1. **Le pic, 33,2-37,9 s** : riser sous tout le passage (−16 dB), impact à 33,5 s (la couleur arrive), bégaiement de la rafale, souffle à 35,1 s (la respiration), impacts à 36,0 et 37,2 s, glitchs à 36,3, 37,7 et 37,8 s. Risque d'encombrement : le riser est le premier à baisser.
2. **Collage A1, 11,2-11,7 s** : déclencheur « Sony α7 III », whoosh fin, glitch du balayage.
3. Le Polaroid recalé sur le gel du collage C1 (27,1 s), raccourci.
4. Les recalages de l'ouverture (clics O et R, whoosh de l'allée à 3,3 s) et des oreilles (6,1-7,0 s).
5. Le glitch de 32,1 s tombe maintenant sur une coupe simple de la rafale rouge (le négatif qui le portait a été retiré pour la photosensibilité).

**À l'œil :**
6. Le bloc des fentes (9,4-18,7 s) : répétitif ou juste ? (autocritique, point 2).
7. Le lavande du premier packshot, un peu rosé.
8. Le mot KORE à la fin du pic : rappel voulu de l'ouverture (même comptoir, autre moment du rush), juste avant Sony.

## Fichiers et pistes
- Pistes vidéo : **V1** plans (dont `A1.mov`, `C1.mov`, `pic_v5.mov` en ProRes 4444 sans LUT) ; **V2** le E du zoom infini et une bande de l'écran partagé ; **V3** flashs blancs, inversions des drops (calques du plan dessous) et bande du bas ; **V4** titre ; **V5** grain (20 %). Audio : **A1** musique, **A2** son du plan de fin Sony, **A3-A8** SFX.
- Nouveaux fichiers de travail (aucun dans `SONY copy/`) : `videos/_travail/sony_v5/pic_b/`, `videos/_travail/sony_v5/rail/`, `videos/_travail/sony_v5/comps/`.
- `run_script_unsafe` utilisé une fois par lot de clés (lecture des trois JSON de stabilisation), rien d'autre.

## Ce que je n'ai pas su faire, ou fait autrement
- Prouver la synchronisation de C6725 et des lettres K-O-R-E : leur mouvement est trop faible pour la mesure ; seul le résultat est mesuré.
- Le pic et les collages sont calculés hors de Resolve (Python) : propres, mais à relancer pour les retoucher.
- Cases « Force sizing / debayer » du rendu : toujours hors API (voir la note V4).
