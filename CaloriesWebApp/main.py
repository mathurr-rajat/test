from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calory import Calory
from Temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html',
                               caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)
        temperature = Temperature(city=calories_form.city.data).get()

        calorie = Calory(temperature,
                         weight=float(calories_form.weight.data),
                         height=float(calories_form.height.data),
                         age=float(calories_form.age.data))
        calories = calorie.calculatecalory()
        return render_template('calories_form_page.html',
                               caloriesform=calories_form,
                               calories=calories,
                               result=True)


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=70)
    height = StringField('Height: ', default= 175)
    age = StringField("Age: ", default = 31)
    city = StringField('City: ', default='Pune')
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesFormPage.as_view('calories_form_page'))
app.run(debug=True)