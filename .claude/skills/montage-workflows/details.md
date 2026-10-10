# Workflows : mesures détaillées

Annexe de `SKILL.md` : mesures et protocoles du labo derrière les règles d'échange, de proxies, de VFR et d'interpolation (le SKILL.md fait foi ; les règles elles-mêmes n'y sont pas répétées). Marqueurs : voir `SKILL.md`.

## Proxies [TESTÉ EN LABO, `labo/proxies/` ; rattachement dans les logiciels THÉORIQUE]
- Sans `-map 0:v -map 0:a`, le proxy n'a qu'une piste audio : il est refusé à la reconnexion, ou l'ambiance est perdue. Nom ou durée différents de l'original : la reconnexion échoue aussi.
- H.264 tout-intra (`-g 1`) : environ 3× plus léger que ProRes Proxy sur le lot testé.
- Pourquoi un proxy fluide compte : on n'ose pas laisser vivre un plan qu'on ne voit pas en temps réel.

## Rushes de téléphone en cadence variable (VFR) [TESTÉ EN LABO, `labo/vfr/`]
Faux rush à vérité terrain : 30 i/s, puis 3-8 s « basse lumière » à ~24 i/s avec gigue, flash et clic à 5,000 s.
- **Repérage** : `r_frame_rate` 30/1 contre `avg_frame_rate` ~27, intervalles d'images inégaux (`mesure_vfr.py`).
- **Lecture à la cadence nominale** (logiciel qui ignore les horodatages) : −400 ms à 5 s ; ≈ 1 s à 10 s (calculé : 271 images lues à 30 i/s = 9,03 s pour 10 s de son).
- **Conformation à l'ingest** (`-fps_mode cfr -r 25`/`30`, ou `-vf fps=25`) : 0 ms d'écart ; 25 images doublées sur 10 s à 30 i/s, là où le téléphone n'a rien capturé. `minterpolate=mi_mode=blend` réduit les doublons à 2 mais fond les images entre elles (traînées).
- Troisième voie, non testée : interpolation par IA pour un plan qui doit être fluide. Ne jamais conformer dans la timeline : une fois, à l'ingest (25 en Europe).

## Interpolation et ralentis [TESTÉ EN LABO]
**Labo synthétique** (`labo/interpolation/`, 30 → 60 i/s contre une vérité terrain) :
- Image lisse à grands mouvements : `mci` bat le fondu de 3 dB en zones en mouvement ; **RIFE 4.25** (MIT, CPU, `labo/interpolation/RIFE.md`) gagne encore +5 dB sur `mci` : le meilleur outil libre testé pour un plan net (famille de Speed Warp / Topaz).
- Texture fine : ni `mci` ni RIFE ne font mieux qu'un fondu. Casse partout : objets fins qui tournent, bords d'occlusion, petits objets rapides.
- À travers une coupe sans détection de changement de plan (`scd=none`) : une image hybride des deux plans (flash), RIFE compris. `minterpolate` raccourcit aussi le plan de 2 images source (−67 ms à 30 i/s).

**Vrais plans** (`labo/interpolation-reel/`, 2 plans CC0 d'Internet Archive, eau et feuillage, petit mouvement, 320×180) : sur le plan « vagues » en ×2, fondu (`blend`) 43,8 dB = `mci` 43,8 dB > RIFE 41,6 dB ; RIFE perd de 1 à 3,6 dB contre le fondu sur tous les cas, et le +5 dB synthétique ne se généralise pas (à retester en 1080p, où les mouvements en pixels sont 4-6× plus grands) ; à petit mouvement, `mci` retombe sur le fondu pour 3,5× le temps de calcul. Sur une coupe, `mci` par défaut montre le plan suivant **une image trop tôt** (33 ms). Sur eau, feuillage, foule : le fondu.

## Vitesses dans l'aller-retour (`labo/workflows/vitesses/RESULTATS.md`) [TESTÉ EN LABO côté fichiers ; imports en phase 3]
- XML FCP7 via OTIO : vitesses, arrêts sur image et inversions perdus sans avertissement.
- EDL : lignes M2 justes mais durée source inversée (ralenti = trop de source déclarée, accéléré = pas assez) ; vitesse du plan entrant d'un fondu perdue à la relecture ; timecode de départ 01:00:00:00 non écrit.
- Un aller-retour qui se relit sans erreur par le même outil ne prouve rien. `verif_edl.py` contrôle la cohérence source / enregistrement / M2, le départ 01:00:00:00 et les trous : 4 défauts sur 4 trouvés, 0 faux positif.

## Recadrages, nests, audio multipiste (`labo/workflows/recadrages/README.md`) [TESTÉ EN LABO côté fichiers ; imports en phase 3]
- XML FCP7 → OTIO → XML : échelle, position, rotation, Crop et images clés « survivent » seulement parce que l'adaptateur **recopie le XML d'origine** ; timeline modifiée ou reconstruite : 7 réglages sur 7 perdus, sans message.
- Nests : relus vides par l'adaptateur FCP7 (3 plans → 0), supprimés par l'EDL sans avertissement.
- Stéréo éclatée G/D : fusionnée à la lecture, canal droit perdu (3 → 2 pistes) ; niveaux de clip perdus hors XML d'origine ; EDL : aucun audio, refus au-delà de 2 pistes. Pour le mixeur, autre voie que l'AAF : WAV polyphoniques.
- `liste_recadrages.py montage.xml > recadrages.csv` sort TC, plan, effet, paramètre, valeur ou images clés ; à l'arrivée, s'arrêter au moindre écart de compte (plans, pistes, canaux).
- Recadrage perdu, précision : le sujet n'est plus au tiers ; canal droit perdu : l'ambiance se rétrécit au centre.
