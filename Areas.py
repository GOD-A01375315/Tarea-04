#encoding: UTF-8
# Genaro Ortiz Durán, A01375315
#Descripción: Programa que calcula el área y perímetro de un rectángulo a partir de sus dimensiones y posteriormente los dibuja con la opción turtle.

import turtle
#Función que dibuja el rectangulo a partir de sus dimensiones con turtle.
def hacerRectangulo(b,h):

    turtle.color("blue")
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(h)

# Calcula el área multiplicando la base por la altura.
def calcularArea(b,h):
    A=(b*h)
    return A

#Calcula el perimetro sumando dos veces la base más dos veces la altura.
def calcularPerimetro(b,h):
    P= (2*b)+(2*h)
    return P


def main():
 #rectangulo uno
    b=float(input("Escribe la base del rectangulo:"))
    h=float(input("Escribe la altura del rectangulo:"))
 # rectangulo dos
    b1= float(input("Escribe la base del rectangulo 1:"))
    h1= float(input("Escribe la altura del rectangulo 2:"))
    area=calcularArea(b1,h1)
    perimetro=calcularPerimetro(b1,h1)
 #Salidas
    print("El área del rectangulo 1 es:", format(calcularArea(b, h,),".2f"))
    print("El area del rectangulo 2 es:",format(calcularArea(b1, h1,),".2f"))
    print("El perimetro del rectangulo 1 es:",calcularPerimetro(b, h))
    print("El perimetro del rectangulo 1 es:",calcularPerimetro(b1, h1))
    if (b*h)>(b1*h1):
        print("El área del rectangulo 1 es mayor al del rectangulo 2 ")
    elif (b*h)==(b1*h1):
        print("Las areas de los dos rectangulos son iguales")
    else:
         print("El área del rectangulo 2 es mayor que el rectangulo 1")
#turtle
    hacerRectangulo(b, h)
    hacerRectangulo(b1,h1)
    turtle.exitonclick()


main()