# POKÉMON PROYECT
# Jorge Luis Morales Huertas
# Carné | 1586322
# Introducción a la programación - Segundo proyecto - Primer semestre

# La importación de esta librería dentro de mi código fuente permitirá que pueda ejecutar tiempos de espera que considere adecuados para la impresión de una respuesta"
import time

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
print("¿Cuál es tu nombre nuevo maestro pokémon?")
nombremaestropk = input()
print("¿Estás seguro que ", nombremaestropk," sea tu nombre de entrenador?")
print("1 = si | 2 = No")
opcionnombre = int(input("ingrese su elección: "))
while opcionnombre == 2:
    print("Entendido, entonces cuéntame, ¿Cómo te llamas?")
    nombremaestropk = input("Nombre: ")
    opcionnombre = int(input("¿Estás seguro de tu elección? | 1 = si | 2 = no | "))
    print("-------------------")
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
time.sleep(1)
print("En este mundo, existen muchos pokémon salvajes y por ello debes ir acompañado")
time.sleep(1)
print("It's Dangerous To go Alone, Please take this: ")
time.sleep(1)
print("Selecciona a tu Pokémon Inicial")
time.sleep(1)
print("Bulbasaur | Charmander | Squirtle")
pokemoninicial = str(input("Escribe el nombre del pokémon inicial que deseas: "))
if pokemoninicial == "Bulbasaur":
    print("¿Estás seguro que deseas al pokémon Bulbasaur como tu compañero?")
    opcionpomemon = int(input("1 = SI | 2 = NO "))
    while opcionpomemon == 2:
        print("Trabajo en desarrollo....")
if pokemoninicial == "Charmander":
    print("Fuego")
if pokemoninicial == "Squirtle":
    print("Agua")
