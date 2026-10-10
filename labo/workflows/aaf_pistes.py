"""Labo workflows — écrire un AAF audio « par familles » (DIAL / MUS / SFX) pour un mixeur, et le relire.
Lancer : python3 labo/workflows/aaf_pistes.py
Dépendances : pyaaf2 (testé 1.7.1), opentimelineio + otio-aaf-adapter pour la contre-lecture (facultatif).
Vérifie : positions et durées de chaque clip à l'image près après relecture (pyaaf2 puis OTIO).
"""
import json, os, wave
import numpy as np
import aaf2

ICI = os.path.dirname(os.path.abspath(__file__))
REND = os.path.join(ICI, "..", "rendus", "aaf"); os.makedirs(REND, exist_ok=True)
FPS, SR = 25, 48000

# Plan de mixage : famille -> [(position timeline, début dans la source, durée)] en images
PLAN = {"DIAL": [(0, 0, 100), (150, 120, 80)],
        "MUS": [(0, 0, 250)],
        "SFX": [(66, 0, 10), (140, 25, 10), (216, 50, 10)]}


def wav(nom, gen):
    t = np.arange(10 * SR) / SR; y = gen(t)
    p = os.path.join(REND, f"{nom}.wav")
    with wave.open(p, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    return p


SOURCES = {
    "DIAL": wav("DIAL", lambda t: 0.3 * np.random.default_rng(1).normal(0, 1, t.size) * (np.sin(2 * np.pi * 3 * t) > 0)),
    "MUS": wav("MUS", lambda t: 0.2 * np.sin(2 * np.pi * 220 * t)),
    "SFX": wav("SFX", lambda t: 0.8 * np.sin(2 * np.pi * 900 * t) * np.exp(-(t % 1.0) * 30)),
}


def ecrire(chemin):
    with aaf2.open(chemin, "w") as f:
        comp = f.create.CompositionMob("pièce06_mix"); f.content.mobs.append(comp)
        for fam, clips in PLAN.items():
            mm = f.create.MasterMob(fam); f.content.mobs.append(mm)
            mm.import_audio_essence(SOURCES[fam], edit_rate=FPS)  # essence embarquée
            slot = comp.create_sound_slot(edit_rate=FPS); slot.name = fam
            pos = 0
            for t0, src, n in clips:
                if t0 > pos:
                    slot.segment.components.append(f.create.Filler("sound", t0 - pos))
                slot.segment.components.append(mm.create_source_clip(slot_id=1, start=src, length=n))
                pos = t0 + n


def relire_pyaaf2(chemin):
    R = {}
    with aaf2.open(chemin, "r") as f:
        comp = next(f.content.compositionmobs())
        for slot in comp.slots:
            pos = 0; R[slot.name] = []
            for c in slot.segment.components:
                if isinstance(c, aaf2.components.SourceClip):
                    R[slot.name].append((pos, c.start, c.length))
                pos += c.length
    return R


def relire_otio(chemin):
    try:
        import opentimelineio as otio
    except ImportError:
        return "opentimelineio absent"
    try:
        tl = otio.adapters.read_from_file(chemin)
    except Exception as e:  # adaptateur AAF absent ou lecture refusée
        return f"échec OTIO : {type(e).__name__}: {e}"
    R = {}
    for tr in tl.tracks:
        R[tr.name] = [(round(tr.range_of_child(c).start_time.to_frames(FPS)), round(c.source_range.start_time.to_frames(FPS)),
                       round(c.source_range.duration.to_frames(FPS))) for c in tr if isinstance(c, otio.schema.Clip)]
    return R


if __name__ == "__main__":
    chemin = os.path.join(REND, "mix_familles.aaf"); ecrire(chemin)
    attendu = {k: [tuple(c) for c in v] for k, v in PLAN.items()}
    a = relire_pyaaf2(chemin); o = relire_otio(chemin)
    res = dict(taille_ko=round(os.path.getsize(chemin) / 1024), pyaaf2_identique=(a == attendu), pyaaf2=a,
               otio=o if isinstance(o, str) else dict(identique=({k: [tuple(c) for c in v] for k, v in o.items()} == attendu), pistes=o))
    print(json.dumps(res, indent=1, ensure_ascii=False))
    json.dump(res, open(os.path.join(ICI, "aaf_resultats.json"), "w"), indent=1, ensure_ascii=False)
