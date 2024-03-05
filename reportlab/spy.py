from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import (Drawing)
c = canvas.Canvas("reportlab_pdf-2.pdf")
c.drawString(10,10,"Hello World")
c.showPage()
c.save()