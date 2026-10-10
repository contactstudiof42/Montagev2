#!/usr/bin/env python3
"""Atelier 03 « rythme macro » : même musique, même banque de plans, deux montages.

Usage : python3 build.py <dossier_rendus> [v1|v2...]
Produit : musique.wav, plans/*.mp4, A.mp4 (micro), B.mp4 (macro), planches et mesures JSON.
"""
import json, os, subprocess, sys, wave
import numpy as np

OUT = sys.argv[1]
VER = sys.argv[2] if len(sys.argv) > 2 else "v1"
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f"{OUT}/plans", exist_ok=True)

SR, BPM, FPS = 48000, 140, 25
BEAT = 60 / BPM            # 0,4286 s
BAR = 4 * BEAT             # 1,714 s
NBARS = 14
DUR = NBARS * BAR          # 24 s
W, H = 480, 270

def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# ---------- musique synthétique (drill 140 BPM, ressenti demi-temps) ----------
def musique(path):
    n = int(DUR * SR); t = np.arange(n) / SR
    mix = np.zeros(n)
    rng = np.random.default_rng(3)
    def add(sig, start):
        i = int(start * SR); j = min(n, i + len(sig)); mix[i:j] += sig[: j - i]
    def env(d, a=0.002, r=None):
        m = int(d * SR); e = np.ones(m)
        k = int(a * SR); e[:k] = np.linspace(0, 1, k)
        r = r or d; e *= np.exp(-np.arange(m) / (r * SR / 5))
        return e
    hat = rng.standard_normal(int(0.04 * SR)); hat = np.diff(hat, prepend=0) * env(0.04, r=0.03) * 0.12
    snare = (rng.standard_normal(int(0.25 * SR)) * 0.5 + np.sin(2 * np.pi * 190 * np.arange(int(0.25 * SR)) / SR)) * env(0.25, r=0.15) * 0.35
    def k808(d, f0=49, f1=41):
        m = int(d * SR); tt = np.arange(m) / SR
        f = f1 + (f0 * 2.5 - f1) * np.exp(-tt * 30)
        ph = 2 * np.pi * np.cumsum(f) / SR
        return np.tanh(2.2 * np.sin(ph)) * env(d, r=d * 0.9) * 0.5
    # nappe sombre sur tout le morceau (mineur), filtrée par section
    pad = sum(np.sin(2 * np.pi * f * t + i) for i, f in enumerate([110, 130.8, 164.8, 98])) * 0.05
    sect = np.ones(n)
    for b in range(NBARS):
        s = int(b * BAR * SR); e = int((b + 1) * BAR * SR)
        if b == 12: sect[s:e] = 0.5   # coupure : la nappe reste seule
    mix += pad * sect
    for b in range(NBARS):
        t0 = b * BAR
        intro, couplet, coupure = b < 4, 4 <= b < 12, b == 12
        if coupure: continue
        # charleston : croches en intro, triolets de doubles en couplet (signature drill)
        step = BEAT / 2 if intro else BEAT / 3
        k = 0
        while k * step < BAR - 1e-6:
            add(hat * (0.6 if intro else (1.0 if k % 3 == 0 else 0.55)), t0 + k * step); k += 1
        if intro: continue
        # caisse claire sur le 3e temps (demi-temps), 808 syncopée
        add(snare, t0 + 2 * BEAT)
        for pos, d in [(0, 0.6), (1.5 * BEAT, 0.35), (2.75 * BEAT, 0.5)]:
            add(k808(d), t0 + pos)
        if b == 11:  # roulement avant la coupure
            for r in range(6): add(snare * 0.5, t0 + 3 * BEAT + r * BEAT / 6)
    mix = mix / np.max(np.abs(mix)) * 0.8
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((mix * 32767).astype(np.int16).tobytes())

