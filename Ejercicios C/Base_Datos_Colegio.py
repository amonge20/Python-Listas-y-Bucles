# Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
# estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
# para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
# También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
# completo.
# Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
# cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
# media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
# clase. 

# Lista de los alumnos junto con las siguientes notas 
# ("Nombre Alumno", deberes, examenes, proyectos)
alumnos = [
    ["Aitor",8,5,5],
    ["Maria",10,10,10],
    ["Diego",4,6,6],
    ["Nerea",4,4,1]
]

# Bucle para la recopilación de las notas 
for datos in alumnos:
    nombre = datos[0]
    deberes = datos[1]
    examen = datos[2]
    proyecto = datos[3]
    print(f"Nombre del alumno:{nombre}")
    print(f"Nota de los deberes:{deberes}")
    print(f"Nota del examen:{examen}")
    print(f"Nota del proyecto:{proyecto}")
    print("")

# Salto de linea
print("")

# Bucle para calcular la nota final
for alumno in alumnos:
    nombre = alumno[0]
    notas = alumno[1:]
    media = sum(notas) / len(notas)
    print(f"Nota final de {nombre}:",round(media,2))