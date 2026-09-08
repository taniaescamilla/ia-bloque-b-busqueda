"""
eval_quiz.py - Evaluador de respuestas del quiz interactivo
============================================================
Valida que las respuestas del quiz en el HTML sean correctas
comparandolas contra un ground truth derivado de fuentes academicas.

Uso:
    python eval_quiz.py presentacion/ia_bloque_b.html

Por que existe este script:
    En un sistema con IA generativa, las respuestas pueden "deslizarse"
    durante ediciones. Este eval detecta si alguna respuesta cambio
    o si el numero de preguntas no coincide con lo esperado.
    Es un guardrail contra alucinacion en contenido educativo.
"""

import re
import sys
import json

EXPECTED_QUESTIONS = 20

GROUND_TRUTH = {
    0: {"correct": 1, "topic": "Formulacion de problemas de busqueda"},
    1: {"correct": 1, "topic": "Estados alcanzables 8-puzzle"},
    2: {"correct": 2, "topic": "IDS combina BFS optimalidad + DFS memoria"},
    3: {"correct": 2, "topic": "Complejidad espacial BFS"},
    4: {"correct": 2, "topic": "Busqueda hacia atras"},
    5: {"correct": 1, "topic": "Busqueda bidireccional"},
    6: {"correct": 1, "topic": "Heuristica admisible"},
    7: {"correct": 2, "topic": "Funcion de A*"},
    8: {"correct": 1, "topic": "Heuristica consistente"},
    9: {"correct": 1, "topic": "Nodo AND"},
    10: {"correct": 1, "topic": "MIN en minimax"},
    11: {"correct": 2, "topic": "Poda alfa-beta"},
    12: {"correct": 1, "topic": "Complejidad mejor caso alfa-beta"},
    13: {"correct": 2, "topic": "AlphaGo"},
    14: {"correct": 2, "topic": "Cromosoma en AG"},
    15: {"correct": 2, "topic": "Operador de diversidad"},
    16: {"correct": 3, "topic": "Cruce para permutaciones"},
    17: {"correct": 1, "topic": "Tasa de mutacion alta"},
    18: {"correct": 2, "topic": "Fitness maximo 8-reinas"},
    19: {"correct": 2, "topic": "Algoritmo optimo con heuristica"},
}


def extract_quiz_answers(html_path):
    """Extrae los indices 'correct' del array quizData en el HTML."""
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"correct:\s*(\d+)"
    matches = re.findall(pattern, content)
    return [int(m) for m in matches]


def run_eval(html_path):
    answers = extract_quiz_answers(html_path)

    print(f"{'='*60}")
    print(f"EVAL: Quiz Bloque B")
    print(f"{'='*60}")
    print(f"Preguntas encontradas: {len(answers)}")
    print(f"Preguntas esperadas:   {EXPECTED_QUESTIONS}")
    print()

    if len(answers) != EXPECTED_QUESTIONS:
        print(f"FAIL: Se esperaban {EXPECTED_QUESTIONS} preguntas, se encontraron {len(answers)}")
        return False

    all_pass = True
    for i, answer in enumerate(answers):
        gt = GROUND_TRUTH.get(i)
        if gt is None:
            print(f"  Q{i+1:02d}: WARN - Sin ground truth")
            continue

        status = "PASS" if answer == gt["correct"] else "FAIL"
        if status == "FAIL":
            all_pass = False
            print(f"  Q{i+1:02d}: {status} - Esperado {gt['correct']}, encontrado {answer} ({gt['topic']})")
        else:
            print(f"  Q{i+1:02d}: {status} - {gt['topic']}")

    print()
    print(f"{'='*60}")
    if all_pass:
        print("RESULTADO: ALL PASS - Todas las respuestas verificadas")
    else:
        print("RESULTADO: FAIL - Hay respuestas incorrectas")
    print(f"{'='*60}")

    return all_pass


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "presentacion/ia_bloque_b.html"
    success = run_eval(path)
    sys.exit(0 if success else 1)
