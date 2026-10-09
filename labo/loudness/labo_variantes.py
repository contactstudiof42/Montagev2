#!/usr/bin/env python3
"""Variantes de la 2e passe loudnorm, pour comprendre les écarts vus dans labo_loudness.py :
  A. linear=true AVEC offset=target_offset (recette « classique » des tutos)
  B. linear=true SANS offset
  C. linear=true avec LRA cible >= LRA mesuré (évite le repli en mode dynamique)
  D. comme C mais TP=-1.5 (marge de sécurité true peak)
Réutilise les WAV générés par labo_loudness.py (à lancer avant).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from labo_loudness import RENDUS, FF, run, mesure_ebur128, mesure_loudnorm, loudnorm_json  # noqa

CAS = [("calme", -23), ("large", -23), ("calme", -14), ("large", -14)]


def passe2(src, dst, I, TP, LRA, m, offset=True):
    af = (f"loudnorm=I={I}:TP={TP}:LRA={LRA}:measured_I={m['input_i']}:measured_TP={m['input_tp']}"
          f":measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}"
          + (f":offset={m['target_offset']}" if offset else "") + ":linear=true:print_format=json")
    err, dt = run(FF + ["-i", str(src), "-af", af, "-ar", "48000", "-c:a", "pcm_s24le", str(dst)])
    return loudnorm_json(err), dt, af


for nom, I in CAS:
    src = RENDUS / f"signal_{'test' if nom == 'large' else 'calme'}.wav"
    LRA0 = 20 if I == -23 else 11
    m, _, _ = mesure_loudnorm(src, I, -1, LRA0)
    lra_haut = min(50, max(LRA0, float(m["input_lra"]) + 1))
    variantes = [
        ("A offset", -1, LRA0, True),
        ("B sans offset", -1, LRA0, False),
        (f"C LRA={lra_haut:g} sans offset", -1, lra_haut, False),
        (f"D LRA={lra_haut:g} TP=-1.5", -1.5, lra_haut, False),
    ]
    print(f"\n{nom} -> {I} LUFS | passe 1 : input_i={m['input_i']} input_tp={m['input_tp']} "
          f"input_lra={m['input_lra']} target_offset={m['target_offset']}")
    for lab, TP, LRA, off in variantes:
        dst = RENDUS / f"var_{nom}_{abs(I)}_{lab[0]}.wav"
        j, dt, af = passe2(src, dst, I, TP, LRA, m, off)
        r, _ = mesure_ebur128(dst)
        print(f"  {lab:24s} type={j['normalization_type']:8s} I={r['I']:6.1f} (ecart {r['I'] - I:+.1f}) "
              f"TP={r['TP']:5.1f} LRA={r['LRA']:5.1f}  t={dt:.2f}s")
