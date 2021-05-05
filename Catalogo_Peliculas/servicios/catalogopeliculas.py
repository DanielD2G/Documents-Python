import os
try:
    ruta_archivo = open("peliculas.txt", "a")
finally:
    ruta_archivo.close()
def AgregarPelicula(pelicula):
    try:
        ruta_archivo = open("peliculas.txt", "a")
        ruta_archivo.write("\n" + pelicula)
    finally:
        ruta_archivo.close()
def EliminarArchivo():
    os.remove("peliculas.txt")
def ListarPeliculas():
    try:
        ruta_archivo = open("peliculas.txt", "r")
        print("Listado de peliculas:" + ruta_archivo.read())
    finally:
        ruta_archivo.close()

