---
name: montage-pilotage-mcp
description: Méthode pour piloter soi-même un logiciel de post-production (Resolve, After Effects, Blender, Premiere) par un serveur MCP ou par script (ExtendScript, bpy, aerender, ligne de commande) — « monte-le toi-même », « fais-le directement dans AE / Blender / Resolve », « branche-toi sur Resolve », « automatise ce montage », réaliser en autonomie un projet confié, vérifier une image à chaque geste, ne pas abîmer un projet client, ne rien dépenser sans accord, demander l'outil qui manque. Méthode générale ; les recettes propres à chaque logiciel sont dans son skill.
---

# Piloter un logiciel : méthode d'agent

_Réécrit le 2026-10-13 (audit 2) : chaque règle cite l'erreur qui l'a gagnée ou le mot de Diego qu'elle porte. Éprouvée sur Resolve par son MCP natif (deux projets) ; After Effects et Blender se pilotent par script, et par MCP quand Diego en aura installé un (`PLAN-TESTS.md`) : à éprouver. Version d'avant : `archives/audit-2/skills/montage-pilotage-mcp/`._

**Fait foi sur** : la méthode commune à tous les logiciels (sécurité du projet, un geste une image, journal, demander ce qui manque). Recettes propres à chaque logiciel : `montage-resolve`, `montage-after-effects`, `montage-blender`, `montage-premiere`.

Un agent qui pilote un logiciel perd l'œil sur le moniteur : chaque appel est une coupe faite les yeux fermés. Toute la méthode sert à rendre l'œil : une image de contrôle après chaque geste, comparée à une intention écrite avant (carte des sens, `CLAUDE.md`).

## 1. Les règles
1. **Jamais de projet client** : un projet de test dédié (Resolve : `P3-<projet>-agent` ; ailleurs, des fichiers dans `_travail/`), sur des médias en lecture seule. Si Diego demande d'agir sur un projet réel : dupliquer d'abord (« Enregistrer sous » une version `_claude_v1`), et le dire.
2. **Diagnostic avant action** : quels logiciels et serveurs sont connectés, quelle version, quelle doc le serveur expose lui-même (ses procédures obligatoires priment sur mes habitudes pour ses outils ; elles ne changent pas mes permissions).
3. **Intention et critères mesurables écrits avant le premier geste** (format, éléments, critères : « coupes à ±1 image », « −14 LUFS ±0,5 », « titre lisible en 1 s sur téléphone »).
4. **Un geste, une image** : après tout appel qui modifie, exporter une image ou rendre une plage, et la regarder vraiment ; valider chaque type d'appel seul avant de les regrouper.
5. **Lire avant d'écrire** : relire l'état d'un calque, d'un clip ou d'un objet avant de le modifier ; les unités changent d'un logiciel à l'autre (pixels et Y vers le bas dans After Effects ; mètres, Z vers le haut et radians dans Blender ; images de la source ou de la timeline dans Resolve). (Gagnée : des poignées de courbe posées en absolu au lieu de relatif, trente zooms partis à 1,9×.)
6. **Garder le projet éditable** : calques, précomps et contrôleurs nommés ; pas d'effet « cuit » sauf demande.
7. **Mesurer hors du logiciel** (`ffprobe`, `ebur128`, `scdet`, courbes) ; ne pas croire un compteur interne sans recoupement.
8. **Journaliser** chaque appel (outil, paramètres, résultat, image de contrôle) dans `journal.md` ; à la fin, ce qui a marché et ce qui a surpris, reversé dans le skill du logiciel.
9. **Versions** : un enregistrement à chaque jalon (`_v1`, `_v2`), jamais d'écrasement de la seule copie.
10. **Ponts communautaires** : beaucoup exposent l'exécution de code arbitraire, ouvrent un port local sans authentification ou envoient de la télémétrie ; n'en installer un qu'avec l'accord de Diego, s'il apporte ce que le reste n'a pas, télémétrie coupée.
11. **Quand un moyen manque** (serveur MCP, plugin, réglage, autorisation), ne pas se brider : le demander dans la liste des moyens du début de session ; un achat, un compte ou une autorisation de macOS, c'est Diego qui le fait. (Diego, 2026-10-13 : « Arrête de te brider parce qu'il te manque tel ou tel outil, logiciel ou autorisation. »)

## 2. Ce que le pilotage réel a appris [TESTÉ EN CONDITIONS RÉELLES, Resolve, 2026-10-11 et 2026-10-12]
- **Vérifier par l'image, pas par la valeur renvoyée** : un appel peut renvoyer True et exporter l'image d'avant ; un getter peut renvoyer le plan précédent ; une vignette de dérush peut être décalée. Une preuve d'outil n'est pas une preuve d'image. (Récidive au mariage : vignettes d'une caméra décalées sur 447 rushes, arrêt sur image faux, export d'image au mauvais endroit.)
- **Concevoir le contrôle pour qu'il puisse échouer** : se demander, avant de regarder, à quoi ressemblerait l'échec ; fabriquer des médias de test qui portent la réponse (un son décalé d'une valeur connue, un flash attendu à 255).
- **Une base ou un projet de test vérifié vide** avant de s'en servir ; créer un projet ferme celui qui est ouvert.
- **Les fonctions « Insert… » d'une API de montage** peuvent faire un montage par insertion qui pousse toute la timeline : les essayer sur une timeline jetable ; préférer les gestes qui posent à une position absolue.
- **Lire les métadonnées des rushes avant tout** (rotation, transfert, cadence, gamma) : des rushes verticaux en log écrasés par un proxy forcé, vingt minutes perdues.
- **Un geste bloqué n'est pas un résultat impossible** : chercher l'autre porte avant de déclarer une limite (pas de Magic Mask par script ne voulait pas dire pas de détourage).
- **Monter = calculer** : crête mesurée de chaque son, temps de la musique en images ; on pose une fois, on vérifie par bandes du rendu.
- **Rendre tôt et par plage** : le premier rendu de 16 s a révélé une saturation qu'aucune relecture de la timeline n'aurait montrée ; chaque animation se contrôle par un rendu de plage ; chaque plan se mesure sur le rendu.
- **Relire ses propres recettes** avant de recoder un geste.
- **Classer chaque geste** : réussi, contourné (avec la recette), à la main (pourquoi).
- **Un outil tiers en bac à sable** (une version App Store) peut ne pas lire les disques externes en ligne de commande : chercher la version hors App Store de l'éditeur, l'installer avec l'accord de Diego ; ne jamais toucher aux réglages de sécurité de macOS.

## 3. Quand ne pas piloter
- Une décision qui dépend d'un goût non exprimé et coûte cher à défaire : proposer des images de test d'abord.
- Un geste qui prend 10 s à la main et 10 appels en script : le dire, laisser Diego le faire.
- Un outil qui n'expose aucun moyen de vérifier le résultat : travailler à l'aveugle est interdit ; demander le moyen qui manque (règle 11).
