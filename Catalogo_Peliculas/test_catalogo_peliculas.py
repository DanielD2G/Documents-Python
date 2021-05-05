import os
from servicios.catalogopeliculas import *
from dominio.pelicula import Pelicula

option = int(input("Seleccione la actividad a realizar \n 1) Agregar una nueva pelicula \n 2) Listar peliculas en el archivo \n 3) Eliminar el archivo de peliculas \n 4) Salir"))
exitt=True
while exitt== True:
    if option== 1:
        pelicula_add= input("Inserte el nombre de la pelicula: ")
        pelicula1= Pelicula(pelicula_add)
        AgregarPelicula(pelicula_add)
        break
    if option == 2:
        ListarPeliculas()
        break
    if option == 3:
        EliminarArchivo()
        break
    if option == 4:
        break