# 1. Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas
# de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa.
lista_frutas = ["manzana","platano","cereza","pera","higo","frambuesa","Fresa"]

# 2. Usa la función len() para imprimir la longitud de la lista frutas.
print(len(lista_frutas))

# 3. Accede al objeto numero 3 de la lista e imprímelo por consola.
print(lista_frutas[3])

# 4. Modifica el segundo objeto de la lista y cambiado a mora.
lista_frutas[1] = "mora" 
print(lista_frutas)

# 5. Añade el string mango al final de la lista.
lista_frutas.append("mango")
print(lista_frutas)

# 6. Usa el método insert() y añade el string “uva“ año comienzo de la lista.
lista_frutas.insert(0,"uva")
print(lista_frutas)
print()

# 7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola
for frutas in lista_frutas:
    print(frutas)
print()

# 8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable
# llamada “ultima_fruta“.
ultima_fruta = lista_frutas.pop()
print(lista_frutas)
print()

# 9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola
for frutas in lista_frutas:
    print(frutas)
print()
    
# 10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola
for frutas in lista_frutas:
    print(f"{frutas}: {len(frutas)} caracter/es")
print()

# 11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que
# tengan más de 5 caracteres
for frutas in lista_frutas:
    if len(frutas) >= 5:
        print(frutas)
print()

# 12. Usa el método remove() para borrar el string “cereza“ de la lista.
lista_frutas.remove("cereza")
print(lista_frutas)

# 13. Usa el método clear() para vaciar la lista. 
lista_frutas.clear()
print("Lista vacia:",lista_frutas)