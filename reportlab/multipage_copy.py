from io import BytesIO
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table, Frame, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm    
from reportlab.lib import colors
from data_table import data_invoice
import datetime
import math
 
class MyPrint:

    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        elif pagesize == 'Landscape':
            self.pagesize = landscape(letter)

        self.width, self.height = self.pagesize

    @staticmethod
    def _header_footer(canvas, doc):
        canvas.saveState()
        styles = getSampleStyleSheet()
 
        # Header
        headerStyle = ParagraphStyle('head style', fontName='Helvetica-Bold', fontSize=11)
        header = Paragraph('General Leadger Card Details', headerStyle)
        header_second = Paragraph('PT. Java Agritech', headerStyle)
        header_third = Paragraph('General Leadger Card Details Periode 01/01/2024 to 31/01/2024')
        w, h = header.wrap(doc.width, doc.topMargin)
        w, h = header_second.wrap(doc.width, doc.height)
        w, h = header_third.wrap(doc.width, doc.height)
        header.drawOn(canvas, doc.leftMargin + 3.8*inch, doc.height + 95 - h)
        header_second.drawOn(canvas, doc.leftMargin + 4.2*inch, doc.height + 80 - h)
        header_third.drawOn(canvas, doc.leftMargin + 2.9*inch, doc.height + 66 - h)
        # Footer
        date = datetime.datetime.now()
        footer = Paragraph( str(date.day) + "/"+ str(date.month)+ "/" + str(date.year), styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin + 9*inch, h + .1*inch)
 
        # create canvas
        canvas.restoreState()


    def print_users(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=50,
                                leftMargin=50,
                                topMargin=60,
                                bottomMargin=50,
                                pagesize=self.pagesize)
 
        # Our container for 'Flowable' objects
        elements = []
 
        # Creates a table with 2 columns, variable width
        colwidths = [2.5*inch, .8*inch]

        # Two rows with variable height
        rowheights = [.4*inch, .2*inch]
        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
 
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.

        flow_obj = []
        data = [[str(x) for x in range(1, 11)], [str(x) for x in range(1, 11)], [str(x) for x in range(1, 11)], [str(x) for x in range(1, 11)]]
# t_style = TableStyle([("GRID", (0,0), (-5, -2), .1, colors.red),
#                       ("GRID", (4,1), (-1, -1), .1, colors.green)])
        arr_style = [("BOX", (0,0), (-1, -1), 2, colors.white),
                      ("FONT", (0,0), (-1, -1), "Helvetica", 8),
                      ("TEXTCOLOR", (0,0), (-1,1), colors.white),
                      ("FONT", (0,0), (-1, 0), "Helvetica-Bold", 9),
                      ("FONT", (0,2), (-1, 2), "Helvetica-Bold", 9),
                      #("FONTSIZE", (0, 0), (-1, 1), 20),
                      ("BACKGROUND", (0,0), (-1, 0), colors.darkblue),
                      ("TEXTCOLOR", (0,1), (-1,1), colors.black),
                      ("TEXTCOLOR", (0,2), (-1,2), colors.white),
                      ("BACKGROUND", (0,2), (-1, 2), colors.darkblue),
                      ("FONT", (0, -1), (-1, -1), "Helvetica-Bold", 9),
                      ('VALIGN',(0,0),(-1,-1),'MIDDLE')
                      ]
        
        for x in data_invoice: 
            print(len(x))       
            hh = False
        
            
            if len(x) < 34:
                t_style = TableStyle(arr_style)
                t = Table(x, rowHeights=.2*inch, colWidths=[2*inch,1.5*inch,1.5*inch,1.5*inch, 1.5*inch, 2.2*inch])
                t.setStyle(t_style)
                flow_obj.append(t)
                flow_obj.append(PageBreak())
                hh = False
            else:
                gsg = len(x) / 34
                selat = 34
                t_style = TableStyle(arr_style)

                for f in [x for x in range(0, math.floor(gsg))]:
                    t_style.add("BACKGROUND", (0, selat), (-1, selat), colors.darkblue)
                    t_style.add("FONT", (0,selat), (-1, selat), "Helvetica-Bold", 9)
                    t_style.add("TEXTCOLOR", (0,selat), (-1,selat), colors.white)
                    print(f, 'jsjsj', selat)
                    x.insert(selat, ["Transaction Code", "Date", "Debit Mutation", "Credit Mutation", "Balance", "Description"])
                    selat += 34
                t = Table(x, rowHeights=.2*inch, colWidths=[2*inch,1.5*inch,1.5*inch,1.5*inch, 1.5*inch, 2.2*inch])
                
                
                t.setStyle(t_style)
                flow_obj.append(t)
                
                flow_obj.append(PageBreak())
                print('kkkk', math.floor(gsg))
            # flow_obj.append(Spacer(1, .2*inch))

        doc.multiBuild(flow_obj, onFirstPage=self._header_footer, onLaterPages=self._header_footer,
                  canvasmaker=NumberedCanvas)
 
        # Get the value of the BytesIO buffer and write it to the response.
        #pdf = buffer.getvalue()
        #buffer.close()
        #return pdf

    '''
        Usage with flask or jango
    @staff_member_required
    def print_users(request):
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="My Users.pdf"'
     
        buffer = BytesIO()
     
        report = MyPrint(buffer, 'Letter')
        pdf = report.print_users()
     
        response.write(pdf)
        return response
    '''


class NumberedCanvas(canvas.Canvas):


    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []
 

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()
 

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)
 
 
    def draw_page_number(self, page_count):
        self.setFont("Helvetica", .14 * inch)
        self.drawRightString(35 * mm, 5 * mm + (0.1 * inch),
                             "Page %d of %d" % (self._pageNumber, page_count))
        self.setStrokeColor(colors.darkblue) #LINE COLOR
        self.setLineWidth(.2)
        self.line(0.5*inch,.5*inch,10.5*inch,.5*inch)




if __name__ == '__main__':
    buffer = BytesIO()
     
    report = MyPrint(buffer, 'Landscape')
    pdf = report.print_users()
    buffer.seek(0)
 
    with open('kbbr-reportlab-xie.pdf', 'wb') as f:
        f.write(buffer.read())