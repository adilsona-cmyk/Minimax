import random

# Crear el tablero vacío

def crear_tabla(fila, columna):

    tabla = [["▩" for _ in range(columna)] for _ in range(fila)]
    return tabla

# Imprimir el tablero en consola
def imprimir_tabla(tabla):

    print()
    for s in tabla:
        print("  ".join(s))
    print()

# Insertar personajes aleatoriamente

def insertar_raton_gato(fila, columna, tabla):

    posiciones = [(f, c) for f in range(fila) for c in range(columna)]
    random.shuffle(posiciones)

    (f_raton, c_raton), (f_gato, c_gato) = posiciones[:2]

    tabla[f_raton][c_raton] = "R"
    tabla[f_gato][c_gato]   = "G"

    return tabla, (f_raton, c_raton), (f_gato, c_gato)

# Ejecutar un movimiento en el tablero

def movimientos_posibles(pos, movimiento, tabla):

    direcciones = {
        "A": (0,  -1),  # Izquierda
        "D": (0,   1),  # Derecha
        "W": (-1,  0),  # Arriba
        "S": (1,   0)  # Abajo
    }

    if movimiento not in direcciones:
        return tabla, pos   # Movimiento inválido: no se hace nada

    dx, dy = direcciones[movimiento]
    fila, columna = pos
    nueva_fila    = fila + dx
    nueva_columna = columna + dy

    # Verificar que no salga de los límites
    if not (0 <= nueva_fila < len(tabla) and 0 <= nueva_columna < len(tabla[0])):
        return tabla, pos

    personaje = tabla[fila][columna]
    destino   = tabla[nueva_fila][nueva_columna]

    # Bloquear colisiones inválidas
    if personaje == "R" and destino == "G":
        return tabla, pos

    # Aplicar el movimiento
    tabla[fila][columna]             = "□"
    tabla[nueva_fila][nueva_columna] = personaje

    return tabla, (nueva_fila, nueva_columna)


# Distancia Manhattan entre dos posiciones

def distancia_manhattan(pos1, pos2):

    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Función de evaluación para Minimax

def evaluar_posicion(pos_gato, pos_raton):

    return -distancia_manhattan(pos_gato, pos_raton)


# Algoritmo Minimax

def minimax(tabla, pos_gato, pos_raton, profundidad, es_turno_gato):

    # Caso base: gato atrapa al ratón
    if pos_gato == pos_raton:
        return 1000, None

    # Caso base: profundidad agotada
    if profundidad == 0:
        return evaluar_posicion(pos_gato, pos_raton), None

    direcciones_gato  = ["A", "D", "W", "S"]
    direcciones_raton = ["A", "D", "W", "S"]

    # Turno del GATO (maximizador)
    if es_turno_gato:
        mejor_valor      = float("-inf")
        mejor_movimiento = None

        for mov in direcciones_gato:
            tabla_copia = [fila[:] for fila in tabla]
            nueva_tabla, nueva_pos_gato = movimientos_posibles(pos_gato, mov, tabla_copia)
            valor, _ = minimax(nueva_tabla, nueva_pos_gato, pos_raton, profundidad - 1, False)

            if valor > mejor_valor:
                mejor_valor      = valor
                mejor_movimiento = mov

        return mejor_valor, mejor_movimiento

    # Turno del RATÓN (minimizador)
    else:
        mejor_valor      = float("inf")
        mejor_movimiento = None

        for mov in direcciones_raton:
            tabla_copia = [fila[:] for fila in tabla]
            nueva_tabla, nueva_pos_raton = movimientos_posibles(pos_raton, mov, tabla_copia)
            valor, _ = minimax(nueva_tabla, pos_gato, nueva_pos_raton, profundidad - 1, True)

            if valor < mejor_valor:
                mejor_valor      = valor
                mejor_movimiento = mov

        return mejor_valor, mejor_movimiento


# Verificar condición de victoria o derrota

