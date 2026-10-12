# resolve_build_v4.py — construit la timeline MARIAGE_JO_V4 dans Resolve à partir de montage_V4.json (V4 : arrêts sur image,
# fondus au noir, fondu de grade dans le plan du baiser, lit musical en piste 4, titres de titres_v4.py, LUT V4 + CDL par plan).
# Exécuté dans le serveur MCP (run_script_unsafe, lecture du JSON seulement) : `resolve` et `project` sont injectés.
# Étapes (variable ETAPE) : "import", "video", "audio", "habillage", "lut", "voix". Chaque étape enregistre le projet.
# Règles : projet P3-mariage-jo-agent seulement ; une nouvelle timeline par version (jamais d'écrasement) ; rien n'est supprimé hors de cette timeline.
import json, os, time
J = json.load(open("/Volumes/SSD FAST/Montage-IA/projets-phase-3/mariage-jo/montage/montage_V4.json"))
RUSH = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
TW = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"
INV = {x["nom"]: x for x in json.load(open(f"{TW}/inventaire.json"))}
TL_NOM = globals().get("TL_NOM", "MARIAGE_JO_V4")
ETAPE = globals().get("ETAPE", "import")
T0 = 90000; FPS = 25
pm = resolve.GetProjectManager(); p = pm.GetCurrentProject()
assert p.GetName() == "P3-mariage-jo-agent", p.GetName()
mp = p.GetMediaPool(); root = mp.GetRootFolder()
def rf(t): return int(round(t * FPS))
def fichier_video(e):
    s = e.get("stab")
    if s: return s["fichier"], e["src"] - s["debut_plage"]
    return f"{RUSH}/{INV[e['nom']]['fichier']}", e["src"]
def dossier(nom):
    for f in root.GetSubFolderList():
        if f.GetName() == nom: return f
    return mp.AddSubFolder(root, nom)
def tous_les_clips():
    out = {}
    def parc(f):
        for c in f.GetClipList(): out[c.GetClipProperty("File Path")] = c
        for s in f.GetSubFolderList(): parc(s)
    parc(root); return out
TIT = json.load(open(f"{TW}/titres_v4/fichiers.json")) if os.path.exists(f"{TW}/titres_v4/fichiers.json") else {}
EXTRA = {"grain": f"{TW}/grain/grain_1080_20s.mov", "kinetic": f"{TW}/kinetic_v4/kinetic_V4.mov", "vignettage": f"{TW}/vignettage/vignettage_20s.mov"}
for k, f in TIT.items(): EXTRA["t:" + k] = f
res = {}
if ETAPE == "import":
    FEN = json.load(open(f"{TW}/fenetres_v4/fenetres.json"))
    chemins = set(fichier_video(e)[0] for e in J["video"]) | set(a["fichier"] for a in J["audio"]) | set(v for v in EXTRA.values() if os.path.exists(v)) | set(f["mov"] for f in FEN.values())
    deja = tous_les_clips(); manquants = sorted(c for c in chemins if c not in deja)
    par = {"RUSH": [], "STAB": [], "SON": [], "HABILLAGE": [], "FENETRES": []}
    for c in manquants:
        k = "FENETRES" if "/fenetres_v4/" in c else "STAB" if "/stab/" in c else ("SON" if c.lower().endswith((".wav", ".mp3")) else ("HABILLAGE" if "/_travail/" in c else "RUSH"))
        par[k].append(c)
    for k, l in par.items():
        if not l: continue
        mp.SetCurrentFolder(dossier(k)); got = mp.ImportMedia(l); res[k] = (len(l), len(got or []))
    res["total_chemins"] = len(chemins)
