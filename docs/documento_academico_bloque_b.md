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
   7.3. Ejemplo paso a paso: optimizando una funcion simple
   7.4. Teorema del esquema de Holland
   7.5. Teorema No Free Lunch
8. Conexion con la Ciencia de Datos
9. Dimension Etica y Responsabilidad
10. Conclusiones
Referencias

---

## 1. Introduccion y Motivacion

La busqueda constituye el mecanismo computacional fundamental mediante el cual un agente inteligente explora sistematicamente un espacio de posibilidades para encontrar una solucion a un problema dado. Historicamente, los primeros programas de inteligencia artificial, como el General Problem Solver de Newell y Simon (1972), operaban esencialmente como algoritmos de busqueda sobre representaciones simbolicas del conocimiento.

Para entender la importancia practica de estos algoritmos, pensemos en algo cotidiano: cuando Google Maps calcula la ruta mas corta entre dos puntos en una ciudad con miles de calles y cruces, lo que hace internamente es resolver un problema de busqueda sobre un grafo. Cada interseccion es un nodo, cada calle es una arista con un costo (distancia, tiempo), y el algoritmo tiene que encontrar el camino optimo entre el origen y el destino. Sin algoritmos de busqueda eficientes, esa consulta que hoy toma milisegundos podria tomar horas.

Russell y Norvig (2021) establecen que la formulacion de un problema de busqueda requiere cinco componentes: un estado inicial, una funcion de acciones aplicables, un modelo de transicion, una prueba de meta y una funcion de costo de camino. Esta abstraccion resulta notablemente general: desde la navegacion de un robot en un almacen hasta la demostracion automatica de teoremas, la estructura subyacente es un grafo de estados que debe recorrerse de manera eficiente.

El reto central es que estos espacios crecen de forma exponencial. Si un problema tiene b opciones en cada paso y la solucion requiere d pasos, el espacio total tiene del orden de b^d estados. Con b = 10 y d = 12, eso ya son un billon de posibilidades. Los algoritmos que se estudian en este bloque son, en esencia, estrategias distintas para manejar esa explosion combinatoria: algunos la enfrentan de frente (busqueda ciega), otros la recortan con conocimiento del problema (heuristicas), y otros la esquivan por completo cambiando la metafora de "buscar" por la de "evolucionar" (algoritmos geneticos).

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

Para dar una referencia tangible: el numero de atomos en el universo observable se estima en 10^80. El espacio de estados del Go supera esa cifra por 90 ordenes de magnitud. Eso significa que aun si cada atomo del universo fuera una computadora evaluando un millon de estados por segundo, no alcanzaria la edad del universo para recorrer ese espacio exhaustivamente.

### 2.2. Ejemplo: el rompecabezas de 8 piezas

El 8-puzzle es un problema clasico con 9!/2 = 181,440 estados alcanzables. Cada estado es una configuracion de las fichas numeradas del 1 al 8 en una cuadricula 3x3, con una casilla vacia. Las acciones consisten en deslizar una ficha adyacente al espacio vacio. La prueba de meta es alcanzar la configuracion ordenada.

Para concretar, veamos una transicion de estados. Supongamos la siguiente configuracion inicial (el guion bajo representa la casilla vacia):

```
Estado inicial:         Despues de mover         Despues de mover
                        el 5 arriba:             el 6 a la izquierda:

  1  2  3                1  2  3                  1  2  3
  4  _  6       ->       4  5  6        ->        4  5  6
  7  5  8                7  _  8                  7  8  _
```

En la primera transicion, la unica ficha que puede moverse al espacio vacio (posicion central) incluye al 2 (arriba), 4 (izquierda), 6 (derecha) y 5 (abajo). Al mover el 5 arriba, se genera un nuevo estado. Cada uno de estos movimientos posibles corresponde a una arista en el grafo del espacio de estados, y el factor de ramificacion promedio del 8-puzzle es aproximadamente 3 (ya que la casilla vacia tiene entre 2 y 4 vecinos segun su posicion).

Este problema ha servido como benchmark historico para comparar algoritmos de busqueda. Korf (1985) demostro que la busqueda iterativa en profundidad (IDA*) con la heuristica de distancia Manhattan resuelve instancias del 15-puzzle (cuyo espacio tiene 10^13 estados) de manera optima con memoria lineal, un resultado que revoluciono el campo.

El paso de la representacion formal a un problema concreto como el 8-puzzle ilustra un patron que se repite en todo el bloque: definir bien los estados y las transiciones es la mitad del trabajo. Los algoritmos que vienen a continuacion son las herramientas para recorrer ese espacio una vez que esta definido.

---

## 3. Estrategias de Busqueda No Informada

Los algoritmos de busqueda no informada (ciega) no utilizan informacion sobre la distancia al estado meta. Se distinguen por cuatro criterios de evaluacion (Russell y Norvig, 2021):

- **Completitud:** si la solucion existe, el algoritmo la encuentra.
- **Optimalidad:** el algoritmo encuentra la solucion de menor costo.
- **Complejidad temporal:** numero de nodos generados.
- **Complejidad espacial:** numero maximo de nodos en memoria.

Sea b el factor de ramificacion y d la profundidad de la solucion mas superficial.

Para ilustrar las diferencias entre algoritmos, usaremos el siguiente grafo simple a lo largo de esta seccion:

```
         A
        / \
       B   C
      / \   \
     D   E   F
        / \
       G   H  (meta)
```

El estado inicial es A y la meta es H. La solucion optima tiene profundidad d = 3 (A -> B -> E -> H).

### 3.1. Busqueda en anchura (BFS)

Explora el arbol de busqueda nivel por nivel, expandiendo todos los nodos de profundidad k antes de pasar a profundidad k+1. Utiliza una cola FIFO como frontera.

**Pseudocodigo:**

```
funcion BFS(problema):
    nodo = crear_nodo(problema.estado_inicial)
    si es_meta(nodo.estado): retornar solucion(nodo)
    frontera = cola_FIFO con {nodo}
    explorados = conjunto vacio

    mientras frontera no este vacia:
        nodo = frontera.extraer()
        explorados.agregar(nodo.estado)

        para cada accion en problema.acciones(nodo.estado):
            hijo = crear_nodo(resultado(nodo, accion))
            si hijo.estado no esta en explorados ni en frontera:
                si es_meta(hijo.estado): retornar solucion(hijo)
                frontera.insertar(hijo)

    retornar fallo
```

**Traza sobre el grafo ejemplo:**

| Paso | Nodo expandido | Frontera (cola FIFO) | Explorados |
|------|---------------|----------------------|------------|
| 1    | A             | [B, C]               | {A}        |
| 2    | B             | [C, D, E]            | {A, B}     |
| 3    | C             | [D, E, F]            | {A, B, C}  |
| 4    | D             | [E, F]               | {A, B, C, D} |
| 5    | E             | [F, G, H]            | {A, B, C, D, E} |
| 6    | F             | [G, H]               | {A, B, C, D, E, F} |
| 7    | G             | [H]                  | {A, B, C, D, E, F, G} |
| 8    | H             | Meta encontrada       | Solucion: A-B-E-H |

BFS exploro 8 nodos y encontro la solucion a profundidad 3. Noten que reviso todos los nodos de profundidad 2 (D, E, F) antes de llegar a profundidad 3.

