# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el
# resultado de aplicar la función dada a cada uno de los elementos de la lista.

def aplica_funcion_lista(funcion, lista):
    '''Función que aplica una función a todos los elementos de una lista.

    Parámetros:
        funcion: Es una función.
        lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    '''
    lista1 = []
    for i in lista:
        lista1.append(funcion(i))
    return lista1


def cuadrado(n):
    return n * n


print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4, 125]))


""" Escribir una función que reciba otra función booleana y una lista, y devuelva
 otra lista con los elementos de la lista que devuelvan True al aplicarles la
 función booleana."""


def filtra_lista(funcion, lista):
    '''Función que filtra los elementos de una lista que devuelven true al aplicarle una función booleana.

    Parámetros:
        - funcion: Es una función booleana (devuleve true o false)
        - lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con los elementos de la lista que devuelven true al aplicarles la función booleana.
    '''
    lista2 = []
    for i in lista:
        if funcion(i):
            lista2.append(i)
    return lista2


def par(n):
    return n % 2 == 0  # <----- True.


print(filtra_lista(par, [1, 2, 3, 4, 5, 6, 100]))
