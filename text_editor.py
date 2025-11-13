"""
Clase TextEditor principal
Contiene la lógica principal de la aplicación del editor de texto.
"""

import tkinter as tk
from tkinter import scrolledtext
from typing import Optional
import logging
from manager.menu_manager import MenuManager
from operations.file_operations import FileOperations
from operations.edit_operations import EditOperations
from operations.search_operations import SearchOperations
from manager.dialog_manager import DialogManager
from error_handler import ErrorHandler

class TextEditor:
    """
    Clase principal que representa el editor de texto.

    Gestiona toda la lógica de la interfaz: menú, área de texto, barra de estado,
    operaciones de archivo y edición, gestión de errores y codificaciones.
    """

    def __init__(self, root: tk.Tk):
        """
        Inicializa la ventana principal del editor y sus componentes gráficos.
        
        Parámetros:
            root (tk.Tk): Instancia principal de la ventana Tkinter.
        """
        self.root = root
        self.root.title("Text Editor - Untitled")
        self.root.geometry("900x600")
        
        # State variables
        self.current_file: Optional[str] = None
        self.is_modified = False
        self.current_encoding = 'utf-8'
        self.search_window: Optional[tk.Toplevel] = None
        self.case_sensitive = tk.BooleanVar()
        
        # Create main components
        self.create_text_area()
        self.create_status_bar()
        
        # Initialize managers
        self.error_handler = ErrorHandler()
        self.file_ops = FileOperations(self)
        self.edit_ops = EditOperations(self)
        self.search_ops = SearchOperations(self)
        self.dialog_manager = DialogManager(self)
        self.menu_manager = MenuManager(self)
        
        # Create menu after initializing managers
        self.menu_manager.create_menu()
        
        # Configure window close event
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)
        
        logging.info("Text editor initialized successfully")

    def create_text_area(self):
        """
        Crea el área de texto principal con soporte para desplazamiento y deshacer/rehacer.
        """
        try:
            self.text_widget = scrolledtext.ScrolledText(
                self.root,
                wrap=tk.WORD,
                undo=True,
                font=("Consolas", 11),
                maxundo=-1
            )
            self.text_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

            # Event bindings
            self.text_widget.bind("<<Modified>>", self.mark_as_modified)
            self.text_widget.bind("<KeyPress>", self.update_status_bar)

        except Exception as e:
            self.error_handler.handle_error("create text area", e, show_user=True)
            raise

    def create_status_bar(self):
        """Crea la barra de estatus."""
        self.status_bar = tk.Label(
            self.root,
            text="Ready | Line: 1, Column: 1",
            bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def mark_as_modified(self, event=None):
        """Marca el documento como modificado"""
        try:
            if self.text_widget.edit_modified():
                self.is_modified = True
                title = self.root.title()
                if not title.startswith("*"):
                    self.root.title("*" + title)
                self.text_widget.edit_modified(False)
        except Exception as e:
            self.error_handler.handle_error("mark as modified", e, show_user=False)
    
    def update_status_bar(self, event=None):
        """Modifica la barra de estado"""
        try:
            cursor_pos = self.text_widget.index(tk.INSERT)
            line, column = cursor_pos.split('.')
            self.status_bar.config(text=f"Ready | Line: {line}, Column: {int(column)+1}")
        except Exception as e:
            self.error_handler.handle_error("update status bar", e, show_user=False)
    
    def exit_application(self):
        """Cierra la app"""
        try:
            if not self.file_ops.verify_unsaved_changes("exit"):
                return
            
            self.root.quit()
            logging.info("Aplicacion cerrada")
            
        except Exception as e:
            self.error_handler.handle_error("exit", e)
            self.root.quit()  # Fuerza la salida
