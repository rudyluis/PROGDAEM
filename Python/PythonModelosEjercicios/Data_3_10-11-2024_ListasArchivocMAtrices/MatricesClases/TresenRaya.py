# Crear el tablero del juego
tablero = [[' ' for _ in range(3)] for _ in range(3)]

# Función para imprimir el tablero
def imprimir_tablero():
    print("---------")
    for fila in tablero:
        print("|", end="")
        for celda in fila:
            print(celda, end="|")
        print("\n---------")

# Función para verificar si alguien ha ganado
def verificar_ganador():
    # Comprobar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != ' ':
            return fila[0]

    # Comprobar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]

    # Comprobar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    # Si no hay ganador, retornar None
    return None

# Función para jugar el juego
def jugar():
    jugador = 'X'  # Jugador inicial

    while True:
        imprimir_tablero()

        # Obtener la posición de la jugada del jugador
        fila = int(input("Ingrese la fila (0-2): "))
        columna = int(input("Ingrese la columna (0-2): "))

        # Verificar si la celda está vacía
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador

            # Verificar si alguien ha ganado
            ganador = verificar_ganador()
            if ganador:
                imprimir_tablero()
                print("¡El jugador", ganador, "ha ganado!")
                break

            # Cambiar el jugador
            jugador = 'O' if jugador == 'X' else 'X'
        else:
            print("¡La celda ya está ocupada! Intente de nuevo.")

        # Verificar si hay un empate
        if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            imprimir_tablero()
            print("¡Empate!")
            break

# Iniciar el juego
jugar()
