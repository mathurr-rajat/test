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
        to_pay = round(bill.amount * factor)
        return to_pay
