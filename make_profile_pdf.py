#!/usr/bin/env python3
"""Genera el PDF de perfil (dossier completo del sitio) en ingles y espanol."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

BRAND = HexColor(0x185FA5); BRAND_DARK = HexColor(0x0C447C)
INK = HexColor(0x1A1A1A); GREY = HexColor(0x5F5F5F); LIGHT = HexColor(0x8A8A8A); RULE = HexColor(0xDDDDDD)
PHOTO = "public/img/profile.jpg"

def styles():
    s = {}
    s['name'] = ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=22, textColor=INK, leading=24, spaceAfter=2)
    s['role'] = ParagraphStyle('role', fontName='Helvetica', fontSize=10.5, textColor=BRAND, leading=14, spaceAfter=8)
    s['tag'] = ParagraphStyle('tag', fontName='Helvetica-Oblique', fontSize=10.5, textColor=GREY, leading=15, spaceAfter=8)
    s['contact'] = ParagraphStyle('contact', fontName='Helvetica', fontSize=8.5, textColor=GREY, leading=12)
    s['h'] = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=11, textColor=BRAND_DARK, leading=14, spaceBefore=12, spaceAfter=5)
    s['body'] = ParagraphStyle('body', fontName='Helvetica', fontSize=9.5, textColor=INK, leading=14, alignment=TA_JUSTIFY, spaceAfter=4)
    s['item_h'] = ParagraphStyle('item_h', fontName='Helvetica-Bold', fontSize=9.5, textColor=INK, leading=13)
    s['item_b'] = ParagraphStyle('item_b', fontName='Helvetica', fontSize=9, textColor=GREY, leading=12.5, spaceAfter=6)
    s['pub'] = ParagraphStyle('pub', fontName='Helvetica', fontSize=9, textColor=INK, leading=13, spaceAfter=3)
    s['foot'] = ParagraphStyle('foot', fontName='Helvetica', fontSize=8, textColor=LIGHT, leading=11)
    return s

def build(path, T):
    s = styles()
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=15*mm, bottomMargin=13*mm, title="Emmanuel Gutierrez Pizarro")
    story = []
    head_left = [Paragraph("Emmanuel Gutierrez Pizarro", s['name']),
                 Paragraph(T['role'], s['role']),
                 Paragraph(T['tagline'], s['tag']),
                 Paragraph(T['contact'], s['contact'])]
    img = Image(PHOTO, width=30*mm, height=30*mm)
    head = Table([[head_left, img]], colWidths=[125*mm, 32*mm])
    head.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),
                              ('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),
                              ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    story.append(head); story.append(Spacer(1, 6))
    story.append(HRFlowable(width='100%', thickness=2, color=BRAND, spaceAfter=2))
    story.append(Paragraph(T['profile_h'], s['h']))
    story.append(Paragraph(T['profile'], s['body']))
    story.append(Paragraph(T['expertise_h'], s['h']))
    for title, desc in T['expertise']:
        story.append(Paragraph(title, s['item_h'])); story.append(Paragraph(desc, s['item_b']))
    story.append(Paragraph(T['work_h'], s['h']))
    for title, desc in T['work']:
        story.append(Paragraph(title, s['item_h'])); story.append(Paragraph(desc, s['item_b']))
    story.append(Paragraph(T['pubs_h'], s['h']))
    for line in T['pubs']:
        story.append(Paragraph("&bull;&nbsp; " + line, s['pub']))
    story.append(Paragraph(T['edu_h'], s['h']))
    for line in T['edu']:
        story.append(Paragraph("&bull;&nbsp; " + line, s['item_b']))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width='100%', thickness=0.5, color=RULE, spaceAfter=5))
    story.append(Paragraph(T['footer'], s['foot']))
    doc.build(story); print("built", path)

EN = {
  'role': "Data, AI &amp; territorial intelligence consultant &nbsp;&middot;&nbsp; Director, JP Asesores",
  'tagline': "I quantify what territories and entities produce, what they capture, and where the gap lives.",
  'contact': "jgutierrez@jpasesorescr.com &nbsp;|&nbsp; +506 6142-7330 &nbsp;|&nbsp; linkedin.com/in/emmanuelgpcr &nbsp;|&nbsp; Costa Rica",
  'profile_h': "Profile",
  'profile': ("Contador Privado Incorporado, Tax Advisor and Master in Financial Management with 13+ years working "
              "with social organizations, communities and institutions across Costa Rica and Central America. My "
              "focus: innovation, data science, impact evaluation and territorial intelligence, with growing emphasis "
              "on applied AI for social and collective good, data sovereignty, and education."),
  'expertise_h': "What I work on",
  'expertise': [
    ("Territorial intelligence", "Subnational fiscal and territorial balances, data systems and evidence for decisions at the district and municipal level."),
    ("Data science", "Analysis, indicators and data systems that turn raw information into usable evidence for action."),
    ("Impact evaluation", "Measurement of outcomes and impact for programs, projects and public interventions."),
    ("Applied AI for social good", "Artificial intelligence applied to social and collective challenges, from automation to territorial analysis."),
    ("Data sovereignty", "Community and territorial control over data: who collects it, who owns it, who decides with it."),
    ("Training &amp; education", "Capacity building and education so that tools, methods and data literacy stay in the territory."),
  ],
  'work_h': "Selected work",
  'work': [
    ("Nosara Community Census (2024)", "First district-level census in Costa Rica. 95.1% household coverage with INEC technical advisory. Foundation of the Cerebro de Nosara system."),
    ("Nosara Territorial Fiscal Balance (2024)", "First district-level fiscal study in the country. Fiscal gap above USD 55M per year, cadastral gap factor of 12.1x, 96.6% informal lodging, estimated district GDP USD 2.13B."),
    ("Cerebro de Nosara (2024-now)", "Territorial intelligence system integrating fiscal analysis, census data and participatory governance (Mapa de Voces de Nosara)."),
    ("Yo Emprendedor Costa Rica &amp; Central America (2015-2024)", "National financial template applied to hundreds of semifinalist business plans across multiple editions."),
  ],
  'pubs_h': "Publications &amp; press",
  'pubs': [
    "Fiscal Balance of the District of Nosara - Study, 2024 (English &amp; Spanish editions)",
    "Nosara District Population and Housing Census 2024 - Census report",
    "\"Nosara: learning about data and narratives\" - Op-ed, Semanario Universidad, 2026",
    "Nosara generates $1.9B a year, receives $25k in direct investment - Semanario Universidad, 2026",
    "Guanacaste in English: Dollars and Luxury... - El Faro, 2025",
    "Nosara presents its first district census - CRHoy / Delfino.cr, 2025",
    "Full list and links at egutierrezp23.github.io/publicaciones",
  ],
  'edu_h': "Education &amp; certifications",
  'edu': [
    "Master in Financial Management - Euncet Business School, Barcelona, Spain (2019)",
    "Specialization in Financial Management - The George Washington University, Washington D.C. (2019)",
    "Contador Privado Incorporado (CPI) &amp; Tax Advisor - Costa Rica",
    "Small Business Development Center (SBDC) certification - INA, MEIC &amp; U.S. Embassy",
  ],
  'footer': "Emmanuel Gutierrez Pizarro &middot; JP Asesores S.R.L. &middot; egutierrezp23.github.io",
}

ES = {
  'role': "Consultor en datos, IA e inteligencia territorial &nbsp;&middot;&nbsp; Director, JP Asesores",
  'tagline': "Cuantifico lo que los territorios y entidades producen, lo que capturan, y donde vive la brecha.",
  'contact': "jgutierrez@jpasesorescr.com &nbsp;|&nbsp; +506 6142-7330 &nbsp;|&nbsp; linkedin.com/in/emmanuelgpcr &nbsp;|&nbsp; Costa Rica",
  'profile_h': "Perfil",
  'profile': ("Contador Privado Incorporado, Asesor Tributario y Master en Administracion Financiera con mas de 13 "
              "anos trabajando con organizaciones sociales, comunidades e instituciones en Costa Rica y Centroamerica. "
              "Mi foco: innovacion, ciencia de datos, evaluacion de impacto e inteligencia territorial, con enfasis "
              "creciente en IA aplicada a lo social y colectivo, soberania de datos y educacion."),
  'expertise_h': "En que trabajo",
  'expertise': [
    ("Inteligencia territorial", "Balances fiscales y territoriales subnacionales, sistemas de datos y evidencia para decisiones a nivel distrital y municipal."),
    ("Ciencia de datos", "Analisis, indicadores y sistemas de datos que convierten informacion en evidencia util para la accion."),
    ("Evaluacion de impacto", "Medicion de resultados e impacto para programas, proyectos e intervenciones publicas."),
    ("IA aplicada a lo social", "Inteligencia artificial aplicada a desafios sociales y colectivos, de la automatizacion al analisis territorial."),
    ("Soberania de datos", "Control comunitario y territorial sobre los datos: quien los recoge, quien los posee, quien decide con ellos."),
    ("Capacitacion y educacion", "Formacion y educacion para que las herramientas, los metodos y la alfabetizacion de datos se queden en el territorio."),
  ],
  'work_h': "Trabajo destacado",
  'work': [
    ("Censo Comunitario de Nosara (2024)", "Primer censo a nivel de distrito en Costa Rica. 95.1% de cobertura con asesoria tecnica del INEC. Base del sistema Cerebro de Nosara."),
    ("Balance Fiscal Territorial de Nosara (2024)", "Primer estudio fiscal a nivel de distrito del pais. Brecha superior a USD 55M anuales, factor de brecha catastral 12.1x, 96.6% de alojamientos informales, PIB estimado USD 2.13B."),
    ("Cerebro de Nosara (2024-hoy)", "Sistema de inteligencia territorial que integra analisis fiscal, datos censales y gobernanza participativa (Mapa de Voces de Nosara)."),
    ("Yo Emprendedor Costa Rica y Centroamerica (2015-2024)", "Plantilla financiera nacional aplicada a cientos de planes de negocio semifinalistas durante multiples ediciones."),
  ],
  'pubs_h': "Publicaciones y prensa",
  'pubs': [
    "Balance Fiscal del Distrito de Nosara - Estudio, 2024 (ediciones en ingles y espanol)",
    "Informe Censo de Poblacion y Vivienda del Distrito de Nosara 2024",
    "\"Nosara: aprender sobre datos y relatos\" - Columna, Semanario Universidad, 2026",
    "Nosara genera 958.000 millones al ano y recibe 12 millones - Semanario Universidad, 2026",
    "Welcome to Guanacaste: la marea de dolares y lujo... - El Faro, 2025",
    "Nosara presenta su primer censo distrital - CRHoy / Delfino.cr, 2025",
    "Lista completa y enlaces en egutierrezp23.github.io/publicaciones",
  ],
  'edu_h': "Educacion y certificaciones",
  'edu': [
    "Master en Administracion Financiera - Euncet Business School, Barcelona, Espana (2019)",
    "Especializacion en Administracion Financiera - The George Washington University, Washington D.C. (2019)",
    "Contador Privado Incorporado (CPI) y Asesor Tributario - Costa Rica",
    "Certificacion Small Business Development Center (SBDC) - INA, MEIC y Embajada de EEUU",
  ],
  'footer': "Emmanuel Gutierrez Pizarro &middot; JP Asesores S.R.L. &middot; egutierrezp23.github.io",
}

build("public/files/emmanuel-gutierrez-profile-en.pdf", EN)
build("public/files/emmanuel-gutierrez-perfil-es.pdf", ES)
