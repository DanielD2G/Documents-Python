from color import Color
from figura_geometrica import FiguraGeometrica
from cuadrado import Cuadrado
from rectangulo import Rectangulo

select = int(input("1: para Cuadrado: 2 para rectangulo"))
fig=0 
if select == 1:
    lado = int(input("Inserta la medida de los lados"))
    colorc= (input("Inserta el color del cuadrado"))
    fig = Cuadrado(lado, colorc)
    print(fig)
elif select == 2:
    alto = int(input("Inserta el alto en cm"))
    ancho = int(input("Inserta el ancho en cm"))
    colorc = (input("Inserta el color del rectangulo"))
    fig = Rectangulo(ancho,alto, colorc)
    print(fig)

    