# Escribe un programa que pida al usuario un número entero y muestre por pantalla una
# estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
# centro de la estructura.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# Pedimos al usuario un numero para formar la piramide ascendente y descendente
n = int(input("Introduce el numero de asteriscos: "))

# Bucle para recorrer dicha piramide
for i in range(1, n+1, 1):
    print("*" * i)
    
for i in range(n - 1, 0, -1):
    print("*" * i)