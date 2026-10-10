#!/usr/bin/env python3
"""Labo marqueurs (session 4) : détecter les temps d'une musique et les écrire en marqueurs importables.
Sortie 1 : XML FCP7 (xmeml v4) — une séquence vide avec un marqueur par temps (les mesures ont un nom « M<n> »).
           Premiere (Fichier > Importer) et Resolve (Import Timeline > XML) lisent ce format : import à vérifier en phase 2.
Sortie 2 : CSV (temps en s, timecode, nom) pour contrôle humain.
Détection : enveloppe d'énergie (fenêtre 1024, saut 256) → flux spectral positif → tempo par autocorrélation
            → phase choisie pour maximiser l'énergie sur la grille. Grille régulière (pas de tempo variable).
Usage : python3 beats_xml.py musique.wav sortie_base [fps=25] [temps_par_mesure=4]"""
import csv, subprocess, sys
import numpy as np
from xml.sax.saxutils import escape
wav, base = sys.argv[1], sys.argv[2]
FPS = int(sys.argv[3]) if len(sys.argv) > 3 else 25
TPM = int(sys.argv[4]) if len(sys.argv) > 4 else 4
SR, HOP, WIN = 22050, 256, 1024
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", wav, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True, check=True).stdout, np.float32)
n = 1 + (len(x) - WIN) // HOP
S = np.abs(np.fft.rfft(np.stack([x[i * HOP:i * HOP + WIN] * np.hanning(WIN) for i in range(n)]), axis=1))
flux = np.maximum(np.diff(np.log1p(S), axis=0), 0).sum(axis=1); flux -= flux.mean()
# flux grave (< 200 Hz) pour la phase : sinon le charleston, plus riche en aigus, gagne et la grille tombe à contretemps
graves = np.fft.rfftfreq(WIN, 1 / SR) < 200
flux_g = np.maximum(np.diff(np.log1p(S[:, graves]), axis=0), 0).sum(axis=1)
T0 = (HOP + WIN / 2) / SR                                   # trame d'enveloppe i ≈ instant (i+1)·HOP + WIN/2
fr = SR / HOP                                               # trames d'enveloppe par seconde
ac = np.correlate(flux, flux, "full")[len(flux) - 1:]
lags = np.arange(len(ac)); bpm = 60 * fr / np.maximum(lags, 1)
ok = (bpm >= 70) & (bpm <= 180)                             # plage de tempo plausible
lag = lags[ok][np.argmax(ac[ok])]
# affinage sub-trame : parabole autour du pic
y0, y1, y2 = ac[lag - 1], ac[lag], ac[lag + 1]; lag_f = lag + 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
periode = lag_f / fr; BPM = 60 / periode
phases = np.linspace(0, periode, 64, endpoint=False)
def score(p): return sum(flux_g[int(round((p + k * periode) * fr))] for k in range(int((len(flux_g) / fr - p) / periode)))
p0 = (phases[np.argmax([score(p) for p in phases])] + T0) % periode
temps = np.arange(p0, len(x) / SR, periode)
# affinage : chaque temps est recalé sur le pic grave le plus proche (±40 ms), puis régression linéaire → période et phase
pics = []
for k, s in enumerate(temps):
    i = int(round((s - T0) * fr)); a, b = max(0, i - int(0.04 * fr)), min(len(flux_g), i + int(0.04 * fr) + 1)
    if b > a and flux_g[a:b].max() > 0: pics.append((k, (a + np.argmax(flux_g[a:b])) / fr + T0))
if len(pics) >= 8:
    kk, tt = np.array(pics).T; periode, p0 = np.polyfit(kk, tt, 1); BPM = 60 / periode
    temps = p0 + periode * np.arange(int((len(x) / SR - p0) / periode) + 1)
# premier temps de mesure : le décalage (0..TPM-1) dont les temps portent le plus d'énergie (accent), pas forcément le 1er temps
def energie(s):
    i = int(round((s - T0) * fr)); return flux[max(0, i - 2):i + 3].max() if 0 <= i < len(flux) else 0.0
acc = [sum(energie(s) for s in temps[o::TPM]) / max(1, len(temps[o::TPM])) for o in range(TPM)]
DEC = int(np.argmax(acc)); srt = sorted(acc)
AMBIGU = srt[-1] < 1.15 * srt[-2]   # pas d'accent net : M1 arbitraire, à vérifier à l'oreille
def tc(s):
    f = int(round(s * FPS)); return f"{f // (3600 * FPS):02d}:{f // (60 * FPS) % 60:02d}:{f // FPS % 60:02d}:{f % FPS:02d}"
with open(base + ".csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["temps_s", "timecode", "image", "nom"])
    for k, s in enumerate(temps):
        w.writerow([f"{s:.3f}", tc(s), int(round(s * FPS)), f"M{(k - DEC) // TPM + 1}" if (k - DEC) % TPM == 0 else f"t{(k - DEC) % TPM + 1}"])
dur = int(round(len(x) / SR * FPS))
mk = "".join(f"<marker><name>{escape('M%d' % ((k - DEC) // TPM + 1) if (k - DEC) % TPM == 0 else '')}</name><comment>{BPM:.2f} BPM</comment>"
             f"<in>{int(round(s * FPS))}</in><out>-1</out></marker>" for k, s in enumerate(temps))
xml = (f'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n<xmeml version="4"><sequence id="beats">'
       f"<name>Temps {BPM:.1f} BPM</name><duration>{dur}</duration><rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate>"
       f"<timecode><rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate><string>00:00:00:00</string><frame>0</frame>"
       f"<displayformat>NDF</displayformat></timecode>{mk}<media><video><track/></video><audio><track/></audio></media>"
       f"</sequence></xmeml>\n")
open(base + ".xml", "w").write(xml)
print(f"BPM={BPM:.2f} phase={p0:.3f}s temps={len(temps)} 1er_temps_de_mesure=temps n°{DEC + 1}" + (" (ACCENT AMBIGU : vérifier M1 à l'oreille)" if AMBIGU else ""))
