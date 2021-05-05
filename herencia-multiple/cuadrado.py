from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def create(self):
        get_ancho= 0

    def area(self):
        return self._alto * self._ancho
    def __str__(self):
        return " El alto del cuadrado es: " + str(self._alto) + " El ancho del cuadrado es: " + str(self._ancho) +  " Lo que hace el total del área: " + str(self._alto + self._ancho) + " El color del cuadrado es: " + self._color

