"""
File operations module
Handles all file-related operations: open, save, new, etc.
"""

import os
import logging
from tkinter import filedialog, messagebox
import tkinter as tk

class FileOperations:
    """
    Class responsible for all file operations
    """
    
    def __init__(self, editor):
        """
        Initializes file operations
        
        Args:
            editor: Reference to the main TextEditor instance
        """
        self.editor = editor
    
    def new_file(self):
        """Creates a new file"""
        if not self.verify_unsaved_changes("create a new file"):
            return
        
        try:
            self.editor.text_widget.delete(1.0, tk.END)
            self.editor.current_file = None
            self.editor.is_modified = False
            self.editor.root.title("Text Editor - Untitled")
            self.editor.status_bar.config(text="New file created")
            logging.info("New file created")
        except Exception as e:
            self.editor.error_handler.handle_error("create new file", e)
    
    def verify_unsaved_changes(self, operation: str) -> bool:
        """
        Verifies if there are unsaved changes and asks the user
        
        Args:
            operation: Description of the operation being performed
            
        Returns:
            bool: True if it's safe to proceed, False otherwise
        """
        if self.editor.is_modified:
            response = messagebox.askyesnocancel(
                "Unsaved Changes",
                f"Do you want to save changes before {operation}?"
            )
            if response is None:  # Cancel
                return False
            elif response:  # Yes
                return self.save_file()
        return True
    
    def open_file(self):
        """Opens a file with handling of different encodings"""
        if not self.verify_unsaved_changes("opening another file"):
            return
        
        file_path = filedialog.askopenfilename(
            title="Open file",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("C++ files", "*.cpp"),
                ("C# files", "*.cs"),
                ("All files", "*.*")
            ]
        )
        
        if not file_path:
            return
        
        # Try different encodings
        encodings = ['utf-8', 'latin-1', 'utf-16', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                
                self.editor.text_widget.delete(1.0, tk.END)
                self.editor.text_widget.insert(1.0, content)
                self.editor.current_file = file_path
                self.editor.is_modified = False
                self.editor.current_encoding = encoding
                self.editor.root.title(f"Text Editor - {os.path.basename(file_path)} [{encoding}]")
                self.editor.status_bar.config(text=f"File opened: {file_path} ({encoding})")
                logging.info(f"File opened: {file_path} with encoding {encoding}")
                return
                
            except UnicodeDecodeError:
                continue
            except Exception as e:
                self.editor.error_handler.handle_error(
                    f"open file {file_path} with encoding {encoding}", e
                )
                return
        
        # If no encoding works
        messagebox.showerror(
            "Encoding Error",
            "Could not read the file with common encodings.\n"
            "The file might be corrupted or use an unsupported encoding."
        )
    
    def save_file(self) -> bool:
        """
        Saves the current file
        
        Returns:
            bool: True if saved successfully, False otherwise
        """
        if self.editor.current_file is None:
            return self.save_file_as()
        
        try:
            content = self.editor.text_widget.get(1.0, tk.END)
            
            # Create backup if file already exists
            if os.path.exists(self.editor.current_file):
                backup_path = self.editor.current_file + ".bak"
                try:
                    import shutil
                    shutil.copy2(self.editor.current_file, backup_path)
                except Exception as e:
                    logging.warning(f"Could not create backup: {e}")
            
            with open(self.editor.current_file, 'w', encoding=self.editor.current_encoding) as f:
                f.write(content)
            
            self.editor.is_modified = False
            title = self.editor.root.title()
            if title.startswith("*"):
                self.editor.root.title(title[1:])
            self.editor.status_bar.config(text=f"Saved: {self.editor.current_file}")
            logging.info(f"File saved: {self.editor.current_file}")
            return True
            
        except PermissionError:
            messagebox.showerror(
                "Permission Error",
                "You don't have permissions to save in this location.\n"
                "Try saving in another folder or with a different name."
            )
            return False
        except Exception as e:
            self.editor.error_handler.handle_error("save file", e)
            return False
    
    def save_file_as(self) -> bool:
        """
        Saves the file with a different name
        
        Returns:
            bool: True if saved successfully, False otherwise
        """
        file_path = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("C++ files", "*.cpp"),
                ("C# files", "*.cs"),
                ("All files", "*.*")
            ]
        )
        
        if not file_path:
            return False
        
        try:
            content = self.editor.text_widget.get(1.0, tk.END)
            with open(file_path, 'w', encoding=self.editor.current_encoding) as f:
                f.write(content)
            
            self.editor.current_file = file_path
            self.editor.is_modified = False
            self.editor.root.title(f"Text Editor - {os.path.basename(file_path)}")
            self.editor.status_bar.config(text=f"Saved as: {file_path}")
            logging.info(f"File saved as: {file_path}")
            return True
            
        except Exception as e:
            self.editor.error_handler.handle_error("save as", e)
            return False
    
    def change_encoding(self, encoding: str):
        """
        Changes the encoding of the current file
        
        Args:
            encoding: New encoding to use
        """
        if self.editor.current_file and self.editor.is_modified:
            response = messagebox.askyesno(
                "Change Encoding",
                "Changing the encoding will lose unsaved changes.\n"
                "Do you want to continue?"
            )
            if not response:
                return
        
        self.editor.current_encoding = encoding
        if self.editor.current_file:
            self.editor.root.title(
                f"Text Editor - {os.path.basename(self.editor.current_file)} [{encoding}]"
            )
        self.editor.status_bar.config(text=f"Encoding changed to: {encoding}")
