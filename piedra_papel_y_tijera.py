#Juego en Python para dos personas con el piedra papel y tijera

Nombre1 = input("Como se llama el jugador 1?: ")
Nombre2 = input("Como se llama el jugador 2?: ")

#Se puede hacer todo upercase o lowercase para que si escriben con mayusculas o minusculas no la caguen
#Con un bucle while hay que hacer varios turnos

jugador1 = input("Hola Jugador 1 que eliges, piedra, papel o tijera?: ")

if jugador1 == "piedra" or jugador1 == "papel" or jugador1 == "tijera":
    print("Bien elegido")
else:
    jugador1 = input("Error de sintaxis, vuelve a elegir.Piedra, papel o tijera?:  ")


jugador2 = input("Hola Jugador 2 que eliges, piedra, papel o tijera?: ")
jugador1 = jugador1.lower()
jugador2 = jugador2.lower()

print(jugador1)
print(jugador2)

#Refactorizacion del codgio, poniendo las condiciones antes en vez del bucle para no extenderlo
condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado:", Nombre1)
else: #(jugador2 == "piedra" and jugador1 == "tijeras") or (jugador2 == "papel" and jugador1 == "piedra") or (jugador2 == "tijera" and jugador1 == "papel"):
    print("Ha ganado:", Nombre2)
