# render_planche.py : rend les images de contrôle des plans de « L'Air » (début, milieu, fin de chaque plan).
# blender -b FICHIER.blend -P render_planche.py -- DOSSIER_SORTIE [mid|all] [LARGEUR]
import bpy, sys, os
args = sys.argv[sys.argv.index("--") + 1:]
OUT = args[0]; MODE = args[1] if len(args) > 1 else "mid"; WID = int(args[2]) if len(args) > 2 else 640
os.makedirs(OUT, exist_ok=True)
FPS = 24
def F(t): return int(round(t * FPS)) + 1
PLANS = [("01", "CAM_01_large", 0, 5), ("02a", "CAM_ELLE", 5, 8), ("02b", "CAM_LUI", 8, 11), ("03", "CAM_LUI", 11, 16),
         ("04a", "CAM_ELLE", 16, 19), ("04b", "CAM_LUI", 19, 22), ("05a", "CAM_ELLE", 22, 25), ("05b", "CAM_LUI", 25, 28),
         ("06", "CAM_06_deux", 28, 31), ("07a", "CAM_07a_taille", 31, 34), ("07b", "CAM_07b_en_pied", 34, 39),
         ("08a", "CAM_08a_mains", 39, 41), ("08b", "CAM_08b_profil", 41, 46)]
sc = bpy.context.scene
sc.render.resolution_x = WID; sc.render.resolution_y = WID * 9 // 16; sc.render.resolution_percentage = 100
sc.render.image_settings.file_format = "PNG"
try: sc.eevee.taa_render_samples = 16
except Exception: pass
for nom, cam, t0, t1 in PLANS:
    moments = {"mid": [("m", (t0 + t1) / 2)], "all": [("a", t0 + 0.05), ("m", (t0 + t1) / 2), ("z", t1 - 0.05)]}[MODE]
    sc.camera = bpy.data.objects[cam]
    for tag, t in moments:
        sc.frame_set(F(t)); sc.render.filepath = os.path.join(OUT, f"P{nom}_{tag}_{t:05.2f}s.png")
        bpy.ops.render.render(write_still=True)
print("PLANCHE_OK")
