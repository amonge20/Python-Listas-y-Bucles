# Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
# pantalla el número de veces que aparece la letra en la frase.

# Pedimos al usuario una frase y una letra
frase = input("Introduce una frase: ")
letra_contar = input("Introduce una letra: ")
nletras = 0

# Bucle para recorrer la frase y que cuente la letra que ha pedido el usuario
for letra in frase:
    if letra == letra_contar:
        nletras += 1

# Resultado de cuantas letras ha contado
print("Con la letra ",letra_contar,"de la frase",frase,".Hay un total de ",nletras," letras")