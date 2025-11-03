# El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se
# compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
# del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
# catalán la ”Ç”, en alemán la ”ß”, etc.).
# Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
# por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
# y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
# la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
# alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual.
#        [a,b,c,d,e,f,g,h,i,j,k,l,m] 		 	 [H, O, L, A]
#                   ROT13
# 	 	 [n,o,p,q,r,s,t,u,v,w,x,y,z]		 	 [U, B, Y, N]
# 1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto
# codificado según el cifrado ROT13
# 2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
# esta codificación ROT13 de la otra. 

# Introducimos la palabra que queremos escribir 
palabra_introducida = input("Introduce un texto: ")

# Creamos una lista vacia para guardar el resultado
Palabra_Normal = []

# El alfabeto
alfabeto_minus = list("abcdefghijklmnopqrstuvwxyz")
alfabeto_mayus = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Recorremos un bucle para descifrar el texto codificado de nuestra lista
for c in palabra_introducida:
    if c in alfabeto_minus:
        # Buscar índice y rotar 13 posiciones
        nueva_pos = (alfabeto_minus.index(c) + 13) % 26
        Palabra_Normal.append(alfabeto_minus[nueva_pos])
    elif c in alfabeto_mayus:
        nueva_pos = (alfabeto_mayus.index(c) + 13) % 26
        Palabra_Normal.append(alfabeto_mayus[nueva_pos])
    else:
        Palabra_Normal.append(c)

# Unimos la lista en un string
descifrado = "".join(Palabra_Normal)

# Resultado final
print(descifrado)