import requests
from bs4 import BeautifulSoup


class GetRecipe:
    def __init__(self, link):
        self.link = link

    def get_soup(self):
        page = requests.get(self.link)
        record = page.content
        soup = BeautifulSoup(record, "html.parser")
        return soup
