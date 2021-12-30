import pandas as pd
import requests
import calendar
import pycountry_convert as pc
import numpy as np

df = pd.read_csv("artist_top_album.csv")

countries_with_artist = []
countries_no_artist = []


cal_dict = {}
for i in range(1, 13):
    cal_dict[i] = calendar.month_name[i]

found_countries = df.loc[df["artist_album_count"] != "None Found"]
not_found_countries = df.loc[df["artist_album_count"] == "None Found"]
df_artist = df.loc[df["artist_album_count"] != "None Found"]

print("running retrival of non countries")

for item in found_countries["country_link"]:
    URL = "https://www.besteveralbums.com" + item
    page = requests.get(URL)
    record = page.content
    record = str(record)
    artist = record.split("Who are the best music artists from")[1].split("?")[
        0
    ]
    countries_no_artist.append(artist)

found_countries["month_num"] = np.random.randint(
    1, 13, found_countries.shape[0]
)
found_countries["month"] = found_countries["month_num"].map(cal_dict)

print("Adding two letter country codes")
country_code = {}
for i in df_artist["country"]:
    try:
        country_code[i] = pc.country_name_to_country_alpha2(i)

    except Exception as e:
        print(e)
        country_code[i] = "not found"

print("combing data")
found_countries["country_code"] = found_countries["country"].map(country_code)

found_countries.to_csv("complete_album_list-test.csv")
countries_no_artist = pd.DataFrame(countries_no_artist)
countries_no_artist.to_csv("countries-no-artist-test.csv")
