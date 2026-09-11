"""
Genera el documento academico extenso en DOCX desde el markdown.
Full-page width, parrafos largos, formato profesional.
"""
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
import re, os

SRC = os.path.join(os.path.dirname(__file__), "docs", "documento_academico_bloque_b.md")
OUT = os.path.join(os.path.dirname(__file__), "docs", "Documento_Academico_BloqueB_Ruffo_Espinosa.docx")

def build():
    doc = Document()

    # Page setup: normal margins, full width
    for section in doc.sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(2.54)
        section.right_margin = Cm(2.54)
        section.page_width = Cm(21.59)
        section.page_height = Cm(27.94)

    style = doc.styles['Normal']
    style.font.name = 'Calibri'
    style.font.size = Pt(12)
    style.paragraph_format.space_after = Pt(6)
    style.paragraph_format.line_spacing = 1.15
    style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    for level in range(1, 4):
        hs = doc.styles[f'Heading {level}']
        hs.font.name = 'Calibri'
        hs.font.color.rgb = RGBColor(0x23, 0x2F, 0x3F)
        if level == 1:
            hs.font.size = Pt(16)
        elif level == 2:
            hs.font.size = Pt(14)
        else:
            hs.font.size = Pt(12)

    # Read markdown
    with open(SRC, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # --- COVER PAGE ---
    for _ in range(3):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("UNIVERSIDAD NACIONAL ROSARIO CASTELLANOS")
    run.bold = True
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(0x9F, 0x22, 0x41)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("LICENCIATURA EN CIENCIA DE DATOS PARA NEGOCIOS")
    run.bold = True
    run.font.size = Pt(13)
    run.font.color.rgb = RGBColor(0x23, 0x5B, 0x4E)

    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("DOCUMENTO ACADEMICO EN EXTENSO")
    run.bold = True
    run.font.size = Pt(18)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("BLOQUE B: BUSQUEDA SIN INFORMACION")
    run.bold = True
    run.font.size = Pt(15)
    run.font.color.rgb = RGBColor(0x28, 0xB4, 0xE7)

    for _ in range(2):
        doc.add_paragraph()

    # Info table on cover
    info = [
        ("Asignatura", "Inteligencia Artificial (LCDN4INT10)"),
        ("Unidad Tematica", "Bloque B: Busqueda sin Informacion"),
        ("Programa Academico", "Licenciatura en Ciencia de Datos para Negocios"),
        ("Institucion", "Universidad Nacional Rosario Castellanos"),
        ("Ciclo Lectivo", "Cuarto Semestre"),
        ("Docente", "Martin Humberto Llamas Haro"),
    ]
    tbl = doc.add_table(rows=len(info), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, (k, v) in enumerate(info):
        c0 = tbl.cell(i, 0)
        c0.text = k
        for par in c0.paragraphs:
            for run in par.runs:
                run.bold = True
                run.font.size = Pt(11)
        c1 = tbl.cell(i, 1)
        c1.text = v
        for par in c1.paragraphs:
            for run in par.runs:
                run.font.size = Pt(11)

    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Equipo")
    run.bold = True
    run.font.size = Pt(12)

    team_tbl = doc.add_table(rows=2, cols=2)
    team_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    team_tbl.cell(0, 0).text = "Daniel Ruffo"
    team_tbl.cell(0, 1).text = "Investigacion, desarrollo, arquitectura del repositorio"
    team_tbl.cell(1, 0).text = "Giovana Espinosa"
    team_tbl.cell(1, 1).text = "Investigacion, revision, validacion academica"
    for row in team_tbl.rows:
        for cell in row.cells:
            for par in cell.paragraphs:
                for run in par.runs:
                    run.font.size = Pt(11)

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Ciudad de Mexico, Mexico, 2026")
    run.font.size = Pt(11)

    doc.add_page_break()

    # --- BODY: parse markdown ---
    # Skip the cover section in the MD (lines until first "## 1.")
    body_start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("## Indice"):
            body_start = i
            break

    # Table of Contents heading
    doc.add_heading("Indice", level=1)

    in_toc = True
    in_table = False
    table_rows = []
    in_references = False
    i = body_start + 1

    while i < len(lines):
        line = lines[i].rstrip()

        # Detect end of TOC
        if in_toc:
            if line.startswith("---"):
                in_toc = False
                doc.add_page_break()
                i += 1
                continue
            if line.strip():
                # TOC entry
                text = line.strip().lstrip("0123456789. ")
                p = doc.add_paragraph(line.strip())
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            i += 1
            continue

        # Skip horizontal rules
        if line.startswith("---"):
            i += 1
            continue

        # Headings
        if line.startswith("### "):
            heading_text = line[4:].strip()
            doc.add_heading(heading_text, level=3)
            i += 1
            continue

        if line.startswith("## "):
            heading_text = line[3:].strip()
            if heading_text == "Referencias":
                in_references = True
            doc.add_heading(heading_text, level=2)
            if heading_text.startswith("1.") or heading_text.startswith("2.") or heading_text.startswith("3.") or heading_text.startswith("4.") or heading_text.startswith("5.") or heading_text.startswith("6.") or heading_text.startswith("7.") or heading_text.startswith("8.") or heading_text.startswith("9.") or heading_text.startswith("10."):
                pass
            i += 1
            continue

        if line.startswith("# "):
            heading_text = line[2:].strip()
            doc.add_heading(heading_text, level=1)
            i += 1
            continue

        # Tables
        if "|" in line and not line.strip().startswith("-"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if cells:
                if not in_table:
                    in_table = True
                    table_rows = [cells]
                else:
                    # skip separator row
                    if all(set(c.strip()) <= set("-: ") for c in cells):
                        i += 1
                        continue
                    table_rows.append(cells)
                i += 1
                continue
        elif in_table:
            # End of table, render it
            if table_rows:
                ncols = max(len(r) for r in table_rows)
                tbl = doc.add_table(rows=len(table_rows), cols=ncols)
                tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                # Style: light grid
                tbl.style = 'Table Grid'
                for ri, row_data in enumerate(table_rows):
                    for ci, val in enumerate(row_data):
                        cell = tbl.cell(ri, ci)
                        cell.text = val.replace("**", "")
                        for par in cell.paragraphs:
                            par.alignment = WD_ALIGN_PARAGRAPH.LEFT
                            for run in par.runs:
                                run.font.size = Pt(10)
                                if ri == 0:
                                    run.bold = True
            in_table = False
            table_rows = []
            # Don't skip this line, process it below

        # Bullet points
        if line.startswith("- **") or line.startswith("- "):
            text = line[2:].strip()
            text = format_inline(text)
            p = doc.add_paragraph(style='List Bullet')
            add_formatted_runs(p, text)
            i += 1
            continue

        # Numbered list
        m = re.match(r"^(\d+)\.\s+", line)
        if m and not line.startswith("## "):
            text = line[m.end():].strip()
            text = format_inline(text)
            p = doc.add_paragraph(style='List Number')
            add_formatted_runs(p, text)
            i += 1
            continue

        # Empty line
        if not line.strip():
            i += 1
            continue

        # Regular paragraph - collect continuation lines for full paragraphs
        para_lines = [line]
        i += 1
        while i < len(lines):
            next_line = lines[i].rstrip()
            if (not next_line.strip() or next_line.startswith("#") or
                next_line.startswith("---") or next_line.startswith("- ") or
                next_line.startswith("|") or re.match(r"^\d+\.\s+", next_line)):
                break
            para_lines.append(next_line)
            i += 1

        full_text = " ".join(l.strip() for l in para_lines)
        full_text = format_inline(full_text)
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_formatted_runs(p, full_text)

    # Flush any remaining table
    if in_table and table_rows:
        ncols = max(len(r) for r in table_rows)
        tbl = doc.add_table(rows=len(table_rows), cols=ncols)
        tbl.style = 'Table Grid'
        for ri, row_data in enumerate(table_rows):
            for ci, val in enumerate(row_data):
                cell = tbl.cell(ri, ci)
                cell.text = val.replace("**", "")

    # Clean metadata
    core = doc.core_properties
    core.author = "Daniel Ruffo Godinez"
    core.title = "Documento Academico en Extenso - Bloque B IA"
    core.subject = "Inteligencia Artificial - Busqueda sin Informacion"
    core.keywords = "IA, busqueda, A*, minimax, geneticos, UNRC, LCDN"

    doc.save(OUT)
    print(f"DOCX generado: {OUT}")
    print(f"Paginas estimadas: ~{len(lines)//45}")


def format_inline(text):
    """Clean markdown inline formatting markers for later processing."""
    # Remove double asterisks but mark for bold
    return text


def add_formatted_runs(paragraph, text):
    """Add runs with bold/italic formatting from markdown-style markers."""
    # Split on **...**  for bold
    parts = re.split(r'(\*\*.*?\*\*)', text)
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
            run.font.size = Pt(12)
            run.font.name = 'Calibri'
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            run = paragraph.add_run(part[1:-1])
            run.italic = True
            run.font.size = Pt(12)
            run.font.name = 'Calibri'
        else:
            # Handle italic within non-bold text
            sub_parts = re.split(r'(\*[^*]+\*)', part)
            for sp in sub_parts:
                if sp.startswith("*") and sp.endswith("*") and len(sp) > 2:
                    run = paragraph.add_run(sp[1:-1])
                    run.italic = True
                    run.font.size = Pt(12)
                    run.font.name = 'Calibri'
                else:
                    if sp:
                        run = paragraph.add_run(sp)
                        run.font.size = Pt(12)
                        run.font.name = 'Calibri'


if __name__ == "__main__":
    build()
