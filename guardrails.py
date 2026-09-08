"""
guardrails.py - Guardrails de calidad para contenido educativo
===============================================================
Valida que el HTML cumple con los estandares de calidad antes
de hacer commit. Detecta problemas comunes de contenido generado
por IA que podrian afectar la calidad academica.

Uso:
    python guardrails.py presentacion/ia_bloque_b.html

Guardrails implementados:
    1. ACCENTS    - Verifica acentos en espanol (comun que la IA los omita)
    2. SOURCES    - Verifica que se citan fuentes academicas
    3. A11Y       - Verifica accesibilidad (tabindex, role, onkeydown)
    4. DARK_MODE  - Verifica que hay CSS para dark mode
    5. NO_LATEX   - Verifica que no hay LaTeX crudo ($...$)
    6. QUIZ_COUNT - Verifica 20 preguntas y 10 Q&A
    7. NO_LOREM   - Detecta texto placeholder
"""

import re
import sys


class Guardrail:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def check(self, content):
        raise NotImplementedError


class AccentGuardrail(Guardrail):
    """Detecta palabras que probablemente necesitan acento."""
    SHOULD_HAVE_ACCENT = [
        (r'\balgoritmo\b', None),  # OK sin acento
        (r'\bbusqueda\b', 'busqueda -> b&uacute;squeda'),
        (r'\boptimo\b', 'optimo -> &oacute;ptimo'),
        (r'\bheuristica\b', 'heuristica -> heur&iacute;stica'),
        (r'\barbol\b', 'arbol -> &aacute;rbol'),
    ]

    def check(self, content):
        issues = []
        for pattern, fix in self.SHOULD_HAVE_ACCENT:
            if fix and re.search(pattern, content, re.IGNORECASE):
                count = len(re.findall(pattern, content, re.IGNORECASE))
                issues.append(f"  WARN: '{fix}' encontrado {count} veces")
        return issues


class SourceGuardrail(Guardrail):
    """Verifica que se citan fuentes clave."""
    REQUIRED_SOURCES = [
        'Russell', 'Norvig', 'Hart', 'Nilsson',
        'Knuth', 'Moore', 'Korf'
    ]

    def check(self, content):
        issues = []
        for source in self.REQUIRED_SOURCES:
            if source.lower() not in content.lower():
                issues.append(f"  WARN: Fuente '{source}' no encontrada en el HTML")
        return issues


class A11yGuardrail(Guardrail):
    """Verifica accesibilidad basica."""
    def check(self, content):
        issues = []
        if 'tabindex="0"' not in content:
            issues.append("  FAIL: No se encontro tabindex='0' para navegacion por teclado")
        if 'role="button"' not in content:
            issues.append("  FAIL: No se encontro role='button' en elementos interactivos")
        if 'onkeydown' not in content:
            issues.append("  FAIL: No se encontro onkeydown para accesibilidad de teclado")
        return issues


class DarkModeGuardrail(Guardrail):
    """Verifica soporte de dark mode."""
    def check(self, content):
        issues = []
        if 'prefers-color-scheme: dark' not in content:
            issues.append("  FAIL: No hay media query para prefers-color-scheme: dark")
        if 'data-theme="dark"' not in content and "data-theme='dark'" not in content:
            issues.append("  FAIL: No hay soporte para data-theme='dark'")
        if '--success: #5CB88A' not in content:
            issues.append("  WARN: --success no ajustado para dark mode (contraste)")
        return issues


class NoLatexGuardrail(Guardrail):
    """Detecta LaTeX crudo que no renderiza en HTML."""
    def check(self, content):
        issues = []
        latex_patterns = re.findall(r'\$[^$]+\$', content)
        real_latex = []
        for p in latex_patterns:
            if p.startswith('${') or p[1:2].isdigit():
                continue
            if chr(92) in p or '^' in p or '_' in p:
                real_latex.append(p)
        if real_latex:
            issues.append(f"  FAIL: {len(real_latex)} expresiones LaTeX crudas encontradas")
            for expr in real_latex[:3]:
                issues.append(f"    -> {expr[:60]}")
        return issues


class QuizCountGuardrail(Guardrail):
    """Verifica el numero correcto de preguntas y Q&A."""
    def check(self, content):
        issues = []
        quiz_q = len(re.findall(r'correct:\s*\d+', content))
        qa_match = re.search(r'const qaData\s*=\s*\[(.*?)\];', content, re.DOTALL)
        qa_items = len(re.findall(r"q:\s*['\"]", qa_match.group(1))) if qa_match else 0
        if quiz_q != 20:
            issues.append(f"  FAIL: Quiz tiene {quiz_q} preguntas, se esperan 20")
        if qa_items < 10:
            issues.append(f"  FAIL: Defensa tiene {qa_items} Q&A, se esperan al menos 10")
        return issues


class NoLoremGuardrail(Guardrail):
    """Detecta texto placeholder."""
    PLACEHOLDERS = ['lorem ipsum', 'FIXME']

    def check(self, content):
        issues = []
        for ph in self.PLACEHOLDERS:
            if ph.lower() in content.lower():
                issues.append(f"  FAIL: Texto placeholder encontrado: '{ph}'")
        return issues


def run_guardrails(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    guardrails = [
        AccentGuardrail('ACCENTS', 'Acentos en espanol'),
        SourceGuardrail('SOURCES', 'Fuentes academicas citadas'),
        A11yGuardrail('A11Y', 'Accesibilidad'),
        DarkModeGuardrail('DARK_MODE', 'Soporte dark mode'),
        NoLatexGuardrail('NO_LATEX', 'Sin LaTeX crudo'),
        QuizCountGuardrail('QUIZ_COUNT', 'Conteo de preguntas'),
        NoLoremGuardrail('NO_LOREM', 'Sin texto placeholder'),
    ]

    print(f"{'='*60}")
    print(f"GUARDRAILS: {html_path}")
    print(f"{'='*60}")

    total_fails = 0
    total_warns = 0

    for g in guardrails:
        issues = g.check(content)
        fails = [i for i in issues if 'FAIL' in i]
        warns = [i for i in issues if 'WARN' in i]
        total_fails += len(fails)
        total_warns += len(warns)

        status = 'PASS' if not fails else 'FAIL'
        if not fails and warns:
            status = 'WARN'

        print(f"\n[{status}] {g.name}: {g.description}")
        for issue in issues:
            print(issue)

    print(f"\n{'='*60}")
    print(f"RESULTADO: {total_fails} FAIL, {total_warns} WARN")
    if total_fails == 0:
        print("Todos los guardrails criticos pasaron.")
    else:
        print("Hay guardrails criticos que fallaron. Corregir antes de commit.")
    print(f"{'='*60}")

    return total_fails == 0


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'presentacion/ia_bloque_b.html'
    success = run_guardrails(path)
    sys.exit(0 if success else 1)
