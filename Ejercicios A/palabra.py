# Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
# de la palabra introducida empezando por la última

# Pedimos al usuario una palabra
palabra = input("Introduce una palabra: ")

# En el siguiente bucle recorreremos la palabra introducida y la leeremos letra por letra
for letra in reversed(palabra):
    print(letra)