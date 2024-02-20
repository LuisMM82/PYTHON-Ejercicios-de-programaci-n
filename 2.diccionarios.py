# Ejercicio 1
# Pide al usuario que impute una lista de alumnos, separadas con ;. Después, pregunta por
# las notas de ellas. Realizar diccionario para después poder preguntar por alguien y
# observar sus notas.

# Solicita al usuario una lista de alumnos separados por ';'
alumnos = input(
    "Ingrese la lista de alumnos separados por ';' y sin espacio: ")
lista_alumnos = alumnos.split(';')

# Crea un diccionario vacío para almacenar los nombres y las notas de los alumnos
diccionario_notas = {}

# Pide las notas de cada alumno y almacénalas en el diccionario
for alumno in lista_alumnos:
    notas = input(f"Ingrese las notas para {alumno}: ")
    notas = [float(nota) for nota in notas.split(',')]
    diccionario_notas[alumno] = notas
# Imprime el diccionario de notas
print("Diccionario de notas:")
print(diccionario_notas)

# Pregunta por un alumno en particular
alumno_buscar = input("Ingrese el nombre del alumno que desea buscar: ")

# Verifica si el alumno está en el diccionario y muestra sus notas
if alumno_buscar in diccionario_notas:
    notas_alumno = diccionario_notas[alumno_buscar]
    print(f"Notas de {alumno_buscar}: {notas_alumno}")
else:
    print(f"{alumno_buscar} no se encuentra en el diccionario de notas.")

# Ejercicio 2
# Utiliza el ejercicio de el sistema a turnos de los ejercicios de Bucles For y While.
# Modifícalo para que las estadísticas de cada jugador sean una estructura de diccionario.
# Después, juega a tu antojo y modifica el cambio de estadísticas como si fueras un
# diseñador de videojuegos.

# Ejercicio 3
# Piensa que quieres usar un diccionario para organizarte. Diseña una agenda donde quieres
# anotar las tareas. Para ello, pedirás al usuario lo siguiente: 'Dime el día de la semana...'
# Usuario: lunes. 'Tienes 0 tareas pendientes. ¿Qué anotamos?'. Si hubiera alguna tarea,
# se mostraría cada elemento. Como ves, la clave será el día y el valor una lista.

agenda = {
    'Lunes': [],
    'Martes': ['paseo', 'estudiar', 'cine'],
    'Miercoles': ['paseo', 'estudiar', 'piscina'],
    'Jueves': ['paseo,estudiar,deporte'],
    'Viernes': ['paseo', 'estudiar', 'compra']
}
dia = input('¿Qué dia de la semana quieres ver?: ').capitalize()

while True:
    if dia in agenda:
        tareas = agenda[dia]
        print(f'Para el {dia} tienes {tareas}')
        añade_tarea = input("¿Quieres añadir alguna tarea?(s/n): ")
        if añade_tarea.lower() == "s":
            nueva_tarea = (
                input(f"Indica qué tarea quieres añadir al {dia}: "))
            tareas.append(nueva_tarea)
        else:
            print("De acuerdo.")
            break
    else:
        print("Error. Ese dia no está en la agenda.")
        break
# Ejercicio 4
# Imagina partir de una super lista de notas en formato texto, algo parecido a esto:
# ‘7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;‘. ¿Serías capaz de extraer el patrón para
# construir un diccionario donde la clave son los alumnos y el valor la puntuación
# promedio?

notas_texto = '7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;'

notas_lista = notas_texto.split(';;')
diccionario_notas = {}

for estudiante in notas_lista:
    if estudiante:
        # Para separar las partes de las notas y del estudiante.
        partes = estudiante.split('#')
        # El nombre del estudiante está en la segunda parte.
        nombre = partes[1]
        puntuaciones = [float(nota) for nota in partes[0].split(',')]
        # Suma de puntuaciones entre el número de puntuaciones.
        promedio = sum(puntuaciones) / len(puntuaciones)
        diccionario_notas[nombre] = promedio

print(diccionario_notas)

# Ejercicio 5
# Construye un sistema escolar entero. Para ello, el diccionario
# principal contendrá los cursos con la información de precio y nombre. Dentro de estas,
# existirán nuevos diccionarios para almacenar la siguiente información: ‘profesor,
# contacto, lista de alumnos totales, evaluación promedio‘.

sistema_escolar = {
    'Curso1': {
        'Nombre': 'Matemáticas',
        'Precio': 200,
        'Información': {
            'Profesor': 'Profesor1',
            'Contacto': 'profesor1@email.com',
            'Alumnos': ['Alumno1', 'Alumno2', 'Alumno3'],
            'Evaluación Promedio': 8.5
        }
    },
    'Curso2': {
        'Nombre': 'Historia',
        'Precio': 150,
        'Información': {
            'Profesor': 'Profesor2',
            'Contacto': 'profesor2@email.com',
            'Alumnos': ['Alumno4', 'Alumno5', 'Alumno6'],
            'Evaluación Promedio': 7.2
        }
    },
}

# Acceso a la información del curso
num_curso = input(
    "Indica qué curso quieres ver (Curso1, Curso2): ").capitalize()
curso = sistema_escolar[num_curso]
print(f'Nombre del curso: {curso["Nombre"]}')
print(f'Precio del curso: ${curso["Precio"]}')
print(f'Profesor del curso: {curso["Información"]["Profesor"]}')
print(f'Contacto del profesor: {curso["Información"]["Contacto"]}')
print(f'Alumnos del curso: {(curso["Información"]["Alumnos"])}')
print(
    f'Evaluación promedio del curso: {curso["Información"]["Evaluación Promedio"]}')
