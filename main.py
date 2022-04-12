# POKÉMON PROYECT
# Jorge Luis Morales Huertas
# Carné | 1586322
# Introducción a la programación - Segundo proyecto - Primer semestre

# La importación de esta librería dentro de mi código fuente permitirá que pueda ejecutar tiempos de espera que considere adecuados para la impresión de una respuesta"
import time

#Introducción o bienvenida por parte del programa que le permitirá al usuario conocer la interfaz y objetivo del programa en general
print ("------------- Bienvenido Maestro Pokemon -----------------")
time.sleep(1)
print("Mi nombre es Profesor Jorge y soy el encargado de darte la bienvenida al mundo Pokémon")
time.sleep(1)
input("Presione Enter para continuar...")
time.sleep(0.75)
print("Dentro de este mundo experimentarás un sinnúmero de aventuras junto a tu compañero Pokémon")
time.sleep(1)
input("Presione Enter para continuar...")
time.sleep(0.75)
print("Por favor, ya no hablemos de mi, ahora me interesa conocer al verdadero protagonista de esta historia")
time.sleep(1.5)
# Conocer a fondo al usuario y reconocerlo dentro del programa
print("¿Cuál es tu nombre nuevo maestro pokémon?")
nombremaestropk = input()
print("¿Estás seguro que ",nombremaestropk," sea tu nombre de entrenador?")
print("1 = si | 2 = No")
opcionnombre = int(input("ingrese su elección: "))
while opcionnombre == 2:
    print("Entendido, entonces cuéntame, ¿Cómo te llamas?")
    nombremaestropk = input("Nombre: ")
    opcionnombre = int(input("¿Estás seguro de tu elección? | 1 = si | 2 = no | "))
    print("-------------------")
#Introducción a acciones básicas y predeterminadas (Interacción entre el programa y el usuario para generar un ambiente más ameno)
time.sleep(2)
print("AH!" + " con que es ",nombremaestropk,"!")
time.sleep(1)
print("¡Mucho Gusto", nombremaestropk,"!")
time.sleep(1)
print("He escuchado mucho acerca de ti, pero ya no te haré esperar más, por favor acompáñame.")
time.sleep(0.75)
print("(",nombremaestropk,"y El profesor Jorge caminan hacia el área de trabajo porque el profesor tiene una sorpresa para ti)")
time.sleep(1.5)
print(".")
time.sleep(1.5)
print(".")
time.sleep(1.5)
print(".")
time.sleep(2)
print("(Finalmente llegan al área de trabajo)")
# Esta parte de código hará que el ususario sea capaz de seleccionar a su compañero Pokémon
# y finalmente de esa manera pueda iniciar el procesamiento de datos
time.sleep(1)
print("En este mundo, existen muchos pokémon salvajes y por ello debes ir acompañado")
time.sleep(1.75)
print("It's Dangerous To go Alone, Please take this: ")
time.sleep(1.50)
print("Selecciona a tu Pokémon Inicial")
time.sleep(1.25)
# Procesamiento de datos y selección inicial de Pokémon por medio de estructuras selectivas y ciclos en general.
print("Bulbasaur | Charmander | Squirtle")
pokemoninicial = str(input("Escribe el nombre del pokémon inicial que deseas: "))
if pokemoninicial == "Bulbasaur":
    print("El pokémon seleccionado fue: ",pokemoninicial,", quieres a Bulbasaur como tu acompañante? ")
    print("1 = si | 2 = no")
    opcionpokemon = int(input("ingrese su opción: "))
    if opcionpokemon == 1:
        print("Felicidades, tu compañero pokémon es: ",pokemoninicial,"!")
    if opcionpokemon == 2:
        print("¿Estás seguro de cambiar de pokémon?")
        print("1 = si | 2 = no")
        opcionpk = int(input("Inserte su opción: "))
        if opcionpk == 1:
            print("Sus opciones son: ")
            print("Charmander | Squirtle")
            inicial = input("Ingrese el nombre del pokémon que desea elegir: ")
            print("¡Felicidades, su nuevo compañero es: ",inicial,"!")
        if opcionpk == 2:
            print("Entonces tu compañero seguirá siendo",inicial,"!")
if pokemoninicial == "Charmander":
    print("El pokémon seleccionado fue: ", pokemoninicial, ", quieres a Charmander como tu acompañante? ")
    print("1 = si | 2 = no")
    opcionpokemon = int(input("ingrese su opción: "))
    if opcionpokemon == 1:
        print("Felicidades, tu compañero pokémon es: ", pokemoninicial, "!")
    if opcionpokemon == 2:
        print("¿Estás seguro de cambiar de pokémon?")
        print("1 = si | 2 = no")
        opcionpk = int(input("Inserte su opción: "))
        if opcionpk == 1:
            print("Sus opciones son: ")
            print("Bulbasaur | Squirtle")
            inicial = input("Ingrese el nombre del pokémon que desea elegir: ")
            print("¡Felicidades, su nuevo compañero es: ", inicial, "!")
        if opcionpk == 2:
            print("Entonces tu compañero seguirá siendo", inicial, "!")
if pokemoninicial == "Squirtle":
    print("El pokémon seleccionado fue: ", pokemoninicial, ", quieres a Squirtle como tu acompañante? ")
    print("1 = si | 2 = no")
    opcionpokemon = int(input("ingrese su opción: "))
    if opcionpokemon == 1:
        print("Felicidades, tu compañero pokémon es: ", pokemoninicial, "!")
    if opcionpokemon == 2:
        print("¿Estás seguro de cambiar de pokémon?")
        print("1 = si | 2 = no")
        opcionpk = int(input("Inserte su opción: "))
        if opcionpk == 1:
            print("Sus opciones son: ")
            print("Bulbasaur | Charmander ")
            inicial = input("Ingrese el nombre del pokémon que desea elegir: ")
            print("¡Felicidades, su nuevo compañero es: ", inicial, "!")
        if opcionpk == 2:
            print("Entonces tu compañero seguirá siendo", inicial, "!")
if pokemoninicial != "Charmander" and pokemoninicial != "Squirtle" and pokemoninicial != "Bulbasaur":
    print("El valor ingresado es inválido, se procederá a finalizar el programa")
    exit()