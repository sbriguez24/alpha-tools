#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 12:55:18 2025

@author: sergio
"""

import time
import os
import pygame

def iniciar_ondas_alfa():
    """Inicializa y reproduce la música de fondo una sola vez"""
    pygame.mixer.init()
    ruta_archivo = "Ondas_Alfa_10Hz_8min.mp3" 
    
    if os.path.exists(ruta_archivo):
        try:
            pygame.mixer.music.load(ruta_archivo)
            pygame.mixer.music.play(-1)  # El -1 hace que se repita en bucle
            print(f"--- 🎵 Ondas Alfa Activas: {ruta_archivo} ---")
        except Exception as e:
            print(f"Error al cargar el audio: {e}")
    else:
        print(f"⚠️ Archivo {ruta_archivo} no encontrado en la carpeta.")

def guia_profesional(fase, segundos):
    """Maneja la visualización del temporizador"""
    for i in range(segundos, 0, -1):
        os.system('clear')
        print(f"--- MODO ALPHA: {fase} ---")
        print(f"\n      [ {i} ] segundos")
        # Mantener la música sonando mientras el tiempo corre
        time.sleep(1)

if __name__ == "__main__":
    # 1. Iniciamos la música UNA SOLA VEZ
    iniciar_ondas_alfa()
    time.sleep(2) # Pausa breve para disfrutar el inicio del audio

    # 2. Ciclo de respiración (puedes repetir esto en un bucle)
    for _ in range(3): # Repite el ciclo 3 veces
        guia_profesional("INHALA PROFUNDO", 4)
        guia_profesional("MANTÉN Y ENFOCA", 4)
        guia_profesional("EXHALA LENTAMENTE", 4)
        guia_profesional("MANTÉN EN VACÍO", 4)

    print("\nSesión completada. Tu cerebro está en estado Alpha.")
    pygame.mixer.music.stop()