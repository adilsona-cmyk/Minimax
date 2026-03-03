# Minimax Lab - Juego Gato y Raton

Juego de tablero en consola donde un gato persigue a un raton usando el algoritmo Minimax. El proyecto fue desarrollado en Python y permite tres modos de juego distintos.

---

## Descripcion

El juego se desarrolla en un tablero de tamano configurable. El gato intenta atrapar al raton antes de que se agote el numero maximo de movimientos. La inteligencia artificial utiliza el algoritmo Minimax con funcion de evaluacion basada en distancia Manhattan para tomar decisiones optimas.

---

## Requisitos

- Python 3.10 o superior (se requiere la sintaxis `match/case`)
- No se necesitan librerias externas

---

## Instalacion

1. Clonar o descargar el repositorio.
2. Verificar que Python 3.10 o superior esta instalado:

```
python --version
```

3. Ejecutar el archivo principal:

```
python minimax_lab.py
```

---

## Configuracion del juego

Al iniciar el programa, se solicitara al usuario configurar los siguientes parametros:

| Parametro           | Descripcion                                      | Restriccion         |
|---------------------|--------------------------------------------------|----------------------|
| Filas               | Numero de filas del tablero                      | Minimo 2             |
| Columnas            | Numero de columnas del tablero                   | Minimo 2             |
| Nivel de dificultad | Profundidad de busqueda del algoritmo Minimax    | 1, 2 o 3             |
| Maximo movimientos  | Cantidad de turnos antes de que el raton escape  | Minimo 1             |
| Modo de juego       | Define quien controla cada personaje             | 1, 2 o 3             |

### Niveles de dificultad

- **Facil (1):** La IA evalua 1 movimiento adelante.
- **Medio (2):** La IA evalua 2 movimientos adelante.
- **Dificil (3):** La IA evalua 3 movimientos adelante.

### Modos de juego

- **Modo 1:** Raton (jugador) vs Gato (IA)
- **Modo 2:** Gato (jugador) vs Raton (IA)
- **Modo 3:** Dos jugadores humanos

---

## Controles

| Tecla | Accion    |
|-------|-----------|
| W     | Arriba    |
| S     | Abajo     |
| A     | Izquierda |
| D     | Derecha   |

---

## Simbolos del tablero

| Simbolo | Significado       |
|---------|-------------------|
| R       | Raton             |
| G       | Gato              |
| []      | Celda recorrida   |
| [#]     | Celda vacia       |

---

## Condiciones de victoria

- **Gato gana:** El gato alcanza la misma posicion que el raton.
- **Raton gana:** Se supera el numero maximo de movimientos sin que el gato atrape al raton.

---

## Estructura del codigo

```
minimax_lab.py
|
|-- crear_tabla()             Genera el tablero inicial
|-- imprimir_tabla()          Muestra el tablero en consola
|-- insertar_raton_gato()     Coloca los personajes en posiciones aleatorias
|-- movimientos_posibles()    Aplica y valida un movimiento
|-- distancia_manhattan()     Calcula la distancia entre dos posiciones
|-- evaluar_posicion()        Funcion heuristica para el algoritmo Minimax
|-- minimax()                 Implementacion del algoritmo Minimax
|-- ganar_perder()            Verifica el estado final del juego
|-- (bucle principal)         Gestiona el flujo del juego por turnos
```

---

## Algoritmo Minimax

El algoritmo Minimax se implementa con las siguientes caracteristicas:

- El **gato** actua como maximizador: busca minimizar la distancia al raton.
- El **raton** actua como minimizador: busca maximizar la distancia al gato.
- La funcion de evaluacion retorna el negativo de la distancia Manhattan entre ambos personajes.
- El caso base de captura devuelve un puntaje de 1000 a favor del gato.
- La profundidad limita el numero de movimientos que la IA analiza hacia adelante.

---

## Ejemplo de ejecucion

```
Inserte la cantidad de filas (minimo 2): 5
Inserte la cantidad de columnas (minimo 2): 5
Nivel de dificultad: 2
Numero maximo de movimientos: 20
Modo de juego: 1

=== TABLERO INICIAL ===

[#]  [#]  [#]  [#]  [#]
[#]  R    [#]  [#]  [#]
[#]  [#]  [#]  [#]  [#]
[#]  [#]  [#]  G    [#]
[#]  [#]  [#]  [#]  [#]

Controles: W = Arriba | S = Abajo | A = Izquierda | D = Derecha

--- Turno 1 ---
Tu movimiento (Raton) [W/A/S/D]: W
El Gato (IA) decide moverse: W
```
