"""
Edit operations module
Handles all text editing operations: undo, redo, copy, cut, paste, etc.
"""

import tkinter as tk

class EditOperations:
    """
    Class responsible for all text editing operations
    """
    
    def __init__(self, editor):
        """
        Initializes edit operations
        
        Args:
            editor: Reference to the main TextEditor instance
        """
        self.editor = editor
    
    def undo(self):
        """Undoes the last action"""
        try:
            if self.editor.text_widget.edit_undo():
                self.editor.text_widget.edit_separator()  # Better undo handling
        except Exception as e:
            self.editor.error_handler.handle_error("undo", e, show_user=False)
    
    def redo(self):
        """Redoes the last undone action"""
        try:
            if self.editor.text_widget.edit_redo():
                self.editor.text_widget.edit_separator()
        except Exception as e:
            self.editor.error_handler.handle_error("redo", e, show_user=False)
    
    def copy(self):
        """Copies the selected text"""
        try:
            if self.editor.text_widget.tag_ranges(tk.SEL):
                self.editor.text_widget.clipboard_clear()
                selected_text = self.editor.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
                self.editor.text_widget.clipboard_append(selected_text)
        except Exception as e:
            self.editor.error_handler.handle_error("copy", e, show_user=False)
    
    def cut(self):
        """Cuts the selected text"""
        try:
            if self.editor.text_widget.tag_ranges(tk.SEL):
                self.copy()
                self.editor.text_widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except Exception as e:
            self.editor.error_handler.handle_error("cut", e, show_user=False)
    
    def paste(self):
        """Pastes text from clipboard"""
        try:
            text = self.editor.text_widget.clipboard_get()
            if text:
                self.editor.text_widget.insert(tk.INSERT, text)
        except Exception as e:
            self.editor.error_handler.handle_error("paste", e, show_user=False)
    
    def select_all(self):
        """Selects all text"""
        try:
            self.editor.text_widget.tag_add(tk.SEL, "1.0", tk.END)
            self.editor.text_widget.mark_set(tk.INSERT, "1.0")
            self.editor.text_widget.see(tk.INSERT)
        except Exception as e:
            self.editor.error_handler.handle_error("select all", e, show_user=False)
