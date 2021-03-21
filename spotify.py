import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import TOKENS
import twitter


username = ""

def setusername(str):
    global username
    username = str

def generatePlaylist():
    scope = 'playlist-modify-public'
    global username
    token=SpotifyOAuth(scope=scope, username=username, client_id=TOKENS.SPOTIPY_CLIENT_ID, client_secret=TOKENS.SPOTIPY_CLIENT_SECRET, redirect_uri=TOKENS.SPOTIPY_REDIRECT_URI)

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=TOKENS.SPOTIPY_CLIENT_ID, client_secret=TOKENS.SPOTIPY_CLIENT_SECRET))
    spotifyObjectAuth = spotipy.Spotify(auth_manager=token)



    #creating a playlist section

    playlist_name = 'Current Trending Songs'
    playlist_description = 'Playlist created from Twitters trending songs'
    spotifyObjectAuth.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)


    artist_list = twitter.gettop10()
    song_list = []

    for artist in artist_list:
        query = spotifyObjectAuth.search(q=artist)
        song_list.append(query['tracks']['items'][0]['uri'])


    #finding the playlist
    prePlaylist = spotifyObjectAuth.current_user_playlists()
    pl = prePlaylist['items'][0]['id']

    #try to add songs
    spotifyObjectAuth.playlist_add_items(playlist_id=pl,items=song_list,position=None)
