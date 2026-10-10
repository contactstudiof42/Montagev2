"""Labo workflows (session 11, BACKLOG 15 suite) : recadrages (Basic Motion / Crop), nests et audio multipiste
survivent-ils à l'aller-retour XML FCP7 / EDL CMX 3600 / AAF via OpenTimelineIO ?
Usage : python3 recadrages.py sortie/   (lit verite_fcp7.xml, écrit les fichiers d'échange et resultats.json)"""
import sys, os, json, xml.etree.ElementTree as ET, opentimelineio as otio
ICI = os.path.dirname(os.path.abspath(__file__)); out = sys.argv[1]; os.makedirs(out, exist_ok=True)
R = 25; RT = otio.opentime.RationalTime; TR = otio.opentime.TimeRange

def releve_xml(f):
    """Relevé « métier » d'un XML FCP7 lu directement (sans OTIO) : filtres, nests, pistes, canaux, fondus."""
    s = ET.parse(f).getroot().find(".//sequence"); r = {"plans": {}, "pistes_video": 0, "pistes_audio": 0, "stereo_eclatees": 0, "fondus_audio": 0}
    for k in ("video", "audio"):
        for tr in s.findall(f"media/{k}/track"):
            r["pistes_" + k] += 1; r["stereo_eclatees"] += tr.get("totalExplodedTrackCount") == "2"
            r["fondus_audio"] += sum(1 for t in tr.findall("transitionitem") if k == "audio")
            for ci in tr.findall("clipitem"):
                p = {"pos": (ci.findtext("start"), ci.findtext("end")), "filtres": {}, "nest": ci.find("sequence") is not None,
                     "canal_source": ci.findtext("sourcetrack/trackindex")}
                if p["nest"]: p["plans_dans_nest"] = len(ci.findall("sequence/media/video/track/clipitem"))
                for fe in ci.findall("filter/effect"):
                    pars = {}
                    for pa in fe.findall("parameter"):
                        kf = [(k_.findtext("when"), k_.findtext("value")) for k_ in pa.findall("keyframe")]
                        v = pa.find("value"); v = (v.findtext("horiz"), v.findtext("vert")) if v is not None and len(v) else (v.text if v is not None else None)
                        pars[pa.findtext("parameterid")] = kf or v
                    p["filtres"][fe.findtext("effectid")] = pars
                r["plans"][ci.findtext("name")] = p
    return r

def releve_otio(t):
    """Relevé côté OTIO : ce que l'adaptateur a compris (objets Effect, Stack, pistes, transitions)."""
    r = {"pistes": [], "plans": {}}
    for tr in t.tracks:
        r["pistes"].append(f"{tr.kind}:{tr.name}:{len(tr)} él.")
        for it in tr:
            if isinstance(it, otio.schema.Transition): r["plans"]["fondu:" + tr.name] = it.name; continue
            if isinstance(it, otio.schema.Gap): continue
            e = {"type": type(it).__name__, "effets": [x.name or x.effect_name for x in it.effects],
                 "effets_avec_valeurs": sum(1 for x in it.effects if x.metadata.get("fcp_xml", {}).get("parameter")),
                 "meta_filtre": "filter" in it.metadata.get("fcp_xml", {}), "dur": it.duration().to_frames()}
            if isinstance(it, otio.schema.Stack): e["plans_dans_nest"] = sum(1 for _ in it.find_clips())
            r["plans"][it.name] = e
    return r

