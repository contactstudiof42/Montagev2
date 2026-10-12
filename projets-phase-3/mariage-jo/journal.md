# Journal des appels Resolve — mariage-jo

_Projet `P3-mariage-jo-agent` (base « TEST IA »). Un geste, une image de contrôle. Aucun autre projet ouvert ni modifié._

1. 2026-10-12 16:52 — `get_resolve_status` : 21.1.1 ; `get_whats_new(21.0.4)` : rien de neuf. Projet courant à l'ouverture : « Untitled Project » ; projets de la base : P3-BAC-A-SABLE, P3-sony-linkbuds-agent (non touchés).
2. 16:53 — `CreateProject("P3-mariage-jo-agent")` ; réglages 3840x2160, 25 i/s (OK) ; `timelinePlaybackFrameRate` refusé (sans effet, la cadence de timeline suffit). `SaveProject` OK.
3. 16:55 — Test des ralentis au-delà de ×2 : chutier TEST_RALENTI, import de C3864 (la dame sous la pluie), timeline TEST_RALENTI, trois copies de 2 s à 25 % (×4 par rapport au temps réel, depuis du 50p) : `RETIME_FRAME_BLEND` ; `RETIME_OPTICAL_FLOW` + `MOTION_EST_ENHANCED_BETTER` ; `RETIME_OPTICAL_FLOW` + `MOTION_EST_SPEED_WARP_BETTER`. `SetSpeed`, `SetProperty("RetimeProcess" / "MotionEstimation")` : relus justes (2/0, 3/4, 3/5). Erreur de script : `p.SaveProject` n'existe pas sur Project (c'est `ProjectManager.SaveProject()`).
4. 16:56 — Rendu ProRes 422 HQ UHD de la timeline de test (6,8 s, ≈ 60 s de calcul). Images à 200 % (`ralenti/ralenti_x4_200pc.jpg`) : fondu d'images = main dédoublée (exclu) ; flux optique amélioré et Speed Warp = main nette, léger étirement au bout des doigts ; visage propre dans les deux. **La LUT n'était pas appliquée** (image log) : `SetLUT` sans `RefreshLUTList()` après l'écriture des nouvelles LUT. À refaire dans la construction.
