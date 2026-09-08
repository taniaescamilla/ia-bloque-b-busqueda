# Declaracion de uso de herramientas de IA

## Contexto

Este repositorio fue desarrollado como parte de la UCA LCDN4INT10 Inteligencia Artificial, Bloque B (Busqueda sin informacion). Como estudiantes de Ciencia de Datos, entendemos que la transparencia en el uso de herramientas de IA no es una concesion sino una competencia profesional.

## Herramientas utilizadas

| Herramienta | Proposito | Alcance |
|-------------|-----------|---------|
| Claude Code (Anthropic) | Asistente de desarrollo para estructura del repositorio, generacion de HTML interactivo, revision de codigo | Arquitectura, codigo, documentacion |
| Kimi K3 (Moonshot AI) | Investigacion profunda de fuentes academicas y demostraciones formales | Contenido de `docs/deep_research_bloque_b.md` |

## Que hizo la IA y que hicimos nosotros

### Lo que hizo la IA
- Genero la estructura HTML de la guia interactiva (CSS, JS, layout de tabs)
- Busco y organizo fuentes academicas para las profundizaciones
- Verifico las 20 respuestas del quiz contra el contenido
- Creo la estructura del repositorio (carpetas, CI, .md scaffolding)

### Lo que hicimos nosotros
- Definimos los temas y la estructura de tabs basandonos en los saberes de la UCA
- Revisamos y corregimos el contenido tecnico (definiciones, algoritmos, complejidades)
- Seleccionamos las preguntas del quiz y validamos las respuestas
- Redactamos las respuestas de defensa basandonos en lo que estudiamos
- Decidimos la arquitectura del repositorio (ADRs, que documentar, como organizar)
- Toda decision de contenido academico fue nuestra

## Filosofia de uso

Usamos IA como **herramienta de andamiaje** (scaffolding), no como autora. El proceso fue:

1. **Nosotros definimos que construir** (basado en la UCA y los saberes declarativos/procedimentales)
2. **La IA nos ayudo a construirlo** (codigo HTML, busqueda de fuentes, verificacion)
3. **Nosotros validamos y corregimos** (contenido, respuestas, precision tecnica)

Esto es analogo a como un ingeniero usa un compilador o un cientifico de datos usa pandas: la herramienta ejecuta, el humano decide que ejecutar y verifica que el resultado sea correcto.

## Verificabilidad

- Cada afirmacion tecnica en la guia tiene una fuente rastreable (ver `references/references.bib`)
- Las 20 respuestas del quiz son verificables contra Russell & Norvig AIMA 4th ed.
- Las demostraciones formales en las profundizaciones citan el paper original
- El repositorio completo es reproducible: clonar, abrir el HTML, verificar