def compare(ref, back):
    """Compare deux relevés XML plan par plan : survit / perdu / déformé."""
    v = {}
    for nom, p in ref["plans"].items():
        q = back["plans"].get(nom)
        if q is None: v[nom] = "PLAN PERDU"; continue
        d = []
        for fid, pars in p["filtres"].items():
            if fid not in q["filtres"]: d.append(f"{fid} perdu")
            elif q["filtres"][fid] != pars: d.append(f"{fid} déformé {pars} -> {q['filtres'][fid]}")
        if p["nest"] != q["nest"]: d.append("nest aplati" if p["nest"] else "nest créé")
        if p.get("plans_dans_nest") != q.get("plans_dans_nest"): d.append(f"plans du nest {p.get('plans_dans_nest')} -> {q.get('plans_dans_nest')}")
        if p["canal_source"] != q["canal_source"]: d.append(f"canal source {p['canal_source']} -> {q['canal_source']}")
        if p["pos"] != q["pos"]: d.append(f"position {p['pos']} -> {q['pos']}")
        v[nom] = "; ".join(d) or "survit"
    for k in ("pistes_video", "pistes_audio", "stereo_eclatees", "fondus_audio"):
        v[k] = f"{ref[k]} -> {back[k]}"
    return v

res = {}
src = os.path.join(ICI, "verite_fcp7.xml"); ref = releve_xml(src); res["verite_xml"] = ref
# 1) XML FCP7 natif -> OTIO -> XML FCP7 (le cas « Premiere exporte, Resolve importe via un outil OTIO »)
tl = otio.adapters.read_from_file(src); res["lu_par_otio"] = releve_otio(tl)
f = os.path.join(out, "aller_retour_fcp7.xml"); otio.adapters.write_to_file(tl, f)
res["xml_aller_retour"] = compare(ref, releve_xml(f))
# 2) La même timeline, effets reconstruits en OTIO « propre » (métadonnées fcp_xml retirées) -> XML : l'adaptateur écrit-il les Effect ?
propre = tl.clone()
for it in propre.find_children():
    if hasattr(it, "metadata"): it.metadata.pop("fcp_xml", None)
f = os.path.join(out, "otio_propre_fcp7.xml"); otio.adapters.write_to_file(propre, f)
res["xml_depuis_otio_sans_meta"] = compare(ref, releve_xml(f))
otio.adapters.write_to_file(tl, os.path.join(out, "recadrages_25p.otio"))
# 3) EDL CMX 3600 : timeline entière, puis V1 seule
for nom, pistes in (("tout", list(tl.tracks)), ("v1", [tl.tracks[0]])):
    t1 = otio.schema.Timeline(name=tl.name); t1.global_start_time = RT(90000, R)
    for p in pistes: t1.tracks.append(p.clone())
    f = os.path.join(out, f"recadrages_{nom}.edl")
    try:
        otio.adapters.write_to_file(t1, f); back = otio.adapters.read_from_file(f, rate=R)
        res["edl_" + nom] = {"relu": releve_otio(back), "mots_cles_effets": [l.strip() for l in open(f) if any(w in l.upper() for w in ("SCALE", "CROP", "MOTION", "LEVEL", "NEST", "* "))]}
    except Exception as e:
        res["edl_" + nom] = f"ÉCHEC : {type(e).__name__}: {e}"
# 4) Vérité construite en OTIO natif : effet « Transform » générique, nest = Stack dans un Track, 3 pistes audio, gain, fondu audio
def clip(nom, debut, duree, fx=None):
    c = otio.schema.Clip(name=nom, media_reference=otio.schema.ExternalReference(target_url=f"file:///rushes/{nom}.mov",
        available_range=TR(RT(0, R), RT(2000, R))), source_range=TR(RT(debut, R), RT(duree, R)))
    if fx: c.effects.append(otio.schema.Effect(name=fx[0], effect_name=fx[0], metadata={"labo": fx[1]}))
    return c
