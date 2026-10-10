#!/usr/bin/env python3
"""Pièce 25 « Au lit » : une minute qui descend (A), qui reste plate (B),
ou dont les canaux se contredisent (C).
Usage : python3 piece.py OUTDIR [A,B,C]"""
import math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw

FPS, W, H, SR = 15, 640, 360, 22050
PHRASES = [
    "Il est tard.",
    "Pendant la nuit, votre cerveau ne s'éteint pas.",
    "Il trie.",
    "Ce qui compte est gardé, le reste est rangé plus loin.",
    "Toutes les quatre-vingt-dix minutes, un cycle recommence.",
    "D'abord léger.",
    "Puis profond.",
    "Puis le rêve.",
    "Vous n'avez rien à faire.",
    "Ça se fait tout seul.",
]


def courbe(version, x, chan):
    """x in [0,1] = avancement. Renvoie un facteur selon la version et le canal."""
    descente = {"lum": 1 - 0.6 * x, "vol": 10 ** (-10 * x / 20), "debit": 150 - 35 * x,
                "pause": 0.4 + 2.1 * x, "plan": 3 + 7 * x}
    moyen = {"lum": 0.7, "vol": 10 ** (-5 / 20), "debit": 132, "pause": 1.45, "plan": 6.0}
    if version in ("A", "D"):
        return descente[chan]
    if version == "B":
        return moyen[chan]
    # C : la voix et le montage descendent, l'image et le son restent au niveau de départ
    return descente[chan] if chan in ("debit", "pause", "plan") else {"lum": 1.0, "vol": 1.0}[chan]


def voix(version):
    parts = []
    n = len(PHRASES)
    for i, ph in enumerate(PHRASES):
        x = i / (n - 1)
        p = "/tmp/_v.wav"
        subprocess.run(["espeak-ng", "-v", "fr", "-s", str(int(courbe(version, x, "debit"))), "-p", "35",
                        "-w", p, ph], check=True)
        with wave.open(p) as w:
            sr = w.getframerate()
            a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
        t = np.linspace(0, len(a) / sr, int(len(a) * SR / sr), endpoint=False)
        a = np.interp(t, np.arange(len(a)) / sr, a)
        nz = np.where(np.abs(a) > 0.01)[0]
        a = a[nz[0]:nz[-1] + 1]
        parts.append(a * 0.35 * courbe(version, x, "vol"))
        parts.append(np.zeros(int(courbe(version, x, "pause") * SR)))
    v = np.concatenate([np.zeros(int(0.8 * SR))] + parts)
    return v


def nappe(n, version):
    t = np.arange(n) / SR
    x = t / t[-1]
    g = np.array([courbe(version, xx, "vol") for xx in x[::SR // 10]])
    g = np.interp(np.arange(n), np.arange(len(g)) * (SR // 10), g)
    pad = sum(np.sin(2 * np.pi * f * t + k) for k, f in enumerate([110, 164.8, 220, 277.2]))
    lfo = 0.75 + 0.25 * np.sin(2 * np.pi * 0.1 * t)
    return 0.03 * pad * lfo * g


def plan(kind, t, lum):
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    L = lambda c: tuple(int(v * lum) for v in c)
    if kind == 0:  # fenêtre sur la ville, lumières
        d.rectangle([0, 0, W, H], fill=L((20, 24, 40)))
        d.rectangle([160, 40, 480, 320], fill=L((35, 45, 80)))
        rng = np.random.default_rng(1)
        for k in range(40):
            x, y = rng.integers(180, 460), rng.integers(180, 300)
            on = (k * 7919 % 100) / 100 > t / 60
            d.rectangle([x, y, x + 6, y + 8], fill=L((240, 200, 120)) if on else L((40, 45, 70)))
        d.line([320, 40, 320, 320], fill=L((15, 15, 20)), width=8)
    elif kind == 1:  # lampe de chevet
        d.rectangle([0, 0, W, H], fill=L((30, 20, 14)))
        d.ellipse([240 - 120, 60 - 40, 400 + 120, 300], fill=L((70, 45, 25)))
        d.polygon([(270, 120), (370, 120), (400, 200), (240, 200)], fill=L((240, 210, 150)))
        d.rectangle([312, 200, 328, 290], fill=L((60, 50, 40)))
    elif kind == 2:  # tasse et vapeur
        d.rectangle([0, 0, W, H], fill=L((25, 22, 26)))
        d.rectangle([260, 200, 380, 300], fill=L((200, 195, 185)))
        for k in range(3):
            pts = [(290 + k * 30 + 10 * math.sin(y / 15 + t * 1.2 + k), y) for y in range(80, 195, 4)]
            d.line(pts, fill=L((90, 90, 100)), width=3)
    elif kind == 3:  # mer de nuit
        d.rectangle([0, 0, W, 170], fill=L((18, 22, 38)))
        d.rectangle([0, 170, W, H], fill=L((10, 14, 28)))
        for k in range(8):
            y = 190 + k * 20 + 3 * math.sin(t * 0.8 + k)
            d.line([0, y, W, y + 2 * math.sin(t + k)], fill=L((40, 50, 80)), width=2)
        d.ellipse([440, 60, 480, 100], fill=L((210, 210, 200)))
    else:  # étoiles
        d.rectangle([0, 0, W, H], fill=L((6, 8, 16)))
        rng = np.random.default_rng(3)
        for k in range(120):
            x, y = rng.integers(0, W), rng.integers(0, H)
            b = 0.6 + 0.4 * math.sin(t * 0.7 + k)
            d.point([(x + t * 2) % W, y], fill=L(tuple(int(220 * b) for _ in range(3))))
    return img


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for version in (sys.argv[2] if len(sys.argv) > 2 else "A,B,C").split(","):
        v = voix(version)
        dur = 60.0
        v = np.pad(v, (0, max(0, int(dur * SR) - len(v))))[:int(dur * SR)]
        a = v + nappe(len(v), version)
        with wave.open(f"{out}/{version}.wav", "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
            w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())
        # découpage : durée de plan selon la courbe
        cuts, t = [], 0.0
        while t < dur:
            cuts.append(t)
            t += courbe(version, t / dur, "plan")
        ordre = None
        if version == "D":
            # v2 : plans ordonnés par luminance propre (lampe, tasse, fenêtre, mer,
            # retour de la fenêtre presque éteinte, étoiles), durées croissantes
            cuts = [0, 5, 11, 19, 28, 40]
            ordre = [1, 2, 0, 3, 0, 4]
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                              "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", f"{out}/{version}.wav",
                              "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac",
                              "-shortest", f"{out}/{version}.mp4"], stdin=subprocess.PIPE)
        for f in range(int(dur * FPS)):
            tt = f / FPS
            k = max(i for i, c in enumerate(cuts) if c <= tt)
            kind = ordre[k] if ordre else k % 5
            p.stdin.write(plan(kind, tt, courbe(version, tt / dur, "lum")).tobytes())
        p.stdin.close(); p.wait()
        print(version, "coupes :", [round(c, 1) for c in cuts])


if __name__ == "__main__":
    main()
