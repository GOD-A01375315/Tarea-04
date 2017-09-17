#encoding UTF-8
# Genaro Ortiz Durán, A01375315
#Descripción: Hacer un programa que lea la cantidad de paquetes comprados, hacer un descuento si lo hay y hacer el total de la compra.

# Calcula el total de la compra multiplicando el número de paquetes por el precio. Si se compran más de 9 paquetes se aplica un descuento a partir de los rangos establecidos.
def calcularDescuento(p):
    if p>=1 and p<=9:
        t=(p*1500)
    elif p>=10 and p<=19:
        t=(p*.80)*1500
    elif p>=20 and p<=49:
        t=(p*.70)*1500
    elif p>=50 and p<=99:
        t=(p*.60)*1500
    else:
        p>100
        t=(p*.50)*1500

    return t

def main():
    p=int(input("¿Cuántos paquetes quieres:"))
    if p<0:
        print("ERROR")
    else:
        print("El total es:", calcularDescuento(p))

main()


