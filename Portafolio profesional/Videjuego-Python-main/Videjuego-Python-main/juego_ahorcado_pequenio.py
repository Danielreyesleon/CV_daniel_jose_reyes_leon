print("daniel jose reyes leon")

palabra = "python"

adivinadas =[]
intentos = 6

while intentos > 0:
    progreso=""
    for letra in palabra:
        if letra in adivinadas:
            progreso += letra
        else:
            progreso += "_"
    print("Palabra: ", progreso)
    try:
        letra = input("Adivina una letra: ")
        if not letra.isalpha() or len(letra) != 1:
            raise ValueError("Entrada inválida. Debes ingresar una sola letra.")
        
        if letra in palabra:
            adivinadas.append(letra)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("¡Incorrecto! Te quedan", intentos, "intentos.")
    except ValueError:
        print("Entrada inválida. Debes ingresar una sola letra.")
if "_" not in progreso:
    print("¡Felicidades! Has adivinado la palabra:", palabra)
else:
    print("¡Has perdido! La palabra era:", palabra)
    
    print("¡Felicidades! Has adivinado la palabra:", palabra)