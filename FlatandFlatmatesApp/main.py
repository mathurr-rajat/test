from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import Flat

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        # this is convention that html file should be in templates folder
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        billform = BillForm()
        return render_template('bill_form_page.html', billform=billform)


class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)

        # we have done import for Flat module
        the_bill = Flat.Bill(float(billform.amount.data), billform.period.data)
        flatmate1 = Flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
        flatmate2 = Flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))
        return render_template('bill_form_page.html', billform=billform, name1=flatmate1.name, amount1=flatmate1.pays(the_bill, flatmate2),
                               name=flatmate2.name, amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):
    amount = StringField("Bill Amount: ", default="50000")
    period = StringField("Bill period: ", default="June 2023")

    name1 = StringField("Name1: ", default="Suresh")
    days_in_house1 = StringField("Days in the house: ", default="31")

    name2 = StringField("Name2: ", default="Ramesh")
    days_in_house2 = StringField("Days in the house: ", default="31")

    button = SubmitField("Calculate")


# It's a good practice to keep page name as class name
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form_page', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('ResultsPage'))
app.run(debug=True)
