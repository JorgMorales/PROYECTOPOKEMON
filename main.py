# POKÉMON PROYECT
# Jorge Luis Morales Huertas
# Carné | 1586322
# Introducción a la programación - Segundo proyecto - Primer semestre

# La importación de esta librería dentro de mi código fuente permitirá que pueda ejecutar tiempos de espera que considere adecuados para la impresión de una respuesta"
import time
import random

#Función que me ayuda a establecer los movimientos que el Pokémon Tendrá posteriormente

#Espacio de desarrollo para Pokémon Salvajes
experienciapokemoninicial = 0
lvlpokemoninicial = 5
nivelpoksalvaje = ((lvlpokemoninicial-4),(lvlpokemoninicial+4))
lvlsalvaje = (random.sample(nivelpoksalvaje,1))

Bulbasaur = {
    "Nombre" : "Bulbasaur",
    "Tipo" : "Planta",
    "LVL" : lvlsalvaje,
    "HP" : 45,
    "ATK" : 49,
    "DEF" : 49,
    "VEL" : 45,
    "XPBS" : 64
}

Charmander = {
    "Nombre" : "Charmander",
    "Tipo" : "Fuego",
    "LVL" : lvlsalvaje,
    "HP" : 39,
    "ATK" : 52,
    "DEF" : 43,
    "VEL" : 65,
    "XPBS" : 65
}

Squirtle = {
    "Nombre" : "Squirtle",
    "Tipo" : "Agua",
    "LVL" : lvlsalvaje,
    "HP" : 39,
    "ATK" : 52,
    "DEF" : 43,
    "VEL" : 65,
    "XPBS" : 65
}

Caterpie = {
    "Nombre" : "Caterpie",
    "Tipo" : "Bicho",
    "LVL": lvlsalvaje,
    "HP" : 45,
    "ATK" : 30,
    "DEF" : 35,
    "VEL" : 45,
    "XPBS" : 53
}

Weedle = {
    "Nombre" : "Weedle",
    "Tipo" : "Bicho",
    "LVL": lvlsalvaje,
    "HP" : 40,
    "ATK" : 35,
    "DEF" : 30,
    "VEL" : 50,
    "XPBS" : 52
}

Pidgey = {
    "Nombre" : "Pidgey",
    "Tipo" : "Volador",
    "LVL": lvlsalvaje,
    "HP" : 40,
    "ATK" : 45,
    "DEF" : 40,
    "VEL" : 56,
    "XPBS" : 55
}

Rattata = {
    "Nombre" : "Rattata",
    "Tipo" : "Normal",
    "LVL": lvlsalvaje,
    "HP" : 30,
    "ATK" : 56,
    "DEF" : 35,
    "VEL" : 72,
    "XPBS" : 57
}

Pidgey = {
    "Nombre" : "Pidgey",
    "Tipo" : "Volador",
    "LVL": lvlsalvaje,
    "HP" : 40,
    "ATK" : 45,
    "DEF" : 40,
    "VEL" : 56,
    "XPBS" : 55
}

Spearow = {
    "Nombre" : "Spearow",
    "Tipo" : "Volador",
    "LVL": lvlsalvaje,
    "HP" : 40,
    "ATK" : 60,
    "DEF" : 30,
    "VEL" : 70,
    "XPBS" : 58
}

Ekans = {
    "Nombre" : "Ekans",
    "Tipo" : "Volador",
    "LVL": lvlsalvaje,
    "HP" : 40,
    "ATK" : 45,
    "DEF" : 40,
    "VEL" : 56,
    "XPBS" : 55
}

Pikachu = {
    "Nombre" : "Pikachu",
    "Tipo" : "Eléctrico",
    "LVL": lvlsalvaje,
    "HP" : 35,
    "ATK" : 55,
    "DEF" : 40,
    "VEL" : 90,
    "XPBS" : 82
}

Sandshrew = {
    "Nombre" : "Sandshrew",
    "Tipo" : "Tierra",
    "LVL": lvlsalvaje,
    "HP" : 50,
    "ATK" : 75,
    "DEF" : 85,
    "VEL" : 40,
    "XPBS" : 93
}

Vulpix = {
    "Nombre" : "Vulpix",
    "Tipo" : "Fuego",
    "LVL": lvlsalvaje,
    "HP" : 38,
    "ATK" : 41,
    "DEF" : 40,
    "VEL" : 65,
    "XPBS" : 63
}

