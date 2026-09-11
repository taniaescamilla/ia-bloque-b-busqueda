# UNIVERSIDAD NACIONAL ROSARIO CASTELLANOS
## LICENCIATURA EN CIENCIA DE DATOS PARA NEGOCIOS

---

# DOCUMENTO ACADEMICO EN EXTENSO
# BLOQUE B: BUSQUEDA SIN INFORMACION

---

**FICHA TECNICA DEL BLOQUE CURRICULAR**

| Campo | Valor |
|-------|-------|
| **Asignatura / UCA** | Inteligencia Artificial (LCDN4INT10) |
| **Unidad Tematica** | Bloque B: Busqueda sin Informacion |
| **Programa Academico** | Licenciatura en Ciencia de Datos para Negocios |
| **Institucion Educativa** | Universidad Nacional Rosario Castellanos |
| **Ciclo Lectivo** | Cuarto Semestre |
| **Docente** | Martin Humberto Llamas Haro |

**Equipo**

| Integrante | Rol |
|------------|-----|
| Daniel Ruffo | Investigacion, desarrollo, arquitectura del repositorio |
| Giovana Espinosa | Investigacion, revision, validacion academica |

Ciudad de Mexico, Mexico, 2026

---

## Indice

1. Introduccion y Motivacion
2. Espacio de Estados y Representacion de Problemas
   2.1. Definicion formal
   2.2. Ejemplo: el rompecabezas de 8 piezas
3. Estrategias de Busqueda No Informada
   3.1. Busqueda en anchura (BFS)
   3.2. Busqueda en profundidad (DFS)
   3.3. Busqueda en profundidad limitada e iterativa (IDS)
   3.4. Busqueda de costo uniforme
4. Busqueda Hacia Adelante y Hacia Atras
   4.1. Busqueda hacia adelante (forward chaining)
   4.2. Busqueda hacia atras (backward chaining)
   4.3. Busqueda bidireccional
5. Busqueda Informada y Reduccion de Problemas
   5.1. Funciones heuristicas: admisibilidad y consistencia
   5.2. Algoritmo A
   5.3. Algoritmo A*
   5.4. Algoritmo IDA*
   5.5. Grafos AND/OR y Algoritmo AO*
6. Juegos de Adversario: Minimax y Poda Alfa-Beta
   6.1. Arboles de juego y el teorema minimax
   6.2. El algoritmo minimax
   6.3. Poda alfa-beta
   6.4. Aplicaciones: de Deep Blue a AlphaGo
7. Algoritmos Geneticos y Computacion Evolutiva
   7.1. Fundamentos biologicos y formalizacion
   7.2. Operadores geneticos
   7.3. Teorema del esquema de Holland
   7.4. Teorema No Free Lunch
8. Conexion con la Ciencia de Datos
9. Dimension Etica y Responsabilidad
10. Conclusiones
Referencias

---

## 1. Introduccion y Motivacion

La busqueda constituye el mecanismo computacional fundamental mediante el cual un agente inteligente explora sistematicamente un espacio de posibilidades para encontrar una solucion a un problema dado. Historicamente, los primeros programas de inteligencia artificial, como el General Problem Solver de Newell y Simon (1972), operaban esencialmente como algoritmos de busqueda sobre representaciones simbolicas del conocimiento.

Russell y Norvig (2021) establecen que la formulacion de un problema de busqueda requiere cinco componentes: un estado inicial, una funcion de acciones aplicables, un modelo de transicion, una prueba de meta y una funcion de costo de camino. Esta abstraccion resulta notablemente general: desde la navegacion de un robot en un almacen hasta la demostracion automatica de teoremas, la estructura subyacente es un grafo de estados que debe recorrerse de manera eficiente.

