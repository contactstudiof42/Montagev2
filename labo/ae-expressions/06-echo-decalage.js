// Suiveur / écho : ce calque reprend la position du calque juste au-dessus avec un retard en images.
// Dupliquer le calque N fois : chaque copie suit la précédente -> traînée en cascade.
var retardImages = effect("Retard (images)")("Slider");
var leader = thisComp.layer(index - 1);
leader.transform.position.valueAtTime(time - retardImages * thisComp.frameDuration);
