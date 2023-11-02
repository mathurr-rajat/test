import webbrowser
from FlatandFlatmatesApp.flatmates_bill.Flat import Bill, Flatmate
from FlatandFlatmatesApp.flatmates_bill.report import PdfReport

amount = float(input("Enter bill amount     "))
period = input("enter period Ex. Dec 2023        ")
name1 = input("enter name of Flatmate 1     ")
days_in_houseName1 = int(input(f"Enter days spent in a house for 1 st flatmate   {name1}        "))

name2 = input("enter name of Flatmate 2     ")
days_in_houseName2 = int(input(f"Enter days spent in a house for 2 st flatmate   {name2}        "))

the_bill = Bill(amount, period)
Flatmate1 = Flatmate(name=name1, days_in_house=days_in_houseName1)
Flatmate2 = Flatmate(name=name2, days_in_house=days_in_houseName2)

finalamountFlatmate1 = Flatmate1.pays(bill=the_bill, flatmate2=Flatmate2)
print(f"{Flatmate1.name} needs to pay {finalamountFlatmate1} rs")

finalamountFlatmate2 = Flatmate2.pays(bill=the_bill, flatmate2=Flatmate1)
print(f"{Flatmate2.name} needs to pay {finalamountFlatmate2} rs")

object = PdfReport(filename=f"{the_bill.period}.pdf")
object.generate(flatmate1=Flatmate1, flatmate2=Flatmate2, bill=the_bill)

# Open file automatically
webbrowser.open(object.filename)
