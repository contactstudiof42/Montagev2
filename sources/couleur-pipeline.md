# Sources : pipeline couleur (consultées le 2026-10-09)

Statut : « joignable » = l'URL a répondu HTTP 200 depuis le labo le 2026-10-09 (contenu non relu en détail faute de temps). « 403 » = bloquée par le proxy du labo (GitHub), pas forcément morte.

## Bibliothèques testées

| Source | URL | Statut | Usage |
|---|---|---|---|
| colour-science, site | https://www.colour-science.org/ | joignable | Projet, installation |
| colour-science, documentation | https://colour.readthedocs.io/en/latest/ | joignable | `RGB_to_RGB`, `log_encoding`, `RGB_COLOURSPACES`, `LUT3D` |
| colour `write_LUT` | https://colour.readthedocs.io/en/latest/generated/colour.write_LUT.html | joignable | Écriture .cube (Resolve/IRIDAS) |
| OpenColorIO, site | https://opencolorio.org/ | joignable | Projet ASWF |
| OpenColorIO, documentation | https://opencolorio.readthedocs.io/en/latest/ | joignable | API Python, configs intégrées (`CreateFromBuiltinConfig`) |
| Configs OCIO ACES (cg/studio) | https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES | 403 via proxy | Noms des espaces (« ARRI LogC3 (EI800) », « S-Log3 S-Gamut3.Cine »…) ; vérifiés en local via OCIO 2.6.0 |
| ffmpeg, filtre `lut3d` | https://ffmpeg.org/ffmpeg-filters.html#lut3d-1 | joignable | Formats acceptés (.cube, .3dl, .dat, .m3d, .csp), `interp=tetrahedral` |

## ACES et normes

| Source | URL | Statut | Usage |
|---|---|---|---|
| ACES Central (communauté AMPAS) | https://acescentral.com/ | joignable | Forum, annonces ACES 2.0 |
| Documentation ACES | https://docs.acescentral.com/ | joignable | Spécifications ACEScg, ACEScct, transformations de sortie |
| Code de référence ACES | https://github.com/ampas/aces-dev | 403 via proxy | CTL de référence |
| ITU-R BT.709 | https://www.itu.int/rec/R-REC-BT.709 | joignable | Primaires et OETF Rec.709 |
| ITU-R BT.1886 | https://www.itu.int/rec/R-REC-BT.1886 | joignable | EOTF d'écran de référence (≈ gamma 2.4) |
| ITU-R BT.2020 | https://www.itu.int/rec/R-REC-BT.2020 | non testée | Primaires Rec.2020 |
| IEC 61966-2-1 (sRGB) | norme payante (IEC webstore) | non consultée | Fonction sRGB par morceaux ; implémentation colour utilisée |
| Spécification Adobe Cube LUT 1.0 | https://kono.phpage.fr/images/a/a1/Adobe-cube-lut-specification-1.0.pdf | joignable (copie tierce) | Format .cube ; rechercher la copie officielle Adobe en phase 2 |

## Constructeurs (à compléter en phase 2)

- ARRI LogC3 / LogC4 : l'URL « image science » testée renvoie 404 (page déplacée). Formules utilisées : implémentation colour-science (`ARRI LogC3`, EI800 par défaut). À retrouver sur arri.com.
- Sony S-Log3 / S-Gamut3.Cine : livre blanc technique Sony (non consulté ce jour) ; implémentation colour-science utilisée.

## Non vérifié

- Version ACES (1.3 ou 2.0) livrée par la version de Resolve et d'After Effects utilisée en phase 2.
- Cause exacte de l'écart de 2e-3 entre colour et OCIO sur LogC3/S-Log3 (hypothèse : passage par AP0 et matrices IDT dans OCIO).
