"""Vérité terrain « tête qui bouge, fond fixe » : fond = image Blender ; « tête » = disque texturé collé, déplacé de dx % entre avant et après.
Question : la mesure globale voit-elle le saut de la tête ? et la mesure par zone ?"""
import sys, numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, '.'); from micro_sauts import mesurer
fond = Image.open(sys.argv[1]).convert('RGB').resize((1280, 540)); W, H = fond.size; rng = np.random.default_rng(2)
if 'fondtexture' in sys.argv:                        # fond très texturé (bibliothèque, feuillage) : il domine la corrélation globale
    fond = Image.fromarray((rng.random((135, 320, 3)) * 255).astype(np.uint8)).resize((W, H), Image.NEAREST)
tex = Image.fromarray((rng.random((160, 160, 3)) * 120 + 90).astype(np.uint8)).resize((220, 220))   # « visage » texturé
masque = Image.new('L', (220, 220), 0); ImageDraw.Draw(masque).ellipse((0, 0, 219, 219), fill=255)
def compo(dx):
    im = fond.copy(); im.paste(tex, (int(W * 0.45 + dx / 100 * W), 150), masque); return im
zone = (0.35, 0.18, 0.35, 0.62)                      # boîte autour de la tête (marge pour le déplacement)
print('dx tête %  | global | zone visage')
for dx in (0.0, 0.5, 1.0, 2.0, 4.0):
    av, ap = compo(0), compo(dx)
    g, z = mesurer(av, ap), mesurer(av, ap, zone)
    print(dx, '|', g['dx_pct'], g['pic'], '|', round(z['dx_pct'] * zone[2], 2), z['pic'])   # zone : ramené en % de la largeur totale
