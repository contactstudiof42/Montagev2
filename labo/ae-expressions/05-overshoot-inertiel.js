// Overshoot inertiel après la dernière clé atteinte (principe décrit par Dan Ebberts, motionscript.com,
// réécrit ici). Le calque arrive avec une vitesse, dépasse sa cible, oscille et se pose.
// Mettre des clés LINÉAIRES (ou une sortie peu amortie) : l'overshoot récupère la vitesse d'arrivée.
var freq = 2.5;   // oscillations par seconde : plus haut = matière plus rigide
var decay = 6;    // amortissement : plus haut = se pose plus vite
var n = 0;
if (numKeys > 0) {
  n = nearestKey(time).index;
  if (key(n).time > time) n--;          // on veut la dernière clé DÉJÀ passée
}
var t = (n > 0) ? time - key(n).time : 0;
if (n > 0 && n == numKeys && t < 3) {   // seulement après la dernière clé ; coupe à 3 s (évite exp() énorme)
  var vIn = velocityAtTime(key(n).time - thisComp.frameDuration / 10); // vitesse JUSTE AVANT la clé
  var w = 2 * Math.PI * freq;
  add(value, mul(vIn, Math.sin(t * w) / Math.exp(decay * t) / w));
} else {
  value;
}
