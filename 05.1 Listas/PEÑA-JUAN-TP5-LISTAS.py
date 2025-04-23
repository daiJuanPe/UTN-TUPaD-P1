# 1)
"""
multiplosDeCuatro = list(range(4, 101, 4)) #el ultimo numero no lo toma, por eso se pone un número mas, el terder numero da los saltos y el primero el inicio
print(multiplosDeCuatro)

# 2)

cincoElementos = [11, True, 11.11, 4, "Mundo"]
print(cincoElementos[3])
print(cincoElementos[-2])



# 3)

listaVacia = []

listaVacia.append("Hola")
listaVacia.append("Mundo")
listaVacia.append("Cruel")

print(listaVacia)

# 4)

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[3] = "oso"

print(animales)


# 5)

numeros = [8, 15, 3, 22, 7] # lista con números enteros aleatorios
numeros.remove(max(numeros)) # el metodo .remove() elimina los elementos indicados de la lista
# y max indica que elimine el número de mayor valor.
print(numeros) # se muestra la nueva lista modificada


# 6)

listaDel10Al30 = list(range(10, 31, 5))
print(listaDel10Al30)
print("Los dos primeros números son:", listaDel10Al30[:2])


# 7)

autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = ["auto rojo", "auto azul"]

print(autos)



# 8)

# 1. Crear una lista vacía llamada "dobles"
dobles = []

# 2. Agregar el doble de 5, 10 y 15 usando append()
dobles.append(5 * 2)  # Doble de 5 (10)
dobles.append(10 * 2)  # Doble de 10 (20)
dobles.append(15 * 2)  # Doble de 15 (30)

# 3. Imprimir la lista resultante
print("La lista de dobles es:", dobles)


# 9)

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

#d) Imprimir la lista resultante por pantalla
print(compras)

"""
# 10)

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)