# ---------- banque de plans (palette acier ; un seul plan chaud) ----------
FROID = "hue=s=0.06,colorbalance=bs=0.10:bm=0.05:rh=-0.05,eq=contrast=1.25:brightness=-0.06"
PLANS = {
    "p1_mandel_lent": f"mandelbrot=s={W}x{H}:rate={FPS}:start_scale=2.5:end_scale=0.6:end_pts={DUR*FPS},{FROID}",
    "p2_mandel_bord": f"mandelbrot=s={W}x{H}:rate={FPS}:start_x=-0.743643887:start_y=0.131825904:start_scale=0.05:end_scale=0.002:end_pts={DUR*FPS},{FROID}",
    "p3_life": f"life=s={W//2}x{H//2}:rate={FPS}:mold=10:ratio=0.3:life_color=#c8d0d8:death_color=#101418:mold_color=#38444c,scale={W}:{H}:flags=neighbor,{FROID}",
    "p4_cellauto": f"cellauto=s={W}x{H}:rate={FPS}:rule=110:scroll=1,{FROID},boxblur=1",
    "p5_gradients": f"gradients=s={W}x{H}:rate={FPS}:c0=0x0a0e12:c1=0x5a6670:speed=0.02:type=radial,{FROID},noise=alls=12:allf=t",
    # le seul plan chaud : braise orange, lente
    "p6_braise": f"mandelbrot=s={W}x{H}:rate={FPS}:start_x=-1.25066:start_y=0.02012:start_scale=0.02:end_scale=0.005:end_pts={DUR*FPS*3},hue=s=0,colorchannelmixer=rr=1.0:gg=0.5:bb=0.12,eq=contrast=1.5:brightness=-0.05",
}

def plans():
    for nom, src in PLANS.items():
        p = f"{OUT}/plans/{nom}.mp4"
        if not os.path.exists(p):
            run(["ffmpeg", "-y", "-f", "lavfi", "-i", src, "-t", f"{DUR:.3f}", "-pix_fmt", "yuv420p",
                 "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", p])

# ---------- montages (EDL = liste de (plan, entrée source, durée)) ----------
ORDRE = ["p1_mandel_lent", "p2_mandel_bord", "p3_life", "p4_cellauto", "p5_gradients"]

def edl_A():
    """Micro : une coupe tous les 2 temps, rotation des plans froids. Le plan chaud tombe où il tombe."""
    edl, t, i = [], 0.0, 0
    pas = 2 * BEAT
    banque = ORDRE + ["p6_braise"]
    while t < DUR - 1e-6:
        d = min(pas, DUR - t)
        edl.append((banque[i % len(banque)], t, d)); t += d; i += 1
    return edl

def edl_B():
    """Macro : la densité suit l'arrangement."""
    edl = [("p1_mandel_lent", 0.0, 4 * BAR)]                 # intro : un seul plan tenu
    t = 4 * BAR; i = 1
    for b in range(4, 12):
        cuts = [BAR] if b < 8 else [BAR / 2, BAR / 2]        # montée de densité sur les 4 dernières mesures
        for d in cuts:
            edl.append((ORDRE[i % len(ORDRE)], t, d)); t += d; i += 1
    edl.append(("p6_braise", 0.0, BAR))                      # coupure : seul plan chaud, ralenti (cf. rendu)
    edl.append(("p1_mandel_lent", 4 * BAR, BAR))             # reprise : retour au plan d'ouverture, là où il s'était arrêté
    return edl

def edl_C():
    """Hybride (v3) : structure macro (intro tenue, coupure chaude, reprise), énergie micro dans le couplet
    (2 temps, puis 1 temps sur les 2 dernières mesures)."""
    edl = [("p1_mandel_lent", 0.0, 4 * BAR)]
    t = 4 * BAR; i = 1
    for b in range(4, 12):
        pas = 2 * BEAT if b < 10 else BEAT
        for _ in range(int(round(BAR / pas))):
            edl.append((ORDRE[i % len(ORDRE)], t, pas)); t += pas; i += 1
    edl.append(("p6_braise", 0.0, BAR))
    edl.append(("p1_mandel_lent", 4 * BAR, BAR))
    return edl

