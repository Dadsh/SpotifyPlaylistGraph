import spotipy
import sys
import pprint
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='43a1cf4b58e24cc9b5fb5a90ad8c1bb7',
                                                      client_secret='4436a0ee76a3474092a0dfe60703c2dc')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

while True:

    aname = input("Enter artist name: ")

    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = aname

    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        print(artist['name'], artist['images'][0]['url'])

    albumresults = spotify.artist_albums(artist['id'], album_type='Album')

    albums = albumresults['items']
    #pprint.pprint(albums, width=2)

    for i in range(len(albums)):
        print(albums[i]['name'])
