from tkinter import messagebox
import webbrowser

class DialogManager:
    """
    Clase que maneja los dialogos
    """
    
    def __init__(self, editor):
        """
        Inicia el Dialogo
        
        Argumentos:
            editor: El nombre del editor de Texto
        """
        self.editor = editor
    
    def show_info(self):
        """Muestra la informacion de la app"""
        info = """
        Editor de Texto Avanzado
        Version: 2.0
        
        Características:
        - Abrir y editar múltiples tipos de archivos
        - Compatibilidad con diferentes codificaciones
        - Guardar y guardar como con copia de seguridad automática
        - Búsqueda avanzada con resaltado
        - Deshacer/rehacer ilimitado
        - Manejo robusto de errores
        - Registro de actividad y errores
        
        
        © 2025 - Derechos reservados
        """
        messagebox.showinfo("Information", info)
    
    def open_manual(self):
        """Opens the user manual"""
        try:
            # Manual URL or repository
            manual_url = "https://github.com/your-username/your-repository"
            webbrowser.open(manual_url)
        except Exception as e:
            self.editor.error_handler.handle_error("open manual", e)
    
    def show_members(self):
        """Shows information about group members"""
        members = """
        Equipo de trabajo/Grupo:        
        
        Marlon Hernández - ID: 7690-25-19080  
        Pamela Alvarado - ID: 7690-25-16439
        Anderson Palma - ID: 7690-25-2440
        
        Curso: Algoritmos - Seccion C
        Universidad: Universidad Mariano Gálvez de Guatemala
        Anio: 2025
        """
        messagebox.showinfo("Group Members", members)
