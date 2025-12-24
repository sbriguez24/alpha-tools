import time
import os
import pygame
import csv
from datetime import datetime

# --- 1. DEFINICIÓN DE FUNCIONES (El banco de herramientas) ---

def iniciar_ondas_alfa():
    pygame.mixer.init()
    ruta_archivo = "Ondas_Alfa_10Hz_8min.mp3" 
    if os.path.exists(ruta_archivo):
        try:
            pygame.mixer.music.load(ruta_archivo)
            pygame.mixer.music.set_volume(0.5) 
            pygame.mixer.music.play(-1)
            print(f"--- 🎵 Ondas Alfa Activas ---")
        except Exception as e:
            print(f"Error al cargar audio: {e}")

def registrar_sesion(calificacion, duracion_min=8):
    """Guarda los datos en log_rendimiento.csv"""
    archivo_log = "log_rendimiento.csv"
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Verificamos si existe para poner o no los encabezados
    file_exists = os.path.isfile(archivo_log)
    
    with open(archivo_log, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Fecha", "Duracion_Min", "Sentimiento_1_10", "Estado"])
        writer.writerow([fecha_hora, duracion_min, calificacion, "Alpha"])

def guia_profesional(fase, segundos):
    for i in range(segundos, 0, -1):
        os.system('clear')
        print(f"--- MODO ALPHA: {fase} ---")
        print(f"\n      [ {i} ]")
        time.sleep(1)

# --- 2. EJECUCIÓN DEL PROGRAMA (Donde usamos las herramientas) ---

if __name__ == "__main__":
    iniciar_ondas_alfa()
    
    # Ciclo de prueba
    for _ in range(5): # Solo un ciclo para probar rápido
        guia_profesional("INHALA", 4)
        guia_profesional("MANTÉN", 4)
        guia_profesional("EXHALA", 4)

    print("\n--- SESIÓN COMPLETADA: Tu cerebro está en estado Alpha ---")
    
    # 1. Detenemos la música Inmediatamente
    pygame.mixer.music.stop()
    pygame.mixer.quit() # Cerramos el sistema de audio para liberar memoria
    print("Silencio Activado. así es tu estado Alpha... Sergio")
    
    # 2. Ahora en silencio, hacemos la pregunta para el log
    try:
        # Aquí es donde llamamos a la función que antes fallaba
        puntaje = input("¿Nivel de claridad mental (1-10)?: ")
        registrar_sesion(puntaje)
        print("✅ Datos guardados con éxito.")
    except Exception as e:
        # Si algo falla, intentamos guardar N/A
        print(f"Error al guardar: {e}")
    
    