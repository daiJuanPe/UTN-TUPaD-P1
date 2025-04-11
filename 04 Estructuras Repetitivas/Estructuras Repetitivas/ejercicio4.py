# Desarrollar un algoritmo que permita ingresar una cantidad de personas. La
# computadora debe pedir la edad de cada una y finalmente mostrar el porcentaje de personas que
# es mayor de edad

cantidadDePersonas = int(input("Ingrese una cantidad de personas: "))
mayorDeEdad = 0
sumatoria = 0


while cantidadDePersonas <= 0:
    cantidadDePersonas = int(input("ERROR! Ingrese una cantidad de personas: "))

for x in range (1, cantidadDePersonas + 1):
    edad = int(input(f"Ingrese la edad de la persona {x}"))
    while edad <= 0:
        edad = int(input(f"Ingrese la edad de la persona {x}"))

    sumatoria += edad

    if edad >= 18:
        mayorDeEdad += edad

porcentaje = (mayorDeEdad * 100) / sumatoria

print(f"El porcentaje de personas mayores de edad es: {porcentaje} %")

