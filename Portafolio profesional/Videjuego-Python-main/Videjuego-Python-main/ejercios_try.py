import random

print("Daniel Reyes")

numero = random.randint(1, 10)
while True:
    try:
        intento = int(input("Adivina el número entre 1 y 10: "))
        if intento < 1 or intento > 10:
            print("Número fuera de rango. Intenta nuevamente.")
            continue

        if intento == numero:
            print("¡Felicidades! Adivinaste el número.")
            break
        else:
            print("Número incorrecto. Intenta nuevamente.")
    except ValueError:
        print("Debes escribir un número válido.")
        break
