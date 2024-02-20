# Ejercicio 1
# Imprimir los números del 1 al 10.

for i in range(1, 11):
    print(i)

# Ejercicio 2
# Calcular el factorial de un número.
num = 5
for i in range(1, num+1):
    resultado = (i * num)
    print(resultado * num)

# Ejercicio 3
# Partiendo de una frase imprimir palabra por palabra y un contador de palabras totales.
frase = "Hola buenos dias, cómo estás? Espero que bien."
contador = 0
for char in frase:
    contador += 1
    print(char)
print(contador)


# Ejercicio 4
# Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos.
lista = []
x = 0
y = 1
z = 0
for num in range(0, 10):
    z = x+y
    x = y
    y = z
    lista.append(z)
print("0, 1,", lista)


# Ejercicio 5
# Crea un algoritmo que dibuje un árbol dado un número, asumiendo que n >1. Para n = 3:
# *
# **
# ***

for i in range(1, 4):
    print(i * "*")


# Ejercicio 6
# Escribir el sumatorio de los números que se quiera hasta ingresar -1.

total = 0
num = int(input("Introduce un número: "))
total += num
while True:
    n = int(input("Introduce número para sumar. Para parar marque -1: "))
    if n == -1:
        print("La suma ha finalizado.")
        break
    else:
        total += n
        print(total)

# Ejercicio 7
# Tenemos la pantalla del móvil bloqueada. Partiendo de un PIN_SECRETO, intentaremos
# desbloquear la pantalla. Tenemos hasta 3 intentos. Simula el proceso con Python.
# En caso de acceder, lanza al usuario 'login correcto'. Sino, 'llamando al policía'.
pin_secreto = 1234
i = 0

while i < 3:
    pin = int(input('Inserta el Pin: '))
    if pin == pin_secreto:
        print("login correcto.")
        break

    else:
        print('ERROR. Sigue intentando insertar el PIN… Te quedan ',
              2 - i, 'intentos.')
    i += 1
else:
    print('Has superado los 3 intentos. Llamando a policia…')
