#!/usr/bin/env python3
"""Labo downmix surround (BACKLOG 34) : 5.1 synthétique -> Lo/Ro, Lt/Rt pan, Lt/Rt Hilbert (scipy et ffmpeg afir).
Usage : python3 labo/surround/labo_surround.py   (depuis la racine du dépôt)
Rendus wav dans labo/rendus/surround/ (ignoré par git). Résultats : labo/surround/resultats.json
Dépendances : ffmpeg 6.1.1, numpy, scipy.
"""
import json, os, re, subprocess
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR, DUR = 48000, 10.0
N = int(SR * DUR)
OUT = os.path.join("labo", "rendus", "surround")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(42)

def db(x): return 20 * np.log10(x)
def rms(x): return np.sqrt(np.mean(x ** 2))

def pink(seed):
    r = np.random.default_rng(seed)
    X = np.fft.rfft(r.standard_normal(N))
    f = np.fft.rfftfreq(N, 1 / SR); f[0] = f[1]
    x = np.fft.irfft(X / np.sqrt(f), N)
    return x / rms(x)

def band(x, lo, hi, order=4):
    if lo is None: sos = signal.butter(order, hi, "lowpass", fs=SR, output="sos")
    elif hi is None: sos = signal.butter(order, lo, "highpass", fs=SR, output="sos")
    else: sos = signal.butter(order, [lo, hi], "bandpass", fs=SR, output="sos")
    return signal.sosfilt(sos, x)

t = np.arange(N) / SR
# --- Dialogue : bruit rose 300-3000 Hz, enveloppe syllabique (~4,5 syll/s), phrases de 2 s séparées de 0,6 s
dia = band(pink(1), 300, 3000)
syl = np.clip(np.sin(2 * np.pi * 4.5 * t + 0.8 * np.sin(2 * np.pi * 0.7 * t)), 0, None) ** 1.5
phrase = ((t % 2.6) < 2.0).astype(float)
phrase = np.convolve(phrase, np.hanning(960) / np.hanning(960).sum(), "same")
dia = dia * syl * phrase
dia *= 10 ** (-25 / 20) / rms(dia[phrase > 0.5])          # ~ -25 dBFS RMS pendant la parole
# --- Musique : accords sinus (Am, F, C, G), voicings différents L/R
chords = [[220, 261.63, 329.63], [174.61, 220, 261.63], [261.63, 329.63, 392], [196, 246.94, 293.66]]
def music(detune, phase):
    m = np.zeros(N)
    for i, ch in enumerate(chords):
        seg = (t >= i * 2.5) & (t < (i + 1) * 2.5)
        env = np.minimum(1, np.minimum((t - i * 2.5) / 0.05, ((i + 1) * 2.5 - t) / 0.3)).clip(0)
        for k, f0 in enumerate(ch):
            m += seg * env * np.sin(2 * np.pi * f0 * detune * t + phase * k) * (1 if k else 0.8)
    return m
musL = music(1.0, 0.0); musR = 0.6 * musL + 0.8 * music(1.002, 1.3)   # stéréo partiellement corrélée
g = 10 ** (-31 / 20) / rms(musL); musL *= g; musR *= g      # musique ~ -31 dBFS RMS par canal (6 dB sous le dialogue)
# --- Ambiance : bruit rose doux décorrélé, passe-bas 8 kHz ; -12 dB sous la musique du front
ambL, ambR = band(pink(11), None, 8000, 2), band(pink(12), None, 8000, 2)
ga = 10 ** (-43 / 20)
ambL, ambR = ambL / rms(ambL) * ga, ambR / rms(ambR) * ga
ambM = band(pink(13), None, 8000, 2); ambM = ambM / rms(ambM) * ga   # variante corrélée (même signal Ls=Rs)
# --- LFE : bruit + sinus 45 Hz, < 120 Hz
lfe = band(band(pink(21), None, 120, 8) + 0.0, 30, None, 2)
lfe = lfe / rms(lfe) * 0.5 + 0.5 * np.sin(2 * np.pi * 45 * t)
lfe *= 10 ** (-29 / 20) / rms(lfe)

