import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_artist_data_from_country(URL):
    page = requests.get(URL)
    record = page.content
    soup = BeautifulSoup(record, "html.parser")

    top_artists = soup.find_all("tr")

    top_artist_link = []
    top_album = top_artists[1]
    for row in top_album:
        top_artist_link.append(row.get_text())

    country_text = str(soup.h1)
    print(country_text)
    country_text = country_text.split("from ")[1].split(" <")[0]
    country = country_text
    top_artist_link.append(country_text)

    for link in top_artists[1].find_all("a"):
        top_artist_link.append(link.get("href"))

    country_rank = top_artist_link[1]
    artist = top_artist_link[2]
    artist_album_count = top_artist_link[3]
    album_name_and_rank = top_artist_link[4]
    score = top_artist_link[5]
    country = top_artist_link[6]
    country_link = top_artist_link[7]
    artist_link = top_artist_link[8]
    album_link = top_artist_link[9]

    data = {
        "country_rank": country_rank,
        "artist": artist,
        "artist_album_count": artist_album_count,
        "album_name_and_rank": album_name_and_rank,
        "score": score,
        "country": country,
        "country_link": country_link,
        "artist_link": artist_link,
        "album_link": album_link,
    }

    return data


def get_country_and_year_list(
    URL="https://www.besteveralbums.com/bandstats.php?l=ng",
):
    page = requests.get(URL)

    record = page.content
    soup = BeautifulSoup(record, "html.parser")

    link_list = []
    for i in soup.find_all("option"):
        link_id = i.get("value")
        link_text = i.get_text()
        link_url = "https://www.besteveralbums.com/bandstats.php?l={}".format(
            link_id
        )
        data = {
            "link_id": link_id,
            "link_text": link_text,
            "link_url": link_url,
        }
        link_list.append(data)

    country_list = []
    for i in range(0, 247):
        country_list.append(link_list[i])

    year_list = []
    for i in range(247, len(link_list)):
        year_list.append(link_list[i])
    return country_list, year_list


def create_df(country_list, name="artist_top_album.csv"):
    all_artists = []
    for i in country_list[1:]:
        try:
            print(i["link_url"])
            data = get_artist_data_from_country(i["link_url"])
            all_artists.append(data)
        except:
            data = {
                "country_rank": "None Found",
                "artist": "None Found",
                "artist_album_count": "None Found",
                "album_name_and_rank": "None Found",
                "score": "None Found",
                "country": "None Found",
                "country_link": i["link_url"],
                "artist_link": "None Found",
                "album_link": "None Found",
            }
            all_artists.append(data)
    df = pd.DataFrame(all_artists)
    df.to_csv(name)


def simple_album_info(url):
    page = requests.get(url)
    record = page.content
    soup = BeautifulSoup(record, "html.parser")
    results = soup.find_all("div", class_="buy-panel-text")
    for job_element in results:
        text = job_element.text.split("Overall rank: ")
        year = text[0].split(": ")[-1]
        overall_rank = text[1].split("th")[0]
    image = soup.find_all("div", class_="panel panel-default")
    for job_element in image:
        image = job_element.div.source["data-srcset"]

    album_data = {
        "year": year,
        "overall_rank": overall_rank,
        "image": image,
        "description": text,
    }
    return album_data


if __name__ == "__main__":
    country_list, year_list = get_country_and_year_list(
        URL="https://www.besteveralbums.com/bandstats.php?l=ng"
    )
    create_df(country_list, name="artist_top_album.csv")