elif ETAPE == "video":
    clips = tous_les_clips()
    tl = None
    for i in range(1, p.GetTimelineCount() + 1):
        if p.GetTimelineByIndex(i).GetName() == TL_NOM: tl = p.GetTimelineByIndex(i)
    if tl is None:
        mp.SetCurrentFolder(dossier("TIMELINES")); tl = mp.CreateEmptyTimeline(TL_NOM)
    p.SetCurrentTimeline(tl)
    while tl.GetTrackCount("video") < 4: tl.AddTrack("video")
    while tl.GetTrackCount("audio") < 4: tl.AddTrack("audio", "stereo")
    for i, n in enumerate(["PLANS", "VIGNETTAGE", "TITRES", "GRAIN"], 1): tl.SetTrackName("video", i, n)
    for i, n in enumerate(["VOIX", "SALLE", "MUSIQUE", "LIT"], 1): tl.SetTrackName("audio", i, n)
    ok = 0; ko = []
    deb, fin = globals().get("DEB", 0), globals().get("FIN", 10**6)
    evs = sorted([e for e in J["video"] if e["piste"] == 1], key=lambda e: e["rec"])[deb:fin]; FG = []
    for e in evs:
        if "KINETIC" in e.get("note", "") and os.path.exists(EXTRA["kinetic"]):
            f, s = EXTRA["kinetic"], 0.0; fps_src = 25
        else:
            f, s = fichier_video(e); fps_src = 50
        it = clips.get(f)
        r0 = rf(e["rec"]); n = rf(e["rec"] + e["dur"]) - r0
        sf = int(round(s * fps_src)); ef = sf + n * fps_src // FPS
        ti = mp.AppendToTimeline([{"mediaPoolItem": it, "startFrame": sf, "endFrame": ef, "recordFrame": T0 + r0, "trackIndex": 1, "mediaType": 1}]) if it else None
        if not ti: ko.append((e["rec"], e["nom"], sf, ef)); continue
        ti = ti[0]
        if e.get("gel"): ti.SetSpeed({"Percentage": 0.0, "RippleTimeline": False})
        elif e["vitesse"] != 1: ti.SetSpeed({"Percentage": 100.0 * e["vitesse"], "RippleTimeline": False})
        if e.get("fondu_noir"): ti.AddTransition({"type": "Cross Dissolve", "category": "simple", "position": "start", "alignment": "right", "duration": rf(e["fondu_noir"])})
        if e.get("fondu_noir_fin"): ti.AddTransition({"type": "Cross Dissolve", "category": "simple", "position": "end", "alignment": "left", "duration": rf(e["fondu_noir_fin"])})
        if e.get("fondu_grade"): FG.append((ti, rf(e["fondu_grade"])))
        if e["vitesse"] < 0.5: ti.SetProperty("RetimeProcess", resolve.RETIME_OPTICAL_FLOW); ti.SetProperty("MotionEstimation", resolve.MOTION_EST_SPEED_WARP_BETTER)
        ok += 1
    fg = [bool(t.AddTransition({"type": "Cross Dissolve", "category": "simple", "position": "end", "alignment": "center", "duration": n})) for t, n in FG]
    res = {"timeline": tl.GetName(), "poses": ok, "echecs": ko, "items": len(tl.GetItemListInTrack("video", 1)), "fondus_de_grade": fg}
elif ETAPE == "audio":
    clips = tous_les_clips(); tl = p.GetCurrentTimeline(); ok = 0; ko = []
    deb, fin = globals().get("DEB", 0), globals().get("FIN", 10**6)
    for a in sorted(J["audio"], key=lambda a: a["rec"])[deb:fin]:
        it = clips.get(a["fichier"]); est_rush = a["fichier"].upper().endswith(".MP4")
        fs = 50 if est_rush else FPS
        r0 = rf(max(0, a["rec"])); n = rf(a["rec"] + a["dur"]) - r0
        sf = int(round(a["src"] * fs)); ef = sf + n * fs // FPS
        ti = mp.AppendToTimeline([{"mediaPoolItem": it, "startFrame": sf, "endFrame": ef, "recordFrame": T0 + r0, "trackIndex": a["piste"], "mediaType": 2}]) if it else None
        if not ti: ko.append((a["rec"], os.path.basename(a["fichier"]), sf, ef)); continue
        ti = ti[0]; ti.SetProperty("AudioVolume", float(a["gain"]))
        ti.SetFades({"FadeIn": max(0, rf(a["fin"])), "FadeOut": max(0, rf(a["fout"]))})
        ok += 1
    res = {"poses": ok, "echecs": ko}
