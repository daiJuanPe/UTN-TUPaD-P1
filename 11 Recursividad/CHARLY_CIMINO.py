
import sys

sys.setrecursionlimit(200000)
def factorial_recur(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recur(x-1)
    

#otra forma

def factorial_recur2(x):
    return 1 if x == 0 else x * factorial_recur2(x - 1)

# Programa principal
factorial_recur(5)

######################################################
#pasando una lista de numeros, obtener la suma total
# de los mismos de forma recursiva

def sum_list(list):
    if len(list)==0:
        return 0
    else:
        return list[0] + sum_list(list[1:])
    
lista=[1,2,3,4,5]
print(f"El valor total de la lista es {sum_list(lista)}")

#####################################################

# repetir frase recursiva

def repetir_frase(num, frase):
    if num >= 1:
        print(frase)
        repetir_frase(num-1, frase)

repetir_frase(3, "Homa mundo")

#####################################################

# sumar n valores recursivo

def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + suma_recursiva(num-1)
    
####################################################

#sucesion de fibonacci

def fibonacci_recursivo(posicion):
    if posicion==0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1)+fibonacci_recursivo(posicion-2)
    
#######################################################

# sumar n primos

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5 + 1)):
        if numero % i == 0:
            return False
    return True

def sumar_primos_recursivo(n):
    if n == 0:
        return 0
    elif es_primo(n):
        return n + sumar_primos_recursivo(n-1)
    else:
        return sumar_primos_recursivo(n-1)
    
#######################################################



