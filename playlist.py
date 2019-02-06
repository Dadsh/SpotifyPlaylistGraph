import spotipy
import sys
import pprint
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='43a1cf4b58e24cc9b5fb5a90ad8c1bb7',
                                                      client_secret='4436a0ee76a3474092a0dfe60703c2dc')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# results = spotify.user_playlist("dadsh", "spotify:user:dadsh:playlist:3TAWHF1eC98T4IT0anOIRW", fields="tracks")

user = "dadsh"
playlist = "spotify:user:dadsh:playlist:3TAWHF1eC98T4IT0anOIRW"

results = spotify.user_playlist_tracks(user, playlist, fields="items(track(artists(name),name,popularity,uri))")

features = spotify.audio_features(["spotify:track:62ubbkWAhTOftwgRjHS1UH"])


pprint.pprint(results['items'][3]['track']['name'])
pprint.pprint(results['items'][3]['track']['uri'])
# pprint.pprint(features)
