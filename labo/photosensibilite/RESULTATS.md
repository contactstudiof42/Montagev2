# Labo photosensibilité (session 7, 2026-10-10) — [TESTÉ EN LABO]

But : un contrôle de montage qui repère les séquences à risque **avant** le test officiel (Harding FPA exigé par l'ASA au Royaume-Uni pour la pub ; seuils WCAG 2.1 SC 2.3.1 et ITU-R BT.1702-3, voir `culture/enter-the-void-generique-noe-tom-kan.md`, section Risques). Ce n'est pas un outil de certification.

Commande : `python3 -I labo/photosensibilite/flash_check.py video.mp4 [--fps 25]` ; vérités terrain : `sh tests.sh` (depuis ce dossier, ~5 s).

| Cas (2 s, 25 i/s) | Attendu | Résultat | Pire seconde |
|---|---|---|---|
| A noir/blanc toutes les 2 images | échec | ÉCHEC | 7 flashs |
| B noir/blanc toutes les 5 images | passe | OK | 3 |
| C teintes néon alternées toutes les 2 images, luminance proche | passe | OK | 0 |
| D rouge saturé / noir toutes les 2 images | échec (général + rouge) | ÉCHEC | 7 / 7 rouges |
| E noir/blanc toutes les 2 images sur 10 % de l'écran | passe (surface) | OK | 0 |
| F flash blanc 1 image, 1 par seconde (recette R4 kinetic) | passe | OK | 1 |
| G flash blanc 1 image, 4 par seconde (impacts sur croches à 120 BPM) | échec | ÉCHEC | 5 |

7/7 conformes. Ce que ça apprend au monteur :
- **Le flash d'une image compte pour un flash entier** (montée + descente). Un flash par impact est sûr à 1-2 impacts/s ; dès 4 impacts flashés par seconde, c'est hors norme (cas G). Dans un montage kinetic dense, réserver le flash au rang 1 (un par séquence).
- **L'effet stroboscopique sans risque passe par la teinte et la forme, pas la luminance** (cas C) : le principe Noé / Kan « une coupe = une rupture de forme » est compatible avec la norme si la luminance moyenne reste stable.
- **Petite surface = permis** (cas E) : un élément qui clignote dans un coin n'est pas un flash plein écran. L'outil approxime la règle de surface (25 % du champ de 10°) par « 25 % de l'écran » : **plus permissif** que le vrai critère sur grand écran ou téléphone tenu près ; à durcir pour du vertical.

Limites : pas de motifs réguliers (rayures), pas d'HDR (BT.1702 : contraste de Michelson ≥ 1/17), surface approximée, luminance d'écran supposée sRGB. Ofcom non lu (403).
