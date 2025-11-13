"""
Módulo de configuración de registro
Configura el sistema de registro para la aplicación del editor de texto.
"""

import logging

def setup_logging():
    """
    Configura el sistema de registro con el formato y el archivo de salida adecuados.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='log/editor_errors.log',
        encoding='utf-8'
    )
