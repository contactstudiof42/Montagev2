# Labo workflows : aller-retour d'une timeline entre formats d'échange (session 4, 2026-10-10)

**Outil** : `otio_aller_retour.py edl.json sortie/` — la liste de 19 plans de la pièce 02 (30 i/s, marqueurs SFX) est convertie
avec OpenTimelineIO 0.18.1 (+ adaptateurs `otio-cmx3600-adapter`, `otio-fcp-adapter`, installés en 5 s par pip) en CMX 3600, FCP7 XML et OTIO JSON,
puis relue et comparée plan par plan. Résultats bruts : `resultats.json`.

| Format | Points d'entrée, durées, positions | Noms de plans | Marqueurs | Piège |
|---|---|---|---|---|
| **CMX 3600 (EDL)** | 19/19 exacts **si la cadence est fournie à la relecture** | conservés (commentaire `FROM CLIP NAME`) | conservés mais **passés en MAJUSCULES** (`hook` → `HOOK`), 1 par plan | **La cadence n'est pas dans le fichier** : relue par défaut à 24 i/s, la lecture plante (« frames beyond 23 ») — dans un vrai logiciel, elle peut au contraire *réussir* avec de faux timecodes. Nom de bobine tronqué (8 caractères). Une seule piste vidéo par EDL. |
| **FCP7 XML** | 19/19 exacts | conservés | conservés | — (fichier 24 Ko) |
| **OTIO JSON** | 19/19 exacts | conservés | conservés | format natif, peu de logiciels l'importent directement (Resolve oui, selon la doc ; à vérifier) |

## Ce que j'apprends [TESTÉ EN LABO, côté fichiers ; imports dans les logiciels THÉORIQUES]
1. **Une EDL ne sait pas à quelle cadence elle a été écrite** : toujours noter la cadence dans le nom du fichier ou dans un mail d'accompagnement (`film_v6_30p.edl`), et la régler dans le logiciel *avant* l'import.
2. Pour passer une structure de montage d'un logiciel à l'autre, **le XML FCP7 est le plus sûr des trois** ici (tout survit) ; l'EDL reste le format universel minimal (une piste, coupes et fondus, pas d'effets), utile pour un conformateur ou un étalonneur qui veut seulement les points de coupe.
3. Ce test ne dit rien des effets, vitesses, recadrages, nests et pistes audio : c'est là que les vrais allers-retours cassent (test n°19 du plan MCP).

## AAF par familles (session 5, 2026-10-10) — `aaf_pistes.py`
- pyaaf2 1.7.1 : CompositionMob + 3 MasterMob (WAV embarqués via `import_audio_essence`), pistes son nommées DIAL / MUS / SFX, `Filler` pour les blancs.
- Relecture pyaaf2 : 6 clips sur 6 identiques (position, début source, durée en images à 25 i/s).
- Relecture OpenTimelineIO + otio-aaf-adapter : identique aussi. Les noms de pistes survivent.
- Limites : ni poignées, ni gain, ni fondus écrits ; aucun logiciel de mixage pour relire ici → test de phase 2.
