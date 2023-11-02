from Temperature import Temperature


class Calory:

    def __init__(self, temperature, height, weight, age):
        self.temperature = temperature
        self.height = height
        self.weight = weight
        self.age = age

    def calculatecalory(self):
        self.temperature = self.temperature.replace('°C', ' ')
        result = (10 * self.weight + 6.5 * self.height + 5 -
                  float(self.temperature) * 10)
        return result


if __name__ == "__main__":
    temperature = Temperature(city="pune").get()
    calorie = Calory(temperature, weight=70, height=175, age=31)
    print(calorie.calculatecalory())
