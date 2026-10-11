# Note de livraison — Sony LinkBuds Clip, V4

_2026-10-11. Fichier : `videos/phase-3/sony-linkbuds/rendus/sony_linkbuds_V4.mp4` (1080x1920, 25 i/s, **HEVC Main 10, 39 Mb/s**, AAC 48 kHz, 44,6 s, −14,0 LUFS, −1,1 dBTP). Resolve : projet `P3-sony-linkbuds-agent`, timeline **`SONY_V4`** (la V3 reste intacte dans `SONY_V3`). Note V3 : `archives/phase-3/sony-linkbuds/note-de-livraison-V3.md`._

## Ce que j'ai fait (tes notes sur la V3, une par une)
| Ta note | Dans la V4 |
|---|---|
| Titre : police et animation | Dessin de ta référence Sony : « **LinkBuds** » SST Pro Medium + « Clip » SST Pro Light, espace 0,3 em, noir sur la fenêtre blanche en haut à gauche ; fondu + montée de 18 px + léger flou qui se résorbe, 14 images, freiné ; « Clip » 3 images après. Comparaison : `images/V4_titre_vs_ref.png` |
| Effets répétitifs, sans folie | Une technique par moment, chacune tirée des rushes : **zoom infini** E → KORE ; **flash cut** des oreilles (l'écouteur au même point) ; rafale qui **monte** ; rafale qui **descend en step-print** ; **écran partagé** en trois bandes (sangles) ; **inversions** d'une image dans le rouge ; **trois collages**. Table des techniques d'eyecannndy : `montage-kinetic-editing` § 4 bis |
| SFX répétitifs | 63 sons, 25 nouveaux d'Artlist (62 sur 100 aujourd'hui), une famille par technique, variantes de hauteur |
| Couleur « bouillie », « pâté » | Séparation des teintes (peau 41° → 50° en OkLCh, écouteur crème, décor qui recule), noirs neutres, trois LUT (salle, jour, rouge) : `look.md` |
| Écouteurs surexposés | Packshots −0,8 diaph ; mesuré sur l'image pleine résolution : 0 à 1,8 % de pixels ≥ 250 (reflets seulement), contre ~10 % du boîtier brûlé en V3 (`look.md`, « Exposition des packshots ») |
| Réglages d'export | H.265, profil Main 10, multipass, 40 Mb/s demandés (39 obtenus), BT.709 ; vérifié au ffprobe ; image du rendu contre la même image en PNG 16 bits : PSNR 40,7 dB, aucun bloc en noirs amplifiés ×6 |
| Détourages « bizarres » | Collages sur arrêt sur image puis reprise du mouvement (orange avec cerne blanc ; papier millimétré ; photo posée sur l'image inversée). Détourage refait sur l'image figée en pleine résolution (carte de profondeur + GrabCut + filtre guidé, chignon corrigé à la main) |
| K-O-R-E : cadrage, flottement | Gyroflow puis lettres épinglées au même point et à la même hauteur : 0,2-0,3 px de résidu |
| Packshots : stabilisation visible | Gyroflow (zoom fixe, lissage modéré, **synchronisation automatique**) puis correction « rail » : le travelling du cadreur est gardé, la main retirée (C6725 : 0,89 px) |
| Dicté en session : mouvement fluide, pas statique | Fixe pour les lettres, rail pour les packshots (`montage-regard` point 3) |
| Dicté : jamais deux fois le même moment | 11 doublons de la V3 supprimés ; contrôle avant chaque rendu : **0 doublon** (`labo/outils/doublons_timeline.py`) |

## Organisation de la timeline
- **V1** les plans (LUT salle / jour / rouge en un nœud ; zooms, épinglage, rail, step-print, montée dans la composition du plan ; collages en ProRes 4444 sans LUT). **V2** le E du zoom infini et la bande du milieu de l'écran partagé. **V3** flashs blancs et bande du bas. **V4** titre. **V5** grain.
- **A1** musique · **A2** son du plan de fin Sony · **A3-A7** SFX.

## À vérifier par toi
**À l'oreille (rien n'a été écouté) :**
1. Les 25 nouveaux sons, surtout : projecteur et tics de verre de l'ouverture (0-2 s), les 7 tics qui montent sur les oreilles (6-7 s), le bégaiement de la rafale 1 (8-9 s), le papier et le scratch des collages (11 s, 20 s), l'armement argentique du step-print (17-18,5 s), les sangles et les « pops » de l'écran partagé (24-26 s), néon + Polaroid + rewind + drop (26-28 s : peut-être chargé), la petite clameur (32 s, à −17 dB : à couper si elle fait « banque de sons »).
2. La coupure musicale à 26,24 s (inchangée depuis la V3).

**À l'œil :**
3. Le **flash cut des oreilles** grossit d'un plan à l'autre (variante de la technique, voir l'autocritique).
4. Les **inversions** dans le rouge (31,4 / 31,7 / 32,1 s) : l'image passe une image en cyan clair, c'est volontairement un flash (photosensibilité contrôlée : 3 par seconde au pire).
5. Le titre : graisse Medium choisie d'après ta référence (floue) ; Bold disponible si tu préfères.

## Fichiers créés dans `SONY copy/RUSH/` (ton accord du 2026-10-11)
Utilisés par la V4 : `C6491`…`C6495_stabilized.mov`, `C6506_stabilized_sync.mov`, `C6507_stabilized_sync.mov` (plage 24-30 s), `C6723_stabilized_s13.mov` (12,5-15,5 s), `C6723_stabilized_s29.mov` (27,5-32,6 s), `C6725_stabilized_sync.mov`.
**Inutilisés, que tu peux supprimer (12,1 Go)** : `C6506_stabilized.mov` (1,46 Go), `C6507_stabilized.mov` (1,00 Go), `C6723_stabilized.mov` (5,61 Go, désynchronisé : il tremblait plus que l'original), `C6723_stabilized_sync.mov` (3,61 Go), `C6725_stabilized.mov` (0,41 Go). Je n'ai rien supprimé. Aucun original touché.

## Ce que je n'ai pas su faire, ou fait autrement
- **Magic Mask** : toujours pas scriptable (les traits ne s'écrivent pas par l'API). Les collages sont calculés hors de Resolve : propres, mais pas modifiables dans Resolve (il faut relancer `labo/outils/phase3/v4/collage.py`).
- Cases « Force sizing / debayer to highest quality » et « Bypass re-encode » : **absentes de l'API**. Elles sont aux valeurs par défaut de Resolve (rendu depuis les originaux, mise à l'échelle « sharper » du projet). Pour les cocher une fois pour toutes, enregistre un préréglage de rendu « F42 H265 Main10 » à la main ; je le chargerai ensuite par script (`LoadRenderPreset`).
- Un plantage de Resolve en cours de session (lecture des réglages d'un effet IA par script) : forcé à quitter avec ton accord, rien perdu (projet enregistré juste avant). Piège noté dans `montage-resolve`.
- Timelines de test dans le projet : `TEST_NIVEAUX`, `TEST_ANIM`, `TEST_GELS` (sans risque, à supprimer si tu veux).
