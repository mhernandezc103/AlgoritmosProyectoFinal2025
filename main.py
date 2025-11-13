"""
Editor de texto avanzado en Python con Tkinter
=============================================

Este módulo implementa una aplicación GUI (interfaz gráfica de usuario) 
para la edición de texto, similar a un bloc de notas, pero con funcionalidades mejoradas.

Características principales:
--------------
- Apertura, edición y guardado de archivos (.txt, .py, .cpp, etc.)
- Compatibilidad con múltiples codificaciones (UTF-8, Latin-1, UTF-16)
- Sistema ilimitado de deshacer/rehacer
- Búsqueda avanzada con resaltado de coincidencias
- Copiar, cortar, pegar, seleccionar todo
- Detección de cambios y advertencias antes de cerrar o abrir un nuevo archivo
- Creación de copias de seguridad (.bak) antes de sobrescribir archivos
- Manejo robusto de errores con registros y mensajes de usuario
- Ventana de información y créditos para el grupo de desarrollo

Proyecto de:
-----------
Universidad Mariano Gálvez de Guatemala  
Curso: Algoritmos - Sección C  
Anio: 2025  

Miembros:
- Marlon Hernández - ID: 7690-25-19080  
- Pamela Alvarado - ID: 7690-25-16439
- Anderson Palma - ID: 7690-25-2440
"""

import tkinter as tk
from text_editor import TextEditor
from config.logger_config import setup_logging
import logging
from tkinter import messagebox

def main():
    """
    Main function with global error handling
    """
    try:
        #Metodo que configura los logs
        setup_logging()
        
        root = tk.Tk()
        app = TextEditor(root)
        root.mainloop()
        
    except Exception as e:
        logging.critical(f"Hubo un error en la app: {e}")
        messagebox.showerror(
            "Error Critico", 
            f"No se inicializo la app:\n{str(e)}\n\n"
            "Verifica los modulos."
        )

if __name__ == "__main__":
    main()