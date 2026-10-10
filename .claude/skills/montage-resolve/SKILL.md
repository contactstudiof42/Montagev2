---
name: montage-resolve
description: DaVinci Resolve — étalonnage par nodes (série, parallèle, layer mixer), gestion des couleurs (RCM, DaVinci Wide Gamut / Intermediate, ACEScct), page Deliver et rendus, Fusion, Fairlight, et automatisation par l'API de scripting Python (resolve.GetProjectManager, MediaPool.AppendToTimeline, SetRenderSettings, AddRenderJob, SetLUT, ApplyGradeFromDRX, export EDL/XML/AAF). Mots d'un étalonneur ou d'un monteur : « on passe en étalo », « arbre de nodes », « monter un look », « node de correction primaire », « qualifier la peau », « power window », « rendu en lot », « automatiser l'export », « script Resolve », « conformation », « faire un round-trip Premiere-Resolve ».
---

# DaVinci Resolve

Rôle : l'étape où l'image prend son **intention de couleur** (`montage-couleur-et-intention`) et où la chaîne technique est tenue propre (`montage-couleur-pipeline`). Ce skill dit comment l'organiser et l'automatiser.

## 1. Quand et pourquoi Resolve
- **Étalonnage** : c'est l'outil de référence (nodes, qualifications, tracking de fenêtres, gestion des couleurs de bout en bout). Premiere Lumetri suffit pour un corporate homogène ; dès qu'il y a un **look** à construire, une peau à protéger dans une dominante « fausse » (goût de l'utilisateur : Joker), des fenêtres à suivre, c'est Resolve.
- **Conformation / round-trip** : monter dans Premiere, exporter XML/AAF, étalonner dans Resolve, rendre en master 10 bits (cf. `labo/encodage/` : le 10 bits évite les bandes dans les noirs).
- **Automatisation** : rendus en lot, import et assemblage d'une liste de plans, application d'une LUT ou d'un grade à toute une timeline. C'est la porte d'entrée d'un agent en phase 2 si aucun MCP Resolve n'est branché.

## 2. Arbre de nodes de référence [THÉORIQUE — à éprouver en phase 2]
Ordre défendu (une idée par node, lisible par un autre étalonneur) :
1. **Entrée / normalisation** (si pas de RCM) : CST log caméra → espace de travail.
2. **Balance / exposition primaire** (Offset d'abord en log, puis Lift/Gamma/Gain).
3. **Contraste et courbe** (pivot réglé sur la valeur moyenne du sujet).
4. **Correction secondaire de peau** (qualifieur + fenêtre suivie) : c'est elle qui permet de garder un environnement vert sodium sans rendre le visage malade.
5. **Fenêtres de relief** (vignettage motivé, ramener l'œil sur le sujet).
6. **Look** (node parallèle ou LUT créative à opacité réglée par la clé du node).
7. **Grain / texture** en dernier (après le look, avant la sortie).
8. **Sortie** : CST ou ODT de l'espace de travail vers Rec.709 Gamma 2.4 (ou 2.2 pour le web, à décider : voir `montage-couleur-pipeline`).
Pourquoi cet ordre : corriger avant de styliser ; un look appliqué sur une image non balancée réagit différemment d'un plan à l'autre.

**Leçons de l'atelier 05 (étalonnage simulé en numpy, `atelier/05-trois-etalonnages/grade.py`)** [TESTÉ EN ATELIER, hors Resolve] :
- Une secondaire qui doit faire vivre une couleur ne se place **ni avant** un node qui écrase (elle est écrasée avec le reste) **ni après** (la couleur à qualifier n'existe plus) : on prend la **clé sur l'entrée** (node parallèle ou clé externe branchée sur la source) et on mélange en sortie. Mesuré : 0 % → 1,7 % de pixels chauds, 0 % hors de l'objet.
- Des gammas un peu différents par canal sur une image grise (0,75 / 0,80 / 0,78) fabriquent une dominante forte : préférer le gamma maître + une balance séparée.
- Qualifier un objet fin et sombre (pieds de chaise rouillés à v ≈ 0,15) ne prend que ses **bords** : liseré coloré. Remèdes : remonter la matière au tournage, clean black / blur de la clé, ou fenêtre + qualifieur.
