# « L'Air » — prompts vidéo

_2026-10-24. Gabarit des pros (`montage-ia-generative/prompts-seedance-pros.md`) : chaque référence avec son rôle, la première image décrite, l'optique en mesures tirées de Blender, l'action minutée, une lumière nommée, le son. Prompts en anglais, résumé en français dessous._

## Test du plan 1 : Omni Flash contre Seedance 2.5

_Plan 1 (0:00 à 0:05, `montage.md`) : plan large fixe, à hauteur de table ; face à face, de profil ; il siffle la première phrase de l'air (sifflement refait en post). Généré sur 6 s : 5 s de plan et 1 s de marge à la fin pour le L-cut. Optique de `CAM_01_large` (Blender) : 24 mm plein format (angle horizontal 74°), caméra à 0,95 m du sol et à 1,72 m du centre de la table._

### V1-OMNI — Plan 1, Omni Flash

> SCENE: a tiny prison chaplaincy at night. A giant young man in a white shirt teaches an old nun to whistle, across a small table lit by one candle.
> REFERENCES: @FirstFrame is the exact first frame of this shot: keep its composition, people, room, light and colors for the whole shot. @Image1 is the man's face reference, @Image2 is the nun's face reference: keep both faces identical to them. @Image3 is the room in the same light.
> CAMERA: locked-off static wide shot, no camera movement, no zoom, no cut. 24mm lens at table height, 0.95 m above the floor.
> ACTION, 6 seconds, real time. 0-4s: the man whistles softly, lips rounded, his head tilted slightly toward her, chest rising with small breaths; his enormous hands stay flat on the table. The nun watches him, still and a little stiff, lips pressed. 4-5s: he stops whistling and gives a small nod of the chin toward her: your turn. 5-6s: hold, both still, looking at each other. The candle flame flickers gently.
> PHYSICS: hands keep contact with the table, no sliding; no object moves except the candle flame; exactly one man and one woman in the frame, nobody enters or leaves.
> LIGHTING: unchanged from @FirstFrame: soft static magenta glow from the frosted window, rim-lighting their profiles; warm amber candlelight from below; deep blacks. The window light does not flicker or pulse.
> AUDIO: quiet room tone and a distant ventilation hum only. No music, no speech, no singing, no whistled melody.
> CONSTRAINTS: their legs and feet stay hidden under the table the whole time. The covered camera dome in the ceiling corner stays covered, its light off. No handcuffs, no shackles. Live-action 35mm film look, fine grain, not CGI, not a video game, no text.

_Résumé : première image S1 tenue tout le plan ; caméra fixe ; 0-4 s il siffle doucement, la tête penchée vers elle, les mains à plat ; elle le regarde, raide ; 4-5 s il s'arrête et lui fait signe du menton ; 5-6 s ils se regardent. Lumière inchangée, néon immobile. Son : ambiance seule, aucune mélodie (le sifflement se fait en post). Jambes cachées, dôme couvert et éteint._

### V1-SEEDANCE — Plan 1, Seedance 2.5

> SCENE CONTEXT: a tiny prison chaplaincy at night. A giant young man in a white shirt teaches an old nun to whistle, across a small table lit by one candle. One continuous shot.
> ACTIVE REFERENCES: @Image1 is the exact first frame of this shot and the authority for composition, people, room, light and colors. @Image2 and @Image3 are the man: same face, same curly dark hair and short beard, same white shirt buttoned up to the collar. @Image4 and @Image5 are the nun: same face, same dark navy habit, veil and white coif. @Image6 is the room in the same light. @Video1 is a grey 3D previz of this shot: read from it only the camera position and the positions of the two people; do NOT read from it its grey mannequins, colors, materials, light or faces.
> FIRST FRAME AND SPATIAL BLOCKING: exactly as @Image1. The man sits on the left in profile, facing right; the nun sits on the right in profile, facing left; the candle between them; the untouched meal tray at the near edge of the table; the covered camera dome in the top left ceiling corner. No empty establishing frame, no delayed reveal.
> FORMAT: one shot, 6 seconds, real time, no cut.
> OPTICS AND CAMERA: locked-off static camera, 24mm full-frame lens (74 degree horizontal field of view), 0.95 m above the floor, 1.72 m from the center of the table. No camera movement, no zoom.
> ACTION TIMING: 0.0-4.0s: he whistles softly, lips rounded, head tilted slightly toward her, chest rising with small breaths; his enormous hands stay flat on the table. She watches him, still and a little stiff, lips pressed. 4.0-5.0s: he stops whistling and gives a small nod of the chin toward her: your turn. 5.0-6.0s: hold, both still, looking at each other.
> PHYSICS: hands keep contact with the table, no sliding; the candle flame flickers gently; nothing else moves. Exactly one man and one woman in the frame; nobody enters or leaves.
> LIGHTING: the soft static magenta glow (#C2185B) of a city neon behind the frosted window, rim-lighting their profiles from above and behind; the warm amber candle (#FF9F43) lighting their faces softly from below. Both faces readable. The window light never flickers or pulses. No other light. Deep blacks with texture, light haze.
> AUDIO: quiet room tone and a distant ventilation hum only. No music, no speech, no singing, no whistled melody.
> CHARACTER ACTING: understated, natural, small movements; no smiling at the camera, no looking at the camera.
> STYLE: live-action cinema, 35mm film, fine grain, gentle halation, 24 fps, 180-degree shutter. Not CGI, not a 3D render, not a video game.
> POSITIVE CONSTRAINTS: their legs and feet stay hidden under the table the whole time; the dome stays covered by the white cloth, its light off; no handcuffs, no shackles, no tattoos; the cross is a plain wooden cross; no text.

_Résumé : même action et même minutage qu'Omni. S1 en référence d'autorité, les quatre fiches pour les visages, D1 v2 pour la pièce, la previz pour la caméra et les positions seulement. Optique de Blender, lumière nommée, son d'ambiance seul._
