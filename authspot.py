import configparser

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import sys

def setup_config():
    config = configparser.ConfigParser()
    config.read('config.cfg')
    client_id = config.get('SPOTIFY', 'CLIENT_ID')
    client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
    return config, client_id, client_secret


def authorise_connection(client_id, client_secret):

    auth = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)
    spotify = spotipy.Spotify(auth_manager=auth)
    return spotify


def authorise():
    config, client_id, client_secret = setup_config()
    spotify = authorise_connection(client_id, client_secret)
    return spotify