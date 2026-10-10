"""Labo paroles incrustées : temps de lecture d'un vers (BACKLOG 79, session 15). python3 -I temps_lecture.py > sortie
Pour chaque vers et chaque norme de vitesse de lecture : durée minimale d'affichage du vers complet (avec le plancher
de la norme), en secondes et en images à 24 et 25 i/s ; puis, pour un affichage mot à mot à un débit donné
(0,3 s par mot ≈ 3 syllabes/s, approximation), le temps de tenue nécessaire APRÈS l'apparition du dernier mot :
tenue = max(0, durée requise − durée d'apparition), durée d'apparition = (nb de mots − 1) × 0,3 s
(du 1er mot au dernier mot). Les espaces et la ponctuation comptent (règle Netflix).
Sources et statut des chiffres : sources/sous-titres-vitesse-lecture-2026-10.md (section Session 15).
Bibliothèque standard seulement."""
import math, sys

VERS = [   # inventés pour le labo (20 à 70 caractères)
    "On danse sous la pluie",
    "Demain on brûlera les cartes",
    "Les néons coulent sur le bitume mouillé",
    "J'ai gardé ta voix dans la poche de mon manteau",
    "Tout le quartier dort, moi je compte encore les fenêtres",
]
REFERENCE = "Les vitrines me rendent un type que je connais pas"   # vers de la pièce 19 (session 14)

def csa_fr(n):
    """Charte CSA 2011 (France, SME) : 12 car. → 1 s, 20 → 2 s, 36 → 3 s, 60 → 4 s (secondes de 25 images).
    Interpolation linéaire entre ces points (hypothèse du labo) ; au-delà de 60 car., prolongée à 15 car./s (hypothèse)."""
    pts = [(0, 1.0), (12, 1.0), (20, 2.0), (36, 3.0), (60, 4.0)]
    if n >= 60: return 4.0 + (n - 60) / 15
    for (a, ta), (b, tb) in zip(pts, pts[1:]):
        if a <= n <= b: return ta + (tb - ta) * (n - a) / (b - a)

# nom : (fonction car. -> secondes requises, plancher en s, plafond en s)
NORMES = {
    "Netflix FR adultes 17 c/s":    (lambda n: n / 17, 5 / 6, 7.0),
    "Netflix FR SME adultes 20 c/s": (lambda n: n / 20, 5 / 6, 7.0),
    "Netflix FR enfants 13 c/s":    (lambda n: n / 13, 5 / 6, 7.0),
    "ATAA 15 c/s (haut)":           (lambda n: n / 15, None, 5.0),   # plancher ATAA = 16 images (dépend de la cadence)
    "ATAA 14 c/s (bas)":            (lambda n: n / 14, None, 5.0),
    "CSA FR 2011 (SME, barème)":    (csa_fr, 1.0, None),
    "CSA Belgique 12 c/s (strict)": (lambda n: n / 12, None, None),
}
FPS = (24, 25)
SEC_PAR_MOT = 0.3

def images(s, fps): return math.ceil(round(s * fps, 6))   # arrondi au-dessus : jamais moins que la norme

def requis(nom, n, fps):
    f, plancher, plafond = NORMES[nom]
    s = f(n)
    if nom.startswith("ATAA"): s = max(s, 16 / fps)
    if plancher: s = max(s, plancher)
    trop = plafond is not None and s > plafond
    return s, trop

def main():
    print(f"Débit mot à mot supposé : {SEC_PAR_MOT} s par mot (≈ 3 syllabes/s). Tenue = images à garder après l'apparition du dernier mot.\n")
    for v in VERS + [REFERENCE]:
        n, mots = len(v), len(v.split())
        assert v == REFERENCE or 20 <= n <= 70, (v, n)
        app = (mots - 1) * SEC_PAR_MOT
        tag = " (référence pièce 19)" if v == REFERENCE else ""
        print(f"« {v} »{tag} : {n} car., {mots} mots, apparition mot à mot {app:.1f} s")
        print(f"  {'norme':31} {'requis s':>8} {'24 i/s':>7} {'25 i/s':>7} | {'tenue s':>7} {'24 i/s':>7} {'25 i/s':>7}")
        for nom in NORMES:
            s24, trop = requis(nom, n, 24); s25, _ = requis(nom, n, 25)
            t24, t25 = max(0.0, s24 - app), max(0.0, s25 - app)
            note = "  > plafond : couper le vers" if trop else ""
            print(f"  {nom:31} {s25:8.2f} {images(s24,24):7d} {images(s25,25):7d} | {t25:7.2f} {images(t24,24):7d} {images(t25,25):7d}{note}")
        print()

if __name__ == "__main__":
    main()
