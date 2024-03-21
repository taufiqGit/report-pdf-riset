from reportlab.pdfgen import canvas
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter, A4
from temp_invoice import my_temp
from invoice_data import my_sale, my_prod

c = canvas.Canvas("./invoice-01.pdf", pagesize=letter)
c = my_temp(c)

c.setFillColorRGB(0,0,1) # font colour
c.setFont("Helvetica", 20)
row_gap=0.5 # gap between each row
line_y=6.7 # location of fist Y position 
total=0

for items in my_sale:
    c.drawString(0*inch, line_y*inch, str(my_prod[items][0]))
    c.drawRightString(3.5*inch, line_y*inch, "$ " + str(my_prod[items][1]))
    c.drawRightString(5*inch, line_y*inch, str(my_sale[items]))
    sub_total = my_prod[items][1]*my_sale[items]
    c.drawRightString(7*inch, line_y*inch, "$ " + str(sub_total))
    total = round(total + sub_total, 1)
    line_y = line_y - row_gap
c.showPage()
c.save()