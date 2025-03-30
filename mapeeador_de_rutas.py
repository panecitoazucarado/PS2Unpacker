import os

def print_directory_structure(start_path, indent=0):
    """
    Función que recorre un directorio y muestra su estructura de manera jerárquica.

    :param start_path: Ruta de inicio para recorrer el directorio.
    :param indent: Nivel de indentación para representar la jerarquía de carpetas.
    """
    # Mostrar el nombre del directorio actual con la indentación correspondiente
    print("    " * indent + f"└── {os.path.basename(start_path)}/")

    # Obtener el listado de directorios y archivos
    try:
        # Listar primero los directorios (para no mostrar archivos antes de tiempo)
        dirnames, filenames = [], []
        for entry in os.scandir(start_path):
            if entry.is_dir():
                dirnames.append(entry.name)
            elif entry.is_file():
                filenames.append(entry.name)

        # Primero, mostrar los directorios ordenados
        for dirname in sorted(dirnames):
            print_directory_structure(os.path.join(start_path, dirname), indent + 1)

        # Luego, mostrar los archivos
        for filename in sorted(filenames):
            print("    " * (indent + 1) + f"├── {filename}")
    except PermissionError:
        print("    " * (indent + 1) + "└── [Acceso denegado]")

if __name__ == "__main__":
    # Usar el directorio actual como punto de inicio
    start_path = os.getcwd()  # Cambiar esta ruta si deseas escanear un directorio específico
    print("Estructura de directorios y archivos:")
    print_directory_structure(start_path)