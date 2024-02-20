# EJERCICIO 1:
# Imaginemos que en nuestra tienda hay un carné por puntos y que alguien debe pagar el
# precio_final_de_compra. Si tienes menos de 100 puntos realizaremos un descuento del 10%.
# Si es mayor a 100 y menor a 150 aplicamos un 12%. Si tienes 150 un 15% y sino, el resto
# de los casos de más de 150, un 20%. ¡Crea la variable puntos y juega con ella.

'''precio = float(input("Indique el precio de la compra: "))
puntos = int(input("Indique los puntos que tiene: "))

if puntos < 100:
    precio_final = precio - precio * 10/100
elif puntos > 99 and puntos < 150:
    precio_final = precio - precio * 12/100
elif puntos == 150:
    precio_final = precio - precio * 15/100
else:
    precio_final = precio - precio * 20/100

print(f"El precio final descontando los puntos es de: {precio_final:.2f}")'''


# Ejercicio 2:
# Calcula sabiendo el valor de una factura cuanto será el precio final para el cliente,
# sabiendo que por norma general, el IVA aplicado es de un 21%. Sin embargo, en
# restaurantes es el 10%.
# Calcular el precio final según IVA aplicado. Pista: Pide al usuario que tipo de factura es.

'''factura = 2000
tipo_factura = input(
    "Indica de qué comercio es la factura (textil, juguetes, gastronomia...: ")

if tipo_factura.lower() == "gastronomia":
    factura_final = factura + factura * 10/100
else:
    factura_final = factura + factura * 21/100
print(f"Su factura final es de {factura_final}")
'''
# Ejercicio 3:
# Guarda una contraseña como password. Crea un sistema de seguridad donde el ordenador
# muestra un mensaje 'Ordenador bloqueado. Contraseña incorrecta.' si el usuario falla la
# contraseña. En caso contrario, que muestre por pantalla 'Bienvenid@...'.

'''password = "Ay oma"
contraseña = input("Ingrese la contraseña: ")
if contraseña == password:
    print("Bienvenid@, puedes usar el ordenador.")
else:
    print("Ordenador bloqueado. Contraseña incorrecta.")'''

# Ejercicio 4:
# Partiendo de la tarifa anual (que puede cambiar), nos piden que debemos calcular el
# precio de la tarifa de nuestro polideportivo, sabiendo las siguientes condiciones:
# Criterio 1: Si es mayor de edad y está trabajando -> Paga el 100%
# Criterio 2: Si es menor de edad y está trabajando -> Paga el 95%
# Criterio 3: Si es mayor de edad y no está trabajando -> Paga el 75%
# Criterio 4: Si es menor de edad y no está trabajando -> Paga el 50%

'''tarifa = float(input("Introduce el precio de la tarifa anual actual: "))
edad = int(input("¿Cuántos años tienes?: "))
trabajo = input("¿Estás trabajando?(s/n): ").lower()

if edad >= 18 and trabajo == "s":
    print(f"Tienes que pagar {tarifa} €.")
elif edad < 18 and trabajo == "s":
    tarifa_descuento = tarifa * 95/100
    print(f"Tienes que pagar {tarifa_descuento} €.")
elif edad >= 18 and trabajo == "n":
    tarifa_descuento = tarifa * 75/100
    print(f"Tienes que pagar {tarifa_descuento} €.")
elif edad < 18 and trabajo == "n":
    tarifa_descuento = tarifa * 50/100
    print(f"Tienes que pagar {tarifa_descuento} €.")
else:
    print("Error. Opción no válida.")'''

# Ejercicio 5:
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no y en
# función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.

# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en
# todas la pizzas.

# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos
# los ingredientes que lleva.

print("############# PIZZERÍA BELLA NAPOLI #############\n\n")
pizza = int(
    input("¿Indica el número de la pizza que desea (1. Vegerariana, 2. Normal): "))

if pizza == 1:
    pizza = "Pizza Vegetariana"
    print(f"Ha elegido {pizza}.\nSu pizza contiene mozzarella y tomate.")
    ingrediente = int(input(
        "Indica si quiere un ingrediente extra (1. Pimiento, 2. Tofu, 3. Ninguno): "))
    if ingrediente == 1:
        ingrediente = "Pimiento"
        print(f"Ha elegido {ingrediente}.\n")
    elif ingrediente == 2:
        ingrediente = "Tofu"
        print(f"Ha elegido {ingrediente}.\n")
    elif ingrediente == 3:
        ingrediente = "nada"
        print("No ha elegido ningún ingrediente extra.\n")
    else:
        print("El número indicado no es una opción. Vuelva a intentarlo.")
    print(
        f"Ha elegido {pizza} con {ingrediente}. Muchas gracias y vuelva cuando quiera.")
elif pizza == 2:
    pizza = "Pizza Normal"
    print(f"Ha elegido {pizza}.\nSu pizza contiene mozzarella y tomate.")
    ingrediente = int(input(
        "Indica si quiere un ingrediente extra (1. Peperoni, 2. Jamón, 3. Salmón, 4. Ninguno): "))
    if ingrediente == 1:
        ingrediente = "Peperoni"
        print(f"Ha elegido {ingrediente}.\n")
    elif ingrediente == 2:
        ingrediente = "Jamón"
        print(f"Ha elegido {ingrediente}.\n")
    elif ingrediente == 3:
        ingrediente = "Salmón"
        print(f"Ha elegido {ingrediente}.\n")
    elif ingrediente == 4:
        ingrediente = "nada"
        print("No ha elegido ningún ingrediente extra.\n")
    else:
        print("El número indicado no es una opción. Vuelva a intentarlo.")
    print(
        f"Ha elegido {pizza} con {ingrediente}. Muchas gracias y vuelva cuando quiera")
else:
    print("El número indicado no es una opción. Vuelva a intentarlo.")