Jigglypuff = {
    "Nombre" : "Jigglypuff",
    "Tipo" : "Normal",
    "LVL": lvlsalvaje,
    "HP" : 115,
    "ATK" : 45,
    "DEF" : 20,
    "VEL" : 20,
    "XPBS" : 76
}

Zubat = {
    "Nombre" : "Zubat",
    "Tipo" : "Veneno",
    "LVL": lvlsalvaje,
    "HP" : 40,
    "ATK" : 45,
    "DEF" : 35,
    "VEL" : 55,
    "XPBS" : 54
}

Oddish = {
    "Nombre" : "Oddish",
    "Tipo" : "Planta",
    "LVL": lvlsalvaje,
    "HP" : 45,
    "ATK" : 50,
    "DEF" : 55,
    "VEL" : 30,
    "XPBS" : 78
}

Gloom = {
    "Nombre" : "Gloom",
    "Tipo" : "Planta",
    "LVL": lvlsalvaje,
    "HP" : 60,
    "ATK" : 65,
    "DEF" : 70,
    "VEL" : 40,
    "XPBS" : 132
}

Diglett = {
    "Nombre" : "Diglett",
    "Tipo" : "Tierra",
    "LVL": lvlsalvaje,
    "HP" : 10,
    "ATK" : 55,
    "DEF" : 25,
    "VEL" : 95,
    "XPBS" : 81
}

Meowth = {
    "Nombre" : "Meowth",
    "Tipo" : "Normal",
    "LVL": lvlsalvaje,
    "HP" : 40,
    "ATK" : 45,
    "DEF" : 35,
    "VEL" : 90,
    "XPBS" : 69
}

Psyduck = {
    "Nombre" : "Psyduck",
    "Tipo" : "Agua",
    "LVL": lvlsalvaje,
    "HP" : 50,
    "ATK" : 52,
    "DEF" : 48,
    "VEL" : 55,
    "XPBS" : 80
}

Mewtwo = {
    "Nombre" : "Mewtwo",
    "Tipo" : "Psíquico",
    "LVL": lvlsalvaje,
    "HP" : 106,
    "ATK" : 110,
    "DEF" : 90,
    "VEL" : 130,
    "XPBS" : 220
}

def poksalvaje():
    print("")

def mov():
    primermovimiento = (random.sample(movimientos, 1))
    print("Primer movimiento: ", primermovimiento)
    return primermovimiento

def mov1():
    segundomovimiento = (random.sample(movimientos, 1))
    print("Segundo movimiento: ", segundomovimiento)
    return segundomovimiento

def stats():
    ataquepk = random.randint(1,15)
    defensa = random.randint(1,15)
    velocidad = random.randint(1,15)
    ps = random.randint(1,15)

Latigo_cepa = {
    "Nombre" : "Látigo cepa",
    "Tipo" : "Planta",
    "Potencia" : 35,
    "Precisión" : 100
}

Latigazo = {
    "Nombre" : "Latigazo",
    "Tipo" : "Planta",
    "Potencia" : 120,
    "Precisión" : 85
}

Rayo_Solar = {
    "Nombre" : "Rayo Solar",
    "Tipo" : "Planta",
    "Potencia" : 120,
    "Precisión" : 100
}

Ascuas = {
    "Nombre" : "Ascuas",
    "Tipo" : "Fuego",
    "Potencia" : 40,
    "Precisión" : 100
}

Lanzallamas = {
    "Nombre" : "Lanzallamas",
    "Tipo" : "Fuego",
    "Potencia" : 90,
    "Precisión" : 100
}

Puño_fuego = {
    "Nombre" : "Puño fuego",
    "Tipo" : "Fuego",
    "Potencia" : 75,
    "Precisión" : 100
}

Hidrobomba = {
    "Nombre" : "Hidrobomba",
    "Tipo" : "Agua",
    "Potencia" : 120,
    "Precisión" : 80
}

Pistola_agua = {
    "Nombre" : "Pistola agua",
    "Tipo" : "Agua",
    "Potencia" : 40,
    "Precisión" : 100
}

Rayo_burbuja = {
    "Nombre" : "Rayo burbuja",
    "Tipo" : "Agua",
    "Potencia" : 65,
    "Precisión" : 100
}

Chupa_vidas = {
    "Nombre" : "Chupa Vidas",
    "Tipo" : "Bicho",
    "Potencia" : 20,
    "Precisión" : 100
}

