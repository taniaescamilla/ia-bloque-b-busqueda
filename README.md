<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Licencia-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Universidad-Rosario%20Castellanos-red" alt="Universidad">
  <img src="https://img.shields.io/badge/Bloque-B-28B4E7" alt="Bloque B">
</p>

<h1 align="center">Bloque B: Busqueda sin Informacion</h1>

<p align="center">
  LCDN4INT10 Inteligencia Artificial, 4o semestre<br>
  Universidad Nacional Rosario Castellanos
</p>

---

## Equipo

| Nombre | GitHub |
|--------|--------|
| Daniel Ruffo | @gespi6961-creator |
| Giovana Espinosa | @gespi6961-creator |

## Contenido del Bloque

### Saberes declarativos
- Busqueda hacia adelante y hacia atras
- Reduccion de problemas: algoritmos A, A* y AO*
- Minimax y algoritmos geneticos

### Saberes procedimentales
- Espacio de estados y funcion heuristica
- Propiedades de los algoritmos de busqueda
- Optimizacion de busqueda
- Minimax: definicion, limites de tiempo, ML en Minimax
- AG: definicion, seleccion, operadores

## Estructura del repositorio

| Carpeta | Contenido |
|---------|-----------|
| `presentacion/` | Guia interactiva HTML con quiz (20 preguntas) y defensa (10 Q&A) |
| `docs/` | Documentacion academica y material de estudio |
| `references/` | Bibliografia con fuentes academicas |
| `tests/` | Tests de correctitud algoritmica |
| `.github/workflows/` | CI pipeline |

## Guia interactiva

La guia de estudio interactiva incluye 7 tabs:

1. **Espacio de estados** - Formulacion de problemas, 8-puzzle, funciones de costo
2. **Adelante/Atras** - Busqueda forward/backward, bidireccional, BFS/DFS/IDS/UCS
3. **A, A*, AO*** - Heuristicas, admisibilidad, consistencia, grafos AND-OR
4. **Minimax** - Arboles de juego, alfa-beta, MCTS, AlphaGo
5. **Alg. geneticos** - Seleccion, cruce, mutacion, 8-reinas
6. **Defensa** - 10 preguntas frecuentes con respuestas detalladas
7. **Quiz** - 20 preguntas de auto-evaluacion

Para verla, abrir `presentacion/ia_bloque_b.html` en cualquier navegador.

## Instalacion

```bash
git clone https://github.com/TU-USUARIO/ia-bloque-b-busqueda.git
cd ia-bloque-b-busqueda
pip install -r requirements.txt
```

## Referencias principales

- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach*, 4th ed.
- Hart, P., Nilsson, N. & Raphael, B. (1968). A Formal Basis for the Heuristic Determination of Minimum Cost Paths.
- Knuth, D. & Moore, R. (1975). An Analysis of Alpha-Beta Pruning.
- Korf, R. (1985). Depth-First Iterative-Deepening.
- Silver, D. et al. (2016/2017). Mastering the game of Go. *Nature*.
- Holland, J. (1975). *Adaptation in Natural and Artificial Systems*.

## Licencia

MIT
