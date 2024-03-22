from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle, colors
from data_table import data_table

my_doc = SimpleDocTemplate('./table-basic.pdf', pagesize=letter)
c_width=[0.4*inch, 1.5*inch, 1*inch, 1*inch]
t=Table(data_table, rowHeights=40, repeatRows=1,colWidths=c_width)
elements=[]
elements.append(t)
my_doc.build(elements)