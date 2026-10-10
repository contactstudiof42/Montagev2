#!/usr/bin/env python3
"""Pièce 24 « Face caméra » : une prise brute (marionnette 2D + voix espeak-ng),
puis quatre montages du même dérushage (A jump cuts, B punch-in alterné,
C punch-in sur les chutes, D = C + B-roll métaphorique).

Usage : python3 piece.py OUTDIR [--versions A,B,C,D] [--handle 0.10]
Écrit OUTDIR/brut.wav, OUTDIR/<V>.mp4, OUTDIR/<V>-events.json.
"""
import json, math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FPS = 25
W, H = 960, 540          # rendu source (sur-échantillonné pour le punch-in)
OW, OH = 640, 360        # sortie
SR = 22050
FONT = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"

# (texte, type) ; type : ok | flub | pause ; drapeaux : chute, broll
PRISE = [
    ("Chaque nuit, vous rêvez pendant à peu près deux heures.", "ok", {}),
    ("Et au réveil, vous... non, attends.", "flub", {}),
    ("Et au réveil, presque tout a disparu.", "ok", {}),
    (1.2, "pause", {}),
    ("Ce n'est pas que vos rêves soient faibles.", "ok", {}),
    ("C'est que la mémoire, la nuit, est en partie débranchée.", "ok", {"chute": 1}),
    ("La nora... la noradré...", "flub", {}),
    ("Une molécule, la noradrénaline, qui aide à graver les souvenirs, est presque absente pendant le sommeil paradoxal.", "ok", {"broll": "rec"}),
    (1.0, "pause", {}),
    ("Résultat : vous vivez le rêve, mais rien ne l'enregistre.", "ok", {"chute": 1}),
    ("Alors, un conseil.", "ok", {}),
    ("Gardez un carnet à côté du lit, et écrivez avant même de bouger.", "ok", {"broll": "carnet"}),
    ("Bouger, c'est déjà oublier.", "ok", {"chute": 1}),
]


def tts(text, path):
    subprocess.run(["espeak-ng", "-v", "fr", "-s", "150", "-p", "40", "-w", path, text], check=True)
    with wave.open(path) as w:
        sr = w.getframerate()
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    if sr != SR:  # rééchantillonnage linéaire simple
        t = np.linspace(0, len(a) / sr, int(len(a) * SR / sr), endpoint=False)
        a = np.interp(t, np.arange(len(a)) / sr, a)
    # retirer les silences de bord d'espeak
    nz = np.where(np.abs(a) > 0.01)[0]
    return a[nz[0]:nz[-1] + 1] if len(nz) else a


def prise_brute(out):
    """Construit l'audio brut et la liste des segments (vérité terrain)."""
    parts, segs, t = [], [], 0.0
    gap = np.zeros(int(0.35 * SR), np.float32)  # respiration entre phrases
    for i, (txt, kind, flags) in enumerate(PRISE):
        if kind == "pause":
            a = np.zeros(int(txt * SR), np.float32)
        else:
            a = tts(txt, os.path.join(out, f"_seg{i}.wav")).astype(np.float32)
            os.remove(os.path.join(out, f"_seg{i}.wav"))
        segs.append({"i": i, "kind": kind, "t0": t, "t1": t + len(a) / SR, "flags": flags,
                     "texte": txt if kind != "pause" else ""})
        parts += [a, gap]
        t += (len(a) + len(gap)) / SR
    audio = np.concatenate(parts)
    audio = 0.5 * audio / max(1e-6, np.abs(audio).max())
    return audio, segs


def enveloppe(audio):
    n = int(math.ceil(len(audio) / SR * FPS))
    env = np.zeros(n)
    hop = SR // FPS
    for f in range(n):
        s = audio[f * hop:(f + 1) * hop]
        env[f] = np.sqrt(np.mean(s ** 2)) if len(s) else 0
    return np.clip(env / (env.max() + 1e-9) * 1.4, 0, 1)


def regard_detourne(t, segs):
    for s in segs:
        if s["kind"] == "flub" and s["t0"] - 0.1 <= t <= s["t1"] + 0.3:
            return 1.0
    return 0.0


def pose(t, e, segs):
    """Centre de la tête (px, rendu W x H) et regard détourné."""
    sway = SWAY * (14 * math.sin(2 * math.pi * 0.23 * t) + 6 * math.sin(2 * math.pi * 0.61 * t + 1))
    nod = 5 * e * math.sin(2 * math.pi * 3.1 * t)
    look = regard_detourne(t, segs)
    return W / 2 + sway + 40 * look, 250 + nod + 10 * look, look


SWAY = 1.0


