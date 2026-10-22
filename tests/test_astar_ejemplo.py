"""Verifica el ejemplo de A* del documento (seccion 5.3) contra un A* real.

Lee del documento las h, la tabla de pasos y el orden de costo uniforme,
y los compara con lo que de verdad hace el algoritmo sobre el mismo mapa.
"""
import heapq, os, re

DOC = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs", "documento_academico_bloque_b.md")

# Aristas del mapa del documento (no dirigidas)
ARISTAS = {("S", "A"): 3, ("A", "G"): 2, ("S", "B"): 1, ("A", "C"): 4, ("B", "C"): 5, ("C", "G"): 3}


def _vecinos():
    v = {}
    for (a, b), c in ARISTAS.items():
        v.setdefault(a, []).append((b, c))
        v.setdefault(b, []).append((a, c))
    return v


def _seccion():
    with open(DOC, "r", encoding="utf-8") as f:
        texto = f.read()
    ini = texto.index("**Ejemplo paso a paso: A* en un mapa de ciudades**")
    fin = texto.index("La complejidad temporal de A*", ini)
    return texto[ini:fin]


def _h_del_documento():
    # solo del bloque del mapa: el texto de abajo tambien menciona h(n) en ejemplos
    mapa = _seccion().split("```")[1]
    return {n: int(x) for n, x in re.findall(r"h\(([SABCG])\) = (\d+)", mapa)}


def _costo_real_a_meta():
    """h*(n): Dijkstra desde G (el grafo no es dirigido)."""
    dist, cola = {"G": 0}, [(0, "G")]
    while cola:
        d, n = heapq.heappop(cola)
        if d > dist[n]:
            continue
        for m, c in _vecinos()[n]:
            if d + c < dist.get(m, float("inf")):
                dist[m] = d + c
                heapq.heappush(cola, (d + c, m))
    return dist


def _buscar(h):
    """A* en grafo con lista cerrada y prueba de meta al extraer, igual que el pseudocodigo.
    Devuelve [(nodo, g)] en orden de expansion."""
    abierta, cerrada, orden = [(h["S"], 0, "S")], set(), []
    while abierta:
        f, g, n = heapq.heappop(abierta)
        if n in cerrada:
            continue
        orden.append((n, g))
        if n == "G":
            return orden
        cerrada.add(n)
        for m, c in _vecinos()[n]:
            if m not in cerrada:
                heapq.heappush(abierta, (g + c + h[m], g + c, m))
    return orden


def test_documento_trae_las_cinco_h():
    assert set(_h_del_documento()) == {"S", "A", "B", "C", "G"}


def test_h_es_admisible():
    h, real = _h_del_documento(), _costo_real_a_meta()
    sobreestima = {n: (h[n], real[n]) for n in h if h[n] > real[n]}
    assert not sobreestima, f"h > h* en {sobreestima}"


def test_h_es_consistente():
    # la busqueda en grafo con lista cerrada no reabre nodos: necesita consistencia
    h = _h_del_documento()
    for (a, b), c in ARISTAS.items():
        assert h[a] <= c + h[b], f"h({a}) > c({a},{b}) + h({b})"
        assert h[b] <= c + h[a], f"h({b}) > c({a},{b}) + h({a})"


def test_tabla_coincide_con_a_estrella():
    h = _h_del_documento()
    filas = re.findall(r"^\| \d+\s*\| ([SABCG])\s*\| (\d+)\s*\| (\d+)\s*\| (\d+)", _seccion(), re.M)
    esperado = [(n, g, h[n], g + h[n]) for n, g in _buscar(h)]
    assert [(n, int(g), int(hh), int(f)) for n, g, hh, f in filas] == esperado


def test_solucion_optima():
    orden = _buscar(_h_del_documento())
    assert orden[-1] == ("G", _costo_real_a_meta()["S"])


def test_orden_de_costo_uniforme():
    m = re.search(r"orden de expansion seria ([SABCG](?:, [SABCG])+)", _seccion())
    assert m, "el documento debe decir el orden de expansion de costo uniforme"
    ucs = [n for n, _ in _buscar({n: 0 for n in "SABCG"})]
    assert m.group(1).split(", ") == ucs
    assert len(_buscar(_h_del_documento())) < len(ucs)
