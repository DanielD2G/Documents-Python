class Pelicula():
    def __init__(self, nombre):
        self.__nombre_pelicula = nombre

    def __str__(self):
        return str(self.__nombre_pelicula)

    def get_nombrepelicula(self):
        return self.__nombre_pelicula

    def set_nombrepelicula(self, nombre):
        self.__nombre_pelicula = nombre
    def Get_Text_Pelicula(self):
        print(self.__nombre_pelicula)
