"""Pièce 19 : python3 -I monte.py DOSSIER_PLANS SORTIE.mp4 PLANCHE.png plan1,plan2,...,plan8
Un vers par plan (21 images à 12 i/s = 1,75 s), texte incrusté en bas (Inter, OFL). Planche = image 14 de chaque plan."""
import sys, subprocess, os
d, out, planche, plans = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split(",")
VERS = ["J'ai gardé tes clés dans la poche de gauche", "Je marche au milieu pour que les voitures m'évitent",
        "Ma mère dit que je parle avec les mains", "Ce soir je les garde fermées",
        "Les vitrines me rendent un type que je connais pas", "Je lui fais signe, il me fait signe",
        "Personne attend en bas de chez moi", "J'allume quand même dans l'escalier"]
FONT = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
inp, filt = [], []
for k, p in enumerate(plans):
    inp += ["-framerate", "12", "-i", f"{d}/{p}/%04d.png"]
    t = VERS[k].replace("'", "’").replace(":", "\\:")
    filt.append(f"[{k}:v]drawtext=fontfile={FONT}:text='{t}':fontsize=15:fontcolor=white@0.92:x=(w-tw)/2:y=h-34:shadowcolor=black@0.6:shadowx=1:shadowy=1[v{k}]")
filt.append("".join(f"[v{k}]" for k in range(len(plans))) + f"concat=n={len(plans)}:v=1:a=0[o]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(filt), "-map", "[o]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", out], check=True)
sel = "+".join(f"eq(n\\,{21 * k + 13})" for k in range(len(plans)))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-vf", f"select='{sel}',scale=320:-1,tile=4x2", "-frames:v", "1", "-vsync", "0", planche], check=True)
print(out, planche, os.path.getsize(planche) // 1024, "Ko")
