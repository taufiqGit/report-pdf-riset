#from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib import colors
#c = canvas.Canvas("reportlab_pdf-2n.pdf")
# c.drawString(10,10,"Hello World")
# c.showPage()
# c.save()

drawing = Drawing(816, 1560)
# beige rectangle
r1 = Rect(0, 0, 100, 500, 0, 0)
r1.fillColor = colors.blue

nu = Rect(0, 0, 100, 100, 0, 0)
nu.fillColor = colors.red
drawing.add(r1)
drawing.add(nu)

drawing.save(formats=['pdf', 'png'], outDir='.', fnRoot="iku-iku-iku-iku-oo")