def rendu(nom, edl, horloge):
    parts = []
    t_tl = 0.0  # position sur la timeline : on coupe sur des numéros d'image ABSOLUS (sinon l'arrondi dérive)
    for k, (plan, src_t, d) in enumerate(edl):
        seg = f"{OUT}/{nom}_seg{k:03d}.mp4"
        if VER != "v1":
            nfr = round((t_tl + d) * FPS) - round(t_tl * FPS)
        t_tl += d
        vf = f"scale={W}:{H},fps={FPS}"
        if plan == "p6_braise" and nom in ("B", "C"):
            vf = f"setpts=2.0*PTS,{vf}"   # ralenti x0,5 sur la coupure
            src_t = src_t / 2
        lim = ["-t", f"{d:.4f}"] if VER == "v1" else ["-frames:v", str(nfr)]
        run(["ffmpeg", "-y", "-ss", f"{src_t:.4f}", "-i", f"{OUT}/plans/{plan}.mp4", *lim,
             "-vf", vf, "-an", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", seg])
        parts.append(seg)
    lst = f"{OUT}/{nom}_list.txt"
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    vf = "null"
    if horloge:  # seconde horloge : +6 % de lumière une image sur 15 (0,6 s), hors tempo
        vf = "eq=brightness='if(eq(mod(n\\,15)\\,0)\\,0.06\\,0)':eval=frame"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", f"{OUT}/musique.wav",
         "-vf", vf, "-t", f"{DUR:.3f}", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "160k", "-shortest", f"{OUT}/{nom}.mp4"])
    for p in parts: os.remove(p)

def mesures(nom, edl):
    coupes = np.cumsum([d for _, _, d in edl])[:-1]
    demi = BAR / 2
    sur_arr = [abs(c / demi - round(c / demi)) * demi < 1 / FPS for c in coupes]
    sur_temps = [abs(c / BEAT - round(c / BEAT)) * BEAT < 1 / FPS for c in coupes]
    durees = [d for _, _, d in edl]
    return {"montage": nom, "plans": len(edl), "coupes": len(coupes),
            "duree_moy_s": round(float(np.mean(durees)), 3), "duree_min_s": round(min(durees), 3),
            "duree_max_s": round(max(durees), 3), "ecart_type_s": round(float(np.std(durees)), 3),
            "coupes_sur_demi_mesure_pct": round(100 * sum(sur_arr) / max(1, len(coupes)), 1),
            "coupes_sur_temps_pct": round(100 * sum(sur_temps) / max(1, len(coupes)), 1),
            "apparitions_plan_chaud": sum(1 for p, _, _ in edl if p == "p6_braise"),
            "coupes_par_section": {
                "intro(0-4)": int(sum(c < 4 * BAR for c in coupes)),
                "couplet(4-12)": int(sum(4 * BAR <= c < 12 * BAR for c in coupes)),
                "fin(12-14)": int(sum(c >= 12 * BAR for c in coupes))}}

def coupes_reelles(nom):
    """Coupes détectées dans le rendu (scdet), comparées à la grille musicale."""
    r = subprocess.run(["ffmpeg", "-i", f"{OUT}/{nom}.mp4", "-vf", "scdet=threshold=8", "-an", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    ts = [float(l.split("lavfi.scd.time:")[1].split()[0]) for l in r.splitlines() if "lavfi.scd.time:" in l]
    ecarts = [round((t - round(t / (BEAT)) * BEAT) * 1000) for t in ts]  # ms par rapport au temps le plus proche
    return {"coupes_detectees": len(ts), "ecart_au_temps_ms": ecarts,
            "ecart_max_ms": max(map(abs, ecarts)) if ecarts else None}

def planche(nom):
    # une image par temps (56 vignettes) en 14 colonnes = une ligne par 4 mesures... ici 1 colonne = 1 temps, 1 ligne = 1 mesure
    run(["ffmpeg", "-y", "-i", f"{OUT}/{nom}.mp4", "-vf",
         f"fps={1/BEAT:.6f},scale=96:54,tile=4x{NBARS}:padding=2:color=0x202020", "-frames:v", "1",
         f"{HERE}/{VER}-{nom}-timeline.png"])

if __name__ == "__main__":
    musique(f"{OUT}/musique.wav")
    plans()
    res = {}
    montages = [("A", edl_A(), False), ("B", edl_B(), True)]
    if VER >= "v3": montages = [("C", edl_C(), True)]
    for nom, edl, horloge in montages:
        rendu(nom, edl, horloge); planche(nom); res[nom] = mesures(nom, edl); res[nom]["reel"] = coupes_reelles(nom)
        res[nom]["edl"] = [(p, round(s, 3), round(d, 3)) for p, s, d in edl]
    with open(f"{HERE}/{VER}-mesures.json", "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "edl"} for k, v in res.items()}, indent=1, ensure_ascii=False))
