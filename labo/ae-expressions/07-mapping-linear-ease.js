// Mapper une plage sur une autre. Ex. : opacité pilotée par un slider "Progression" 0..100,
// visible seulement entre 20 et 60 % de la progression, avec un fondu doux.
var p = effect("Progression")("Slider");
ease(p, 20, 60, 0, 100);
