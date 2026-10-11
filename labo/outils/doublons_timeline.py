# doublons_timeline.py — à coller tel quel dans l'outil MCP `run_script` de Resolve (bac à sable, sans accès disque).
# Règle de Diego (2026-10-11) : dans un after movie, un événementiel, un run and gun ou un montage dynamique, on ne
# montre JAMAIS deux fois le même moment d'un même rush (un rush peut donner plusieurs plans, à des moments différents).
# Exception seulement si un ressort de récit le justifie (flashback, rappel voulu…) : à écrire dans plan.md.
# Liste chaque plan vidéo (rush, entrée et sortie en secondes du rush) et signale tout chevauchement entre deux plans
# du même rush. À lancer AVANT CHAQUE RENDU. Variables à régler : TIMELINE (None = timeline courante), PISTES, TOL.
TIMELINE = None          # nom de la timeline, ou None
PISTES = None            # liste de pistes vidéo à contrôler, ou None = toutes
TOL = 0.04               # tolérance en secondes (2 images à 50 i/s) : un contact bord à bord n'est pas un doublon
IGNORER = ("blanc", "grain", "noir", "sony_white", "Fusion", "Text")   # flashs, grain, titres, plan de fin fourni

pr = resolve.GetProjectManager().GetCurrentProject()
tl = pr.GetCurrentTimeline()
if TIMELINE:
    for i in range(1, pr.GetTimelineCount() + 1):
        if pr.GetTimelineByIndex(i).GetName() == TIMELINE:
            tl = pr.GetTimelineByIndex(i)
t0 = tl.GetStartFrame()
plans = []
for tr in (PISTES or range(1, tl.GetTrackCount("video") + 1)):
    for it in tl.GetItemListInTrack("video", tr) or []:
        n = it.GetName()
        if any(k.lower() in n.lower() for k in IGNORER) or it.GetMediaPoolItem() is None:
            continue
        s, e = it.GetSourceStartTime(), it.GetSourceEndTime()
        plans.append(dict(piste=tr, debut=it.GetStart() - t0, fin=it.GetEnd() - t0, rush=n,
                          src_in=round(s, 3), src_out=round(e, 3), arret=(e - s) < 0.05))
par_rush = {}
for p in plans:
    par_rush.setdefault(p["rush"].replace("_stabilized", "").split(".")[0], []).append(p)
doublons = []
for r, L in par_rush.items():
    L.sort(key=lambda p: p["src_in"])
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            a, b = L[i], L[j]
            # un arrêt sur image a une durée source presque nulle : on l'élargit à ±1 image pour le comparer
            ai, ao = (a["src_in"] - .02, a["src_out"] + .02) if a["arret"] else (a["src_in"], a["src_out"])
            bi, bo = (b["src_in"] - .02, b["src_out"] + .02) if b["arret"] else (b["src_in"], b["src_out"])
            ch = min(ao, bo) - max(ai, bi)
            if ch > TOL:
                doublons.append(dict(rush=r, plan_a=[a["debut"], a["fin"]], plan_b=[b["debut"], b["fin"]],
                                     source_a=[a["src_in"], a["src_out"]], source_b=[b["src_in"], b["src_out"]],
                                     chevauchement_s=round(ch, 3), arret_sur_image=a["arret"] or b["arret"]))
result = dict(timeline=tl.GetName(), plans=len(plans), rushes=len(par_rush), doublons=len(doublons),
              liste=sorted(doublons, key=lambda d: d["plan_b"][0]))
