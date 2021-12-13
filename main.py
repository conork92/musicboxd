from authspot import authorise
from get_artist import return_artist_info
from get_album_list import get_artists_albums
import class_api


if __name__ == "__main__":
    spotify = authorise()
    artist_info = return_artist_info("Nix Northwest", spotify)
    print(artist_info)
    albums = get_artists_albums(spotify, artist_info["uri"])
    result = class_api.LastpassAPI("COINDESK").get()
    result = class_api.LastpassAPI("BITSTAMP").get()
