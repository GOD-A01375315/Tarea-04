#encoding: UTF-8
# Genaro Ortiz Durán, A01375315
#Descripción: Programa que calcula el resultante de la combinación entre dos colores primarios

# Saca las combinaciones a partir de los colores.
def sacarCombinaciones(color,color1):
    if color=="ROJO" and color1=="ROJO":
        c= "ROJO"

    elif color=="AZUL" and color1=="AZUL":
        c="AZUL"

    elif color=="AMARILLO" and color1=="AMARILLO":
        c="AMARILLO"
    elif color=="ROJO" and color1=="AZUL":
         c="MORADO"

    elif color == "AZUL" and color1 == "ROJO":
        c="MORADO"

    elif color == "AMARILLO" and color1 == "ROJO":
        c="NARANJA"

    elif color == "ROJO" and color1 == "AMARILLO":
         c="NARANJA"
    elif color == "AZUL" and color1 == "AMARILLO":
        c="VERDE"

    elif color == "AMARILLO" and color1 == "AZUL":
        c="VERDE"

    return c



def main():

    c=str(input("Escribe el primer color:"))
    c1=str(input("Escribe el segundo color:"))
    color = c.upper()
    color1 = c1.upper()
    color2 = c.lower()
    color3 = c1.lower()


    if color==("ROJO")or color2==("rojo") or color==("AZUL")or color2==("azul")or color==("AMARILLO") or color2==("amarillo") or color1== "ROJO" or color3=="rojo" or color1==("AZUL")or color3==("azul")or color1==("AMARILLO") or color3==("amarillo") :
        print("El color es valido")

    else:
        print("Solo se pueden combinar los colores primarios")



    print("La combinacion es:", sacarCombinaciones(color, color1))
main()