Z = np.zeros(N)
stems = {   # ordre ffmpeg 5.1 : FL FR FC LFE BL BR
    "full":     [musL, musR, dia, lfe, ambL, ambR],
    "dia":      [Z, Z, dia, Z, Z, Z],
    "mus":      [musL, musR, Z, Z, Z, Z],
    "amb":      [Z, Z, Z, Z, ambL, ambR],
    "amb_corr": [Z, Z, Z, Z, ambM, ambM],
    "lfe":      [Z, Z, Z, lfe, Z, Z],
    # ambiance enveloppante : le MÊME signal à l'avant et à l'arrière (réverbe/room tone étalé sur 4 canaux)
    "amb_wrap": [ambM, ambM, Z, Z, ambM, ambM],
}
def write51(name, chs):
    tmp = os.path.join(OUT, f"_{name}_f32.wav")
    wavfile.write(tmp, SR, np.stack(chs, 1).astype(np.float32))
    dst = os.path.join(OUT, f"{name}_51.wav")
    run(["ffmpeg", "-y", "-v", "error", "-i", tmp, "-af", "aformat=channel_layouts=5.1",
         "-c:a", "pcm_s24le", dst]); os.remove(tmp); return dst

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, check=True)

def read(path):
    sr, x = wavfile.read(path)
    if x.dtype == np.int32: x = x / 2 ** 31
    return x.astype(np.float64)

# --- Downmixes ffmpeg pan
PAN = {
    "loro": "pan=stereo|FL=FL+0.7071*FC+0.7071*BL|FR=FR+0.7071*FC+0.7071*BR",
    "ltrt_pan": "pan=stereo|FL=FL+0.7071*FC-0.5*BL-0.5*BR|FR=FR+0.7071*FC+0.5*BL+0.5*BR",
}
# --- Hilbert ffmpeg : FIR de Hilbert (type III, 2047 taps, fenêtre de Blackman) appliqué à S,
#     fronts retardés de (taps-1)/2 = 1023 échantillons pour rester alignés.
TAPS = 2047; D = (TAPS - 1) // 2
n = np.arange(TAPS) - D
h = np.where(n % 2 != 0, 2 / (np.pi * np.where(n == 0, 1, n)), 0.0) * np.blackman(TAPS)
IR = os.path.join(OUT, "hilbert_ir_2047.wav")
wavfile.write(IR, SR, h.astype(np.float32))
FF_HILB = (
    "[0:a]asplit=2[a][b];"
    "[a]pan=stereo|c0=FL+0.7071*FC|c1=FR+0.7071*FC,adelay=delays=%dS:all=1[fr];"
    "[b]pan=mono|c0=0.5*BL+0.5*BR[s];[s][1:a]afir=gtype=none:irgain=1:dry=1:wet=1[hs];"
    "[hs]asplit=2[h1][h2];[h1]pan=mono|c0=-1*c0[hn];"
    "[fr]channelsplit=channel_layout=stereo[fl][frr];"
    "[fl][hn]amix=inputs=2:normalize=0[lt];[frr][h2]amix=inputs=2:normalize=0[rt];"
    "[lt][rt]join=inputs=2:channel_layout=stereo[out]" % D
)

def downmixes(name, src):
    outs = {}
    for k, af in PAN.items():
        dst = os.path.join(OUT, f"{name}_{k}.wav")
        run(["ffmpeg", "-y", "-v", "error", "-i", src, "-af", af, "-c:a", "pcm_s24le", dst]); outs[k] = dst
    # Hilbert scipy (non causal, FFT) : Lt = L+.707C - j*S ; Rt = R+.707C + j*S, S = 0.5(Ls+Rs) ~ -3 dB sur la somme
    x = read(src); L, R, C, _, Ls, Rs = x.T
    S = 0.5 * (Ls + Rs); jS = np.imag(signal.hilbert(S))
    st = np.stack([L + 0.7071 * C - jS, R + 0.7071 * C + jS], 1)
    dst = os.path.join(OUT, f"{name}_ltrt_hilb_py.wav")
    wavfile.write(dst, SR, st.astype(np.float32)); outs["ltrt_hilb_py"] = dst
    dst = os.path.join(OUT, f"{name}_ltrt_hilb_ff.wav")
    run(["ffmpeg", "-y", "-v", "error", "-i", src, "-i", IR, "-filter_complex", FF_HILB, "-map", "[out]",
         "-c:a", "pcm_s24le", dst]); outs["ltrt_hilb_ff"] = dst
    return outs

