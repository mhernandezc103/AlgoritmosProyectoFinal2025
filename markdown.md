# Editor de Texto Avanzado - Seccion C - Python Tkinter

A professional text editor built with Python and Tkinter, featuring a modular architecture with full UTF-8 support.

## 📋 Features

- ✨ Open, edit and save multiple file types (.txt, .py, .cpp, .cs, etc.)
- 🔄 Unlimited undo/redo system
- 🔍 Advanced search with match highlighting
- 📝 Full text editing capabilities (copy, cut, paste, select all)
- 💾 Automatic backup creation (.bak files)
- 🌐 Multiple encoding support (UTF-8, Latin-1, UTF-16)
- 🔔 Change detection with save prompts
- 📊 Status bar with line/column position
- 🐛 Robust error handling with logging
- 🌍 Full UTF-8 support (accents, special characters, etc.)

## 📁 Project Structure

```
text-editor/
├── main.py                 # Application entry point
├── text_editor.py          # Main TextEditor class
├── logger_config.py        # Logging configuration
├── error_handler.py        # Error handling and logging
├── menu_manager.py         # Menu creation and management
├── file_operations.py      # File operations (open, save, new)
├── edit_operations.py      # Edit operations (undo, redo, copy, cut, paste)
├── search_operations.py    # Search functionality
├── dialog_manager.py       # Information dialogs
└── README.md              # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- tkinter (usually comes with Python)

### Running the Application

1. Clone or download this repository
2. Navigate to the project directory
3. Run the main file:

```bash
python main.py
```

## 📖 Usage

### Keyboard Shortcuts

- `Ctrl+N` - New file
- `Ctrl+O` - Open file
- `Ctrl+S` - Save file
- `Ctrl+Shift+S` - Save as
- `Ctrl+F` - Search
- `Ctrl+Z` - Undo
- `Ctrl+Y` - Redo
- `Ctrl+C` - Copy
- `Ctrl+X` - Cut
- `Ctrl+V` - Paste
- `Ctrl+A` - Select all

### Menus

#### File Menu
- **New**: Create a new empty file
- **Open**: Open an existing file
- **Save**: Save current file
- **Save As**: Save with a new name/extension
- **Search**: Find text in the document
- **Exit**: Close the application

#### Edit Menu
- **Undo**: Undo last action
- **Redo**: Redo last undone action
- **Copy**: Copy selected text
- **Cut**: Cut selected text
- **Paste**: Paste from clipboard
- **Select All**: Select all text

#### Encoding Menu
- Change file encoding (UTF-8, Latin-1, UTF-16)

#### Help Menu
- **Information**: About the application
- **User Manual**: Open documentation
- **Members**: View development team information

## 🔧 Module Descriptions

### main.py
Entry point of the application. Initializes logging and creates the main window.

### text_editor.py
Main class containing the text editor logic. Manages the text widget, status bar, and coordinates all operations.

### logger_config.py
Configures the logging system for error tracking and debugging.

### error_handler.py
Centralized error handling with user-friendly messages and detailed logging.

### menu_manager.py
Creates and manages all application menus and keyboard shortcuts.

### file_operations.py
Handles all file-related operations:
- Opening files with automatic encoding detection
- Saving files with backup creation
- Creating new files
- Managing unsaved changes

### edit_operations.py
Manages text editing operations:
- Undo/redo functionality
- Clipboard operations (copy, cut, paste)
- Text selection

### search_operations.py
Provides search functionality:
- Case-sensitive/insensitive search
- Match highlighting
- Match counting and navigation

### dialog_manager.py
Manages information dialogs:
- Application information
- User manual access
- Team member information

## 🌐 UTF-8 Support

This editor fully supports UTF-8 encoding, allowing you to work with:
- Spanish characters (á, é, í, ó, ú, ñ, ¿, ¡)
- Special symbols and diacritics
- Multiple language scripts
- Extended Unicode characters

## 📝 Logging

The application creates an `editor_errors.log` file that records:
- Application startup and shutdown
- File operations (open, save)
- Errors and exceptions
- Debug information

## 👥 Authors

**Universidad Mariano Gálvez de Guatemala**  
Course: Algoritmos - Section C  
Year: 2025

### Team Members
- Marlon Hernández - ID: 7690-25-19080
- Pamela Alvarado - ID: [Add]
- Anderson Palma - ID: [Add]

## 📄 License

GPL v3.0 - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 🐛 Known Issues

- None at the moment

## 🔮 Future Enhancements

- Syntax highlighting for different programming languages
- Line numbers
- Multiple tabs support
- Find and replace functionality
- Print support
- Theme customization

## 📞 Support

For issues or questions, please check the log file (`editor_errors.log`) or contact the development team.# Advanced Text Editor - Python Tkinter

A professional text editor built with Python and Tkinter, featuring a modular architecture with full UTF-8 support.

## 📋 Features

- ✨ Open, edit and save multiple file types (.txt, .py, .cpp, .cs, etc.)
- 🔄 Unlimited undo/redo system
- 🔍 Advanced search with match highlighting
- 📝 Full text editing capabilities (copy, cut, paste, select all)
- 💾 Automatic backup creation (.bak files)
- 🌐 Multiple encoding support (UTF-8, Latin-1, UTF-16)
- 🔔 Change detection with save prompts
- 📊 Status bar with line/column position
- 🐛 Robust error handling with logging
- 🌍 Full UTF-8 support (accents, special characters, etc.)

## 📁 Project Structure

```
text-editor/
├── main.py                 # Application entry point
├── text_editor.py          # Main TextEditor class
├── logger_config.py        # Logging configuration
├── error_handler.py        # Error handling and logging
├── menu_manager.py         # Menu creation and management
├── file_operations.py      # File operations (open, save, new)
├── edit_operations.py      # Edit operations (undo, redo, copy, cut, paste)
├── search_operations.py    # Search functionality
├── dialog_manager.py       # Information dialogs
└── README.md              # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- tkinter (usually comes with Python)

