import random


numero_secreto = random.randint(1,100) #Entero entre el 1 y el 100
cant_intentos = 0
cant_maxima = 5
adivinado =  False # SI Logra adivinar le asigno True

print("Bienvenida Lulita al juego de adivinar el numero secreto. Tienes 5 intentos")

#Le pido un numero al que va a ingresar, utilizando input, esto trae str hay que cambiarlo a numero
while not adivinado  and cant_intentos < cant_maxima:
    numero = input("Introduce un numero del 1 al 99: ") # TODO: convertir a numero
    numero = int(numero) # Esto lo podria poner directamente con la linea de arriba
    if numero == numero_secreto:
        print("Felicitaciones has adivinado el numero secreto! Te ganaste un batito naranja")
        adivinado =  True #Cambio condicion para cortar el bucle
    elif  numero < numero_secreto:
        print("EL numero es mayor al ingresado")
    else:
        print("EL numero es menor al ingresado")
    cant_intentos +=1
if not cant_intentos < cant_maxima:
    print("GAME OVER. No has podido avidinar dentro de los 10 intentos. Tu batito se transformara en piraña") #Esto lo puedo hacer con un break al ppio tambien



