# render_decors.py : rend la pièce vide de « L'Air » (sans personnages), une image par caméra, au début de son premier plan, pour les décors GPT.
# Plus une image du 7b porte ouverte (le couloir cyan). blender -b FICHIER.blend -P render_decors.py -- DOSSIER_SORTIE [LARGEUR]
import bpy, sys, os
args = sys.argv[sys.argv.index("--") + 1:]; OUT = args[0]; WID = int(args[1]) if len(args) > 1 else 1920
os.makedirs(OUT, exist_ok=True)
FPS = 24
def F(t): return int(round(t * FPS)) + 1
CAMS = [("01", "CAM_01_large", 0), ("02a", "CAM_ELLE", 5), ("02b", "CAM_LUI", 8), ("06", "CAM_06_deux", 28), ("07a", "CAM_07a_taille", 31),
        ("07b", "CAM_07b_en_pied", 34), ("08a", "CAM_08a_mains", 39), ("08b", "CAM_08b_profil", 41)]
sc = bpy.context.scene
for c in ("LUI", "ELLE"):                     # les personnages, entraves comprises, sont exclus du calque (hide_render seul ne suffit pas)
    bpy.context.view_layer.layer_collection.children[c].exclude = True
sc.render.resolution_x = WID; sc.render.resolution_y = WID * 9 // 16; sc.render.resolution_percentage = 100
sc.render.image_settings.file_format = "PNG"
try: sc.eevee.taa_render_samples = 64
except Exception: pass
def rendre(nom, cam, frame):
    sc.camera = bpy.data.objects[cam]; sc.frame_set(frame)
    sc.render.filepath = os.path.join(OUT, f"decor_P{nom}_{cam}.png"); bpy.ops.render.render(write_still=True)
for nom, cam, t0 in CAMS: rendre(nom, cam, F(t0 + 0.05))
# 7b porte ouverte : l'image du plan où le battant est le plus ouvert
h = bpy.data.objects["PORTE_charniere"]
best = max(range(F(34), F(39)), key=lambda f: (sc.frame_set(f), abs(h.matrix_world.to_euler().z))[1])
rendre("07b_porte_ouverte", "CAM_07b_en_pied", best)
print("DECORS_OK porte_ouverte_image", best)
