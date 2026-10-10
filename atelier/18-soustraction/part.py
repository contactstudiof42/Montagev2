"""Part de chaque lampadaire dans la lumière du cadre (pièce 18 v3) : python3 -I part.py <dossier>
Chaque source rendue seule (seul0..6.png, ambre et fenêtres éteintes) ; on soustrait le rendu sans aucune source
(ciel seul) et on rapporte la luminance moyenne ajoutée par chacune. Équivalent plateau : allumer les sources une par une."""
import sys
import numpy as np
from PIL import Image
d = sys.argv[1]
def lum(n):
    a = np.asarray(Image.open(f"{d}/{n}.png").convert("RGB")).astype(float)
    return (0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]).mean()
base = lum("seul_aucun"); parts = [max(0.0, lum(f"seul{i}") - base) for i in range(7)]; tot = sum(parts)
for i, p in enumerate(parts): print(f"lampadaire {i} (y = {6 + 9 * i} m) : +{p:.1f} de luminance, {100 * p / tot:.0f} %")
print(f"fond sans source : {base:.1f}")
