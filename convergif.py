import argparse
from moviepy import VideoFileClip
def convertir_video(input_path, output_path, fps_value, width_value):
    video = VideoFileClip(input_path)
    video.resized(width=width_value)
    video.write_gifgiu(output_path, fps=fps_value)
    print(f"¡Éxito! GIF guardado en: {output_path}")
if __name__ == "__main__":
    #1.Crear el parser
    parser = argparse.ArgumentParser(description="Herramienta para convertir Video a GIF")

    # 2. Agregar argumentos
    # Argumento obligatorio: la ruta del video
    parser.add_argument("entrada", help="Ruta del archivo de video original")

    # Argumentos opcionales (con valores por defecto)
    parser.add_argument("--salida", default="resultado.gif", help="Nombre del archivo GIF de salida")
    parser.add_argument("--fps", type=int, default=10, help="Fotogramas por segundo (default: 10)")
    parser.add_argument("--ancho", type=int, default=480, help="Ancho del GIF en píxeles (default: 480)")

    # 3. Leer los argumentos de la terminal
    args = parser.parse_args()

    # 4. Llamar a tu función principal con los datos capturados
    convertir_video(args.entrada, args.salida, args.fps, args.ancho)

##Creditos JeamC


