# Autocritique — Sony LinkBuds Clip

_Phase 3, session 1 (2026-10-11). Regardé sur planches (milieu et première image de chaque plan), bandes image par image aux moments clés, luminance moyenne par plan, `qc_livraison.sh`, loudness par bloc, `flash_check.py`. **Rien n'a été écouté.**_

## V0 (brouillon, premier rendu)
- **Son saturé** : -7,6 LUFS, true peak **+4,4 dBTP**, crêtes décodées au-dessus de 0 dBFS. La musique (master MP3 très fort) posée à 0 dB suffisait à dépasser -9 LUFS. → musique -8 dB, SFX -6 dB, logo sonore Sony +6 dB (il est à -23,7 LUFS dans le fichier fourni).
- **Texte « LinkBuds Clip » trop petit** (taille 0,09 dans une composition 2160 de large) → 0,17, entrée de 0,153 à 0,17 en 4 images.
- Corrigés avant la V1.

## V1 (`rendus/sony_linkbuds_V1.mp4`) — défauts par ordre de gravité
1. **Plans trop sombres dans le sommet rouge** (luminance moyenne mesurée sur le rendu, sur 255) : C6662 à 1125 (31), C6664 à 1171 (28), C6672 à 1312 (27), et C6553 à 188 (38) dans l'ouverture. Ce sont des plans larges, sujets petits et décentrés : à 1 s sur un téléphone, on ne lit qu'une masse rouge. Le goût de Diego : « visages sombres, mais un minimum de lumière sur l'info à voir ». → CDL sur le nœud 1 (pente 1,25, décalage 0,02 : 28 → 45 mesuré sur C6664), et pente 1,15 sur C6665 (40).
2. **Dernier packshot flou** : C6724 (0,5-2,2 s) est pris pendant que la caméra recule, la mise au point décroche ; c'est l'image qui porte le nom du produit juste avant le plan de fin. → C6723 à 29,0 s (les trois boîtiers ouverts, nets et fixes de 28,5 à 31,5 s).
3. **Première image peu lisible** : la rafale s'ouvre sur C6660 (oreille en lumière rouge, très gros plan, à moitié dans le flou) : sur un fil, l'image 1 est une tache rouge. → ouvrir sur C6612 (écouteur net dans l'oreille, chouchou orange), puis rire, groupe, oreille rouge.
4. **Niveau un peu bas** : -15,5 LUFS intégré, -2,4 dBTP (cible -14 / ≤ -1). → +1 dB sur toutes les pistes (≈ -14,5 LUFS, ≈ -1,4 dBTP attendus).
5. **Le bloc C est une suite régulière de plans de 1 à 2 temps** (468-1030) : le « mur » est évité de justesse par quatre plans tenus (ralenti 562, souffle 656, groupe 796, néons 936, environ un toutes les 4 mesures). À surveiller à l'œil par Diego ; je ne change pas en V2.
6. **Le monde produit (packshots blancs, lumière du jour) tranche** avec la salle chaude : voulu (c'est « l'objet » avant la marque), mais le passage du rouge au blanc par un Zoom In est brutal. Accepté pour la V2 ; à juger par Diego.
7. Mineur : logo KORE lisible sur la sangle (C6632, 12 images) ; la marque du lieu reste discrète ailleurs.

## Ce qui marche (mesuré)
- Calage : flashs exactement à 368, 374, 468 et 1078 ; noir de 415 à 418 sur le silence numérique de la musique ; drops coupés 0,4 image avant l'attaque (468,4) ; plan de fin à 1447 sur le dernier coup.
- Produit porté visible dans 13 plans sur 68 (oreilles, boucles, chouchous) + 3 packshots ; nommé une fois.
- Photosensibilité : `flash_check.py` OK (20 flashs généraux, pire seconde 3, fenêtre 1/3).
- Fiche technique : H.264 1080x1920 25 i/s yuv420p, BT.709 ; AAC 48 kHz stéréo ; 59,56 s.
