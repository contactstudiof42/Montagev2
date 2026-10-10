#!/usr/bin/env python3
"""Pulsations qui tombent sur des images entières (Y45). Pour chaque cadence : les BPM entiers de 60 à 180 dont la noire
dure un nombre entier d'images, et la dérive (en images, après 8 mesures de 4 temps) des tempos courants.
usage : tempos.py [bpm ...]"""
import sys
from fractions import Fraction as F
CAD = {'23,976': F(24000, 1001), '24': F(24), '25': F(25), '29,97': F(30000, 1001), '30': F(30), '50': F(50)}
courants = [int(x) for x in sys.argv[1:]] or [90, 100, 120, 128, 140, 48]   # 48 BPM = un tic de 1,25 s
for nom, fps in CAD.items():
    entiers = [b for b in range(60, 181) if (60 * fps / b).denominator == 1]
    print(f'{nom:>6} i/s : BPM entiers à noire = images entières : {entiers}')
    for b in courants:
        p = 60 * fps / b                                       # images par temps (exact)
        derive = max(abs(round(k * p) - k * p) for k in range(33))   # erreur d'arrondi max sur 32 temps
        cum = 32 * (p - round(p))                              # dérive si on coupe tous les round(p) images
        print(f'         {b:>3} BPM : {float(p):7.3f} images/temps ; arrondi par temps ±{float(derive):.2f} im ; '
              f'si l\'on coupe toutes les {round(p)} images, dérive de {float(cum):+.1f} im en 8 mesures')