nat = otio.schema.Timeline(name="natif_25p"); nat.global_start_time = RT(90000, R)
v1 = otio.schema.Track(name="V1"); v1.append(clip("A_zoom150", 100, 50, ("Transform", {"scale": 1.5, "rotation": 10, "pos": [0.1, -0.05], "crop_ltrb": [5, 12, 5, 12]})))
nest = otio.schema.Stack(name="NEST_interview"); n1 = otio.schema.Track(name="NV1"); n1.extend([clip("N1_large", 300, 25), clip("N2_serre", 400, 25)])
n2 = otio.schema.Track(name="NV2"); n2.append(clip("N3_nom_incruste", 0, 50)); nest.extend([n1, n2]); v1.append(nest)
nat.tracks.append(v1)
for nom, plans in (("A1", [("A_son_G", 100, 75, ("AudioLevels", {"gain_db": -6}))]), ("A2", [("A_son_D", 100, 75, ("AudioLevels", {"gain_db": -6}))]),
                   ("A3_musique", [("MUSIQUE_mono", 0, 50, None), ("AMBIANCE_mono", 500, 50, None)])):
    a = otio.schema.Track(name=nom, kind=otio.schema.TrackKind.Audio)
    for k, p in enumerate(plans):
        a.append(clip(*p))
        if nom == "A3_musique" and k == 0: a.append(otio.schema.Transition(name="fondu_audio", in_offset=RT(12, R), out_offset=RT(12, R)))
    nat.tracks.append(a)
otio.adapters.write_to_file(nat, os.path.join(out, "natif_25p.otio"))
def resume_nat(t):
    r = {"pistes": [f"{tr.kind}:{tr.name}" for tr in t.tracks], "plans": {}}
    for tr in t.tracks:
        for it in tr:
            if isinstance(it, otio.schema.Transition): r["plans"]["fondu:" + tr.name] = [it.in_offset.to_frames(), it.out_offset.to_frames()]
            elif isinstance(it, (otio.schema.Clip, otio.schema.Stack)):
                r["plans"][it.name] = {"type": type(it).__name__, "effets": [(e.effect_name or e.name, json.loads(otio.core.serialize_json_to_string(e.metadata.get("labo"))) if e.metadata.get("labo") else None) for e in it.effects],
                                       "plans_internes": sum(1 for _ in it.find_clips()) if isinstance(it, otio.schema.Stack) else None}
    return r
res["natif_reference"] = resume_nat(nat)
def essai(cle, t, ext):
    f = os.path.join(out, cle + ext)
    try:
        otio.adapters.write_to_file(t, f)
        res[cle + ext] = resume_nat(otio.adapters.read_from_file(f, rate=R) if ext == ".edl" else otio.adapters.read_from_file(f))
        if ext == ".xml": x = releve_xml(f); res[cle + ".xml_brut"] = {k: v for k, v in x.items() if k != "plans"} | {
            "plans_dans_nest_ecrits": x["plans"].get("NEST_interview", {}).get("plans_dans_nest"), "filtres_ecrits": {n: list(p["filtres"]) for n, p in x["plans"].items()}}
    except Exception as e:
        res[cle + ext] = f"ÉCHEC : {type(e).__name__}: {str(e).strip().splitlines()[0][:200]}"
        if os.path.exists(f): os.remove(f)  # pas de fichier à moitié écrit
for ext in (".xml", ".edl", ".aaf"): essai("natif_25p", nat, ext)  # tel quel
# variantes de contournement : nest avec source_range explicite ; EDL limitée à 2 pistes audio ; AAF sans le fondu audio
nest.source_range = TR(RT(0, R), RT(50, R)); essai("natif_nest_borne", nat, ".xml")
t2 = nat.clone(); del t2.tracks[3]; essai("natif_2audio", t2, ".edl")
t3 = nat.clone(); t3.tracks[3].remove(t3.tracks[3][1]); essai("natif_sans_fondu", t3, ".aaf")
json.dump(res, open(os.path.join(out, "resultats.json"), "w"), indent=1, ensure_ascii=False)
for k, v in res.items():
    if k in ("verite_xml", "lu_par_otio"): continue
    print("==", k); print(json.dumps(v, indent=1, ensure_ascii=False) if not isinstance(v, str) else v)
