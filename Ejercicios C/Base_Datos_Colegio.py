# Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
# estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
# para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
# También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
# completo.
# Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
# cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
# media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
# clase. 

# Lista de los estudiantes
alumnos = ["Aitor","Maria","Diego","Nerea"]
# Lista para guardar los datos de los alumnos junto con sus notas
Base_Datos = []

# Bucle para preguntar las notas que han sacado
for alumno in alumnos:
    # Por cada estudiante preguntaremos sus notas correspondientes a las diferentes tareas
    print(f"Estudiante {alumno}")
    deberes = float(input("Nota de los deberes: "))
    examen = float(input("Nota del examen: "))
    proyecto = float(input("Nota del proyecto: "))
    # Nueva lista para guardar los datos del alumno junto con sus notas
    Datos_Alumno = [alumno,deberes,examen,proyecto]
    # Lista para añadir a los alumnos junto con sus notas
    Base_Datos.append(Datos_Alumno)
    # Salto de linea
    print("")

# Salto de linea
print("")

# Bucle para calcular la media de cada alumno
for nota_final in Base_Datos:
    estudiante = nota_final[0]
    notas = nota_final[1:]
    media = sum(notas) / len(notas)
    print(f"Nota final del estudiante {estudiante}:",round(media,2))