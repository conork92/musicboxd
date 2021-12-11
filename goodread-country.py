import requests
from bs4 import BeautifulSoup
import json
import string

URL = "https://www.besteveralbums.com/objectindex.php?o=band&l=A"
page = requests.get(URL)

record = page.content

soup = BeautifulSoup(record, "html.parser")

mydivs1 = soup.find_all("tr", {"class": "chartrow"})
mydivs2 = soup.find_all("tr", {"class": "chartrow2"})

artists = []
for record in mydivs:
    alt_country = record.img["alt"]
    country = record.img["title"]
    country_img = record.img["src"]
    link = record.a["href"]
    artist = record.a.string
    row = {
        "alt_country": alt_country,
        "country": country,
        "country_img": country_img,
        "link": link,
        "artist": artist,
    }
    artists.append(row)

for record in mydivs2:
    alt_country = record.img["alt"]
    country = record.img["title"]
    country_img = record.img["src"]
    link = record.a["href"]
    artist = record.a.string
    row = {
        "alt_country": alt_country,
        "country": country,
        "country_img": country_img,
        "link": link,
        "artist": artist,
    }
    artists.append(row)

"https://www.besteveralbums.com/bandstats.php?l=ng"

URL = "https://www.besteveralbums.com/bandstats.php?l=ng"
page = requests.get(URL)

record = page.content
soup = BeautifulSoup(record, "html.parser")

link_list = []
for i in soup.find_all("option"):
    link_id = i.get("value")
    link_text = i.get_text()
    link_url = "https://www.besteveralbums.com/bandstats.php?l={}".format(link_id)
    data = {"link_id": link_id, "link_text": link_text, "link_url": link_url}
    link_list.append(data)

country_list = []
for i in range(0, 247):
    country_list.append(link_list[i])

year_list = []
for i in range(247, len(link_list)):
    year_list.append(link_list[i])

soup.find_all("tr")


top_artists = soup.find_all("tr")
j = 0
for i in top_artists[1]:
    print(i)

top_artist_link = []
for i.a in top_artists[1]:
    top_artist_link.append((i.a.get_text()))
top_artist_link.append(links[0]["href"])
top_artist_link.append(links[1]["href"])
