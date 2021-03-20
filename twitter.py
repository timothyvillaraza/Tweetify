from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re
# TODO: Return Artists or Song Titles, etc

import TOKENS
import topSongs


class artistList():
    def __init__(self):
        self.artist_list = topSongs.get_top_artists()

def parseTweet(list):
    for string in list:
        if string in artist_list:
            artist_list[string] = artist_list[string] + 1


# # # # Twitter Authenticator  # # # #
class TwitterAuthenticator():
    """
    Handles Authentication Process
    """
    def authetnicateTwitterApplication(self):
        auth = OAuthHandler(TOKENS.TWITTER_CONSUMER_KEY, TOKENS.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TOKENS.TWITTER_ACCESS_TOKEN, TOKENS.TWITTER_ACCESS_TOKEN_SECRET)
        return auth

# # # # Twitter Listener # # # #

class TwitterListener(StreamListener):

    def on_status(self, status):
        TOKENS.counter += 1
        adjusted = re.sub(r'[^a-zA-Z0-9 ]','',status.text)
        adjusted = adjusted.upper()

        word_list = adjusted.split()
        parseTweet(word_list)
        # print(adjusted)
        if(TOKENS.counter % 100 == 0):
            print(TOKENS.counter)
        if TOKENS.counter < 300:
            return True
        else:
            return False

    def on_error(self, status):
        """
        Error Handler
        """
        print(status)

class TwitterStreamer():
    def __init__(self):
        # Instance of twitter authenticator
        self.twitter_authenticator = TwitterAuthenticator()

    def streamTweets(self, hashTagList):
        """
        Displays to console
        """
        # Setup
        listener = TwitterListener()  # Implements on_data which handles code to execute when a tweet is grabbed
        auth = self.twitter_authenticator.authetnicateTwitterApplication()  # Twitter authentication instance

        # Stream instance: Listens to public tweets after authentication and handles them based on listener object

        stream = Stream(auth, listener)
        stream.filter(track=hashTagList)





# # # # USED FOR TESTING TWITTER.PY # # # #
def gettop10():
    top10ArtistsInstance = artistList()
    artist_list = top10ArtistsInstance.artist_list

    print("Inside twitter.py main")
    hashlist = list(artist_list.keys())
    hashlist.append('music')
    testHashTagList = hashlist

    twitter_streamer_instance = TwitterStreamer()
    twitter_streamer_instance.streamTweets(testHashTagList)

    #print(song_list)
    artist_list = dict(sorted(artist_list.items(), key=lambda x: x[1],reverse=True))
    top_10_artists = list(artist_list.keys())
    top_10_artists = top_10_artists[:10]

    return top_10_artists


