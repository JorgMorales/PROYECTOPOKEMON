# POKÉMON PROYECT
# Jorge Luis Morales Huertas
# Carné | 1586322
# Introducción a la programación - Segundo proyecto - Primer semestre

# La importación de esta librería dentro de mi código fuente permitirá que pueda ejecutar tiempos de espera que considere adecuados para la impresión de una respuesta"
import time
import random

#Función que me ayuda a establecer los movimientos que el Pokémon Tendrá posteriormente

movimientos = ("Látigo cepa","Latigazo","Rayo solar","Ascuas","Lanzallamas","Puño fuego","Hidrobomba","Pistola agua","Rayo burbujas","Chupa vidas","Pin misil","Tijera X","Picotazo","Pico taladro","Tornado","Agarre","Ataque rápido","Bomba huevo","Ácido","Picotazo venenoso","Residuos","Pueño trueno","Trueno","Rayo","Hueso palo","Huesomerang","Terremoto","Come sueños","Bola neblina","Resplandor")

def mov():
    primermovimiento = (random.sample(movimientos, 1))
    segundomovimiento = (random.sample(movimientos, 1))
    print("Primer movimiento: ", primermovimiento)
    print("Segundo movimiento: ", segundomovimiento)

def stats():
    ataquepk = random.randint(1,15)
    defensa = random.randint(1,15)
    velocidad = random.randint(1,15)
    ps = random.randint(1,15)

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
        tipo = "Planta"
    if opcionpokemon == 2:
        print("¿Estás seguro de cambiar de pokémon?")
        print("1 = si | 2 = no")
        opcionpk = int(input("Inserte su opción: "))
        if opcionpk == 1:
            print("Sus opciones son: ")
            print("Charmander | Squirtle")
            pokemoninicial = input("Ingrese el nombre del pokémon que desea elegir: ")
            print("¡Felicidades, su nuevo compañero es: ",pokemoninicial,"!")
            if pokemoninicial == "Squirtle":
                tipo = "Agua"
            if pokemoninicial == "Charmander":
                tipo = "Fuego"
        if opcionpk == 2:
            print("Entonces tu compañero seguirá siendo",pokemoninicial,"!")
            tipo = "Planta"
if pokemoninicial == "Charmander":
    print("El pokémon seleccionado fue: ", pokemoninicial, ", quieres a Charmander como tu acompañante? ")
    print("1 = si | 2 = no")
    opcionpokemon = int(input("ingrese su opción: "))
    if opcionpokemon == 1:
        print("Felicidades, tu compañero pokémon es: ", pokemoninicial, "!")
        tipo = "Fuego"
    if opcionpokemon == 2:
        print("¿Estás seguro de cambiar de pokémon?")
        print("1 = si | 2 = no")
        opcionpk = int(input("Inserte su opción: "))
        if opcionpk == 1:
            print("Sus opciones son: ")
            print("Bulbasaur | Squirtle")
            pokemoninicial = input("Ingrese el nombre del pokémon que desea elegir: ")
            if pokemoninicial == "Bulbasaur":
                tipo = "planta"
            if pokemoninicial == "Squirtle":
                tipo = "Agua"
            print("¡Felicidades, su nuevo compañero es: ", pokemoninicial, "!")
        if opcionpk == 2:
            print("Entonces tu compañero seguirá siendo", pokemoninicial, "!")
            tipo = "Fuego"
if pokemoninicial == "Squirtle":
    print("El pokémon seleccionado fue: ", pokemoninicial, ", quieres a Squirtle como tu acompañante? ")
    print("1 = si | 2 = no")
    opcionpokemon = int(input("ingrese su opción: "))
    if opcionpokemon == 1:
        print("Felicidades, tu compañero pokémon es: ", pokemoninicial, "!")
        tipo = "Agua"
    if opcionpokemon == 2:
        print("¿Estás seguro de cambiar de pokémon?")
        print("1 = si | 2 = no")
        opcionpk = int(input("Inserte su opción: "))
        if opcionpk == 1:
            print("Sus opciones son: ")
            print("Bulbasaur | Charmander ")
            pokemoninicial = input("Ingrese el nombre del pokémon que desea elegir: ")
            print("¡Felicidades, su nuevo compañero es: ", pokemoninicial, "!")
            if pokemoninicial == "Bulbasaur":
                tipo = "Planta"
            if pokemoninicial == "Charmander":
                tipo = "Fuego"
        if opcionpk == 2:
            print("Entonces tu compañero seguirá siendo", pokemoninicial, "!")
            tipo = "Agua"
if pokemoninicial != "Charmander" and pokemoninicial != "Squirtle" and pokemoninicial != "Bulbasaur":
    print("Parece que ese Pokémon no se encuentra registrado en los iniciales o no existe en la Pokedex, se procederá a finalizar el programa")
    exit()
#La siguiente parte se encarga de la asignación de emote al pokemon seleccionado anteriormente
emote = str(input("Por favor asígnele un nuevo apodo a su compañero Pokémon: "))
print("Tu compañero Pokémon ",pokemoninicial," recibió el emote: ",emote)
lvlpkinicial = 5
xpinicial = 0
i = 0
c = 0
#función que me permite definir los movimientos del compañero
print("-------------------")
print("-------------------")
print("----------MENÚ PRINCIPAL----------")
print(" 1) Chequeo de estadísticas ")
print(" 2) Batalla contra Pokémon ")
print(" 3) Salir del videojuego")
opcionmenu = int(input("Ingrese la opción que desee: "))
while opcionmenu > 0 and opcionmenu<3:
    print(" ")
    print("CHEQUEO DE ESTADÍSTICAS")
    print("-----------------------")
    print(" ")
    print("Dato | Descripción ")
    A1 = ["Nombre", "Apodo", "Nivel", "Experiencia", "Tipo", "Movimientos"]
    A2 = [pokemoninicial, emote, lvlpkinicial, xpinicial,tipo, mov()]
    for i in range(i, 6):
        print(A1[i], " : ", A2[c])
        i = i + 1
        c = c + 1
    print("-------------------")
    print("Cinta de opciones")
    print("1) Regresar al menú")
    print("2) Salir del programa")
    opcionmenu2 = int(input())
    if opcionmenu2 == 1:
        print("-------------------")
        print("----------MENÚ PRINCIPAL----------")
        print(" 1) Chequeo de estadísticas ")
        print(" 2) Batalla contra Pokémon ")
        print(" 3) Salir del videojuego")
        opcionmenu = int(input("Ingrese la opción que desee: "))
    if opcionmenu2 == 2:
        print("Se seleccionó")
while opcionmenu > 0 and opcionmenu<3:
    print("opcion 2")
if opcionmenu == 3:
    print("Gracias por usar el programa Entrenador ",nombremaestropk)