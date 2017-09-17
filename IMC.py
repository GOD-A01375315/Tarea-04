#encoding UTF-8
# Genaro Ortiz Durán, A01375315
#Descripción: Hacer un programa que calcula el IMC

#Calcula el Indice de Masa Corporal dividiendo el peso por la altura al cuadrado.
def calcularIMC(m,h):
    IMC=(m/(h**2))
    return IMC


def main():
    m=float(input("¿Cuál es tu peso?:"))
    h=float(input("¿Cual es tu altura?:"))
    print("Tu indice de masa corporal es:",format(calcularIMC(m, h),".2f"))

    if calcularIMC(m,h)<=18.5:
        print(" Tienes bajo peso")
    elif calcularIMC(m,h)>18.5 and calcularIMC(m,h)<=25:
        print("Tienes un peso normal")
    elif calcularIMC(m,h)>25:
        print("Tienes sobrepeso")








main()