def ganar_perder(pos_gato, pos_raton, turno, max_movimientos):

    if pos_raton == pos_gato:
        print("╔══════════════════════════════╗")
        print("║  ¡El gato atrapó al ratón!  :(  ║")
        print("╚══════════════════════════════╝")
        return False
    elif turno > max_movimientos:
        print("╔══════════════════════════════════════╗")
        print("║  ¡Tiempo agotado! El ratón sobrevivió :D ║")
        print("╚══════════════════════════════════════╝")
        return False
    return True

# CONFIGURACIÓN INICIAL DEL JUEGO

# Número de filas
while True:
    try:
        fila = int(input("Inserte la cantidad de filas (mínimo 2): "))
        if fila >= 2:
            break
        print("El número de filas debe ser mayor o igual a 2.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

# Número de columnas
while True:
    try:
        columna = int(input("Inserte la cantidad de columnas (mínimo 2): "))
        if columna >= 2:
            break
        print("El número de columnas debe ser mayor o igual a 2.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

# Nivel de dificultad (profundidad del Minimax)
niveles = """
Seleccione el nivel de dificultad:
  1 - Fácil   (la IA piensa 1 movimiento adelante)
  2 - Medio   (la IA piensa 2 movimientos adelante)
  3 - Difícil (la IA piensa 3 movimientos adelante)
"""
while True:
    try:
        profundidad = int(input(niveles + "\nIngrese el número: "))
        if profundidad in (1, 2, 3):
            break
        print("Debe ingresar 1, 2 o 3.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

# Máximo de movimientos
while True:
    try:
        max_movimientos = int(input("Ingrese el número máximo de movimientos (mínimo 1): "))
        if max_movimientos >= 1:
            break
        print("Debe ingresar un número mayor o igual a 1.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

# Modo de juego
modos = """
Seleccione el modo de juego:
  1 - Gato (IA) vs Ratón (tú)
  2 - Ratón (IA) vs Gato (tú)
  3 - Dos jugadores humanos (Gato vs Ratón)
"""
while True:
    try:
        caso_elegido = int(input(modos + "\nIngrese el número: "))
        if caso_elegido in (1, 2, 3):
            break
        print("Debe ingresar 1, 2 o 3.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

# INICIALIZACIÓN DEL TABLERO

tabla = crear_tabla(fila, columna)
tabla, pos_raton, pos_gato = insertar_raton_gato(fila, columna, tabla)

print("\n=== TABLERO INICIAL ===")
imprimir_tabla(tabla)
print("Controles: W = Arriba | S = Abajo | A = Izquierda | D = Derecha")
print(f"R = Ratón | G = Gato | □ = Celda recorrida\n")

# BUCLE PRINCIPAL DEL JUEGO

turno = 1
juego_activo = True

while juego_activo:
    print(f"--- Turno {turno} ---")

    match caso_elegido:

        # Modo 1: Ratón humano vs Gato IA
        case 1:
            movimiento_raton = input("Tu movimiento (Ratón) [W/A/S/D]: ").upper()
            _, movimiento_gato = minimax(tabla, pos_gato, pos_raton, profundidad, es_turno_gato=True)
            print(f"El Gato (IA) decide moverse: {movimiento_gato}")

        # Modo 2: Gato humano vs Ratón IA 
        case 2:
            _, movimiento_raton = minimax(tabla, pos_gato, pos_raton, profundidad, es_turno_gato=False)
            print(f"El Ratón (IA) decide moverse: {movimiento_raton}")
            movimiento_gato = input("Tu movimiento (Gato) [W/A/S/D]: ").upper()

        # Modo 3: Dos jugadores humanos 
        case 3:
            movimiento_raton = input("Movimiento del Ratón [W/A/S/D]: ").upper()
            movimiento_gato  = input("Movimiento del Gato  [W/A/S/D]: ").upper()

    # Aplicar movimientos al tablero 
    tabla, pos_raton = movimientos_posibles(pos_raton, movimiento_raton, tabla)
    tabla, pos_gato  = movimientos_posibles(pos_gato,  movimiento_gato,  tabla)

    # Mostrar tablero actualizado
    imprimir_tabla(tabla)

    # Verificar si el juego terminó
    juego_activo = ganar_perder(pos_gato, pos_raton, turno, max_movimientos)
    turno += 1