# Arquitectura del Proyecto
## Bloque B: Busqueda sin Informacion — LCDN4INT10

> Documento de arquitectura tecnica del repositorio para el Bloque B de Inteligencia Artificial.

---

## 1. Proposito y alcance

Material de estudio interactivo y documentacion academica para el Bloque B (Busqueda sin informacion) de la UCA Inteligencia Artificial. Incluye una guia HTML autocontenida con quiz, defensa oral preparada y documentacion de respaldo con trazabilidad bibliografica.

**Alcance:** material de estudio, evaluacion y defensa oral. **Fuera de alcance:** implementaciones de produccion.

## 2. Vista de componentes

| Componente | Responsabilidad | Tecnologia |
|---|---|---|
| `presentacion/ia_bloque_b.html` | Guia interactiva: 7 tabs, quiz 20 preguntas, defensa 10 Q&A | HTML, CSS, JS |
| `docs/contenido_bloque_b.md` | Contenido teorico del bloque | Markdown |
| `docs/deep_research_bloque_b.md` | Investigacion profunda complementaria | Markdown |
| `references/references.bib` | Bibliografia con fuentes primarias | BibTeX |
| `tests/` | Validacion de algoritmos si aplica | Python, pytest |
| `AI_USAGE.md` | Transparencia en uso de IA | Markdown |

## 3. Temas cubiertos

### Saberes declarativos
1. Busqueda hacia adelante y hacia atras
2. Reduccion de problemas: A, A*, AO*
3. Minimax y algoritmos geneticos

### Saberes procedimentales
1. Espacio de estados y funcion heuristica
2. Propiedades de los algoritmos (completitud, optimalidad, complejidad)
3. Optimizacion de busqueda
4. Minimax: definicion, limites de tiempo, ML
5. AG: definicion, seleccion, operadores

## 4. Decisiones de arquitectura

### ADR-001 — Guia HTML autocontenida
- **Contexto:** el material debe ser accesible sin instalacion.
- **Decision:** un archivo HTML unico con CSS y JS embebidos, sin dependencias externas (excepto Google Fonts).
- **Consecuencias:** portabilidad maxima; abrir en cualquier navegador.

### ADR-002 — Quiz con feedback inmediato
- **Contexto:** la auto-evaluacion requiere retroalimentacion rapida.
- **Decision:** quiz de 20 preguntas con respuestas verificadas y marcado visual (correcto/incorrecto).
- **Consecuencias:** el estudiante identifica gaps de conocimiento antes de la defensa.

### ADR-003 — Profundizaciones colapsables
- **Contexto:** el contenido avanzado (demostraciones formales, complejidad) no debe abrumar al lector casual.
- **Decision:** secciones `<details>` con contenido avanzado que el usuario puede expandir.
- **Consecuencias:** navegacion limpia con profundidad disponible bajo demanda.

## 5. Atributos de calidad

| Atributo | Mecanismo | Verificacion |
|---|---|---|
| Accesibilidad | tabindex, role, onkeydown en elementos interactivos | Navegacion por teclado |
| Portabilidad | HTML self-contained, 0 dependencias de build | Abrir en cualquier navegador |
| Tema dual | CSS custom properties + prefers-color-scheme | Light y dark mode |
| Correctitud | Quiz con respuestas verificadas contra fuentes | Revision manual |

## 6. Stack

HTML5, CSS3, JavaScript vanilla, Google Fonts (JetBrains Mono + Source Sans 3)
