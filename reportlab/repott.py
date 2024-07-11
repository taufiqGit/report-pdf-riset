from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def create_pdf(filename):
    document = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Data for the table
    data = [
        ["Header 1", "Header 2", "Header 3"],
        ["Row 1, Col 1", "Row 1, Col 2", "Row 1, Col 3"],
        ["Row 2, Col 1", "Row 2, Col 2", "Row 2, Col 3"],
        ["Row 3, Col 1", "Row 3, Col 2", "Row 3, Col 3"]
    ]

    # Create a table
    table = Table(data)

    # Style the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Adding padding (gaps) around cells
    style.add('LEFTPADDING', (0, 0), (-1, -1), 10)
    style.add('RIGHTPADDING', (0, 0), (-1, -1), 10)
    style.add('TOPPADDING', (0, 0), (-1, -1), 10)
    style.add('BOTTOMPADDING', (0, 0), (-1, -1), 10)

    table.setStyle(style)

    elements.append(table)
    document.build(elements)

if __name__ == "__main__":
    create_pdf("table_with_gaps.pdf")
