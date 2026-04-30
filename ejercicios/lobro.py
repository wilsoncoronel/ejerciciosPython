#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Libro: HTML & CSS Moderno 2026 — Enfoque en Componentes
Autor: Generado con ReportLab
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether,
    Table, TableStyle, HRFlowable, ListFlowable, ListItem, Preformatted
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import os

# ─────────────────────────────────────────
# PALETA DE COLORES
# ─────────────────────────────────────────
C_BG         = HexColor('#0d0d12')
C_SURFACE    = HexColor('#16161e')
C_ACCENT     = HexColor('#7ee787')   # Verde acid
C_ACCENT2    = HexColor('#58a6ff')   # Azul
C_AMBER      = HexColor('#f0b030')
C_ROSE       = HexColor('#ff7b93')
C_VIOLET     = HexColor('#d2a8ff')
C_TEXT       = HexColor('#e6edf3')
C_MUTED      = HexColor('#8b949e')
C_DIM        = HexColor('#484f58')
C_BORDER     = HexColor('#21262d')
C_CODE_BG    = HexColor('#0d1117')
C_CODE_TEXT  = HexColor('#c9d1d9')
C_WHITE      = HexColor('#ffffff')
C_DARK_CARD  = HexColor('#161b22')
C_EXERCISE   = HexColor('#1c2128')
C_TIP_BG     = HexColor('#0d2b1a')
C_WARN_BG    = HexColor('#2b1f0d')
C_INFO_BG    = HexColor('#0d1f2b')
C_PAGE_BG    = HexColor('#0a0c10')

W, H = A4  # 595.27 x 841.89 points

# ─────────────────────────────────────────
# CANVAS CON HEADER/FOOTER
# ─────────────────────────────────────────
class BookCanvas:
    def __init__(self, chapter_title=""):
        self.chapter_title = chapter_title

    def __call__(self, canv, doc):
        canv.saveState()
        w, h = A4

        # Fondo de página
        canv.setFillColor(C_PAGE_BG)
        canv.rect(0, 0, w, h, fill=1, stroke=0)

        # Línea superior decorativa
        canv.setFillColor(C_ACCENT)
        canv.rect(0, h - 3, w, 3, fill=1, stroke=0)

        # Header
        if doc.page > 1:
            canv.setFillColor(C_SURFACE)
            canv.rect(0, h - 28, w, 25, fill=1, stroke=0)
            canv.setFont("Helvetica-Bold", 7)
            canv.setFillColor(C_ACCENT)
            canv.drawString(2*cm, h - 19, "HTML & CSS MODERNO 2026")
            canv.setFillColor(C_MUTED)
            canv.setFont("Helvetica", 7)
            canv.drawRightString(w - 2*cm, h - 19, self.chapter_title[:60])

        # Footer
        canv.setFillColor(C_SURFACE)
        canv.rect(0, 0, w, 22, fill=1, stroke=0)
        canv.setFillColor(C_ACCENT)
        canv.rect(0, 22, w, 1, fill=1, stroke=0)

        canv.setFont("Helvetica", 7)
        canv.setFillColor(C_MUTED)
        canv.drawString(2*cm, 7, "© 2026 — Libro de Componentes HTML & CSS")
        canv.setFont("Helvetica-Bold", 8)
        canv.setFillColor(C_ACCENT)
        canv.drawRightString(w - 2*cm, 7, f"Página {doc.page}")

        canv.restoreState()

# ─────────────────────────────────────────
# ESTILOS
# ─────────────────────────────────────────
def make_styles():
    s = {}

    base = ParagraphStyle(
        'base',
        fontName='Helvetica',
        fontSize=10,
        leading=16,
        textColor=C_TEXT,
        backColor=C_PAGE_BG,
    )

    s['body'] = ParagraphStyle('body', parent=base,
        fontSize=10, leading=17, textColor=HexColor('#c9d1d9'),
        spaceAfter=8, spaceBefore=2, firstLineIndent=0,
        leftIndent=0, alignment=TA_JUSTIFY)

    s['body_small'] = ParagraphStyle('body_small', parent=s['body'],
        fontSize=9, leading=14, textColor=C_MUTED)

    s['h1'] = ParagraphStyle('h1', parent=base,
        fontName='Helvetica-Bold', fontSize=36, leading=42,
        textColor=C_ACCENT, spaceAfter=6, spaceBefore=0,
        alignment=TA_CENTER)

    s['h1_sub'] = ParagraphStyle('h1_sub', parent=base,
        fontName='Helvetica', fontSize=15, leading=22,
        textColor=C_MUTED, spaceAfter=4, spaceBefore=0,
        alignment=TA_CENTER)

    s['h2'] = ParagraphStyle('h2', parent=base,
        fontName='Helvetica-Bold', fontSize=24, leading=30,
        textColor=C_WHITE, spaceAfter=6, spaceBefore=24,
        borderPad=0)

    s['h2_accent'] = ParagraphStyle('h2_accent', parent=s['h2'],
        textColor=C_ACCENT)

    s['h3'] = ParagraphStyle('h3', parent=base,
        fontName='Helvetica-Bold', fontSize=15, leading=20,
        textColor=C_ACCENT2, spaceAfter=5, spaceBefore=16)

    s['h4'] = ParagraphStyle('h4', parent=base,
        fontName='Helvetica-Bold', fontSize=11, leading=16,
        textColor=C_AMBER, spaceAfter=4, spaceBefore=10)

    s['h5'] = ParagraphStyle('h5', parent=base,
        fontName='Helvetica-Bold', fontSize=10, leading=14,
        textColor=C_VIOLET, spaceAfter=3, spaceBefore=8)

    s['chapter_tag'] = ParagraphStyle('chapter_tag', parent=base,
        fontName='Helvetica-Bold', fontSize=8, leading=12,
        textColor=C_ACCENT, spaceAfter=4, spaceBefore=0,
        alignment=TA_LEFT, letterSpacing=2)

    s['lead'] = ParagraphStyle('lead', parent=base,
        fontSize=12, leading=20, textColor=C_MUTED,
        spaceAfter=12, spaceBefore=4, leftIndent=12,
        borderPad=6, fontName='Helvetica-Oblique')

    s['code'] = ParagraphStyle('code', parent=base,
        fontName='Courier', fontSize=8.5, leading=14,
        textColor=C_CODE_TEXT, backColor=C_CODE_BG,
        leftIndent=0, rightIndent=0,
        spaceAfter=0, spaceBefore=0)

    s['code_label'] = ParagraphStyle('code_label', parent=base,
        fontName='Helvetica-Bold', fontSize=7, leading=10,
        textColor=C_MUTED, spaceAfter=0, spaceBefore=0)

    s['tip_title'] = ParagraphStyle('tip_title', parent=base,
        fontName='Helvetica-Bold', fontSize=9.5, leading=13,
        textColor=C_ACCENT, spaceAfter=2)

    s['tip_body'] = ParagraphStyle('tip_body', parent=base,
        fontSize=9, leading=14, textColor=HexColor('#a8d9b0'),
        spaceAfter=0)

    s['warn_title'] = ParagraphStyle('warn_title', parent=base,
        fontName='Helvetica-Bold', fontSize=9.5, leading=13,
        textColor=C_AMBER, spaceAfter=2)

    s['warn_body'] = ParagraphStyle('warn_body', parent=base,
        fontSize=9, leading=14, textColor=HexColor('#d9c0a8'),
        spaceAfter=0)

    s['info_title'] = ParagraphStyle('info_title', parent=base,
        fontName='Helvetica-Bold', fontSize=9.5, leading=13,
        textColor=C_ACCENT2, spaceAfter=2)

    s['info_body'] = ParagraphStyle('info_body', parent=base,
        fontSize=9, leading=14, textColor=HexColor('#a8c4d9'),
        spaceAfter=0)

    s['exercise_title'] = ParagraphStyle('exercise_title', parent=base,
        fontName='Helvetica-Bold', fontSize=11, leading=15,
        textColor=C_AMBER, spaceAfter=3)

    s['exercise_body'] = ParagraphStyle('exercise_body', parent=base,
        fontSize=9.5, leading=15, textColor=HexColor('#c5b88a'),
        spaceAfter=3)

    s['toc_chapter'] = ParagraphStyle('toc_chapter', parent=base,
        fontName='Helvetica-Bold', fontSize=13, leading=18,
        textColor=C_WHITE, spaceAfter=3, spaceBefore=6)

    s['toc_section'] = ParagraphStyle('toc_section', parent=base,
        fontName='Helvetica', fontSize=9.5, leading=14,
        textColor=C_MUTED, spaceAfter=1, spaceBefore=0,
        leftIndent=16)

    s['cover_tag'] = ParagraphStyle('cover_tag', parent=base,
        fontName='Helvetica-Bold', fontSize=8, leading=12,
        textColor=C_ACCENT, alignment=TA_CENTER, letterSpacing=3)

    s['bullet'] = ParagraphStyle('bullet', parent=base,
        fontSize=9.5, leading=15, textColor=HexColor('#c9d1d9'),
        spaceAfter=3, leftIndent=14, firstLineIndent=-10)

    s['center'] = ParagraphStyle('center', parent=base,
        alignment=TA_CENTER, fontSize=10, leading=16, textColor=C_MUTED)

    s['project_title'] = ParagraphStyle('project_title', parent=base,
        fontName='Helvetica-Bold', fontSize=19, leading=24,
        textColor=C_ACCENT, spaceAfter=4, spaceBefore=8)

    s['project_sub'] = ParagraphStyle('project_sub', parent=base,
        fontName='Helvetica-Bold', fontSize=11, leading=16,
        textColor=C_ACCENT2, spaceAfter=3, spaceBefore=8)

    s['tree'] = ParagraphStyle('tree', parent=base,
        fontName='Courier', fontSize=8.5, leading=14,
        textColor=C_CODE_TEXT, backColor=C_CODE_BG,
        leftIndent=0)

    return s

# ─────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────

def spacer(h=8):
    return Spacer(1, h)

def hr(color=C_BORDER, thickness=1):
    return HRFlowable(width="100%", thickness=thickness,
                      color=color, spaceAfter=8, spaceBefore=8)

def code_block(label, lines, s):
    """Bloque de código estilo terminal con etiqueta"""
    items = []
    # Header del bloque
    hdr_data = [[
        Paragraph(f"● ● ●", ParagraphStyle('dot', fontName='Helvetica',
            fontSize=8, textColor=HexColor('#ff5f57'), backColor=HexColor('#1a1a22'))),
        Paragraph(label.upper(), ParagraphStyle('lbl', fontName='Helvetica-Bold',
            fontSize=7, textColor=C_DIM, backColor=HexColor('#1a1a22'), alignment=TA_CENTER)),
        Paragraph("", ParagraphStyle('empty', backColor=HexColor('#1a1a22')))
    ]]
    hdr_table = Table(hdr_data, colWidths=[2*cm, None, 2*cm])
    hdr_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#1a1a22')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('BOX', (0,0), (-1,-1), 1, HexColor('#2d2d3a')),
    ]))
    items.append(hdr_table)

    # Código
    code_text = '\n'.join(lines)
    code_p = Paragraph(code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'),
                       ParagraphStyle('cp', fontName='Courier', fontSize=8, leading=13.5,
                           textColor=C_CODE_TEXT, backColor=C_CODE_BG,
                           leftIndent=12, rightIndent=12, spaceAfter=0, spaceBefore=0))
    code_wrap = Table([[code_p]], colWidths=[None])
    code_wrap.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CODE_BG),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOX', (0,0), (-1,-1), 1, HexColor('#2d2d3a')),
        ('LINEBELOW', (0,-1), (-1,-1), 2, HexColor('#2d2d3a')),
    ]))
    items.append(code_wrap)
    items.append(spacer(10))
    return items

def callout(icon, title, body, bg, title_style, body_style):
    """Callout box coloreado"""
    content = [
        Paragraph(f"{icon}  {title}", title_style),
        Paragraph(body, body_style)
    ]
    t = Table([[content]], colWidths=[None])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('ROUNDEDCORNERS', [6]),
        ('BOX', (0,0), (-1,-1), 1, HexColor('#2d4a35')),
    ]))
    return [t, spacer(8)]

def tip(title, body, s):
    return callout("💡", title, body, C_TIP_BG, s['tip_title'], s['tip_body'])

def warn(title, body, s):
    return callout("⚠️", title, body, C_WARN_BG, s['warn_title'], s['warn_body'])

def info(title, body, s):
    return callout("ℹ️", title, body, C_INFO_BG, s['info_title'], s['info_body'])

def exercise_block(num, level, title, instructions, s):
    """Bloque de ejercicio con nivel de dificultad"""
    stars = {"Fácil": "★☆☆", "Medio": "★★☆", "Difícil": "★★★"}[level]
    colors_lv = {"Fácil": C_ACCENT, "Medio": C_AMBER, "Difícil": C_ROSE}

    header = Table([[
        Paragraph(f"EJERCICIO {num}", ParagraphStyle('en', fontName='Helvetica-Bold',
            fontSize=7, textColor=HexColor('#1a1a22'), backColor=colors_lv[level])),
        Paragraph(f"{stars}  {level}", ParagraphStyle('el', fontName='Helvetica-Bold',
            fontSize=7, textColor=colors_lv[level], backColor=HexColor('#1a1a22'),
            alignment=TA_RIGHT)),
    ]], colWidths=[6*cm, None])
    header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors_lv[level]),
        ('BACKGROUND', (1,0), (1,0), HexColor('#1a1a22')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))

    body_items = [
        Paragraph(title, s['exercise_title']),
    ]
    for inst in instructions:
        body_items.append(Paragraph(f"▸  {inst}", s['exercise_body']))

    body_t = Table([[body_items]], colWidths=[None])
    body_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_EXERCISE),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('BOX', (0,0), (-1,-1), 1, HexColor('#2d2d1a')),
        ('LINEABOVE', (0,0), (-1,0), 2, colors_lv[level]),
    ]))

    return [spacer(6), header, body_t, spacer(10)]

def section_header(tag, title, s):
    return [
        Paragraph(f"// {tag}", s['chapter_tag']),
        Paragraph(title, s['h2']),
        hr(C_ACCENT, 2),
        spacer(6),
    ]

def sub_header(title, s):
    return [
        Paragraph(title, s['h3']),
        spacer(4),
    ]

def bullet_list(items, s):
    result = []
    for item in items:
        result.append(Paragraph(f"<bullet>•</bullet>  {item}", s['bullet']))
    return result

def colored_box(text, bg, text_color, s):
    p = Paragraph(text, ParagraphStyle('cb', fontName='Helvetica', fontSize=9,
        leading=14, textColor=text_color, backColor=bg))
    t = Table([[p]], colWidths=[None])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('BOX', (0,0), (-1,-1), 1, HexColor('#2d2d3a')),
    ]))
    return [t, spacer(8)]

# ─────────────────────────────────────────
# PORTADA
# ─────────────────────────────────────────
def make_cover(s):
    items = []
    items.append(spacer(60))

    # Decorative badge
    badge_data = [[ Paragraph("EDICIÓN 2026 · DESDE CERO · CON EJERCICIOS", s['cover_tag']) ]]
    badge_t = Table(badge_data, colWidths=[None])
    badge_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#0d2b1a')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
        ('BOX', (0,0), (-1,-1), 1, HexColor('#1a4a2a')),
    ]))
    items.append(badge_t)
    items.append(spacer(28))

    items.append(Paragraph("HTML &amp; CSS", ParagraphStyle('ct1', fontName='Helvetica-Bold',
        fontSize=54, leading=58, textColor=C_WHITE, alignment=TA_CENTER)))
    items.append(Paragraph("MODERNO 2026", ParagraphStyle('ct2', fontName='Helvetica-Bold',
        fontSize=54, leading=62, textColor=C_ACCENT, alignment=TA_CENTER)))
    items.append(spacer(10))
    items.append(Paragraph("Enfoque en Componentes", ParagraphStyle('ct3', fontName='Helvetica-Oblique',
        fontSize=22, leading=28, textColor=C_MUTED, alignment=TA_CENTER)))
    items.append(spacer(32))

    # Separator line
    items.append(HRFlowable(width="60%", thickness=2, color=C_ACCENT,
        hAlign='CENTER', spaceAfter=24, spaceBefore=0))

    items.append(Paragraph(
        "De la estructura semántica a sistemas de componentes de producción.<br/>"
        "Todo lo indispensable para construir interfaces web modernas,<br/>"
        "accesibles y con excelente experiencia de usuario.",
        ParagraphStyle('cs', fontName='Helvetica', fontSize=12.5, leading=20,
            textColor=HexColor('#8b949e'), alignment=TA_CENTER)))

    items.append(spacer(40))

    # Feature chips
    chips = ["Component-Driven", "Design Tokens", "CSS Custom Properties",
             "WCAG 2.2", "Mobile First", "Dark Mode", "Ejercicios Prácticos",
             "Proyecto Final Incluido"]
    chip_text = "  ·  ".join(chips)
    items.append(Paragraph(chip_text, ParagraphStyle('chips', fontName='Helvetica-Bold',
        fontSize=7.5, leading=12, textColor=C_ACCENT, alignment=TA_CENTER, letterSpacing=1)))

    items.append(spacer(50))
    items.append(HRFlowable(width="100%", thickness=1, color=C_BORDER,
        hAlign='CENTER', spaceAfter=16))

    items.append(Paragraph(
        "HTML Living Standard  ·  CSS Level 4+  ·  Responsive First  ·  UX Driven",
        ParagraphStyle('footer_cover', fontName='Helvetica', fontSize=8,
            textColor=C_DIM, alignment=TA_CENTER)))

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# TABLA DE CONTENIDOS
# ─────────────────────────────────────────
def make_toc(s):
    items = []
    items += section_header("ÍNDICE", "Tabla de Contenidos", s)
    items.append(spacer(8))

    toc_data = [
        ("CAPÍTULO 1", "¿Qué es HTML y CSS? — Empezando desde cero", 5),
        ("CAPÍTULO 2", "Estructura HTML Semántica — El esqueleto correcto", 9),
        ("CAPÍTULO 3", "CSS Fundamentos — Selección, cascada y especificidad", 14),
        ("CAPÍTULO 4", "Box Model & Display — Todo es una caja", 19),
        ("CAPÍTULO 5", "Flexbox — Layouts en una dimensión", 24),
        ("CAPÍTULO 6", "CSS Grid — Layouts bidimensionales", 30),
        ("CAPÍTULO 7", "Design Tokens & Variables CSS", 36),
        ("CAPÍTULO 8", "Componentes Base: Botones, Badges, Alertas", 41),
        ("CAPÍTULO 9", "Componentes de Formulario", 47),
        ("CAPÍTULO 10", "Componentes de Tarjetas y Listas", 53),
        ("CAPÍTULO 11", "Navegación y Modales", 58),
        ("CAPÍTULO 12", "Tipografía y Espaciado", 64),
        ("CAPÍTULO 13", "Responsive Design y Container Queries", 69),
        ("CAPÍTULO 14", "Animaciones y Microinteracciones", 75),
        ("CAPÍTULO 15", "Accesibilidad (A11y) y UX", 81),
        ("CAPÍTULO 16", "Dark Mode y Temas de Color", 86),
        ("CAPÍTULO 17", "Arquitectura CSS — @layer y BEM", 91),
        ("PROYECTO FINAL", "Portafolio de Desarrollador — Guía Completa", 97),
    ]

    for cap, title, page in toc_data:
        row = [
            Paragraph(f"<b>{cap}</b>", ParagraphStyle('tc', fontName='Helvetica-Bold',
                fontSize=8.5, textColor=C_ACCENT, leading=13)),
            Paragraph(title, ParagraphStyle('tt', fontName='Helvetica',
                fontSize=9.5, textColor=C_TEXT, leading=13)),
            Paragraph(str(page), ParagraphStyle('tp', fontName='Helvetica-Bold',
                fontSize=8.5, textColor=C_MUTED, leading=13, alignment=TA_RIGHT)),
        ]
        t = Table([row], colWidths=[3.5*cm, None, 1.2*cm])
        t.setStyle(TableStyle([
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('LINEBELOW', (0,0), (-1,-1), 1, C_BORDER),
            ('BACKGROUND', (0,0), (0,-1), HexColor('#0d1a10')),
        ]))
        items.append(t)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 1: Qué es HTML y CSS
