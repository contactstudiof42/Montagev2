---
name: montage-after-effects
description: Faire bouger juste dans After Effects, et piloter After Effects par script ou par MCP — easing, Graph Editor (courbes de vitesse et de valeur), influence des clés, Easy Ease (F9), anticipation, overshoot, rebond, flou de mouvement, expressions (wiggle, loopOut, valueAtTime, posterizeTime, time remap, compteur), rigs à sliders, organisation de comp (précomps, nulls), ExtendScript, aerender. Mots d'un motion designer : « ça fait amateur », « ça manque de poids », « c'est mou », « trop linéaire », « ça claque pas », « boucle propre », « ça rebondit trop », « fais-le trembler ». Quoi animer et pourquoi : `montage-motion-design-principes`.
---

# After Effects : le mouvement d'abord

_Réécrit le 2026-10-13 (audit 2). **Statut honnête** : After Effects a été piloté en conditions réelles sur des projets du cabinet (2026-10-21 à 2026-10-29) ; ce qui y a été appris est au § 6. Hors l'E0 (une composition de test) et ce § 6, le reste du skill n'a pas encore été confronté au logiciel. Les expressions 01 à 11 sont vérifiées sous Node avec un faux After Effects (syntaxe et maths, `labo/ae-expressions/RESULTATS.md`), pas dans le logiciel ; tout le reste est [THÉORIQUE] jusqu'aux exercices E0 à E2 de `PLAN-TESTS.md`. Recettes, durées types, réglages, saccade et pièges : [expressions.md](expressions.md). Version d'avant : `archives/audit-2/skills/montage-after-effects/`._

**Fait foi sur** : la technique du mouvement dans After Effects (courbes, expressions, rigs) et son pilotage sur ce Mac. Quoi animer : `montage-motion-design-principes` ; méthode générale de pilotage : `montage-pilotage-mcp` ; saccade dans Premiere ou Resolve : `montage-premiere`, `montage-resolve`.

**Avant de régler une courbe** : choisir *quoi* animer (le paramètre qui porte le sens, un seul signe) avec `montage-motion-design-principes`. La plus belle courbe sur le mauvais paramètre (l'échelle d'un mot) reste un « pulse » de logo [ÉPROUVÉ EN MAQUETTE] (atelier 01).

