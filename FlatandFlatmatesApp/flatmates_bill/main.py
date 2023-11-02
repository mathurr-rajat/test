import webbrowser

from fpdf import FPDF

class Bill:
    """
    Object which contains data about bill such as amount,period of bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in flat and pays a shared bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        factor = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        # print(f"factor = {factor}")
        to_pay = bill.amount * factor
        return to_pay


class PdfReport:
    """
    creates pdf of bill that contains data about names,their amount due and time period
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        flatmate1_pay = str(flatmate1.pays(bill,flatmate2))
        flatmate2_pay = str(flatmate2.pays(bill, flatmate1))
        # add some text
        pdf.set_font(family='Times', size=15, style='B')
        # if border=0 we don't have borders around the cells
        # pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align="C", ln=1)
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="C", ln=1)
        pdf.cell(w=50, h=40, txt="Period", border=0)
        pdf.cell(w=100, h=40, txt=bill.period, border=0, ln=1)
        pdf.set_font(family='Times', size=13)
        # amount of first flatmate
        # pdf.cell(w=50, h=40, txt=flatmate1.name, border=1, align="C")
        pdf.cell(w=50, h=40, txt=flatmate1.name, border=0, align="C")
        pdf.cell(w=100, h=40, txt=flatmate1_pay, border=0, ln=1)
        # amount of second flatmate
        pdf.cell(w=50, h=40, txt=flatmate2.name,border=0, align="C")
        pdf.cell(w=100, h=40, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount=11000, period="august 2023")
Rajat = Flatmate(name="Rajat", days_in_house=30)
Anuj = Flatmate(name="anuj", days_in_house=18)

finalamount = Rajat.pays(bill=the_bill, flatmate2=Anuj)
print(f"{Rajat.name} needs to pay {finalamount} rs")

finalamount = Anuj.pays(bill=the_bill, flatmate2=Rajat)
print(f"{Anuj.name} needs to pay {finalamount} rs")

# PdfReport.generate("bill.pdf", flatmate1=Rajat, flatmate2=Anuj,bill=the_bill)


object = PdfReport(filename="../file1.pdf")
object.generate(flatmate1=Rajat, flatmate2=Anuj, bill=the_bill)
webbrowser.open("../file1.pdf")
