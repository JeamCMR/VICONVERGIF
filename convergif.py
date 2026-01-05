#Inicio de pruebas

import moviepy

video= moviepy.VideoFileClip("prueba.mp4").write_gif("prueba.gif" )
print(video.duration)

