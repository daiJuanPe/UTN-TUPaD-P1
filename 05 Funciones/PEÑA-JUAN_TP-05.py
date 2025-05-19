import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# def imprimir_hola_mundo():
#     return print("Hola Mundo!")

# imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# def saludar_usuario(nombre):
#     return print(f"Hola {nombre}!!!")


# nombre=input("Ingrese su nombre ")
# saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# def informacion_personal(nombre, apellido, edad, residencia):
#     return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivio en {residencia}")


# nombre = input("Ingrese su nombre ")
# apellido = input("Ingrese su apellido ")
# edad = int(input("Ingrese su edad "))
# residencia = input("Ingrese su residencia ")

# informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar
# el radio al usuario y llamar ambas funciones para mostrar los resultados.
# pi = math.pi 
# def calcular_area_circulo(radio):
#     area = pi*(radio*radio)
#     return print(f"El área del círculo es: {area}")

# def calcular_perimetro_circulo(radio):
#     perimetro = 2*pi*radio
#     return print(f"El perímetro de la circunferencia es: {perimetro}")

# radio = float(input("Ingrese el radio de la circunferencia: "))
# calcular_area_circulo(radio)
# calcular_perimetro_circulo(radio)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# def segundos_a_horas(segundos):
#     horas = segundos/3600
#     return print(f"{segundos} segundos, equivalen a {horas} horas.")

# segundos = float(input("Ingrese la cantidad de segundos "))
# segundos_a_horas(segundos)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# def tabla_multiplicar(numero):
#     for i in range(1,11):
#         print (f"{numero} x {i} = {numero*i}")
    
# num = int(input("Ingrese un número entero para saber su tabla de multiplicar "))
# tabla_multiplicar(num)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Función para realizar operaciones y devolver una tupla
# def operaciones_basicas(a, b):
#     return (a + b, a - b, a * b, a / b if b != 0 else "Error: División por cero")

# # Función para validar que b no sea 0 antes de operar
# def validar_numero():
#     while True:
#         b = float(input("Ingrese el segundo número (distinto de cero): "))
#         if b != 0:
#             return b
#         print("ERROR: el número debe ser distinto de cero.")  # Mensaje de error

# # Solicitar entrada del usuario
# a = float(input("Ingrese el primer número: "))
# b = validar_numero()  # Ahora `b` recibe el valor actualizado correctamente

# # Llamar a la f/unción y guardar resultados
# resultado = operaciones_basicas(a, b)

# # Mostrar resultados de manera clara
# print(f"El resultado de la suma es: {resultado[0]}")
# print(f"El resultado de la resta es: {resultado[1]}")
# print(f"El resultado de la multiplicación es: {resultado[2]}")
# print(f"El resultado de la división es: {resultado[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# def calcular_imc(peso, altura):
#     IMC = peso / (altura**2)
#     return print(f"El IMC es {IMC}")


# peso = float(input("Ingrese su peso en kg "))
# altura = float(input("Ingrese su altura en metros "))

# calcular_imc(peso, altura)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# def celsius_a_fahrenheit(celsius):
#     F=(celsius * 9/5)+32
#     return print(f"{F}°F")

# celsius = float(input("Ingrese una temperatura en grados celsius "))
# celsius_a_fahrenheit(celsius)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# def calcular_promedio(a, b, c):
#     promedio = float((a + b + c) / 3)
#     return print(f"El promedio de los números ingresados es: {promedio}")

# num1 = int(input("Ingrese el primer número "))
# num2 = int(input("Ingrese el segundo número "))
# num3 = int(input("Ingrese el tercer número "))

# calcular_promedio(num1, num2, num3)