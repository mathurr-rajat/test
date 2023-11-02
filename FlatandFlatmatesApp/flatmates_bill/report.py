from fpdf import FPDF
class PdfReport:
    """
    creates pdf of bill that contains data about names,their amount due and time period
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        flatmate1_pay = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pay = str(flatmate2.pays(bill, flatmate1))
        # add some text
        pdf.set_font(family='Times', size=15, style='B')
        # if border=0 we don't have borders around the cells
        # pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align="C", ln=1)
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="C", ln=1)
        pdf.cell(w=0, h=40, txt='Total amount', border=0, align="C")
        pdf.cell(w=100, h=40, txt=str(bill.amount), border=0, align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period", border=0, align="C")
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        pdf.set_font(family='Times', size=13)
        # amount of first flatmate
        # pdf.cell(w=50, h=40, txt=flatmate1.name, border=1, align="C")
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0, align="C")
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0, ln=1)
        # amount of second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0, align="C")
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)