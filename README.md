# demo
Demo

## Script de Lectura de Archivos

Este repositorio incluye un script en Python (`read_file.py`) que permite leer y mostrar el contenido de archivos de texto en la consola.

### Uso

```bash
python3 read_file.py <ruta_del_archivo>
```

### Ejemplo

```bash
python3 read_file.py ejemplo.txt
python3 read_file.py README.md
```

### Características

- Lee archivos de texto y muestra su contenido en consola
- Manejo de errores básico:
  - Verifica que el archivo existe
  - Verifica que es un archivo válido (no un directorio)
  - Maneja errores de permisos
  - Maneja errores de codificación UTF-8
- Muestra mensajes de error apropiados cuando ocurre un problema
