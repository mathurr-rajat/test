from bs4 import BeautifulSoup
import requests


class Temperature:
    def __init__(self, city):
        self.city = city

    def get(self):
        url = "https://www.google.com/search?q=" + "weather" + self.city
        # requests instance
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')

        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # formatting data
        data = str.split('\n')
        time = data[0]
        sky = data[1]

        # getting all div tag
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text

        # getting other required data
        pos = strd.find('Wind')
        other_data = strd[pos:]

        # printing all data
        print("Temperature is", temp)
        print("Time: ", time)
        print("Sky Description: ", sky)
        print(other_data)
        return temp

#
# temperature = Temperature(city="pune", country="India")
# print(temperature.get())
