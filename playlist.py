import spotipy
import sys
import pprint
import numpy as np
import matplotlib.pyplot as plt
from spotipy.oauth2 import SpotifyClientCredentials

# Log in
client_credentials_manager = SpotifyClientCredentials(client_id='43a1cf4b58e24cc9b5fb5a90ad8c1bb7',
                                                      client_secret='4436a0ee76a3474092a0dfe60703c2dc')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get playlist
user = "dadsh"
playlist = "spotify:user:dadsh:playlist:1zeoeTuPGQsAao5uBDhaa1"
results = spotify.user_playlist_tracks(user, playlist, fields="items(track(artists(name),name,popularity,uri))")
# pprint.pprint(results)

# Get URIs of tracks
uris = []
for i in range(len(results['items'])):
    uri = results['items'][i]['track']['uri']
    uris.append(uri)

# Get features of tracks
features = spotify.audio_features(uris)
# pprint.pprint(features)

# Rebuild playlist object
pl = results['items']
for i in range(len(pl)):
    pl[i]['track']['features'] = features[i]

# Create x and y coordinates
tempo = []
energy = []
name = []
for i in range(len(pl)):
    tempo.append(pl[i]['track']['features']['tempo'])
    energy.append(pl[i]['track']['features']['energy'])
    name.append(pl[i]['track']['name'])
print(tempo)
print(energy)
print(name)

plt.scatter(tempo, energy)
for i, txt in enumerate(name):
    plt.annotate(txt, (tempo[i], energy[i]))
plt.xlabel("Tempo")
plt.ylabel("Energy")
plt.show()

# print(type(pl))
# pprint.pprint(pl)