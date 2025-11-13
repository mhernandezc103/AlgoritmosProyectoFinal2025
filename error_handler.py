"""
Módulo de gestión de errores
Gestiona los errores y el registro en toda la aplicación.
"""

import logging
import traceback
from tkinter import messagebox

class ErrorHandler:
    """
    Clase responsable del manejo y registro de errores.
    """
    
    def handle_error(self, operation: str, error: Exception, show_user: bool = True):
        """
        Registra un error y muestra un mensaje al usuario (opcional).

        Argumentos:
        operation (str): nombre de la operación fallida.
        error (Exception): excepción capturada.
        show_user (bool): si es True, muestra un cuadro de mensaje al usuario.
        """
        logging.error(f"Error en {operation}: {error}")
        logging.debug(traceback.format_exc())
        
        if show_user:
            messagebox.showerror(
                "Error", 
                f"Ocurrio algo cuando: {operation}:\n{error}\n"
                "Revise el archivo <<editor_errors.log>> en la carpeta ./log"
            )
