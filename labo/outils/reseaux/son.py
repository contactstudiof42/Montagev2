# son.py DOSSIER "frames des coupes vues" : coupes.json vérifié (coupes_oeil.json), spectrogramme mix + musique + voix avec coupes,
# calage contre le hasard (attaques fortes de la musique séparée), tempo.
import sys, json, subprocess, numpy as np, librosa
from PIL import Image, ImageDraw
D = sys.argv[1]; fr_list = [int(x) for x in sys.argv[2].split()]
r = subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=r_frame_rate","-of","default=nw=1:nk=1",f"{D}/proxy.mp4"],capture_output=True,text=True).stdout.strip().split("/")
fps = float(r[0]) / float(r[1]); cuts = np.array(fr_list) / fps
json.dump({"coupes": cuts.tolist(), "fps": fps}, open(f"{D}/coupes_oeil.json", "w"))
sr = 22050; hop = 256
def charge(f): return librosa.load(f, sr=sr, mono=True)[0]
mix = charge(f"{D}/audio.wav"); mus = charge(f"{D}/sep/htdemucs/audio/no_vocals.wav"); voc = charge(f"{D}/sep/htdemucs/audio/vocals.wav")
L = len(mix) / sr
env = librosa.onset.onset_strength(y=mus, sr=sr, hop_length=hop)
tempo, beats = librosa.beat.beat_track(onset_envelope=env, sr=sr, hop_length=hop, units="time")
pk = librosa.util.peak_pick(env, pre_max=3, post_max=3, pre_avg=10, post_avg=10, delta=0, wait=4)
for pc in (90, 75):
    f = librosa.frames_to_time(pk[env[pk] >= np.percentile(env, pc)], sr=sr, hop_length=hop)
    c = cuts[(cuts > 0.3) & (cuts < L - 0.3)]
    for tol_i in (1, 2):
        tol = tol_i / fps
        part = lambda cs, ref: float(np.mean([np.min(np.abs(ref - x)) <= tol for x in cs]))
        rng = np.random.default_rng(0)
        h = [part(np.mod(c + rng.uniform(0, L), L), f) for _ in range(2000)]
        hb = [part(np.mod(c + rng.uniform(0, L), L), beats) for _ in range(2000)]
        print(f"attaques>{pc}e ({len(f)}) ±{tol_i}i : {part(c,f):.0%} (hasard {np.mean(h):.0%}, 95e {np.percentile(h,95):.0%}) | temps : {part(c,beats):.0%} (hasard {np.mean(hb):.0%}, 95e {np.percentile(hb,95):.0%})")
print(f"{len(cuts)} coupes, tempo {float(np.atleast_1d(tempo)[0]):.0f} BPM, durée {L:.1f} s, plans médiane {np.median(np.diff(np.r_[0,cuts,L])):.2f} s")
# spectrogrammes
Wpx = 2000; rows = []
for y, nom in ((mix, "mix"), (mus, "musique"), (voc, "voix")):
    S = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=1024, hop_length=hop)), ref=np.max)
    S = S[:300][::-1]; S = np.clip((S + 70) / 70, 0, 1)
    im = Image.fromarray((S * 255).astype(np.uint8)).resize((Wpx, 140)).convert("RGB")
    dr = ImageDraw.Draw(im); dr.text((3, 2), nom, fill=(255, 255, 0))
    for t in cuts: x = int(t / L * Wpx); dr.line([(x, 0), (x, 14)], fill=(255, 0, 0)); dr.line([(x, 126), (x, 140)], fill=(255, 0, 0))
    for t in beats: x = int(t / L * Wpx); dr.line([(x, 60), (x, 64)], fill=(0, 255, 255))
    rows.append(im)
o = librosa.frames_to_time(np.arange(len(env)), sr=sr, hop_length=hop)
g = Image.new("RGB", (Wpx, 60)); dr = ImageDraw.Draw(g); e = env / env.max()
for i in range(len(env)): x = int(o[i] / L * Wpx); dr.line([(x, 60), (x, 60 - int(55 * e[i]))], fill=(230, 200, 0))
for t in cuts: x = int(t / L * Wpx); dr.line([(x, 0), (x, 8)], fill=(255, 0, 0))
for s in range(int(L) + 1): x = int(s / L * Wpx); dr.text((x + 1, 10), str(s), fill=(255, 255, 255)); dr.line([(x, 0), (x, 60)], fill=(80, 80, 80))
rows.append(g)
out = Image.new("RGB", (Wpx, sum(i.height for i in rows))); y0 = 0
for i in rows: out.paste(i, (0, y0)); y0 += i.height
out.save(f"{D}/son.png"); print(f"{D}/son.png")