Pin_misil = {
    "Nombre" : "Pin Misil",
    "Tipo" : "Bicho",
    "Potencia" : 14,
    "Precisión" : 85
}

Tijera_X = {
    "Nombre" : "Tijera X",
    "Tipo" : "Planta",
    "Potencia" : 80,
    "Precisión" : 100
}

Picotazo = {
    "Nombre" : "Picotazo",
    "Tipo" : "Volar",
    "Potencia" : 35,
    "Precisión" : 100
}

Pico_taladro = {
    "Nombre" : "Pico taladro",
    "Tipo" : "Volador",
    "Potencia" : 35,
    "Precisión" : 100
}

Tornado = {
    "Nombre" : "Tornado",
    "Tipo" : "Volador",
    "Potencia" : 40,
    "Precisión" : 100
}

Agarre = {
    "Nombre" : "Agarre",
    "Tipo" : "Normal",
    "Potencia" : 55,
    "Precisión" : 100
}

Ataque_rapido = {
    "Nombre" : "Ataque Rápido",
    "Tipo" : "Normal",
    "Potencia" : 40,
    "Precisión" : 100
}

Agarre = {
    "Nombre" : "Agarre",
    "Tipo" : "Normal",
    "Potencia" : 55,
    "Precisión" : 100
}

Bomba_huevo= {
    "Nombre" : "Bomba",
    "Tipo" : "Normal",
    "Potencia" : 100,
    "Precisión" : 75
}

Acido = {
    "Nombre" : "Ácido",
    "Tipo" : "Veneno",
    "Potencia" : 40,
    "Precisión" : 100
}

Picotazo_venenoso = {
    "Nombre" : "Picotazo Venenoso",
    "Tipo" : "Veneno",
    "Potencia" : 55,
    "Precisión" : 100
}

Residuos = {
    "Nombre" : "Residuos",
    "Tipo" : "Veneno",
    "Potencia" : 65,
    "Precisión" : 100
}

Puño_trueno = {
    "Nombre" : "Puño Trueno",
    "Tipo" : "Eléctrico",
    "Potencia" : 75,
    "Precisión" : 100
}

Trueno = {
    "Nombre" : "Trueno",
    "Tipo" : "Eléctrico",
    "Potencia" : 120,
    "Precisión" : 70
}

Rayo = {
    "Nombre" : "Rayo",
    "Tipo" : "Eléctrico",
    "Potencia" : 95,
    "Precisión" : 100
}

Hueso_Palo = {
    "Nombre" : "Hueso Palo",
    "Tipo" : "Tierra",
    "Potencia" : 65,
    "Precisión" : 85
}

Huesomerang = {
    "Nombre" : "Huesomerang",
    "Tipo" : "Tierra",
    "Potencia" : 50,
    "Precisión" : 90
}

Terremoto = {
    "Nombre" : "Terremoto",
    "Tipo" : "Tierra",
    "Potencia" : 100,
    "Precisión" : 100
}

Come_sueños = {
    "Nombre" : "Come Sueños",
    "Tipo" : "Psíquico",
    "Potencia" : 100,
    "Precisión" : 100
}

Bola_neblina = {
    "Nombre" : "Bola Neblina",
    "Tipo" : "Psíquico",
    "Potencia" : 70,
    "Precisión" : 100
}

Resplandor = {
    "Nombre" : "Resplandor",
    "Tipo" : "Psíquico",
    "Potencia" : 70,
    "Precisión" : 100
}

Pokemon = (Bulbasaur,Charmander,Squirtle,Caterpie,Weedle,Pidgey,Rattata,Spearow,Ekans,Pikachu,Sandshrew,Vulpix,Jigglypuff,Zubat,Oddish,Gloom,Diglett,Meowth,Psyduck,Mewtwo)
movimientos = (Latigo_cepa,Latigazo,Rayo_Solar,Ascuas,Lanzallamas,Puño_fuego,Hidrobomba,Pistola_agua,Rayo_burbuja,Chupa_vidas,Pin_misil,Tijera_X,Picotazo,Pico_taladro,Tornado,Agarre,Ataque_rapido,Bomba_huevo,Acido,Picotazo_venenoso,Residuos,Puño_trueno,Trueno,Rayo,Hueso_Palo,Huesomerang,Terremoto,Come_sueños,Bola_neblina,Resplandor)


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
while opcionmenu != 3:
    if opcionmenu == 1:
        print("----------------")
        print("Chequeo de estadísticas")
