class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    
    def __str__(self):
        return "El ancho proporcionado es: " + str(self._ancho) + " El alto proporcionado es: " + str(self._alto)

    def get_ancho(self):
        return self._ancho
    def set_ancho(self):
        self._ancho = ancho_mod
    def get_alto(self):
        return self._alto
    def set_alto(self):
        self._alto = alto_mod         

