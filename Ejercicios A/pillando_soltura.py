# 1. Escribe un programa en Python para encontrar los elementos duplicados de una lista,
# añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los
# elementos únicos.

# Creamos la lista duplicada
lista_duplicada = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]

# Eliminamos los duplicados y crearemos una lista unica
lista_unica = set(lista_duplicada)
print("Ejercicio 1: Quitamos la duplicacion de la lista creada.",lista_unica)

# 2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.

# Creamos 2 listas desordenadas
lista1 = [5,4,3,9,10]
lista2 = [1,6,7,8,2]

# Fusionamos las 2 listas y las ordenamos de manera ascendente
lista_fusionada = sorted(lista1 + lista2)
print("Ejercicio 2: Fusion de 2 listas en 1 de manera ordenada",lista_fusionada)

# 3. Escribe un script que encuentre el segundo número más grande de una lista.

# Creamos una lista desordenada
lista_desordenada = [10,4,6,7,2,3,5,1,9,8]

# La ordenamos pero en orden descendente
lista_desordenada.sort(reverse=True)

# Mostrara el resultado eligiendo el segundo mayor del orden inverso
print("Ejercicio 3: El segundo numero más grande de la lista invertida es",lista_desordenada[1])

# 4. Crea un script que cuente el número de elementos más grandes que un determinado número
# dado por el usuario (supón una lista numérica).

# Creamos una lista de 10 numeros
lista_elevada = [5,10,15,20,25,30,35,40,45,50]

# Pediremos al usuario que introduzca un numero
numero_pedido = int(input("Introduce un numero: "))

# Recorremos un bucle para saber si el numero que ha introducido el usuario es mayor que el numero que hay en la lista
contador = 0
for numero in lista_elevada:
    if numero < numero_pedido:
        contador += 1

# Resultado de cuantos numeros són mayores que el numero pedido
print("Ejercicio 4: El numero de veces de que el numero",numero_pedido," es mayor es de",contador,"vez/ces")

# 5. Crea un script dado un número introducido por el usuario o determinado al inicio del
# programa, realice la suma de aquellos números que sean divisibles por este.

# Creamos una lista para realizar la division 
lista_division = [5,10,15,20,25,30,35,40,45,50]

# Pediremos al usuario que introduzca un numero
numero_pedido = int(input("Introduce un numero: "))

# Recorremos un bucle para saber si el numero introducido se puede dividir por el numero introducido por el usuario
contador = 0
for numero in lista_division:
    if numero % numero_pedido == 0:
        contador += 1

print("Ejercicio 5: El numero de veces de que el numero",numero_pedido," se puede dividir es de",contador,"vez/ces")

# 6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
# que es inferior al número introducido o determinado al inicio del programa.

# Creamos una lista
lista_mas_alto = [5,10,15,20,25,30,35,40,45,50]

# Pedimos al usuario de que introduzca un numero
numero_pedido = int(input("Ejercicio 6: Numeros menores. Introduce un numero:" ))

# Recorremos un bucle para saber si el numero que ha introducido el usuario es mayor que el de la lista
numeros_menores = [n for n in lista_mas_alto if n < numero_pedido]

if numeros_menores:
    numero_max_inferior = max(numeros_menores)
    print("El número más alto menor que",numero_pedido," es:",numero_max_inferior)
else:
    print("No hay ningun numero menor que",numero_pedido)

# 7. Crea un script que extraiga los elementos comunes entre dos listas.

# Creamos 2 listas
lista1 = [1,2,3,4]
lista2 = [3,4,5,6]

# Extraemos los elementos comunes de las 2 listas
numeros_comunes = list(set(lista1) & set(lista2))

# Resultado de los numeros comunes extraidos
print("Ejercicio 7: Extraccion de numeros comunes:",numeros_comunes)

# 8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
# (P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)

# Creamos una lista para el numero de veces
lista_doble = [23, 65, 23, 45, 45, 45, 45, 10]

# Preguntamos al usuario de cual numero quiere de la lista que le proponemos
print(lista_doble)
numero_pedido = int(input("Ejercicio 8: De esta lista, ¿Que numero quieres que cuente?"))

# Contaremos el numero que ha pedido el usuario
numeros_contados = lista_doble.count(numero_pedido)
print("El numero de apariciones de",numero_pedido,"es",numeros_contados)

# 9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
# números positivos de la lista original.

# Se crearan una lista, en que juntara los positivos y los negativos
lista_positivo_negativo = [-5,10,-15,20,-25,30,-35,40,-45,50]

# Recorremos un bucle para coger los numeros positivos de dicha lista
numeros_positivos = [n for n in lista_positivo_negativo if n > 0]

# Resultado junto con los numeros positivos
print("Ejercicio 9 - numeros positivos:",numeros_positivos)

# 10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
# los strings de la lista original.

# Crearemos 2 listas para los textos y otra para que nos devuelta la longitud de dichas cadenas
lista_cadenas = ["Aitor","Monge","Santiago","python","viva"]
lista_tamano = [len(s) for s in lista_cadenas]

print("Ejercicio 10: Longitud de la lista.")
print("Lista original:",lista_cadenas)
print("Tamaño de los strings:",lista_tamano)

# 11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en
# mayúscula. 
lista_cadenas = ["Aitor","Monge","Santiago","python","viva"]
lista_mayuscula = [s.upper() for s in lista_cadenas]

print("Ejercicio 11: Lista en mayuscula.")
print("Lista original:",lista_cadenas)
print("Lista original pero con mayusculas:",lista_mayuscula)