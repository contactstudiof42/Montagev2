# mots.py SOURCE.wav DEBUT_s DUREE_s [sortie] : extrait un passage, transcrit au mot près (whisper -ml 1), imprime les mots avec leurs temps absolus
import sys, subprocess, os, re, tempfile
src, d0, dur = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
tmp = tempfile.mkdtemp(dir="/private/tmp/claude-501/-Volumes-SSD-FAST-Montage-IA/183e5f12-4475-4d09-96ab-ea6dd321e42f/scratchpad")
w = f"{tmp}/x.wav"; subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(d0), "-t", str(dur), "-i", src, "-ac", "1", "-ar", "16000", w])
subprocess.run(["whisper-cli", "-m", os.path.expanduser("~/.cache/whisper-cpp/ggml-large-v3-turbo.bin"), "-l", "fr", "-ml", "1", "-sow", "-osrt", "-of", f"{tmp}/x", "-f", w], capture_output=True)
out = []
for b in open(f"{tmp}/x.srt").read().strip().split("\n\n"):
    L = [l for l in b.split("\n") if l.strip()]
    if len(L) < 3 or " --> " not in L[1]: continue
    def s(t): h, m, r = t.split(":"); return int(h)*3600 + int(m)*60 + float(r.replace(",", "."))
    a, z = L[1].split(" --> "); out.append(f"{d0 + s(a):.2f}-{d0 + s(z):.2f} {' '.join(L[2:]).strip()}")
print("\n".join(out))
