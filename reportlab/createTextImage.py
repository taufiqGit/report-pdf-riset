from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4

c = canvas.Canvas('./repot-01.pdf', pagesize=letter)

c.translate(inch, inch)
c.setStrokeColorRGB(1,0,0) #LINE COLOR
c.setLineWidth(10)
c.line(0,8*inch,7*inch,8*inch)

c.setFillColorRGB(0,0,1)
c.setFont("Helvetica", 20)
c.drawString(100, 200, 'report')
# c.setFillColorCMYK(.2, .2, 0, .39)
# c.setFillColorRGB(0, 0, 1)

c.setFillColor('lightblue')
c.setFont('Helvetica', 20)
c.setFontSize(40)
c.drawString(180, 620, "Report Pedeef")

c.rotate(45)
c.setFillColorCMYK(0,0,0,0.08)
c.setFont('Helvetica', 100)
c.drawString(2*inch, 1*inch, 'CONTOH')
c.rotate(-45)

c.drawImage('./padi.png', 0*inch, 8.2*inch)
c.setLineWidth(10)
c.setStrokeColor('yellow')
c.setFillColor('transparent')
c.rect(1*inch,2*inch,3.5*inch,5*inch,fill=1)


c.showPage()
c.save()