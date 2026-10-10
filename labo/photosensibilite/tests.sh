#!/bin/sh
# Vérités terrain synthétiques (2 s, 25 i/s, 320x180). Sorties dans labo/rendus/photosens/.
O=../rendus/photosens; mkdir -p $O
# A : noir/blanc alterné toutes les 2 images (6,25 flashs/s) -> doit échouer
ffmpeg -y -loglevel error -f lavfi -i "color=black:s=320x180:r=25:d=2" -vf "geq=lum='255*mod(floor(N/2),2)':cb=128:cr=128" $O/A.mp4
# B : noir/blanc toutes les 5 images (2,5 flashs/s) -> doit passer
ffmpeg -y -loglevel error -f lavfi -i "color=black:s=320x180:r=25:d=2" -vf "geq=lum='255*mod(floor(N/5),2)':cb=128:cr=128" $O/B.mp4
# C : cartons « néon » qui changent de teinte toutes les 2 images à luminance proche -> doit passer
ffmpeg -y -loglevel error -f lavfi -i "color=black:s=320x180:r=25:d=2" -vf "format=rgb24,geq=r='if(mod(floor(N/2),2),230,40)':g='if(mod(floor(N/2),2),60,120)':b='if(mod(floor(N/2),2),200,255)'" -pix_fmt yuv420p $O/C.mp4
# D : rouge saturé / noir toutes les 2 images -> doit échouer (général ET rouge)
ffmpeg -y -loglevel error -f lavfi -i "color=black:s=320x180:r=25:d=2" -vf "format=rgb24,geq=r='255*mod(floor(N/2),2)':g=0:b=0" -pix_fmt yuv420p $O/D.mp4
# E : noir/blanc toutes les 2 images sur un carré de 6 % de l'écran -> échoue avec la fenêtre WCAG 1/3 (passait avec --plein-ecran)
ffmpeg -y -loglevel error -f lavfi -i "color=gray:s=320x180:r=25:d=2" -vf "drawbox=x=130:y=60:w=60:h=60:c=white:t=fill:enable='mod(floor(n/2),2)'" $O/E.mp4
# F : flash blanc d'une image sur l'impact, un par seconde (recette R4 du kinetic) -> passe
ffmpeg -y -loglevel error -f lavfi -i "color=0x303030:s=320x180:r=25:d=2" -vf "drawbox=c=white:t=fill:enable='eq(mod(n,25),12)'" $O/F.mp4
# G : même flash d'une image, mais 4 par seconde (impacts sur des croches à 120 BPM) -> doit échouer
ffmpeg -y -loglevel error -f lavfi -i "color=0x303030:s=320x180:r=25:d=2" -vf "drawbox=c=white:t=fill:enable='eq(mod(n,6),3)'" $O/G.mp4
for x in A B C D E F G; do python3 -I flash_check.py $O/$x.mp4; done
