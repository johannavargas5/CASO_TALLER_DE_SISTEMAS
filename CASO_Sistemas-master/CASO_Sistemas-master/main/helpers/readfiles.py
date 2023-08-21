import os
#* Función para obtener la ruta de la carpeta raíz.
def Route():
    my_path = os.getcwd()
    if "\main" in my_path:
        my_path = my_path[:]
    else:
        my_path = my_path
    return my_path

