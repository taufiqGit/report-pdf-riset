from reportlab.pdfgen import canvas
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter, A4
from temp_invoice import my_temp
from invoice_data import my_sale, my_prod, discount_rate, tax_rate

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

c.drawRightString(7*inch,2.1*inch,str(float(total))) # Total 
discount=round((discount_rate/100) * total,1)
c.drawRightString(4*inch,1.6*inch,str(discount_rate)+'%') # discount
c.drawRightString(7*inch,1.6*inch,'-'+str(discount)) # discount
tax=round((tax_rate/100) * (total-discount),1)
c.drawRightString(4*inch,1*inch,str(tax_rate)+'%') # tax 
c.drawRightString(7*inch,1*inch,str(tax)) # tax 
total_final=total-discount+tax
c.setFont("Times-Bold", 22)
c.setFillColorRGB(1,0,0) # font colour
c.drawRightString(7*inch,0.6*inch,str(total_final)) # tax 
c.showPage()
c.save()