## 1. Ce que le mouvement raconte [THÉORIQUE jusqu'aux exercices E1 et E2]
- **Le poids, c'est l'accélération.** Un objet lourd démarre lentement et s'arrête lentement ; un objet léger démarre sec. Une sortie de clé très tirée (forte influence) donne du poids ; une sortie courte donne de la nervosité.
- **L'anticipation prépare l'œil** : 2 à 4 images de recul (quelques pixels, quelques %) avant un départ rapide.
- **L'overshoot dit la matière** : fréquence haute et amortissement fort = métal, plastique dur, interface ; fréquence basse, peu amorti = gélatine, cartoon ; pas d'overshoot = verre, pierre, luxe, sobriété.
- **L'Easy Ease par défaut est sans opinion** : F9 pose une vitesse nulle avec une influence d'environ 33 % des deux côtés, une courbe symétrique et molle. Partir de F9 puis tirer les poignées (60 à 90 % d'influence côté arrivée pour un arrêt « luxe »).
- **L'asymétrie entrée / sortie** : départ vif et arrivée longue (interface, apparition), ou départ lent et arrivée sèche (impact, chute).
- **Le ralenti avant l'arrêt** : les 30 à 40 % finaux d'un mouvement d'arrivée portent la décélération ; un arrêt net sur une vitesse non nulle se lit comme un bug, sauf impact voulu.
- **Vitesse et valeur** : timing et poids dans le graphe de vitesse ; trajectoires, dépassements et arcs dans le graphe de valeur (dimensions séparées).
- **Le temps de lecture** : un mouvement qui finit laisse au moins 0,5 à 1 s de tenue avant le suivant.

## 2. La méthode, adaptée à ce que je perçois
1. Poser les clés en linéaire et régler le timing d'abord : si c'est faux en linéaire, l'easing ne sauvera rien.
2. F9 partout, puis tirer les poignées selon la matière (au chiffre près : vitesse et influence de chaque clé ; par script, `setTemporalEaseAtKey` avec des `KeyframeEase`).
3. Relire les valeurs posées à quelques instants (pas de dépassement involontaire, pas de plateau parasite).
4. Ajouter la vie (anticipation, overshoot, décalage de 2 à 4 images entre éléments), jamais tout en même temps.
5. Flou de mouvement sur tout ce qui va vite : à 25 i/s, un mouvement rapide sans flou paraît saccadé.
6. **Juger** : je ne vois pas la vitesse réelle. Rendre toutes les images, mesurer la courbe de position et de vitesse sur le rendu (`labo/outils/courbe_mouvement.py`, à écrire en E0), regarder la bande d'images, comparer à la référence mesurée de la même manière ; puis le directeur artistique à froid, puis l'œil de Diego (carte des sens, `CLAUDE.md`).

## 3. Piloter After Effects sur ce Mac [THÉORIQUE, à éprouver en E0]
- Installé : After Effects 26.3 (« Adobe After Effects 2026 »), `aerender` et le plugin Higgsfield (relevé le 2026-10-13). Choix de Diego (2026-10-13) : le MCP de Higgsfield pour construire, modifier et voir le projet ; le script (ExtendScript, `aerender`) quand c'est plus fiable ou plus mesurable. Ce MCP passe par les serveurs de Higgsfield : ses règles sont dans `montage-pilotage-mcp` (règle 12) ; ce que ses outils font vraiment, ce qui consomme des crédits et ce qui transite : `PLAN-TESTS.md` (6.7, rempli en E0). Réglages d'After Effects et autorisations de macOS : `PLAN-TESTS.md`, liste des moyens.
- **Construire** : un script ExtendScript (`.jsx`) lancé par `osascript -e 'tell application "Adobe After Effects 2026" to DoScriptFile "/chemin/script.jsx"'`, After Effects ouvert ; il crée la composition, pose les clés et les expressions, enregistre le projet (`.aep`) dans `_travail/`.
- **Rendre** : `"/Applications/Adobe After Effects 2026/aerender" -project <fichier.aep> -comp "<nom>" -output <dossier>/img_[#####].png` (modèle de module de sortie à vérifier en E0), puis mesurer hors du logiciel (`ffprobe`, courbes, planches).
- Écrire pour le moteur JavaScript ; nommer calques, précomps et contrôleurs : Diego doit pouvoir reprendre le projet sans moi.

## 4. Organisation de projet et rigs
- Arborescence : `00_COMPS_FINALES`, `01_PRECOMPS`, `02_RIGS`, `03_ASSETS`, `99_ARCHIVES` ; les comps finales portent le format et la version (`TITRE_16x9_v03`).
- Un calque `CTRL` (null ou calque d'effets) porte les sliders, cases et couleurs du rig ; les expressions pointent vers `thisComp.layer("CTRL").effect("…")`.
- Les nulls parents portent le mouvement global, les enfants le détail (« un mouvement, un calque ») ; les précomps isolent ce qui se réutilise, et se calent sur la musique sans casser l'easing interne.

## 5. Les deux pièges qui coûtent le plus
- **Vitesse d'arrivée nulle = pas d'overshoot** : une clé en Easy Ease arrive à vitesse nulle ; l'overshoot inertiel exige une arrivée avec de la vitesse (clés linéaires ou sortie peu amortie). Cause n° 1 de « mon expression ne fait rien ».
- **Bézier spatial non voulu** : le calque boucle ou dépasse dans l'espace ; interpolation spatiale linéaire.
Les autres pièges (moteur, expressions lentes, `exp()` qui explose, période qui varie dans un `sin`, wiggle dupliqué) : [expressions.md](expressions.md).

## 6. Ce que le pilotage réel a appris (projets du cabinet, 2026-10) [TESTÉ EN CONDITIONS RÉELLES]
Leçons validées par Diego (`/Users/diego/Post-prod clients/LECONS-A-REMONTER.md`), intégrées le 2026-10-29. Ce qu'il faut animer (carton titre, frise) : `montage-motion-design-principes` § 5.
- **Frise ou défilement à plusieurs jalons** : un null de travelling, parent de nulls de jalon qui portent un curseur « focus » calculé par expression (distance au centre de l'image), pilote d'un coup taille, position, flou et luminosité de chaque date et image. Une précomp par jalon, dupliquée, dont la date vient du nom de la comp (`thisComp.name`).
- **Pièges du MCP** : `replace_source` garde le point d'ancrage et la durée de l'ancien rush (les recaler) ; « Output White » des Niveaux n'accepte pas d'expression (passer par un effet Exposition) ; le tracé d'un calque de forme ne se modifie pas après coup (recréer le calque) ; un calque dupliqué se place sous l'original ; le rendu emporte le son de tous les rushs (rendre ou exporter sans son).
- **Allonger une comp par script** : changer la durée de la comp ne rallonge pas les calques ; repousser aussi le point de sortie de tous les calques, dans chaque précomp. Décaler une fin déjà animée sans retoucher les clés : `valueAtTime(linear(time, nouveau_début, nouvelle_fin, ancien_début, ancienne_fin))` rejoue les anciennes clés aux nouveaux temps.
- **Retiming par time remap décalé** (« début + time ») [universel] : quand le rythme change, chaque jalon apparaît à un autre moment, donc pioche un autre passage de la source. Revérifier chaque jalon après un retiming : un extrait peut tomber avant le début du fichier (image noire), sur une coupe, ou sur un plan à bandes noires.
- **SFX calés sur le mouvement** : la vitesse se lit image par image dans les clés ou la table d'expression du travelling (`montage-son-et-emotion` § 5).
