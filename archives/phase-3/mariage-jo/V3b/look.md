# Look et mouvement — mariage-jo

## Le look (réglé sur des images clés en pleine résolution, à côté des références de `da/`)
Trois LUT fabriquées (`labo/couleur/look_mariage.py`, écrites dans `LUT/P3/` de Resolve, accord de Diego du 2026-10-11), chacune « S-Log3 / S-Gamut3.Cine → Rec.709 » en un seul nœud :
| LUT | Pour | Réglages | Mesuré (images clés) | Référence |
|---|---|---|---|---|
| `P3_mariage_couleur` | la journée | tirage 2383 dosé à 85 %, exposition −0,85, épaule 0,62 (les blancs tenus), pied 0,10, chroma ×0,9, dominante olive +0,035 vers 112°, peau ramenée vers 55° et plafonnée, ombres neutres | guitariste : p2 10, p50 66, p98 232, 0 % brûlé, tons moyens 107° ; fleurs : chroma 0,047 | shcreativedept : p2 7, p50 74, p98 207, chroma 0,040, 106-129° |
| `P3_mariage_nb` | la cérémonie | luminance d'un mélange 0,42 R / 0,48 V / 0,10 B (la peau s'éclaircit, la pierre orange devient gris clair), courbe du 2383, exposition −0,8, épaule 0,70, pied 0,06, aucune teinte | rire : p2 7, p50 92, p98 231 ; baiser : p2 5, p98 189 ; chroma 0,000 | plustwofilms : chroma 0,003-0,005, p98 158-235 |
| `P3_mariage_nuit` | la soirée violette | comme la couleur, exposition −0,6, chroma ×0,72, pas d'olive, peau plafonnée à 0,06 (la peau reste une peau sous le violet) | Ornella sous les néons : p98 120, la lumière colorée reste dans le décor | (pas de référence de nuit dans le corpus mariage) |
| `P3_mariage_photobooth` | le passage kinetic | exposition −1,25 (fond blanc du photobooth très lumineux), chroma ×0,8 | | pivetedomato |

**Itérations** : 1) sans compensation, ciel blanc et robes à 235 (« plat ») ; 2) −0,55 diaph, épaule 0,72 : plus dense, ciel encore laiteux ; 3) −0,85, épaule 0,70, pied 0,10 ; 4) épaule 0,62, olive 0,035 : retenu. Le ciel couvert du jour reste blanc : c'est la lumière du jour (pas de ciel à inventer).

**Le changement de look** : N&B pour toute la cérémonie (on écoute), retour de la couleur sur le baiser, puis la couleur de la soirée suit la lumière réelle (rose du dîner, violet des projecteurs). Une seule bascule voulue (le oui), les autres viennent du lieu.

**Plan par plan** : décalage CDL d'exposition par plan (`labo/outils/phase3/mariage/expo_plans.py`) : visages détectés (MediaPipe, modèle local) amenés à une luminance cible (couleur 0,50, N&B 0,56, nuit 0,40 ; sans visage : médiane), hautes lumières plafonnées (p99,5 ≤ 0,93), par quart de diaph, ±1,5 diaph au plus. Résultats : `montage/cdl.json`. Ce n'est qu'un raccord d'exposition : la teinte des peaux reste celle de la LUT (vérifiée en planche).

**Grain** : un grain fin (bruit gris 1080p en Overlay, 22 %, ×2) sur toute la durée, piste V3 désactivable.

## Le mouvement
- Tremblement mesuré sur chaque plan retenu : la mesure globale (`tremblement.py`) est faussée par les sujets qui bougent (un plan serré de mariés qui rient), d'où un indice de **saccade** (variation du déplacement d'une image à l'autre, `saccades.py`) vérifié à l'œil sur des bandes d'images consécutives à 50 i/s (`jitter_voir.py`) : avant Gyroflow les écarts d'image à image sont irréguliers, après ils sont réguliers (mouvement voulu gardé).
- **Gyroflow** (version GitHub, synchronisation automatique sur la plage utilisée, lissage 0,5, zoom fixe ≤ 115 %) sur les 49 plans dont la saccade dépasse 1,0 ; **le stabilisé n'est gardé que s'il réduit la saccade d'au moins 20 %** ; sinon le brut. Sorties dans `videos/phase-3/mariage-jo/_travail/stab/` (rien n'est écrit dans le dossier source), nommées `_stabilized_agent`.
- Plans coupés là où ils sont bons (fouettés retirés) : C3686 (« je redis oui ») déplacé à 184 s, C3541 à 1,3 s, FX30.5589 à 11,6 s, C3689 à 58,6 s, C3922 à 1,0 s.
- Ralentis : ×2 natif (rush 50p lu à 50 % dans la timeline 25p) sur six plans ; **×4 sur la dame sous la pluie** (Speed Warp de Resolve) : test comparatif à 200 % dans `ralenti/ralenti_x4_200pc.jpg` (fondu d'images : main dédoublée, exclu ; flux optique et Speed Warp propres, léger étirement au bout des doigts).
