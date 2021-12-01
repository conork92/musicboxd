from authspot import authorise
import spotipy

def get_artists_albums(spotify,uri):
    album = spotify.artist_albums(uri,album_type="album")
    return album