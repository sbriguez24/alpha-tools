import tkinter as tk
import time
import os
import pygame
import subprocess
import sys
import csv
from datetime import datetime

# --- CONFIGURACIÓN DE AFIRMACIONES ---
AFIRMACIONES = [
    "ACEPTO Y AGRADEZCO MI PERFECTA SALUD",
    "MI MENTE ES BRILLANTE Y ENFOCADA",
    "LA LIBERTAD FINANCIERA FLUYE HACIA MÍ",
    "SOY CLARIDAD Y PODER DECISIVO",
    "DESARROLLO MI CEREBRO AL MÁXIMO"
]

class RespiracionAlphaGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alpha Mind Reprogramming")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.root.bind('<Escape>', lambda e: self.root.destroy())

        # Etiqueta para la instrucción de respiración (Superior)
        self.instruccion_label = tk.Label(self.root, text="", font=("Verdana", 25, "italic"), fg="#333333", bg="black")
        self.instruccion_label.pack(side="top", pady=50)

        # Etiqueta central para los mensajes de reprogramación
        self.label = tk.Label(self.root, text="", font=("Verdana", 20), fg="black", bg="black")
        self.label.pack(expand=True)

        self.ciclos_totales = 5
        self.iniciar_audio()
        self.ejecutar_ciclos(0)
        self.root.mainloop()

    def iniciar_audio(self):
        pygame.mixer.init()
        ruta_archivo = "Ondas_Alfa_10Hz_8min.mp3"
        if os.path.exists(ruta_archivo):
            try:
                pygame.mixer.music.load(ruta_archivo)
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
            except Exception as e:
                print(f"Error audio: {e}")

    def animar_fase(self, mensaje, duracion, modo):
        pasos = 60
        intervalo = int((duracion * 1000) / pasos)
        
        # Colores para las instrucciones
        colores_instruccion = {
            "INHALA": "#00FF00", # Verde
            "MANTÉN": "#00FFFF",  # Cian
            "EXHALA": "#FFFF00"  # Amarillo
        }
        
        for i in range(pasos):
            progreso = i / pasos
            if modo == "INHALA":
                size = 20 + int(progreso * 25)
                val = int(progreso * 255)
            elif modo == "MANTÉN":
                size = 45
                val = 255 if (i // 5) % 2 == 0 else 210
            else: # EXHALA
                size = 45 - int(progreso * 25)
                val = 255 - int(progreso * 255)
            
            color_hex = f'#{val:02x}{val:02x}{val:02x}'
            
            # Actualizar instrucción y mensaje central
            self.instruccion_label.config(text=modo, fg=colores_instruccion[modo])
            self.label.config(text=mensaje, font=("Verdana", size, "bold"), fg=color_hex)
            
            self.root.update()
            time.sleep(intervalo / 1000)

    def ejecutar_ciclos(self, contador):
        if contador < self.ciclos_totales:
            mensaje = AFIRMACIONES[contador % len(AFIRMACIONES)]
            
            # Sincronización rítmica 4-4-4
            self.animar_fase(mensaje, 4, "INHALA")
            self.animar_fase(mensaje, 4, "MANTÉN")
            self.animar_fase(mensaje, 4, "EXHALA")
            
            self.root.after(100, lambda: self.ejecutar_ciclos(contador + 1))
        else:
            self.finalizar()

    def finalizar(self):
        pygame.mixer.music.stop()
        self.root.destroy()
        
        directorio = os.path.dirname(os.path.abspath(__file__))
        path_test = os.path.join(directorio, "visual_test.py")
        
        print("\n--- SESIÓN DE RESPIRACIÓN COMPLETADA ---")
        try:
            subprocess.run([sys.executable, path_test], check=True)
            self.procesar_resultados()
        except Exception as e:
            print(f"Error al lanzar el test visual: {e}")

    def procesar_resultados(self):
        nota_automatica = 8
        ms_actual = 350
        if os.path.exists("temp_result.txt"):
            with open("temp_result.txt", "r") as f:
                datos = f.read().split(',')
                nota_automatica = int(datos[0])
                ms_actual = int(datos[1])
            os.remove("temp_result.txt")
        self.registrar_en_log(nota_automatica, ms_actual)

    def registrar_en_log(self, calificacion, ms):
        archivo_log = "log_rendimiento.csv"
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_exists = os.path.isfile(archivo_log)
        with open(archivo_log, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Fecha", "Duracion_Min", "Sentimiento_1_10", "Reaccion_MS", "Estado"])
            writer.writerow([fecha_hora, 8, calificacion, ms, "Alpha GUI+Reprog"])
        print(f"✅ Datos guardados: {ms}ms (Nota {calificacion})")

if __name__ == "__main__":
    RespiracionAlphaGUI()