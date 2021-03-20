from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
# TODO: Return Artists or Song Titles, etc

import TOKENS


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
        adjusted = status.text.upper()
        adjusted = adjusted.replace(' ','')
        adjusted = adjusted.replace('\n','')
        print(adjusted)
        if TOKENS.counter < 100:
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
if __name__ == "__main__":
    print("Inside twitter.py main")
    testHashTagList = ["music", "rich brian"]

    twitter_streamer_instance = TwitterStreamer()
    twitter_streamer_instance.streamTweets(testHashTagList)

    print("Execution finished")


