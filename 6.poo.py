# Ejercicio 1
# Escribir una clase en python que convierta un número entero a número romano

class Entero_romano:
    def __init__(self, num):
        self.num = num

    def entero_a_romano(self):

        numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        n_romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                     'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        numeral = ""
        i = 0

        while self.num > 0:
            for _ in range(self.num // numeros[i]):
                numeral += n_romanos[i]
                self.num -= numeros[i]
            i += 1

        return numeral


nume = Entero_romano(11749)
print(nume.entero_a_romano())


# Ejercicio 2
# Escribir una clase en python que convierta un número romano en un número entero

class Romanos_entero:
    def __init__(self, romano):
        self.romano = romano

    def romano_a_entero(self):

        dic_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'C': 100, 'D': 500, 'M': 1000}
        entero = 0

        for i in range(len(self.romano)):
            if i > 0 and dic_romanos[self.romano[i]] > dic_romanos[self.romano[i - 1]]:
                entero += dic_romanos[self.romano[i]] - \
                    2 * dic_romanos[self.romano[i - 1]]

            else:
                entero += dic_romanos[self.romano[i]]

        return entero


n_rom = Romanos_entero('MMMMMMMMMMMDCCXLIX')
print(n_rom.romano_a_entero())


# Ejercicio 3
# Escribir una clase en python para encontrar la validez de una cadena de paréntesis,
# '(', ')', '{', '}', '['  ']. Los paréntesis deben aparecer en el orden correcto, por
# ejemplo "()" y "()[]{}" son validos, pero "[)", "({[)]" y "{{{" son inválidos.

class Parentesis:

    def __init__(self, cadena):
        self.cadena = cadena

    def ordenar_cadena(self):
        dicc = {'pa': '(', 'pc': ')',
                'ca': '[', 'cc': ']', 'la': '{', 'lc': '}'}
        lista = []
        for i in self.cadena:
            for j in dicc:
                if i == dicc[j]:
                    lista.append(i)

        lista.sort()
        print("".join(lista))


caden = Parentesis(']{)}[(')
caden.ordenar_cadena()
ca = Parentesis('[}{]')
ca.ordenar_cadena()

# Ejercicio 4
# Escribir una clase en python que obtenga todos los posibles subconjuntos únicos de un
# conjunto de números enteros distintos.
# Entrada: [4, 5, 6]
# Salida: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

# SOLUCIONADO CON FUNCIONES, NO CON CLASES.


def subconjuntos(numeros):
    return dev_subconjuntos([], sorted(numeros))


def dev_subconjuntos(actual, conjunto):

    if conjunto:
        return dev_subconjuntos(actual, conjunto[1:]) + dev_subconjuntos(actual + [conjunto[0]], conjunto[1:])
    return [actual]


numeros = [4, 5, 6]
resultados = subconjuntos(numeros)
print(resultados)
print(type(resultados))


# Ejercicio 7
# Escribir una clase en python que calcule pow(x, n)
# x = es la base
# n = es el exponente
# Entrada: pow(2, -3)
# Salida: 0.125
# Entrada: pow(3, 5)
# Salida: 243


class Pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def ejecutar(self):
        print(pow(self.x, self.n))


numero = Pow(2, -3)
numero.ejecutar()


# Ejercicio 8
# Escribir una clase en python que revierta una cadena de palabras
# Entrada: "Mi Diario Python"
# Salida: "Python Diario Mi"

class Revierte_cadena:
    def __init__(self, cadena):
        self.cadena = cadena.split()

    def ejecuta(self):
        print(" ".join(self.cadena[::-1]))


cadena = Revierte_cadena("Mi Diario Python")
cadena.ejecuta()


# Ejercicio 9
# Escribir una clase en python con 2 métodos: get_string y print_string. get_string acepta una
# cadena ingresada por el usuario y print_string imprime la cadena en mayúsculas.
class String():
    def __init__(self):
        self.stri = ""

    def get_String(self):
        self.stri = input("Escribe la cadena: ")

    def print_String(self):
        print(self.stri.upper())


stri = String()
stri.get_String()
stri.print_String()
