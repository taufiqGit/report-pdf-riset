from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch, A1, A0, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

doc = SimpleDocTemplate("simple_table_grid_fire.pdf", pagesize=A4)
elements = []

data1 = [['00', '01', '02', '03', '04', '10', '11', '12', '13', '14'],
        ['10', '11', '12', '13', '14', '10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24', '10', '11', '12', '13', '14'],
        ['30', '31', '32', '33', '34', '10', '11', '12', '13', '14']]

t1 = Table(data1, 5 * [0.3 * inch], 4 * [0.2 * inch])
t1b = Table(data1, 5 * [0.3 * inch], 4 * [0.2 * inch])
# t1.setStyle(TableStyle([
#     ('BACKGROUND', (0, 0), (4, 0), colors.gray),
#     ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#     ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
# ]))


data2 = [['100', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['', '', '', '', ''],
        ['30', '31', '32', '33', '34']]
data2b = [['100', '01', '02', '03', '04'],
          ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['', '', '', '', '']
        ]

t2 = Table(data2, 10 * [0.4 * inch], 4 * [0.2 * inch])
t2b = Table(data2b, 10 * [0.4 * inch], 4 * [0.2 * inch])
# t2.setStyle(TableStyle([
#     ('BACKGROUND', (0, 0), (4, 0), colors.gray),
#     ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
#     ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
# ]))

data = [[[t1, t1b], [t2, t2b]]]
# adjust the length of tables
t1_w = 3 * inch
t2_w = 5 * inch
shell_table = Table(data, colWidths=[t1_w, t2_w])
style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        # ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        # ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        # ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

style.add('LEFTPADDING', (0, 0), (-1, -1), 10)
style.add('RIGHTPADDING', (0, 0), (-1, -1), 10)
style.add('TOPPADDING', (0, 0), (-1, -1), 10)
style.add('BOTTOMPADDING', (0, 0), (-1, -1), 10)

shell_table.setStyle(style)

elements.append(shell_table)
doc.build(elements)