### Running the Application

1. Clone or download this repository
2. Navigate to the project directory
3. Run the main file:

```bash
python main.py
```

## 📖 Usage

### Keyboard Shortcuts

- `Ctrl+N` - New file
- `Ctrl+O` - Open file
- `Ctrl+S` - Save file
- `Ctrl+Shift+S` - Save as
- `Ctrl+F` - Search
- `Ctrl+Z` - Undo
- `Ctrl+Y` - Redo
- `Ctrl+C` - Copy
- `Ctrl+X` - Cut
- `Ctrl+V` - Paste
- `Ctrl+A` - Select all

### Menus

#### File Menu
- **New**: Create a new empty file
- **Open**: Open an existing file
- **Save**: Save current file
- **Save As**: Save with a new name/extension
- **Search**: Find text in the document
- **Exit**: Close the application

#### Edit Menu
- **Undo**: Undo last action
- **Redo**: Redo last undone action
- **Copy**: Copy selected text
- **Cut**: Cut selected text
- **Paste**: Paste from clipboard
- **Select All**: Select all text

#### Encoding Menu
- Change file encoding (UTF-8, Latin-1, UTF-16)

#### Help Menu
- **Information**: About the application
- **User Manual**: Open documentation
- **Members**: View development team information

## 🔧 Module Descriptions

### main.py
Entry point of the application. Initializes logging and creates the main window.

### text_editor.py
Main class containing the text editor logic. Manages the text widget, status bar, and coordinates all operations.

### logger_config.py
Configures the logging system for error tracking and debugging.

### error_handler.py
Centralized error handling with user-friendly messages and detailed logging.

### menu_manager.py
Creates and manages all application menus and keyboard shortcuts.

### file_operations.py
Handles all file-related operations:
- Opening files with automatic encoding detection
- Saving files with backup creation
- Creating new files
- Managing unsaved changes

### edit_operations.py
Manages text editing operations:
- Undo/redo functionality
- Clipboard operations (copy, cut, paste)
- Text selection

### search_operations.py
Provides search functionality:
- Case-sensitive/insensitive search
- Match highlighting
- Match counting and navigation

### dialog_manager.py
Manages information dialogs:
- Application information
- User manual access
- Team member information

## 🌐 UTF-8 Support

This editor fully supports UTF-8 encoding, allowing you to work with:
- Spanish characters (á, é, í, ó, ú, ñ, ¿, ¡)
- Special symbols and diacritics
- Multiple language scripts
- Extended Unicode characters

## 📝 Logging

The application creates an `editor_errors.log` file that records:
- Application startup and shutdown
- File operations (open, save)
- Errors and exceptions
- Debug information

## 👥 Authors

**Universidad Mariano Gálvez de Guatemala**  
Course: Algoritmos - Section C  
Year: 2025

### Team Members
- Marlon Hernández - ID: 7690-25-19080
- Pamela Alvarado - ID: [Add]
- Anderson Palma - ID: [Add]

## 📄 License

GPL v3.0 - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 🐛 Known Issues

- None at the moment

## 🔮 Future Enhancements

- Syntax highlighting for different programming languages
- Line numbers
- Multiple tabs support
- Find and replace functionality
- Print support
- Theme customization

## 📞 Support

For issues or questions, please check the log file (`editor_errors.log`) or contact the development team.