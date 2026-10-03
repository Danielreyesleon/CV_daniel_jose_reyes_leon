import random

print("daniel jose reyes leon: que el código los acompañe")

vida_jugador = 30
vida_enemigo = 30

while vida_jugador > 0 and vida_enemigo > 0:
    print("\nTu vida:", vida_jugador)
    print("Vida del enemigo:", vida_enemigo)
    
    try:
        print("Elige tu acción:")
        print("1. Atacar")
        print("2. Defender")
        accion = int(input("Ingresa el número de tu acción: "))
        
        if accion == 1:
            daño = random.randint(5, 10)
            vida_enemigo -= daño
            print("¡Atacaste al enemigo y le hiciste", daño, "puntos de daño!")
        elif accion == 2:
            defensa = random.randint(3, 7)
            vida_jugador += defensa
            print("¡Defendiste y recuperaste", defensa, "puntos de vida!")
        else:
            print("Opción inválida. Intenta nuevamente.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
if vida_jugador <= 0:
    print("\n¡Has sido derrotado por el enemigo!")
elif vida_enemigo <= 0:
    print("\n¡Felicidades! Has derrotado al enemigo!")
    
    print("_"*30)
    print("¡Gracias por jugar! Que el código te acompañe.") 
    print("_"*30)
    print("que el codigo te acompañe, hasta la próxima aventura.")