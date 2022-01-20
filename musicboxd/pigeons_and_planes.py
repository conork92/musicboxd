import requests
from bs4 import BeautifulSoup

link = "https://www.complex.com/pigeons-and-planes/best-new-artists-august-21/"


class Pigeons:
    def __init__(self, link):
        self.link = link

    def get_simple_artist(self):
        page = requests.get(self.link)
        record = page.content
        soup = BeautifulSoup(record, "html.parser")
        mydivs = soup.find_all("a", {"class": "article-tags__tag"})
        month_str = str(soup.title)
        month = month_str.split("(")[1].split(")")[0]
        return mydivs, month

    def get_basic_artist_info(self, mydivs, month):
        month_artist = []
        for i in mydivs[3:]:
            href = i["href"]
            artist = i.text
            link_page = self.link
            data = {
                "artist": artist,
                "href": href,
                "link_page": link_page,
                "month": month,
            }
            month_artist.append(data)
        return month_artist

    def get_artist_list(self):
        mydivs, month = self.get_simple_artist()
        month_artist = self.get_basic_artist_info(mydivs, month)
        return month_artist
