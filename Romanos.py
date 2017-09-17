#encoding: UTF-8
# Genaro Ortiz Durán, A01375315
#Descripción: Convertir números enteros positivos en el rango (1,10) a números romanos.

#Convierte los números enteros a romanos multiplicando el entero por sus similares en unidad.
def convertirRomanos(n):
    if n>=1 and n<=3:
        romano=(n*"I")
        return romano
    elif n==4:
        romano= ("I")+ ("V")
        return romano
    elif n>=5 and n<=8:
        romano= ("V")+(n-5)*("I")
        return romano
    elif n==9:
        romano=("I")+(n-8)*("X")
        return romano
    else:
        romano=(n-9)*("X")
        return romano

def main():
    n=int(input("Teclea el número que desees convertir:"))
    if n>=1 and n<=10:
        print("El número romano es:", convertirRomanos(n))
    else:
        print("Error solo se pueden convertir números del 1 al 10")

main()
