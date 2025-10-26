# Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
# los números primos de la lista original. Además, el script debe devolver el número total de
# números primos encontrados y la suma de los números primos encontrados 

# Extraemos una lista para calcular los numeros primos
lista_primos = [84, 7, 51, 36, 98, 12, 3, 72, 43, 57, 
                1, 65, 89, 19, 24, 99, 30, 8, 61, 46, 
                91, 15, 81, 33, 10, 5, 70, 25, 62, 56, 
                94, 23, 29, 37, 50, 85, 66, 13, 2, 47, 
                88, 20, 38, 9, 73, 41, 92, 34, 64, 77]

# Variable para el numero limite de los numeros primos
numero_limite = 100

# Lista para que nos devuelva que numeros són primos
lista_primos_devuelta = []

# Variables en que contarán de cuantos numeros primos hay
total_primos = 0
suma_primos = 0

# Generamos un bucle para recorrer la lista de numeros primos
for numero in lista_primos:
    if numero <= 1:
        continue
    
    # Verificamos si es primo
    es_primo = True
    
    # Generamos otro bucle para saber si són numeros primos
    for num in range(2, int(numero ** 0.5) + 1):
        if numero % num == 0:
            es_primo = False
            break
        
        # Si el numero es primo, se añadira en la lista de numeros primos devueltos
        if es_primo:
            lista_primos_devuelta.append(numero)
            suma_primos += 1
            total_primos += numero

# Resultado final
print("Numeros primos encontrados:",lista_primos_devuelta)
print("Cantidad de numeros primos:",total_primos)
print("Suma de los números primos:",suma_primos)