def frame_brute(f, env, segs):
    """Personne en plan rapproché poitrine, caméra fixe. Bouge comme un corps qui parle."""
    t = f / FPS
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    # fond : un mur, une étagère floue, une lampe chaude à droite (décor de chaîne)
    for y in range(H):
        c = int(46 + 18 * y / H)
        d.line([(0, y), (W, y)], fill=(c, c - 4, c - 10))
    d.rectangle([90, 150, 330, 162], fill=(70, 58, 48))
    for k, col in enumerate([(120, 60, 50), (60, 90, 120), (150, 130, 70), (80, 110, 80)]):
        d.rectangle([110 + k * 45, 100 - (k % 2) * 12, 140 + k * 45, 150], fill=col)
    d.ellipse([760, 120, 840, 200], fill=(230, 170, 90))
    # corps : balancement lent + petites relances sur l'énergie de la voix
    e = env[min(f, len(env) - 1)]
    cx, cy, look = pose(t, e, segs)
    # épaules / buste
    d.polygon([(cx - 190, H), (cx - 150, cy + 150), (cx + 150, cy + 150), (cx + 190, H)], fill=(40, 70, 95))
    d.rectangle([cx - 30, cy + 95, cx + 30, cy + 155], fill=(205, 160, 130))
    # tête
    d.ellipse([cx - 95, cy - 125, cx + 95, cy + 120], fill=(215, 170, 140))
    d.chord([cx - 100, cy - 135, cx + 100, cy + 10], 180, 360, fill=(50, 35, 28))  # cheveux
    # yeux : regard caméra, ou détourné en bas à droite pendant les ratés ; clignements
    blink = any(abs(t - b) < 0.06 for b in np.arange(1.7, 60, 3.3))
    gx, gy = 9 * look, 7 * look
    for ex in (-38, 38):
        if blink:
            d.line([cx + ex - 16, cy - 15, cx + ex + 16, cy - 15], fill=(40, 30, 25), width=4)
        else:
            d.ellipse([cx + ex - 16, cy - 26, cx + ex + 16, cy - 4], fill=(245, 245, 240))
            d.ellipse([cx + ex - 7 + gx, cy - 22 + gy, cx + ex + 7 + gx, cy - 8 + gy], fill=(35, 30, 30))
    # sourcils : se lèvent sur l'énergie
    for ex in (-38, 38):
        d.line([cx + ex - 18, cy - 40 - 6 * e, cx + ex + 18, cy - 42 - 6 * e], fill=(50, 35, 28), width=6)
    # bouche
    mo = 4 + 30 * e
    d.ellipse([cx - 28, cy + 50 - mo / 2, cx + 28, cy + 50 + mo / 2], fill=(110, 40, 45))
    return img


def broll_frame(kind, t_local, dur):
    img = Image.new("RGB", (W, H), (12, 12, 14))
    d = ImageDraw.Draw(img)
    if kind == "rec":
        # un voyant REC qui clignote... puis s'éteint (la mémoire débranchée)
        on = t_local < dur * 0.45 and int(t_local * 2) % 2 == 0
        col = (220, 30, 30) if on else (70, 70, 72)
        d.ellipse([W / 2 - 150, H / 2 - 30, W / 2 - 90, H / 2 + 30], fill=col)
        fnt = ImageFont.truetype(FONT, 64)
        d.text((W / 2 - 60, H / 2 - 40), "REC", font=fnt, fill=(200, 200, 200) if on else (90, 90, 92))
    else:
        # un carnet sur une table de nuit, une ligne d'écriture qui avance
        img.paste((28, 24, 22), [0, 0, W, H])
        d.rectangle([250, 90, 710, 470], fill=(236, 230, 214))
        for k in range(8):
            d.line([280, 140 + k * 40, 680, 140 + k * 40], fill=(190, 200, 215), width=2)
        prog = min(1, t_local / (dur * 0.9))
        x1 = 290 + 370 * prog
        xs = np.arange(290, x1, 3)
        pts = [(x, 170 + 8 * math.sin(x / 7) * math.sin(x / 31)) for x in xs]
        if len(pts) > 1:
            d.line(pts, fill=(30, 40, 90), width=3)
        d.line([x1, 172, x1 + 70, 100], fill=(20, 20, 20), width=9)  # stylo
    return img


def recadre(img, z, cible=(0.5, 0.44)):
    """Punch-in : recadrage centré sur le visage, sortie OWxOH."""
    if z == 1.0:
        return img.resize((OW, OH), Image.LANCZOS)
    cw, ch = W / z, H / z
    x0 = min(max(cible[0] * W - cw / 2, 0), W - cw)
    y0 = min(max(cible[1] * H - ch / 2, 0), H - ch)
    return img.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((OW, OH), Image.LANCZOS)


