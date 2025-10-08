#!/usr/bin/env python3
"""
Script que lee el contenido de un archivo y lo muestra en consola.
Incluye manejo básico de errores.
"""

import sys
import os


def read_and_display_file(filepath):
    """
    Lee y muestra el contenido de un archivo.
    
    Args:
        filepath: Ruta del archivo a leer
    
    Returns:
        True si fue exitoso, False en caso de error
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(filepath):
            print(f"Error: El archivo '{filepath}' no existe.", file=sys.stderr)
            return False
        
        # Verificar si es un archivo (no un directorio)
        if not os.path.isfile(filepath):
            print(f"Error: '{filepath}' no es un archivo válido.", file=sys.stderr)
            return False
        
        # Intentar abrir y leer el archivo
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
            return True
            
    except PermissionError:
        print(f"Error: No se tienen permisos para leer el archivo '{filepath}'.", file=sys.stderr)
        return False
    except UnicodeDecodeError:
        print(f"Error: El archivo '{filepath}' no se puede decodificar como texto UTF-8.", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error inesperado al leer el archivo '{filepath}': {str(e)}", file=sys.stderr)
        return False


def main():
    """Función principal del script."""
    if len(sys.argv) < 2:
        print("Uso: python read_file.py <ruta_del_archivo>", file=sys.stderr)
        print("Ejemplo: python read_file.py README.md", file=sys.stderr)
        sys.exit(1)
    
    filepath = sys.argv[1]
    success = read_and_display_file(filepath)
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
