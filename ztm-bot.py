# This file is for the Streaming tweepy API
# import time, tweepy, and the create_api function from config.py
import tweepy
import time
from config import create_api
# Create a class that accepts the tweepy.StreamListener
class Fav_tweet_Retweet(tweepy.StreamListener):
# Define an __init__ function inside the class that accepts self and api parameters
    def __init__(self, api):
        self.api = api
        self.me = api.me()
# Define an on_status function inside the class that accepts self and tweet parameters, retweet and favorite if the tweet has not been already
    def on_status(self, tweet):
        if tweet.in_reply_to_status_id is not None or \
        tweet.user.id == self.me.id:
            return
        if not tweet.favorite():
            tweet.favorite()
            print("I have liked the tweet")
        if not tweet.retweet():
            tweet.retweet()
            print('Retweeted the tweet')
# Define an on_error function inside the class to catch errors
    def on_error(self, status_code):
        if status_code == 420:
            return False
        elif status_code == 429:
            time.sleep(60)
            return
        else:
            print(status_code)
################### END OF CLASS ########################

# Define a main function that takes keywords and ids and connects to the tweepy stream api using those keywords and ids to track and follow
def main(keywords, id):
    api = create_api()
    tweet_listener = Fav_tweet_Retweet(api)
    stream = tweepy.Stream(api.auth, tweet_listener)
    stream.filter(track=keywords, follow=id, languages=['en'])
# if __name__ main define keywords to search for and ids to follow and run the main function with those
if __name__ == '__main__':
    main(["#ZTM", "#Zerotomastery"], ['743086819', '2998698451', '224115510'])
