"""Labo workflows (session 10) : les vitesses, arrêts sur image, inversions, fondus et 2e piste
survivent-ils à l'aller-retour EDL CMX 3600 / FCP7 XML / OTIO ? Usage : python3 vitesses.py sortie/"""
import sys, os, json, opentimelineio as otio
R = 25
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
RT = otio.opentime.RationalTime; TR = otio.opentime.TimeRange
def clip(nom, debut, duree, warp=None):
    c = otio.schema.Clip(name=nom, media_reference=otio.schema.ExternalReference(target_url=f"file:///rushes/{nom}.mov",
        available_range=TR(RT(0, R), RT(2000, R))), source_range=TR(RT(debut, R), RT(duree, R)))
    if warp == "freeze": c.effects.append(otio.schema.FreezeFrame())
    elif warp is not None: c.effects.append(otio.schema.LinearTimeWarp(time_scalar=warp))
    return c
tl = otio.schema.Timeline(name="vitesses_25p"); tl.global_start_time = RT(90000, R)  # 01:00:00:00
v1 = otio.schema.Track(name="V1"); v2 = otio.schema.Track(name="V2")
plans = [("A_normal", 100, 50, None), ("B_ralenti50", 200, 50, 0.5), ("C_accel200", 300, 50, 2.0),
         ("D_arret", 400, 25, "freeze"), ("E_inverse", 500, 50, -1.0), ("F_ralenti40", 600, 50, 0.4)]
for i, p in enumerate(plans):
    v1.append(clip(*p))
    if i == 4:  # fondu enchaîné de 12 images entre E et F
        v1.append(otio.schema.Transition(transition_type=otio.schema.TransitionTypes.SMPTE_Dissolve,
                                         in_offset=RT(6, R), out_offset=RT(6, R)))
v2.append(otio.schema.Gap(source_range=TR(RT(0, R), RT(60, R)))); v2.append(clip("TITRE_incruste", 0, 40))
tl.tracks.append(v1); tl.tracks.append(v2)
def resume(t):
    r = []
    for tr in t.video_tracks():
        for it in tr:
            if isinstance(it, otio.schema.Clip):
                fx = [(type(e).__name__, getattr(e, "time_scalar", None)) for e in it.effects]
                r.append({"piste": tr.name, "nom": it.name, "src_in": it.source_range.start_time.to_frames(),
                          "duree": it.source_range.duration.to_frames(), "pos": it.range_in_parent().start_time.to_frames(), "fx": fx})
            elif isinstance(it, otio.schema.Transition):
                r.append({"piste": tr.name, "transition": it.transition_type, "in": it.in_offset.to_frames(), "out": it.out_offset.to_frames()})
    return r
ref = resume(tl); res = {"reference": ref}
for ext, kw in ((".otio", {}), (".xml", {}), (".edl", {})):
    f = os.path.join(out, "vitesses_25p" + ext)
    try:
        if ext == ".edl":
            t1 = otio.schema.Timeline(name=tl.name); t1.global_start_time = tl.global_start_time
            t1.tracks.append(v1.clone()); otio.adapters.write_to_file(t1, f)  # une piste par EDL
            back = otio.adapters.read_from_file(f, rate=R)
        else:
            otio.adapters.write_to_file(tl, f); back = otio.adapters.read_from_file(f)
        res[ext] = resume(back)
    except Exception as e:
        res[ext] = f"ÉCHEC : {type(e).__name__}: {e}"
json.dump(res, open(os.path.join(out, "resultats.json"), "w"), indent=1, ensure_ascii=False)
for k, v in res.items():
    print("==", k)
    if isinstance(v, str): print(v); continue
    for x in v: print("  ", x)
