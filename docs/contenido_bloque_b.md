# Bloque B: Busqueda sin Informacion — Resumen Teorico

## 1. Formulacion de problemas como espacio de estados

Un problema de busqueda se define por cuatro elementos:
- **Estado inicial:** configuracion de partida
- **Acciones/operadores:** transiciones validas entre estados
- **Test de meta:** condicion que define el objetivo
- **Funcion de costo:** costo de cada paso (path cost)

El espacio de estados es el grafo implicito de todas las configuraciones alcanzables desde el estado inicial mediante la aplicacion de operadores.

**Ejemplo canonico:** el 8-puzzle tiene 9!/2 = 181,440 estados alcanzables (la mitad del total, ya que la paridad de las inversiones divide el espacio en dos componentes desconectadas).

## 2. Busqueda sin informacion (uninformed search)

### BFS (Breadth-First Search)
- Explora por niveles (FIFO)
- Completo: si, si b es finito
- Optimo: si, si costos son uniformes
- Complejidad temporal: O(b^d)
- Complejidad espacial: O(b^d) — principal desventaja

### DFS (Depth-First Search)
- Explora en profundidad primero (LIFO)
- Completo: no, en espacios infinitos
- Optimo: no
- Complejidad espacial: O(bm) — ventaja principal

### IDS (Iterative Deepening Search)
- Combina optimalidad de BFS con memoria de DFS
- Complejidad temporal: O(b^d) (el re-trabajo es factor constante)
- Complejidad espacial: O(bd) — lineal
- **Algoritmo preferido cuando no hay heuristica y se desconoce la profundidad**

### Busqueda bidireccional
- Busca desde inicio y meta simultaneamente
- Reduce complejidad de O(b^d) a O(b^{d/2})
- Requiere que la meta sea explicita y los operadores reversibles

## 3. Busqueda hacia adelante y hacia atras

- **Hacia adelante (forward):** del estado inicial hacia la meta. Natural cuando el estado inicial es unico
- **Hacia atras (backward):** de la meta hacia el inicio. Mejor cuando hay muchos estados iniciales o el factor de ramificacion hacia atras es menor
- **Bidireccional:** combina ambas. La frontera de busqueda se encuentra en el medio

## 4. Busqueda informada: A, A*, AO*

### Heuristicas
- **Admisible:** h(n) <= h*(n), nunca sobreestima el costo real
- **Consistente (monotona):** h(n) <= c(n,n') + h(n'), satisface desigualdad triangular
- Toda heuristica consistente es admisible (pero no al reves)

### Algoritmo A*
- f(n) = g(n) + h(n)
- g(n): costo acumulado desde el inicio
- h(n): estimacion heuristica al objetivo
- Con heuristica admisible: A* es optimo y completo
- Con heuristica consistente: A* no re-expande nodos (eficiente)

### Grafos AND-OR y AO*
- Para problemas descomponibles en subproblemas
- Nodo AND: todos los hijos deben resolverse
- Nodo OR: basta con resolver un hijo
- AO* propaga costos bottom-up en el grafo solucion

## 5. Minimax y poda alfa-beta

### Minimax
- Para juegos de suma cero entre dos jugadores
- MAX maximiza la utilidad, MIN la minimiza
- Explora todo el arbol de juego
- Complejidad: O(b^m) donde m es profundidad maxima

### Poda alfa-beta
- Optimizacion de minimax que poda ramas que no afectan la decision
- alfa: mejor valor para MAX en el camino actual
- beta: mejor valor para MIN en el camino actual
- Poda cuando alfa >= beta
- Mejor caso (orden perfecto): O(b^{m/2}) — duplica la profundidad explorable
- Caso promedio: O(b^{3m/4})

### MCTS (Monte Carlo Tree Search)
- Alternativa a minimax para juegos con factor de ramificacion enorme
- 4 fases: seleccion (UCT), expansion, simulacion (rollout), retropropagacion
- Usado por AlphaGo (Silver et al., 2016) combinado con redes neuronales

## 6. Algoritmos geneticos

### Componentes
- **Cromosoma:** representacion de una solucion candidata
- **Poblacion:** conjunto de cromosomas
- **Fitness:** funcion de aptitud que evalua cada individuo
- **Seleccion:** ruleta, torneo, ranking
- **Cruce (crossover):** combina dos padres para crear hijos
- **Mutacion:** perturbacion aleatoria para mantener diversidad

### Tipos de cruce
- Un punto, dos puntos, uniforme (para cadenas binarias)
- OX (Order Crossover): para permutaciones como el TSP
- PMX (Partially Mapped Crossover)

### Parametros criticos
- Tasa de mutacion: tipicamente 0.5%-5%. Muy alta (>30%) = busqueda aleatoria
- Tamano de poblacion: balance entre diversidad y costo computacional
- Criterio de parada: generaciones maximas, convergencia, fitness objetivo

### Teorema del esquema (Holland, 1975)
Los esquemas cortos, de bajo orden y alta aptitud reciben un numero exponencialmente creciente de representantes en generaciones sucesivas.

## Fuentes principales

- Russell, S. & Norvig, P. (2021). Artificial Intelligence: A Modern Approach, 4th ed.
- Hart, P.E., Nilsson, N.J. & Raphael, B. (1968). A Formal Basis for the Heuristic Determination of Minimum Cost Paths. IEEE Transactions on SSC.
- Knuth, D.E. & Moore, R.W. (1975). An Analysis of Alpha-Beta Pruning. Artificial Intelligence.
- Korf, R.E. (1985). Depth-First Iterative-Deepening. Artificial Intelligence.
- Silver, D. et al. (2016). Mastering the Game of Go with Deep Neural Networks and Tree Search. Nature.
- Holland, J.H. (1975). Adaptation in Natural and Artificial Systems. U of Michigan Press.
