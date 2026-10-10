"""Pièce 10 v6 : 8 s en deux temps — B4 tenu 4 s, C15 (le téléphone s'allume) 1,5 s, V1 (visage refroidi) 2,5 s.
Son : ton de pièce chaud (grave), une vibration de téléphone courte à 4,0 s, puis le ton de pièce baisse de 3 dB (le froid entre)."""
import subprocess
import numpy as np
import sys
R = "/home/user/Montagev2/atelier/rendus/10"; SR = 48000; G = sys.argv[1] if len(sys.argv) > 1 else "V1"; NOM = "v7" if G == "W1" else "v6"  # v7 : gros plan W1 (contre l ombre)
rng = np.random.default_rng(5); n = SR * 8
b = np.convolve(rng.standard_normal(n), np.ones(200) / 200, "same") * 0.05  # ton de pièce sourd
b[4 * SR:] *= 10 ** (-3 / 20)
t = np.arange(int(.35 * SR)) / SR; vib = .12 * np.sin(2 * np.pi * 170 * t) * (np.sin(2 * np.pi * 9 * t) > 0)
b[4 * SR:4 * SR + len(t)] += vib
b.astype(np.float32).tofile(f"{R}/v6.f32")
open(f"{R}/v6.txt", "w").write(f"ffconcat version 1.0\nfile B4/0001.png\nduration 4\nfile C15/0001.png\nduration 1.5\nfile {G}/0001.png\nduration 2.5\nfile {G}/0001.png\n")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-safe", "0", "-f", "concat", "-i", f"{R}/v6.txt", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", f"{R}/v6.f32",
                "-vf", "fps=25,format=yuv420p", "-t", "8", "-c:v", "libx264", "-c:a", "aac", f"{R}/{NOM}.mp4"], check=True)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{R}/{NOM}.mp4", "-vf", "select='not(mod(n\\,25))',scale=240:-1,drawtext=text='%{n}':x=4:y=4:fontsize=12:fontcolor=yellow,tile=4x2",
                "-frames:v", "1", f"{NOM}-montage-planche.png"], check=True)
