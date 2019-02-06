import spotipy
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + 'Tuxedo', type='artist')
print(results)
