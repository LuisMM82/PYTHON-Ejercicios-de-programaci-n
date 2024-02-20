# Proyecto:

# El proyecto va a ser un pequeño programa de consola que permita al usuario hacer un pedido
# de pizza con ingredientes extra para añadir.

# Requisitos del proyecto:
# Añade un título con un print() para la pizzería, algo como -> Pizzería PF <-.
# El usuario introducirá el dinero que quiera. Guárdalo en una variable.
# Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
# Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
# Cada pizza tendrá un coste diferente.
# El usuario podrá elegir solo una pizza.
# Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
# Se le debe solicitar, si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
# Añade al menos 3 ingredientes extra. El usuario podrá elegir ninguno, uno o varios de estos. No hay límite de ingredientes extra. Si se pasa del dinero que tiene, se le dirá que no le llega y que vuelva a realizar el pedido.
# Las pizzas e ingredientes, tendrán sus precios almacenados en variables o constantes (piensa que los precios son los que son y no deben variar en todo el programa).
# Con cada ingrediente extra, se le debe ir sumando el precio al total y mostrárselo al usuario con el cambio que le queda.
# Si el usuario no quiere ingredientes extra, puede pagar directamente sin añadir ninguno.
# Finalmente, se le debe presentar el ticket (imprimido en la consola) con el total gastado, el cambio y todos los elementos que se han añadido al pedido, pizza, ingredientes extra y precios.
# Título del programa

print('--------->>>> PIZZERÍA ZEUS <<<<------------')

dinero_inicial = float(input("Indica cuánto es su presupuesto (€): "))
dinero = dinero_inicial
pedido = []
costo = 0

Margarita = 5.75
Cuatro_Quesos = 6.25
Peperoni = 7.15

while True:
    print(f'1. Pizza Margarita. Precio: {Margarita} €.')
    print(f'2. Pizza Cuatro Quesos. Precio: {Cuatro_Quesos} €.')
    print(f'3. Pizza Peperoni. Precio: {Peperoni} €.')
    print(f'4. No quiero más.')
    opcion = int(input("Elija qué pizza quiere degustar (1,2,3): "))

    if opcion == 1:
        print('Ha elegido Pizza Margarita.')
        dinero -= Margarita
        costo += Margarita
        print(f'Lleva gastado {costo:.2f} €.\n')
        pedido.append(f'Margarita- {Margarita} €.')

    elif opcion == 2:
        print('Ha elegido Pizza Cuatro Quesos.')
        dinero -= Cuatro_Quesos
        costo += Cuatro_Quesos
        print(f'Lleva gastado {costo:.2f} €.\n')
        pedido.append(f'Cuatro Quesos- {Cuatro_Quesos}')

    elif opcion == 3:
        print('Ha elegido Pizza Peperoni.')
        dinero -= Peperoni
        costo += Peperoni
        print(f'Lleva gastado {costo:.2f} €.\n')
        pedido.append(f'Peperoni- {Peperoni}')

    elif opcion == 4:
        print(f'De acuerdo. Lleva gastado {costo}\n')
        break

    else:
        print('Opción erronea. Vuelva a intentarlo.')


queso = 0.55
atun = 1.15
oregano = 0.30

while True:
    print('\n¿Desea algún ingrediente extra?')
    print(f'1. Queso. Precio: {queso} €')
    print(f'2. Atún. Precio: {atun} €')
    print(f'3. Orégano. Precio: {oregano} €')
    print(f'4. No quiero.')
    opcion2 = int(input('Elija una opción: '))

    if opcion2 == 1:
        print('Ha elegido extra de queso.')
        dinero -= queso
        costo += queso
        print(f'Lleva gastado {costo:.2f} €.')
        print(f'Le queda {dinero:.2f} €.\n')
        pedido.append(f'queso- {queso}')

    elif opcion2 == 2:
        print('Ha elegido atún.')
        dinero -= atun
        costo += atun
        print(f'Lleva gastado {costo:.2f} €.')
        print(f'Le queda {dinero:.2f} €.\n')
        pedido.append(f'atún- {atun}')

    elif opcion2 == 3:
        print('Ha elegido orégano.')
        dinero -= oregano
        costo += oregano
        print(f'Lleva gastado {costo:.2f} €.')
        print(f'Le queda {dinero:.2f} €.\n')
        pedido.append(f'orégano- {oregano}')

    elif opcion2 == 4:
        print('De acuerdo.')
        print(f'Lleva gastado {costo:.2f} €.')
        print(f'Le queda {dinero:.2f} €.\n')
        break

    else:
        print('Opción erronea. Vuelva a intentarlo.')

if dinero_inicial > costo - 0.01:
    print('\nSu pedido se ha realizado exitosamente.')
    for i in pedido:
        print(f'-{i}')

    print(f'\nEl total del pedido es de {costo:.2f}')
    print(f'Le sobra {dinero:.2f} €.\n')
    print('Buen provecho.')
    print('Gracias y vuelva cuando quiera. ;)')

else:
    print('Se ha pasado de su presupuesto.')
    print('Por favor, vuelva a intentarlo. :(')