El presente documento examina en profundidad los algoritmos de busqueda correspondientes al Bloque B del programa de Inteligencia Artificial de la Licenciatura en Ciencia de Datos para Negocios de la Universidad Nacional Rosario Castellanos. El bloque abarca desde las estrategias no informadas clasicas hasta los metodos heuristicos, la teoria de juegos de adversario y la computacion evolutiva, articulando cada tema con sus fundamentos teoricos, su complejidad computacional y sus aplicaciones contemporaneas.

---

## 2. Espacio de Estados y Representacion de Problemas

### 2.1. Definicion formal

Un problema de busqueda se define formalmente como una tupla (S, s0, A, T, G, c) donde:

- **S** es el conjunto de estados posibles (espacio de estados).
- **s0** pertenece a S y es el estado inicial.
- **A(s)** es el conjunto de acciones aplicables en el estado s.
- **T(s, a)** es la funcion de transicion que, dado un estado s y una accion a, produce el estado sucesor s'.
- **G** es un subconjunto de S que contiene los estados meta.
- **c(s, a, s')** es la funcion de costo que asigna un valor numerico no negativo a cada transicion (Russell y Norvig, 2021).

El espacio de estados puede representarse como un grafo dirigido donde los nodos corresponden a estados y las aristas a acciones. La solucion al problema es un camino desde s0 hasta algun estado en G, y la solucion optima es aquella con costo minimo.

La complejidad del espacio de estados es un factor determinante en la seleccion del algoritmo. Para el ajedrez, el espacio tiene aproximadamente 10^43 estados legales (Shannon, 1950). Para el juego de Go, la cifra asciende a 10^170, lo que hace inviable cualquier enumeracion exhaustiva y motiva el uso de heuristicas y metodos de Monte Carlo (Silver et al., 2016).

### 2.2. Ejemplo: el rompecabezas de 8 piezas

El 8-puzzle es un problema clasico con 9!/2 = 181,440 estados alcanzables. Cada estado es una configuracion de las fichas numeradas del 1 al 8 en una cuadricula 3x3, con una casilla vacia. Las acciones consisten en deslizar una ficha adyacente al espacio vacio. La prueba de meta es alcanzar la configuracion ordenada.

Este problema ha servido como benchmark historico para comparar algoritmos de busqueda. Korf (1985) demostro que la busqueda iterativa en profundidad (IDA*) con la heuristica de distancia Manhattan resuelve instancias del 15-puzzle (cuyo espacio tiene 10^13 estados) de manera optima con memoria lineal, un resultado que revoluciono el campo.

---

## 3. Estrategias de Busqueda No Informada

Los algoritmos de busqueda no informada (ciega) no utilizan informacion sobre la distancia al estado meta. Se distinguen por cuatro criterios de evaluacion (Russell y Norvig, 2021):

- **Completitud:** si la solucion existe, el algoritmo la encuentra.
- **Optimalidad:** el algoritmo encuentra la solucion de menor costo.
- **Complejidad temporal:** numero de nodos generados.
- **Complejidad espacial:** numero maximo de nodos en memoria.

Sea b el factor de ramificacion y d la profundidad de la solucion mas superficial.

### 3.1. Busqueda en anchura (BFS)

Explora el arbol de busqueda nivel por nivel, expandiendo todos los nodos de profundidad k antes de pasar a profundidad k+1. Utiliza una cola FIFO como frontera.

- Completitud: Si, si b es finito.
- Optimalidad: Si, cuando el costo es uniforme (todos los pasos cuestan igual).
- Tiempo: O(b^d).
- Espacio: O(b^d).

La complejidad espacial es el talon de Aquiles de BFS. Para b = 10 y d = 12, la frontera requiere almacenar 10^12 nodos, lo cual excede la memoria de cualquier computadora actual (Nilsson, 1980).

### 3.2. Busqueda en profundidad (DFS)

Explora el arbol siguiendo una rama hasta su maxima profundidad antes de retroceder. Utiliza una pila LIFO como frontera (o recursion).

- Completitud: No en espacios infinitos o con ciclos (si, en grafos finitos con deteccion de repetidos).
- Optimalidad: No.
- Tiempo: O(b^m), donde m es la profundidad maxima del arbol.
- Espacio: O(bm), es decir, lineal en la profundidad.

La ventaja fundamental de DFS es su eficiencia en memoria: requiere almacenar solo O(bm) nodos, frente a los O(b^d) de BFS. Esta propiedad la hace viable para espacios de busqueda muy grandes cuando la solucion se encuentra a profundidad razonable.

### 3.3. Busqueda en profundidad limitada e iterativa (IDS)

Korf (1985) propuso la busqueda iterativa en profundidad (Iterative Deepening Search), que combina las ventajas de BFS y DFS. Ejecuta sucesivas busquedas DFS con limites de profundidad crecientes: primero busca a profundidad 0, luego 1, luego 2, y asi sucesivamente.

- Completitud: Si.
- Optimalidad: Si, cuando el costo es uniforme.
- Tiempo: O(b^d).
- Espacio: O(bd).

Aunque pareciera ineficiente regenerar los niveles superiores, el trabajo redundante es insignificante: la capa d tiene b^d nodos, y el trabajo total de IDS es aproximadamente b^d * b/(b-1), un factor constante respecto a BFS. IDS es el algoritmo de busqueda no informada preferido cuando el espacio de estados es grande y la profundidad de la solucion es desconocida (Russell y Norvig, 2021).

### 3.4. Busqueda de costo uniforme

Generaliza BFS para costos de arista no uniformes. Expande el nodo con menor costo acumulado g(n), utilizando una cola de prioridad. Es completa y optima siempre que los costos sean positivos (Dijkstra, 1959). Su complejidad temporal y espacial es O(b^(1+C*/epsilon)), donde C* es el costo de la solucion optima y epsilon es el costo minimo de una arista.

---

## 4. Busqueda Hacia Adelante y Hacia Atras

### 4.1. Busqueda hacia adelante (forward chaining)

La busqueda hacia adelante, tambien denominada encadenamiento progresivo o data-driven search, parte del estado inicial y aplica acciones sucesivas hacia la meta. Es el paradigma natural de la mayoria de los algoritmos de busqueda (BFS, DFS, A*). En sistemas basados en reglas, corresponde al encadenamiento hacia adelante: si los datos satisfacen las premisas de una regla, se ejecuta la accion y se produce un nuevo estado.

Su ventaja principal radica en que solo genera estados alcanzables desde el estado inicial, evitando explorar regiones del espacio de estados irrelevantes para el problema.

### 4.2. Busqueda hacia atras (backward chaining)

La busqueda hacia atras parte del estado meta y trabaja en sentido inverso, buscando que acciones pudieron producir ese estado. En planificacion automatica, corresponde a la regresion: dado un estado meta G, se identifican las acciones cuyo efecto incluye algun subobjetivo de G, y se computa el estado predecesor necesario.

Este enfoque resulta eficiente cuando el conjunto de estados meta es pequeno pero el factor de ramificacion hacia adelante es grande. En demostracion automatica de teoremas, por ejemplo, es mas natural partir del teorema a demostrar y buscar las premisas que lo sustenten (Nilsson, 1980).

### 4.3. Busqueda bidireccional

La busqueda bidireccional ejecuta simultaneamente una busqueda hacia adelante desde el estado inicial y una busqueda hacia atras desde la meta, hasta que ambas fronteras se intersectan.

Su ventaja teorica es considerable: si la busqueda unidireccional tiene complejidad O(b^d), la bidireccional tiene O(2 * b^(d/2)) = O(b^(d/2)), una reduccion exponencial. Para b = 10 y d = 12, esto significa 2 * 10^6 nodos en lugar de 10^12.

La dificultad practica reside en computar eficientemente los predecesores de un estado y en disenar un criterio de terminacion correcto que garantice optimalidad (Russell y Norvig, 2021).

---

## 5. Busqueda Informada y Reduccion de Problemas

### 5.1. Funciones heuristicas: admisibilidad y consistencia

Una funcion heuristica h(n) estima el costo desde el nodo n hasta la meta mas cercana. Se dice que h es:

- **Admisible** si nunca sobreestima el costo real: h(n) <= h*(n) para todo n, donde h*(n) es el costo real optimo.
- **Consistente** (o monotona) si para todo nodo n y sucesor n' generado por la accion a: h(n) <= c(n, a, n') + h(n').

Toda heuristica consistente es admisible, pero no al reves. La consistencia garantiza que los valores de f(n) = g(n) + h(n) son no decrecientes a lo largo de cualquier camino, lo que simplifica la demostracion de optimalidad de A* (Pearl, 1984).

**Ejemplos clasicos para el 8-puzzle:**

- h1: numero de fichas mal colocadas (admisible, subestima).
- h2: suma de distancias Manhattan de cada ficha a su posicion meta (admisible, domina a h1).

Pearl (1984) demostro que si h2(n) >= h1(n) para todo n (h2 domina a h1), entonces A* con h2 expande un subconjunto de los nodos que A* expandiria con h1. Por lo tanto, heuristicas mas informadas producen busquedas mas eficientes.

### 5.2. Algoritmo A

El Algoritmo A es la version basica de busqueda best-first que utiliza la funcion de evaluacion f(n) = g(n) + h(n), donde g(n) es el costo del camino desde el inicio hasta n, y h(n) es una estimacion heuristica del costo restante. Sin restricciones sobre h, el Algoritmo A no garantiza optimalidad.

### 5.3. Algoritmo A*

Hart, Nilsson y Raphael (1968) introdujeron A* como una extension del Algoritmo A con la restriccion de que h sea admisible. Este resultado fundamental establece que:

**Teorema (Hart et al., 1968):** Si h es admisible, A* es completo y optimo. Es decir, la primera solucion que A* encuentra es necesariamente la de menor costo.

**Teorema de optimalidad de eficiencia:** Ningun otro algoritmo que use la misma informacion heuristica puede garantizar expandir menos nodos que A* sin sacrificar optimalidad (dada una heuristica consistente).

El funcionamiento de A* se resume asi:

1. Inicializar la lista abierta con el nodo inicial (f = h(s0)).
2. Extraer el nodo n con menor f de la lista abierta.
3. Si n es meta, retornar la solucion.
4. Expandir n, calculando f(n') = g(n') + h(n') para cada sucesor.
5. Si n' no esta en la lista cerrada (o se encontro un camino mas corto), agregarlo a la lista abierta.
6. Repetir desde el paso 2.

La complejidad temporal de A* depende criticamente de la calidad de la heuristica. Con una heuristica perfecta (h = h*), A* va directo a la solucion en O(d). Con h = 0 (sin informacion), A* degenera en busqueda de costo uniforme. En el peor caso, la complejidad es exponencial, pero en la practica heuristicas bien disenadas reducen drasticamente el espacio explorado.

La principal limitacion de A* es su consumo de memoria: almacena todos los nodos generados, lo que puede agotar la RAM antes de encontrar la solucion.

### 5.4. Algoritmo IDA*

Korf (1985) propuso Iterative Deepening A* (IDA*) para resolver el problema de memoria de A*. IDA* realiza sucesivas busquedas en profundidad, pero en lugar de usar la profundidad como limite, usa el valor de f:

1. Establecer el umbral t = f(s0) = h(s0).
2. Ejecutar DFS, podando nodos donde f(n) > t.
3. Si no se encontro solucion, actualizar t al menor valor de f que excedio el umbral.
4. Repetir.

IDA* es completo, optimo (con h admisible) y usa memoria lineal O(bd). Es el algoritmo de eleccion para problemas con espacios de estados muy grandes y costos uniformes. Korf lo utilizo para resolver de manera optima todas las instancias del 15-puzzle, un logro notable considerando que el espacio tiene mas de 10^13 estados.

### 5.5. Grafos AND/OR y Algoritmo AO*

Algunos problemas admiten descomposicion: resolver el problema principal equivale a resolver un conjunto de subproblemas. Esta estructura se representa mediante grafos AND/OR:

- **Nodo OR:** se resuelve si al menos uno de sus hijos se resuelve (alternativas).
- **Nodo AND:** se resuelve solo si todos sus hijos se resuelven (subproblemas obligatorios).

El algoritmo AO* (Martelli y Montanari, 1973) generaliza A* para grafos AND/OR. Mantiene un grafo de solucion parcial y en cada iteracion:

1. Selecciona el nodo hoja no resuelto mas prometedor del grafo de solucion actual.
2. Lo expande.
3. Actualiza los costos de manera ascendente (bottom-up) por el grafo.
4. Revisa el grafo de solucion optimo.

AO* es relevante en planificacion con incertidumbre, donde las acciones pueden tener multiples resultados (nodos AND representan los posibles resultados, todos los cuales deben poder manejarse). Tambien se utiliza en demostracion automatica de teoremas y en descomposicion jerarquica de tareas.

---

## 6. Juegos de Adversario: Minimax y Poda Alfa-Beta

### 6.1. Arboles de juego y el teorema minimax

Un juego de adversario de suma cero con informacion perfecta se modela como un arbol donde los niveles alternan entre los movimientos de MAX (jugador que maximiza) y MIN (jugador que minimiza). En los nodos terminales, una funcion de utilidad asigna un valor numerico que refleja el resultado (victoria, derrota, empate).

Von Neumann demostro el teorema minimax en 1928, formalizado extensamente en Von Neumann y Morgenstern (1944): en un juego finito de suma cero con informacion perfecta, existe una estrategia optima para cada jugador y un valor del juego determinado. Este resultado fundamental establece que la teoria de juegos tiene una solucion racional bien definida.

### 6.2. El algoritmo minimax

El algoritmo minimax (Russell y Norvig, 2021) computa recursivamente el valor minimax de cada nodo:

- Si n es terminal: valor(n) = utilidad(n).
- Si n es nodo MAX: valor(n) = max sobre los hijos de n de valor(hijo).
- Si n es nodo MIN: valor(n) = min sobre los hijos de n de valor(hijo).

El algoritmo realiza una exploracion completa en profundidad (DFS) del arbol de juego. Su complejidad es O(b^m), donde b es el factor de ramificacion y m es la profundidad maxima. Para el ajedrez, con b aproximadamente 35 y m aproximadamente 80, esto es computacionalmente intratable.

En la practica, minimax se combina con:
- **Profundidad limitada:** se corta la busqueda a profundidad d y se aplica una funcion de evaluacion heuristica en los nodos hoja.
- **Quiescence search:** se extiende la busqueda en posiciones "inestables" (capturas, jaques) para evitar el efecto horizonte.

### 6.3. Poda alfa-beta

Knuth y Moore (1975) analizaron formalmente la poda alfa-beta, un metodo que elimina ramas del arbol de juego que no pueden influir en la decision final. El algoritmo mantiene dos valores:

- **alfa:** el mejor valor que MAX puede garantizar en el camino actual (limite inferior).
- **beta:** el mejor valor que MIN puede garantizar en el camino actual (limite superior).

La poda ocurre cuando alfa >= beta: si MAX ya tiene una opcion que garantiza al menos alfa, y MIN tiene una opcion que garantiza a lo sumo beta <= alfa, entonces la rama actual es irrelevante.

**Resultado fundamental (Knuth y Moore, 1975):** Con ordenamiento perfecto de movimientos, la poda alfa-beta reduce la complejidad de O(b^d) a O(b^(d/2)), duplicando efectivamente la profundidad de busqueda alcanzable con los mismos recursos. Esto equivale a reducir el factor de ramificacion efectivo de b a la raiz cuadrada de b.

En el ajedrez, esto significa pasar de b = 35 a un factor efectivo de aproximadamente 6, lo que hace viable la busqueda a profundidades competitivas.

### 6.4. Aplicaciones: de Deep Blue a AlphaGo

**Deep Blue** (Campbell et al., 2002) derroto al campeon mundial Garry Kasparov en 1997 utilizando minimax con poda alfa-beta, hardware especializado capaz de evaluar 200 millones de posiciones por segundo, y una funcion de evaluacion afinada por grandes maestros.

**AlphaGo** (Silver et al., 2016) represento un cambio de paradigma al combinar redes neuronales profundas con busqueda de arbol Monte Carlo (MCTS) para dominar el juego de Go, cuyo factor de ramificacion (b aproximadamente 250) y profundidad hacen inviable el enfoque clasico de minimax. La red de politica guia la seleccion de movimientos a explorar, mientras que la red de valor evalua posiciones sin necesidad de jugar hasta el final.

**AlphaGo Zero** (Silver et al., 2017) elimino por completo el conocimiento humano previo: aprendio exclusivamente mediante autopartidas (self-play) con aprendizaje por refuerzo, superando a todas las versiones anteriores. Este resultado demostro que la busqueda combinada con aprendizaje profundo puede trascender el conocimiento humano experto.

---

## 7. Algoritmos Geneticos y Computacion Evolutiva

### 7.1. Fundamentos biologicos y formalizacion

Los algoritmos geneticos (AG), introducidos por Holland (1975), son metaheuristicas de optimizacion inspiradas en la seleccion natural darwiniana. Operan sobre una poblacion de soluciones candidatas (cromosomas o individuos) que evolucionan iterativamente mediante operadores que simulan procesos biologicos.

Formalmente, un AG se define por:

- **Representacion:** codificacion de una solucion como un cromosoma (cadena binaria, vector de reales, permutacion).
- **Funcion de aptitud (fitness):** f: C -> R que cuantifica la calidad de cada cromosoma.
- **Poblacion:** conjunto de N cromosomas que evoluciona en cada generacion.
- **Operadores geneticos:** seleccion, cruzamiento y mutacion.
- **Criterio de paro:** numero maximo de generaciones, convergencia, o aptitud objetivo alcanzada.

### 7.2. Operadores geneticos

**Seleccion:** Mecanismo que favorece la reproduccion de individuos con mayor aptitud. Los metodos principales incluyen:

- Ruleta proporcional (roulette wheel): la probabilidad de seleccion de un individuo es proporcional a su fitness relativo.
- Torneo (tournament): se eligen k individuos al azar y se selecciona el de mayor fitness. Controla la presion selectiva ajustando k.
- Elitismo: los mejores n individuos pasan directamente a la siguiente generacion sin modificacion.

**Cruzamiento (crossover):** Recombina material genetico de dos padres para producir descendencia. Tipos principales:

- Un punto: se elige un punto de corte y se intercambian los segmentos.
- Dos puntos: se eligen dos puntos y se intercambia el segmento intermedio.
- Uniforme: cada gen se hereda de uno u otro padre con probabilidad 0.5.

**Mutacion:** Introduce variaciones aleatorias en un cromosoma individual. En codificacion binaria, se invierte un bit con probabilidad pm (tipicamente 0.001 a 0.01). La mutacion previene la convergencia prematura al mantener diversidad genetica en la poblacion, permitiendo la exploracion de nuevas regiones del espacio de busqueda (Goldberg, 1989).

### 7.3. Teorema del esquema de Holland

Holland (1975) demostro que los AG procesan implicitamente un numero exponencial de esquemas (patrones parciales) de manera simultanea. Un esquema H es un patron con posiciones fijas y comodines. El teorema establece que esquemas cortos, de bajo orden y con aptitud superior al promedio reciben un numero exponencialmente creciente de representantes en generaciones sucesivas.

Este resultado, conocido como el "paralelismo implicito" de los AG, explica por que los AG pueden explorar eficientemente espacios de busqueda exponencialmente grandes: no evaluan cada solucion independientemente, sino que procesan simultaneamente bloques constructivos (building blocks) que se combinan para formar soluciones cada vez mejores.

### 7.4. Teorema No Free Lunch

Wolpert y Macready (1997) demostraron el teorema No Free Lunch (NFL): promediado sobre todos los problemas posibles, ningun algoritmo de optimizacion supera a otro. Es decir, si el AG es superior a la busqueda aleatoria en un problema, necesariamente sera inferior en algun otro.

La implicacion practica del NFL es que la efectividad de un AG depende criticamente de que su representacion, operadores y parametros se ajusten a la estructura del problema especifico. No existe un algoritmo universal de optimizacion, lo que resalta la importancia del conocimiento del dominio en la aplicacion de cualquier metodo de busqueda.

---

## 8. Conexion con la Ciencia de Datos

Los algoritmos de busqueda del Bloque B no son meras abstracciones teoricas; constituyen pilares operativos de la ciencia de datos contemporanea:

**Optimizacion de hiperparametros:** La busqueda en cuadricula (grid search) es una busqueda exhaustiva en el espacio de hiperparametros. La busqueda aleatoria y los metodos bayesianos aplican estrategias mas sofisticadas. Los algoritmos geneticos se utilizan en AutoML para evolucionar arquitecturas de redes neuronales (neuroevolucion).

**Planificadores de consultas SQL:** Los optimizadores de bases de datos relacionales (PostgreSQL, Oracle) implementan variantes de A* para encontrar el plan de ejecucion de menor costo entre las multiples estrategias posibles de JOIN, escaneo e indexacion.

**Sistemas de recomendacion:** Los grafos de conocimiento se recorren mediante busquedas informadas para descubrir relaciones entre usuarios, productos y preferencias.

**Aprendizaje por refuerzo:** Los metodos de busqueda de arbol Monte Carlo (MCTS), que combinan minimax con muestreo estocastico, son fundamentales en AlphaGo y en la planificacion de agentes autonomos.

**Seleccion de caracteristicas:** Los AG se aplican como metodo wrapper para seleccionar subconjuntos optimos de features, donde cada cromosoma codifica una mascara binaria de inclusion/exclusion de variables.

---

## 9. Dimension Etica y Responsabilidad

En consonancia con el perfil de egreso de la Licenciatura en Ciencia de Datos para Negocios de la UNRC, la aplicacion de algoritmos de busqueda y optimizacion en contextos reales conlleva responsabilidades eticas significativas:

**Transparencia algoritmica:** Los sistemas de toma de decisiones automatizadas deben ser auditables. Un algoritmo A* que planifica rutas de reparto debe poder explicar por que eligio una ruta sobre otra, especialmente si las decisiones afectan condiciones laborales.

**Sesgos en funciones de evaluacion:** Las funciones heuristicas y de fitness codifican valores implicitos. Una funcion de evaluacion para contratacion automatizada puede perpetuar discriminaciones historicas si se entrena con datos sesgados.

**Uso dual de la IA en juegos y conflictos:** Los mismos algoritmos minimax que permiten jugar ajedrez se aplican en estrategia militar y ciberseguridad. La comunidad cientifica tiene la responsabilidad de considerar las implicaciones de los avances en busqueda adversarial.

**Consumo energetico:** El entrenamiento de sistemas como AlphaGo Zero requirio miles de TPUs durante dias. La eficiencia computacional de los algoritmos de busqueda tiene implicaciones ambientales directas.

---

## 10. Conclusiones

El recorrido del Bloque B revela que la busqueda no es un tema aislado sino el hilo conductor que conecta los fundamentos de la inteligencia artificial con sus aplicaciones mas avanzadas. Desde la busqueda ciega en grafos hasta la poda alfa-beta en juegos de adversario, pasando por la optimizacion evolutiva, el tema central es siempre el mismo: como explorar eficientemente un espacio de posibilidades que crece exponencialmente.

Los resultados fundamentales del bloque, como la optimalidad de A* (Hart et al., 1968), la eficiencia de IDA* (Korf, 1985), la poda alfa-beta (Knuth y Moore, 1975) y el paralelismo implicito de los AG (Holland, 1975), no son curiosidades academicas: son los cimientos sobre los que se construyen los optimizadores de bases de datos, los sistemas de planificacion, los motores de juego y los frameworks de AutoML que un cientifico de datos utiliza cotidianamente.

La leccion mas profunda del No Free Lunch (Wolpert y Macready, 1997) es que no existe un algoritmo universal: la eleccion del metodo de busqueda correcto requiere comprender tanto la estructura del problema como las garantias y limitaciones de cada algoritmo. Esa comprension es precisamente lo que distingue al cientifico de datos del usuario de herramientas.

---

## Referencias

Campbell, M., Hoane, A. J., y Hsu, F. H. (2002). Deep Blue. *Artificial Intelligence*, 134(1-2), 57-83. https://doi.org/10.1016/S0004-3702(01)00129-1

Dijkstra, E. W. (1959). A note on two problems in connexion with graphs. *Numerische Mathematik*, 1(1), 269-271. https://doi.org/10.1007/BF01386390

Goldberg, D. E. (1989). *Genetic algorithms in search, optimization, and machine learning*. Addison-Wesley.

Hart, P. E., Nilsson, N. J., y Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths. *IEEE Transactions on Systems Science and Cybernetics*, 4(2), 100-107. https://doi.org/10.1109/TSSC.1968.300136

Holland, J. H. (1975). *Adaptation in natural and artificial systems*. University of Michigan Press.

Knuth, D. E., y Moore, R. W. (1975). An analysis of alpha-beta pruning. *Artificial Intelligence*, 6(4), 293-326. https://doi.org/10.1016/0004-3702(75)90019-3

Korf, R. E. (1985). Depth-first iterative-deepening: An optimal admissible tree search. *Artificial Intelligence*, 27(1), 97-109. https://doi.org/10.1016/0004-3702(85)90084-0

Martelli, A., y Montanari, U. (1973). Additive AND/OR graphs. *Proceedings of the Third International Joint Conference on Artificial Intelligence*, 1-11.

Newell, A., y Simon, H. A. (1972). *Human problem solving*. Prentice-Hall.

Nilsson, N. J. (1980). *Principles of artificial intelligence*. Tioga Publishing.

Pearl, J. (1984). *Heuristics: Intelligent search strategies for computer problem solving*. Addison-Wesley.

Russell, S., y Norvig, P. (2021). *Artificial intelligence: A modern approach* (4ta ed.). Pearson.

Shannon, C. E. (1950). Programming a computer for playing chess. *The London, Edinburgh, and Dublin Philosophical Magazine*, 41(314), 256-275. https://doi.org/10.1080/14786445008521796

Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., van den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., Dieleman, S., Grewe, D., Nham, J., Kalchbrenner, N., Sutskever, I., Lillicrap, T., Leach, M., Kavukcuoglu, K., Graepel, T., y Hassabis, D. (2016). Mastering the game of Go with deep neural networks and tree search. *Nature*, 529(7587), 484-489. https://doi.org/10.1038/nature16961

Silver, D., Schrittwieser, J., Simonyan, K., Antonoglou, I., Huang, A., Guez, A., Hubert, T., Baker, L., Lai, M., Bolton, A., Chen, Y., Lillicrap, T., Hui, F., Sifre, L., van den Driessche, G., Graepel, T., y Hassabis, D. (2017). Mastering the game of Go without human knowledge. *Nature*, 550(7676), 354-359. https://doi.org/10.1038/nature24270

Von Neumann, J., y Morgenstern, O. (1944). *Theory of games and economic behavior*. Princeton University Press.

Wolpert, D. H., y Macready, W. G. (1997). No free lunch theorems for optimization. *IEEE Transactions on Evolutionary Computation*, 1(1), 67-82. https://doi.org/10.1109/4235.585893
