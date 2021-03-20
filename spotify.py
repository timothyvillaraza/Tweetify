import argparse
import logging
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
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



lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=TOKENS.SPOTIPY_CLIENT_ID, client_secret=TOKENS.SPOTIPY_CLIENT_SECRET))
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()




def get_args():
    parser = argparse.ArgumentParser(description='Creates a playlist for user')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Name of Playlist')
    parser.add_argument('-d', '--description', required=False, default='',
                        help='Description of Playlist')
    return parser.parse_args()


def main():
    args = get_args()
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    user_id = sp.me()['id']
    sp.user_playlist_create(user_id, args.playlist)


if __name__ == '__main__':
    main()
