"""Coupes de parole au mot près, d'après l'alignement forcé (WhisperX, `aligne.py`).

cale(J, h0, h1) : premier mot qui commence après h0 - 0,3 s, dernier mot qui finit avant h1 + 0,3 s ; la coupe tombe dans le
silence voisin (air de 0,12 à 0,35 s, jamais plus de la moitié du silence). Renvoie (début, fin, texte, avertissements).
Un avertissement si le silence de coupe fait moins de 0,08 s (coupe collée à un mot) ou si l'extrait ne commence pas par une
majuscule / ne finit pas par une ponctuation forte (phrase incomplète probable).
Usage en ligne de commande : parole.py MOTS.json h0 h1   (affiche le découpage et les silences)
"""
import json, sys

def mots(J):
    return [w for s in J["segments"] for w in s["mots"]]

import numpy as np, subprocess
_son = {}
def energie(f, a, b, sr=16000):
    # RMS par trames de 10 ms entre a et b (s) du fichier f
    k = (f, round(a, 2), round(b, 2))
    if k not in _son:
        x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(0, a):.3f}", "-t", f"{b - max(0, a):.3f}", "-i", f, "-ac", "1",
                                          "-ar", str(sr), "-f", "f32le", "-"], capture_output=True).stdout, np.float32)
        n = len(x) // 160; _son[k] = np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1) + 1e-12)
    return _son[k]

def creux(f, a, b, larg=0.08):
    # centre de la fenêtre la plus calme (larg s) entre a et b ; renvoie (temps, niveau dBFS)
    e = energie(f, a, b); w = max(1, int(larg / 0.01))
    if len(e) <= w: return (a + b) / 2, -99
    m = np.convolve(e, np.ones(w) / w, "valid"); i = int(np.argmin(m))
    return a + (i + w / 2) * 0.01, 20 * np.log10(m[i] + 1e-9)

def cale_son(J, f, h0, h1):
    """Comme cale(), mais la coupe tombe au creux d'énergie mesuré entre le mot gardé et son voisin (le silence absorbé par
    l'alignement est retrouvé). Renvoie (début, fin, texte, alertes) ; alerte si le creux reste fort (> -35 dBFS : on coupe
    dans un son, pas dans un silence)."""
    W = mots(J)
    i0 = next(i for i, w in enumerate(W) if w["s"] >= h0 - 0.3 and w["e"] > h0)
    i1 = max(i for i, w in enumerate(W) if w["e"] <= h1 + 0.3 and w["s"] < h1)
    p, n = (W[i0 - 1] if i0 else None), (W[i1 + 1] if i1 + 1 < len(W) else None)
    a0 = max(p["s"] + 0.6 * (p["e"] - p["s"]), W[i0]["s"] - 0.8) if p else W[i0]["s"] - 0.8
    d, ld = creux(f, a0, W[i0]["s"] + 0.04)
    b1 = min(n["s"] + 0.04, W[i1]["e"] + 1.0) if n else W[i1]["e"] + 1.0
    fi, lf = creux(f, max(W[i1]["e"] - 0.25, W[i1]["s"] + 0.6 * (W[i1]["e"] - W[i1]["s"])), b1)
    txt = " ".join(w["m"] for w in W[i0:i1 + 1]); alertes = []
    if ld > -35: alertes.append(f"début dans un son ({ld:.0f} dBFS)")
    if lf > -35: alertes.append(f"fin dans un son ({lf:.0f} dBFS)")
    if not txt[:1].isupper() and not txt.startswith(("«", "\"")): alertes.append("début sans majuscule")
    if not txt.rstrip(" »\"").endswith((".", "!", "?", "…")): alertes.append("fin sans ponctuation forte")
    return round(d, 3), round(fi, 3), txt, alertes

def cale(J, h0, h1, air_av=0.25, air_ap=0.35):
    W = mots(J)
    i0 = next(i for i, w in enumerate(W) if w["s"] >= h0 - 0.3 and w["e"] > h0)
    i1 = max(i for i, w in enumerate(W) if w["e"] <= h1 + 0.3 and w["s"] < h1)
    av = W[i0]["s"] - (W[i0 - 1]["e"] if i0 > 0 else W[i0]["s"] - 2)
    ap = (W[i1 + 1]["s"] if i1 + 1 < len(W) else W[i1]["e"] + 2) - W[i1]["e"]
    d = W[i0]["s"] - max(0.0, min(air_av, av / 2)); f = W[i1]["e"] + max(0.0, min(air_ap, ap / 2))
    txt = " ".join(w["m"] for w in W[i0:i1 + 1]); alertes = []
    if av < 0.08: alertes.append(f"début collé au mot précédent ({av:.2f} s)")
    if ap < 0.08: alertes.append(f"fin collée au mot suivant ({ap:.2f} s)")
    if not txt[:1].isupper() and not txt.startswith(("«", "\"")): alertes.append("début sans majuscule")
    if not txt.rstrip(" »\"").endswith((".", "!", "?", "…")): alertes.append("fin sans ponctuation forte")
    return round(d, 3), round(f, 3), txt, alertes

if __name__ == "__main__":
    J = json.load(open(sys.argv[1])); h0, h1 = float(sys.argv[2]), float(sys.argv[3])
    W = mots(J)
    for k, w in enumerate(W):
        if h0 - 3 <= w["s"] <= h1 + 3:
            gap = w["s"] - W[k - 1]["e"] if k else 0
            print(f"{w['s']:9.3f}-{w['e']:9.3f}  (silence avant {gap:5.2f})  {w['m']}")
    print(cale(J, h0, h1))
