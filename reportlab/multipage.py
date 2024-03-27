from io import BytesIO
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm    
from reportlab.lib import colors
 
class MyPrint:

    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    @staticmethod
    def _header_footer(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()
 
        # Header
        header = Paragraph('General Leadger Card Details', styles['Normal'])
        # nu = Frame()
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + 120 - h)
 
        # Footer
        footer = Paragraph('footer', styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin + 120, h)
 
        # Release the canvas
        canvas.restoreState()


    def print_users(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)
 
        # Our container for 'Flowable' objects
        elements = []
 
        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
 
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.

        flow_obj = []
        data = [[str(x) for x in range(1, 11)], [str(x) for x in range(1, 11)], [str(x) for x in range(1, 11)], [str(x) for x in range(1, 11)]]
# t_style = TableStyle([("GRID", (0,0), (-5, -2), .1, colors.red),
#                       ("GRID", (4,1), (-1, -1), .1, colors.green)])
        t_style = TableStyle([("BOX", (0,0), (-1, -1), 2, colors.red),
                      ("FONT", (0,0), (-1, -1), "Helvetica", 20),
                      ("TEXTCOLOR", (0,0), (-1,-1), colors.white),
                      ("BACKGROUND", (0,0), (-1, -1), colors.blue),
                      ("BACKGROUND", (4,1), (-1, -1), colors.green), 
                      ])
        t = Table(data)
        t.setStyle(t_style)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        flow_obj.append(t)
        doc.build(flow_obj, onFirstPage=self._header_footer, onLaterPages=self._header_footer,
                  canvasmaker=NumberedCanvas)
 
        # Get the value of the BytesIO buffer and write it to the response.
        #pdf = buffer.getvalue()
        #buffer.close()
        #return pdf

    '''
        Usage with django
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
        # Change the position of this to wherever you want the page number to be
        self.setFont("Helvetica", .15 * inch)
        self.drawRightString(35 * mm, 5 * mm + (0.1 * inch),
                             "Page %d of %d" % (self._pageNumber, page_count))
        self.setStrokeColor(colors.darkblue) #LINE COLOR
        self.setLineWidth(.2)
        self.line(0.5*inch,.5*inch,8*inch,.5*inch)




if __name__ == '__main__':
    buffer = BytesIO()
     
    report = MyPrint(buffer, 'Letter')
    pdf = report.print_users()
    buffer.seek(0)
 
    with open('arquivo.pdf', 'wb') as f:
        f.write(buffer.read())