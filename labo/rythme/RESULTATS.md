# Labo rythme — détection de coupes avec ffmpeg `scdet` (session 1, 2026-10-09)

ffmpeg 6.1.1. Script : `detect_coupes.sh` (monte 9 plans synthétiques aux durées connues, 50→6 images puis un plan de 75 : « montée puis respiration »).

## Résultats
| Cas | Seuil | Résultat |
|---|---|---|
| Coupes franches entre sources très différentes (8 coupes) | 10 | **8/8 détectées, au centième près** (2.00, 3.60, 4.80, 5.60, 6.08, 6.40, 6.72, 6.96 s) |
| Fondu enchaîné de 0,5 s (`xfade`) | 10, 5, 3 | **0 détection** : scdet ne voit pas les fondus |
| Coupe entre deux plans presque identiques (teinte +12°, luminosité +0,03) | 10, 5 | 0 détection |
| idem | 3 | détectée (2.00 s) |
Durée totale du test : ~1 s de calcul.

## Conclusions
- `scdet` est fiable pour les **coupes franches** ; c'est un bon outil pour mesurer le rythme d'un montage (durées de plans, histogramme).
- Il **rate les fondus** : sur un film qui en contient, compléter par une analyse de la différence image à image sur une fenêtre (à développer) ou un repérage manuel.
- Entre plans très proches (même axe, même lumière : jump cut, champ/contrechamp homogène), il faut descendre vers 3, avec un risque de faux positifs sur des plans réels en mouvement (flash, panoramique rapide) : **à tester sur du vrai matériau CC0** (session suivante).

## Commande [TESTÉ EN LABO]
```
ffmpeg -i film.mp4 -vf "scdet=threshold=10,metadata=print:key=lavfi.scd.time:file=-" -f null - 2>/dev/null | grep -o "lavfi.scd.time=[0-9.]*" | cut -d= -f2
```
