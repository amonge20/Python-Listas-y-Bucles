# Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
# un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
# o sí mismo

# Bucle para recorrer entre el 2 al 100
for numero in range(2,101):
    # Si el numero es menor o igual a 1, no son primos
    if numero <= 1:
        continue
    # Se pone por defecto TRUE
    es_primo = True
    # Se inicializa otro bucle en que iterara desde 2 hasta num - 1
    for i in range(2, numero):
        # Si el numero es divisible por i, no es primo
        if numero % i == 0:
            # Se convierte en false
            es_primo = False
    # Si no es divisible, el numero es primo
    if es_primo:
        print(numero)