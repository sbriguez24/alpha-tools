import time
import os
import pygame
import csv
import subprocess
import sys
from datetime import datetime
from colorama import Fore, Style, init

# Inicializa colorama para linux
init(autoreset=True)

# --- 1. DEFINICIÓN DE FUNCIONES ---

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

# MODIFICADA: Ahora acepta 'ms' y tiene la nueva columna en el CSV
def registrar_sesion(calificacion, ms, duracion_min=8):
    archivo_log = "log_rendimiento.csv"
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(archivo_log)
    
    with open(archivo_log, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Añadimos la columna "Reaccion_MS"
            writer.writerow(["Fecha", "Duracion_Min", "Sentimiento_1_10", "Reaccion_MS", "Estado"])
        writer.writerow([fecha_hora, duracion_min, calificacion, ms, "Alpha"])

# NUEVA: Para el histórico de progreso
def obtener_ultimo_progreso():
    archivo_log = "log_rendimiento.csv"
    if not os.path.exists(archivo_log):
        return None
    try:
        with open(archivo_log, mode='r') as file:
            lineas = list(csv.reader(file))
            if len(lineas) > 1:
                return int(lineas[-1][3]) # Lee la columna de los ms
    except:
        return None
    return None

def guia_profesional(fase, segundos):
    if "INHALA" in fase:
        color= Fore.GREEN
    elif "MANTÉN" in fase:
        color = Fore.CYAN
    elif "EXHALA" in fase:
        color = Fore.YELLOW
    else:
        color = Fore.WHITE
        
    for i in range(segundos, 0, -1):
        os.system('clear')
        print(color + Style.BRIGHT + f"--- MODO ALPHA: {fase} ---")
        print(color + f"\n    [{i}]")
        time.sleep(1)

# --- 2. EJECUCIÓN DEL PROGRAMA ---

if __name__ == "__main__":
    iniciar_ondas_alfa()
    
    for _ in range(2): 
        guia_profesional("INHALA", 4)
        guia_profesional("MANTÉN", 4)
        guia_profesional("EXHALA", 4)

    print("\n--- SESIÓN COMPLETADA ---")
    pygame.mixer.music.stop()
    
    # ---Lanzar el Test Visual (con ruta absoluta) ---
    print("\nIniciando Test de Enfoque Visual...")
    
    # Obtenemos la ruta completa de la carpeta donde está este script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_visual_test = os.path.join(directorio_actual, "visual_test.py")

    try:
        # Ejecutamos usando el Python dentro de tu venv y la ruta absoluta del archivo
        subprocess.run([sys.executable, ruta_visual_test], check=True)
    except Exception as e:
        print(f" Error al lanzar el test visual: {e}")
        print(f"Buscando en: {ruta_visual_test}")
    
    # --- Leer el resultado del archivo temporal
    nota_automatica = 8 # Default
    ms_actual = 350
    
    if os.path.exists("temp_result.txt"):
        with open("temp_result.txt", "r") as f:
            datos =f.read().split(',')
            nota_automatica = int(datos[0])
            ms_actual = int(datos[1])
        os.remove("temp_result.txt") # Limpiamos el temporal

     # --- LÓGICA DE HISTÓRICO ---
    ultimo_ms = obtener_ultimo_progreso()
    print("\n" + "-"*40)
    if ultimo_ms:
        dif = ultimo_ms - ms_actual
        if dif > 0:
            print(f"📈 ¡PROGRESO! Has mejorado {dif}ms respecto a la última sesión.")
        elif dif < 0:
            print(f"📉 Alerta: Estás {abs(dif)}ms más lento. Considera descansar.")
        else:
            print("➖ Mantienes tu nivel de respuesta.")
    else:
        print("🚀 Primera sesión con registro de métricas.")

    # --- GUARDADO 100% AUTOMÁTICO ---
    registrar_sesion(nota_automatica, ms_actual)
    print(f"✅ Datos guardados automáticamente: Nota {nota_automatica} ({ms_actual}ms)")
    print("-" * 40 + "\n")