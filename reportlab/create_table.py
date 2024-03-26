from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors, pagesizes
from functools import partial

PAGESIZE = pagesizes.portrait(pagesizes.A4)
pdf = SimpleDocTemplate("tutor.pdf",
                         rightMargin=72,
                         leftMargin=72,
                         topMargin=72,
                         bottomMargin=72,
                         pagesizes=PAGESIZE)
flow_obj = []
styles = getSampleStyleSheet()

def header(canvas, doc, content):
    canvas.saveState()
    w, h = content.wrap(doc.width, doc.topMargin)
    content.drawOn(canvas, doc.leftMargin, doc.height + doc.bottomMargin + doc.topMargin - h)
    canvas.restoreState()

def footer(canvas, doc, content):
    canvas.saveState()
    w, h = content.wrap(doc.width, doc.bottomMargin)
    content.drawOn(canvas, doc.leftMargin, h)
    canvas.restoreState()

def header_and_footer(canvas, doc, header_content, footer_content):
    header(canvas, doc, header_content)
    footer(canvas, doc, footer_content)

data = [[str(x) for x in range(1, 11)], [str(x) for x in range(1, 11)], [str(x) for x in range(1, 11)]]
# t_style = TableStyle([("GRID", (0,0), (-5, -2), .1, colors.red),
#                       ("GRID", (4,1), (-1, -1), .1, colors.green)])
t_style = TableStyle([("BOX", (0,0), (-1, -1), 2, colors.red),
                      ("FONT", (0,0), (-1, -1), "Helvetica", 20),
                      ("TEXTCOLOR", (0,0), (-1,-1), colors.white),
                      ("BACKGROUND", (0,0), (-1, -1), colors.blue),
                      ("BACKGROUND", (4,1), (-1, -1), colors.green), 
                      ])
t = Table(data)
t.setStyle(t_style)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
flow_obj.append(t)
frame = Frame(pdf.leftMargin, pdf.bottomMargin, pdf.width, pdf.height, id='normal')

header_content = Paragraph("This is a header. testing testing testing hhuuhuhuhu  ", styles['Normal'])
footer_content = Paragraph("This is a footer. It goes on every page.  kmmommk", styles['Normal'])
template = PageTemplate(id='test', frames=frame, onPage=partial(header_and_footer, header_content=header_content, footer_content=footer_content))

pdf.addPageTemplates([template])

pdf.build(flow_obj)