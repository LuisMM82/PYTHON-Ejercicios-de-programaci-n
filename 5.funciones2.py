# 1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de
# ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros
# mismos es un muy buen ejercicio.

def max(n1, n2):
    if n1 > n2:
        print(n1)
    elif n1 == n2:
        print("Son iguales.")
    else:
        print(n2)


max(2, 5)

# 2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva
# el mayor de ellos.


def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    else:
        print(n3)


max_de_tres(13, 10, 8)


# 3 - Definir una función que calcule la longitud de una lista o una cadena dada.

def longitud(cadena):
    print(len(cadena))


longitud("hola, buenos dias, qué tal?")

# 4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
# contrario devuelve False.


def caracter_true(char):
    if char.lower() in "aeiou":
        print(True)
    else:
        print(False)


caracter_true("E")

# 5 - Escribir una función sum() y una función multip() que sumen y multipliquen
# respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
# devolver 10 y multip([1,2,3,4]) debería devolver 24.


def sum(list):
    total = 0
    for i in list:
        total += i
    print(total)


def multip(list):
    total = 1
    for i in list:
        total *= i
    print(total)


sum([1, 2, 3, 4])
multip([1, 2, 3, 4])

# 6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
# cadena "estoy probando" debería devolver la cadena "odnaborp yotse"


def inversa(cadena):
    cad_inv = cadena[::-1]
    print(cad_inv)


inversa("estoy probando")

# 7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que
# tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría
# que devolver True.


def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        print("Es palíndromo.")
    else:
        print("No es palíndromo.")


es_palindromo("radar")

# 8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al
# menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el
# bucle for anidado.


def superposicion(lista1, lista2):

    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False


print(superposicion([1, 3, 5, 8], [2, 8, 6, 9]))

# 9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
# multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".


def generar_n_caracteres(num, char):
    print(num * char)


generar_n_caracteres(12, "W")

# 10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima
# un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******


def procedimiento(lista):
    for i in lista:
        print(i * "*")


procedimiento([4, 9, 7])
