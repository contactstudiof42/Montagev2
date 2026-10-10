"""Monte une version de la pièce 07 depuis une EDL (même temps pour toutes les caméras : la simulation est unique).
EDL : {"nom": "B", "plans": [["livre", 1, 41], ["dominos", 41, 63], ...]}  (image de début incluse, de fin exclue)
Usage : python3 montage.py edl.json dossier_rendus son.wav sortie_dir
Écrit : <nom>.mp4, <nom>-planche.png (1 vignette / 4 images, coupes encadrées), <nom>-mesures.json (distance coupe-contact)."""
import json, sys, os, subprocess
E = json.load(open(sys.argv[1])); R = sys.argv[2]; son = sys.argv[3]; out = sys.argv[4]; os.makedirs(out, exist_ok=True)
ev = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "evenements.json")))
contacts = sorted(v for k, v in ev.items() if (k.endswith("_bouge") or k == "tasse_sol") and isinstance(v, int))
nom = E["nom"]; lst = os.path.join(out, nom + ".txt"); frames = []
with open(lst, "w") as f:
    for cam, a, b in E["plans"]:
        for i in range(a, b):
            p = os.path.join(R, cam, "%04d.png" % i); assert os.path.exists(p), p
            f.write("file '%s'\nduration 0.04\n" % p); frames.append((cam, i))
    f.write("file '%s'\n" % p)
vid = os.path.join(out, nom + ".mp4")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", son,
                "-vf", "fps=25,format=yuv420p", "-c:v", "libx264", "-crf", "18", "-c:a", "aac", "-shortest", vid], check=True)
coupes = [a for _, a, _ in E["plans"][1:]]
dist = {c: min(abs(c - k) for k in contacts) for c in coupes}
# contact visible ? (l'objet du contact est-il dans le plan qui le contient : noté à la main dans l'EDL si besoin)
json.dump({"coupes": coupes, "contacts": contacts, "distance_min_coupe_contact": dist}, open(os.path.join(out, nom + "-mesures.json"), "w"), indent=1)
# Planche : 1 vignette toutes les 4 images + toute 1re image de plan, numéro d'image incrusté, bord rouge aux coupes
sel = [k for k, (cam, i) in enumerate(frames) if i % 4 == 1 or i in coupes]
f = "+".join("eq(n\\,%d)" % k for k in sel)
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", vid, "-vf",
                "drawtext=text='%%{eif\\:n+1\\:d}':x=4:y=4:fontsize=28:fontcolor=yellow,select='%s',scale=240:-1,tile=6x%d" % (f, (len(sel) + 5) // 6),
                "-frames:v", "1", "-vsync", "0", os.path.join(out, nom + "-planche.png")], check=True)
print(nom, "coupes", coupes, "distance coupe-contact", dist)
