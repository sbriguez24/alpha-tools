#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 23:27:58 2025

@author: sergio
"""

import tkinter as tk
import time
import random

class AlphaVisualChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alpha Visual Checker - Test de la Lente")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        
        # ---Nueva Línea: para garantizar visibilidad ---
        self.root.lift() # Eleva la ventana
        self.root.attributes('-topmost', True) # La pone sobre todas las demás
        self.root.focus_force() # Fuerza el foco del  teclado
        # Quita el siempre arriba después de 1 segundo para que no moleste
        self.root.after(1000, lambda: self.root.attributes('-topmost', False))
        # ------------------------------------------------------------
        
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black', highlightthickness=0)
        self.canvas.pack()
        
        # El círculo de fijación
        self.target = self.canvas.create_oval(375, 275, 425, 325, fill='gray')
        
        self.reacciones = []
        self.inicio_estimulo = 0
        self.esperando_respuesta = False
        
        self.root.bind('<space>', self.registrar_respuesta)
        self.instrucciones = self.canvas.create_text(400, 550, text="Presiona ESPACIO cuando el círculo cambie de color", fill="white", font=("Arial", 12))
        
        # Iniciar el ciclo de pruebas después de 2 segundos
        self.root.after(2000, self.lanzar_estimulo)
        self.root.mainloop()

    def lanzar_estimulo(self):
        if len(self.reacciones) < 5: # Haremos 5 pruebas rápidas
            delay = random.randint(2000, 5000) # Entre 2 y 5 segundos
            self.root.after(delay, self.cambiar_color)
        else:
            self.finalizar_test()

    def cambiar_color(self):
        self.canvas.itemconfig(self.target, fill='cyan') # Color Alpha
        self.inicio_estimulo = time.time()
        self.esperando_respuesta = True
        # El color solo dura 300ms (exige enfoque láser)
        self.root.after(300, lambda: self.canvas.itemconfig(self.target, fill='gray'))

    def registrar_respuesta(self, event):
        if self.esperando_respuesta:
            reaccion = (time.time() - self.inicio_estimulo) * 1000 # En milisegundos
            self.reacciones.append(reaccion)
            self.esperando_respuesta = False
            print(f"Reacción: {int(reaccion)}ms")
            self.lanzar_estimulo()

    def finalizar_test(self):
        promedio = sum(self.reacciones) / len(self.reacciones)
        promedio_int = int(promedio)
        
        # Lógica de la Tabla de Claridad Alpha
        if promedio_int < 250:
            nota = 10
            estado = "Estado de Flujo Total: Conexión neuronal óptima."
        elif 250 <= promedio_int <= 300:
            nota = 9
            estado = "Alto Rendimiento: Enfoque láser."
        elif 301 <= promedio_int <= 360:
            nota = 8
            estado = "Zona Alpha Estable: Tu cerebro está Despierto pero Tranquilo."
        elif 361 <= promedio_int <= 420:
            nota = 7
            estado = "Funcional: Hay presencia, pero con algo de ruido mental."
        elif 421 <= promedio_int <= 500:
            nota = 5
            estado = "Fatiga Leve: El sistema nervioso está lento."
        else:
            nota = 3
            estado = "Neblina Mental: Se recomienda descanso."
        # Crear Archivo temporal para el script Principal
        with open("temp_result.txt", "w") as f:
            f.write(f"{nota},{promedio_int}")
        print(f"\n--- TEST FINALIZADO: {promedio_int}ms ---")
        self.root.destroy()
        
 # --- Añade para probar ---
if __name__ == "__main__":
    test = AlphaVisualChecker()

