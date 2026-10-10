"""Continuité de direction à une coupe A|B par flot optique.
python3 mesure_flot.py DOSSIER_CAS [--mvs]   (DOSSIER_CAS contient <cas>/A, <cas>/B et éventuellement verite.json)
python3 mesure_flot.py --paire dossierA dossierB   (une seule coupe, sans vérité terrain)

Méthode 1 : Farneback dense (OpenCV) sur les 3 paires d'images avant la coupe (A n-3→n) et après (B 1→4).
Méthode 2 (--mvs) : vecteurs de mouvement du codec (A+B encodés en H.264, export_mvs lu par PyAV).
Vecteur dominant = médiane des vecteurs ; confiance = cohérence |Σv|/Σ|v| et part de pixels à < 30° du dominant."""
import sys, os, glob, json, time, subprocess, tempfile, numpy as np, cv2

def lit(d): return [cv2.imread(f, cv2.IMREAD_GRAYSCALE) for f in sorted(glob.glob(d + "/f_*.png"))]

def resume(fx, fy):
    """Vecteur dominant (médiane), cohérence et part de vecteurs alignés à < 30°."""
    v = np.array([np.median(fx), np.median(fy)]); mag = np.hypot(fx, fy)
    coh = np.hypot(fx.sum(), fy.sum()) / (mag.sum() + 1e-9)
    nv = np.linalg.norm(v)
    if nv < 1e-6: return v, coh, 0.0
    cosang = (fx * v[0] + fy * v[1]) / (mag * nv + 1e-9)
    return v, coh, float(((cosang > np.cos(np.radians(30))) & (mag > .3 * nv)).mean())

def fb_plein(a, b):   # Farneback « classique » pleine résolution, pyramide 6 niveaux
    return cv2.calcOpticalFlowFarneback(a, b, None, .5, 6, 25, 5, 7, 1.5, cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
def fb_quart(a, b):   # Farneback sur images réduites au quart (le filé devient un déplacement de ~10 px)
    r = lambda x: cv2.resize(x, (x.shape[1] // 4, x.shape[0] // 4), interpolation=cv2.INTER_AREA)
    return 4 * cv2.resize(cv2.calcOpticalFlowFarneback(r(a), r(b), None, .5, 3, 15, 5, 5, 1.2, 0), (a.shape[1], a.shape[0]))
def dis(a, b):        # DIS (OpenCV), recherche par patchs grossier→fin
    return cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM).calc(a, b, None)
METHODES = {"fb": fb_plein, "fb4": fb_quart, "dis": dis}

def flot(fn, a, b, m=8):
    f = fn(a, b)[m:-m, m:-m]; return resume(f[..., 0].ravel(), f[..., 1].ravel())

def cote(paires, fn):
    """Moyenne des 3 paires : vecteur, cohérence, part alignée."""
    r = [flot(fn, a, b) for a, b in paires]
    return np.mean([x[0] for x in r], 0), float(np.mean([x[1] for x in r])), float(np.mean([x[2] for x in r]))

def mvs(dA, dB):
    """Vecteurs de mouvement du codec : A puis B concaténés, H.264 sans B-frames, recherche exhaustive large."""
    import av
    with tempfile.TemporaryDirectory() as t:
        lst = sorted(glob.glob(dA + "/f_*.png")) + sorted(glob.glob(dB + "/f_*.png"))
        for i, f in enumerate(lst): os.symlink(os.path.abspath(f), f"{t}/s_{i:03d}.png")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{t}/s_%03d.png", "-c:v", "libx264", "-bf", "0", "-g", "999",
                        "-sc_threshold", "0", "-x264-params", "me=esa:merange=128:subme=7", "-crf", "18",
                        "-pix_fmt", "yuv420p", f"{t}/v.mp4"], check=True)
        c = av.open(f"{t}/v.mp4"); s = c.streams.video[0]; s.codec_context.options = {"flags2": "+export_mvs"}
        par_image = []
        for fr in c.decode(s):
            sd = fr.side_data.get("MOTION_VECTORS") if hasattr(fr.side_data, "get") else None
            if sd is None:
                try: sd = fr.side_data["MOTION_VECTORS"]
                except Exception: sd = None
            if sd is None: par_image.append(None); continue
            a = sd.to_ndarray(); a = a[a["source"] == -1]
            if len(a) == 0: par_image.append(None); continue
            w = a["w"].astype(float) * a["h"]   # pondération par surface de bloc (répétition simple)
            rep = np.maximum((w / w.min()).astype(int), 1)
            fx = np.repeat((a["dst_x"] - a["src_x"]).astype(float), rep); fy = np.repeat((a["dst_y"] - a["src_y"]).astype(float), rep)
            par_image.append(resume(fx, fy))
        c.close()
    n = len(sorted(glob.glob(dA + "/f_*.png")))
    def moy(ix):
        r = [par_image[i] for i in ix if par_image[i] is not None]
        if not r: return np.zeros(2), 0.0, 0.0
        return np.mean([x[0] for x in r], 0), float(np.mean([x[1] for x in r])), float(np.mean([x[2] for x in r]))
    return moy(range(n - 3, n)), moy(range(n + 1, n + 4))   # B : images 2..4 (l'image 1 après la coupe est surtout intra)

