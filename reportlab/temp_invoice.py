from reportlab.lib.units import inch
from  datetime import date

def my_temp(c):
    c.translate(inch,inch)
# define font
    c.setFont("Helvetica", 14)
# choose some colors
    c.setStrokeColorRGB(0.1,0.8,0.1)
    c.setFillColorRGB(0,0,1) # font colour
    c.drawImage('./padi.png',0*inch,8.4*inch) #change path
    c.drawString(0, 8.150*inch, "1234, Buntu Road")
    c.drawString(0, 7.9*inch, "Semarang, ZIP : 50117  ")
    c.setFillColorRGB(0,0.5,1) # font colour
    c.drawString(2*inch, 7.9*inch, " www.padi.com ")
    c.setFillColorRGB(0,0,0) # font colour
    c.line(0,7.8*inch,6.8*inch,7.8*inch)
    c.drawString(5.6*inch,9.3*inch,"Bill No : 828282-aa")
    dt = date.today().strftime('%d-%b-%Y')
    c.drawString(5.6*inch,9*inch,dt) # print the date
    c.setFontSize(35)
    c.setFillColor('red')
    c.drawString(5.3*inch,8.2*inch, "INVOICE")
    c.setFont("Helvetica", 8)
    c.drawString(3*inch,9.6*inch,'Tax no : ESDF 9392020')
    c.line(0,-0.7*inch,6.8*inch,-0.7*inch)
    c.setFillColorRGB(1,0,0) # font colour
    c.drawString(0, -0.9*inch, u"\u00A9"+" padi.com")
    c.rotate(45)
    c.setFillColorCMYK(0,0,0,0.08) 
    c.setFont("Helvetica", 100)
    c.drawString(2.5*inch, 1*inch, "SAMPLE") 
    c.rotate(-45)
    c.setFillColorCMYK(0,0,0,1)
    c.setFont("Helvetica", 100)
    c.setFontSize(22)
    c.drawString(0*inch, 7.3*inch, "Products")
    c.drawString(2.8*inch, 7.3*inch, "Price")
    c.drawString(4.2*inch, 7.3*inch, "Quantity")
    c.drawString(6*inch, 7.3*inch, "Total")
    c.setStrokeColorCMYK(0,0,0,1)
    c.line(2.5*inch, 2*inch, 2.5*inch, 7.5*inch)
    c.line(3.8*inch, 2*inch, 3.8*inch, 7.5*inch)
    c.line(5.7*inch, 2*inch, 5.7*inch, 7.5*inch)
    c.drawString(1*inch,1.6*inch,'Discount')
    c.drawString(1*inch,1*inch,'Tax')
    c.setFont("Times-Bold", 22)
    c.drawString(2*inch,0.6*inch,'Total')
    c.setFont("Times-Roman", 22)
    c.drawString(5.6*inch,-0.1*inch,'Signature')
    c.setStrokeColorRGB(0.1,0.8,0.1) # Bottom Line colour 
    c.line(0,-0.7*inch,6.8*inch,-0.7*inch)
    return c