def montage(version, segs, handle):
    """Retourne la liste de plans : (t_in, t_out, zoom, broll|None, seg).
    A, B : dérushage serré (chaque respiration coupée). A0, C, D : dérushage
    minimal (on ne coupe que les ratés et les silences ; les phrases
    consécutives restent d'un seul tenant, la coupe y est invisible en temps)."""
    serre = version in ("A", "B")
    plans, k = [], 0
    prev_ok = False
    for s in segs:
        if s["kind"] != "ok":
            prev_ok = False
            continue
        z, br = 1.0, None
        if version == "B":
            z = 1.0 if k % 2 == 0 else 1.25
        elif version in ("C", "D") and s["flags"].get("chute"):
            z = 1.3
        if version == "D" and s["flags"].get("broll"):
            br = s["flags"]["broll"]
        if serre or not prev_ok:
            t0 = s["t0"] - handle
        else:  # continuité de source avec le plan précédent
            t0 = plans[-1][1]
        plans.append([t0, s["t1"] + handle, z, br, s])
        prev_ok = True
        k += 1
    # fusionner les plans contigus sans changement de traitement
    fus = [plans[0]]
    for p in plans[1:]:
        q = fus[-1]
        if abs(p[0] - q[1]) < 1e-6 and p[2] == q[2] and p[3] == q[3] is None:
            q[1] = p[1]
        else:
            fus.append(p)
    return [tuple(p) for p in fus]


def evenements(plans, env=None, segs=None):
    """Événements visuels à chaque frontière de plan : jump (saut de temps,
    même cadre), echelle (punch-in / out), broll (entrée ou sortie)."""
    ev, t = [], 0.0
    for k, (t0, t1, z, br, s) in enumerate(plans):
        if k > 0:
            p = plans[k - 1]
            saut = abs(t0 - p[1]) > 1e-6
            if br or p[3]:
                typ = "broll"
            elif z != p[2]:
                typ = "echelle" + ("+saut" if saut else "")
            else:
                typ = "jump"
            item = {"t": round(t, 2), "type": typ}
            if env is not None and not (br or p[3]):
                ea = env[min(int(p[1] * FPS) - 1, len(env) - 1)]
                eb = env[min(int(t0 * FPS), len(env) - 1)]
                xa, ya, _ = pose((int(p[1] * FPS) - 1) / FPS, ea, segs)
                xb, yb, _ = pose(int(t0 * FPS) / FPS, eb, segs)
                # déplacement à l'écran, en % de la largeur de sortie (tient compte du zoom)
                item["depl_pct"] = round(100 * abs(xb * z - xa * p[2] + (W / 2) * (p[2] - z)) / W, 1)
                item["zoom"] = [p[2], z]
            ev.append(item)
        t += round((t1 - t0) * FPS) / FPS
    return ev, t


def rendre(version, plans, audio, env, segs, out):
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{OW}x{OH}",
           "-r", str(FPS), "-i", "-", "-i", os.path.join(out, f"{version}.wav"),
           "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest",
           os.path.join(out, f"{version}.mp4")]
    # audio monté
    a = np.concatenate([audio[int(max(0, t0) * SR):int(t1 * SR)] for t0, t1, *_ in plans])
    with wave.open(os.path.join(out, f"{version}.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((a * 32767).astype(np.int16).tobytes())
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for t0, t1, z, br, s in plans:
        n = int(round((t1 - t0) * FPS))
        for j in range(n):
            if br:
                img = broll_frame(br, j / FPS, n / FPS)
                fr = img.resize((OW, OH), Image.LANCZOS)
            else:
                fr = recadre(frame_brute(int(t0 * FPS) + j, env, segs), z)
            p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    versions = "A,B,A0,C,D"
    handle = 0.10
    if "--versions" in sys.argv:
        versions = sys.argv[sys.argv.index("--versions") + 1]
    global SWAY
    if "--sway" in sys.argv:
        SWAY = float(sys.argv[sys.argv.index("--sway") + 1])
    if "--handle" in sys.argv:
        handle = float(sys.argv[sys.argv.index("--handle") + 1])
    audio, segs = prise_brute(out)
    env = enveloppe(audio)
    with wave.open(os.path.join(out, "brut.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((audio * 32767).astype(np.int16).tobytes())
    json.dump(segs, open(os.path.join(out, "segments.json"), "w"), ensure_ascii=False, indent=1)
    for v in versions.split(","):
        plans = montage(v, segs, handle)
        ev, dur = evenements(plans, env, segs)
        stats = {"version": v, "duree_s": round(dur, 2), "brut_s": round(len(audio) / SR, 2),
                 "evenements": len(ev), "par_minute": round(len(ev) / dur * 60, 1),
                 "ecart_moyen_s": round(dur / (len(ev) + 1), 2), "detail": ev}
        json.dump(stats, open(os.path.join(out, f"{v}-events.json"), "w"), ensure_ascii=False, indent=1)
        rendre(v, plans, audio, env, segs, out)
        print(v, stats["duree_s"], "s", stats["evenements"], "év.", stats["par_minute"], "/min")


if __name__ == "__main__":
    main()
