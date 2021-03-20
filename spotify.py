import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import TOKENS

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
post_uri = 'spotify:artist:246dkjvS1zLTtiykXe5h60'



scope = 'playlist-modify-public'
username = 'xstriker9190'
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

playlist_name = 'Current Trending Songs'
playlist_description = 'Playlist created from Twitters trending songs'
spotifyObjectAuth.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)

user_input = input("Enter in a song name(quit to exit): ")
song_list = []


while user_input != 'quit':
    query = spotifyObjectAuth.search(q=user_input)
    song_list.append(query['tracks']['items'][0]['uri'])
    user_input = input("Enter in a song name(quit to exit): ")


#finding the playlist
prePlaylist = spotifyObjectAuth.current_user_playlists()
pl = prePlaylist['items'][0]['id']

#try to add songs
spotifyObjectAuth.playlist_add_items(playlist_id=pl,items=song_list,position=None)