def ebur(path, mono=False):
    af = ("pan=mono|c0=0.5*c0+0.5*c1," if mono else "") + "ebur128=peak=true"
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", af, "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    summ = r[r.rfind("Summary:"):]
    I = float(re.search(r"I:\s+(-?[\d.]+|-inf)", summ).group(1))
    tp = re.search(r"Peak:\s+(-?[\d.]+|-inf)", summ)
    return I, (float(tp.group(1)) if tp else None)

def corr(path):
    x = read(path)
    if x.ndim < 2: return None
    a, b = x[:, 0], x[:, 1]
    d = np.sqrt(np.sum(a * a) * np.sum(b * b))
    return float(np.sum(a * b) / d) if d > 0 else None

res = {}
for name, chs in stems.items():
    src = write51(name, chs)
    I, tp = ebur(src)
    res[name] = {"5.1": {"I": I, "TP": tp}}
    for k, p in downmixes(name, src).items():
        Is, tps = ebur(p); Im, tpm = ebur(p, mono=True)
        res[name][k] = {"I": Is, "TP": tps, "I_mono": Im, "TP_mono": tpm, "corr": corr(p)}

# Écart Hilbert scipy vs ffmpeg afir (null test, hors bords)
a = read(os.path.join(OUT, "full_ltrt_hilb_py.wav")); b = read(os.path.join(OUT, "full_ltrt_hilb_ff.wav"))
b = b[D:D + len(a)]   # afir retarde S de D échantillons, adelay retarde les fronts d'autant
m = min(len(a), len(b)); seg = slice(SR // 2, m - SR // 2)
res["null_py_vs_ff_dB"] = float(db(rms(a[seg] - b[seg]) / rms(a[seg])))
hp = signal.butter(8, 50, "highpass", fs=SR, output="sos")
A, B = signal.sosfiltfilt(hp, a[:m], axis=0), signal.sosfiltfilt(hp, b[:m], axis=0)
res["null_py_vs_ff_dB_above50Hz"] = float(db(rms(A[seg] - B[seg]) / rms(A[seg])))
# Corrélation par canal Lt, Rt pour amb_wrap (pan simple : Lt s'annule)
for k in ["ltrt_pan", "ltrt_hilb_py"]:
    x = read(os.path.join(OUT, f"amb_wrap_{k}.wav")); res[f"amb_wrap_{k}_rms_Lt_Rt_dBFS"] = [float(db(rms(x[:, 0]) + 1e-12)), float(db(rms(x[:, 1])))]
# Contrôle du déphasage : corrélation entre S et H(S) (doit être ~0) et gain du FIR à 100 Hz / 1 kHz / 15 kHz
w, H = signal.freqz(h, worN=[100, 1000, 15000], fs=SR)
res["fir_gain_dB_100_1k_15k"] = [float(v) for v in db(np.abs(H))]
json.dump(res, open(os.path.join("labo", "surround", "resultats.json"), "w"), indent=1, ensure_ascii=False)

print(f"{'stem':9} {'version':13} {'I st':>7} {'TP st':>7} {'I mono':>7} {'TP mono':>7} {'corr':>6}")
for name in stems:
    r = res[name]; print(f"{name:9} {'5.1':13} {r['5.1']['I']:7.1f} {r['5.1']['TP'] or 0:7.1f}")
    for k in ["loro", "ltrt_pan", "ltrt_hilb_py", "ltrt_hilb_ff"]:
        v = r[k]; c = v["corr"]
        print(f"{'':9} {k:13} {v['I']:7.1f} {v['TP']:7.1f} {v['I_mono']:7.1f} {v['TP_mono']:7.1f} {c if c is None else round(c,3)!s:>6}")
print("null py vs ff (dB):", round(res["null_py_vs_ff_dB"], 1), "| >50 Hz:", round(res["null_py_vs_ff_dB_above50Hz"], 1), "| gain FIR 100/1k/15k:", [round(v, 2) for v in res["fir_gain_dB_100_1k_15k"]])
for k in ["ltrt_pan", "ltrt_hilb_py"]:
    print(f"amb_wrap {k} RMS Lt/Rt dBFS:", [round(v, 1) for v in res[f"amb_wrap_{k}_rms_Lt_Rt_dBFS"]])
