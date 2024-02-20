# Ejercicio 2
# Pedir la puntuación media de las personas para cada asignatura de un curso a partir de
# un número de personas. Deberás iniciar los cursos para después añadir el número de
# alumnos y pedir las puntuaciones media. Ejemplo del programa resultado:
# Insertar la lista de los nombres de las asignaturas del instituto BigBayData.com
# El usuario introduce: Python,SQL,Hadoop,Js,Html,Css,Swift
# Ahora introduce las puntuaciones uno por uno en Python:
# Introducimos las puntuaciones de los alumnos por cada alumno para cada curso.
# Resultado de las evaluaciones este año:
# [Python, 12 alumnos. Nota media: 7.6, Suspensos: 2]
# [SQL, 12 alumnos. Nota media: 6.9, Suspensos: 1]

listas = []

while True:

    opcion = input("Quiere hacer una lista nueva? (S/N): ")

    if opcion.upper() == "S":
        lista_nueva = []
        asignatura = input("Introduce la asignatura: ")
        lista_nueva.append(asignatura.capitalize())
        alumnos = input("Introduce el número de alumnos: ")
        nota = input("Introduce la nota media: ")
        lista_nueva.append(f"{alumnos} alumnos. Nota media: {nota}")
        suspensos = input("Introduce el número de suspensos: ")
        lista_nueva.append(f"Suspensos: {suspensos}")
        listas.append(lista_nueva)
        print(listas)

    else:
        print(listas)
        break

# Ejercicio 3
# Imagina un sistema de nombres donde queremos identificar el nombre más común. Para ello
# primero pide al usuario que inserte nombres. Utiliza la estructura do-while.
# Introduce los nombres... (-1 para terminar)
# carmen,julia,juan,carmen,carmen,julia
# carmen: 3, julia: 2,juan: 1

nombres = []
while True:
    opcion = input("Quiere introducir otro nombre? (S/N): ")

    if opcion.upper() == "S":
        nombre = input("Introduce un nombre: ")
        nombres.append(nombre.capitalize())
    elif opcion.upper() == "N":
        break
    else:
        continue

# Creamos un conjunto para poder sacar los nombres sin repetir.
nombres_unicos = set(nombres)

for nombre in nombres_unicos:
    cantidad = nombres.count(nombre)
    print(f"{nombre}: {cantidad} veces")

# Ejercicio 4
# Utiliza el ejercicio anterior y modifícalo para, una vez se añaden los usuarios, se
# eliminen los duplicados.

# Pasar el conjunto sin nombres duplicados y convertirlo en lista para poder operarla.
nombres_unicos = list(set(nombres))
nombres_unicos.sort()
# Imprimir la lista de nombres sin repeticiones
print("Nombres sin repeticiones:")
for nombre in nombres_unicos:
    print(nombre)

# Ejercicio 5
# Calcular la tabla de multiplicar de los 20 primeros números dado un número. La lista,
# según su posición, almacenará el resultado de la multiplicación.

num = int(input("Ingresa un número: "))
lista = []

for i in range(num, num + 20):
    for j in range(1, 11):
        tabla = i * j
        lista.append(tabla)
print(lista)

# Ejercicio 6
# Haz un programa que inicialice una lista con los primeros 10 números primos. Después,
# ordenalos de mayor a menor.

primos = []
numero = 2

while len(primos) < 11:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(numero)
    numero += 1
primos.sort(reverse=True)
print(f"Los primeros 10 números primos son: {primos}")

# Ejercicio 7
# Simula una cesta de la compra. Después, una vez tengas la lista de la compra, elimina el
# último elemento. Después, invierte los elementos de la lista y muestra qué queda de
# resultado.
# Pista: Utiliza la función pop()

compra = ['pan', 'leche', 'dulces', 'postres', 'cena', 'cervezas', 'fruta']
compra.pop()
compra.reverse()
print(compra)


# Ejercicio 9
# Imagina construir un sistema de planning de vuelos de un aeropuerto cercano. Crea una
# planificación donde dentro contiene, por día de la semana, horario, compañia,
# duracion_estimada, tipo_avion. Utiliza una lista dentro de otra lista.
# PD: Después de llenar los datos necesitarás ofrecer al usuario ver la información.

planificacion_vuelos = [
    # Lunes
    [
        ["08:00", "Aerolínea A", "2 horas", "Boeing 737"],
        ["12:30", "Aerolínea B", "3 horas", "Airbus A320"],
    ],
    # Martes
    [
        ["09:00", "Aerolínea C", "2 horas", "Boeing 737"],
        ["14:00", "Aerolínea D", "3 horas", "Airbus A320"],
    ],
    # Miércoles
    [
        ["10:00", "Aerolínea E", "2 horas", "Boeing 737"],
        ["16:00", "Aerolínea F", "3 horas", "Airbus A320"],
    ],
    # Jueves
    [
        ["08:30", "Aerolínea A", "2 horas", "Boeing 737"],
        ["13:00", "Aerolínea B", "3 horas", "Airbus A320"],
    ],
    # Viernes
    [
        ["09:30", "Aerolínea C", "2 horas", "Boeing 737"],
        ["15:00", "Aerolínea D", "3 horas", "Airbus A320"],
    ],
    # Sábado
    [
        ["11:00", "Aerolínea E", "2 horas", "Boeing 737"],
        ["17:00", "Aerolínea F", "3 horas", "Airbus A320"],
    ],
    # Domingo
    [
        ["10:30", "Aerolínea A", "2 horas", "Boeing 737"],
        ["14:30", "Aerolínea B", "3 horas", "Airbus A320"],
    ],
]

# Pedir al usuario el día de la semana
dia_semana = int(
    input("Introduce el número de día de la semana (1=Lunes, 2=Martes, etc.): "))

# Validar la entrada del usuario
if dia_semana >= 1 and dia_semana <= 7:
    # Mostrar la planificación de vuelos para el día seleccionado
    print(f"Planificación de vuelos para el día {dia_semana}:")
    vuelos = planificacion_vuelos[dia_semana - 1]
    for i, vuelo in enumerate(vuelos):
        print(f"Vuelo {i + 1}:")
        print(f"Hora: {vuelo[0]}")
        print(f"Compañía: {vuelo[1]}")
        print(f"Duración Estimada: {vuelo[2]}")
        print(f"Tipo de Avión: {vuelo[3]}")

else:
    print("Día no válido. Debe estar en el rango de 1 (Lunes) a 7 (Domingo).")


# Ejercicio 10
# Haz un sistema de ordenamiento de ayudas para tu comunidad. La idea es que insertes
# todos los emails que quieras para, aleatoriamente, ofrecer N ayudas. El objetivo es
# tener un sistema justo de ayudas para repartir entre la ciudadanía que se postula. Una
# vez lo tengas, desarrolla un sistema de envío automático por correo.
