# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def validar_numero(num):
    while num <= 1 :
        num = int(input("ERROR!! Ingrese un numero mayor a 1 "))
    return num 


num = int(input("Ingrese un numero mayor a 1 "))
validar_numero(num)

# Mostrar factoriales desde 1 hasta el número ingresado
print(f"Factoriales del 1 al {num}:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

###################################################################################

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique

# Función recursiva para calcular Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Validación de entrada
posicion = int(input("Ingrese una posición (número entero mayor o igual a 0): "))
while posicion < 0:
    posicion = int(input("ERROR. Ingrese un número mayor o igual a 0: "))

# Mostrar la serie de Fibonacci hasta la posición indicada
print(f"Serie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")

##################################################################################

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛
# (𝑚−1)
# . Prueba esta función en un
# algoritmo general.

# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Programa principal
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (mayor o igual a 0): "))

# Validación básica
while exponente < 0:
    exponente = int(input("ERROR. Ingrese un exponente mayor o igual a 0: "))

# Mostrar resultado
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")

################################################################################

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# 🧠Ejemplo:
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

# Función recursiva que convierte decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
num = int(input("Ingrese un número entero positivo: "))

# Validar entrada
while num < 0:
    num = int(input("ERROR. Ingrese un número POSITIVO: "))

# Mostrar el resultado
binario = decimal_a_binario(num)
print(f"El número {num} en binario es: {binario}")


######################################################################################

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    # Caso base: si tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si la primera y la última letra no son iguales, no es palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    else:
        # Llamada recursiva con la palabra sin primera y última letra
        return es_palindromo(palabra[1:-1])

# Programa principal para probar
texto = input("Ingrese una palabra sin espacios ni tildes: ").lower()

if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo')
else:
    print(f'"{texto}" no es un palíndromo')

################################################################################

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Programa para probar la función
numero = int(input("Ingrese un número entero positivo: "))

while numero < 0:
    numero = int(input("ERROR. Ingrese un número positivo: "))

resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

################################################################################

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Programa principal
nivel = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))

while nivel < 1:
    nivel = int(input("ERROR. Ingrese un número mayor o igual a 1: "))

total = contar_bloques(nivel)
print(f"Para construir la pirámide se necesitan {total} bloques en total.")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0 

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        contador = 1 if ultimo == digito else 0
        return contador + contar_digito(numero // 10, digito)

# Programa principal
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9) que desea contar: "))

while numero < 0 or digito < 0 or digito > 9:
    print("Error. Número debe ser positivo y dígito entre 0 y 9.")
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese un dígito (0-9) que desea contar: "))

resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en {numero}.")

