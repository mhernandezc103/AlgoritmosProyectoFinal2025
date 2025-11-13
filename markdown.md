# Editor de Texto Avanzado - Sección C - Python Tkinter

Un editor de texto profesional construido con Python y Tkinter, con una arquitectura modular y soporte completo para UTF-8.

## 📋 Características

- ✨ Abrir, editar y guardar múltiples tipos de archivo (.txt, .py, .cpp, .cs, etc.)
- 🔄 Sistema ilimitado de deshacer/rehacer
- 🔍 Búsqueda avanzada con resaltado de coincidencias
- 📝 Capacidades completas de edición de texto (copiar, cortar, pegar, seleccionar todo)
- 💾 Creación automática de respaldos (archivos .bak)
- 🌐 Soporte para múltiples codificaciones (UTF-8, Latin-1, UTF-16)
- 🔔 Detección de cambios con avisos para guardar
- 📊 Barra de estado con posición de línea/columna
- 🐛 Manejo robusto de errores con registro
- 🌍 Soporte completo para UTF-8 (acentos, caracteres especiales, etc.)

## 📁 Estructura del Proyecto
```
text-editor/
├── main.py                 # Punto de entrada de la aplicación
├── text_editor.py          # Clase principal TextEditor
├── logger_config.py        # Configuración de registro
├── error_handler.py        # Manejo y registro de errores
├── menu_manager.py         # Creación y gestión de menús
├── file_operations.py      # Operaciones de archivo (abrir, guardar, nuevo)
├── edit_operations.py      # Operaciones de edición (deshacer, rehacer, copiar, cortar, pegar)
├── search_operations.py    # Funcionalidad de búsqueda
├── dialog_manager.py       # Diálogos de información
└── README.md              # Este archivo
```

## 🚀 Instalación

### Requisitos Previos
- Python 3.6 o superior
- tkinter (usualmente viene con Python)

### Ejecutar la Aplicación

1. Clonar o descargar este repositorio
2. Navegar al directorio del proyecto
3. Ejecutar el archivo principal:
```bash
python main.py
```

## 📖 Uso

### Atajos de Teclado

- `Ctrl+N` - Nuevo archivo
- `Ctrl+O` - Abrir archivo
- `Ctrl+S` - Guardar archivo
- `Ctrl+Shift+S` - Guardar como
- `Ctrl+F` - Buscar
- `Ctrl+Z` - Deshacer
- `Ctrl+Y` - Rehacer
- `Ctrl+C` - Copiar
- `Ctrl+X` - Cortar
- `Ctrl+V` - Pegar
- `Ctrl+A` - Seleccionar todo

### Menús

#### Menú Archivo
- **Nuevo**: Crear un nuevo archivo vacío
- **Abrir**: Abrir un archivo existente
- **Guardar**: Guardar el archivo actual
- **Guardar Como**: Guardar con un nuevo nombre/extensión
- **Buscar**: Encontrar texto en el documento
- **Salir**: Cerrar la aplicación

#### Menú Editar
- **Deshacer**: Deshacer la última acción
- **Rehacer**: Rehacer la última acción deshecha
- **Copiar**: Copiar el texto seleccionado
- **Cortar**: Cortar el texto seleccionado
- **Pegar**: Pegar desde el portapapeles
- **Seleccionar Todo**: Seleccionar todo el texto

#### Menú Codificación
- Cambiar la codificación del archivo (UTF-8, Latin-1, UTF-16)

#### Menú Ayuda
- **Información**: Acerca de la aplicación
- **Manual de Usuario**: Abrir la documentación
- **Miembros**: Ver información del equipo de desarrollo

## 🔧 Descripción de Módulos

### main.py
Punto de entrada de la aplicación. Inicializa el registro y crea la ventana principal.

### text_editor.py
Clase principal que contiene la lógica del editor de texto. Gestiona el widget de texto, la barra de estado y coordina todas las operaciones.

### logger_config.py
Configura el sistema de registro para el seguimiento y depuración de errores.

### error_handler.py
Manejo centralizado de errores con mensajes amigables para el usuario y registro detallado.

### menu_manager.py
Crea y gestiona todos los menús de la aplicación y los atajos de teclado.

### file_operations.py
Maneja todas las operaciones relacionadas con archivos:
- Abrir archivos con detección automática de codificación
- Guardar archivos con creación de respaldo
- Crear nuevos archivos
- Gestionar cambios no guardados

### edit_operations.py
Gestiona las operaciones de edición de texto:
- Funcionalidad de deshacer/rehacer
- Operaciones de portapapeles (copiar, cortar, pegar)
- Selección de texto

### search_operations.py
Proporciona funcionalidad de búsqueda:
- Búsqueda sensible/insensible a mayúsculas
- Resaltado de coincidencias
- Conteo y navegación de coincidencias

### dialog_manager.py
Gestiona los diálogos de información:
- Información de la aplicación
- Acceso al manual de usuario
- Información de los miembros del equipo

## 🌐 Soporte UTF-8

Este editor soporta completamente la codificación UTF-8, permitiéndote trabajar con:
- Caracteres españoles (á, é, í, ó, ú, ñ, ¿, ¡)
- Símbolos especiales y diacríticos
- Múltiples sistemas de escritura
- Caracteres Unicode extendidos

## 📝 Registro

La aplicación crea un archivo `editor_errors.log` que registra:
- Inicio y cierre de la aplicación
- Operaciones de archivo (abrir, guardar)
- Errores y excepciones
- Información de depuración

## 👥 Autores

**Universidad Mariano Gálvez de Guatemala**  
Curso: Algoritmos - Sección C  
Año: 2025

### Miembros del Equipo
- Marlon Hernández - Carné: 7690-25-19080
- Pamela Alvarado - Carné: 7690-25-16439
- Anderson Palma - Carné: 7690-25-2440

## 📄 Licencia

GPL v3.0 - Ver el archivo LICENSE para más detalles

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! No dudes en enviar issues o pull requests.

## 🐛 Problemas Conocidos

- Ninguno por el momento

## 🔮 Mejoras Futuras

- Resaltado de sintaxis para diferentes lenguajes de programación
- Números de línea
- Soporte para múltiples pestañas
- Funcionalidad de buscar y reemplazar
- Soporte de impresión
- Personalización de temas

## 📞 Soporte

Para problemas o preguntas, por favor revisa el archivo de registro (`editor_errors.log`) o contacta al equipo de desarrollo.