"""
Genera cuestionario separado en DOCX con las 20 preguntas del Bloque B.
"""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os, html, re

OUT = os.path.join(os.path.dirname(__file__), "docs", "Cuestionario_BloqueB_Ruffo_Espinosa.docx")

QUESTIONS = [
    {"q": "¿Cuales son los 4 elementos de la formulacion de un problema de busqueda?",
     "opts": ["Grafo, aristas, nodos, peso", "Estado inicial, estado meta, operadores, funcion de costo", "Entrada, salida, proceso, memoria", "Inicio, fin, condicion, ciclo"],
     "correct": 1,
     "explain": "La formulacion requiere: estado inicial, estado meta (o test de meta), operadores (acciones) y funcion de costo."},
    {"q": "¿Cuantos estados alcanzables tiene el 8-puzzle?",
     "opts": ["362,880", "181,440", "40,320", "3,628,800"],
     "correct": 1,
     "explain": "9! = 362,880 permutaciones totales, pero solo la mitad (181,440) son alcanzables desde cualquier configuracion dada (paridad de inversiones)."},
    {"q": "¿Que algoritmo combina la optimalidad de BFS con la memoria de DFS?",
     "opts": ["DLS (profundidad limitada)", "UCS (costo uniforme)", "IDS (profundizacion iterativa)", "A*"],
     "correct": 2,
     "explain": "IDS ejecuta DLS con limites crecientes (0,1,2...). Es completo y optimo como BFS, pero usa memoria O(bd) como DFS."},
    {"q": "¿Cual es la complejidad espacial de BFS?",
     "opts": ["O(bd)", "O(bm)", "O(b^d)", "O(d)"],
     "correct": 2,
     "explain": "BFS almacena toda la frontera en memoria, que en el peor caso es O(b^d) donde b es el factor de ramificacion y d la profundidad de la solucion."},
    {"q": "¿La busqueda hacia atras es mejor cuando...?",
     "opts": ["La meta no esta definida", "Hay muchas metas posibles", "La meta esta bien definida y el inicio es amplio", "El espacio de estados es pequeno"],
     "correct": 2,
     "explain": "Backward search funciona mejor cuando la meta es clara y el estado inicial generaria demasiadas ramas."},
    {"q": "¿Que reduce la busqueda bidireccional?",
     "opts": ["De O(b^d) a O(b^d * 2)", "De O(b^d) a O(b^(d/2))", "De O(b^d) a O(d)", "De O(b^d) a O(b*d)"],
     "correct": 1,
     "explain": "La bidireccional ejecuta dos busquedas de profundidad d/2 cada una, reduciendo de O(b^d) a O(2 * b^(d/2))."},
    {"q": "¿Que significa que una heuristica sea admisible?",
     "opts": ["Que siempre da el costo exacto", "Que nunca sobreestima el costo real", "Que es consistente", "Que es facil de calcular"],
     "correct": 1,
     "explain": "Admisible = h(n) <= h*(n) para todo nodo n. La heuristica nunca sobreestima el costo real al objetivo."},
    {"q": "¿Que funcion usa A* para elegir el siguiente nodo?",
     "opts": ["f(n) = h(n)", "f(n) = g(n)", "f(n) = g(n) + h(n)", "f(n) = max(g(n), h(n))"],
     "correct": 2,
     "explain": "A* combina el costo real acumulado g(n) con la estimacion heuristica h(n)."},
    {"q": "¿Que condicion tiene una heuristica consistente?",
     "opts": ["h(n) = h*(n)", "h(n) <= c(n,n') + h(n')", "h(n) >= h*(n)", "h(n) = 0 para todo n"],
     "correct": 1,
     "explain": "Consistencia (monotonia): h(n) <= c(n,n') + h(n') para todo sucesor n' de n. Implica admisibilidad."},
    {"q": "¿En un grafo AND-OR, un nodo AND significa...?",
     "opts": ["Elegir la mejor alternativa", "Resolver todos los subproblemas hijos", "Que no hay solucion", "Que el problema es trivial"],
     "correct": 1,
     "explain": "Un nodo AND indica descomposicion: el problema se resuelve solo si se resuelven TODOS sus subproblemas."},
    {"q": "¿En Minimax, que hace el jugador MIN?",
     "opts": ["Maximiza la utilidad", "Minimiza la utilidad", "Elige al azar", "No participa en la decision"],
     "correct": 1,
     "explain": "MIN busca minimizar el valor de utilidad (peor caso para MAX). Minimax asume que el oponente juega de forma optima."},
    {"q": "¿Cuando se poda en alfa-beta?",
     "opts": ["Cuando alfa = 0", "Cuando beta = 0", "Cuando alfa >= beta", "Cuando alfa + beta = 0"],
     "correct": 2,
     "explain": "Se poda cuando alfa >= beta. MAX ya tiene algo mejor (alfa) que lo que MIN le permitiria (beta)."},
    {"q": "¿Cual es la complejidad de alfa-beta en el mejor caso?",
     "opts": ["O(b^d)", "O(b^(d/2))", "O(bd)", "O(d*log(b))"],
     "correct": 1,
     "explain": "Con orden perfecto de nodos, alfa-beta reduce de O(b^d) a O(b^(d/2)), duplicando la profundidad explorable."},
    {"q": "¿Que tecnica uso AlphaGo para vencer a Lee Sedol?",
     "opts": ["Minimax puro", "Solo alfa-beta", "MCTS + redes neuronales", "Algoritmos geneticos"],
     "correct": 2,
     "explain": "AlphaGo (2016) combino Monte Carlo Tree Search con redes neuronales profundas entrenadas con partidas humanas y self-play."},
    {"q": "¿Que es un cromosoma en un algoritmo genetico?",
     "opts": ["Una funcion de aptitud", "Un operador genetico", "Una solucion candidata codificada", "La poblacion completa"],
     "correct": 2,
     "explain": "Un cromosoma es la representacion codificada de una solucion candidata."},
    {"q": "¿Que operador genetico introduce diversidad para escapar de optimos locales?",
     "opts": ["Seleccion", "Cruce", "Mutacion", "Elitismo"],
     "correct": 2,
     "explain": "La mutacion introduce cambios aleatorios pequenos que permiten explorar nuevas regiones del espacio de busqueda."},
    {"q": "¿Que tipo de cruce es mejor para permutaciones como el TSP?",
     "opts": ["Un punto", "Dos puntos", "Uniforme", "Order Crossover (OX)"],
     "correct": 3,
     "explain": "OX preserva el orden relativo de los genes, esencial en permutaciones. Los cruces de punto simple pueden generar soluciones invalidas."},
    {"q": "¿Que pasa si la tasa de mutacion es muy alta (>30%)?",
     "opts": ["Converge mas rapido al optimo", "Se destruyen buenas soluciones y se vuelve busqueda aleatoria", "No tiene ningun efecto", "Se eliminan todos los individuos"],
     "correct": 1,
     "explain": "Con mutacion excesiva, las buenas soluciones se corrompen constantemente. El AG se convierte en busqueda aleatoria."},
    {"q": "¿Cual es la aptitud maxima en el problema de 8 reinas con la formulacion de pares no atacados?",
     "opts": ["8", "16", "28", "56"],
     "correct": 2,
     "explain": "28 = C(8,2) = numero de pares posibles de reinas. Si ningun par se ataca, la aptitud es 28 (maxima)."},
    {"q": "¿Cual algoritmo usarias para encontrar el camino optimo en un mapa con una buena heuristica de distancia?",
     "opts": ["DFS", "Algoritmo genetico", "A* con heuristica admisible", "Minimax"],
     "correct": 2,
     "explain": "A* con heuristica admisible garantiza encontrar el camino optimo y es mucho mas eficiente que BFS gracias a la heuristica."},
]

