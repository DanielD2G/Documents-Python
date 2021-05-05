import os
class Catalogo():
    ruta_archivo = "peliculas.txt"
    @staticmethod 
    def AgregarPelicula(pelicula):
        try:
            archivo = open(Catalogo.ruta_archivo, "a")
            archivo.write("\n" + pelicula)
        except Exception as e:
            print("Ocurrió un Error")
        finally:
            archivo.close()
    @staticmethod
    def EliminarArchivo():
        try:
            os.remove(Catalogo.ruta_archivo)
            print("\nEliminado satisfactoriamente")
        except Exception as e:
            print("\nNo se pudo borrar el archivo porque no existe") 
    @staticmethod
    def ListarPeliculas():
        try:
            archivo = open(Catalogo.ruta_archivo, "r")
            print("\nListado de peliculas:" + archivo.read())
        except Exception as e:
            print("Debes agregar peliculas antes")
        
