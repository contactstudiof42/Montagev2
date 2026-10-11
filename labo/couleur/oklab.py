# Oklab / OkLCh depuis du Rec.709 encodé (gamma 2.4) et retour. Matrices de Björn Ottosson (primaires sRGB = Rec.709).
import numpy as np
M1 = np.array([[0.4122214708,0.5363325363,0.0514459929],[0.2119034982,0.6806995451,0.1073969566],[0.0883024619,0.2817188376,0.6299787005]])
M2 = np.array([[0.2104542553,0.7936177850,-0.0040720468],[1.9779984951,-2.4285922050,0.4505937099],[0.0259040371,0.7827717662,-0.8086757660]])
def vers_lch(rgb, g=2.4):
    lin = np.clip(rgb,0,1)**g; lms = np.cbrt(lin@M1.T); lab = lms@M2.T
    L, a, b = lab[...,0], lab[...,1], lab[...,2]
    return L, np.hypot(a,b), (np.degrees(np.arctan2(b,a)) % 360)
def depuis_lch(L, C, h, g=2.4):
    a, b = C*np.cos(np.radians(h)), C*np.sin(np.radians(h))
    lms = np.stack([L,a,b],-1)@np.linalg.inv(M2).T; lin = (lms**3)@np.linalg.inv(M1).T
    return np.clip(lin,0,1)**(1/g)
