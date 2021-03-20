import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import TOKENS

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
post_uri = 'spotify:artist:246dkjvS1zLTtiykXe5h60'



scope = 'playlist-modify-public'
username = 'daniel_hrubec'
token=SpotifyOAuth(scope=scope, username=username, client_id=TOKENS.SPOTIPY_CLIENT_ID, client_secret=TOKENS.SPOTIPY_CLIENT_SECRET, redirect_uri=TOKENS.SPOTIPY_REDIRECT_URI)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=TOKENS.SPOTIPY_CLIENT_ID, client_secret=TOKENS.SPOTIPY_CLIENT_SECRET))
spotifyObjectAuth = spotipy.Spotify(auth_manager=token)

results = spotify.artist_albums(post_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])



lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=TOKENS.SPOTIPY_CLIENT_ID, client_secret=TOKENS.SPOTIPY_CLIENT_SECRET))
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()


#creating a playlist section

playlist_name = 'twitter spotify playlist test'
playlist_description = 'bigNUT'
spotifyObjectAuth.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)




