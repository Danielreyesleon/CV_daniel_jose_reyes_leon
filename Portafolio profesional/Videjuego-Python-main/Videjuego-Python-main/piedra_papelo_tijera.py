import random

print("Hello, World!")


class Juegador:
    def __init__(self, nombre):
        self.nombre = nombre

    def elegir(self):
        opcion = input("Elige tu jugada (piedra, papel, tijera): ").lower()
        return opcion


class Computadora:
    def elegir(self):
        opciones = ["piedra", "papel", "tijera"]
        opcion = random.choice(opciones)
        return opcion

class Juego:
    def __init__(self):
        self.jugador = Juegador("Jugador")
        self.cpu = Computadora()

    def determiner_ganador(self, j, c):
        if j == c:
          return "Empate"
        elif (j == "piedra" and c == "tijera") or (j == "papel" and c == "piedra") or (j == "tijera" and c == "papel"):
            return "Jugador gana"
        else:
            return "Computadora gana"
    def jugar(self):    
        j = self.jugador.elegir()
        c = self.cpu.elegir()
        print(f"Jugador eligió: {j}")
        print(f"Computadora eligió: {c}")
        resultado = self.determiner_ganador(j, c)
        print(resultado)

juego = Juego()
juego.jugar()