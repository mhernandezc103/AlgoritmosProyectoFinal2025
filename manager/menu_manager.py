# menu_manager.py
"""
Menu management module
Creates and manages all application menus
"""

from tkinter import Menu

class MenuManager:
    """
    Clase que crea el menu
    """
    
    def __init__(self, editor):
        """
        Inicializa el gestor de menús.
        
        Argumentos:
            editor: Referencia a la instancia principal de TextEditor.
        """
        self.editor = editor
    
    def create_menu(self):
        """
        Crea el menu principal
        """
        try:
            menubar = Menu(self.editor.root)
            self.editor.root.config(menu=menubar)

            # -------------------- FILE MENU --------------------
            file_menu = Menu(menubar, tearoff=0)
            menubar.add_cascade(label="File", menu=file_menu)
            file_menu.add_command(
                label="New", 
                command=self.editor.file_ops.new_file, 
                accelerator="Ctrl+N"
            )
            file_menu.add_command(
                label="Open", 
                command=self.editor.file_ops.open_file, 
                accelerator="Ctrl+O"
            )
            file_menu.add_command(
                label="Save", 
                command=self.editor.file_ops.save_file, 
                accelerator="Ctrl+S"
            )
            file_menu.add_command(
                label="Save As...", 
                command=self.editor.file_ops.save_file_as, 
                accelerator="Ctrl+Shift+S"
            )
            file_menu.add_separator()
            file_menu.add_command(
                label="Search", 
                command=self.editor.search_ops.open_search_window, 
                accelerator="Ctrl+F"
            )
            file_menu.add_separator()
            file_menu.add_command(label="Exit", command=self.editor.exit_application)

            # -------------------- EDIT MENU --------------------
            edit_menu = Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Edit", menu=edit_menu)
            edit_menu.add_command(
                label="Undo", 
                command=self.editor.edit_ops.undo, 
                accelerator="Ctrl+Z"
            )
            edit_menu.add_command(
                label="Redo", 
                command=self.editor.edit_ops.redo, 
                accelerator="Ctrl+Y"
            )
            edit_menu.add_separator()
            edit_menu.add_command(
                label="Copy", 
                command=self.editor.edit_ops.copy, 
                accelerator="Ctrl+C"
            )
            edit_menu.add_command(
                label="Cut", 
                command=self.editor.edit_ops.cut, 
                accelerator="Ctrl+X"
            )
            edit_menu.add_command(
                label="Paste", 
                command=self.editor.edit_ops.paste, 
                accelerator="Ctrl+V"
            )
            edit_menu.add_separator()
            edit_menu.add_command(
                label="Select All", 
                command=self.editor.edit_ops.select_all, 
                accelerator="Ctrl+A"
            )

            # -------------------- ENCODING MENU --------------------
            encoding_menu = Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Encoding", menu=encoding_menu)
            for enc in ['UTF-8', 'Latin-1', 'UTF-16']:
                encoding_menu.add_command(
                    label=enc, 
                    command=lambda e=enc.lower(): self.editor.file_ops.change_encoding(e)
                )

            # -------------------- HELP MENU --------------------
            help_menu = Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Help", menu=help_menu)
            help_menu.add_command(
                label="Information", 
                command=self.editor.dialog_manager.show_info
            )
            help_menu.add_command(
                label="User Manual", 
                command=self.editor.dialog_manager.open_manual
            )
            help_menu.add_command(
                label="Members", 
                command=self.editor.dialog_manager.show_members
            )

            self.setup_keyboard_shortcuts()

        except Exception as e:
            self.editor.error_handler.handle_error("create menu", e)
    
    def setup_keyboard_shortcuts(self):
        """Configura los atajos del teclado"""
        self.editor.root.bind('<Control-n>', lambda e: self.editor.file_ops.new_file())
        self.editor.root.bind('<Control-o>', lambda e: self.editor.file_ops.open_file())
        self.editor.root.bind('<Control-s>', lambda e: self.editor.file_ops.save_file())
        self.editor.root.bind('<Control-Shift-S>', lambda e: self.editor.file_ops.save_file_as())
        self.editor.root.bind('<Control-f>', lambda e: self.editor.search_ops.open_search_window())
        self.editor.root.bind('<Control-a>', lambda e: self.editor.edit_ops.select_all())
