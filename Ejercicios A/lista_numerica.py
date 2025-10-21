# 1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros:
# [1,2,3,4,5,6,7,8,9,10].
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
print("Array original:",lista_numeros)

# 2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
pares_inverso = [n for n in reversed(lista_numeros) if n % 2 == 0]
print("Pares en orden inverso:",pares_inverso)

# 3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por
# consola.
print()
print("Bucle de lista de numeros elevado al cuadrado")
for numero in lista_numeros:
    print(numero**2)

# 4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
# compresión).
print()
print("Reaciendo los ejercicios 2 y 3")
pares_inverso_comprension = [n for n in lista_numeros[::-1] if n % 2 == 0]
cuadrados_comprension = [n**2 for n in lista_numeros]

print("Pares en orden inverso con comprension:",pares_inverso_comprension)
print("Cuadrados en comprension:",cuadrados_comprension)

# 5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
menor = min(lista_numeros)
print("El numero más pequeño:",menor)

# 6. Haz lo mismo con el número más alto
mayor = max(lista_numeros)
print("El numero más grande:",mayor)

# 7. Suma todos los elementos de la lista con y sin un bucle.
suma_numeros = sum(lista_numeros)
print("Suma total de la lista numeros:",suma_numeros)

# 8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
# el punto 2.
indice = lista_numeros.index(8)
print("El indice para el 8 es:",indice)