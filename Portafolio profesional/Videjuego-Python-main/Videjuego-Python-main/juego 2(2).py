print("="*60)
print("codigo de Paula, Victor y Daniel.J")
print("="*60)

print("="*60)
print("Bienvenido al juego de 21 con mazo real!")
print("Reglas: El objetivo es acercarse lo más posible a 21 sin pasarse. Las cartas del 1 al 11 valen su valor,")
print("Puedes jugar contra la máquina o contra otro jugador. ¡Buena suerte!")
print("="*60)
print("Iniciando el juego...")
print("="*60)


import random

mazo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def repartir_carta():
    if len(mazo) > 0:
        # 1. Elegimos una carta al azar de la lista actual
        carta_seleccionada = random.choice(mazo)
        
        # 2. Eliminamos esa carta específica de la lista para que no se repita
        mazo.remove(carta_seleccionada)
        
        return carta_seleccionada
    else:
        print("No quedan cartas en el mazo.")
        return 0

def revelar_resultado(nombre1, puntos1, nombre2, puntos2):
    print("\n--- EL GANADOR . . . ---")
    print(f"{nombre1} termino con: {puntos1}")
    print(f"{nombre2} termino con: {puntos2}")
    
    if puntos1 > 21 and puntos2 > 21:
        print("Ambos se pasaron. ¡Empate tecnico!")
    elif puntos1 > 21:
        print(f"¡{nombre1} se paso! Gana {nombre2}")
    elif puntos2 > 21:
        print(f"¡{nombre2} se paso! Gana {nombre1}")
    elif puntos1 > puntos2:
        print(f"¡Gana {nombre1} por mayor puntaje!")
    elif puntos2 > puntos1:
        print(f"¡Gana {nombre2} por mayor puntaje!")
    else:
        print("¡Es un empate!")

def jugar_21():
    print("--- BIENVENIDO AL JUEGO DE 21 (MAZO REAL) ---")
    print("1. Contra la Maquina")
    print("2. Contra otro Jugador")
    modo = input("Seleccione el modo: ")

    nombre_j1 = input("Nombre del Jugador 1: ")
    nombre_j2 = "Maquina" if modo == "1" else input("Nombre del Jugador 2: ")

    # Reparto inicial
    puntos_j1 = repartir_carta() + repartir_carta()
    puntos_j2 = repartir_carta() + repartir_carta()

    paso_j1 = False
    paso_j2 = False

    while not (paso_j1 and paso_j2):
        # Turno Jugador 1
        if not paso_j1:
            print(f"\nTurno de {nombre_j1} ({puntos_j1} pts). Cartas restantes en mazo: {len(mazo)}")
            accion = input("1. Pedir carta | 2. Pasar: ")
            if accion == "1":
                puntos_j1 += repartir_carta()
                if puntos_j1 > 21:
                    print(f"¡{puntos_j1}! Te pasaste.")
                    paso_j1 = True
            else:
                paso_j1 = True

        # Turno Jugador 2 / Maquina
        if not paso_j2:
            if modo == "1":
                # La maquina se planta con 17 o más (lógica simple)
                if puntos_j2 < 17:
                    puntos_j2 += repartir_carta()
                else:
                    paso_j2 = True
            else:
                print(f"\nTurno de {nombre_j2} ({puntos_j2} pts). Cartas restantes: {len(mazo)}")
                accion = input("1. Pedir carta | 2. Pasar: ")
                if accion == "1":
                    puntos_j2 += repartir_carta()
                    if puntos_j2 > 21:
                        print(f"¡{puntos_j2}! Se paso.")
                        paso_j2 = True
                else:
                    paso_j2 = True

    revelar_resultado(nombre_j1, puntos_j1, nombre_j2, puntos_j2)

# Ejecutar
jugar_21()