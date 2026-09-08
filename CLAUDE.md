# CLAUDE.md — Bloque B: Busqueda sin Informacion

## Proposito de este archivo

Este archivo proporciona contexto al agente de IA (Claude Code) sobre el proyecto. En una clase de Inteligencia Artificial, esto no es solo una conveniencia tecnica sino una demostracion de como se configura un agente con contexto adecuado para que sus outputs sean utiles y verificables.

Un agente sin contexto alucina. Un agente con contexto acotado produce outputs verificables. Este archivo es el mecanismo de acotacion.

## Contexto del proyecto

- **Materia:** LCDN4INT10 Inteligencia Artificial, 4o semestre
- **Bloque:** B - Busqueda sin informacion
- **Universidad:** Universidad Nacional Rosario Castellanos (UNRC)
- **Profesor:** Martin Humberto Llamas Haro
- **Equipo:** Daniel Ruffo, Giovana Espinosa
- **Programa:** Licenciatura en Ciencia de Datos para Negocios (LCDN)

## Saberes evaluados (fuente: UCA oficial)

### Declarativos (saber que)
- Busqueda hacia adelante y hacia atras
- Reduccion de problemas: algoritmos A, A* y AO*
- Minimax y algoritmos geneticos

### Procedimentales (saber hacer)
- Modelar un problema como espacio de estados
- Definir y evaluar funciones heuristicas
- Analizar propiedades de algoritmos: completitud, optimalidad, complejidad temporal y espacial
- Optimizar busqueda con poda alfa-beta
- Definir Minimax, aplicar limites de tiempo, integrar ML
- Definir AG, implementar seleccion y operadores geneticos

## Estructura del repositorio

```
ia-bloque-b-busqueda/
├── presentacion/
│   └── ia_bloque_b.html    ← Guia interactiva (7 tabs, quiz, defensa)
├── docs/
│   ├── contenido_bloque_b.md       ← Resumen teorico
│   └── deep_research_bloque_b.md   ← Investigacion profunda (Kimi K3)
├── references/
│   └── references.bib              ← BibTeX con fuentes primarias
├── tests/                          ← Tests si aplica
├── .github/workflows/ci.yml        ← CI pipeline
├── ARCHITECTURE.md                 ← Decisiones de arquitectura (ADRs)
├── AI_USAGE.md                     ← Transparencia en uso de IA
├── CLAUDE.md                       ← Este archivo
├── README.md                       ← Entrada principal
└── requirements.txt                ← Dependencias Python
```

## Reglas para el agente

1. **Contenido verificable:** toda afirmacion debe tener fuente. Si no hay fuente, marcar como "pendiente de verificacion"
2. **Respuestas del quiz:** cada respuesta correcta debe ser verificable contra Russell & Norvig AIMA o el paper original
3. **Espanol:** todo el contenido en espanol, terminos tecnicos en ingles entre parentesis cuando sea estandar
4. **Sin LaTeX en HTML:** formulas en texto plano o HTML (no $...$ que no renderiza en el navegador)
5. **Accesibilidad:** tabindex, role, onkeydown en todos los elementos interactivos
6. **Dark mode:** CSS custom properties con prefers-color-scheme Y data-theme

## Fuentes primarias del bloque

| Tema | Fuente primaria |
|------|----------------|
| A* optimalidad | Hart, Nilsson & Raphael (1968) |
| Alfa-beta | Knuth & Moore (1975) |
| IDS | Korf (1985) |
| MCTS | Browne et al. survey; Kocsis & Szepesvar (2006) |
| AlphaGo | Silver et al., Nature (2016/2017) |
| AG schema theorem | Holland (1975) |
| No Free Lunch | Wolpert & Macready (1997) |
| Libro de texto | Russell & Norvig, AIMA 4th ed. |
