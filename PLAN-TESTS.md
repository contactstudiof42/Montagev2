# PLAN DE TESTS — exercices techniques courts dans After Effects et Blender

_Créé le 2026-10-13 (audit 2, section 8 d'`AUDIT-2.md`, exercices approuvés par Diego). Remplace `PLAN-TESTS-MCP.md`, archivé dans `archives/phase-3/` (environ 75 tests écrits pour un serveur MCP absent de ce Mac). Résultats de la session 0 de Resolve : `labo/mcp/resolve-mcp.md`. Une session d'exercice suit le démarrage de `CLAUDE.md`, puis ce fichier ; les règles de sécurité de `PROMPT-PHASE-3.md` s'appliquent._

## 1. Où en sont les skills (2026-10-13)
| Skill | Éprouvé | Seulement théorique | Ce qui le tranchera |
|---|---|---|---|
| `montage-after-effects` | expressions 01-11 : syntaxe et maths sous Node, avec un faux After Effects (2026-10-09) | tout le reste : rien n'a jamais tourné dans After Effects (courbe réelle d'`ease()`, F9, overshoot, `posterizeTime`, `seedRandom`, durées types, pilotage) | E0, E1, E2 |
| `montage-blender` | méthode et réglages en VM Linux, Blender 4.2.3, CPU (34 pièces d'atelier) | le Mac : Blender 5.2.2 LTS, GPU, API de 4.2 à 5.x, Eevee | E0, E3, E4 |
| `montage-motion-design-principes` | le titre de marque, jugé par Diego ; l'habillage vu sur 45 vidéos | les principes d'animation (paramètre qui porte le sens, asymétrie, matière, lisibilité) : maquettes | E1, E2 |
| `montage-pilotage-mcp` | Resolve par son MCP, sur deux projets | After Effects (ExtendScript par `osascript`, `aerender`) et Blender (ligne de commande, MCP) : jamais | E0 |

Sur le Mac (relevé le 2026-10-13) : After Effects 26.3.0 avec `aerender`, Blender 5.2.2 LTS, Premiere 26.3.0, Resolve Studio 21.1.1 ; seul serveur MCP de montage installé : Resolve.

## 2. La liste des moyens
_Préparée après l'application de l'audit 2, dans la même session : voir la section 6._

## 3. Où travailler
Fichiers de travail (projets `.aep` et `.blend`, rendus, mesures lourdes) dans `videos/phase-3/tests-techniques/_travail/` et `rendus/` (hors Git) ; brief des exercices dans `videos/phase-3/tests-techniques/brief.md` (le directeur artistique le lit) ; textes, journal, mesures et planches légères dans `projets-phase-3/tests-techniques/`. Rien d'acheté, aucun compte créé par moi.

## 4. La méthode commune à chaque exercice
1. **Intention et critères écrits avant le premier geste** (`montage-pilotage-mcp`).
2. **Construit par script** (ExtendScript ou bpy), rendu en images PNG, **mesuré hors du logiciel** ; quand un serveur MCP est installé, il sert à voir la scène ouverte et à vérifier chaque geste, le script à construire et à rendre.
3. **Un témoin raté**, rendu exprès, que la mesure doit attraper : sinon le contrôle ne prouve rien (« concevoir le contrôle pour qu'il puisse échouer »).
4. Pour ce qui touche au goût : **planche côte à côte avec la référence**, puis **directeur artistique à froid** (bande d'images du rendu à côté de celle de la référence), puis **une seule question à l'œil de Diego**.
5. Après l'exercice : les marqueurs des skills montent ([TESTÉ EN CONDITIONS RÉELLES], avec la date) ou la règle est corrigée ; un échec gagne une règle, et n'empêche pas les autres exercices.

L'outil de mesure du mouvement (`labo/outils/courbe_mouvement.py`, à écrire en E0) suit le centre d'un élément image par image (moyenne pondérée par l'alpha, sur fond uni) et trace position, vitesse et accélération en PNG : ma façon de « voir » une courbe d'animation, et de la comparer à celle de la référence mesurée de la même manière.

## 5. Les exercices

**E0 — Préalable : piloter les deux logiciels.**
Blender : rendre une image de test en ligne de commande sur le GPU du Mac ; relever le moteur, le temps par image, les identifiants d'API qui ont changé depuis la 4.2. After Effects : un script de dix lignes lancé par `osascript` crée une composition et l'enregistre ; `aerender` la rend en PNG ; `ffprobe` la lit. Si un serveur MCP est installé : `get` de l'état de la scène, une capture, une modification lue en retour. Résultat : une table « réussi / contourné / à la main » dans ce fichier, comme la session 0 de Resolve. Écrire `labo/outils/courbe_mouvement.py` et le vérifier sur un rendu synthétique dont la courbe est connue.

**E1 — After Effects : un titre qui se pose (3 s, 1920×1080, 25 i/s).**
Deux mots montent d'une vingtaine de pixels avec un fondu et un léger flou qui se résorbe, en 12 à 16 images, arrivée freinée (influence d'arrivée forte, de sortie faible), flou de mouvement activé, puis tenue.
Témoins : clés linéaires ; Easy Ease symétrique (F9).
Critères mesurés sur le rendu : (a) vitesse maximale dans le premier tiers du mouvement, décroissance continue, aucune vitesse négative (pas de rebond) ; (b) moins de 0,5 px par image sur les trois dernières images du mouvement, puis position stable à ±0,25 px pendant la tenue ; (c) sur l'image la plus rapide, le flou étale l'alpha d'au moins 1 px de plus qu'au repos ; (d) tenue d'au moins 1,5 s ; (e) les deux témoins sont distingués par la mesure.
Goût : planche des bandes d'images à côté de la référence choisie par Diego, directeur artistique à froid (« au niveau » ou « presque » attendu). La question de Diego : le titre se pose-t-il avec poids, ou flotte-t-il ?

**E2 — After Effects : overshoot et boucle par expressions (2 × 3 s).**
(a) Un carré passe de 0 à 100 % d'échelle en 12 images, clés linéaires, puis l'overshoot inertiel (recette 05). Critères : pic de 107 % ±1 point, deux images (±1) après la dernière clé, comme sous Node ; posé à 100 % ±0,5 avant une seconde. Témoin : dernière clé en Easy Ease → aucun dépassement (le piège « vitesse d'arrivée nulle »).
(b) Une boucle de 2 s (`loopOut("cycle")`) et un `wiggle` figé par `seedRandom`. Critères : images 0 et 50 identiques (écart moyen < 0,5/255) ; deux rendus successifs identiques ; vitesse continue à la jointure ; `posterizeTime(8)` à 25 i/s donne des tenues de 3 et 4 images.
Pas de jugement de goût : cet exercice confirme ou corrige mes recettes (les onze vérifications de l'ancienne liste « À vérifier dans After Effects »).

**E3 — Blender : un packshot dans le noir (5 s, 1920×1080, 25 i/s).**
Une sphère chromée et un petit objet mat sur un sol noir brillant ; deux softbox émissives invisibles à la caméra ; travelling avant lent, accéléré puis freiné ; vue AgX. Une image de test avant le rendu complet.
Témoins : sans les softbox (chrome noir) ; caméra linéaire.
Critères mesurés sur le rendu : (a) au moins deux reflets de softbox lisibles sur la sphère, et la sphère nettement plus lumineuse que dans le témoin, qui doit échouer ; (b) au plus 0,5 % des pixels à 250 ou plus (des reflets ponctuels seulement), et le blanc maximal relevé, pour confirmer ou corriger « AgX plafonne vers 222 » ; (c) noirs du fond au 5e centile ≤ 10/255, sans bruit visible une fois amplifiés six fois ; (d) diamètre apparent de la sphère monotone, vitesse maximale vers le milieu du mouvement, aucune image dont la vitesse saute de plus de 20 % par rapport à ses voisines ; (e) même image 0 sur deux rendus ; temps par image relevé.
Goût : planche côte à côte avec la référence choisie par Diego, directeur artistique à froid. La question de Diego : ça fait CG, ou cheap ?

**E4 — Blender : une chute calée à l'image (3 s).**
Un objet tombe sur une table et rebondit deux fois, par clés calculées ; l'impact tombe exactement à l'image 40 ; flou de mouvement ; un son d'impact posé à l'image 40.
Témoin : un objet qui traverse le cadre en une image (il doit disparaître dans le flou, ce qui confirme « ralentir l'objet ou rapprocher la caméra »).
Critères mesurés : (a) image de contact = 40, sans pénétration de la table (à 1 px près sur toutes les images) ; (b) hauteurs des rebonds dans le rapport prévu, à ±10 % ; (c) flou présent aux images rapides, et objet lisible sur chaque image (aire au moins la moitié de l'aire au repos) ; (d) attaque du son à 1,600 s ±1 ms ; −14 LUFS ±0,5 et crête ≤ −1 dBTP sur le fichier encodé.
La question de Diego (à l'œil et à l'oreille) : la chute a-t-elle du poids, l'impact tombe-t-il juste ?

**E5 — Assemblage et livraison (8 s).**
Le rendu de E3 en fond, le titre de E1 composé dans After Effects, un étalonnage simple, livré en master du studio (H.265 Main 10) et en H.264 pour le web.
Critères : (a) pas de double conversion : un gris à 18 % rendu dans Blender sort à la valeur Rec.709 attendue, à ±2 codes près ; (b) titre lisible : contraste d'au moins 4,5:1 avec le fond sous le texte ; (c) master : hevc, Main 10, `yuv420p10le`, BT.709 ; web : High, `yuv420p`, faststart ; autant d'images que la composition, aucune perdue ni doublée ; (d) PSNR du master contre un PNG 16 bits ≥ 40 dB, noirs amplifiés six fois sans bloc.
Goût : directeur artistique à froid sur la planche finale.

## 6. La liste des moyens et les références à choisir
_À préparer (étape suivante de la session du 2026-10-13)._