def decide(vA, cA, vB, cB, seuil_mvt=1.0, seuil_coh=.4):
    nA, nB = np.linalg.norm(vA), np.linalg.norm(vB)
    cos = float(vA @ vB / (nA * nB + 1e-9)); pond = float(vA @ vB / (max(nA, nB) ** 2 + 1e-9))
    if max(nA, nB) < seuil_mvt: return "statique", cos, pond
    if min(cA, cB) < seuil_coh: return "incertain", cos, pond
    if min(nA, nB) < seuil_mvt: return "arret", cos, pond
    if cos >= .7: return "raccord", cos, pond
    if cos <= -.5: return "inverse", cos, pond
    return "cassure", cos, pond

def cascade(r, seuil_coh=.85):
    """Règle retenue : DIS si cohérence >= 0,85 des deux côtés, sinon vecteurs du codec, sinon « incertain »."""
    for m in ("dis", "mv"):
        if m not in r: continue
        x = r[m]; d = decide(np.array(x["vA"]), x["cohA"], np.array(x["vB"]), x["cohB"], seuil_coh=seuil_coh)
        if d[0] != "incertain": return d[0], m, round(d[1], 2)
    return "incertain", "-", None

def mesure(dA, dB, avec_mvs=False):
    A, B = lit(dA), lit(dB); r = {}
    for nom, fn in METHODES.items():
        t0 = time.time()
        vA, cA, pA = cote([(A[i], A[i + 1]) for i in range(len(A) - 4, len(A) - 1)], fn)
        vB, cB, pB = cote([(B[i], B[i + 1]) for i in range(0, 3)], fn)
        r[nom] = dict(vA=vA.round(1).tolist(), vB=vB.round(1).tolist(), cohA=round(cA, 2), cohB=round(cB, 2),
                      alA=round(pA, 2), alB=round(pB, 2), t=round(time.time() - t0, 2))
        r[nom]["decision"], r[nom]["cos"], r[nom]["pond"] = decide(vA, cA, vB, cB)
    if avec_mvs:
        t0 = time.time(); (mA, kA, qA), (mB, kB, qB) = mvs(dA, dB)
        r["mv"] = dict(vA=mA.round(1).tolist(), vB=mB.round(1).tolist(), cohA=round(kA, 2), cohB=round(kB, 2), t=round(time.time() - t0, 2))
        r["mv"]["decision"], r["mv"]["cos"], r["mv"]["pond"] = decide(mA, kA, mB, kB)
    return r

if __name__ == "__main__":
    if sys.argv[1] == "--paire":
        print(json.dumps(mesure(sys.argv[2], sys.argv[3], "--mvs" in sys.argv), indent=1)); sys.exit()
    racine = sys.argv[1]; avec = "--mvs" in sys.argv
    vt = json.load(open(racine + "/verite.json")); tout = {}
    meth = list(METHODES) + (["mv"] if avec else []); ok = {m: 0 for m in meth}
    print("| cas | vérité | " + " | ".join(f"{m} vA → vB (px/img) · coh · cos · décision" for m in meth) + " |")
    print("|---|---|" + "---|" * len(meth))
    for nom, g in vt.items():
        r = mesure(f"{racine}/{nom}/A", f"{racine}/{nom}/B", avec); tout[nom] = r; cel = []
        for m in meth:
            f = r[m]; ok[m] += f["decision"] == g["verite"]
            v = lambda x: "(%.0f,%.0f)" % tuple(x)
            cel.append(f"{v(f['vA'])}→{v(f['vB'])} · {min(f['cohA'], f['cohB']):.2f} · {f['cos']:.2f} · {f['decision']}{'' if f['decision'] == g['verite'] else ' ✗'}")
        print(f"| {nom} | {g['verite']} | " + " | ".join(cel) + " |", flush=True)
    print("\nRéussites : " + " ; ".join(f"{m} {ok[m]}/{len(vt)}" for m in meth))
    print("temps moyen par coupe (6 paires) : " + " ; ".join(f"{m} %.2f s" % np.mean([r[m]["t"] for r in tout.values()]) for m in meth))
    if avec:
        c = {k: cascade(r) for k, r in tout.items()}
        bon = sum(c[k][0] == vt[k]["verite"] for k in c); abst = sum(c[k][0] == "incertain" for k in c)
        print(f"Cascade DIS→MV (coh >= 0,85) : {bon}/{len(c)} justes, {abst} « incertain », {len(c) - bon - abst} erreurs")
        for k in c: print(f"  {k}: {c[k]}")
    json.dump(tout, open(racine + "/resultats.json", "w"), indent=1)
