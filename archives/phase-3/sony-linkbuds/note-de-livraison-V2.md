# Note de livraison — Sony LinkBuds Clip × KORE (V2)

_Phase 3, session 1 (2026-10-11). Projet Resolve **`P3-sony-linkbuds-agent`** (base « TEST IA »), timeline **`SONY_V1`** (enregistré). Rendu : `videos/phase-3/sony-linkbuds/rendus/sony_linkbuds_V2.mp4` (V0 brouillon et V1 conservés à côté). Travail fait en environ 45 minutes de session, dont 25 de dérushage._

## Ce que j'ai fait
- **59,56 s**, 9:16 1080x1920, 25 i/s, H.264, BT.709, AAC 48 kHz ; **-14,5 LUFS, -1,4 dBTP** ; `flash_check.py` OK.
- 68 plans tirés de 252 rushes (tous dérushés : `derush.md`), en six blocs calés sur un **montage musical sans couture apparente** : un seul extrait continu du morceau (90,12 → 151,6 s) moins une mesure (la 62, au milieu d'un drop qui boucle). La structure suit la musique : montée (accueil, salle, boîtiers, oreilles), respiration (la coach, deux « photos », **4 images noires sur le silence numérique du morceau**), drop (la séance en blanc chaud), ralenti, dernier drop (la lumière passe au rouge), packshots, plan de fin Sony avec son logo sonore.
- **Le produit est montré porté** (13 plans d'oreilles, de bijoux et de chouchous), nommé une seule fois (« LinkBuds Clip », SST Pro Medium, sur les packshots), jamais démontré.
- Effets, tous faits par le MCP : 5 flashs blancs, 3 punch-ins et un zoom lent par clés Fusion, une secousse au drop, 3 ralentis à 50 % (vrais, depuis le 50p), 4 transitions différentes (Push, Glitch, Blur Dissolve, Zoom In), un texte animé.
- 19 SFX Artlist (13 sons, `sfx.md`), crête calée sur l'image de l'événement ; voix de la coach (décompte « quatre… trois… deux… sur un ») qui finit sur le silence avant le drop.
- Couleur : LUT technique Sony S-Log3 → 709 sur chaque plan ; CDL pour relever 6 plans trop sombres. Pas de look ajouté.

## Mes choix (à discuter)
- **Aucune parole porteuse de sens** (« que du visuel ») : les interviews, l'intro de l'animatrice et la voix off produit (« Le design ouvert des LinkBuds Clip, c'est LA solution… », HF1 REC070) sont dans `derush.md`, prêts pour une autre version. Seule exception : le décompte de la coach, utilisé comme un son (piste A4, facile à couper).
- Peu de marque du lieu (KORE est partout dans les rushes) : un plan de hall, la sangle de C6632 (12 images).
- Pas de whoosh sur chaque coupe (tes références réseaux n'en mettent pas) : SFX aux événements seulement.

## Ce que tu dois vérifier (surtout à l'oreille : je n'ai rien entendu)
1. **La coupure musicale à 33,7 s** (mesure 62 retirée, fondu de 2 images) : est-ce qu'elle s'entend ?
2. **Le décompte de la coach (13,7-16,6 s)** : intelligible sous la musique ? Le « sur un » tombe-t-il juste avant le silence ? Niveau (+5 dB sur le son caméra).
3. **Les SFX** : je les ai choisis au nom et à la forme d'onde. À écouter en priorité : le sub du drop (18,7 s, BOOM Library), le sub drop (43,1 s), les deux déclencheurs photo (14,7 et 15,0 s), l'aspiration et le riser autour du silence (14,6-18,8 s), le glitch (33,7 s).
4. **Le logo sonore Sony** (+7 dB par rapport au fichier fourni, qui est à -23,7 LUFS) : assez présent, pas trop ?
5. À l'œil : la rafale d'ouverture (4 éclats de 3 images) ; le passage du rouge aux packshots blancs (Zoom In à 54,2 s) ; la densité du bloc 18,7-41,2 s (plans de 1 à 2 temps, un plan tenu toutes les 4 mesures).

## Ce que je n'ai pas fait (ou pas su faire dans Resolve)
- **Détourages** : pas de Magic Mask par script. La liste des plans où ils serviraient, avec leurs images, est dans `plan.md` § « Plans à détourer » (5 plans) : si tu traces les traits, je peux lancer le suivi et poser les effets.
- **Grain / look film** : non ajouté (pas de nœud créable par script ; un outil de grain par composition Fusion sur 68 plans est possible mais je ne l'ai pas validé à l'image). C'est ton choix par défaut quand il n'y a pas de demande : à ajouter en un nœud de timeline.
- **Rampes de vitesse lisses** : non utilisées (ralentis francs à 50 %).
- **Mix dans Fairlight** : niveaux réglés par clip et mesurés sur le rendu ; pas de compresseur ni de limiteur (la crête reste à -1,4 dBTP sans limiteur).
- L'horloge de la caméra est fausse (fuseau -05:00) : je n'ai pas synchronisé de son HF ni de perche, aucun n'étant utilisé.
