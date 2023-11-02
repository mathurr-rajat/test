class Bill:
    """
    Object which contains data about bill such as amount,period of bill
    """

    def __init__(self,amount,period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatmate person who lives in flat and pays a shared bill
    """

    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self,bill,flatmate2):
        factor = self.days_in_house/(self.days_in_house + flatmate2.days_in_house)
        print(f"factor = {factor}")
        to_pay = bill.amount * factor
        return to_pay


class PdfReport:
    """
    creates pdf of bill that contains data about names,their amount due and time period
    """

    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2,bill):
        pass

the_bill = Bill(amount = 12000,period = "august 2023")
Rajat = Flatmate(name = "Rajat",days_in_house = 30)
Anuj = Flatmate(name = "anuj", days_in_house = 18)

finalamount = Rajat.pays(bill = the_bill, flatmate2 = Anuj)
print(f"{Rajat.name} needs to pay {finalamount} rs")

finalamount = Anuj.pays(bill = the_bill, flatmate2=Rajat)
print(f"{Anuj.name} needs to pay {finalamount} rs")
