# Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de
# Scrabble. Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el
# segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la
# ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos
# en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano. 

# Creamos una lista de palabras con su letra y numero
palabras = ["A1","B2","C3","D4"]

# Variable de los puntos totales
total = 0

# Recorremos un bucle para contar la puntuacion de la lista "Palabras"
for ficha in palabras:
    puntos = int(ficha[1])
    total += puntos

# Resultado final de la puntuación
print("Puntos totales:",total)