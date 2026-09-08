"""Verifica la estructura del HTML de la guia interactiva."""
import os, re

HTML = os.path.join(os.path.dirname(os.path.dirname(__file__)), "presentacion", "ia_bloque_b.html")

def _read():
    with open(HTML, "r", encoding="utf-8") as f:
        return f.read()

def test_html_exists():
    assert os.path.exists(HTML)

def test_has_doctype():
    with open(HTML, "r", encoding="utf-8") as f:
        assert "<!DOCTYPE html>" in f.readline()

def test_20_quiz_questions():
    assert len(re.findall(r"correct:\s*\d+", _read())) == 20

def test_dark_mode():
    assert "prefers-color-scheme: dark" in _read()

def test_accessibility():
    c = _read()
    assert 'tabindex="0"' in c
    assert 'role="button"' in c
