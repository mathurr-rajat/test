# api key f05608f067314113a0601cb5c755210e

import requests
from pprint import pprint


class NewsFeed:

    def __init__(self,data):
        self.data = data

    def get(self):
        pass


response = requests.get('https://newsapi.org/v2/top-headlines?country=india&apiKey=f05608f067314113a0601cb5c755210e')
content = response.text
pprint(content)