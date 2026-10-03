import random
print("daniel jose reyes leon")
numero = random.randint(1, 10)
while True:
    try:
        intentos=int(input("Adivina el número entre 1 y 10: "))
        if intentos <1 or intentos >10:
            raise ValueError
        if intentos == numero:
            print("="*26)
            print("¡Felicidades! Adivinaste el número.")
            print("="*2*2)
            break
        elif intentos < numero:
            print("="*26)
            print("muy bajo")
            print("="*26)
        else:
            print("="*26)
            print("muy alto")
            print("="*26)
    except ValueError:
        print("Número fuera de rango. Intenta nuevamente.")
        print("gracias por jugar, que el código te acompañe")

