# Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
# Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
# aquellas palabras que no tienen ninguna letra prohibida.

# Importamos los siguientes modulos
import random, string

# Generamos las 5 palabras en una lista
palabras = []

# Bucle en que se muestren las 5 palabras
for _ in range(5):
    longitud = random.randint(3,8)   # Determina la longitud que tendra las 5 palabras
    palabra = ''.join(random.choices(string.ascii_lowercase, k=longitud))
    palabras.append(palabra)

# Resultado de las palabras aleatorias
print("Lista de palabras:",palabras)

# Generamos las 3 letras prohibidas en una lista
letras_prohibidas = []

# Bucle para mostrar las 3 letras prohibidas
for _ in range(3):
    letra = ''.join(random.choices(string.ascii_lowercase))
    letras_prohibidas.append(letra)

# Resultado de las 3 letras prohibidas
print("letras prohibidas:",letras_prohibidas)

# Creamos una lista para filtrar las palabras que NO contengan esas letras prohibidas
palabras_filtradas = [p for p in palabras if not any(letra in p for letra in letras_prohibidas)]

print("Palabras filtradas:",palabras_filtradas)