**Propiedades:**

- Completitud: Si, si b es finito.
- Optimalidad: Si, cuando el costo es uniforme (todos los pasos cuestan igual).
- Tiempo: O(b^d).
- Espacio: O(b^d).

La complejidad espacial es el talon de Aquiles de BFS. Para b = 10 y d = 12, la frontera requiere almacenar 10^12 nodos, lo cual excede la memoria de cualquier computadora actual (Nilsson, 1980). En terminos practicos, si cada nodo ocupa 1 KB, eso seria un petabyte de RAM solo para la frontera.

**Aplicacion practica:** BFS es el algoritmo detras del calculo de "grados de separacion" en redes sociales. LinkedIn, por ejemplo, muestra si un contacto esta a 1, 2 o 3 conexiones de distancia. Eso se computa con BFS partiendo del usuario, explorando nivel por nivel (conexiones directas, conexiones de conexiones, etc.).

### 3.2. Busqueda en profundidad (DFS)

Explora el arbol siguiendo una rama hasta su maxima profundidad antes de retroceder. Utiliza una pila LIFO como frontera (o recursion).

**Pseudocodigo (version recursiva):**

```
funcion DFS(nodo, problema, explorados):
    si es_meta(nodo.estado): retornar solucion(nodo)
    explorados.agregar(nodo.estado)

    para cada accion en problema.acciones(nodo.estado):
        hijo = crear_nodo(resultado(nodo, accion))
        si hijo.estado no esta en explorados:
            resultado = DFS(hijo, problema, explorados)
            si resultado != fallo: retornar resultado

    retornar fallo
```

**Traza sobre el mismo grafo (asumiendo que los hijos se procesan de izquierda a derecha):**

| Paso | Nodo expandido | Pila (frontera) | Profundidad actual |
|------|---------------|-----------------|-------------------|
| 1    | A             | [C, B]          | 0                 |
| 2    | B             | [C, E, D]       | 1                 |
| 3    | D             | [C, E]          | 2 (hoja, backtrack) |
| 4    | E             | [C, H, G]       | 2                 |
| 5    | G             | [C, H]          | 3 (hoja, backtrack) |
| 6    | H             | Meta encontrada  | Solucion: A-B-E-H |

DFS encontro la solucion en 6 expansiones (frente a las 8 de BFS en este caso), pero esto es suerte del ordenamiento. Si H estuviera bajo F en vez de bajo E, DFS habria explorado toda la rama izquierda primero sin encontrar nada util.

**Propiedades:**

- Completitud: No en espacios infinitos o con ciclos (si, en grafos finitos con deteccion de repetidos).
- Optimalidad: No.
- Tiempo: O(b^m), donde m es la profundidad maxima del arbol.
- Espacio: O(bm), es decir, lineal en la profundidad.

La ventaja fundamental de DFS es su eficiencia en memoria: requiere almacenar solo O(bm) nodos, frente a los O(b^d) de BFS. Esta propiedad la hace viable para espacios de busqueda muy grandes cuando la solucion se encuentra a profundidad razonable. En el ejemplo, DFS solo mantuvo a lo mas 4 nodos en la pila, mientras que BFS llego a tener 3.

**Aplicacion practica:** DFS es la base de los web crawlers que indexan sitios web. Un crawler que sigue enlaces recursivamente desde una pagina raiz esta haciendo DFS sobre el grafo de la web. Tambien es el patron natural de la exploracion de laberintos: "sigue el muro izquierdo hasta el fondo, luego regresa y prueba la siguiente rama."

### 3.3. Busqueda en profundidad limitada e iterativa (IDS)

Korf (1985) propuso la busqueda iterativa en profundidad (Iterative Deepening Search), que combina las ventajas de BFS y DFS. Ejecuta sucesivas busquedas DFS con limites de profundidad crecientes: primero busca a profundidad 0, luego 1, luego 2, y asi sucesivamente.

**Pseudocodigo:**

```
funcion IDS(problema):
    para profundidad_limite = 0, 1, 2, ...:
        resultado = DFS_limitada(problema.estado_inicial, problema, profundidad_limite)
        si resultado != corte: retornar resultado

funcion DFS_limitada(nodo, problema, limite):
    si es_meta(nodo.estado): retornar solucion(nodo)
    si limite == 0: retornar corte

    hubo_corte = falso
    para cada accion en problema.acciones(nodo.estado):
        hijo = crear_nodo(resultado(nodo, accion))
        resultado = DFS_limitada(hijo, problema, limite - 1)
        si resultado == corte: hubo_corte = verdadero
        si resultado != fallo y resultado != corte: retornar resultado

    si hubo_corte: retornar corte
    sino: retornar fallo
```

**Propiedades:**

- Completitud: Si.
- Optimalidad: Si, cuando el costo es uniforme.
- Tiempo: O(b^d).
- Espacio: O(bd).

Aunque pareciera ineficiente regenerar los niveles superiores, el trabajo redundante es insignificante: la capa d tiene b^d nodos, y el trabajo total de IDS es aproximadamente b^d * b/(b-1), un factor constante respecto a BFS. Para b = 10, el factor es 10/9 = 1.11, o sea que IDS hace apenas 11% mas trabajo que BFS, pero con memoria lineal en vez de exponencial. Esa es una de esas asimetrias que al principio no resultan intuitivas: regenerar niveles parece un desperdicio, pero el crecimiento exponencial hace que el ultimo nivel domine completamente el costo total.

IDS es el algoritmo de busqueda no informada preferido cuando el espacio de estados es grande y la profundidad de la solucion es desconocida (Russell y Norvig, 2021).

### 3.4. Busqueda de costo uniforme

Generaliza BFS para costos de arista no uniformes. Expande el nodo con menor costo acumulado g(n), utilizando una cola de prioridad. Es completa y optima siempre que los costos sean positivos (Dijkstra, 1959). Su complejidad temporal y espacial es O(b^(1+C*/epsilon)), donde C* es el costo de la solucion optima y epsilon es el costo minimo de una arista.

**Ejemplo concreto:** Supongamos que queremos ir de la ciudad A a la ciudad H, pero las carreteras tienen distancias distintas:

```
A --1-- B --3-- E --2-- H
|               |
4               1
|               |
C ------5----- F
        |
        2
        |
        G
```

BFS encontraria A-B-E-H (3 aristas). Pero la busqueda de costo uniforme evalua costos acumulados: el camino A-B-E-H tiene costo 1+3+2 = 6. Si existiera un camino A-C-F-H con costo 4+5+? = ... bueno, en este caso no hay arista directa F-H, asi que la solucion sigue siendo A-B-E-H con costo 6. El punto es que costo uniforme expande siempre el nodo con menor g(n) acumulado, lo que garantiza optimalidad aun cuando las aristas tienen pesos distintos.

Este es exactamente el algoritmo de Dijkstra (1959), que sigue siendo la base de los sistemas de navegacion GPS cuando no se dispone de una heuristica para estimar la distancia al destino.

Con las estrategias de busqueda ciega cubiertas, surge una pregunta natural: si el agente no tiene ninguna informacion sobre donde esta la meta, solo puede explorar sistematicamente. Pero en muchos problemas reales si tenemos pistas sobre la direccion correcta. Antes de ver como aprovechar esas pistas (seccion 5), conviene entender otra dimension de la busqueda: la direccion en la que se recorre el espacio.