# ─────────────────────────────────────────
def chapter_1(s):
    items = []
    items += section_header("CAPÍTULO 01", "¿Qué es HTML y CSS?\nEmpezando desde Cero", s)

    items.append(Paragraph(
        "Imagina que estás construyendo una casa. El HTML sería los ladrillos, "
        "las paredes y la estructura. El CSS sería la pintura, los muebles y la decoración. "
        "Juntos hacen que una página web se vea bien y funcione.", s['lead']))

    items += sub_header("1.1 ¿Qué es HTML?", s)
    items.append(Paragraph(
        "HTML significa <b>HyperText Markup Language</b> (Lenguaje de Marcado de Hipertexto). "
        "Es el lenguaje que le dice al navegador QUÉ hay en la página: "
        "un título, un párrafo, una imagen, un botón, etc.", s['body']))

    items += tip("Analogía para recordarlo siempre",
        "HTML = El CONTENIDO y la ESTRUCTURA. CSS = El ESTILO y la APARIENCIA. "
        "JavaScript = El COMPORTAMIENTO y la INTERACTIVIDAD.", s)

    items += sub_header("1.2 Estructura Básica de HTML", s)
    items.append(Paragraph(
        "Todo archivo HTML tiene una estructura mínima obligatoria. "
        "Sin esto, el navegador no sabe cómo interpretar tu página correctamente:", s['body']))

    items += code_block("HTML — estructura-minima.html", [
        '<!DOCTYPE html>              <!-- Le dice al navegador: "soy HTML5" -->',
        '<html lang="es">             <!-- Elemento raíz. lang="es" indica español -->',
        '<head>                       <!-- Información para el navegador (no visible) -->',
        '  <meta charset="UTF-8">    <!-- Acepta letras como ñ, á, é, etc. -->',
        '  <meta name="viewport"     <!-- MUY IMPORTANTE: hace la web responsive -->',
        '        content="width=device-width, initial-scale=1.0">',
        '  <title>Mi Primera Página</title>  <!-- Título en la pestaña del navegador -->',
        '  <link rel="stylesheet" href="css/styles.css">  <!-- Enlaza tu CSS -->',
        '</head>',
        '<body>                       <!-- Todo lo visible va aquí -->',
        '',
        '  <h1>Hola Mundo</h1>       <!-- Título principal -->',
        '  <p>Mi primer párrafo.</p>  <!-- Un párrafo de texto -->',
        '',
        '</body>',
        '</html>',
    ], s)

    items += sub_header("1.3 ¿Qué es CSS?", s)
    items.append(Paragraph(
        "CSS significa <b>Cascading Style Sheets</b> (Hojas de Estilo en Cascada). "
        "Es el lenguaje que le dice al navegador CÓMO se ve la página: "
        "colores, tamaños, posiciones, fuentes, etc.", s['body']))

    items += code_block("CSS — styles.css (primeros estilos)", [
        '/* Esto es un comentario en CSS — el navegador lo ignora */',
        '',
        '/* Seleccionamos el elemento body y le ponemos estilos */',
        'body {',
        '  background-color: #f5f5f5;  /* Color de fondo: gris claro */',
        '  color: #333333;             /* Color del texto: casi negro */',
        '  font-family: Arial, sans-serif;  /* Fuente del texto */',
        '  margin: 0;                  /* Sin márgenes externos */',
        '  padding: 0;                 /* Sin espaciado interno */',
        '}',
        '',
        '/* Seleccionamos todos los h1 */',
        'h1 {',
        '  color: #0070f3;             /* Color azul para títulos */',
        '  font-size: 2rem;            /* Tamaño: 2 veces el tamaño base */',
        '}',
    ], s)

    items += sub_header("1.4 Cómo se conectan HTML y CSS", s)
    items.append(Paragraph(
        "Hay 3 formas de añadir CSS a tu HTML. La mejor práctica es siempre usar "
        "un <b>archivo externo</b> separado:", s['body']))

    # Tabla comparativa
    table_data = [
        [Paragraph("<b>Método</b>", s['h5']),
         Paragraph("<b>Cómo se usa</b>", s['h5']),
         Paragraph("<b>Recomendado</b>", s['h5'])],
        [Paragraph("Externo (✓ MEJOR)", s['body_small']),
         Paragraph('<link rel="stylesheet" href="styles.css">', s['body_small']),
         Paragraph("✅ Sí", s['body_small'])],
        [Paragraph("Interno", s['body_small']),
         Paragraph('<style> body { color: red; } </style>', s['body_small']),
         Paragraph("⚠️ A veces", s['body_small'])],
        [Paragraph("En línea (✗ EVITAR)", s['body_small']),
         Paragraph('<p style="color:red">Texto</p>', s['body_small']),
         Paragraph("❌ No", s['body_small'])],
    ]
    t = Table(table_data, colWidths=[4*cm, None, 2.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1a1a22')),
        ('BACKGROUND', (0,1), (-1,-1), C_CODE_BG),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_CODE_BG, HexColor('#0f0f16')]),
        ('TEXTCOLOR', (0,0), (-1,0), C_ACCENT),
        ('GRID', (0,0), (-1,-1), 1, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    items.append(t)
    items.append(spacer(10))

    items += warn("Nunca uses estilos en línea",
        "Escribir style='...' directamente en el HTML mezcla contenido con presentación. "
        "Esto hace el código difícil de mantener. Usa siempre un archivo .css separado.", s)

    # Ejercicios
    items.append(spacer(10))
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 1 ──", s['h4']))
    items.append(spacer(6))

    items += exercise_block(1, "Fácil", "Tu primera página HTML",
        ["Crea un archivo llamado index.html",
         "Escribe la estructura mínima de HTML (DOCTYPE, html, head, body)",
         "Agrega un título en la pestaña: 'Mi Portfolio'",
         "Dentro del body agrega: un h1 con tu nombre, un párrafo que diga 'Bienvenido a mi portafolio'",
         "Abre el archivo en tu navegador — ¡ya tienes tu primera web!"], s)

    items += exercise_block(2, "Fácil", "Conecta tu primer CSS",
        ["Crea una carpeta llamada 'css'",
         "Dentro crea el archivo 'css/styles.css'",
         "En el CSS pon: body { background-color: #1a1a2e; color: white; font-family: Arial; }",
         "Enlaza el CSS desde tu HTML con <link rel='stylesheet' href='css/styles.css'>",
         "Recarga el navegador y ve cómo cambia la apariencia"], s)

    items += exercise_block(3, "Medio", "Experimenta con colores y fuentes",
        ["En tu styles.css cambia el color del h1 a tu color favorito",
         "Prueba font-family con: Georgia, Verdana, 'Times New Roman'",
         "Agrega font-size: 3rem al h1 y observa el cambio",
         "Agrega al body: margin: 20px y compara con margin: 0",
         "Pregunta: ¿qué diferencia hay entre color y background-color?"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 2: HTML Semántico
# ─────────────────────────────────────────
def chapter_2(s):
    items = []
    items += section_header("CAPÍTULO 02", "HTML Semántico\nEl Esqueleto Correcto", s)

    items.append(Paragraph(
        "Semántico significa que cada elemento HTML tiene un SIGNIFICADO específico. "
        "No es solo código — le dice a los navegadores, motores de búsqueda y "
        "personas con discapacidad qué es cada parte de tu página.", s['lead']))

    items += sub_header("2.1 Elementos de Sección (los más importantes)", s)
    items.append(Paragraph(
        "Estos son los elementos que organizan tu página en regiones con significado:", s['body']))

    items += code_block("HTML — estructura-semantica.html", [
        '<body>',
        '  <!-- HEADER: Cabecera del sitio (logo, nav) -->',
        '  <!-- Regla: Solo UN header principal por página -->',
        '  <header>',
        '    <a href="/" class="logo">Mi Portfolio</a>',
        '    <nav aria-label="navegación principal">  <!-- aria-label lo describe -->',
        '      <a href="#proyectos">Proyectos</a>',
        '      <a href="#contacto">Contacto</a>',
        '    </nav>',
        '  </header>',
        '',
        '  <!-- MAIN: Contenido único de ESTA página -->',
        '  <!-- Regla: Solo UN main por página -->',
        '  <main id="main-content">',
        '',
        '    <!-- SECTION: Agrupa contenido relacionado con un tema -->',
        '    <!-- Siempre debe tener un heading (h1-h6) -->',
        '    <section aria-labelledby="titulo-hero">',
        '      <h1 id="titulo-hero">Hola, soy Juan</h1>',
        '      <p>Desarrollador Frontend apasionado.</p>',
        '    </section>',
        '',
        '    <!-- ARTICLE: Contenido autónomo (puede existir solo) -->',
        '    <article>',
        '      <h2>Proyecto: App del Tiempo</h2>',
        '      <p>Descripción del proyecto...</p>',
        '    </article>',
        '',
        '    <!-- ASIDE: Información relacionada pero no principal -->',
        '    <aside>',
        '      <p>Dato curioso: llevo 3 años programando</p>',
        '    </aside>',
        '',
        '  </main>',
        '',
        '  <!-- FOOTER: Pie de página -->',
        '  <footer>',
        '    <p>© 2026 Juan García</p>',
        '  </footer>',
        '',
        '</body>',
    ], s)

    items += sub_header("2.2 Jerarquía de Headings (h1 a h6)", s)
    items.append(Paragraph(
        "Los headings son como un índice de libro. El h1 es el título principal, "
        "h2 son capítulos, h3 son subcapítulos, etc. <b>NUNCA saltes niveles</b>:", s['body']))

    items += code_block("HTML — jerarquia-correcta.html", [
        '<!-- ✅ CORRECTO: jerarquía lógica sin saltos -->',
        '<h1>Portfolio de Ana García</h1>',
        '  <h2>Mis Proyectos</h2>',
        '    <h3>Diseño Web</h3>',
        '      <h4>Proyecto Alpha</h4>',
        '    <h3>Aplicaciones Móviles</h3>',
        '  <h2>Sobre Mí</h2>',
        '    <h3>Experiencia</h3>',
        '',
        '<!-- ❌ INCORRECTO: salta de h1 a h4 -->',
        '<!-- Esto confunde a los lectores de pantalla y al SEO -->',
        '<h1>Mi Portfolio</h1>',
        '<h4>Proyectos</h4>  <!-- ← MALO: saltó h2 y h3 -->',
        '',
        '<!-- ❌ INCORRECTO: usar headings para hacer texto grande -->',
        '<!-- No uses h2 solo porque quieres letra grande -->',
        '<h2>Texto grande pero no es un título</h2>',
        '<!-- ✅ Usa CSS para el tamaño, no el heading -->',
        '<p class="texto-grande">Texto grande</p>',
    ], s)

    items += tip("Regla de oro para headings",
        "Pregúntate: ¿Si alguien leyera solo los headings de mi página, "
        "entendería de qué trata? Si la respuesta es sí, tu jerarquía está bien.", s)

    items += sub_header("2.3 Elementos de Texto Importantes", s)

    items += code_block("HTML — elementos-texto.html", [
        '<!-- Para enfatizar texto con SIGNIFICADO (no solo visual) -->',
        '<strong>Texto muy importante</strong>  <!-- Énfasis fuerte (negrita semántica) -->',
        '<em>Texto con énfasis</em>              <!-- Énfasis suave (cursiva semántica) -->',
        '',
        '<!-- ❌ NO uses b e i para dar significado: son solo visuales -->',
        '<b>Negrita visual</b>   <!-- Sin significado semántico -->',
        '<i>Cursiva visual</i>   <!-- Sin significado semántico -->',
        '',
        '<!-- Listas: la más usada en portfolios -->',
        '<ul>                           <!-- Lista sin orden (bullets) -->',
        '  <li>HTML & CSS</li>          <!-- Cada ítem de la lista -->',
        '  <li>JavaScript</li>',
        '  <li>React</li>',
        '</ul>',
        '',
        '<ol>                           <!-- Lista con orden (números) -->',
        '  <li>Planifica el proyecto</li>',
        '  <li>Diseña el wireframe</li>',
        '  <li>Escribe el código</li>',
        '</ol>',
        '',
        '<!-- Imágenes: SIEMPRE con alt -->',
        '<img',
        '  src="foto-perfil.jpg"',
        '  alt="Ana García sonriendo frente a su computadora"  <!-- OBLIGATORIO -->',
        '  width="300"         <!-- Define dimensiones: evita saltos visuales -->',
        '  height="300"',
        '  loading="lazy"      <!-- Carga solo cuando el usuario llega a la imagen -->',
        '>',
        '',
        '<!-- Links -->',
        '<a href="https://github.com/ana" target="_blank"  <!-- Abre en nueva pestaña -->',
        '   rel="noopener noreferrer">   <!-- Seguridad al abrir en nueva pestaña -->',
        '  Ver en GitHub',
        '</a>',
    ], s)

    items += warn("El atributo alt en imágenes no es opcional",
        "Si una imagen transmite información, alt debe describirla. "
        "Si es decorativa, usa alt='' (cadena vacía). "
        "Nunca pongas alt='imagen' o alt='foto' — eso no dice nada.", s)

    # Ejercicios
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 2 ──", s['h4']))
    items.append(spacer(6))

    items += exercise_block(4, "Fácil", "Estructura semántica de tu portfolio",
        ["Actualiza tu index.html con: header, main, footer",
         "Dentro del main agrega una section para el hero y otra para proyectos",
         "Verifica en Chrome DevTools → Accessibility → que el árbol sea correcto",
         "Añade aria-label='navegación principal' a tu nav"], s)

    items += exercise_block(5, "Medio", "Página de proyecto con article",
        ["Crea proyecto-detalle.html",
         "Usa article para envolver el contenido del proyecto",
         "Agrega: h1 con el nombre, h2 'Descripción', h3 'Tecnologías usadas'",
         "Agrega una imagen con alt descriptivo y loading='lazy'",
         "Agrega una lista <ul> con las tecnologías usadas"], s)

    items += exercise_block(6, "Difícil", "Auditoría de semántica",
        ["Abre cualquier sitio web que uses frecuentemente",
         "Con clic derecho → Inspeccionar → busca el HTML",
         "Identifica: ¿usa header, main, footer, nav correctamente?",
         "¿Los h1-h6 están en orden lógico?",
         "¿Las imágenes tienen alt descriptivo?",
         "Documenta 3 buenas prácticas y 3 errores que encuentres"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 3: CSS Fundamentos
# ─────────────────────────────────────────
def chapter_3(s):
    items = []
    items += section_header("CAPÍTULO 03", "CSS Fundamentos\nSelección, Cascada y Especificidad", s)

    items.append(Paragraph(
        "CSS funciona aplicando estilos a través de 'selectores'. "
        "Cuando hay conflicto entre reglas, CSS decide cuál gana usando la cascada y la especificidad. "
        "Entender esto es la clave para no luchar contra tu propio CSS.", s['lead']))

    items += sub_header("3.1 Selectores CSS", s)
    items.append(Paragraph("Los selectores son el 'apunta a esto' de CSS:", s['body']))

    items += code_block("CSS — selectores.css", [
        '/* ─── SELECTOR DE ELEMENTO: afecta TODOS los elementos de ese tipo ─── */',
        'p { color: gray; }              /* Todos los párrafos en gris */',
        'h1 { font-size: 2rem; }         /* Todos los h1 grandes */',
        '',
        '/* ─── SELECTOR DE CLASE: afecta elementos con esa clase ─── */',
        '/* En HTML: <div class="tarjeta">...</div> */',
        '.tarjeta { background: white; padding: 20px; }',
        '.btn-principal { background: blue; color: white; }',
        '',
        '/* ─── SELECTOR DE ID: afecta UN elemento único ─── */',
        '/* En HTML: <div id="hero">...</div> */',
        '/* Úsalo con moderación — las clases son más reutilizables */',
        '#hero { min-height: 100vh; }',
        '',
        '/* ─── SELECTOR DE ATRIBUTO ─── */',
        '[type="email"] { border: 2px solid blue; }  /* Inputs de email */',
        '[disabled] { opacity: 0.5; cursor: not-allowed; }',
        '',
        '/* ─── SELECTORES COMBINADOS ─── */',
        '.card .card-title { font-size: 1.5rem; }  /* .card-title DENTRO de .card */',
        '.btn + .btn { margin-left: 8px; }         /* .btn junto a otro .btn */',
        '.lista > li { padding: 8px; }             /* li HIJO DIRECTO de .lista */',
        '',
        '/* ─── PSEUDO-CLASES: estados del elemento ─── */',
        'a:hover { color: blue; }          /* Cuando el mouse está encima */',
        'button:focus-visible { outline: 2px solid blue; }  /* Cuando tiene foco (teclado) */',
        'input:valid { border-color: green; }   /* Input con valor válido */',
        'li:first-child { font-weight: bold; }  /* Primer elemento de una lista */',
        'li:nth-child(2n) { background: #f5f5f5; }  /* Elementos pares */',
        '',
        '/* ─── PSEUDO-ELEMENTOS: partes del elemento ─── */',
        'p::first-line { font-weight: bold; }    /* Primera línea del párrafo */',
        '.btn::before { content: "→ "; }         /* Agrega contenido antes */',
        '::selection { background: yellow; }     /* Texto seleccionado por el usuario */',
        '::placeholder { color: #999; }          /* Texto placeholder de inputs */',
    ], s)

    items += sub_header("3.2 La Cascada: ¿Quién Gana?", s)
    items.append(Paragraph(
        "Cuando dos reglas CSS apuntan al mismo elemento, ¿cuál se aplica? "
        "CSS tiene un sistema de prioridades claro:", s['body']))

    # Tabla de prioridad
    prio_data = [
        [Paragraph("<b>Prioridad</b>", s['h5']),
         Paragraph("<b>Tipo</b>", s['h5']),
         Paragraph("<b>Ejemplo</b>", s['h5']),
         Paragraph("<b>Puntos</b>", s['h5'])],
        [Paragraph("1° (gana)", s['body_small']),
         Paragraph("!important", s['body_small']),
         Paragraph("color: red !important", s['body_small']),
         Paragraph("∞", s['body_small'])],
        [Paragraph("2°", s['body_small']),
         Paragraph("Estilos en línea", s['body_small']),
         Paragraph('<div style="color:red">', s['body_small']),
         Paragraph("1000", s['body_small'])],
        [Paragraph("3°", s['body_small']),
         Paragraph("ID", s['body_small']),
         Paragraph("#hero { color: red }", s['body_small']),
         Paragraph("100", s['body_small'])],
        [Paragraph("4°", s['body_small']),
         Paragraph("Clase / Atributo", s['body_small']),
         Paragraph(".btn { color: red }", s['body_small']),
         Paragraph("10", s['body_small'])],
        [Paragraph("5° (pierde)", s['body_small']),
         Paragraph("Elemento", s['body_small']),
         Paragraph("p { color: red }", s['body_small']),
         Paragraph("1", s['body_small'])],
    ]
    t = Table(prio_data, colWidths=[2.5*cm, 3.5*cm, None, 2*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1a1a22')),
        ('TEXTCOLOR', (0,0), (-1,0), C_ACCENT),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_CODE_BG, HexColor('#0f0f16')]),
        ('GRID', (0,0), (-1,-1), 1, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ]))
    items.append(t)
    items.append(spacer(10))

    items += warn("!important es la última opción",
        "Usa !important solo para sobreescribir estilos de librerías externas. "
        "Si lo usas mucho en tu propio código, significa que tu especificidad "
        "está mal organizada. Es como gritar siempre — pierde efectividad.", s)

    items += sub_header("3.3 La Herencia: Propiedades que se Propagan", s)
    items.append(Paragraph(
        "Algunas propiedades CSS se heredan automáticamente de padre a hijo. "
        "Esto es muy útil: defines la fuente en el body y todos los elementos la heredan.", s['body']))

    items += code_block("CSS — herencia.css", [
        '/* Propiedades que SÍ se heredan: */',
        'body {',
        '  /* ✅ Estas se propagan a todos los hijos automáticamente */',
        '  font-family: "Syne", sans-serif;  /* Fuente */,',
        '  font-size: 16px;                  /* Tamaño base */',
        '  color: #333;                       /* Color de texto */',
        '  line-height: 1.6;                  /* Interlineado */',
        '}',
        '',
        '/* Propiedades que NO se heredan: */',
        '/* margin, padding, border, background, width, height */',
        '/* Cada elemento tiene sus propios valores por defecto */',
        '',
        '/* Puedes forzar herencia con "inherit" */',
        '.boton {',
        '  border: inherit;        /* Hereda el borde del padre */',
        '  color: inherit;         /* Hereda el color aunque no se heredaría */',
        '}',
    ], s)

    # Ejercicios Cap 3
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 3 ──", s['h4']))
    items.append(spacer(6))

    items += exercise_block(7, "Fácil", "Experimenta con selectores",
        ["Agrega al HTML un párrafo con class='destacado' y uno sin clase",
         "En CSS: p { color: gray } y .destacado { color: red; font-weight: bold }",
         "Observa: ¿cuál tiene más prioridad?",
         "Agrega también un estilo en línea al párrafo sin clase y observa qué pasa"], s)

    items += exercise_block(8, "Medio", "Batalla de especificidad",
        ["Crea un div con id='caja' y class='azul rojo'",
         "En CSS escribe: #caja { color: green } .azul { color: blue } .rojo { color: red }",
         "¿Qué color gana? ¿Por qué?",
         "Ahora agrega: div { color: orange !important } — ¿qué pasa?",
         "Reflexión: ¿Cuándo usarías !important en un proyecto real?"], s)

    items += exercise_block(9, "Difícil", "Sistema de clases para tu portfolio",
        ["Planifica las clases que necesitarás (sin escribir HTML todavía)",
         "Escribe: .btn, .btn-primary, .btn-secondary, .card, .card-title, .card-body",
         "Para cada una, define en CSS 2-3 propiedades lógicas",
         "Crea un archivo CSS/components/button.css separado para los botones",
         "Reflexión: ¿por qué es mejor .btn-primary que #btn-primario?"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 4: Box Model
# ─────────────────────────────────────────
def chapter_4(s):
    items = []
    items += section_header("CAPÍTULO 04", "Box Model & Display\nTodo es una Caja", s)

    items.append(Paragraph(
        "En CSS, ABSOLUTAMENTE TODOS los elementos son cajas rectangulares. "
        "Una imagen es una caja. Un texto es una caja. Un botón es una caja. "
        "El Box Model describe cómo se calcula el tamaño de esas cajas.", s['lead']))

    items += sub_header("4.1 Las 4 Capas del Box Model", s)
    items.append(Paragraph(
        "Cada elemento tiene 4 capas, de adentro hacia afuera:", s['body']))

    # Box model visual con tabla
    bm_data = [
        [Paragraph("MARGIN\n(espacio exterior — transparente)", ParagraphStyle('bm',
            fontName='Helvetica-Bold', fontSize=8, textColor=HexColor('#f0b030'),
            alignment=TA_CENTER, leading=12))],
    ]

    items += code_block("CSS — box-model.css (el más importante del libro)", [
        '/* ═══════════════════════════════════════════════════════ */',
        '/*  LA REGLA #1 DE TODO PROYECTO — Escríbela SIEMPRE     */',
        '/* ═══════════════════════════════════════════════════════ */',
        '',
        '*,                 /* El asterisco selecciona TODOS los elementos */',
        '*::before,         /* Incluyendo el pseudo-elemento before */',
        '*::after {         /* Y el pseudo-elemento after */',
        '  box-sizing: border-box;  /* El tamaño INCLUYE padding y borde */',
        '  /* Sin esto: width:200px + padding:20px = 240px (sorpresa!) */',
        '  /* Con esto: width:200px + padding:20px = 200px (predecible) */',
        '}',
        '',
        '/* ─── LAS 4 CAPAS ─── */',
        '.caja {',
        '  /* CONTENIDO: el área donde va el texto/imagen */',
        '  width: 300px;           /* Ancho del contenido */',
        '  height: 150px;          /* Alto del contenido */',
        '',
        '  /* PADDING: espacio INTERIOR (entre contenido y borde) */',
        '  padding: 20px;          /* 20px en los 4 lados */',
        '  padding: 10px 20px;     /* 10px arriba/abajo, 20px izq/der */',
        '  padding-top: 10px;      /* Solo arriba */',
        '  padding-inline: 20px;   /* Izquierda y derecha (moderno 2026) */',
        '',
        '  /* BORDER: el borde visible */',
        '  border: 2px solid #333;  /* Grosor, estilo, color */',
        '  border-radius: 8px;      /* Esquinas redondeadas */',
        '',
        '  /* MARGIN: espacio EXTERIOR (entre este y otros elementos) */',
        '  margin: 16px;           /* 16px en los 4 lados */',
        '  margin: 0 auto;         /* 0 arriba/abajo, auto centra horizontalmente */',
        '  margin-block: 24px;     /* Arriba y abajo (moderno 2026) */',
        '}',
        '',
        '/* El colapso de márgenes: margen arriba + margen abajo = el mayor, no la suma */',
        '.parrafo-1 { margin-bottom: 20px; }',
        '.parrafo-2 { margin-top: 30px; }',
        '/* El espacio entre ellos será 30px (el mayor), NO 50px */',
    ], s)

    items += tip("Por qué box-sizing: border-box es la regla #1",
        "Sin border-box, si pones width:300px y padding:20px, "
        "el elemento tendrá 340px de ancho total — ¡una sorpresa! "
        "Con border-box, siempre tendrá 300px. Esto hace el diseño predecible.", s)

    items += sub_header("4.2 Display: Cómo se Comporta la Caja", s)
    items.append(Paragraph(
        "La propiedad <b>display</b> controla cómo el elemento participa "
        "en el flujo del documento:", s['body']))

    items += code_block("CSS — display.css", [
        '/* ─── block: ocupa TODO el ancho disponible ─── */',
        '/* Los div, p, h1-h6, section son block por defecto */',
        '.bloque {',
        '  display: block;        /* Una línea completa para él solo */',
        '  width: 50%;            /* Puedes darle ancho */',
        '  margin: 0 auto;        /* Y centrarlo horizontalmente */',
        '}',
        '',
        '/* ─── inline: solo ocupa el ancho de su contenido ─── */',
        '/* Los span, a, strong, em son inline por defecto */',
        '.en-linea {',
        '  display: inline;       /* Fluye con el texto */',
        '  /* ❌ width y height NO funcionan en inline */',
        '  /* ❌ margin-top y margin-bottom NO funcionan */',
        '}',
        '',
        '/* ─── inline-block: lo mejor de ambos mundos ─── */',
        '.boton-antiguo {',
        '  display: inline-block; /* Fluye en línea PERO acepta dimensiones */',
        '  width: 120px;          /* Ahora sí funciona */',
        '  padding: 10px 20px;',
        '}',
        '',
        '/* ─── flex: para layouts (los más usados hoy) ─── */',
        '.contenedor-flex {',
        '  display: flex;         /* Activa Flexbox para los hijos */',
        '  /* Ver Capítulo 5 para Flexbox completo */',
        '}',
        '',
        '/* ─── grid: para layouts bidimensionales ─── */',
        '.contenedor-grid {',
        '  display: grid;         /* Activa CSS Grid para los hijos */',
        '  /* Ver Capítulo 6 para Grid completo */',
        '}',
        '',
        '/* ─── none: el elemento DESAPARECE del flujo ─── */',
        '.oculto {',
        '  display: none;         /* Como si no existiera en el HTML */',
        '  /* Los lectores de pantalla tampoco lo leen */',
        '}',
        '',
        '/* ─── Ocultar visualmente pero mantener accesible ─── */',
        '.sr-only {',
        '  position: absolute;    /* Sale del flujo normal */',
        '  width: 1px;            /* Casi invisible */',
        '  height: 1px;',
        '  overflow: hidden;      /* Esconde el contenido que sobresalga */',
        '  clip: rect(0,0,0,0);',
        '  white-space: nowrap;',
        '  /* ✅ Los lectores de pantalla SÍ lo leen */',
        '}',
    ], s)

    items += sub_header("4.3 Position: Cómo se Posiciona la Caja", s)

    items += code_block("CSS — position.css", [
        '/* ─── static (por defecto): flujo normal ─── */',
        '.normal { position: static; }  /* top/left NO tienen efecto aquí */',
        '',
        '/* ─── relative: se mueve respecto a SU posición original ─── */',
        '.relativo {',
        '  position: relative;',
        '  top: 10px;    /* Se mueve 10px hacia abajo desde donde estaría */',
        '  left: 20px;   /* Se mueve 20px hacia la derecha */',
        '  /* El espacio original se mantiene reservado */',
        '}',
        '',
        '/* ─── absolute: se posiciona respecto al ANCESTRO con position ─── */',
        '.contenedor { position: relative; }  /* Ancla al padre */',
        '.badge {',
        '  position: absolute;',
        '  top: -8px;    /* 8px arriba del borde del padre */',
        '  right: -8px;  /* 8px a la derecha del borde del padre */',
        '}',
        '',
        '/* ─── fixed: se fija al VIEWPORT (ventana) ─── */',
        '.navbar {',
        '  position: fixed;',
        '  top: 0;        /* Siempre arriba de la pantalla */',
        '  left: 0;',
        '  width: 100%;   /* Ocupa todo el ancho */',
        '  z-index: 100;  /* Por encima de otros elementos */',
        '}',
        '',
        '/* ─── sticky: hibrido relative + fixed ─── */',
        '.header-seccion {',
        '  position: sticky;',
        '  top: 60px;    /* Se queda fijo cuando llega a 60px del tope */',
        '  /* Antes de llegar, se comporta como relative */',
        '}',
    ], s)

    # Ejercicios
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 4 ──", s['h4']))
    items.append(spacer(6))

    items += exercise_block(10, "Fácil", "Experimenta con el Box Model",
        ["Crea un div con: width:200px, height:100px, padding:20px, border:2px solid red, margin:30px",
         "SIN box-sizing: border-box — mide el ancho total resultante",
         "AGREGA box-sizing: border-box — mide nuevamente",
         "¿Qué diferencia hay?",
         "Agrega la regla *, *::before, *::after { box-sizing: border-box } al inicio de tu CSS"], s)

    items += exercise_block(11, "Medio", "Construye tu primera card",
        ["Crea un div con class='card'",
         "Dale: background white, padding:24px, border-radius:12px, border:1px solid #e0e0e0",
         "Agrega un h3 con el nombre de un proyecto, un párrafo de descripción",
         "Agrega margin: 20px para separar múltiples cards",
         "Bonus: agrega box-shadow: 0 4px 12px rgba(0,0,0,0.1)"], s)

    items += exercise_block(12, "Difícil", "Badge sobre una card (position absolute)",
        ["A tu card del ejercicio anterior, agrega position: relative",
         "Crea un span con class='badge' que diga 'Nuevo'",
         "Posiciona el badge con position:absolute, top:-8px, right:16px",
         "Dale estilo: background azul, color blanco, padding:2px 10px, border-radius:100px",
         "Resultado: un badge flotando sobre la esquina de la card"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 5: Flexbox
# ─────────────────────────────────────────
def chapter_5(s):
    items = []
    items += section_header("CAPÍTULO 05", "Flexbox\nLayouts en Una Dimensión", s)

    items.append(Paragraph(
        "Flexbox es el sistema de layout más usado para componentes. "
        "Resuelve en una línea de CSS lo que antes requería trucos complicados. "
        "Su superpoder: distribuir y alinear elementos en una fila o columna.", s['lead']))

    items += sub_header("5.1 Conceptos Base de Flexbox", s)

    items += code_block("CSS — flexbox-base.css", [
        '/* ─── El contenedor padre activa Flexbox ─── */',
        '.flex-contenedor {',
        '  display: flex;          /* ✨ Activa Flexbox para los HIJOS DIRECTOS */',
        '',
        '  /* ── Dirección del flujo principal ── */',
        '  flex-direction: row;          /* → Horizontal (por defecto) */',
        '  /* flex-direction: row-reverse;   ← Horizontal al revés */',
        '  /* flex-direction: column;         ↓ Vertical */',
        '  /* flex-direction: column-reverse; ↑ Vertical al revés */',
        '',
        '  /* ── ¿Se envuelven los items? ── */',
        '  flex-wrap: nowrap;    /* En una sola línea (por defecto) */',
        '  /* flex-wrap: wrap;     Se van a la siguiente línea si no caben */',
        '',
        '  /* ── Alineación en el eje PRINCIPAL (horizontal en row) ── */',
        '  justify-content: flex-start;    /* Todos a la izquierda (por defecto) */',
        '  /* justify-content: flex-end;      Todos a la derecha */',
        '  /* justify-content: center;         Centrados */',
        '  /* justify-content: space-between;  Espacio entre items, no en extremos */',
        '  /* justify-content: space-around;   Espacio alrededor de cada item */',
        '  /* justify-content: space-evenly;   Espacio igual entre TODOS */',
        '',
        '  /* ── Alineación en el eje CRUZADO (vertical en row) ── */',
        '  align-items: stretch;     /* Estira para llenar el alto (por defecto) */',
        '  /* align-items: flex-start;  Alineados arriba */',
        '  /* align-items: flex-end;    Alineados abajo */',
        '  /* align-items: center;      Centrados verticalmente */',
        '  /* align-items: baseline;    Alineados por línea base del texto */',
        '',
        '  /* ── Espacio entre items ── */',
        '  gap: 16px;            /* Espacio entre TODOS los items */',
        '  row-gap: 24px;        /* Solo entre filas */',
        '  column-gap: 16px;     /* Solo entre columnas */',
        '}',
        '',
        '/* ─── Propiedades de los HIJOS (flex items) ─── */',
        '.flex-item {',
        '  /* flex: [grow] [shrink] [basis] */',
        '  flex: 1;           /* Crece para llenar el espacio disponible */',
        '  flex: 0 0 200px;   /* Tamaño fijo: no crece ni encoge */',
        '  flex: 2;           /* Crece el DOBLE que los items con flex:1 */',
        '',
        '  align-self: center;  /* Anula align-items solo para este item */',
        '  order: -1;           /* Aparece primero visualmente (OJO: afecta accesibilidad) */',
        '}',
    ], s)

    items += sub_header("5.2 Recetas de Flexbox más Usadas", s)

    items += code_block("CSS — flexbox-recetas.css", [
        '/* ─── RECETA 1: Centrar perfectamente (horizontal + vertical) ─── */',
        '.centrado-perfecto {',
        '  display: flex;',
        '  align-items: center;      /* Centra verticalmente */',
        '  justify-content: center;  /* Centra horizontalmente */',
        '  /* También funciona: place-items: center con Grid */',
        '}',
        '',
        '/* ─── RECETA 2: Navbar con logo + links + botón ─── */',
        '.navbar {',
        '  display: flex;',
        '  align-items: center;',
        '  gap: 24px;',
        '}',
        '.navbar-spacer {',
        '  flex: 1;  /* Este div invisible empuja el botón al extremo derecho */',
        '}',
        '',
        '/* ─── RECETA 3: Card con footer siempre abajo ─── */',
        '.card {',
        '  display: flex;',
        '  flex-direction: column;',
        '  height: 100%;             /* La card ocupa todo el alto disponible */',
        '}',
        '.card-body {',
        '  flex: 1;                  /* Se estira para ocupar el espacio */',
        '}',
        '.card-footer {',
        '  margin-top: auto;         /* Se empuja automáticamente al final */',
        '}',
        '',
        '/* ─── RECETA 4: Grid de pills/tags que se envuelven ─── */',
        '.tags {',
        '  display: flex;',
        '  flex-wrap: wrap;          /* Los tags se van a la siguiente línea */',
        '  gap: 8px;                 /* Espacio entre tags */',
        '}',
        '',
        '/* ─── RECETA 5: Layout sidebar + contenido ─── */',
        '.layout {',
        '  display: flex;',
        '  gap: 32px;',
        '}',
        '.sidebar { width: 260px; flex-shrink: 0; }  /* No encoge */',
        '.contenido { flex: 1; }  /* Ocupa el resto */',
    ], s)

    items += tip("Truco para recordar los ejes de Flexbox",
        "Imagina una flecha. En flex-direction:row, la flecha apunta → (horizontal). "
        "justify-content mueve los items EN la dirección de la flecha. "
        "align-items los mueve PERPENDICULAR a la flecha (vertical en este caso).", s)

    # Ejercicios
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 5 ──", s['h4']))
    items.append(spacer(6))

    items += exercise_block(13, "Fácil", "Tu primera barra de navegación con Flexbox",
        ["Crea un header con class='navbar'",
         "Dentro: un a con tu nombre (logo) y un nav con 3 links",
         "CSS: .navbar { display:flex; align-items:center; padding:16px 32px; }",
         "Agrega entre el logo y el nav un div con class='spacer' y flex:1",
         "El spacer empujará el nav al extremo derecho — ¡como una navbar real!"], s)

    items += exercise_block(14, "Medio", "Grid de cards responsive",
        ["Crea un div con class='cards-grid'",
         "Dentro pon 6 divs con class='card', cada uno con título y descripción",
         "CSS: .cards-grid { display:flex; flex-wrap:wrap; gap:20px; }",
         "CSS: .card { flex: 1 1 280px; } — se adapta al espacio disponible",
         "Redimensiona la ventana y observa cómo las cards se reorganizan"], s)

    items += exercise_block(15, "Difícil", "Sección hero con Flexbox",
        ["Crea una section con class='hero' de min-height:100vh",
         "Dentro: un div con texto (h1, p, botón) y uno con imagen",
         "Usando flexbox, el texto va a la izquierda y la imagen a la derecha",
         "En pantallas pequeñas (max-width:768px), cambia a flex-direction:column",
         "Centra perfectamente el contenido vertical y horizontalmente"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 6: CSS Grid
# ─────────────────────────────────────────
def chapter_6(s):
    items = []
    items += section_header("CAPÍTULO 06", "CSS Grid\nLayouts Bidimensionales", s)

    items.append(Paragraph(
        "CSS Grid es el sistema más poderoso para crear layouts. "
        "Mientras Flexbox trabaja en una sola dirección (fila O columna), "
        "Grid trabaja en AMBAS (filas Y columnas simultáneamente). "
        "Es perfecto para el layout general de la página.", s['lead']))

    items += sub_header("6.1 Fundamentos de CSS Grid", s)

    items += code_block("CSS — grid-base.css", [
        '/* ─── El contenedor padre define la cuadrícula ─── */',
        '.grid {',
        '  display: grid;  /* ✨ Activa Grid para los HIJOS DIRECTOS */',
        '',
        '  /* ── Definir columnas ── */',
        '  grid-template-columns: 200px 200px 200px;  /* 3 columnas de 200px */',
        '  grid-template-columns: 1fr 2fr 1fr;         /* Ratio 1:2:1 (fr = fracción) */',
        '  grid-template-columns: repeat(3, 1fr);      /* 3 columnas iguales */',
        '  grid-template-columns: repeat(4, minmax(200px, 1fr));  /* Responsive! */',
        '',
        '  /* ── Definir filas ── */',
        '  grid-template-rows: auto 1fr auto;  /* Header | Main (crece) | Footer */',
        '',
        '  /* ── Espacio entre celdas ── */',
        '  gap: 24px;           /* Entre filas Y columnas */',
        '  row-gap: 32px;       /* Solo entre filas */',
        '  column-gap: 16px;    /* Solo entre columnas */',
        '',
        '  /* ── Alineación de todos los items ── */',
        '  justify-items: center;  /* Centra items en su celda (horizontal) */',
        '  align-items: center;    /* Centra items en su celda (vertical) */',
        '  place-items: center;    /* Shorthand: centra en ambos ejes */',
        '}',
        '',
        '/* ─── Posicionar items en la cuadrícula ─── */',
        '.item-especial {',
        '  /* Por líneas numéricas: línea-inicio / línea-fin */',
        '  grid-column: 1 / 3;   /* Desde la línea 1 hasta la 3 (ocupa 2 celdas) */',
        '  grid-column: 1 / -1;  /* Desde el inicio hasta el FIN (toda la fila) */',
        '  grid-column: span 2;  /* Ocupa 2 columnas desde donde esté */',
        '  grid-row: 1 / 3;      /* Ocupa 2 filas */',
        '}',
    ], s)

    items += sub_header("6.2 Grid Areas: Nombrar Zonas del Layout", s)
    items.append(Paragraph(
        "grid-template-areas es la joya de Grid. "
        "Puedes 'dibujar' tu layout con texto y asignar elementos a zonas nombradas:", s['body']))

    items += code_block("CSS — grid-areas.css (layout de página completa)", [
        '/* Layout: header arriba, sidebar + main en el centro, footer abajo */',
        '',
        '.pagina {',
        '  display: grid;',
        '  grid-template-areas:     /* "Dibujas" el layout con texto */',
        '    "header  header  header"  /* Fila 1: header ocupa las 3 columnas */',
        '    "sidebar main    main"    /* Fila 2: sidebar + main (main ocupa 2) */',
        '    "footer  footer  footer"; /* Fila 3: footer ocupa las 3 columnas */',
        '  grid-template-columns: 260px 1fr 1fr;  /* sidebar fijo + main flexible */',
        '  grid-template-rows: auto 1fr auto;      /* header auto + main crece + footer */',
        '  min-height: 100vh;  /* La página siempre ocupa toda la pantalla */',
        '}',
        '',
        '/* Asigna cada elemento a su área */',
        '.header  { grid-area: header;  }',
        '.sidebar { grid-area: sidebar; }',
        '.main    { grid-area: main;    }',
        '.footer  { grid-area: footer;  }',
        '',
        '/* En móvil: todo en una columna */',
        '@media (max-width: 768px) {',
        '  .pagina {',
        '    grid-template-areas:',
        '      "header"   /* Fila 1 */',
        '      "main"     /* Fila 2 (el main va antes del sidebar en móvil) */',
        '      "sidebar"  /* Fila 3 */',
        '      "footer";  /* Fila 4 */',
        '    grid-template-columns: 1fr;  /* Una sola columna */',
        '  }',
        '}',
    ], s)

    items += sub_header("6.3 Grid Responsive con auto-fill y auto-fit", s)
    items.append(Paragraph(
        "La combinación de <b>repeat(auto-fill, minmax())</b> crea grids "
        "que se adaptan solos sin media queries:", s['body']))

    items += code_block("CSS — grid-responsive.css", [
        '/* ─── auto-fill: Responsive SIN media queries ─── */',
        '.galeria {',
        '  display: grid;',
        '  /*           auto-fill: llena con todas las columnas que quepan */',
        '  /*           minmax(280px, 1fr): mínimo 280px, máximo 1 fracción */',
        '  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));',
        '  gap: 24px;',
        '}',
        '/* En pantalla grande: 4 columnas. En tablet: 2. En móvil: 1. */',
        '/* ¡Todo automáticamente! */',
        '',
        '/* Diferencia entre auto-fill y auto-fit: */',
        '/* auto-fill: mantiene celdas vacías al final */',
        '/* auto-fit: colapsa celdas vacías y estira las existentes */',
        '/* Para galerías: auto-fill. Para que 1 item ocupe todo: auto-fit */',
    ], s)

    # Ejercicios
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 6 ──", s['h4']))
    items.append(spacer(6))

    items += exercise_block(16, "Fácil", "Tu primera cuadrícula",
        ["Crea un div con class='grid-3-columnas'",
         "Dentro pon 6 divs con números del 1 al 6",
         "CSS: display:grid; grid-template-columns:repeat(3,1fr); gap:16px;",
         "Dale a cada div: background:#f0f0f0; padding:20px; text-align:center",
         "Observa cómo se organizan automáticamente en 3 columnas"], s)

    items += exercise_block(17, "Medio", "Layout de página con grid-template-areas",
        ["Crea la estructura: header, aside (sidebar), main, footer",
         "Usa grid-template-areas para el layout",
         "sidebar: 250px de ancho, main ocupa el resto, header y footer full width",
         "Dale colores diferentes a cada área para verlas claramente",
         "min-height: 100vh para que ocupe toda la pantalla"], s)

    items += exercise_block(18, "Difícil", "Galería responsive de proyectos",
        ["Crea una sección de proyectos con 6 cards",
         "Usa repeat(auto-fill, minmax(300px, 1fr)) para el grid",
         "Haz que el primer proyecto ocupe 2 columnas: grid-column: span 2",
         "Haz que si el viewport es menor a 640px, todos ocupen 1 columna",
         "Bonus: usa grid-row: span 2 en el primer proyecto para que sea más alto"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 7: Design Tokens
# ─────────────────────────────────────────
def chapter_7(s):
    items = []
    items += section_header("CAPÍTULO 07", "Design Tokens & Variables CSS\nEl Corazón de tu Sistema", s)

    items.append(Paragraph(
        "Los Design Tokens son los valores de diseño de tu proyecto: colores, "
        "tamaños, espaciados, fuentes. Guardarlos como variables CSS hace que "
        "cambiar el tema completo de tu sitio sea cuestión de editar un solo archivo.", s['lead']))

    items += sub_header("7.1 CSS Custom Properties (Variables CSS)", s)

    items += code_block("CSS — css/00-tokens.css (tu archivo más importante)", [
        '/*',
        '  tokens.css — EL ARCHIVO MÁS IMPORTANTE DEL PROYECTO',
        '  Aquí defines TODO: colores, espaciados, fuentes, radios, sombras.',
        '  Si quieres cambiar el tema, solo editas ESTE archivo.',
        '*/',
        '',
        ':root {  /* :root equivale a html pero con mayor especificidad */',
        '',
        '  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */',
        '  /*   NIVEL 1: PRIMITIVOS (valores crudos)     */',
        '  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */',
        '',
        '  /* Colores (usando oklch para mayor control) */',
        '  --color-brand-400: oklch(65% 0.20 145);  /* verde brillante */',
        '  --color-brand-500: oklch(55% 0.22 145);  /* verde principal */',
        '  --color-brand-600: oklch(45% 0.18 145);  /* verde oscuro */',
        '  --color-gray-50:   oklch(97% 0 0);       /* casi blanco */',
        '  --color-gray-500:  oklch(52% 0 0);       /* gris medio */',
        '  --color-gray-950:  oklch(12% 0 0);       /* casi negro */',
        '',
        '  /* Escala tipográfica (Major Third x1.25) */',
        '  --size-xs:   0.64rem;   /* 10.2px */',
        '  --size-sm:   0.8rem;    /* 12.8px */',
        '  --size-base: 1rem;      /* 16px   */',
        '  --size-lg:   1.25rem;   /* 20px   */',
        '  --size-xl:   1.563rem;  /* 25px   */',
        '  --size-2xl:  1.953rem;  /* 31px   */',
        '  --size-3xl:  2.441rem;  /* 39px   */',
        '  --size-4xl:  3.052rem;  /* 49px   */',
        '',
        '  /* Escala de espaciado (base 4px) */',
        '  --space-1:  0.25rem;  /* 4px  */',
        '  --space-2:  0.5rem;   /* 8px  */',
        '  --space-3:  0.75rem;  /* 12px */',
        '  --space-4:  1rem;     /* 16px */',
        '  --space-6:  1.5rem;   /* 24px */',
        '  --space-8:  2rem;     /* 32px */',
        '  --space-12: 3rem;     /* 48px */',
        '  --space-16: 4rem;     /* 64px */',
        '',
        '  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */',
        '  /*   NIVEL 2: SEMÁNTICOS (significado de negocio)   */',
        '  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */',
        '',
        '  /* Los semánticos REFERENCIAN a los primitivos */',
        '  --color-bg:           var(--color-gray-50);    /* Fondo de la página */',
        '  --color-surface:      white;                   /* Fondo de cards */',
        '  --color-text:         var(--color-gray-950);   /* Texto principal */',
        '  --color-text-muted:   var(--color-gray-500);   /* Texto secundario */',
        '  --color-accent:       var(--color-brand-500);  /* Color principal */',
        '  --color-accent-hover: var(--color-brand-600);  /* Hover del acento */',
        '  --color-border:       oklch(88% 0 0);          /* Bordes */',
        '',
        '  /* Estados del sistema */',
        '  --color-success: oklch(55% 0.18 145);  /* Verde éxito */',
        '  --color-warning: oklch(70% 0.18 70);   /* Amarillo advertencia */',
        '  --color-danger:  oklch(58% 0.22 25);   /* Rojo error */',
        '  --color-info:    oklch(60% 0.18 220);  /* Azul informacion */',
        '',
        '  /* Radios de borde */',
        '  --radius-sm:   4px;',
        '  --radius-md:   8px;',
        '  --radius-lg:   16px;',
        '  --radius-xl:   24px;',
        '  --radius-full: 9999px;  /* Círculo/pill */',
        '',
        '  /* Sombras */',
        '  --shadow-sm: 0 1px 4px oklch(0% 0 0 / 8%);',
        '  --shadow-md: 0 4px 16px oklch(0% 0 0 / 10%);',
        '  --shadow-lg: 0 8px 32px oklch(0% 0 0 / 14%);',
        '',
        '  /* Fuentes */',
        '  --font-body:    "Syne", system-ui, sans-serif;',
        '  --font-heading: "Fraunces", Georgia, serif;',
        '  --font-mono:    "JetBrains Mono", "Courier New", monospace;',
        '',
        '  /* Transiciones */',
        '  --duration-fast:   100ms;',
        '  --duration-normal: 200ms;',
        '  --duration-slow:   350ms;',
        '  --ease-out:        cubic-bezier(0.16, 1, 0.3, 1);',
        '}',
    ], s)

    items += sub_header("7.2 Cómo Usar las Variables", s)

    items += code_block("CSS — usando-variables.css", [
        '/* En vez de escribir valores hardcodeados (MALO): */',
        '.btn-malo {',
        '  background: #16a34a;   /* ❌ Si cambias el brand color, debes buscar */',
        '  color: white;          /*    y reemplazar en TODOS los archivos */',
        '  padding: 12px 24px;    /* ❌ Valores arbitrarios — ¿por qué 12 y 24? */',
        '  border-radius: 8px;',
        '}',
        '',
        '/* Usa variables (BUENO): */',
        '.btn-bueno {',
        '  background: var(--color-accent);       /* ✅ Cambia el token = cambia todo */',
        '  color: white;',
        '  padding: var(--space-3) var(--space-6); /* ✅ De la escala de espaciado */',
        '  border-radius: var(--radius-md);        /* ✅ Del sistema de radios */',
        '  font-family: var(--font-body);          /* ✅ Del sistema de fuentes */',
        '  transition: background var(--duration-normal) ease;  /* ✅ */',
        '}',
        '',
        '/* color-mix: crea variantes sin definir nuevas variables */',
        '.btn-hover {',
        '  /* Mezcla el color accent con negro al 12% */',
        '  background: color-mix(in oklch, var(--color-accent), black 12%);',
        '}',
        '',
        '.overlay {',
        '  /* Mezcla el color accent con transparente al 85% (muy translúcido) */',
        '  background: color-mix(in srgb, var(--color-accent), transparent 85%);',
        '}',
    ], s)

    # Ejercicios
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 7 ──", s['h4']))

    items += exercise_block(19, "Fácil", "Crea tu archivo de tokens",
        ["Crea css/00-tokens.css en tu proyecto",
         "Define al menos: 3 colores de marca, 2 colores de estado (success, danger)",
         "Define: 6 valores de espaciado (space-1 a space-12)",
         "Define: 4 radios de borde (sm, md, lg, full)",
         "Importa este archivo primero en tu main.css"], s)

    items += exercise_block(20, "Medio", "Refactoriza tu CSS con variables",
        ["Revisa tu CSS actual y encuentra todos los valores hardcodeados",
         "Reemplaza colores (#333, #0070f3) por variables (var(--color-text))",
         "Reemplaza tamaños (16px, 24px) por variables de espaciado",
         "Reemplaza border-radius por variables de radio",
         "Verifica que el diseño siga igual"], s)

    items += exercise_block(21, "Difícil", "Cambia el tema completo con 3 líneas",
        ["Tu portfolio tiene tokens definidos",
         "Crea una variante oscura cambiando SOLO los tokens semánticos en :root",
         "Cambia: --color-bg a #0d0d0d, --color-text a #f0f0f0, --color-surface a #1a1a1a",
         "¿Todo el sitio cambió al tema oscuro? Eso es el poder de los tokens",
         "En el siguiente capítulo haremos esto automático con dark mode"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 8: Componentes Base
# ─────────────────────────────────────────
def chapter_8(s):
    items = []
    items += section_header("CAPÍTULO 08", "Componentes Base\nBotones, Badges y Alertas", s)

    items.append(Paragraph(
        "Los componentes base son los átomos de tu sistema de diseño. "
        "Bien construidos una vez, los reutilizas cientos de veces. "
        "La clave: HTML semántico, CSS con BEM, y accesibilidad desde el inicio.", s['lead']))

    items += sub_header("8.1 Sistema de Botones Completo", s)

    items += code_block("HTML — botones-accesibles.html", [
        '<!-- ✅ Usa <button> para ACCIONES (no divs ni spans) -->',
        '<!-- <button> tiene focus, Enter y Space por teclado gratis -->',
        '',
        '<!-- Botón principal -->',
        '<button type="button" class="btn btn--primary">',
        '  Guardar cambios',
        '</button>',
        '',
        '<!-- Botón con ícono (accesible) -->',
        '<button type="button" class="btn btn--secondary">',
        '  <!-- El SVG es decorativo: aria-hidden lo oculta del lector de pantalla -->',
        '  <svg aria-hidden="true" focusable="false" width="16" height="16">',
        '    <path d="..."/>',
        '  </svg>',
        '  Descargar CV',
        '</button>',
        '',
        '<!-- Botón ícono solo: NECESITA aria-label -->',
        '<button type="button" class="btn btn--icon" aria-label="Compartir en Twitter">',
        '  <svg aria-hidden="true">...</svg>',
        '</button>',
        '',
        '<!-- Botón deshabilitado: usa disabled, NO solo CSS -->',
        '<button type="button" class="btn btn--primary" disabled>',
        '  Procesando...  <!-- El disabled lo hace no clickeable y lo anuncia -->',
        '</button>',
        '',
        '<!-- ✅ Usa <a> para NAVEGACIÓN (no buttons) -->',
        '<a href="/proyectos" class="btn btn--outline">Ver proyectos</a>',
    ], s)

    items += code_block("CSS — components/button.css", [
        '@layer components {',
        '',
        '  /* ── Base: todos los botones heredan esto ── */',
        '  .btn {',
        '    display: inline-flex;',
        '    align-items: center;',
        '    justify-content: center;',
        '    gap: var(--space-2);            /* Espacio entre ícono y texto */',
        '    padding: var(--space-3) var(--space-6); /* 12px arriba/abajo, 24px lados */',
        '    border-radius: var(--radius-md);',
        '    font-family: var(--font-body);',
        '    font-size: var(--size-sm);      /* 0.875rem = 14px */',
        '    font-weight: 600;',
        '    line-height: 1;',
        '    white-space: nowrap;            /* El texto no se parte en dos líneas */',
        '    cursor: pointer;',
        '    border: 1.5px solid transparent;',
        '    text-decoration: none;          /* Para el caso de <a class="btn"> */',
        '    user-select: none;              /* No se puede seleccionar el texto */',
        '',
        '    /* WCAG 2.5.5: área mínima de toque 44x44px */',
        '    min-height: 44px;',
        '    min-width: 44px;',
        '',
        '    /* Transiciones solo en propiedades baratas (no layout) */',
        '    transition:',
        '      background-color var(--duration-normal) ease,',
        '      border-color var(--duration-normal) ease,',
        '      color var(--duration-normal) ease,',
        '      transform var(--duration-fast) ease,',
        '      box-shadow var(--duration-normal) ease;',
        '  }',
        '',
        '  /* Focus visible: NUNCA quites outline sin reemplazarlo */',
        '  .btn:focus-visible {',
        '    outline: 2px solid var(--color-accent);',
        '    outline-offset: 3px;',
        '  }',
        '',
        '  /* Feedback de clic (solo propiedades de composición = rápido) */',
        '  .btn:not(:disabled):active {',
        '    transform: scale(0.97);',
        '  }',
        '',
        '  /* Estado deshabilitado */',
        '  .btn:disabled, .btn[aria-disabled="true"] {',
        '    opacity: 0.4;',
        '    cursor: not-allowed;',
        '    pointer-events: none; /* No activa hover ni click */',
        '  }',
        '',
        '  /* ── Variantes ── */',
        '  .btn--primary {',
        '    background: var(--color-accent);',
        '    color: white;',
        '    border-color: var(--color-accent);',
        '  }',
        '  .btn--primary:hover:not(:disabled) {',
        '    background: var(--color-accent-hover);',
        '    transform: translateY(-1px); /* Efecto de elevación */',
        '    box-shadow: 0 8px 24px color-mix(in srgb, var(--color-accent), transparent 60%);',
        '  }',
        '',
        '  .btn--secondary {',
        '    background: transparent;',
        '    color: var(--color-text);',
        '    border-color: var(--color-border);',
        '  }',
        '  .btn--secondary:hover:not(:disabled) {',
        '    border-color: var(--color-accent);',
        '    color: var(--color-accent);',
        '  }',
        '',
        '  .btn--danger {',
        '    background: color-mix(in srgb, var(--color-danger), transparent 88%);',
        '    color: var(--color-danger);',
        '    border-color: color-mix(in srgb, var(--color-danger), transparent 75%);',
        '  }',
        '  .btn--danger:hover:not(:disabled) {',
        '    background: var(--color-danger);',
        '    color: white;',
        '  }',
        '',
        '  /* ── Tamaños ── */',
        '  .btn--sm { padding: var(--space-2) var(--space-4); font-size: var(--size-xs); min-height: 36px; }',
        '  .btn--lg { padding: var(--space-4) var(--space-8); font-size: var(--size-base); min-height: 52px; }',
        '',
        '  /* ── Modificadores ── */',
        '  .btn--full   { width: 100%; }',
        '  .btn--rounded{ border-radius: var(--radius-full); }',
        '  .btn--icon   { padding: var(--space-3); aspect-ratio: 1; }',
        '',
        '  /* ── Loading state ── */',
        '  .btn--loading { pointer-events: none; }',
        '  .btn--loading::after {',
        '    content: "";',
        '    width: 14px; height: 14px;',
        '    border: 2px solid transparent;',
        '    border-top-color: currentColor;',
        '    border-radius: 50%;',
        '    animation: spin 0.7s linear infinite;',
        '  }',
        '  @keyframes spin { to { transform: rotate(360deg); } }',
        '',
        '}',
    ], s)

    items += sub_header("8.2 Badges y Tags", s)

    items += code_block("CSS — components/badge.css", [
        '@layer components {',
        '',
        '  .badge {',
        '    display: inline-flex;',
        '    align-items: center;',
        '    gap: 5px;',
        '    padding: 0.2em 0.65em;   /* em: el padding escala con la fuente */',
        '    border-radius: var(--radius-full);',
        '    font-size: 0.7em;        /* 70% de la fuente del contexto */',
        '    font-weight: 500;',
        '    white-space: nowrap;',
        '    border: 1px solid transparent;',
        '    vertical-align: middle;  /* Se alinea con el texto adyacente */',
        '  }',
        '',
        '  /* Punto de estado dentro del badge */',
        '  .badge__dot {',
        '    width: 6px; height: 6px;',
        '    border-radius: 50%;',
        '    background: currentColor; /* Hereda el color del badge */',
        '    flex-shrink: 0;           /* No se encoge si el espacio es limitado */',
        '  }',
        '',
        '  /* Variantes con color-mix: más mantenible que valores hardcodeados */',
        '  .badge--success {',
        '    color: var(--color-success);',
        '    background: color-mix(in srgb, var(--color-success), transparent 88%);',
        '    border-color: color-mix(in srgb, var(--color-success), transparent 75%);',
        '  }',
        '  .badge--warning {',
        '    color: var(--color-warning);',
        '    background: color-mix(in srgb, var(--color-warning), transparent 88%);',
        '    border-color: color-mix(in srgb, var(--color-warning), transparent 75%);',
        '  }',
        '  .badge--danger {',
        '    color: var(--color-danger);',
        '    background: color-mix(in srgb, var(--color-danger), transparent 88%);',
        '    border-color: color-mix(in srgb, var(--color-danger), transparent 75%);',
        '  }',
        '',
        '  /* Badge contador (número sobre un ícono) */',
        '  .badge-host   { position: relative; display: inline-flex; }',
        '  .badge--counter {',
        '    position: absolute;',
        '    top: -4px; right: -4px;',
        '    min-width: 18px; height: 18px;',
        '    padding: 0 4px;',
        '    background: var(--color-danger);',
        '    color: white;',
        '    border: 2px solid var(--color-surface); /* Separa del fondo */',
        '    border-radius: var(--radius-full);',
        '    font-size: 0.6rem; font-weight: 700;',
        '    display: flex; align-items: center; justify-content: center;',
        '  }',
        '',
        '}',
    ], s)

    # Ejercicios
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 8 ──", s['h4']))

    items += exercise_block(22, "Fácil", "Implementa los botones en tu portfolio",
        ["Crea css/components/button.css con el código del capítulo",
         "Impórtalo en main.css dentro de @layer components",
         "En index.html agrega: un btn--primary 'Ver Proyectos', un btn--secondary 'Descargar CV'",
         "Verifica que funcionen con Tab (foco visible) y Enter"], s)

    items += exercise_block(23, "Medio", "Badges de tecnologías",
        ["En la sección de proyectos, agrega badges para las tecnologías",
         "Ej: <span class='badge badge--info'>React</span>",
         "Crea variantes de color para cada tipo de tecnología",
         "Agrúpalos en un div con display:flex; flex-wrap:wrap; gap:8px"], s)

    items += exercise_block(24, "Difícil", "Botón con estado de carga",
        ["Crea un botón 'Enviar mensaje' en tu formulario",
         "Al hacer clic, con JavaScript agrega la clase btn--loading",
         "El botón debe mostrar el spinner y deshabilitar el clic",
         "Después de 2 segundos, quita la clase y cambia el texto a 'Enviado ✓'",
         "Asegúrate de manejar aria-busy='true' durante la carga"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 9: Formularios
# ─────────────────────────────────────────
def chapter_9(s):
    items = []
    items += section_header("CAPÍTULO 09", "Componentes de Formulario\nLa Interfaz que más Importa", s)

    items.append(Paragraph(
        "Los formularios son donde el usuario ACTÚA. Un formulario confuso "
        "hace que el usuario abandone. Uno claro y accesible convierte. "
        "La diferencia está en los detalles: labels correctos, errores claros, "
        "validación amable.", s['lead']))

    items += sub_header("9.1 Anatomía de un Campo Perfecto", s)

    items += code_block("HTML — campo-perfecto.html", [
        '<!-- Un campo bien construido tiene 4 partes: */',
        '<!-- 1. Label vinculado, 2. Input semántico, 3. Hint, 4. Error -->',
        '',
        '<div class="field">',
        '',
        '  <!-- LABEL: siempre vinculado con for/id -->',
        '  <!-- El * de requerido está oculto para el lector (aria-hidden) -->',
        '  <label class="field__label" for="email">',
        '    Email',
        '    <span aria-hidden="true"> *</span>',
        '  </label>',
        '',
        '  <!-- INPUT: tipo correcto para mejor UX en móvil -->',
        '  <input',
        '    class="field__input"',
        '    type="email"                 <!-- Teclado con @ en móvil -->',
        '    id="email"                   <!-- Vincula con el label -->',
        '    name="email"                 <!-- Para envío de formulario -->',
        '    autocomplete="email"         <!-- Autocompletado del navegador -->',
        '    required                     <!-- Requerido nativo -->',
        '    aria-required="true"         <!-- Requerido para lectores de pantalla -->',
        '    aria-describedby="email-hint email-error"  <!-- Vincula hint y error -->',
        '    aria-invalid="false"         <!-- Se cambia a "true" si hay error -->',
        '    placeholder="tu@email.com"   <!-- Ejemplo de formato -->',
        '  >',
        '',
        '  <!-- HINT: ayuda preventiva, siempre visible -->',
        '  <p class="field__hint" id="email-hint">',
        '    Te contactaremos a este email. No compartimos tu información.',
        '  </p>',
        '',
        '  <!-- ERROR: aparece solo si hay error (role="alert" lo anuncia) -->',
        '  <p class="field__error" id="email-error" role="alert" hidden>',
        '    <!-- El texto se pone aquí con JavaScript cuando hay error -->',
        '  </p>',
        '',
        '</div>',
    ], s)

    items += code_block("CSS — components/form.css", [
        '@layer components {',
        '',
        '  /* Grupo de campo: organiza label + input + hint + error */',
        '  .field {',
        '    display: flex;',
        '    flex-direction: column;',
        '    gap: 0.375rem;  /* 6px entre cada parte */',
        '  }',
        '',
        '  .field__label {',
        '    font-size: var(--size-sm);',
        '    font-weight: 600;',
        '    color: var(--color-text);',
        '  }',
        '',
        '  /* El input, select y textarea comparten estilos base */',
        '  .field__input {',
        '    width: 100%;',
        '    padding: 0.625rem 0.875rem;  /* 10px arriba/abajo, 14px lados */',
        '    background: var(--color-bg);',
        '    border: 1.5px solid var(--color-border);',
        '    border-radius: var(--radius-md);',
        '    font-size: var(--size-base);  /* 16px: evita zoom en iOS */',
        '    font-family: inherit;         /* Hereda la fuente del proyecto */',
        '    color: var(--color-text);',
        '    min-height: 44px;             /* WCAG: área mínima */',
        '    outline: none;                /* Quitamos el outline nativo... */',
        '    transition:',
        '      border-color var(--duration-fast) ease,',
        '      box-shadow var(--duration-fast) ease;',
        '  }',
        '',
        '  /* Placeholder: más claro que el texto real */',
        '  .field__input::placeholder {',
        '    color: var(--color-text-muted);',
        '    opacity: 0.5;',
        '  }',
        '',
        '  /* Hover: señal de que es interactivo */',
        '  .field__input:hover:not(:focus) {',
        '    border-color: color-mix(in oklch, var(--color-border), var(--color-accent) 30%);',
        '  }',
        '',
        '  /* Focus: ...y ponemos el nuestro, más bonito y accesible */',
        '  .field__input:focus {',
        '    border-color: var(--color-accent);',
        '    box-shadow: 0 0 0 3px color-mix(in srgb, var(--color-accent), transparent 80%);',
        '  }',
        '',
        '  /* :user-invalid: SOLO muestra el error tras interacción del usuario */',
        '  /* (no al cargar la página como hace :invalid) */',
        '  .field__input:user-invalid,',
        '  .field__input[aria-invalid="true"] {',
        '    border-color: var(--color-danger);',
        '  }',
        '  .field__input:user-invalid:focus {',
        '    box-shadow: 0 0 0 3px color-mix(in srgb, var(--color-danger), transparent 80%);',
        '  }',
        '',
        '  /* :user-valid: muestra verde solo cuando el usuario completó el campo */',
        '  .field__input:user-valid:not(:placeholder-shown) {',
        '    border-color: var(--color-success);',
        '  }',
        '',
        '  .field__hint {',
        '    font-size: var(--size-xs);',
        '    color: var(--color-text-muted);',
        '    line-height: 1.4;',
        '  }',
        '',
        '  .field__error {',
        '    font-size: var(--size-xs);',
        '    color: var(--color-danger);',
        '    display: flex;',
        '    align-items: center;',
        '    gap: 4px;',
        '  }',
        '  .field__error::before { content: "⚠"; }  /* Ícono visual del error */',
        '',
        '}',
    ], s)

    # Ejercicios
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 9 ──", s['h4']))

    items += exercise_block(25, "Fácil", "Formulario de contacto básico",
        ["Crea contacto.html con un formulario",
         "Agrega campos: nombre (text), email (email), mensaje (textarea)",
         "Cada campo debe tener label vinculado con for/id",
         "El email y nombre deben ser required",
         "Agrega un botón submit con class='btn btn--primary btn--full'"], s)

    items += exercise_block(26, "Medio", "Valida con :user-invalid",
        ["Agrega el CSS de validación del capítulo a tus campos",
         "Pon minlength='2' en el campo nombre",
         "Prueba: intenta enviar con email incorrecto — ¿aparece el borde rojo?",
         "Agrega un hint visible debajo de cada campo",
         "Bonus: cuando el campo sea válido, muestra borde verde con :user-valid"], s)

    items += exercise_block(27, "Difícil", "Validación completa con JavaScript",
        ["Al hacer submit, prevén el envío por defecto con event.preventDefault()",
         "Valida: nombre mínimo 2 chars, email con regex, mensaje mínimo 10 chars",
         "Si hay error: pon aria-invalid='true' en el input y muestra el .field__error",
         "Si es válido: agrega la clase btn--loading al botón, simula envío 2 segundos",
         "Después muestra una alerta de éxito (.alert--success) y resetea el formulario"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULO 10: Cards y Listas
# ─────────────────────────────────────────
def chapter_10(s):
    items = []
    items += section_header("CAPÍTULO 10", "Cards y Listas\nPatrones de Contenido", s)

    items.append(Paragraph(
        "Las cards son el patrón de UI más versátil. "
        "Sirven para proyectos, posts, usuarios, productos — cualquier cosa que "
        "agrupa información relacionada en un contenedor visual.", s['lead']))

    items += sub_header("10.1 Sistema de Cards", s)

    items += code_block("HTML — card-completa.html", [
        '<!-- article: semántico para contenido autónomo (un proyecto, post, etc.) -->',
        '<article class="card card--interactive" aria-label="Proyecto: App del Clima">',
        '',
        '  <!-- Media: imagen del proyecto -->',
        '  <div class="card__media">',
        '    <picture>',
        '      <!-- Formato moderno WebP primero, JPEG como fallback -->',
        '      <source type="image/webp" srcset="proyecto.webp">',
        '      <img',
        '        src="proyecto.jpg"',
        '        alt="Captura de pantalla de la app del clima mostrando temperatura"',
        '        width="400" height="225"  <!-- Evita Layout Shift (CLS) -->',
        '        loading="lazy"            <!-- No carga hasta que el usuario llegue -->',
        '      >',
        '    </picture>',
        '    <!-- Badge sobre la imagen -->',
        '    <span class="card__badge badge badge--success">Completado</span>',
        '  </div>',
        '',
        '  <!-- Cuerpo de la card -->',
        '  <div class="card__body">',
        '    <!-- Header interno: categoría + título -->',
        '    <header class="card__header">',
        '      <span class="card__category">API REST</span>',
        '      <h3 class="card__title">App del Clima</h3>',
        '    </header>',
        '',
        '    <p class="card__description">',
        '      Aplicación del tiempo con datos en tiempo real de OpenWeather API.',
        '    </p>',
        '',
        '    <!-- Tags de tecnologías -->',
        '    <div class="card__tags">',
        '      <span class="badge badge--info">JavaScript</span>',
        '      <span class="badge badge--info">CSS Grid</span>',
        '      <span class="badge badge--info">API REST</span>',
        '    </div>',
        '  </div>',
        '',
        '  <!-- Footer de la card: acciones -->',
        '  <footer class="card__footer">',
        '    <a href="/proyecto/clima" class="btn btn--primary btn--sm">Ver proyecto</a>',
        '    <a href="https://github.com/..." class="btn btn--ghost btn--sm"',
        '       target="_blank" rel="noopener noreferrer">GitHub</a>',
        '  </footer>',
        '',
        '</article>',
    ], s)

    items += code_block("CSS — components/card.css", [
        '@layer components {',
        '',
        '  .card {',
        '    display: flex;',
        '    flex-direction: column;  /* Contenido se apila verticalmente */',
        '    background: var(--color-surface);',
        '    border: 1px solid var(--color-border);',
        '    border-radius: var(--radius-lg);',
        '    overflow: hidden;        /* El hover de la imagen no se sale */',
        '    isolation: isolate;      /* Contexto de apilado propio (z-index local) */',
        '  }',
        '',
        '  /* Media: imagen del proyecto */',
        '  .card__media {',
        '    position: relative;     /* Para posicionar el badge */',
        '    aspect-ratio: 16 / 9;  /* Proporción fija: previene Layout Shift */',
        '    overflow: hidden;',
        '    background: var(--color-surface-2);  /* Placeholder mientras carga */',
        '  }',
        '',
        '  .card__media img {',
        '    width: 100%; height: 100%;',
        '    object-fit: cover;       /* Llena el espacio sin deformar */',
        '    transition: transform var(--duration-slow) ease;',
        '  }',
        '',
        '  .card__badge {',
        '    position: absolute;',
        '    top: 12px; left: 12px;',
        '  }',
        '',
        '  /* El body ocupa todo el espacio disponible (sticky footer) */',
        '  .card__body {',
        '    padding: var(--space-6);',
        '    flex: 1;  /* Crece para llenar el espacio — footer siempre abajo */',
        '    display: flex;',
        '    flex-direction: column;',
        '    gap: var(--space-3);',
        '  }',
        '',
        '  .card__category {',
        '    font-size: var(--size-xs);',
        '    font-weight: 600;',
        '    text-transform: uppercase;',
        '    letter-spacing: 0.08em;',
        '    color: var(--color-accent);',
        '  }',
        '',
        '  .card__title {',
        '    font-size: var(--size-lg);',
        '    font-weight: 700;',
        '    line-height: 1.3;',
        '    color: var(--color-text);',
        '    margin: 0;',
        '  }',
        '',
        '  .card__description {',
        '    font-size: var(--size-sm);',
        '    color: var(--color-text-muted);',
        '    line-height: 1.6;',
        '    flex: 1;  /* Empuja el footer de tags y acciones hacia abajo */',
        '  }',
        '',
        '  .card__tags {',
        '    display: flex;',
        '    flex-wrap: wrap;',
        '    gap: var(--space-2);',
        '    margin-top: auto;  /* Siempre al final del body */',
        '  }',
        '',
        '  .card__footer {',
        '    display: flex;',
        '    align-items: center;',
        '    gap: var(--space-3);',
        '    padding: var(--space-4) var(--space-6);',
        '    border-top: 1px solid var(--color-border);',
        '  }',
        '',
        '  /* Variante interactiva: hover effect */',
        '  .card--interactive {',
        '    cursor: pointer;',
        '    transition:',
        '      transform 250ms ease,',
        '      box-shadow 250ms ease,',
        '      border-color 250ms ease;',
        '    text-decoration: none;',
        '    color: inherit;',
        '  }',
        '',
        '  .card--interactive:hover {',
        '    transform: translateY(-4px);',
        '    box-shadow: var(--shadow-xl);',
        '    border-color: var(--color-accent);',
        '  }',
        '',
        '  /* El hover en la card hace zoom en la imagen */',
        '  .card--interactive:hover .card__media img {',
        '    transform: scale(1.04);',
        '  }',
        '',
        '  /* Versión horizontal (landscape) */',
        '  .card--horizontal {',
        '    flex-direction: row;',
        '  }',
        '  .card--horizontal .card__media {',
        '    aspect-ratio: unset;',
        '    width: 200px;',
        '    flex-shrink: 0;  /* No encoge aunque el contenido sea largo */',
        '  }',
        '',
        '}',
    ], s)

    # Ejercicios
    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 10 ──", s['h4']))

    items += exercise_block(28, "Fácil", "Cards de proyectos",
        ["Crea 3 cards para proyectos reales o ficticios",
         "Cada una con: imagen (o placeholder), título, descripción, 2-3 badges",
         "Usa <article> para cada card (contenido autónomo)",
         "Ponlas en un grid: repeat(auto-fill, minmax(300px, 1fr))"], s)

    items += exercise_block(29, "Medio", "Card con hover effect completo",
        ["Implementa .card--interactive en tus cards",
         "Agrega la imagen con aspect-ratio:16/9 y object-fit:cover",
         "Al hacer hover: translateY(-4px) + box-shadow grande",
         "La imagen debe hacer zoom (scale(1.04)) al hacer hover en la card",
         "Verifica que el overflow:hidden de .card__media contenga el zoom"], s)

    items += exercise_block(30, "Difícil", "Filtro de proyectos por tecnología",
        ["Agrega data-tech='react' (o 'css', 'js') a cada card",
         "Crea botones de filtro: Todos, JavaScript, CSS, React",
         "Con JavaScript, al hacer clic en un filtro oculta las cards que no coincidan",
         "Anima la entrada/salida con opacity y transform",
         "Bonus: muestra el número de proyectos visible en cada filtro"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# CAPÍTULOS 11-17 + PROYECTO FINAL (resumidos pero completos)
# ─────────────────────────────────────────
def chapters_11_to_13(s):
    items = []

    # CAP 11: Navegación
    items += section_header("CAPÍTULO 11", "Navegación y Modales\nInterfaces de Flujo", s)
    items.append(Paragraph(
        "La navegación es la hoja de ruta del usuario. Un modal es una pausa necesaria "
        "que requiere atención inmediata. Ambos tienen patrones de accesibilidad específicos "
        "que no se pueden ignorar.", s['lead']))

    items += sub_header("11.1 Navbar Responsive y Accesible", s)
    items += code_block("CSS — components/navbar.css", [
        '.navbar {',
        '  display: flex;',
        '  align-items: center;',
        '  gap: var(--space-8);',
        '  padding: var(--space-4) var(--space-8);',
        '  /* Glassmorphism: fondo semi-transparente con blur */',
        '  background: color-mix(in srgb, var(--color-surface), transparent 10%);',
        '  backdrop-filter: blur(12px);   /* Efecto vidrio esmerilado */',
        '  -webkit-backdrop-filter: blur(12px); /* Safari */',
        '  position: sticky;              /* Se queda fija al hacer scroll */',
        '  top: 0;',
        '  z-index: 100;                  /* Por encima del contenido */',
        '  border-bottom: 1px solid var(--color-border);',
        '}',
        '',
        '/* Link activo: usa aria-current="page" en lugar de clase */',
        '.navbar__link[aria-current="page"] {',
        '  color: var(--color-accent);',
        '  background: color-mix(in srgb, var(--color-accent), transparent 88%);',
        '}',
        '',
        '/* Menú hamburguesa en móvil */',
        '.navbar__toggle {',
        '  display: none;  /* Solo visible en móvil */',
        '}',
        '',
        '@media (max-width: 768px) {',
        '  .navbar__toggle { display: flex; }',
        '  .navbar__nav {',
        '    position: fixed; top: 60px; left: 0; right: 0;',
        '    background: var(--color-surface);',
        '    padding: var(--space-4);',
        '    flex-direction: column;',
        '    border-bottom: 1px solid var(--color-border);',
        '    display: none;  /* Oculto por defecto */',
        '  }',
        '  .navbar__nav.is-open { display: flex; }  /* JS añade esta clase */',
        '}',
    ], s)

    items += sub_header("11.2 Modal con &lt;dialog&gt; Nativo", s)
    items += code_block("HTML + CSS — modal-nativo.html", [
        '<!-- <dialog> nativo: focus trap, Escape, aria-modal GRATIS -->',
        '<dialog class="modal" id="modal-contacto"',
        '        aria-labelledby="modal-titulo" aria-describedby="modal-desc">',
        '  <div class="modal__content">',
        '    <header class="modal__header">',
        '      <h2 class="modal__title" id="modal-titulo">Contáctame</h2>',
        '      <!-- ✅ Cerrar con botón, NO solo con Escape -->',
        '      <button class="modal__close btn btn--ghost btn--icon"',
        '              aria-label="Cerrar diálogo"',
        '              onclick="this.closest(\'dialog\').close()">✕</button>',
        '    </header>',
        '    <div class="modal__body" id="modal-desc">',
        '      <!-- Contenido del modal -->',
        '    </div>',
        '  </div>',
        '</dialog>',
        '',
        '/* CSS del modal */',
        '.modal {',
        '  max-width: min(480px, 90vw);  /* Máximo 480px pero no más del 90% del viewport */',
        '  border: 1px solid var(--color-border);',
        '  border-radius: var(--radius-xl);',
        '  padding: 0;',
        '  background: var(--color-surface);',
        '  box-shadow: var(--shadow-lg);',
        '  animation: modal-in 0.3s var(--ease-out) both;',
        '}',
        '.modal::backdrop {',
        '  background: oklch(0% 0 0 / 55%);',
        '  backdrop-filter: blur(4px);',
        '}',
        '@keyframes modal-in {',
        '  from { opacity: 0; transform: translateY(-20px) scale(0.97); }',
        '  to   { opacity: 1; transform: none; }',
        '}',
        '',
        '/* JavaScript para abrir: */',
        "/* document.getElementById('modal-contacto').showModal(); */",
    ], s)

    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 11 ──", s['h4']))
    items += exercise_block(31, "Fácil", "Navbar con link activo",
        ["Implementa la navbar en todas tus páginas",
         "En cada página, agrega aria-current='page' al link correspondiente",
         "El link activo debe verse diferente visualmente con CSS",
         "Prueba con Tab: ¿puedes navegar la navbar solo con teclado?"], s)
    items += exercise_block(32, "Difícil", "Modal de formulario de contacto",
        ["Crea un botón 'Contáctame' en el hero",
         "Al hacer clic, abre un <dialog> con el formulario de contacto",
         "El modal debe cerrarse con: el botón X, la tecla Escape, clic en el backdrop",
         "Verifica: al cerrar el modal, el foco vuelve al botón que lo abrió"], s)

    items.append(PageBreak())

    # CAP 12: Tipografía
    items += section_header("CAPÍTULO 12", "Tipografía y Espaciado\nEl 95% del Diseño Web", s)
    items.append(Paragraph(
        "El 95% del diseño web es tipografía. Elegir la fuente correcta, "
        "establecer una escala coherente y garantizar legibilidad son las habilidades "
        "que distinguen a un desarrollador frontend de uno excepcional.", s['lead']))

    items += sub_header("12.1 Carga de Fuentes Óptima", s)
    items += code_block("HTML + CSS — tipografia-optima.html", [
        '<!-- En el <head>: preconnect ANTES de cargar la fuente -->,',
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800',
        '           &family=Fraunces:opsz,wght@9..144,300;9..144,600',
        '           &display=swap" rel="stylesheet">',
        '',
        '/* En CSS: define la escala tipográfica con clamp() para fluidez */',
        'body {',
        '  font-family: var(--font-body);',
        '  font-size: 1rem;  /* 16px: base segura — NO bajes de aquí */',
        '  line-height: 1.7; /* Interlineado: 1.5 mínimo, 1.8 máximo para cuerpo */',
        '  text-rendering: optimizeLegibility; /* Kerning y hinting mejorado */',
        '  -webkit-font-smoothing: antialiased; /* Texto más suave en Mac */',
        '}',
        '',
        '/* clamp(mínimo, preferido, máximo): tipografía FLUIDA */',
        'h1 { font-size: clamp(2rem, 5vw + 1rem, 4.5rem); }',
        'h2 { font-size: clamp(1.5rem, 3vw + 0.5rem, 2.5rem); }',
        'h3 { font-size: clamp(1.2rem, 2vw + 0.4rem, 1.75rem); }',
        '',
        '/* Ancho de lectura óptimo: 45-75 caracteres por línea */',
        '.prose p {',
        '  max-width: 65ch;     /* "ch" = ancho del carácter "0" */',
        '  line-height: 1.8;',
        '  text-wrap: pretty;   /* Evita líneas huérfanas/viudas (CSS 2024) */',
        '}',
        '',
        '/* Headings: text-wrap:balance para mejor salto de línea */',
        'h1, h2, h3 {',
        '  text-wrap: balance;  /* CSS 2024: balancea los saltos de línea */',
        '  overflow-wrap: break-word; /* Rompe palabras muy largas */',
        '}',
    ], s)

    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 12 ──", s['h4']))
    items += exercise_block(33, "Medio", "Escala tipográfica completa",
        ["Implementa la escala de tamaños en tu tokens.css",
         "Aplica font-size: clamp() a todos tus headings",
         "Verifica que el texto sea legible en móvil (min 16px en body)",
         "Pon max-width: 65ch en todos tus párrafos de contenido extenso"], s)
    items += exercise_block(34, "Difícil", "Jerarquía tipográfica visual",
        ["Tu portfolio debe tener al menos 4 niveles tipográficos visualmente distintos",
         "Define: display (hero), heading (secciones), subheading, body, caption",
         "Usa font-weight, letter-spacing y color para diferenciarlos",
         "Sin cambiar el tamaño de fuente, ¿puedes crear jerarquía solo con peso y color?"], s)

    items.append(PageBreak())

    # CAP 13: Responsive
    items += section_header("CAPÍTULO 13", "Responsive Design y Container Queries\nPara Todos los Dispositivos", s)
    items.append(Paragraph(
        "En 2026, más del 60% del tráfico web es desde móvil. "
        "Responsive Design no es opcional — es el punto de partida. "
        "La filosofía Mobile First garantiza la mejor experiencia en "
        "el dispositivo más limitado y escala hacia arriba.", s['lead']))

    items += sub_header("13.1 Mobile First: La Filosofía Correcta", s)
    items += code_block("CSS — responsive-mobile-first.css", [
        '/* ═══ MOBILE FIRST: el CSS base es para MÓVIL ═══ */',
        '/* Luego escalas hacia arriba con min-width */',
        '',
        '/* BASE (Móvil: 0px en adelante) — siempre primero */',
        '.hero {',
        '  padding: var(--space-8) var(--space-4);  /* Poco espacio en móvil */',
        '  text-align: center;',
        '}',
        '',
        '.hero__content {',
        '  display: flex;',
        '  flex-direction: column;  /* En móvil: texto arriba, imagen abajo */',
        '  gap: var(--space-8);',
        '}',
        '',
        '/* TABLET (768px en adelante) */',
        '@media (min-width: 768px) {',
        '  .hero {',
        '    padding: var(--space-16) var(--space-8);  /* Más espacio */',
        '    text-align: left;',
        '  }',
        '  .hero__content {',
        '    flex-direction: row;  /* Tablet+: texto izq, imagen der */',
        '    align-items: center;',
        '  }',
        '}',
        '',
        '/* DESKTOP (1200px en adelante) */',
        '@media (min-width: 1200px) {',
        '  .hero {',
        '    max-width: 1100px;',
        '    margin: 0 auto;',
        '    padding: var(--space-24) var(--space-12);',
        '  }',
        '}',
        '',
        '/* ═══ CONTAINER QUERIES (CSS 2024) ═══ */',
        '/* Responsive basado en el CONTENEDOR, no el viewport */',
        '.card-wrapper {',
        '  container-type: inline-size;  /* Define este div como contenedor */',
        '  container-name: card;',
        '}',
        '',
        '/* La card se adapta al CONTENEDOR, no a la pantalla */',
        '@container card (min-width: 500px) {',
        '  .card {',
        '    flex-direction: row;  /* Horizontal si el contenedor es ancho */',
        '  }',
        '  .card__media {',
        '    width: 200px;',
        '    flex-shrink: 0;',
        '  }',
        '}',
        '/* Ahora la card se ve bien en un sidebar estrecho Y en un main ancho */',
    ], s)

    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 13 ──", s['h4']))
    items += exercise_block(35, "Fácil", "Revisa tu portfolio en móvil",
        ["Abre Chrome DevTools (F12) → botón de dispositivo móvil",
         "Prueba en iPhone SE (375px) — ¿el texto es legible? ¿hay scroll horizontal?",
         "Si hay scroll horizontal: busca qué elemento tiene width fijo mayor al viewport",
         "Prueba también en tablet (768px) — ¿el layout se adapta?"], s)
    items += exercise_block(36, "Difícil", "Container Queries en cards",
        ["Implementa container-type:inline-size en el wrapper de tus cards",
         "Define @container para que la card sea horizontal cuando el contenedor > 480px",
         "Pon una sección de 2 columnas: las cards de la derecha se ven diferentes",
         "Comprueba: la misma card se ve vertical en el sidebar y horizontal en el main"], s)

    items.append(PageBreak())
    return items

def chapters_14_to_17(s):
    items = []

    # CAP 14: Animaciones
    items += section_header("CAPÍTULO 14", "Animaciones y Microinteracciones\nEl Lenguaje del Movimiento", s)
    items.append(Paragraph(
        "El movimiento bien usado reduce la carga cognitiva y da feedback. "
        "El movimiento mal usado distrae y molesta. La clave: propósito, velocidad "
        "y respeto por el usuario. Siempre respeta prefers-reduced-motion.", s['lead']))

    items += sub_header("14.1 Transiciones y @keyframes", s)
    items += code_block("CSS — animations.css", [
        '/* ─── Transiciones: cambio entre dos estados ─── */',
        '.btn {',
        '  /* Solo anima propiedades baratas: NO activan layout */',
        '  /* transform y opacity van a la GPU: 60fps garantizado */',
        '  transition:',
        '    transform var(--duration-fast) ease,     /* 100ms */',
        '    opacity var(--duration-normal) ease,      /* 200ms */',
        '    background-color var(--duration-normal) ease,',
        '    box-shadow var(--duration-normal) ease;',
        '  /* ❌ NUNCA animes: width, height, top, left, margin, padding */',
        '  /* Estas propiedades activan layout/reflow = lento y brusco */',
        '}',
        '',
        '/* ─── @keyframes: animaciones de entrada ─── */',
        '@keyframes fade-up {',
        '  from {',
        '    opacity: 0;',
        '    transform: translateY(24px);  /* Empieza 24px abajo */',
        '  }',
        '  to {',
        '    opacity: 1;',
        '    transform: translateY(0);     /* Llega a su posición */',
        '  }',
        '}',
        '',
        '/* Aplicar con stagger (delay escalonado) */',
        '.hero__title   { animation: fade-up 0.5s ease both; }',
        '.hero__text    { animation: fade-up 0.5s ease 0.1s both; }  /* 100ms después */',
        '.hero__buttons { animation: fade-up 0.5s ease 0.2s both; }  /* 200ms después */',
        '',
        '/* ─── Skeleton loader ─── */',
        '@keyframes shimmer {',
        '  from { background-position: 200% 0; }',
        '  to   { background-position: -200% 0; }',
        '}',
        '.skeleton {',
        '  background: linear-gradient(90deg,',
        '    var(--color-surface-2) 25%,',
        '    var(--color-surface) 50%,',
        '    var(--color-surface-2) 75%',
        '  );',
        '  background-size: 200%;',
        '  animation: shimmer 1.6s linear infinite;',
        '  border-radius: var(--radius-sm);',
        '}',
        '',
        '/* ─── Scroll-driven (CSS 2024): sin JavaScript ─── */',
        '@keyframes reveal {',
        '  from { opacity: 0; transform: translateY(20px); }',
        '  to   { opacity: 1; transform: none; }',
        '}',
        '.reveal-on-scroll {',
        '  animation: reveal linear both;',
        '  animation-timeline: view();         /* Se activa al entrar al viewport */',
        '  animation-range: entry 0% entry 30%;',
        '}',
        '',
        '/* ─── OBLIGATORIO: respetar preferencia del usuario ─── */',
        '@media (prefers-reduced-motion: reduce) {',
        '  *, *::before, *::after {',
        '    animation-duration: 0.01ms !important;',
        '    animation-iteration-count: 1 !important;',
        '    transition-duration: 0.01ms !important;',
        '  }',
        '}',
    ], s)

    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 14 ──", s['h4']))
    items += exercise_block(37, "Fácil", "Animación de entrada en el hero",
        ["Agrega la animación fade-up al h1, párrafo y botones de tu hero",
         "Usa animation-delay para el efecto escalonado (stagger)",
         "Verifica que con prefers-reduced-motion desactivado funcionen",
         "Activa 'Prefers reduced motion' en DevTools → Rendering y verifica que se detenga"], s)
    items += exercise_block(38, "Difícil", "Skeleton loader para las cards",
        ["Antes de mostrar las cards, muestra 3 skeletons con la animación shimmer",
         "El skeleton debe tener la misma estructura que la card real",
         "Después de 1.5 segundos (simulando una API), oculta los skeletons y muestra las cards",
         "La transición debe ser suave con fade-in"], s)

    items.append(PageBreak())

    # CAP 15: Accesibilidad
    items += section_header("CAPÍTULO 15", "Accesibilidad (A11y) y UX\nDiseño para Todos", s)
    items.append(Paragraph(
        "La accesibilidad no es un feature adicional — es un derecho. "
        "Un sitio inaccesible excluye a millones de personas. "
        "Además, las mismas prácticas que mejoran la accesibilidad "
        "mejoran el SEO y la usabilidad para todos.", s['lead']))

    items += sub_header("15.1 Los 4 Principios WCAG (POUR)", s)
    wcag_data = [
        [Paragraph("<b>Principio</b>", s['h5']), Paragraph("<b>Qué significa</b>", s['h5']),
         Paragraph("<b>Ejemplos prácticos</b>", s['h5'])],
        [Paragraph("P — Perceptible", s['body_small']),
         Paragraph("La información puede verse/oírse", s['body_small']),
         Paragraph("Alt en imágenes, contraste 4.5:1, no usar solo color", s['body_small'])],
        [Paragraph("O — Operable", s['body_small']),
         Paragraph("Se puede usar con teclado", s['body_small']),
         Paragraph("Focus visible, área táctil 44px, sin trampa de foco", s['body_small'])],
        [Paragraph("U — Comprensible", s['body_small']),
         Paragraph("Lenguaje claro, comportamiento predecible", s['body_small']),
         Paragraph("Errores descriptivos, lang='es', labels claros", s['body_small'])],
        [Paragraph("R — Robusto", s['body_small']),
         Paragraph("Compatible con tecnologías asistivas", s['body_small']),
         Paragraph("HTML válido, ARIA correcto, semántica correcta", s['body_small'])],
    ]
    t = Table(wcag_data, colWidths=[3.5*cm, 4.5*cm, None])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1a1a22')),
        ('TEXTCOLOR', (0,0), (-1,0), C_ACCENT),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_CODE_BG, HexColor('#0f0f16')]),
        ('GRID', (0,0), (-1,-1), 1, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    items.append(t)
    items.append(spacer(10))

    items += sub_header("15.2 Utilidades de Accesibilidad Esenciales", s)
    items += code_block("CSS + HTML — accesibilidad.css", [
        '/* ── Skip link: PRIMER elemento de la página ── */',
        '/* Permite a usuarios de teclado saltar la navegación directamente al contenido */',
        '.skip-link {',
        '  position: fixed;',
        '  top: -100px;          /* Fuera de pantalla por defecto */',
        '  left: var(--space-4);',
        '  background: var(--color-accent);',
        '  color: white;',
        '  padding: var(--space-3) var(--space-6);',
        '  border-radius: var(--radius-md);',
        '  font-weight: 600;',
        '  z-index: 9999;',
        '  text-decoration: none;',
        '  transition: top 200ms ease;',
        '}',
        '.skip-link:focus { top: var(--space-4); }  /* Aparece al hacer Tab */',
        '',
        '/* ── .sr-only: texto solo para lectores de pantalla ── */',
        '/* Visible para tecnologías asistivas pero no en pantalla */',
        '.sr-only {',
        '  position: absolute;',
        '  width: 1px; height: 1px;',
        '  padding: 0; margin: -1px;',
        '  overflow: hidden;',
        '  clip: rect(0,0,0,0);',
        '  white-space: nowrap;',
        '  border: 0;',
        '}',
        '',
        '<!-- En el HTML: skip link como PRIMER elemento del body -->',
        '<a href="#main-content" class="skip-link">Saltar al contenido principal</a>',
        '<!-- ... navbar ... -->',
        '<main id="main-content">  <!-- El destino del skip link -->',
        '',
        '/* ── Focus visible: NUNCA elimines el outline sin reemplazarlo ── */',
        ':focus-visible {',
        '  outline: 2px solid var(--color-accent);',
        '  outline-offset: 3px;',
        '  border-radius: 3px;',
        '  /* :focus-visible solo aplica cuando el usuario usa teclado */',
        '  /* No aparece al hacer clic con ratón (UX correcto) */',
        '}',
    ], s)

    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 15 ──", s['h4']))
    items += exercise_block(39, "Fácil", "Auditoría básica de accesibilidad",
        ["Instala la extensión 'axe DevTools' en Chrome",
         "Ejecuta el análisis en tu portfolio — ¿cuántos errores hay?",
         "Corrige los 3 más críticos (generalmente: alt en imágenes, contraste, labels)",
         "Prueba navegando solo con Tab — ¿puedes llegar a todos los elementos?"], s)
    items += exercise_block(40, "Difícil", "Implementa el skip link",
        ["Agrega el skip link como primer elemento de tu body",
         "El link debe ir a <main id='main-content'>",
         "Estiliza el skip link para que aparezca solo al enfocarse (Tab)",
         "Verifica: al hacer Tab en tu página, ¿el skip link aparece primero?"], s)

    items.append(PageBreak())

    # CAP 16: Dark Mode
    items += section_header("CAPÍTULO 16", "Dark Mode y Temas de Color\nDos Caras del Mismo Diseño", s)
    items.append(Paragraph(
        "El dark mode no es hacer todo negro. Es un sistema de color paralelo "
        "que cuida los ojos del usuario en entornos oscuros. "
        "Con tokens de diseño bien definidos, implementarlo es cambiar "
        "solo las variables semánticas.", s['lead']))

    items += code_block("CSS — dark-mode.css", [
        '/* ── Nivel 1: Automático por preferencia del sistema ── */',
        '@media (prefers-color-scheme: dark) {',
        '  :root {',
        '    /* Solo cambias los tokens SEMÁNTICOS — los primitivos no cambian */',
        '    --color-bg:           oklch(12% 0.005 250);  /* Fondo oscuro */',
        '    --color-surface:      oklch(16% 0.005 250);  /* Cards oscuras */',
        '    --color-surface-2:    oklch(20% 0.005 250);  /* Bordes sutiles */',
        '    --color-text:         oklch(94% 0.005 250);  /* Texto casi blanco */',
        '    --color-text-muted:   oklch(60% 0.005 250);  /* Texto secundario */',
        '    --color-border:       oklch(26% 0.005 250);  /* Bordes oscuros */',
        '    --shadow-md: 0 4px 16px oklch(0% 0 0 / 30%); /* Sombras más fuertes */',
        '  }',
        '}',
        '',
        '/* ── Nivel 2: Toggle manual con data-theme en <html> ── */',
        '[data-theme="dark"] {',
        '  --color-bg:         oklch(12% 0.005 250);',
        '  /* ... mismo código que arriba ... */',
        '}',
        '',
        '/* ── Sin parpadeo en carga de página: script en <head> ── */',
        '<!-- Antes del CSS, en el <head>: -->',
        '<script>',
        "  const saved = localStorage.getItem('theme');",
        "  const prefersDark = matchMedia('(prefers-color-scheme:dark)').matches;",
        "  const theme = saved ?? (prefersDark ? 'dark' : 'light');",
        "  document.documentElement.setAttribute('data-theme', theme);",
        '</script>',
        '',
        '/* Botón de toggle en JavaScript: */',
        'function toggleTheme() {',
        "  const current = document.documentElement.getAttribute('data-theme');",
        "  const next = current === 'dark' ? 'light' : 'dark';",
        "  document.documentElement.setAttribute('data-theme', next);",
        "  localStorage.setItem('theme', next);",
        '  // Actualizar aria-label del botón',
        "  themeBtn.setAttribute('aria-label',",
        "    next === 'dark' ? 'Cambiar a modo claro' : 'Cambiar a modo oscuro'",
        '  );',
        '}',
    ], s)

    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 16 ──", s['h4']))
    items += exercise_block(41, "Medio", "Dark mode automático",
        ["Agrega el @media prefers-color-scheme:dark a tu CSS",
         "Cambia solo los tokens semánticos (bg, surface, text, border)",
        "En macOS: System Preferences → Appearance → Dark para probarlo",
         "En Windows: Settings → Personalization → Colors → Dark"], s)
    items += exercise_block(42, "Difícil", "Toggle de tema completo",
        ["Agrega el script sin-parpadeo en el <head> de tu HTML",
         "Crea un botón con ícono de sol/luna en la navbar",
         "Al hacer clic, alterna data-theme entre 'light' y 'dark'",
         "Guarda la preferencia en localStorage",
         "El botón debe tener aria-label actualizado según el tema activo"], s)

    items.append(PageBreak())

    # CAP 17: Arquitectura
    items += section_header("CAPÍTULO 17", "Arquitectura CSS\n@layer y BEM", s)
    items.append(Paragraph(
        "Sin arquitectura, el CSS se convierte en espagueti. "
        "@layer permite controlar la cascada explícitamente. "
        "BEM da nombres consistentes. Juntos hacen que tu CSS "
        "sea mantenible incluso 2 años después.", s['lead']))

    items += code_block("CSS — arquitectura-completa.css", [
        '/* ── css/main.css: El entry point de todo el CSS ── */',
        '',
        '/* 1. Declarar el orden de la cascada (mayor prioridad = último) */',
        '@layer reset, tokens, base, layout, components, pages, utilities;',
        '',
        '/* 2. Importar en orden */',
        '@import "01-reset.css"               layer(reset);',
        '@import "00-tokens.css"              layer(tokens);',
        '@import "02-typography.css"          layer(base);',
        '@import "03-layout.css"              layer(layout);',
        '@import "components/button.css"      layer(components);',
        '@import "components/card.css"        layer(components);',
        '@import "components/navbar.css"      layer(components);',
        '@import "components/form.css"        layer(components);',
        '@import "components/badge.css"       layer(components);',
        '@import "components/modal.css"       layer(components);',
        '@import "pages/home.css"             layer(pages);',
        '@import "pages/projects.css"         layer(pages);',
        '@import "pages/contact.css"          layer(pages);',
        '@import "utilities.css"              layer(utilities);',
        '/* Las utilities SIEMPRE ganan — sin !important */',
        '',
        '/* ── BEM: Block, Element, Modifier ── */',
        '/* .bloque                 → El componente */',
        '/* .bloque__elemento       → Parte del componente */',
        '/* .bloque--modificador    → Variante del componente */',
        '',
        '/* Ejemplo aplicado: */',
        '.card { }                  /* Block: la card en sí */',
        '.card__media { }           /* Element: imagen de la card */',
        '.card__body { }            /* Element: cuerpo de la card */',
        '.card__title { }           /* Element: título de la card */',
        '.card--featured { }        /* Modifier: card destacada */',
        '.card--horizontal { }      /* Modifier: card en horizontal */',
    ], s)

    items.append(Paragraph("── EJERCICIOS DEL CAPÍTULO 17 ──", s['h4']))
    items += exercise_block(43, "Medio", "Restructura tu CSS con @layer",
        ["Crea el archivo main.css con @layer y los @import del proyecto",
         "Mueve cada CSS a su archivo correspondiente (components/, pages/)",
         "Verifica que el orden de importación no rompa ningún estilo",
         "Abre DevTools → Sources y verifica que el CSS esté organizado"], s)
    items += exercise_block(44, "Difícil", "Refactoriza con BEM",
        ["Revisa tus componentes actuales y aplica nomenclatura BEM",
         "Ejemplo: .project-card → .card; .project-card-title → .card__title",
         "Si tienes variantes, usa el doble guión: .card--featured",
         "Documenta en README.md qué bloques, elementos y modificadores tiene tu sistema"], s)

    items.append(PageBreak())
    return items

# ─────────────────────────────────────────
# PROYECTO FINAL: PORTAFOLIO
# ─────────────────────────────────────────
def final_project(s):
    items = []
    items += section_header("PROYECTO FINAL", "Portfolio de Desarrollador\nGuía Completa Paso a Paso", s)

    items.append(Paragraph(
        "Este es el momento de aplicar todo lo aprendido. "
        "Construirás un portfolio profesional que demuestre tus habilidades "
        "como desarrollador frontend. Este proyecto ES tu aplicación de trabajo.", s['lead']))

    # Estructura de carpetas
    items.append(Paragraph("ESTRUCTURA DE CARPETAS (Buenas Prácticas)", s['project_title']))
    items.append(Paragraph(
        "La organización de tu código es tan importante como el código mismo. "
        "Un reclutador técnico revisará tu estructura de archivos:", s['body']))

    items += code_block("ESTRUCTURA — portfolio/ (distribución de carpetas)", [
        'portfolio/',
        '│',
        '├── 📄 index.html                 ← Página principal (Home)',
        '├── 📄 proyectos.html              ← Galería de proyectos',
        '├── 📄 sobre-mi.html               ← Página about',
        '├── 📄 contacto.html               ← Formulario de contacto',
        '├── 📄 proyecto-detalle.html       ← Template de proyecto individual',
        '│',
        '├── 📁 css/',
        '│   ├── 00-tokens.css              ← Design tokens (primitivos + semánticos)',
        '│   ├── 01-reset.css               ← Reset y base tipográfica',
        '│   ├── 02-typography.css          ← Escala tipográfica',
        '│   ├── 03-layout.css              ← Container, grid de página',
        '│   ├── main.css                   ← Entry point: @layer + @import',
        '│   ├── components/',
        '│   │   ├── button.css             ← Sistema de botones',
        '│   │   ├── card.css               ← Componente card',
        '│   │   ├── navbar.css             ← Navegación',
        '│   │   ├── form.css               ← Formularios',
        '│   │   ├── badge.css              ← Badges y tags',
        '│   │   ├── modal.css              ← Modales',
        '│   │   ├── avatar.css             ← Avatar de perfil',
        '│   │   └── skeleton.css           ← Loading states',
        '│   └── pages/',
        '│       ├── home.css               ← Estilos específicos del home',
        '│       ├── projects.css           ← Estilos de la galería',
        '│       └── contact.css            ← Estilos del formulario',
        '│',
        '├── 📁 js/',
        '│   ├── main.js                    ← Entry point JS (type="module")',
        '│   ├── theme.js                   ← Toggle dark/light mode',
        '│   ├── components/',
        '│   │   ├── navbar.js              ← Menú mobile toggle',
        '│   │   ├── modal.js               ← Abrir/cerrar modales',
        '│   │   └── tabs.js                ← Tabs con keyboard navigation',
        '│   └── utils/',
        '│       ├── helpers.js             ← Funciones reutilizables',
        '│       └── form-validation.js     ← Lógica de validación',
        '│',
        '├── 📁 assets/',
        '│   ├── fonts/                     ← WOFF2 de fuentes locales',
        '│   ├── images/',
        '│   │   ├── hero/                  ← Imagen(es) del hero',
        '│   │   ├── projects/              ← Capturas de proyectos',
        '│   │   └── profile/               ← Foto de perfil',
        '│   ├── icons/',
        '│   │   └── sprite.svg             ← Todos los SVG en un sprite',
        '│   └── og/                        ← Imágenes Open Graph (1200x630px)',
        '│',
        '├── 📁 data/',
        '│   └── projects.json              ← Lista de proyectos (JSON)',
        '│',
        '└── 📄 README.md                   ← Documentación del proyecto',
    ], s)

    items += tip("Por qué esta estructura",
        "Separar tokens → base → componentes → páginas es la misma lógica de @layer. "
        "Cada archivo tiene una responsabilidad. Un archivo de componente nunca "
        "debería tener más de 150 líneas — si lo supera, divídelo.", s)

    # HTML Base
    items.append(Paragraph("TEMPLATE BASE (Aplicar a TODAS las páginas)", s['project_title']))
    items += code_block("HTML — template-base.html (copia esto en cada .html)", [
        '<!DOCTYPE html>',
        '<html lang="es" data-theme="light">',
        '<head>',
        '  <!-- Script sin-parpadeo: ANTES del CSS, restaura el tema guardado -->',
        '  <script>',
        "    const t = localStorage.getItem('theme');",
        "    const d = matchMedia('(prefers-color-scheme:dark)').matches;",
        "    document.documentElement.setAttribute('data-theme', t ?? (d ? 'dark' : 'light'));",
        '  </script>',
        '',
        '  <meta charset="UTF-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        '  <meta name="description" content="Portfolio de [Tu Nombre], desarrollador frontend">',
        '',
        '  <!-- Theme color dinámico según el tema -->',
        '  <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">',
        '  <meta name="theme-color" content="#0d0d12" media="(prefers-color-scheme: dark)">',
        '',
        '  <title>[Página] — [Tu Nombre] | Frontend Developer</title>',
        '',
        '  <!-- Open Graph: cómo se ve al compartir en redes -->',
        '  <meta property="og:title" content="[Tu Nombre] — Portfolio">',
        '  <meta property="og:description" content="Desarrollador Frontend apasionado...">',
        '  <meta property="og:image" content="/assets/og/home.jpg">',
        '  <meta property="og:type" content="website">',
        '',
        '  <!-- Favicon SVG: escala perfecto a cualquier tamaño -->',
        '  <link rel="icon" href="/assets/icons/favicon.svg" type="image/svg+xml">',
        '',
        '  <!-- Fuentes: preconnect primero para reducir latencia -->',
        '  <link rel="preconnect" href="https://fonts.googleapis.com">',
        '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '  <!-- Reemplaza esta URL con tus fuentes elegidas -->',
        '  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400..800&display=swap"',
        '        rel="stylesheet">',
        '',
        '  <!-- CSS principal: @layer organiza toda la cascada -->',
        '  <link rel="stylesheet" href="/css/main.css">',
        '</head>',
        '<body>',
        '',
        '  <!-- Skip link: PRIMER elemento para usuarios de teclado -->',
        '  <a href="#main-content" class="skip-link">Saltar al contenido</a>',
        '',
        '  <!-- ═══ HEADER GLOBAL ═══ -->',
        '  <header class="navbar">',
        '    <a href="/" class="navbar__brand">',
        '      <span class="navbar__logo">[Tu Nombre]</span>',
        '    </a>',
        '',
        '    <!-- Hamburguesa: visible solo en móvil -->',
        '    <button class="navbar__toggle btn btn--ghost btn--icon"',
        '            aria-expanded="false"',
        '            aria-controls="main-nav"',
        '            aria-label="Abrir menú">',
        '      <!-- Ícono hamburguesa SVG -->',
        '    </button>',
        '',
        '    <nav id="main-nav" class="navbar__nav" aria-label="Principal">',
        '      <a href="/" class="navbar__link">Inicio</a>',
        '      <a href="/proyectos.html" class="navbar__link">Proyectos</a>',
        '      <a href="/sobre-mi.html" class="navbar__link">Sobre mí</a>',
        '      <a href="/contacto.html" class="navbar__link">Contacto</a>',
        '    </nav>',
        '',
        '    <div class="navbar__actions">',
        '      <!-- Botón de tema: aria-label se actualiza con JS -->',
        '      <button id="theme-toggle" class="btn btn--ghost btn--icon"',
        '              aria-label="Cambiar a modo oscuro">',
        '        <!-- Ícono sol/luna -->',
        '      </button>',
        '    </div>',
        '  </header>',
        '',
        '  <!-- ═══ CONTENIDO PRINCIPAL ═══ -->',
        '  <!-- id="main-content": destino del skip link -->',
        '  <main id="main-content">',
        '',
        '    <!-- ══════════════════════════════════════════════════ -->',
        '    <!--           CONTENIDO DE CADA PÁGINA               -->',
        '    <!-- ══════════════════════════════════════════════════ -->',
        '',
        '  </main>',
        '',
        '  <!-- ═══ FOOTER GLOBAL ═══ -->',
        '  <footer class="footer">',
        '    <div class="footer__container">',
        '      <p class="footer__copy">',
        '        © <span id="year"></span> [Tu Nombre] — Hecho con HTML &amp; CSS',
        '      </p>',
        '      <div class="footer__social">',
        '        <a href="https://github.com/tuusuario" target="_blank"',
        '           rel="noopener noreferrer" aria-label="GitHub de [Tu Nombre]">',
        '          GitHub',
        '        </a>',
        '        <a href="https://linkedin.com/in/tuusuario" target="_blank"',
        '           rel="noopener noreferrer" aria-label="LinkedIn de [Tu Nombre]">',
        '          LinkedIn',
        '        </a>',
        '      </div>',
        '    </div>',
        '  </footer>',
        '',
        '  <!-- Scripts al FINAL del body: no bloquean el render -->',
        '  <!-- type="module": habilita import/export y defer automático -->',
        '  <script type="module" src="/js/main.js"></script>',
        '',
        '  <!-- Año dinámico en el footer -->',
        '  <script>document.getElementById("year").textContent = new Date().getFullYear();</script>',
        '',
        '</body>',
        '</html>',
    ], s)

    # Secciones del home
    items.append(Paragraph("SECCIÓN HERO — index.html", s['project_title']))
    items += code_block("HTML — sections/hero.html", [
        '<!-- ═══ SECCIÓN HERO ═══ -->',
        '<!-- section con aria-labelledby conecta el título al lector de pantalla -->',
        '<section class="hero" aria-labelledby="hero-titulo">',
        '  <div class="hero__container">',
        '',
        '    <!-- Contenido textual -->',
        '    <div class="hero__content">',
        '',
        '      <!-- Etiqueta pequeña encima del título -->',
        '      <p class="hero__eyebrow">',
        '        <span aria-hidden="true">👋</span> Hola, soy',
        '      </p>',
        '',
        '      <!-- H1: Solo uno por página. El más importante para SEO -->',
        '      <h1 class="hero__title" id="hero-titulo">',
        '        [Tu Nombre]',
        '        <span class="hero__title-accent">Frontend Developer</span>',
        '      </h1>',
        '',
        '      <p class="hero__description">',
        '        Construyo interfaces web modernas, accesibles y con',
        '        atención al detalle. Especializado en HTML, CSS y JavaScript.',',
        '      </p>',
        '',
        '      <!-- CTAs principales -->',
        '      <div class="hero__actions">',
        '        <a href="#proyectos" class="btn btn--primary btn--lg">',
        '          Ver mis proyectos',
        '        </a>',
        '        <a href="/assets/cv-tunombre.pdf"',
        '           class="btn btn--secondary btn--lg"',
        '           download',
        '           aria-label="Descargar CV de [Tu Nombre] en PDF">',
        '          Descargar CV',
        '        </a>',
        '      </div>',
        '',
        '      <!-- Estadísticas -->',
        '      <dl class="hero__stats">',
        '        <div class="hero__stat">',
        '          <dt class="sr-only">Años de experiencia</dt>',
        '          <dd class="hero__stat-number">3+</dd>',
        '          <dd class="hero__stat-label">Años</dd>',
        '        </div>',
        '        <div class="hero__stat">',
        '          <dt class="sr-only">Proyectos completados</dt>',
        '          <dd class="hero__stat-number">20+</dd>',
        '          <dd class="hero__stat-label">Proyectos</dd>',
        '        </div>',
        '        <div class="hero__stat">',
        '          <dt class="sr-only">Tecnologías dominadas</dt>',
        '          <dd class="hero__stat-number">10+</dd>',
        '          <dd class="hero__stat-label">Tecnologías</dd>',
        '        </div>',
        '      </dl>',
        '    </div>',
        '',
        '    <!-- Foto de perfil -->',
        '    <div class="hero__visual">',
        '      <div class="hero__avatar">',
        '        <picture>',
        '          <source type="image/webp" srcset="/assets/images/profile/foto.webp">',
        '          <img',
        '            src="/assets/images/profile/foto.jpg"',
        '            alt="[Tu Nombre] — Desarrollador Frontend"',
        '            width="400" height="400"',
        '            loading="eager"   <!-- La imagen hero es LCP: cárgala inmediatamente -->',
        '            fetchpriority="high"',
        '          >',
        '        </picture>',
        '      </div>',
        '    </div>',
        '',
        '  </div>',
        '</section>',
    ], s)

    items += code_block("CSS — pages/home.css (sección hero)", [
        '/* ═══ HERO ═══ */',
        '.hero {',
        '  /* Altura: min 100svh usa el alto dinámico del viewport (evita el bug de móvil) */',
        '  min-height: 100svh;',
        '  display: flex;',
        '  align-items: center;',
        '  padding: var(--space-12) 0;',
        '  /* Fondo con gradiente sutil */',
        '  background: radial-gradient(',
        '    ellipse 80% 50% at 20% 40%,',
        '    color-mix(in srgb, var(--color-accent), transparent 90%) 0%,',
        '    transparent 60%',
        '  );',
        '}',
        '',
        '.hero__container {',
        '  width: min(1100px, 100% - 2 * var(--space-6));  /* Ancho máximo centrado */',
        '  margin: 0 auto;',
        '  display: grid;',
        '  grid-template-columns: 1fr;        /* Móvil: una columna */',
        '  gap: var(--space-12);',
        '  align-items: center;',
        '}',
        '',
        '@media (min-width: 768px) {',
        '  .hero__container {',
        '    grid-template-columns: 1fr 1fr;  /* Tablet+: dos columnas */',
        '  }',
        '}',
        '',
        '.hero__eyebrow {',
        '  font-size: var(--size-sm);',
        '  color: var(--color-text-muted);',
        '  margin-bottom: var(--space-3);',
        '}',
        '',
        '.hero__title {',
        '  font-size: clamp(2.5rem, 6vw + 1rem, 5rem);  /* Fluido: 40px → 80px */',
        '  font-weight: 800;',
        '  line-height: 1.0;',
        '  letter-spacing: -0.03em;',
        '  margin-bottom: var(--space-4);',
        '}',
        '',
        '.hero__title-accent {',
        '  display: block;                   /* En su propia línea */',
        '  color: var(--color-accent);',
        '  font-style: italic;',
        '}',
        '',
        '.hero__description {',
        '  font-size: clamp(1rem, 1.5vw, 1.15rem);',
        '  color: var(--color-text-muted);',
        '  max-width: 50ch;',
        '  line-height: 1.7;',
        '  margin-bottom: var(--space-8);',
        '}',
        '',
        '.hero__actions {',
        '  display: flex;',
        '  flex-wrap: wrap;',
        '  gap: var(--space-4);',
        '  margin-bottom: var(--space-10);',
        '}',
        '',
        '/* Estadísticas */',
        '.hero__stats {',
        '  display: flex;',
        '  gap: var(--space-8);',
        '  flex-wrap: wrap;',
        '}',
        '',
        '.hero__stat {',
        '  display: flex;',
        '  flex-direction: column;',
        '}',
        '',
        '.hero__stat-number {',
        '  font-size: var(--size-2xl);',
        '  font-weight: 800;',
        '  color: var(--color-accent);',
        '  line-height: 1;',
        '}',
        '',
        '.hero__stat-label {',
        '  font-size: var(--size-xs);',
        '  color: var(--color-text-muted);',
        '  text-transform: uppercase;',
        '  letter-spacing: 0.08em;',
        '}',
        '',
        '/* Avatar */',
        '.hero__avatar {',
        '  width: min(360px, 100%);',
        '  aspect-ratio: 1;',
        '  border-radius: var(--radius-xl);',
        '  overflow: hidden;',
        '  border: 3px solid var(--color-border);',
        '  box-shadow: var(--shadow-lg);',
        '  margin: 0 auto;',
        '}',
        '',
        '.hero__avatar img {',
        '  width: 100%; height: 100%;',
        '  object-fit: cover;',
        '}',
        '',
        '/* Animación de entrada */',
        '.hero__eyebrow  { animation: fade-up 0.5s ease both; }',
        '.hero__title    { animation: fade-up 0.5s ease 0.1s both; }',
        '.hero__description { animation: fade-up 0.5s ease 0.2s both; }',
        '.hero__actions  { animation: fade-up 0.5s ease 0.3s both; }',
        '.hero__stats    { animation: fade-up 0.5s ease 0.4s both; }',
        '.hero__visual   { animation: fade-up 0.5s ease 0.2s both; }',
    ], s)

    # Sección de proyectos
    items.append(Paragraph("SECCIÓN PROYECTOS — index.html", s['project_title']))
    items += code_block("HTML — sections/projects.html", [
        '<section class="projects" id="proyectos" aria-labelledby="projects-titulo">',
        '  <div class="section-container">',
        '',
        '    <header class="section-header">',
        '      <p class="section-eyebrow">Mi trabajo</p>',
        '      <h2 class="section-title" id="projects-titulo">Proyectos Destacados</h2>',
        '      <p class="section-description">',
        '        Una selección de mis mejores proyectos. Cada uno representa',
        '        un reto diferente y una habilidad desarrollada.',
        '      </p>',
        '    </header>',
        '',
        '    <!-- Grid de proyectos con container queries -->',
        '    <div class="projects-grid">',
        '',
        '      <!-- Proyecto 1 -->',
        '      <div class="card-wrapper">  <!-- Container para container queries -->',
        '        <article class="card card--interactive"',
        '                 aria-label="Proyecto: App del Clima">',
        '          <div class="card__media">',
        '            <picture>',
        '              <source type="image/webp" srcset="/assets/images/projects/clima.webp">',
        '              <img src="/assets/images/projects/clima.jpg"',
        '                   alt="App del clima mostrando temperatura 24°C"',
        '                   width="600" height="338" loading="lazy">',
        '            </picture>',
        '            <span class="card__badge badge badge--success">Completado</span>',
        '          </div>',
        '          <div class="card__body">',
        '            <header class="card__header">',
        '              <span class="card__category">API REST</span>',
        '              <h3 class="card__title">App del Clima</h3>',
        '            </header>',
        '            <p class="card__description">',
        '              Aplicación del tiempo con datos en tiempo real de OpenWeather API.',
        '              Geolocalización automática, diseño responsive.',
        '            </p>',
        '            <div class="card__tags">',
        '              <span class="badge badge--info">JavaScript</span>',
        '              <span class="badge badge--info">CSS Grid</span>',
        '              <span class="badge badge--info">API REST</span>',
        '            </div>',
        '          </div>',
        '          <footer class="card__footer">',
        '            <a href="/proyecto-detalle.html" class="btn btn--primary btn--sm">',
        '              Ver proyecto',
        '            </a>',
        '            <a href="https://github.com/..." target="_blank"',
        '               rel="noopener noreferrer" class="btn btn--ghost btn--sm">',
        '              GitHub',
        '            </a>',
        '          </footer>',
        '        </article>',
        '      </div>',
        '',
        '      <!-- Repite la estructura para cada proyecto -->',
        '      <!-- ..._PROYECTO 2_, ..._PROYECTO 3_, etc. -->',
        '',
        '    </div>',
        '',
        '    <div class="projects-cta">',
        '      <a href="/proyectos.html" class="btn btn--secondary btn--lg">',
        '        Ver todos los proyectos',
        '      </a>',
        '    </div>',
        '',
        '  </div>',
        '</section>',
    ], s)

    # CSS Proyectos
    items += code_block("CSS — pages/projects.css", [
        '.projects { padding: var(--space-24) 0; }',
        '',
        '.section-container {',
        '  width: min(1100px, 100% - 2 * var(--space-6));',
        '  margin: 0 auto;',
        '}',
        '',
        '.section-header {',
        '  text-align: center;',
        '  max-width: 60ch;',
        '  margin: 0 auto var(--space-12);',
        '}',
        '',
        '.section-eyebrow {',
        '  font-size: var(--size-sm);',
        '  font-weight: 600;',
        '  text-transform: uppercase;',
        '  letter-spacing: 0.1em;',
        '  color: var(--color-accent);',
        '  margin-bottom: var(--space-3);',
        '}',
        '',
        '.section-title {',
        '  font-size: clamp(1.8rem, 3vw, 2.5rem);',
        '  font-weight: 800;',
        '  margin-bottom: var(--space-4);',
        '  text-wrap: balance;',
        '}',
        '',
        '.section-description {',
        '  font-size: var(--size-base);',
        '  color: var(--color-text-muted);',
        '  line-height: 1.7;',
        '}',
        '',
        '/* Grid responsive SIN media queries */',
        '.projects-grid {',
        '  display: grid;',
        '  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));',
        '  gap: var(--space-6);',
        '}',
        '',
        '/* Container query en las cards */',
        '.card-wrapper {',
        '  container-type: inline-size;',
        '  container-name: project-card;',
        '}',
        '',
        '.projects-cta {',
        '  text-align: center;',
        '  margin-top: var(--space-12);',
        '}',
    ], s)

    # Contacto
    items.append(Paragraph("SECCIÓN CONTACTO — contacto.html", s['project_title']))
    items += code_block("HTML — sections/contact.html", [
        '<section class="contact" id="contacto" aria-labelledby="contact-titulo">',
        '  <div class="section-container">',
        '',
        '    <header class="section-header">',
        '      <p class="section-eyebrow">¿Hablamos?</p>',
        '      <h2 class="section-title" id="contact-titulo">Contáctame</h2>',
        '    </header>',
        '',
        '    <form class="contact-form" id="contact-form"',
        '          action="/enviar" method="POST" novalidate',
        '          aria-label="Formulario de contacto">',
        '',
        '      <div class="form-grid">',
        '',
        '        <!-- Campo Nombre -->',
        '        <div class="field">',
        '          <label class="field__label" for="contact-nombre">',
        '            Nombre completo <span aria-hidden="true">*</span>',
        '          </label>',
        '          <input class="field__input" type="text" id="contact-nombre"',
        '                 name="nombre" autocomplete="name"',
        '                 required minlength="2"',
        '                 aria-required="true"',
        '                 aria-describedby="nombre-error"',
        '                 aria-invalid="false"',
        '                 placeholder="Tu nombre">',
        '          <p class="field__error" id="nombre-error" role="alert" hidden></p>',
        '        </div>',
        '',
        '        <!-- Campo Email -->',
        '        <div class="field">',
        '          <label class="field__label" for="contact-email">',
        '            Email <span aria-hidden="true">*</span>',
        '          </label>',
        '          <input class="field__input" type="email" id="contact-email"',
        '                 name="email" autocomplete="email"',
        '                 required',
        '                 aria-required="true"',
        '                 aria-describedby="email-error"',
        '                 aria-invalid="false"',
        '                 placeholder="tu@email.com">',
        '          <p class="field__error" id="email-error" role="alert" hidden></p>',
        '        </div>',
        '',
        '        <!-- Campo Asunto (full width) -->',
        '        <div class="field field--full">',
        '          <label class="field__label" for="contact-asunto">',
        '            Asunto <span aria-hidden="true">*</span>',
        '          </label>',
        '          <input class="field__input" type="text" id="contact-asunto"',
        '                 name="asunto" required minlength="5"',
        '                 aria-required="true"',
        '                 placeholder="¿En qué puedo ayudarte?">',
        '        </div>',
        '',
        '        <!-- Campo Mensaje (full width) -->',
        '        <div class="field field--full">',
        '          <label class="field__label" for="contact-mensaje">',
        '            Mensaje <span aria-hidden="true">*</span>',
        '          </label>',
        '          <textarea class="field__input" id="contact-mensaje"',
        '                    name="mensaje" rows="6"',
        '                    required minlength="20"',
        '                    aria-required="true"',
        '                    aria-describedby="mensaje-hint mensaje-error"',
        '                    placeholder="Cuéntame sobre tu proyecto..."></textarea>',
        '          <p class="field__hint" id="mensaje-hint">',
        '            Mínimo 20 caracteres. Sé específico sobre tu proyecto.',
        '          </p>',
        '          <p class="field__error" id="mensaje-error" role="alert" hidden></p>',
        '        </div>',
        '',
        '      </div><!-- /form-grid -->',
        '',
        '      <div class="contact-form__actions">',
        '        <button type="submit" class="btn btn--primary btn--lg" id="submit-btn">',
        '          Enviar mensaje',
        '        </button>',
        '      </div>',
        '',
        '      <!-- Área de mensajes de estado del formulario -->',
        '      <div id="form-status" role="status" aria-live="polite"></div>',
        '',
        '    </form>',
        '  </div>',
        '</section>',
    ], s)

    # JS del formulario
    items.append(Paragraph("JAVASCRIPT DEL FORMULARIO", s['project_title']))
    items += code_block("JS — utils/form-validation.js", [
        '// Validación del formulario de contacto',
        '// Módulo ES: se importa en main.js con import { initContactForm } from ...',
        '',
        "export function initContactForm() {",
        "  const form = document.getElementById('contact-form');",
        "  if (!form) return;  // Salir si no existe el formulario en esta página",
        '',
        "  form.addEventListener('submit', handleSubmit);",
        '',
        "  async function handleSubmit(e) {",
        "    e.preventDefault();  // Evita el envío nativo del formulario",
        '',
        '    // Limpiar errores anteriores',
        '    clearErrors(form);',
        '',
        '    // Validar todos los campos',
        '    const isValid = validateForm(form);',
        '    if (!isValid) return;  // Detener si hay errores',
        '',
        '    // Iniciar estado de carga',
        "    const btn = document.getElementById('submit-btn');",
        "    btn.classList.add('btn--loading');",
        "    btn.setAttribute('aria-busy', 'true');",
        "    btn.disabled = true;",
        '',
        '    try {',
        '      // Aquí irá tu lógica real de envío (fetch, formspree, etc.)',
        '      await simulateSubmit();  // Simulación de 2 segundos',
        '',
        '      // Éxito: mostrar mensaje y resetear formulario',
        "      showStatus('¡Mensaje enviado! Te responderé en menos de 24 horas.', 'success');",
        '      form.reset();',
        '',
        '    } catch (error) {',
        "      showStatus('Error al enviar. Intenta de nuevo o escríbeme directamente.', 'error');",
        '',
        '    } finally {',
        '      // Restaurar el botón siempre',
        "      btn.classList.remove('btn--loading');",
        "      btn.removeAttribute('aria-busy');",
        '      btn.disabled = false;',
        '    }',
        '  }',
        '',
        '  function validateForm(form) {',
        '    let isValid = true;',
        "    const nombre = form.querySelector('#contact-nombre');",
        "    const email = form.querySelector('#contact-email');",
        "    const mensaje = form.querySelector('#contact-mensaje');",
        '',
        "    if (!nombre.value.trim() || nombre.value.trim().length < 2) {",
        "      showError(nombre, 'El nombre debe tener al menos 2 caracteres.');",
        '      isValid = false;',
        '    }',
        '',
        '    const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;',
        '    if (!emailRegex.test(email.value.trim())) {',
        "      showError(email, 'Ingresa un email válido (ej: nombre@dominio.com)');",
        '      isValid = false;',
        '    }',
        '',
        '    if (!mensaje.value.trim() || mensaje.value.trim().length < 20) {',
        "      showError(mensaje, 'El mensaje debe tener al menos 20 caracteres.');",
        '      isValid = false;',
        '    }',
        '',
        '    return isValid;',
        '  }',
        '',
        '  function showError(input, message) {',
        "    const errorId = input.getAttribute('aria-describedby')?.split(' ')[0];",
        '    const errorEl = document.getElementById(errorId);',
        '    if (errorEl) {',
        '      errorEl.textContent = message;',
        '      errorEl.hidden = false;',
        '    }',
        "    input.setAttribute('aria-invalid', 'true');",
        "    input.classList.add('has-error');",
        '    input.focus();  // Foco al primer campo con error',
        '  }',
        '',
        '  function clearErrors(form) {',
        "    form.querySelectorAll('[aria-invalid]').forEach(el => {",
        "      el.setAttribute('aria-invalid', 'false');",
        "      el.classList.remove('has-error');",
        '    });',
        "    form.querySelectorAll('.field__error').forEach(el => {",
        '      el.textContent = "";',
        '      el.hidden = true;',
        '    });',
        '  }',
        '',
        '  function showStatus(message, type) {',
        "    const status = document.getElementById('form-status');",
        "    status.innerHTML = `<div class='alert alert--${type}' role='${type === 'error' ? 'alert' : 'status'}'>${message}</div>`;",
        '  }',
        '',
        '  function simulateSubmit() {',
        '    return new Promise(resolve => setTimeout(resolve, 2000));',
        '  }',
        '}',
    ], s)

    # Criterios de calidad
    items.append(Paragraph("CRITERIOS DE CALIDAD DEL PROYECTO FINAL", s['project_title']))
    items.append(Paragraph(
        "Antes de considerar tu portfolio terminado, verifica CADA punto de esta lista:", s['body']))

    criterios = [
        ("✅ HTML Semántico", "Usa header, main, footer, section, article, nav — sin divitis"),
        ("✅ Design Tokens", "Cero valores hardcodeados. Todo usa var(--token)"),
        ("✅ Responsive", "Funciona de 320px a 2560px sin scroll horizontal"),
        ("✅ Mobile First", "CSS base es para móvil, escala con min-width"),
        ("✅ Dark Mode", "Automático + toggle manual, sin parpadeo al cargar"),
        ("✅ Accesibilidad", "Skip link, focus-visible, contraste 4.5:1, navegable con Tab"),
        ("✅ Imágenes", "width+height definidos, loading=lazy, alt descriptivo, WebP"),
        ("✅ Formulario", ":user-invalid, aria, labels vinculados, errores claros"),
        ("✅ Animaciones", "prefers-reduced-motion respetado, solo transform/opacity"),
        ("✅ BEM + @layer", "Nomenclatura consistente, cascada organizada"),
        ("✅ Archivos CSS", "Organizados en tokens, base, components, pages, utilities"),
        ("✅ JavaScript", "Módulos ES, sin console.log en producción, sin errores en consola"),
        ("✅ Fuentes", "preconnect antes de cargar, font-display:swap"),
        ("✅ Meta tags", "title, description, og:image en todas las páginas"),
        ("✅ README.md", "Instrucciones de instalación y estructura del proyecto"),
    ]

    for check, desc in criterios:
        row_data = [[
            Paragraph(check, ParagraphStyle('ck', fontName='Helvetica-Bold',
                fontSize=8.5, textColor=C_ACCENT, leading=12, backColor=HexColor('#0d1a10'))),
            Paragraph(desc, ParagraphStyle('cd', fontName='Helvetica',
                fontSize=9, textColor=C_TEXT, leading=13)),
        ]]
        t = Table(row_data, colWidths=[4.5*cm, None])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,-1), HexColor('#0d1a10')),
            ('BACKGROUND', (1,0), (1,-1), C_CODE_BG),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 10),
            ('LINEBELOW', (0,0), (-1,-1), 1, C_BORDER),
        ]))
        items.append(t)

    items.append(spacer(16))
    items += tip("El portfolio ES tu carta de presentación técnica",
        "Un reclutador senior revisará tu código fuente. La calidad del HTML, "
        "la organización del CSS y los detalles de accesibilidad dicen más que cualquier "
        "bullet en el CV. Trata este proyecto con los mismos estándares que tendrías "
        "en un equipo de producción de nivel senior.", s)

    # Cierre
    items.append(spacer(20))
    items.append(HRFlowable(width="100%", thickness=2, color=C_ACCENT,
        spaceAfter=16, spaceBefore=0))
    items.append(Paragraph(
        "FELICITACIONES — COMPLETASTE EL LIBRO",
        ParagraphStyle('fin_t', fontName='Helvetica-Bold', fontSize=16, leading=22,
            textColor=C_ACCENT, alignment=TA_CENTER)))
    items.append(spacer(8))
    items.append(Paragraph(
        "Has aprendido los fundamentos y técnicas avanzadas del frontend moderno. "
        "La práctica constante es la clave. Sigue construyendo, sigue aprendiendo. "
        "El mejor código que escribirás es el próximo.",
        ParagraphStyle('fin_b', fontName='Helvetica-Oblique', fontSize=11, leading=18,
            textColor=C_MUTED, alignment=TA_CENTER)))

    return items

# ─────────────────────────────────────────
# MAIN: Construir el PDF
# ─────────────────────────────────────────
def build_pdf(output_path):
    s = make_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2*cm,
        rightMargin=2*cm,
        topMargin=2.2*cm,
        bottomMargin=1.8*cm,
        title="HTML & CSS Moderno 2026 — Libro de Componentes",
        author="Libro de Referencia Frontend 2026",
        subject="HTML, CSS, Componentes, UX, Responsive Design",
        creator="ReportLab + Anthropic Claude",
    )

    story = []

    # Portada
    story += make_cover(s)

    # TOC
    story += make_toc(s)

    # Capítulos
    print("Generando Cap. 1...")
    story += chapter_1(s)
    print("Generando Cap. 2...")
    story += chapter_2(s)
    print("Generando Cap. 3...")
    story += chapter_3(s)
    print("Generando Cap. 4...")
    story += chapter_4(s)
    print("Generando Cap. 5...")
    story += chapter_5(s)
    print("Generando Cap. 6...")
    story += chapter_6(s)
    print("Generando Cap. 7...")
    story += chapter_7(s)
    print("Generando Cap. 8...")
    story += chapter_8(s)
    print("Generando Cap. 9...")
    story += chapter_9(s)
    print("Generando Cap. 10...")
    story += chapter_10(s)
    print("Generando Caps. 11-13...")
    story += chapters_11_to_13(s)
    print("Generando Caps. 14-17...")
    story += chapters_14_to_17(s)
    print("Generando Proyecto Final...")
    story += final_project(s)

    # Build con canvas personalizado
    doc.build(story, onFirstPage=BookCanvas("Portada"),
              onLaterPages=BookCanvas("HTML & CSS Moderno 2026"))

    print(f"✅ PDF generado: {output_path}")
    return output_path

if __name__ == "__main__":
    output = "/mnt/user-data/outputs/libro-html-css-2026.pdf"
    build_pdf(output)