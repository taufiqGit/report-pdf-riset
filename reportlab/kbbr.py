from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate
from reportlab.lib import colors

# Define the filename for the PDF document
pdf_filename = "multi_page_tables.pdf"

# Sample data for the tables
table_data = [
    [["Name", "Age", "Country"],
     ["John", 30, "USA"],
     ["Emily", 25, "UK"],
     ["Ahmed", 35, "Egypt"],
     ["Maria", 28, "Brazil"]],
    [["ID", "City", "Population"],
     [1, "New York", "8.6M"],
     [2, "Los Angeles", "4M"],
     [3, "Chicago", "2.7M"],
     [4, "Houston", "2.3M"]]
]

# Create a SimpleDocTemplate object with a fixed page size (letter) and margin
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Define a page template for subsequent pages
page_template = PageTemplate(id='OneColumn', pagesize=letter)

# Add the page template to the document
doc.addPageTemplates([page_template])

# Loop through the table data and create tables for each page
for data in table_data:
    # Create a Table object
    table = Table(data)

    # Add style to the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Add the table to the document
    doc.build([table], canvasmaker=doc.multiBuild)

print("PDF document created successfully:", pdf_filename)
