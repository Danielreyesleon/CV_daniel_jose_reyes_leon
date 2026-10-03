# tablero = [" "] * 9

# def mostrar_tablero():
#     print(tablero[0], "|", tablero[1], "|", tablero[2])
#     print("--+---+--")
#     print(tablero[3], "|", tablero[4], "|", tablero[5])
#     print("--+---+--")
#     print(tablero[6], "|", tablero[7], "|", tablero[8])

# turno = "X"

# for i in range(9):
#     mostrar_tablero()
#     pos = int(input("Elige posición (0-8): "))
#     if pos == "-0" or pos == "-1" or pos == "-2" or pos == "-3" or pos == "-4" or pos == "-5" or pos == "-6" or pos == "-7" or pos == "-8":
#         print("Posición inválida")
#         continue
#     if pos not in range(9):
#         print("Posición inválida")
#         continue
#     if pos not in range(float(0, 9)):
#         print("Posición inválida")
#         continue
    
    
#     if tablero[pos] == " ":
#         tablero[pos] = turno
#         turno = "O" if turno == "X" else "X"
#     else:
#         print("Posición ocupada")


tablero = [" "] * 9

def mostrar_tablero():
    print(tablero[0], "|", tablero[1], "|", tablero[2])
    print("--+---+--")
    print(tablero[3], "|", tablero[4], "|", tablero[5])
    print("--+---+--")
    print(tablero[6], "|", tablero[7], "|", tablero[8])

turno = "X"

while True:
    mostrar_tablero()
    
    try:
        pos = int(input("Elige posición (0-8): "))
        
        # 🔹 Validar rango
        if pos < 0 or pos > 8:
            print(" Número fuera de rango. Debe ser entre 0 y 8.")
            continue
        pos = int(input("Elige posición (0-8): "))
        if pos == "-0" or pos == "-1" or pos == "-2" or pos == "-3" or pos == "-4" or pos == "-5" or pos == "-6" or pos == "-7" or pos == "-8":
          print("Posición inválida")
          continue
        # 🔹 Validar si está ocupada
        if tablero[pos] != " ":
            print(" Esa posición ya está ocupada.")
            continue
        
        tablero[pos] = turno
        
        # Cambiar turno
        turno = "O" if turno == "X" else "X"
    
    except ValueError:
        print(" Debes escribir un número válido.")