def build():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(2.54)
        section.right_margin = Cm(2.54)

    style = doc.styles['Normal']
    style.font.name = 'Calibri'
    style.font.size = Pt(12)
    style.paragraph_format.space_after = Pt(4)
    style.paragraph_format.line_spacing = 1.15

    # Title
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("UNIVERSIDAD NACIONAL ROSARIO CASTELLANOS")
    run.bold = True
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0x9F, 0x22, 0x41)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Inteligencia Artificial (LCDN4INT10) - 4o Semestre")
    run.font.size = Pt(11)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Prof. Martin Humberto Llamas Haro")
    run.font.size = Pt(11)

    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("CUESTIONARIO - BLOQUE B: BUSQUEDA SIN INFORMACION")
    run.bold = True
    run.font.size = Pt(16)

    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run("Nombre: ________________________________     Fecha: ______________")
    run.font.size = Pt(11)

    doc.add_paragraph()

    p = doc.add_paragraph()
    run = p.add_run("Instrucciones: ")
    run.bold = True
    run.font.size = Pt(11)
    run = p.add_run("Selecciona la respuesta correcta para cada pregunta. Cada pregunta vale 0.5 puntos (total: 10 puntos).")
    run.font.size = Pt(11)

    doc.add_paragraph()

    # Questions
    letters = "ABCD"
    for qi, q in enumerate(QUESTIONS):
        # Question number and text
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        run = p.add_run(f"{qi+1}. {q['q']}")
        run.bold = True
        run.font.size = Pt(11)

        # Options
        for oi, opt in enumerate(q["opts"]):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(1)
            run = p.add_run(f"    {letters[oi]}) {opt}")
            run.font.size = Pt(11)

    doc.add_page_break()

    # Answer key
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("HOJA DE RESPUESTAS")
    run.bold = True
    run.font.size = Pt(14)

    doc.add_paragraph()

    tbl = doc.add_table(rows=21, cols=3)
    tbl.style = 'Table Grid'

    # Header
    tbl.cell(0, 0).text = "Pregunta"
    tbl.cell(0, 1).text = "Respuesta"
    tbl.cell(0, 2).text = "Explicacion"
    for ci in range(3):
        for par in tbl.cell(0, ci).paragraphs:
            for run in par.runs:
                run.bold = True
                run.font.size = Pt(10)

    for qi, q in enumerate(QUESTIONS):
        tbl.cell(qi+1, 0).text = str(qi+1)
        tbl.cell(qi+1, 1).text = f"{letters[q['correct']]}) {q['opts'][q['correct']]}"
        tbl.cell(qi+1, 2).text = q["explain"]
        for ci in range(3):
            for par in tbl.cell(qi+1, ci).paragraphs:
                for run in par.runs:
                    run.font.size = Pt(9)

    core = doc.core_properties
    core.author = "Daniel Ruffo Godinez"
    core.title = "Cuestionario Bloque B - IA"

    doc.save(OUT)
    print(f"Cuestionario generado: {OUT}")

if __name__ == "__main__":
    build()
