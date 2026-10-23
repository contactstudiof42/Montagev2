# collisions_previz.py : cherche les traversées réelles (maillages) entre les personnages et les meubles de « L'Air ».
# blender -b FICHIER.blend -P collisions_previz.py -- [DEBUT_S] [FIN_S]
# Jusqu à 4 échantillons (0,3 s) de contact pendant une transition (s asseoir, se lever) sont tolérés ; une traversée qui dure, non.
import bpy, sys
from mathutils.bvhtree import BVHTree
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
t0, t1 = (float(args[0]), float(args[1])) if len(args) >= 2 else (0.0, 46.0)
sc = bpy.context.scene; O = bpy.data.objects
obst = [o for o in O if o.type == "MESH" and o.name.startswith(("CHAISE_", "TABLE_", "MUR_", "PORTE_battant"))]
corps = [o for o in O if o.type == "MESH" and o.name.startswith(("LUI_", "ELLE_")) and not o.name.startswith(("LUI_bouton", "LUI_nez", "ELLE_nez", "ELLE_chapelet", "ELLE_montre"))]
CONTACT = {("cuisse", "CHAISE"), ("jupe", "CHAISE")}     # être assis : la cuisse et la jupe touchent l'assise
def tree(o, dg):
    e = o.evaluated_get(dg); m = e.to_mesh(); m.transform(e.matrix_world)
    t = BVHTree.FromPolygons([v.co.copy() for v in m.vertices], [list(p.vertices) for p in m.polygons]); e.to_mesh_clear(); return t
hits = {}
for f in range(int(t0 * 24) + 1, int(t1 * 24) + 2, 2):
    sc.frame_set(f); dg = bpy.context.evaluated_depsgraph_get(); T = {o.name: tree(o, dg) for o in obst}
    for c in corps:
        tc = tree(c, dg)
        for n, t in T.items():
            if any(a in c.name and n.startswith(b) for a, b in CONTACT): continue
            if tc.overlap(t): hits.setdefault((c.name, n), []).append(round((f - 1) / 24, 2))
longues = 0
for (a, b), v in sorted(hits.items()):
    print("TRAVERSEE" if len(v) > 4 else "contact", a, b, v[0], "->", v[-1], f"{len(v)} échantillons")
    longues += len(v) > 4
print("TRAVERSEES_LONGUES", longues)
