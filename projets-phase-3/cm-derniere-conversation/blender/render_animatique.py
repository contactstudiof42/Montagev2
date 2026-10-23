# render_animatique.py : rend l'animatique de « L'Air » (0:00 à 0:47), une caméra par plan selon le découpage de montage.md.
# blender -b FICHIER.blend -P render_animatique.py -- DOSSIER_IMAGES [LARGEUR]
import bpy, sys, os
args = sys.argv[sys.argv.index("--") + 1:]; OUT = args[0]; WID = int(args[1]) if len(args) > 1 else 960
os.makedirs(OUT, exist_ok=True)
FPS = 24
def F(t): return int(round(t * FPS)) + 1
PLANS = [("1", "CAM_01_large", 0), ("2a", "CAM_ELLE", 5), ("2b", "CAM_LUI", 8), ("3", "CAM_LUI", 11), ("4a", "CAM_ELLE", 16),
         ("4b", "CAM_LUI", 19), ("5a", "CAM_ELLE", 22), ("5b", "CAM_LUI", 25), ("6", "CAM_06_deux", 28), ("7a", "CAM_07a_taille", 31),
         ("7b", "CAM_07b_en_pied", 34), ("8a", "CAM_08a_mains", 39), ("8b", "CAM_08b_profil", 41)]
sc = bpy.context.scene
sc.timeline_markers.clear()
for nom, cam, t0 in PLANS:
    m = sc.timeline_markers.new("P" + nom, frame=F(t0)); m.camera = bpy.data.objects[cam]
sc.frame_start, sc.frame_end = F(0), F(46) - 1
sc.render.resolution_x = WID; sc.render.resolution_y = WID * 9 // 16; sc.render.resolution_percentage = 100
sc.render.image_settings.file_format = "PNG"; sc.render.filepath = os.path.join(OUT, "f_")
try: sc.eevee.taa_render_samples = 16
except Exception: pass
bpy.ops.render.render(animation=True)
print("ANIMATIQUE_OK", sc.frame_start, sc.frame_end)
