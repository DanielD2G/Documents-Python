from dominio.pelicula import Pelicula
from servicios.CaTalogodePeliculas import Catalogo
from os import *

#Menu 

bucle = True

while bucle != False:
    print("\nSeleccione la actividad a realizar")
    print("1) Agregar una nueva pelicula")
    print("2) Listar peliculas en el archivo")
    print("3) Eliminar el archivo de peliculas")
    print("4) Salir")
    selection = input("Selecciona 1-4 :")
    if selection == "1":
        peliculaInput = input("\nInserta la pelicula que quieres agregar: ")
        pelicula1 = Pelicula(peliculaInput)
        Catalogo.AgregarPelicula(peliculaInput)
        print(pelicula1)
    if selection == "2":
        Catalogo.ListarPeliculas()
    if selection == "3":
        Catalogo.EliminarArchivo()
    if selection == "4":
        bucle = False
else:
    print("\nExiting program...")
    