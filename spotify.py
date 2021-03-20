import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import TOKENS



birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
post_uri = 'spotify:artist:246dkjvS1zLTtiykXe5h60'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=TOKENS.SPOTIPY_CLIENT_ID, client_secret=TOKENS.SPOTIPY_CLIENT_SECRET))

results = spotify.artist_albums(post_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])