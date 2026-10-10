# Labo photosensibilité (session 7, 2026-10-10) — [TESTÉ EN LABO]

But : un contrôle de montage qui repère les séquences à risque **avant** le test officiel (Harding FPA exigé par l'ASA au Royaume-Uni pour la pub ; seuils WCAG 2.1 SC 2.3.1 et ITU-R BT.1702-3, voir `culture/enter-the-void-generique-noe-tom-kan.md`, section Risques). Ce n'est pas un outil de certification.

Commande : `python3 -I labo/photosensibilite/flash_check.py video.mp4 [--fps 25]` ; vérités terrain : `sh tests.sh` (depuis ce dossier, ~5 s).

| Cas (2 s, 25 i/s) | Attendu | Résultat | Pire seconde |
|---|---|---|---|
| A noir/blanc toutes les 2 images | échec | ÉCHEC | 7 flashs |
| B noir/blanc toutes les 5 images | passe | OK | 3 |
| C teintes néon alternées toutes les 2 images, luminance proche | passe | OK | 0 |
| D rouge saturé / noir toutes les 2 images | échec (général + rouge) | ÉCHEC | 7 / 7 rouges |
| E noir/blanc toutes les 2 images sur un carré de 6 % de l'écran | v1 « passe » ; **corrigé : échec** | v1 OK (plein écran) ; **v2 ÉCHEC (fenêtre 1/3)** | 0 → 7 |
| F flash blanc 1 image, 1 par seconde (recette R4 kinetic) | passe | OK | 1 |
| G flash blanc 1 image, 4 par seconde (impacts sur croches à 120 BPM) | échec | ÉCHEC | 5 |

7/7 conformes au critère v1 (plein écran). **Correction de la même session** : le critère de surface du WCAG porte sur la pire fenêtre de 1/3 × 1/3 de l'écran (341×256 sur 1024×768), pas sur l'écran entier. Avec la v2 de l'outil (par défaut), E échoue, ce qui est juste : un carré qui clignote à 12,5 Hz occupe plus de 25 % de sa fenêtre locale. Ce que ça apprend au monteur :
- **Le flash d'une image compte pour un flash entier** (montée + descente). Un flash par impact est sûr à 1-2 impacts/s ; dès 4 impacts flashés par seconde, c'est hors norme (cas G). Dans un montage kinetic dense, réserver le flash au rang 1 (un par séquence).
- **L'effet stroboscopique sans risque passe par la teinte et la forme, pas la luminance** (cas C) : le principe Noé / Kan « une coupe = une rupture de forme » est compatible avec la norme si la luminance moyenne reste stable.
- ~~Petite surface = permis~~ **Faux** (corrigé) : une zone qui clignote ne passe que si elle reste sous ~25 % d'une fenêtre de 1/3 × 1/3 de l'écran, soit **moins de ~3 % de l'écran** si elle est concentrée. Un logo ou un mot de 6 % de l'écran qui clignote vite échoue.
- **Pièce 09** (générique) : la v3 « à luminance constante » passait à 0 flash en plein écran ; en fenêtre locale, **6 flashs, pire seconde 3 : à la limite**. Ce sont les grands mots clairs qui apparaissent et disparaissent qui comptent, pas le fond. Pour garder une marge : texte moins lumineux pendant les quarts de temps, ou cartons de 4 images au lieu de 3.

Limites : pas de motifs réguliers (rayures), pas d'HDR (BT.1702 : contraste de Michelson ≥ 1/17), fenêtre fixe à 1/3 de l'écran (sur un téléphone tenu près, le champ de 10° est plus petit que l'écran : à durcir), luminance d'écran supposée sRGB. Ofcom non lu (403).
