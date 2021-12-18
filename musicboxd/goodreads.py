import requests
from bs4 import BeautifulSoup
import json
import string


def get_artist_letter(letter):

    URL = "https://www.besteveralbums.com/objectindex.php?o=band&l={}".format(
        letter
    )
    page = requests.get(URL)

    record = page.content

    soup = BeautifulSoup(record, "html.parser")

    mydivs1 = soup.find_all("tr", {"class": "chartrow"})
    mydivs2 = soup.find_all("tr", {"class": "chartrow2"})

    artists = []

    for record in mydivs1:
        alt_country = record.img["alt"]
        country = record.img["title"]
        country_img = record.img["src"]
        link = record.a["href"]
        artist = record.a.string
        artist_1 = {
            "alt_country": alt_country,
            "country": country,
            "country_img": country_img,
            "link": link,
            "artist": artist,
        }
        artists.append(artist_1)
        art_string = str(record)
        second_artist = art_string.split("</a></td>")[0].split(
            '<td class="chartstring"'
        )[1]
        alt_country = second_artist.split('<img alt="')[1].split('"')[0]
        country_img = second_artist.split('src="')[1].split('"')[0]
        country = second_artist.split('title="')[1].split('"')[0]
        link = second_artist.split('href="')[1].split('"')[0]
        artist = second_artist.split('artist">')[1]
        artist_2 = {
            "alt_country": alt_country,
            "country": country,
            "country_img": country_img,
            "link": link,
            "artist": artist,
        }
        artists.append(artist_2)

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
        second_artist = art_string.split("</a></td>")[0].split(
            '<td class="chartstring"'
        )[1]
        alt_country = second_artist.split('<img alt="')[1].split('"')[0]
        country_img = second_artist.split('src="')[1].split('"')[0]
        country = second_artist.split('title="')[1].split('"')[0]
        link = second_artist.split('href="')[1].split('"')[0]
        artist = second_artist.split('artist">')[1]
        artist_2 = {
            "alt_country": alt_country,
            "country": country,
            "country_img": country_img,
            "link": link,
            "artist": artist,
        }
        artists.append(artist_2)
    return artists


def get_all_artists():
    all_artist = []
    for c in string.ascii_lowercase:
        artists = get_artist_letter(c)
        all_artist.append(artists)
    artists = get_artist_letter("#")
    all_artist.append(artists)
    return all_artist


def make_json(all_artist):
    with open("artists.json", "w") as outfile:
        json.dump(all_artist, outfile)


if __name__ == "__main__":
    all_artist = get_all_artists()
    make_json(all_artist)
