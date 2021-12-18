import requests
from bs4 import BeautifulSoup
import configparser


def auth_lastfm():
    config = configparser.ConfigParser()
    config.read("config.cfg")
    api_key = config.get("LASTFM", "API_KEY")
    shared_secret = config.get("LASTFM", "SHARED_SECRET")
    return api_key, shared_secret


def get_artist(artist, api_key):
    artist = "http://ws.audioscrobbler.com/2.0/?method=artist.search&artist={}&api_key={}&format=json".format(
        artist, api_key
    )
    artist_json = requests.get(artist)
    return artist_json


def get_artist_info(artist, api_key):
    artist = "http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={}&api_key={}&format=json".format(
        artist, api_key
    )
    artist_json_info = requests.get(artist)
    return artist_json_info


if __name__ == "__main__":
    api_key, shared_secret = auth_lastfm()
    print("Type Artist Name:")
    artist = input()
    artist_json = get_artist(artist, api_key)
    print("The artist:")
    print(artist_json.text)
    artist_json_info = get_artist_info(artist, api_key)
    print("The info:")
    print(artist_json_info.text)