elif ETAPE == "habillage":
    clips = tous_les_clips(); tl = p.GetCurrentTimeline(); out = []
    for t in J["textes"]:
        f = EXTRA.get("t:" + t["texte"])
        it = clips.get(f); r0 = rf(t["rec"]); n = rf(t["rec"] + t["dur"]) - r0
        ti = mp.AppendToTimeline([{"mediaPoolItem": it, "startFrame": 0, "endFrame": n, "recordFrame": T0 + r0, "trackIndex": 3, "mediaType": 1}])
        out.append((t["texte"], bool(ti)))
    FEN = json.load(open(f"{TW}/fenetres_v4/fenetres.json")); nv = 0
    for e in sorted([e for e in J["video"] if e["piste"] == 1], key=lambda e: e["rec"]):
        fe = FEN.get(f"{e['rec']:.3f}")
        if not fe: continue
        it = clips.get(fe["mov"]); r0 = rf(e["rec"]); n = rf(e["rec"] + e["dur"]) - r0
        ti = mp.AppendToTimeline([{"mediaPoolItem": it, "startFrame": 0, "endFrame": n, "recordFrame": T0 + r0, "trackIndex": 2, "mediaType": 1}]) if it else None
        if ti and ti[0]: ti[0].SetProperty("CompositeMode", resolve.COMPOSITE_MULTIPLY); nv += 1
    g = clips.get(EXTRA["grain"]); fin = rf(J["duree"]); r = 0; ng = 0
    while r < fin:
        n = min(500, fin - r)
        ti = mp.AppendToTimeline([{"mediaPoolItem": g, "startFrame": 0, "endFrame": n, "recordFrame": T0 + r, "trackIndex": 4, "mediaType": 1}])
        if ti and ti[0]:
            ti[0].SetProperty("CompositeMode", resolve.COMPOSITE_OVERLAY); ti[0].SetProperty("Opacity", 22.0); ti[0].SetProperty("ZoomX", 2.0); ti[0].SetProperty("ZoomY", 2.0); ng += 1
        r += n
    res = {"titres": out, "grain": ng, "fenetres": nv}
elif ETAPE == "lut":
    p.RefreshLUTList(); tl = p.GetCurrentTimeline(); ok = 0; ko = []
    looks = {}
    for e in J["video"]:
        if e["piste"] == 1: looks[T0 + rf(e["rec"])] = e
    for ti in tl.GetItemListInTrack("video", 1):
        e = looks.get(ti.GetStart())
        if not e or "KINETIC" in e.get("note", ""): continue
        ng = ti.GetNodeGraph()
        if ng is None: ko.append(("sans graphe", e["nom"], e["rec"])); continue
        r1 = ng.SetLUT(1, f"P3/P3_mariage_{e['look']}.cube")
        cdl = e.get("cdl")
        if cdl: ti.SetCDL({"NodeIndex": "1", "Slope": cdl["slope"], "Offset": cdl["offset"], "Power": cdl["power"], "Saturation": cdl.get("sat", "1.0")})
        ok += int(bool(r1))
        if not r1: ko.append(e["nom"])
    res = {"lut_ok": ok, "echecs": ko}
elif ETAPE == "voix":
    tl = p.GetCurrentTimeline(); ok = 0
    vi = globals().get("VI", 35)
    for ti in tl.GetItemListInTrack("audio", 1):
        ok += int(bool(ti.SetVoiceIsolationState({"isEnabled": True, "amount": vi})))
    res = {"isolation_voix": ok, "montant": vi}
pm.SaveProject()
result = res
