// Respiration asymétrique sur l'Échelle : inspiration (montée) / rétention (tenue) / expiration (descente plus longue) / pause.
// Sliders en IMAGES : "Inspiration", "Rétention", "Expiration", "Pause" ; "Amplitude %" (ex. 4).
var f = thisComp.frameDuration;
var tIn = effect("Inspiration")("Slider") * f;
var tHold = effect("Rétention")("Slider") * f;
var tOut = effect("Expiration")("Slider") * f;
var tRest = effect("Pause")("Slider") * f;
var amp = effect("Amplitude %")("Slider") / 100;
var cycle = tIn + tHold + tOut + tRest;
var t = ((time - inPoint) % cycle + cycle) % cycle;
var k;
if (t < tIn) k = ease(t, 0, tIn, 0, 1);                                   // on gonfle, doux aux deux bouts
else if (t < tIn + tHold) k = 1;                                          // poumons pleins
else if (t < tIn + tHold + tOut) k = easeOut(t, tIn + tHold, tIn + tHold + tOut, 1, 0); // relâche vite puis se pose
else k = 0;                                                               // vide
mul(value, 1 + amp * k);
