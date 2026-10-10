# Labo YouTube (session 17)

## 1. Validateur de chapitres — [TESTÉ EN LABO]
`chapitres.py description.txt DUREE_S [--ffmeta out.txt]` applique les règles de l'aide YouTube (consultée le 2026-10-10) : premier horodatage à 00:00, au moins 3, ordre croissant, 10 s minimum. Cas valide (5 chapitres sur 13 min) accepté ; cas fautif (début à 0:05, 2 chapitres, un de 7 s) refusé avec les trois raisons, code de sortie 1. Le FFMETADATA produit, muxé par ffmpeg (`-map_chapters`), est relu à l'identique par ffprobe (3 chapitres, bornes exactes au ms). YouTube lit les chapitres dans la **description**, pas dans le fichier : les chapitres du MP4 servent aux autres lecteurs.

## 2. Banc de lisibilité des miniatures — résultat négatif pour l'OCR, résultat à l'œil
**Méthode** (`miniature.py`) : miniature 1280×720, Inter Black en capitales, hauteur de capitale 6 / 9 / 12 / 16 / 22 % de la hauteur, trois styles (blanc plein, blanc à contour noir, bandeau jaune texte noir), trois textes (2, 4, 8 mots), deux fonds (dégradé sombre uni ; texture colorée à haute fréquence, pire cas), réduite à 168×94, 246×138 et 360×202 (tailles d'affichage de mémoire, à vérifier), puis OCR tesseract.

**L'OCR ne mesure pas la lisibilité ici, et je le dis** (trois versions, `resultats-v1-sans-recadrage.tsv`, `resultats-v2-x4.tsv`, `resultats.tsv` + `tableau-v3.txt`) :
- v1 (image entière) : la texture est lue comme des lettres, ~0,3 partout.
- v2 (bande du texte, ×4) : les scores **baissent quand le texte grossit** (tesseract ne lit plus des lettres de 300 px).
- v3 (capitale ramenée à ~30 px) : encore incohérent : 5,6 px de capitale « lus » parfaitement, un bandeau de 16 % « illisible ». Un proxy qui ne croît pas avec la taille ne classe rien.

**Jugement à l'œil** (`planche-168px.png` : tous les cas à 168×94, affichés ×2 ≈ un écran Retina ; à 1× strict ce serait plus dur) :
| | fond uni | fond chargé (pire cas) |
|---|---|---|
| blanc plein | lisible dès 9 % ; 6 % se lit mais n'existe pas (une ligne de légende) | **mangé** à 6-9 % ; lisible à partir de 12 % |
| contour noir | idem plein | aide nettement dès 9 % |
| bandeau jaune | lisible à toutes les tailles | **le seul style lisible à toutes les tailles**, même à 6 % |
- **8 mots** : lisibles à 9-12 % sur fond uni, mais à 168 px c'est une phrase à lire, pas un coup d'œil, et elle occupe la moitié de l'image : la miniature devient un carton.
- **À 16-22 %**, le retour à la ligne automatique coupe au mauvais endroit (« J'AI TESTÉ LE / PIRE », « IL A / MENTI ») : en grand, la coupure de ligne se décide à la main, par le sens.
- Coût : 51 s pour 234 cas une fois tesseract limité à 1 fil (`OMP_THREAD_LIMIT=1`) ; plusieurs minutes et des blocages quand plusieurs tesseract multi-fils se disputent les 4 cœurs.

**Règles retenues** [TESTÉ EN LABO à l'œil, sur fonds synthétiques ; à valider sur de vraies miniatures avec visage, PLAN-TESTS 63] :
1. Le texte d'une miniature se dimensionne **à 168 px de large**, pas à 1280 : capitale ≥ 12 % de la hauteur sur une image chargée, ≥ 9 % sur une image calme.
2. **2 à 4 mots** : au-delà, la miniature devient un carton à lire.
3. Sur une image chargée (foule, décor, feuillage), **un fond sous le texte** (bandeau, aplat, zone floutée) plutôt qu'un contour ; le contour suffit sur une image calme.
4. En grande taille, **couper la ligne à la main** selon le sens.
5. La miniature dit autre chose que le titre (complément, pas répétition : principe des fiches, non testé ici).

Pièges : `pgrep -f motif` dans une boucle `until` se trouve lui-même (la boucle ne finit jamais) ; et `pkill -f` tue le shell qui l'appelle (déjà noté en session 15). Une commande lancée avec `&` dans un appel Bash **survit** à la fin de l'appel : deux copies du banc ont tourné en parallèle sur le même fichier.
