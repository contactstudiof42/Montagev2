# Pièce 24 « Face caméra » — critique (session 20, 2026-10-10)

Commande : `python3 piece.py ../rendus/24 [--versions A,B,A0,C,D,E] [--sway 1.0]` puis `python3 planche.py ../rendus/24 V sortie.png` (chaque coupe = paire « dernière image avant / première image après », avec le type d'événement). Mesures dans `../rendus/24/<V>-events.json` (non versionné ; relancer le script, 40 s).

Prise brute : 34 s, 13 segments (8 phrases gardées, 2 ratés, 2 silences, 1 phrase recommencée). Les montages durent 28 s.

## Mesures (v1)
| Version | Dérushage | Traitement | Événements | /min | Déplacement du sujet aux sauts (% de largeur) |
|---|---|---|---|---|---|
| A | serré (chaque respiration coupée) | jump cuts, cadre fixe | 8 | 17,2 | 7,0 · 3,0 · **0,2** · 2,3 · **1,0** · **0,2** · **0,7** · **0,4** |
| B | serré | punch-in alterné 100/125 % | 8 | 17,2 | (changement d'échelle à chaque coupe) |
| A0 | minimal (ratés et silences seulement) | jump cuts | 4 | 8,4 | 7,0 · 3,0 · 2,3 · 1,0 |
| C | minimal | punch-in 130 % sur les 3 chutes | 7 | 14,7 | |
| D | minimal | C + 2 plans de coupe (REC, carnet) | 8 | 16,8 | |
| E (v2) | minimal | C, 1re image du punch-in hors clignement | 7 | 14,7 | |

## Verdict par version
- **A (jump cuts serrés)** : 5 des 8 sauts déplacent la tête de **moins de 1 % de la largeur** (1 à 6 px en 640). Sur planche, la paire avant/après est presque identique : ce n'est plus un jump cut, c'est **une image qui saute**, une panne de lecture. Un jump cut se lit comme intention quand il **se voit** (7 % à la coupe du raté) ; en dessous de ~2 %, il se lit comme erreur. Les respirations coupées produisent justement les micro-sauts (le corps n'a pas eu le temps de bouger) ; et elles ne font gagner que 0,6 s sur 28 (2 %) dans cette prise.
- **B (alternance mécanique)** : aucun micro-saut (chaque coupe change d'échelle), mais **la parité décide de l'emphase** : la chute finale « Bouger, c'est déjà oublier » tombe sur le **plan large** (k pair), et « Alors, un conseil » sur le serré. Toutes les phrases ont le même poids ; le serré ne veut plus rien dire. C'est le « papier peint » du face caméra.
- **A0 (minimal)** : 8,4 événements/min, propre mais plat : rien ne désigne les chutes.
- **C (punch-in sur les chutes)** : la hiérarchie est là (3 punch-ins = les 3 idées fortes). Défaut vu sur planche : la 1re image du 1er punch-in (« C'est que la mémoire… débranchée ») a **les yeux fermés** (clignement). Un punch-in qui s'ouvre sur un clignement rate l'adresse au spectateur : le regard caméra est ce qu'on vient chercher en serrant.
- **D (B-roll métaphore)** : le voyant REC qui s'éteint porte l'idée (« rien ne l'enregistre ») mieux que n'importe quelle illustration de molécule ; mais le REC couvre la phrase « noradrénaline », et c'est la phrase **suivante** (« rien ne l'enregistre ») qui en aurait besoin : **le plan de coupe métaphorique doit tomber sur la phrase qui énonce la métaphore**, pas sur la phrase technique qu'il remplace. À corriger en v3 (REC sur le segment 9). Le carnet, lui, est littéral : il illustre (« gardez un carnet ») et vole la chute qui suit son retour au visage. Ma règle « métaphore, pas illustration » tient pour le REC, pas pour le carnet.
- **E (v2)** : en retardant la coupe hors du clignement, l'image *avant* la coupe tombe **sur** le clignement : on coupe juste après que les yeux se rouvrent. C'est exactement la règle de Murch (*In the Blink of an Eye* : le clignement ponctue la fin d'une pensée ; couper là où l'on cligne). Le punch-in paraît « naturel » sur planche. Effet de bord : la 3e chute est retardée de 0,28 s (le punch arrive au milieu de « c'est déjà oublier ») : acceptable seulement parce qu'il tombe sur le mot-clé « oublier » ; sinon, chercher le clignement **avant** la coupe (décalage négatif). À rendre symétrique en v3.

## Leçons (versées dans `montage-youtube`)
1. **Seuil du jump cut** : mesurer le déplacement du sujet. Sous ~2 % de la largeur, le jump cut se lit comme une erreur : soit on ne coupe pas (garder la respiration), soit on change d'échelle, soit on couvre. Au-dessus de ~5 %, il se lit comme un geste. (Seuils de ma marionnette, à vérifier sur un vrai visage en phase 2.)
2. **Couper chaque respiration** est la source des micro-sauts et rapporte très peu de temps : dans une prise déjà vive, ne couper que les ratés et les silences.
3. **Le punch-in est une hiérarchie, pas un cache-coupe** : l'alternance mécanique donne l'emphase au hasard (la chute finale sur le large).
4. **La 1re image d'un serré ne cligne pas** ; idéalement, la coupe tombe juste après un clignement (Murch).
5. **Le plan de coupe métaphorique se pose sur la phrase de la métaphore**.

## Limites
Marionnette 2D, voix synthétique, aucune écoute. Les seuils en % sont ceux d'une tête qui se balance de ±20 px sur 960 ; un vrai corps bouge plus (et autrement : épaules, mains). Événements/min = frontières de plans, sans pondération (un saut de 0,2 % compte comme un punch-in) : la vraie fatigue n'est pas mesurée.

## v3 (à faire)
REC sur « rien ne l'enregistre » ; carnet remplacé ou supprimé ; décalage de coupe vers le clignement le plus proche, avant ou après ; version 9:16 (le punch-in vertical recadre autrement) ; même pièce avec `--sway 2.5` (corps plus mobile) pour voir si le seuil se déplace.
