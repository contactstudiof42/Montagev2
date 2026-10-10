#!/usr/bin/env python3
"""Labo workflows (session 4) : une liste de plans (EDL JSON de l'atelier 02) → OpenTimelineIO → CMX 3600 et FCP7 XML,
puis relecture de chaque fichier et comparaison plan par plan (source in, durée, position, nom, marqueurs).
Question : qu'est-ce qui survit à un aller-retour entre logiciels ? Usage : python3 otio_aller_retour.py edl.json sortie_dir"""
import json, os, sys
import opentimelineio as otio
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
FPS = 30
edl = json.load(open(src))
tl = otio.schema.Timeline(name="Etincelle v6")
tr = otio.schema.Track(name="V1", kind=otio.schema.TrackKind.Video); tl.tracks.append(tr)
for i, (cam, a, d, sfx) in enumerate(edl):
    ref = otio.schema.ExternalReference(target_url=f"file:///rendus/02/{cam}.mov",
                                        available_range=otio.opentime.TimeRange(otio.opentime.RationalTime(0, FPS), otio.opentime.RationalTime(400, FPS)))
    c = otio.schema.Clip(name=f"{i+1:02d}_{cam}", media_reference=ref,
                         source_range=otio.opentime.TimeRange(otio.opentime.RationalTime(a, FPS), otio.opentime.RationalTime(d, FPS)))
    if sfx: c.markers.append(otio.schema.Marker(name=sfx, marked_range=otio.opentime.TimeRange(otio.opentime.RationalTime(a, FPS), otio.opentime.RationalTime(0, FPS))))
    tr.append(c)
def lire(t):
    res, pos = [], 0
    for c in t.tracks[0]:
        if isinstance(c, otio.schema.Gap): pos += c.source_range.duration.to_frames(); continue
        r = c.source_range; res.append({"nom": c.name, "in": r.start_time.to_frames(), "dur": r.duration.to_frames(), "pos": pos,
                                        "marqueurs": [m.name for m in c.markers]}); pos += r.duration.to_frames()
    return res
ref = lire(tl); bilan = {"plans": len(ref)}
for ad, ext in (("cmx_3600", "edl"), ("fcp_xml", "xml"), ("otio_json", "otio")):
    f = os.path.join(out, f"etincelle_v6.{ext}")
    try:
        otio.adapters.write_to_file(tl, f, adapter_name=ad); kw = {"rate": FPS} if ad == "cmx_3600" else {}   # une EDL CMX ne contient PAS la cadence : à fournir à la relecture
        back = lire(otio.adapters.read_from_file(f, adapter_name=ad, **kw))
    except Exception as e:
        bilan[ad] = f"ÉCHEC : {type(e).__name__}: {e}"[:300]; continue
    diffs = {k: sum(1 for x, y in zip(ref, back) if x[k] != y[k]) for k in ("in", "dur", "pos", "nom", "marqueurs")}
    bilan[ad] = {"cadence_fournie": bool(kw), "plans_relus": len(back), "differences": diffs, "exemple_relu": back[0], "octets": os.path.getsize(f)}
print(json.dumps(bilan, ensure_ascii=False, indent=1))