---

## 4. Busqueda Hacia Adelante y Hacia Atras

### 4.1. Busqueda hacia adelante (forward chaining)

La busqueda hacia adelante, tambien denominada encadenamiento progresivo o data-driven search, parte del estado inicial y aplica acciones sucesivas hacia la meta. Es el paradigma natural de la mayoria de los algoritmos de busqueda (BFS, DFS, A*). En sistemas basados en reglas, corresponde al encadenamiento hacia adelante: si los datos satisfacen las premisas de una regla, se ejecuta la accion y se produce un nuevo estado.

**Ejemplo concreto:** Pensemos en un sistema de diagnostico medico simplificado con tres reglas:

```
Regla 1: SI fiebre Y tos ENTONCES posible_gripe
Regla 2: SI posible_gripe Y dolor_muscular ENTONCES diagnostico = gripe
Regla 3: SI fiebre Y erupcion ENTONCES diagnostico = sarampion
```

Dado un paciente con los sintomas {fiebre, tos, dolor_muscular}, la busqueda hacia adelante opera asi:
1. Datos iniciales: {fiebre, tos, dolor_muscular}
2. La Regla 1 se activa (fiebre Y tos): se agrega posible_gripe al conjunto de hechos.
3. La Regla 2 se activa (posible_gripe Y dolor_muscular): se concluye diagnostico = gripe.

El sistema partio de los datos y "avanzo" hasta llegar a una conclusion. Cada paso genero nuevos hechos que habilitaron nuevas reglas.

Su ventaja principal radica en que solo genera estados alcanzables desde el estado inicial, evitando explorar regiones del espacio de estados irrelevantes para el problema. Esto lo hace adecuado cuando el numero de datos iniciales es pequeno y las reglas van acumulando conclusiones progresivamente.

### 4.2. Busqueda hacia atras (backward chaining)

La busqueda hacia atras parte del estado meta y trabaja en sentido inverso, buscando que acciones pudieron producir ese estado. En planificacion automatica, corresponde a la regresion: dado un estado meta G, se identifican las acciones cuyo efecto incluye algun subobjetivo de G, y se computa el estado predecesor necesario.

**Ejemplo concreto (mismo sistema):** Si queremos saber si el paciente tiene gripe:
1. Meta: diagnostico = gripe
2. Buscamos que regla produce "diagnostico = gripe": Regla 2 requiere posible_gripe Y dolor_muscular.
3. Submeta: demostrar posible_gripe. Buscamos que regla la produce: Regla 1 requiere fiebre Y tos.
4. Verificamos: fiebre esta en los datos? Si. tos esta en los datos? Si. Entonces posible_gripe = verdadero.
5. Verificamos: dolor_muscular esta en los datos? Si. Conclusion: diagnostico = gripe.

La diferencia con la busqueda hacia adelante es sutil pero practica: aqui no activamos la Regla 3 (sarampion) en ningun momento, porque nunca fue necesaria para probar nuestra meta. La busqueda hacia atras es mas dirigida, solo investiga lo que necesita para confirmar o refutar el objetivo.

Este enfoque resulta eficiente cuando el conjunto de estados meta es pequeno pero el factor de ramificacion hacia adelante es grande. En demostracion automatica de teoremas, por ejemplo, es mas natural partir del teorema a demostrar y buscar las premisas que lo sustenten (Nilsson, 1980). Prolog, el lenguaje de programacion logica, usa busqueda hacia atras como su mecanismo fundamental de inferencia.

### 4.3. Busqueda bidireccional

La busqueda bidireccional ejecuta simultaneamente una busqueda hacia adelante desde el estado inicial y una busqueda hacia atras desde la meta, hasta que ambas fronteras se intersectan.

Su ventaja teorica es considerable: si la busqueda unidireccional tiene complejidad O(b^d), la bidireccional tiene O(2 * b^(d/2)) = O(b^(d/2)), una reduccion exponencial. Para b = 10 y d = 12, esto significa 2 * 10^6 nodos en lugar de 10^12. Dicho de otro modo: en vez de buscar una aguja en un pajar, dos personas buscan desde extremos opuestos del pajar y se encuentran a la mitad.

**Ejemplo practico:** Supongamos que queremos encontrar la ruta mas corta entre Ciudad de Mexico y Monterrey en un mapa de carreteras. La busqueda unidireccional desde CDMX exploraria ciudades en circulos concentricos cada vez mas grandes (Puebla, Queretaro, Toluca, Cuernavaca...) hasta alcanzar Monterrey. La bidireccional lanza una busqueda desde CDMX y otra desde Monterrey simultaneamente. Las dos fronteras se encuentran en algun punto intermedio (probablemente cerca de San Luis Potosi), y al combinarse forman la ruta completa. El ahorro es dramatico porque cada busqueda solo necesita cubrir la mitad de la distancia.

La dificultad practica reside en computar eficientemente los predecesores de un estado y en disenar un criterio de terminacion correcto que garantice optimalidad (Russell y Norvig, 2021). Ademas, no siempre es trivial invertir las acciones: en el 8-puzzle se puede (cada movimiento es reversible), pero en un problema donde las acciones son irreversibles, como en quimica (mezclar reactivos), la busqueda hacia atras puede no tener sentido.

Las secciones anteriores han cubierto como explorar un espacio de estados (seccion 3) y en que direccion hacerlo (seccion 4). La siguiente pregunta natural es: podemos ser mas inteligentes en la exploracion? Si sabemos algo sobre donde esta la meta, podemos usar ese conocimiento para evitar explorar regiones inútiles. Esa es precisamente la idea detras de la busqueda informada.

---

## 5. Busqueda Informada y Reduccion de Problemas

### 5.1. Funciones heuristicas: admisibilidad y consistencia

Una funcion heuristica h(n) estima el costo desde el nodo n hasta la meta mas cercana. Se dice que h es:

- **Admisible** si nunca sobreestima el costo real: h(n) <= h*(n) para todo n, donde h*(n) es el costo real optimo.
- **Consistente** (o monotona) si para todo nodo n y sucesor n' generado por la accion a: h(n) <= c(n, a, n') + h(n').

Toda heuristica consistente es admisible, pero no al reves. La consistencia garantiza que los valores de f(n) = g(n) + h(n) son no decrecientes a lo largo de cualquier camino, lo que simplifica la demostracion de optimalidad de A* (Pearl, 1984).

Una intuicion util: la admisibilidad dice "soy optimista, nunca digo que falta mas de lo que realmente falta". La consistencia dice algo mas fuerte: "mi optimismo es coherente entre nodos vecinos". En la practica, la mayoria de las heuristicas utiles cumplen ambas propiedades.

**Ejemplos clasicos para el 8-puzzle:**

- h1: numero de fichas mal colocadas (admisible, subestima).
- h2: suma de distancias Manhattan de cada ficha a su posicion meta (admisible, domina a h1).

Para concretar la diferencia, consideremos esta configuracion del 8-puzzle:

```
Estado actual:       Estado meta:
  1  2  3             1  2  3
  4  _  6             4  5  6
  7  5  8             7  8  _
```

Calculemos ambas heuristicas:
- h1 (fichas mal colocadas): las fichas 5, 6 y 8 estan fuera de lugar, asi que h1 = 3.
- h2 (distancias Manhattan): la ficha 5 esta a 1 movimiento de su lugar, la 6 esta a 1, y la 8 esta a 1. Total: h2 = 3.

Pero en otra configuracion la diferencia puede ser mayor. Si el 5 estuviera en la esquina superior izquierda en vez de su posicion meta (centro), h1 seguiria contandolo como 1 ficha mal colocada, pero h2 contaria que necesita moverse 2 pasos (1 horizontal + 1 vertical). Manhattan captura "que tan lejos" esta cada ficha, no solo si esta o no en su sitio.

Pearl (1984) demostro que si h2(n) >= h1(n) para todo n (h2 domina a h1), entonces A* con h2 expande un subconjunto de los nodos que A* expandiria con h1. Por lo tanto, heuristicas mas informadas producen busquedas mas eficientes.

### 5.2. Algoritmo A

El Algoritmo A es la version basica de busqueda best-first que utiliza la funcion de evaluacion f(n) = g(n) + h(n), donde g(n) es el costo del camino desde el inicio hasta n, y h(n) es una estimacion heuristica del costo restante. Sin restricciones sobre h, el Algoritmo A no garantiza optimalidad. Es, en cierto sentido, el "esqueleto" que A* hereda y fortalece con la exigencia de admisibilidad.

### 5.3. Algoritmo A*

Hart, Nilsson y Raphael (1968) introdujeron A* como una extension del Algoritmo A con la restriccion de que h sea admisible. Este resultado fundamental establece que:

**Teorema (Hart et al., 1968):** Si h es admisible, A* es completo y optimo. Es decir, la primera solucion que A* encuentra es necesariamente la de menor costo.

**Teorema de optimalidad de eficiencia:** Ningun otro algoritmo que use la misma informacion heuristica puede garantizar expandir menos nodos que A* sin sacrificar optimalidad (dada una heuristica consistente).

**Pseudocodigo de A*:**

```
funcion A_estrella(problema, h):
    nodo_inicial = crear_nodo(problema.estado_inicial)
    nodo_inicial.g = 0
    nodo_inicial.f = h(nodo_inicial)
    abierta = cola_prioridad ordenada por f, con {nodo_inicial}
    cerrada = conjunto vacio

    mientras abierta no este vacia:
        nodo = abierta.extraer_minimo()

        si es_meta(nodo.estado): retornar solucion(nodo)

        cerrada.agregar(nodo.estado)

        para cada accion en problema.acciones(nodo.estado):
            hijo = crear_nodo(resultado(nodo, accion))
            hijo.g = nodo.g + costo(nodo, accion, hijo)
            hijo.f = hijo.g + h(hijo)

            si hijo.estado esta en cerrada: continuar
            si hijo.estado esta en abierta con f menor: continuar
            abierta.insertar(hijo)

    retornar fallo
```

**Ejemplo paso a paso: A* en un mapa de ciudades**

Consideremos un mapa simplificado donde queremos ir de la ciudad S (inicio) a la ciudad G (meta). Las distancias reales entre ciudades son los costos de las aristas, y la heuristica h es la distancia en linea recta al destino (siempre admisible porque la linea recta nunca sobreestima la distancia real por carretera).

```
Mapa:                          Distancias en linea recta a G:
S --3-- A --2-- G              h(S) = 6
|       |                      h(A) = 2
1       4                      h(B) = 5
|       |                      h(C) = 4
B --5-- C --3-- G              h(G) = 0
```

Hay dos caminos de S a G:
- S -> A -> G: costo real = 3 + 2 = 5
- S -> B -> C -> G: costo real = 1 + 5 + 3 = 9

Veamos como A* lo descubre sin explorar todo:

| Paso | Extraer | g | h | f=g+h | Abierta (nodo: f)           | Accion |
|------|---------|---|---|-------|-----------------------------|--------|
| 0    | -       | - | - | -     | {S: 0+6=6}                 | Inicio |
| 1    | S       | 0 | 6 | 6     | {A: 3+2=5, B: 1+5=6}       | Expandir S |
| 2    | A       | 3 | 2 | 5     | {B: 1+5=6, G: 5+0=5}       | Expandir A |
| 3    | G       | 5 | 0 | 5     | Meta! Solucion: S-A-G, costo 5 | |

A* encontro la solucion optima (S-A-G, costo 5) sin necesidad de explorar B ni C. La heuristica le dijo que A estaba "mas cerca" de G (h=2) y le dio prioridad. Noten que en el paso 2, A* elige entre expandir A (f=5) y B (f=6): elige A porque tiene menor f. Al expandir A, descubre la meta directamente.

Si hubieramos usado busqueda de costo uniforme (h=0 para todos), habriamos expandido B primero (g=1 < g=3 para A), y luego C, antes de llegar a A y finalmente a G. A* se ahorro esas exploraciones gracias a la heuristica.

La complejidad temporal de A* depende criticamente de la calidad de la heuristica. Con una heuristica perfecta (h = h*), A* va directo a la solucion en O(d). Con h = 0 (sin informacion), A* degenera en busqueda de costo uniforme. En el peor caso, la complejidad es exponencial, pero en la practica heuristicas bien disenadas reducen drasticamente el espacio explorado.

La principal limitacion de A* es su consumo de memoria: almacena todos los nodos generados, lo que puede agotar la RAM antes de encontrar la solucion. Este es un problema real en aplicaciones como planificacion de rutas en mapas nacionales con millones de nodos.

### 5.4. Algoritmo IDA*

Korf (1985) propuso Iterative Deepening A* (IDA*) para resolver el problema de memoria de A*. IDA* realiza sucesivas busquedas en profundidad, pero en lugar de usar la profundidad como limite, usa el valor de f:

1. Establecer el umbral t = f(s0) = h(s0).
2. Ejecutar DFS, podando nodos donde f(n) > t.
3. Si no se encontro solucion, actualizar t al menor valor de f que excedio el umbral.
4. Repetir.

IDA* es completo, optimo (con h admisible) y usa memoria lineal O(bd). Es el algoritmo de eleccion para problemas con espacios de estados muy grandes y costos uniformes. Korf lo utilizo para resolver de manera optima todas las instancias del 15-puzzle, un logro notable considerando que el espacio tiene mas de 10^13 estados.

La relacion entre A* e IDA* es analoga a la que vimos entre BFS e IDS en la seccion 3: IDA* sacrifica algo de tiempo (regenera nodos) para obtener memoria lineal, exactamente el mismo trade-off que convertia a IDS en el algoritmo no informado preferido.

### 5.5. Grafos AND/OR y Algoritmo AO*

Algunos problemas admiten descomposicion: resolver el problema principal equivale a resolver un conjunto de subproblemas. Esta estructura se representa mediante grafos AND/OR:

- **Nodo OR:** se resuelve si al menos uno de sus hijos se resuelve (alternativas).
- **Nodo AND:** se resuelve solo si todos sus hijos se resuelven (subproblemas obligatorios).

**Ejemplo concreto:** Supongamos que queremos preparar una cena (nodo raiz, OR):

```
Preparar cena (OR)
├── Opcion 1: Cocinar pasta (AND)
│   ├── Hervir agua
│   ├── Cocer la pasta
│   └── Preparar salsa
└── Opcion 2: Pedir comida (AND)
    ├── Elegir restaurante
    └── Hacer el pedido
```

El nodo raiz es OR porque basta con elegir una opcion. Pero cada opcion es AND porque necesitamos completar todos sus subpasos. AO* exploraria ambas opciones y calcularia el costo total de cada una (sumando los costos de todos los subpasos del AND), para elegir la opcion mas barata.

El algoritmo AO* (Martelli y Montanari, 1973) generaliza A* para grafos AND/OR. Mantiene un grafo de solucion parcial y en cada iteracion:

1. Selecciona el nodo hoja no resuelto mas prometedor del grafo de solucion actual.
2. Lo expande.
3. Actualiza los costos de manera ascendente (bottom-up) por el grafo.
4. Revisa el grafo de solucion optimo.

AO* es relevante en planificacion con incertidumbre, donde las acciones pueden tener multiples resultados (nodos AND representan los posibles resultados, todos los cuales deben poder manejarse). Tambien se utiliza en demostracion automatica de teoremas, en descomposicion jerarquica de tareas, y en compiladores que optimizan expresiones descomponiendolas en sub-expresiones.

Los algoritmos de busqueda vistos hasta aqui asumen un agente unico que busca una solucion en un entorno pasivo. La siguiente seccion aborda un escenario radicalmente distinto: que pasa cuando hay un adversario que activamente intenta frustrar nuestros planes?

---

## 6. Juegos de Adversario: Minimax y Poda Alfa-Beta

### 6.1. Arboles de juego y el teorema minimax

Un juego de adversario de suma cero con informacion perfecta se modela como un arbol donde los niveles alternan entre los movimientos de MAX (jugador que maximiza) y MIN (jugador que minimiza). En los nodos terminales, una funcion de utilidad asigna un valor numerico que refleja el resultado (victoria, derrota, empate).

Von Neumann demostro el teorema minimax en 1928, formalizado extensamente en Von Neumann y Morgenstern (1944): en un juego finito de suma cero con informacion perfecta, existe una estrategia optima para cada jugador y un valor del juego determinado. Este resultado fundamental establece que la teoria de juegos tiene una solucion racional bien definida.

En terminos mas concretos: para cualquier juego como ajedrez o damas, existe un resultado teorico "perfecto" (victoria de blancas, empate, o victoria de negras) que ambos jugadores alcanzarian si jugaran de forma optima. Para las damas, ese valor se determino computacionalmente en 2007: con juego perfecto de ambos lados, el resultado es empate (Schaeffer et al., 2007).

### 6.2. El algoritmo minimax

El algoritmo minimax (Russell y Norvig, 2021) computa recursivamente el valor minimax de cada nodo:

- Si n es terminal: valor(n) = utilidad(n).
- Si n es nodo MAX: valor(n) = max sobre los hijos de n de valor(hijo).
- Si n es nodo MIN: valor(n) = min sobre los hijos de n de valor(hijo).

**Pseudocodigo:**

```
funcion minimax(nodo, profundidad, es_maximizador):
    si profundidad == 0 o nodo es terminal:
        retornar evaluacion(nodo)

    si es_maximizador:
        mejor = -infinito
        para cada hijo de nodo:
            valor = minimax(hijo, profundidad - 1, falso)
            mejor = max(mejor, valor)
        retornar mejor

    sino:  // es minimizador
        mejor = +infinito
        para cada hijo de nodo:
            valor = minimax(hijo, profundidad - 1, verdadero)
            mejor = min(mejor, valor)
        retornar mejor
```

**Ejemplo paso a paso: gato (tic-tac-toe) simplificado**

Para hacer la traza manejable, veamos un arbol de juego pequeno donde MAX elige entre tres movimientos, cada uno con dos respuestas de MIN, y los nodos terminales tienen valores de utilidad:

```
                    MAX (raiz)
                 /      |      \
              MIN      MIN      MIN
             /   \    /   \    /   \
            3     5  2     9  0     7
```

Paso 1: Evaluar los nodos terminales (ya tienen valor).

Paso 2: Calcular los nodos MIN (cada uno elige el minimo de sus hijos):
- MIN izquierdo: min(3, 5) = 3
- MIN central: min(2, 9) = 2
- MIN derecho: min(0, 7) = 0

Paso 3: Calcular el nodo MAX (elige el maximo de sus hijos):
- MAX: max(3, 2, 0) = 3

```
                    MAX = 3
                 /      |      \
            MIN=3    MIN=2    MIN=0
             /   \    /   \    /   \
            3     5  2     9  0     7
```

El valor minimax de la raiz es 3. MAX elige la rama izquierda (que garantiza al menos 3), porque asume que MIN jugara de forma optima. Aunque la rama central tiene un nodo terminal de valor 9, MIN nunca lo dejaria llegar ahi (elegiria el 2). La logica de minimax es pesimista: "asumo que mi oponente juega lo mejor posible, y elijo lo que maximiza mi peor caso."

El algoritmo realiza una exploracion completa en profundidad (DFS) del arbol de juego. Su complejidad es O(b^m), donde b es el factor de ramificacion y m es la profundidad maxima. Para el ajedrez, con b aproximadamente 35 y m aproximadamente 80, esto es computacionalmente intratable.

En la practica, minimax se combina con:
- **Profundidad limitada:** se corta la busqueda a profundidad d y se aplica una funcion de evaluacion heuristica en los nodos hoja.
- **Quiescence search:** se extiende la busqueda en posiciones "inestables" (capturas, jaques) para evitar el efecto horizonte, que ocurre cuando un movimiento desastroso queda justo fuera del alcance de la busqueda.

### 6.3. Poda alfa-beta

Knuth y Moore (1975) analizaron formalmente la poda alfa-beta, un metodo que elimina ramas del arbol de juego que no pueden influir en la decision final. El algoritmo mantiene dos valores:

- **alfa:** el mejor valor que MAX puede garantizar en el camino actual (limite inferior).
- **beta:** el mejor valor que MIN puede garantizar en el camino actual (limite superior).

La poda ocurre cuando alfa >= beta: si MAX ya tiene una opcion que garantiza al menos alfa, y MIN tiene una opcion que garantiza a lo sumo beta <= alfa, entonces la rama actual es irrelevante.

**Pseudocodigo:**

```
funcion alfa_beta(nodo, profundidad, alfa, beta, es_maximizador):
    si profundidad == 0 o nodo es terminal:
        retornar evaluacion(nodo)

    si es_maximizador:
        valor = -infinito
        para cada hijo de nodo:
            valor = max(valor, alfa_beta(hijo, profundidad-1, alfa, beta, falso))
            alfa = max(alfa, valor)
            si alfa >= beta:
                break    // poda beta: MIN no elegira esta rama
        retornar valor

    sino:
        valor = +infinito
        para cada hijo de nodo:
            valor = min(valor, alfa_beta(hijo, profundidad-1, alfa, beta, verdadero))
            beta = min(beta, valor)
            si alfa >= beta:
                break    // poda alfa: MAX no elegira esta rama
        retornar valor

// Llamada inicial: alfa_beta(raiz, profundidad_max, -infinito, +infinito, verdadero)
```

**Traza de la poda sobre nuestro ejemplo:**

Retomemos el arbol anterior, pero ahora con poda alfa-beta:

```
                    MAX (raiz)     alfa=-inf, beta=+inf
                 /      |      \
              MIN      MIN      MIN
             /   \    /   \    /   \
            3     5  2     9  0     7
```

1. Exploramos la rama izquierda de MAX:
   - MIN izquierdo evalua hijo 3: beta = min(+inf, 3) = 3
   - MIN izquierdo evalua hijo 5: beta = min(3, 5) = 3
   - MIN izquierdo retorna 3.
   - MAX actualiza alfa = max(-inf, 3) = 3.

2. Exploramos la rama central de MAX:
   - MIN central evalua hijo 2: beta = min(+inf, 2) = 2.
   - Ahora alfa (3) >= beta (2). PODA! No necesitamos evaluar el hijo 9.
   - Razon: MAX ya tiene garantizado un 3 (de la rama izquierda). MIN central va a devolver a lo sumo 2 (ya encontro un 2). MAX nunca elegiria esta rama porque 2 < 3.

3. Exploramos la rama derecha de MAX:
   - MIN derecho evalua hijo 0: beta = min(+inf, 0) = 0.
   - alfa (3) >= beta (0). PODA! No evaluamos el hijo 7.
   - Razon: MAX no elegiria esta rama porque MIN ya puede forzar un 0, peor que el 3 que MAX ya tiene.

Resultado: el valor minimax sigue siendo 3, pero evaluamos 4 nodos terminales en vez de 6. En este ejemplo pequeno ahorramos 2 evaluaciones, pero en un arbol de ajedrez con millones de nodos la diferencia es dramatica.

**Resultado fundamental (Knuth y Moore, 1975):** Con ordenamiento perfecto de movimientos, la poda alfa-beta reduce la complejidad de O(b^d) a O(b^(d/2)), duplicando efectivamente la profundidad de busqueda alcanzable con los mismos recursos. Esto equivale a reducir el factor de ramificacion efectivo de b a la raiz cuadrada de b.

En el ajedrez, esto significa pasar de b = 35 a un factor efectivo de aproximadamente 6, lo que hace viable la busqueda a profundidades competitivas. La clave practica esta en el ordenamiento de movimientos: si evaluamos primero los movimientos mas prometedores (capturas, jaques), las podas ocurren mas temprano y se eliminan mas ramas.

### 6.4. Aplicaciones: de Deep Blue a AlphaGo

**Deep Blue** (Campbell et al., 2002) derroto al campeon mundial Garry Kasparov en 1997 utilizando minimax con poda alfa-beta, hardware especializado capaz de evaluar 200 millones de posiciones por segundo, y una funcion de evaluacion afinada por grandes maestros. Deep Blue podia buscar a profundidades de 12 a 40 movimientos (dependiendo de la posicion), lo que le daba una vision tactica superior a cualquier humano.

**AlphaGo** (Silver et al., 2016) represento un cambio de paradigma al combinar redes neuronales profundas con busqueda de arbol Monte Carlo (MCTS) para dominar el juego de Go, cuyo factor de ramificacion (b aproximadamente 250) y profundidad hacen inviable el enfoque clasico de minimax. La red de politica guia la seleccion de movimientos a explorar, mientras que la red de valor evalua posiciones sin necesidad de jugar hasta el final.

La diferencia de enfoque es reveladora: Deep Blue usaba fuerza bruta guiada por heuristicas humanas (minimax + alfa-beta + evaluacion experta), mientras que AlphaGo aprendio sus propias heuristicas a traves de redes neuronales. En Go, donde la intuicion posicional es mas relevante que el calculo tactico, el enfoque neuronal resulto superior.

**AlphaGo Zero** (Silver et al., 2017) elimino por completo el conocimiento humano previo: aprendio exclusivamente mediante autopartidas (self-play) con aprendizaje por refuerzo, superando a todas las versiones anteriores. Este resultado demostro que la busqueda combinada con aprendizaje profundo puede trascender el conocimiento humano experto.

Los juegos de adversario son un caso particular de optimizacion: encontrar la mejor estrategia. La siguiente seccion aborda la optimizacion desde una perspectiva completamente distinta, inspirada no en la teoria de juegos sino en la biologia evolutiva.

---

## 7. Algoritmos Geneticos y Computacion Evolutiva

### 7.1. Fundamentos biologicos y formalizacion

Los algoritmos geneticos (AG), introducidos por Holland (1975), son metaheuristicas de optimizacion inspiradas en la seleccion natural darwiniana. Operan sobre una poblacion de soluciones candidatas (cromosomas o individuos) que evolucionan iterativamente mediante operadores que simulan procesos biologicos.

La analogia biologica funciona asi: cada "individuo" de la poblacion es una solucion candidata al problema, codificada como una cadena (el "cromosoma"). Los individuos mas aptos (que mejor resuelven el problema) tienen mayor probabilidad de reproducirse (pasar sus "genes" a la siguiente generacion). A lo largo de muchas generaciones, la poblacion converge hacia soluciones cada vez mejores, de la misma forma en que la seleccion natural produce organismos cada vez mas adaptados a su entorno.

Formalmente, un AG se define por:

- **Representacion:** codificacion de una solucion como un cromosoma (cadena binaria, vector de reales, permutacion).
- **Funcion de aptitud (fitness):** f: C -> R que cuantifica la calidad de cada cromosoma.
- **Poblacion:** conjunto de N cromosomas que evoluciona en cada generacion.
- **Operadores geneticos:** seleccion, cruzamiento y mutacion.
- **Criterio de paro:** numero maximo de generaciones, convergencia, o aptitud objetivo alcanzada.

**Pseudocodigo del ciclo principal:**

```
funcion algoritmo_genetico(tam_poblacion, prob_cruce, prob_mutacion, max_generaciones):
    poblacion = generar_poblacion_aleatoria(tam_poblacion)
    evaluar_fitness(poblacion)

    para generacion = 1 hasta max_generaciones:
        nueva_poblacion = []

        // Elitismo: conservar los mejores
        nueva_poblacion.agregar(mejores_k(poblacion, k=2))

        mientras tamano(nueva_poblacion) < tam_poblacion:
            padre1 = seleccion_torneo(poblacion)
            padre2 = seleccion_torneo(poblacion)

            si aleatorio() < prob_cruce:
                hijo1, hijo2 = cruzamiento(padre1, padre2)
            sino:
                hijo1, hijo2 = padre1, padre2

            hijo1 = mutacion(hijo1, prob_mutacion)
            hijo2 = mutacion(hijo2, prob_mutacion)

            nueva_poblacion.agregar(hijo1, hijo2)

        poblacion = nueva_poblacion
        evaluar_fitness(poblacion)

        si mejor_fitness(poblacion) >= objetivo:
            retornar mejor_individuo(poblacion)

    retornar mejor_individuo(poblacion)
```

### 7.2. Operadores geneticos

**Seleccion:** Mecanismo que favorece la reproduccion de individuos con mayor aptitud. Los metodos principales incluyen:

- Ruleta proporcional (roulette wheel): la probabilidad de seleccion de un individuo es proporcional a su fitness relativo. Si un individuo tiene fitness 30 y el total de la poblacion suma 100, su probabilidad de ser seleccionado es 30%.
- Torneo (tournament): se eligen k individuos al azar y se selecciona el de mayor fitness. Controla la presion selectiva ajustando k. Con k=2, la presion es moderada; con k grande, solo los mejores sobreviven.
- Elitismo: los mejores n individuos pasan directamente a la siguiente generacion sin modificacion. Garantiza que el mejor fitness nunca empeora entre generaciones.

**Cruzamiento (crossover):** Recombina material genetico de dos padres para producir descendencia. Tipos principales:

- Un punto: se elige un punto de corte y se intercambian los segmentos.
  ```
  Padre 1:  1 0 1 | 1 0 0      Hijo 1:  1 0 1 | 0 1 1
  Padre 2:  0 1 0 | 0 1 1      Hijo 2:  0 1 0 | 1 0 0
                ^corte                         ^corte
  ```
- Dos puntos: se eligen dos puntos y se intercambia el segmento intermedio.
- Uniforme: cada gen se hereda de uno u otro padre con probabilidad 0.5.

**Mutacion:** Introduce variaciones aleatorias en un cromosoma individual. En codificacion binaria, se invierte un bit con probabilidad pm (tipicamente 0.001 a 0.01).

```
Antes de mutacion:   1 0 1 1 0 0
                             ^
                     (bit seleccionado para mutar)
Despues de mutacion: 1 0 1 1 1 0
```

La mutacion previene la convergencia prematura al mantener diversidad genetica en la poblacion, permitiendo la exploracion de nuevas regiones del espacio de busqueda (Goldberg, 1989). Sin mutacion, la poblacion puede quedarse atrapada en un optimo local: todos los individuos se parecen y el cruzamiento ya no genera nada nuevo. La mutacion inyecta la variabilidad necesaria para "saltar" fuera de esos valles.

### 7.3. Ejemplo paso a paso: optimizando una funcion simple

Para aterrizar los conceptos, tracemos un AG que maximiza f(x) = x^2 en el rango [0, 31], usando cromosomas binarios de 5 bits.

**Generacion 0 (poblacion inicial aleatoria, 4 individuos):**

| Individuo | Cromosoma | Valor decimal (x) | Fitness f(x)=x^2 | Proporcion |
|-----------|-----------|-------------------|-------------------|------------|
| A         | 01101     | 13                | 169               | 14.4%      |
| B         | 11000     | 24                | 576               | 49.2%      |
| C         | 01000     | 8                 | 64                | 5.5%       |
| D         | 10011     | 19                | 361               | 30.9%      |
|           |           |                   | Total: 1170       | 100%       |

**Seleccion (ruleta proporcional):** B tiene 49.2% de probabilidad de ser seleccionado, C solo 5.5%. Supongamos que la ruleta elige los pares (B, D) y (B, A) como padres.

**Cruzamiento (un punto, posicion 3):**

```
Par 1: B = 110|00, D = 100|11 -> Hijos: 110|11 = 27, 100|00 = 16
Par 2: B = 110|00, A = 011|01 -> Hijos: 110|01 = 25, 011|00 = 12
```

**Mutacion (pm = 0.01 por bit):** Supongamos que un bit del tercer hijo muta:

```
Hijo 3 antes: 11001 (25) -> Hijo 3 despues: 11011 (27)
```

**Generacion 1:**

| Individuo | Cromosoma | x  | Fitness |
|-----------|-----------|-----|---------|
| E         | 11011     | 27  | 729     |
| F         | 10000     | 16  | 256     |
| G         | 11011     | 27  | 729     |
| H         | 01100     | 12  | 144     |

El mejor fitness paso de 576 (generacion 0, individuo B con x=24) a 729 (generacion 1, individuos E y G con x=27). La poblacion "evoluciono" hacia valores mas altos de x, que es donde f(x)=x^2 tiene sus maximos en el rango [0,31]. Despues de varias generaciones, el AG convergeria al optimo x=31 (11111) con f(31) = 961.

Este ejemplo es trivial a proposito (el optimo se puede encontrar por inspeccion), pero la misma mecanica aplica a problemas donde el espacio de busqueda tiene millones de dimensiones y no existe una formula cerrada para el optimo.

**Aplicaciones practicas de los AG:**

- **Diseno de antenas:** La NASA uso AG para disenar la antena de la mision ST5 en 2006. El cromosoma codificaba la geometria del alambre (angulos y longitudes de segmentos), y el fitness era la calidad de la senal. El resultado fue una antena con forma irregular que ningun ingeniero habria disenado intuitivamente, pero que superaba a los disenos convencionales.
- **Optimizacion de portafolios:** En finanzas, el cromosoma puede codificar las proporciones de inversion en distintos activos, y el fitness puede ser el ratio de Sharpe (rendimiento ajustado por riesgo). El AG explora combinaciones de activos que un analista no probaria manualmente.
- **Rutas de vehiculos:** El problema del agente viajero (TSP) se codifica como una permutacion de ciudades. El cruzamiento de permutaciones requiere operadores especiales (como el Order Crossover) para que los hijos sigan siendo permutaciones validas.

### 7.4. Teorema del esquema de Holland

Holland (1975) demostro que los AG procesan implicitamente un numero exponencial de esquemas (patrones parciales) de manera simultanea. Un esquema H es un patron con posiciones fijas y comodines (*). Por ejemplo, 1**0* es un esquema de orden 2 (dos posiciones fijas) y longitud de definicion 3 (distancia entre la primera y la ultima posicion fija).

El teorema establece que esquemas cortos, de bajo orden y con aptitud superior al promedio reciben un numero exponencialmente creciente de representantes en generaciones sucesivas.

En nuestro ejemplo anterior, el esquema 11*** (que incluye a los individuos B=11000 y E=11011) tiene alta aptitud promedio porque los numeros grandes en binario empiezan con 11. El teorema predice que este esquema tendra cada vez mas representantes en generaciones futuras, que es exactamente lo que observamos.

Este resultado, conocido como el "paralelismo implicito" de los AG, explica por que los AG pueden explorar eficientemente espacios de busqueda exponencialmente grandes: no evaluan cada solucion independientemente, sino que procesan simultaneamente bloques constructivos (building blocks) que se combinan para formar soluciones cada vez mejores. Con una poblacion de N individuos de longitud L, el AG procesa del orden de N^3 esquemas en cada generacion, pese a solo evaluar N individuos (Goldberg, 1989).

### 7.5. Teorema No Free Lunch

Wolpert y Macready (1997) demostraron el teorema No Free Lunch (NFL): promediado sobre todos los problemas posibles, ningun algoritmo de optimizacion supera a otro. Es decir, si el AG es superior a la busqueda aleatoria en un problema, necesariamente sera inferior en algun otro.

La implicacion practica del NFL es que la efectividad de un AG depende criticamente de que su representacion, operadores y parametros se ajusten a la estructura del problema especifico. No existe un algoritmo universal de optimizacion, lo que resalta la importancia del conocimiento del dominio en la aplicacion de cualquier metodo de busqueda.

Esto conecta con un tema recurrente del bloque completo: la eleccion del algoritmo no es una decision teorica sino practica. BFS es optimo en costos uniformes pero devora memoria. DFS es eficiente en memoria pero puede perderse. A* es optimo con buena heuristica pero tambien puede quedarse sin RAM. Los AG son flexibles para optimizacion pero requieren calibracion cuidadosa. El NFL formalmente confirma lo que la experiencia sugiere: no hay almuerzo gratis, y entender las fortalezas y debilidades de cada herramienta es lo que permite elegir la correcta para cada problema.

---

## 8. Conexion con la Ciencia de Datos

Los algoritmos de busqueda del Bloque B no son meras abstracciones teoricas; constituyen pilares operativos de la ciencia de datos contemporanea:

**Optimizacion de hiperparametros:** La busqueda en cuadricula (grid search) es una busqueda exhaustiva en el espacio de hiperparametros, equivalente a BFS sobre una rejilla multidimensional. Si un modelo tiene 3 hiperparametros y cada uno tiene 10 valores posibles, grid search evalua 10^3 = 1,000 combinaciones. La busqueda aleatoria (Bergstra y Bengio, 2012) resulta mas eficiente cuando no todos los hiperparametros son igualmente importantes, porque no desperdicia evaluaciones en dimensiones irrelevantes. Los metodos bayesianos (como Optuna o HyperOpt) aplican algo similar a una busqueda informada: usan los resultados de evaluaciones anteriores para construir un modelo probabilistico de donde es mas probable encontrar buenos hiperparametros. Los algoritmos geneticos se utilizan en AutoML para evolucionar arquitecturas de redes neuronales (neuroevolucion), donde cada cromosoma codifica el numero de capas, neuronas por capa, funciones de activacion y tasas de aprendizaje.

**Planificadores de consultas SQL:** Los optimizadores de bases de datos relacionales (PostgreSQL, Oracle) implementan variantes de busqueda informada para encontrar el plan de ejecucion de menor costo entre las multiples estrategias posibles de JOIN, escaneo e indexacion. Cuando escribimos un query con 5 tablas unidas por JOINs, hay 5! = 120 ordenes posibles de unirlas, y cada una puede ejecutarse con distintas estrategias (nested loop, hash join, merge join). El optimizador debe explorar este espacio y encontrar el plan mas rapido, un problema que tiene exactamente la misma estructura que la busqueda en grafos con funcion de costo. PostgreSQL usa programacion dinamica (similar a A* con memoria de sub-soluciones) para queries de hasta 12 tablas, y AG para queries con mas tablas donde la programacion dinamica ya no escala (PostgreSQL, parametro geqo_threshold).

**Sistemas de recomendacion:** Los grafos de conocimiento se recorren mediante busquedas informadas para descubrir relaciones entre usuarios, productos y preferencias. Netflix, por ejemplo, modela las interacciones usuario-pelicula como un grafo bipartito, y la recomendacion equivale a encontrar caminos cortos en ese grafo entre un usuario y peliculas que aún no ha visto pero que son "cercanas" a las que le gustaron.

**Aprendizaje por refuerzo:** Los metodos de busqueda de arbol Monte Carlo (MCTS), que combinan minimax con muestreo estocastico, son fundamentales en AlphaGo y en la planificacion de agentes autonomos. En robotica, un robot que planifica como apilar cajas usa A* para encontrar secuencias de movimientos, y MCTS cuando hay incertidumbre (la caja puede resbalar).

**Seleccion de caracteristicas:** Los AG se aplican como metodo wrapper para seleccionar subconjuntos optimos de features, donde cada cromosoma codifica una mascara binaria de inclusion/exclusion de variables. Con 50 variables, hay 2^50 (mas de un cuadrillos) subconjuntos posibles. Un AG con 100 individuos y 200 generaciones evalua apenas 20,000 combinaciones y tipicamente encuentra soluciones cercanas al optimo. Es un caso donde la busqueda exhaustiva es imposible y la busqueda evolutiva brilla.

---

## 9. Dimension Etica y Responsabilidad

En consonancia con el perfil de egreso de la Licenciatura en Ciencia de Datos para Negocios de la UNRC, la aplicacion de algoritmos de busqueda y optimizacion en contextos reales conlleva responsabilidades eticas significativas:

**Transparencia algoritmica:** Los sistemas de toma de decisiones automatizadas deben ser auditables. Un algoritmo A* que planifica rutas de reparto debe poder explicar por que eligio una ruta sobre otra, especialmente si las decisiones afectan condiciones laborales. En el contexto de ciencia de datos, cuando un optimizador de hiperparametros selecciona un modelo, deberia quedar registro de por que se descartaron alternativas.

**Sesgos en funciones de evaluacion:** Las funciones heuristicas y de fitness codifican valores implicitos. Una funcion de evaluacion para contratacion automatizada puede perpetuar discriminaciones historicas si se entrena con datos sesgados. El problema es que el sesgo puede estar escondido en la heuristica: si h(candidato) incluye implicitamente la universidad de origen como proxy de calidad, y ciertas universidades estan correlacionadas con nivel socioeconomico, el algoritmo "optimiza" la discriminacion sin que nadie lo haya disenado para eso.

**Uso dual de la IA en juegos y conflictos:** Los mismos algoritmos minimax que permiten jugar ajedrez se aplican en estrategia militar y ciberseguridad. La comunidad cientifica tiene la responsabilidad de considerar las implicaciones de los avances en busqueda adversarial. Los drones autonomos que usan planificacion A* y minimax para tomar decisiones en campo de batalla plantean preguntas fundamentales sobre la delegacion de decisiones letales a algoritmos.

**Consumo energetico:** El entrenamiento de sistemas como AlphaGo Zero requirio miles de TPUs durante dias. La eficiencia computacional de los algoritmos de busqueda tiene implicaciones ambientales directas. Elegir un IDA* en vez de A* cuando la memoria es escasa no solo es una decision tecnica sino tambien de sustentabilidad: un algoritmo que usa menos RAM tambien tiende a usar menos energia.

---

## 10. Conclusiones

El recorrido del Bloque B revela que la busqueda no es un tema aislado sino el hilo conductor que conecta los fundamentos de la inteligencia artificial con sus aplicaciones mas avanzadas. Desde la busqueda ciega en grafos hasta la poda alfa-beta en juegos de adversario, pasando por la optimizacion evolutiva, el tema central es siempre el mismo: como explorar eficientemente un espacio de posibilidades que crece exponencialmente.

Los resultados fundamentales del bloque, como la optimalidad de A* (Hart et al., 1968), la eficiencia de IDA* (Korf, 1985), la poda alfa-beta (Knuth y Moore, 1975) y el paralelismo implicito de los AG (Holland, 1975), no son curiosidades academicas: son los cimientos sobre los que se construyen los optimizadores de bases de datos, los sistemas de planificacion, los motores de juego y los frameworks de AutoML que un cientifico de datos utiliza cotidianamente.

Un patron que se repite a lo largo de todo el bloque es el trade-off entre tiempo, espacio e informacion. BFS gasta memoria pero garantiza optimalidad. DFS ahorra memoria pero pierde optimalidad. IDS recupera ambas propiedades con un costo marginal de tiempo. A* incorpora informacion heuristica para reducir el espacio explorado, pero hereda el problema de memoria de BFS. IDA* combina las ideas de IDS con las de A*. Y la poda alfa-beta nos recuerda que a veces la mejor estrategia no es buscar mas, sino dejar de buscar donde no vale la pena.

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
