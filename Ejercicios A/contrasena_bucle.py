# Escribe un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# Variable en que sera la contraseña correcta
Contrasena_Correcta = "Aitor"

# Pedimos por primera vez la contraseña al usuario
Contrasena_Introducida = input("Introduce la contraseña: ")
# Entramos en un bucle para pedir al usuario que introduzca la contraseña correcta
while Contrasena_Introducida != Contrasena_Correcta:
    print("Contraseña incorrecta, intentelo de nuevo")
    Contrasena_Introducida = input("Introduce la contraseña: ")
    
# Si la contraseña que introduce es la correcta, aparecera de que la contraseña introducida es la correcta
if Contrasena_Introducida == Contrasena_Correcta:
    print("Acceso garantizado, bienvenido usuario Aitor")