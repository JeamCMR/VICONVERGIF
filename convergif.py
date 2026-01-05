#Inicio de pruebas

#import moviepy
from moviepy import VideoFileClip

video = VideoFileClip("prueba.mp4")

#Redimencionar
video_redimencion = video.resized(width=400)
#conversion gif
gif_video = video_redimencion.write_gif("prueba5.gif" ,fps=10)



