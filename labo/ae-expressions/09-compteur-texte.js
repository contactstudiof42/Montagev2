// Texte source : compteur 0 -> cible, avec ralenti à l'arrivée et séparateur de milliers français.
// Sliders : "Cible", "Début (s)", "Durée (s)".
var cible = effect("Cible")("Slider");
var t0 = effect("Début (s)")("Slider");
var d = effect("Durée (s)")("Slider");
var n = Math.round(easeOut(time, t0, t0 + d, 0, cible));
var s = String(Math.abs(n));
var out = "";
for (var i = 0; i < s.length; i++) {
  if (i > 0 && (s.length - i) % 3 === 0) out += " ";  // espace fine insécable
  out += s.charAt(i);
}
(n < 0 ? "-" : "") + out;
