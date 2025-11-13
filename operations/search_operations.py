"""
Search operations module
Handles text search functionality with highlighting
"""

import tkinter as tk

class SearchOperations:
    """
    Class responsible for search operations
    """
    
    def __init__(self, editor):
        """
        Initializes search operations
        
        Args:
            editor: Reference to the main TextEditor instance
        """
        self.editor = editor
    
    def open_search_window(self):
        """Opens search window with better handling"""
        # Avoid multiple search windows
        if self.editor.search_window and self.editor.search_window.winfo_exists():
            self.editor.search_window.lift()
            return
        
        try:
            self.editor.search_window = tk.Toplevel(self.editor.root)
            self.editor.search_window.title("Search")
            self.editor.search_window.geometry("400x200")
            self.editor.search_window.transient(self.editor.root)
            self.editor.search_window.resizable(False, False)
            
            # Center window
            self.editor.search_window.grab_set()
            
            tk.Label(self.editor.search_window, text="Search:").pack(pady=10)
            
            search_entry = tk.Entry(self.editor.search_window, width=40)
            search_entry.pack(pady=5)
            search_entry.focus()
            
            # Options frame
            options_frame = tk.Frame(self.editor.search_window)
            options_frame.pack(pady=5)
            
            tk.Checkbutton(
                options_frame, 
                text="Match case", 
                variable=self.editor.case_sensitive
            ).pack(side=tk.LEFT, padx=5)
            
            result_label = tk.Label(self.editor.search_window, text="", fg="blue")
            result_label.pack(pady=5)
            
            def perform_search():
                try:
                    # Clear previous selection
                    self.editor.text_widget.tag_remove("found", "1.0", tk.END)
                    
                    term = search_entry.get().strip()
                    if not term:
                        result_label.config(text="Enter a search term", fg="red")
                        return
                    
                    content = self.editor.text_widget.get(1.0, tk.END)
                    start = 1.0
                    count = 0
                    
                    # Configure highlighting tag
                    self.editor.text_widget.tag_config(
                        "found", 
                        background="yellow", 
                        foreground="black"
                    )
                    
                    while True:
                        if self.editor.case_sensitive.get():
                            pos = self.editor.text_widget.search(term, start, tk.END)
                        else:
                            pos = self.editor.text_widget.search(term, start, tk.END, nocase=True)
                        
                        if not pos:
                            break
                        
                        end = f"{pos}+{len(term)}c"
                        self.editor.text_widget.tag_add("found", pos, end)
                        count += 1
                        start = end
                    
                    if count > 0:
                        result_label.config(text=f"Found {count} match(es)")
                        # Go to first match
                        first_match = self.editor.text_widget.tag_ranges("found")[0]
                        self.editor.text_widget.see(first_match)
                        self.editor.text_widget.focus_set()
                    else:
                        result_label.config(text="No matches found", fg="red")
                        
                except Exception as e:
                    self.editor.error_handler.handle_error("perform search", e)
            
            def close_search():
                try:
                    self.editor.text_widget.tag_remove("found", "1.0", tk.END)
                    self.editor.search_window.destroy()
                    self.editor.search_window = None
                except Exception as e:
                    self.editor.error_handler.handle_error("close search", e, show_user=False)
            
            # Buttons frame
            buttons_frame = tk.Frame(self.editor.search_window)
            buttons_frame.pack(pady=10)
            
            tk.Button(
                buttons_frame, 
                text="Search", 
                command=perform_search
            ).pack(side=tk.LEFT, padx=5)
            tk.Button(
                buttons_frame, 
                text="Close", 
                command=close_search
            ).pack(side=tk.LEFT, padx=5)
            
            search_entry.bind('<Return>', lambda e: perform_search())
            self.editor.search_window.bind('<Escape>', lambda e: close_search())
            self.editor.search_window.protocol("WM_DELETE_WINDOW", close_search)
            
        except Exception as e:
            self.editor.error_handler.handle_error("open search window", e)
