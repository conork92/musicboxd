from authspot import authorise_connection, setup_config
import spotipy

import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

def return_artist_info(artist_name, spotify):
    results = spotify.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        artist_info = {"Artist":items[0]['name'],
                      "image": artist['images'][0]['url'],
                      "genres" : items[0]["genres"],
                      "id": items[0]["id"],
                      "href":items[0]['href'],
                      "images":items[0]['images'],
                      "popularity":items[0]['popularity'],
                       "type":items[0]['type'],
                       "uri": items[0]['uri']
                      }
    return artist_info


if __name__ == "__main__":
    config, client_id, client_secret = setup_config()
    spotify = authorise_connection(client_id, client_secret)
    artist_info = return_artist_info("R.A.P Ferreira", spotify)
    print(artist_info)
