import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def tablero_lleno(tablero):
    return all(tablero[i][j] != " " for i in range(3) for j in range(3))

def movimiento_valido(tablero, fila, columna):
    return tablero[fila][columna] == " "

def realizar_movimiento(tablero, fila, columna, jugador):
    tablero[fila][columna] = jugador

def turno_de_la_computadora(tablero):
    fila, columna = random.randint(0, 2), random.randint(0, 2)
    while not movimiento_valido(tablero, fila, columna):
        fila, columna = random.randint(0, 2), random.randint(0, 2)
    return fila, columna

def juego():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)

        if jugador_actual == "X":
            fila = int(input("Ingrese el número de fila (0, 1, 2): "))
            columna = int(input("Ingrese el número de columna (0, 1, 2): "))
        else:
            print("Turno de la computadora:")
            fila, columna = turno_de_la_computadora(tablero)

        if movimiento_valido(tablero, fila, columna):
            realizar_movimiento(tablero, fila, columna, jugador_actual)

            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"{jugador_actual} ha ganado!")
                break
            elif tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("El juego ha terminado en empate.")
                break
            else:
                jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Movimiento no válido. Inténtelo de nuevo.")

if __name__ == "__main__":
    juego()