# partition_sfx.py : la partition sonore de la V4 (une famille de sons par technique visuelle) -> placement calé sur la
# crête de chaque son (crete.json), pistes A3-A8 attribuées sans chevauchement. Sortie : JSON compact à coller dans run_script.
import json, math
C = json.load(open("videos/phase-3/sony-linkbuds/sfx/crete.json"))
def f(debut):  # retrouve le fichier par le début de son nom
    k = [n for n in C if n.startswith(debut)]; assert len(k) == 1, (debut, k); return k[0]
V = "variantes/"
P = [  # (fichier, image de l'événement, gain dB)
 (f("Artlist Foley - Vintage Devices - Film Projector"), 0, -12),
 (f(V+"Phil Michalski - UI - Glassy Click (+0)"), 0, -9), (f(V+"Phil Michalski - UI - Glassy Click (+2)"), 13, -9),
 (f(V+"Phil Michalski - UI - Glassy Click (+4)"), 24, -9), (f(V+"Phil Michalski - UI - Glassy Click (+7)"), 36, -9),
 (f("Adam Pietruszko"), 48, -13), (f("Artlist Original - Hits  Pieces - Sub Drop"), 48, -7), (f(V+"Phil Michalski - UI - Glassy Click (+12)"), 48, -12),
 (f(V+"Cinemear - Petite Transitions - Fabric Whoosh Swift (+0)"), 94, -11),
 (f("Artlist Foley - Snapshots - Picture This"), 117, -9), (f("Soundkrampf - Cameraman - Chunky"), 129, -9),
 (f("Effectsworks - Real Life Whooshes - Thin Wire"), 140, -13),
 (f(V+"Phil Michalski - UI - Glassy Click (+0)"), 152, -15), (f(V+"Phil Michalski - UI - Glassy Click (+2)"), 157, -14),
 (f(V+"Phil Michalski - UI - Glassy Click (+4)"), 161, -13), (f(V+"Phil Michalski - UI - Glassy Click (+5)"), 165, -12),
 (f(V+"Phil Michalski - UI - Glassy Click (+7)"), 169, -11), (f(V+"Phil Michalski - UI - Glassy Click (+9)"), 172, -10),
 (f(V+"Phil Michalski - UI - Glassy Click (+12)"), 175, -9),
 (f("Artlist Original - Cymbal Risers - Reversed"), 179, -14),
 (f("Sampletraxx - Stutter"), 229, -10), (f("Sound Response - Thriller"), 233, -11),
 (f("DT Sound - Aural Impacts - Body Slam"), 233, -5), (f("BOOM Library - Transitions - Impact Sub"), 233, -8),
 (f(V+"Cinemear - Petite Transitions - Fabric Whoosh Swift (-3)"), 256, -13), (f("HD Audio - Unarmed Combat - Whoosh Quick"), 268, -13),
 (f("SoundBits - Tiny Transitions"), 281, -7), (f("Bjorn Lynne - Mr DJ"), 293, -10),
 (f("Selkor Studio"), 305, -14), (f("Artlist Foley - Female Breath"), 340, -15),
 (f("Martin Scaglia - Swoosh - Airy"), 363, -13), (f("Krotos - Cinematic Transitions - Basic"), 386, -13),
 (f(V+"Artlist Foley - Vintage Cameras - Konica EE Matic Mechanical Lever Pull Film Advance (-1)"), 421, -7),
 (f(V+"Artlist Foley - Vintage Cameras - Konica EE Matic Mechanical Lever Pull Film Advance (-3)"), 431, -7),
 (f(V+"Artlist Foley - Vintage Cameras - Konica EE Matic Mechanical Lever Pull Film Advance (+0)"), 440, -7),
 (f(V+"Artlist Foley - Vintage Cameras - Konica EE Matic Mechanical Lever Pull Film Advance (+2)"), 448, -7),
 (f(V+"Artlist Foley - Vintage Cameras - Konica EE Matic Mechanical Lever Pull Film Advance (+4)"), 455, -7),
 (f(V+"Artlist Foley - Vintage Cameras - Konica EE Matic Mechanical Lever Pull Film Advance (+5)"), 462, -7),
 (f("Artlist Original - Tonal Downers"), 466, -9),
 (f("CB Sounddesign"), 503, -7), (f("Artlist Original - Interference - Swipe"), 515, -11),
 (f(V+"Cinemear - Petite Transitions - Fabric Whoosh Swift (+3)"), 538, -13), (f("BOOM Library - Adrenaline"), 552, -11),
 (f("HD Audio - Unarmed Combat - Whoosh Powerful"), 562, -13), (f("Shapeforms - Hit and Punch"), 597, -11),
 (f("DeanKR - Graphical Essence"), 609, -14), (f("Vadi Sound - UI Clicks"), 621, -13), (f("Unrealsfx - Morph - Pop Click"), 632, -12),
 (f("Vadi Sound - Practical Materials"), 640, -8),
 (f("Airborne Sound - Electric Feel"), 656, -9),
 (f("Artlist Foley - Vintage Cameras - Polaroid"), 678, -7), (f("Callum Donaldson"), 688, -12),
 (f("Andy Rapaporte"), 690, -7), (f("Krotos - Cinematic Transitions - Short Fire"), 690, -13),
 (f("JBoB - Super Transitions"), 737, -13),
 (f(V+"DeanKR - Glitch Transitions - Digital Whoosh Buzzing (+0)"), 784, -10), (f(V+"DeanKR - Glitch Transitions - Digital Whoosh Buzzing (+3)"), 793, -10),
 (f(V+"DeanKR - Glitch Transitions - Digital Whoosh Buzzing (-2)"), 802, -10),
 (f("Travsonic - Group Reactions"), 809, -17),
 (f("Martin Scaglia - Swoosh - Thin"), 854, -14),
 (f("Echoto Sound - Streaming Logos"), 948, -9), (f("Effectsworks - Sounds From the Future"), 972, -15),
 (f(V+"Phil Michalski - UI - Glassy Click (+5)"), 1004, -19),
]
out = []; pistes = {k: [] for k in range(3, 9)}
for fic, ev, g in sorted(P, key=lambda p: p[1]):
    c = C[fic]; dur = math.ceil(c["duree"] * 25)
    deb = ev - round(c["crete"] * 25)              # la crête tombe sur l'image de l'événement
    src = 0
    if deb < 0: src, deb = -deb, 0                 # son qui commencerait avant 0 : on rogne sa tête
    fin = deb + dur - src
    for k in range(3, 9):
        if all(fin <= a or deb >= b for a, b in pistes[k]): pistes[k].append((deb, fin)); break
    else: raise SystemExit("pas de piste libre à %d" % ev)
    out.append([fic.split("/")[-1], deb, src, dur, k, g])
print(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
