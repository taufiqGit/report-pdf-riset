from reportlab.pdfgen import canvas
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter, A4
from temp_marksheet import my_temp

c = canvas.Canvas("./markshit.pdf", pagesize=letter)
c = my_temp(c)

c.setFillColorRGB(1,0,0)
c.setFont("Helvetica", 70)
c.drawRightString(5.5*inch, 6.5*inch, 'INI Report')

c.showPage()
c.save()