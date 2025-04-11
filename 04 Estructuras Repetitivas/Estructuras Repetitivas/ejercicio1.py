# Desarrollar un algoritmo que permita ingresar un número entero positivo.
# La computadora debe mostrar la sucesión de números pares desde el número ingresado hasta el cero ( inclusive ), en una sola linea.

numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    if numero % 2 != 0:
        numero = numero -1 
    cont = numero
    while cont >= 0:
          print(str(cont) + " ", end="")
          cont = cont - 2
else:
    print("El número ingresado no es válido.")