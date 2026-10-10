"""Contrôle automatique des sauts de regard sur un montage entier (BACKLOG 48, outil généralisé de l'atelier 11).
Entrées : un EDL JSON {version: [[plan, durée], ...]} et des mesures JSON {plan: {perso: {x, regard, visible}}}
(produites par world_to_camera_view dans Blender, ou par un tracking 2D en post).
Règle : à une coupe entre deux plans centrés sur des personnages DIFFÉRENTS, les regards à l'écran doivent être opposés.
Un plan en mouvement (ex. "trav") peut fournir une entrée "<plan>_debut" / "<plan>_fin".
Usage : python3 sauts_regard.py edl.json mesures.json"""
import json, sys
edl = json.load(open(sys.argv[1])); edl = edl.get("EDL", edl); M = json.load(open(sys.argv[2]))


def sujet(m):
    """personnage cadré = visible et le plus proche du centre ; None si plan d'ensemble (2 visibles près du centre)"""
    vis = [(abs(v["x"] - .5), p, v["regard"]) for p, v in m.items() if v.get("visible")]
    if len(vis) != 1:
        return None  # plan à deux : pas de champ / contrechamp à contrôler
    return vis[0][1], vis[0][2]


def mesure(plan, bout):
    return M.get(f"{plan}_{bout}") or M.get(plan)


for version, plans in edl.items():
    t, sauts = 0.0, []
    for (a, da), (b, _) in zip(plans, plans[1:]):
        t += da; ma, mb = mesure(a, "fin"), mesure(b, "debut")
        if not (ma and mb):
            sauts.append((round(t, 2), a, b, "mesure absente")); continue
        sa, sb = sujet(ma), sujet(mb)
        if sa and sb and sa[0] != sb[0] and sa[1] == sb[1]:
            sauts.append((round(t, 2), a, b, f"{sa[0]} et {sb[0]} regardent tous deux à {sa[1]}"))
    print(version, f"{len(sauts)} saut(s)", *[f"\n  {s[0]} s : {s[1]} → {s[2]} : {s[3]}" for s in sauts])
