# Note de livraison — Sony LinkBuds Clip, V3

_2026-10-11. Fichier : `videos/phase-3/sony-linkbuds/rendus/sony_linkbuds_V3.mp4` (1080x1920, 25 i/s, H.264, AAC 48 kHz, 44,6 s, −14,1 LUFS, −1,1 dBTP). Resolve : projet `P3-sony-linkbuds-agent`, timeline **`SONY_V3`** (la V2 reste dans `SONY_V1`). Note de la V2 : `archives/phase-3/sony-linkbuds/note-de-livraison-V2.md`._

## Ce que j'ai fait
Une V3 qui applique tes notes sur la V2, ta comparaison avec Claude nu et ton retour sur l'ordre des plans : plus courte (44,6 s), beaucoup plus dense (91 plans, 4 rafales, 64 SFX, 19 impacts, 3 arrêts détourés), ouverte sur la série K-O-R-E du cadreur, un vrai look (tirage Kodak 2383, noirs denses), aucune transition « PowerPoint », un nouveau titre, des packshots stabilisés. Le pourquoi de chaque bloc est dans `plan.md`.

## Organisation de la timeline (pour reprendre vite)
- **V1** : les plans. Chaque plan porte **un seul nœud** : la LUT `LUT/P3/P3_sony_look_film_D2.cube` (conversion S-Log3 et look en un) + un décalage CDL pour l'exposition quand il faut. Les zooms, secousses, détourages et la stabilisation sont dans la composition Fusion du plan.
- **V3** : flashs blancs (courte vidéo blanche, mode Add). **V4** : titre (composition Fusion). **V5** : grain (Overlay 35 %). Chaque piste se coupe d'un clic pour alléger la lecture.
- **A1** musique (2 segments) · **A2** son du plan de fin (+7,3 dB) · **A3-A8** SFX.

## À vérifier par toi
**À l'oreille (rien n'a été écouté) :**
1. La **coupure musicale à 26,24 s** (image 656) : 125,736 s → 133,236 s du morceau, calée sur la phase des temps forts. Si ça boite, décaler le segment 2 de ±1 image.
2. Les **64 SFX** : surtout les clics des lettres K-O-R-E (0-48), les déclencheurs des arrêts (281, 503, 678), les impacts des deux drops (233, 690) et les glitchs des rafales. Niveaux de −7 à −17 dB, impacts baissés de 2,5 dB pour le true peak.
3. Le mélange musique / SFX dans les rafales : densité voulue, mais peut-être chargée.

**À l'œil :**
4. **Le halo jaune** autour des cheveux du premier arrêt détouré (281-293).
5. **Le packshot rose (948-972)** tremble encore un peu (2,7 px de moyenne après ma stabilisation, 5,5 avant).
6. **Le titre** : à garder, à changer ou à retirer (le plan de fin Sony suffit).
7. **Le grain** (V5) : dosé à 35 % sans écran étalonné.

## Ce que je n'ai pas su faire
- **Gyroflow** : bloqué par le bac à sable de macOS en ligne de commande (il ne lit que son propre dossier). Tu as choisi de lui donner l'accès au dossier `SONY copy` (marche à suivre dans la conversation). Dès que c'est fait, je stabilise les packshots avec les gyroscopes et je remplace ma stabilisation.
- La **stabilisation de Resolve** par l'API (`Stabilize()`) recadre beaucoup trop : abandonnée. J'ai stabilisé moi-même en compensant la trajectoire mesurée (translation seulement, sans rotation).
- Pas de **vrai Magic Mask** : la carte de profondeur fait les détourages, très bien sur un sujet proche, moins bien sur des cheveux éclairés.
- **Rien écouté.**
