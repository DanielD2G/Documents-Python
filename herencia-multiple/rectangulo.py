from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    def __str__(self):
        return "El alto de el rectangulo es: " + str(self._alto) + " El ancho del rectangulo es: "+ str(self._ancho) + " El area total es: " + str(self._alto+self._ancho) + " El color del rectangulo es: " + self._color

