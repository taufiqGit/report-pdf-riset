from reportlab.pdfgen import canvas
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter, A4
from temp_invoice import my_temp

c = canvas.Canvas("./invoice-01.pdf", pagesize=letter)
c = my_temp(c)

c.showPage()
c.save()