# resolve_lib.py : fonctions à coller en tête des scripts run_script de la V4 (bac à sable Resolve, sans accès disque).
# Une image de composition = une image source à 50 i/s, image 0 = point d'entrée du plan.
def trouve_clip(nom):
    mp = project.GetMediaPool(); pile = [mp.GetRootFolder()]
    while pile:
        f = pile.pop()
        for c in f.GetClipList() or []:
            if c.GetName() == nom: return c
        pile += f.GetSubFolderList() or []
def pose(tl, nom, piste, debut, fin, src, lut=None, t0=90000):
    c = trouve_clip(nom)
    r = project.GetMediaPool().AppendToTimeline([{"mediaPoolItem": c, "startFrame": src, "endFrame": src + 2 * (fin - debut),
                                                  "trackIndex": piste, "recordFrame": t0 + debut}])
    it = r[0]
    if lut: it.GetNodeGraph().SetLUT(1, lut)
    return it
def comp_de(it):
    if it.GetFusionCompCount() == 0: it.AddFusionComp()
    comp = it.GetFusionCompByIndex(1)
    mi = comp.FindTool("MediaIn1"); mo = comp.FindTool("MediaOut1")
    return comp, mi, mo
def transfo(comp, nom, entree, cles=None, fixe=None, flou=False):
    # cles : [[image, Size, Angle, X, Y], ...] ; fixe : dict(size, cx, cy[, ang])
    t = comp.AddTool("Transform", -32768, -32768); t.SetAttrs({"TOOLS_Name": nom})
    t.ConnectInput("Input", entree)
    if cles:
        t.AddModifier("Size", "BezierSpline"); t.AddModifier("Angle", "BezierSpline"); t.AddModifier("Center", "XYPath")
        xy = t.Center.GetConnectedOutput().GetTool()
        for i, s, a, x, y in cles:
            t.SetInput("Size", s, i); t.SetInput("Angle", a, i); xy.SetInput("X", x, i); xy.SetInput("Y", y, i)
    elif fixe:
        t.SetInput("Size", fixe["size"]); t.SetInput("Center", {1: fixe["cx"], 2: fixe["cy"]})
    if flou:
        t.SetInput("MotionBlur", 1); t.SetInput("Quality", 8); t.SetInput("ShutterAngle", 180)
    return t
def anime(comp, nom, entree, cles, flou=True):
    # cles : [[image, {"size", "cx", "cy"}], ...]
    t = comp.AddTool("Transform", -32768, -32768); t.SetAttrs({"TOOLS_Name": nom}); t.ConnectInput("Input", entree)
    t.AddModifier("Size", "BezierSpline"); t.AddModifier("Center", "XYPath")
    xy = t.Center.GetConnectedOutput().GetTool()
    for i, k in cles:
        t.SetInput("Size", k["size"], i); xy.SetInput("X", k["cx"], i); xy.SetInput("Y", k["cy"], i)
    if flou: t.SetInput("MotionBlur", 1); t.SetInput("Quality", 8); t.SetInput("ShutterAngle", 180)
    return t
