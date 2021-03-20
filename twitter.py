from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


import TOKENS

class TwitterListener(StreamListener):
    def on_data(self, data):
        """
        Takes tweets from from stream listener
        """
        print(data)
        return True
        pass

    def on_error(self, status):
        """
        Error Handler
        """
        print(status)

if __name__ == "__main__":
    print("Inside twitter.py main")
    print()

    # Listener Object
    listener = TwitterListener()

    # Authentication Process
    auth = OAuthHandler(TOKENS.TWITTER_CONSUMER_KEY, TOKENS.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TOKENS.TWITTER_ACCESS_TOKEN, TOKENS.TWITTER_ACCESS_TOKEN_SECRET)

    # # # # Stream # # # #
    # Stream of Twitter Data
    stream = Stream(auth, listener)
    # Filter Stream Data
    stream.filter(track=["Joe Biden"])

    print("Execution finished")


