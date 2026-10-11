# gen_ouverture.py : écrit le script Resolve (à coller dans run_script) de l'ouverture V4 :
# K, O, R, E épinglées (stabiliser.py --mode fixe) et calées au même point (même hauteur de lettre), puis zoom infini
# du E (piste V2, bord fondu) vers le plan large KORE (piste V1), alignés par SIFT (E_vers_KORE.json).
import json, math, sys
W = "videos/phase-3/sony-linkbuds/_travail/kore/"
L = json.load(open(W + "lettres.json")); EK = json.load(open(W + "E_vers_KORE.json"))
Q0 = (560.0, 990.0); HT = 720.0          # point commun et hauteur commune des lettres (px, image 1080x1920)
plans = [("C6491", 0, 13, 0.30), ("C6492", 13, 24, 0.60), ("C6493", 24, 36, 0.50), ("C6494", 36, 41, 0.80)]
nx = lambda x: x / 1080.0; ny = lambda y: 1 - y / 1920.0
data = {"lettres": [], "E2": None, "KORE": None}
for c, a, b, t0 in plans:
    st = json.load(open(W + f"st_{c}.json")); base = st["base"]; l = L[c]
    # centre de la lettre après le Transform Stab (zoom base autour du centre de l'image)
    px, py = 540 + base * (l["cx"] - 540), 960 + base * (l["cy"] - 960)
    k = HT / (l["h"] * base)
    cale = dict(size=k, cx=nx(Q0[0]) - k * (nx(px) - 0.5), cy=ny(Q0[1]) - k * (ny(py) - 0.5))
    cles = [[d["image"], d["Size"], d["Angle"], d["X"], d["Y"]] for d in st["cles"] if d["image"] >= -2]
    data["lettres"].append(dict(rush=c, debut=a, fin=b, src=round(t0 * 50), cles=cles, cale=cale))
# E sur V2 (41-48) : mêmes clés décalées de 10 images source (entrée à 1,00 s au lieu de 0,80)
e = data["lettres"][3]
data["E2"] = dict(rush="C6494", debut=41, fin=48, src=50, cles=[[i - 10, s, an, x, y] for i, s, an, x, y in e["cles"] if i >= 8], cale=e["cale"])
# zoom : le E (centre Q0, échelle kE = HT/h) doit finir là où le E est dans le plan large (centre pE, échelle s)
s = EK["s"]; M = EK["M"]; lE = L["C6494"]
pE = (M[0][0] * lE["cx"] + M[0][1] * lE["cy"] + M[0][2], M[1][0] * lE["cx"] + M[1][1] * lE["cy"] + M[1][2])
kE = HT / lE["h"]; Z0 = kE / s          # échelle du plan large au départ du zoom
N = 14                                    # 7 images de timeline = 14 images source
zoom = []
for i in range(N + 1):
    u = i / N; e_ = u * u * (3 - 2 * u)                       # départ et arrivée freinés
    z = math.exp(math.log(Z0) * (1 - e_))                     # échelle du plan large (exponentielle : vitesse perçue constante)
    q = (Q0[0] + (pE[0] - Q0[0]) * e_, Q0[1] + (pE[1] - Q0[1]) * e_)
    ang = EK["ang"] * (1 - e_)                                # +0,9° au départ (le plan large est tourné), 0 à l'arrivée
    # plan large : son point pE doit être en q, échelle z
    kc = dict(size=z, cx=nx(q[0]) - z * (nx(pE[0]) - 0.5), cy=ny(q[1]) - z * (ny(pE[1]) - 0.5), ang=ang)
    # E (déjà épinglé en Q0) : échelle relative r = z / Z0 autour de Q0, puis déplacé en q
    r = z / Z0
    ke = dict(size=r, cx=nx(q[0]) - r * (nx(Q0[0]) - 0.5), cy=ny(q[1]) - r * (ny(Q0[1]) - 0.5), ang=ang)
    zoom.append([i, kc, ke])
data["KORE"] = dict(rush="C6495", debut=41, fin=71, src=6, zoom=zoom, Z0=Z0)
print(json.dumps(dict(Z0=round(Z0, 3), pE=[round(v, 1) for v in pE], cales=[round(d["cale"]["size"], 3) for d in data["lettres"]])), file=sys.stderr)
json.dump(data, open(W + "ouverture.json", "w"))
