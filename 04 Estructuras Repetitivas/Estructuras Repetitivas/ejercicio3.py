# Desarrollar un algoritmo que permita ingresar un número entero
# entre 1 y 10 (inclusive). La computadora debe mostrar la tabla de multiplicar del número ingresado.

numero = int(input("Ingresa un número entre 1 y 10"))

while numero > 10 or numero < 1:
    numero = int(input("ERROR! Ingresa un número entre 1 y 10"))

for x in range (1, 11):
    resultado = numero * x
    print(f"{numero} x {x} = {resultado}")
    
print("Chau!!!")