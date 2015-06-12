import tweepy
from whatstrending import settings

__all__ = [
    'api'
]

auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
                           settings.TWITTER_CONSUMER_SECRET)

auth.set_access_token(settings.TWITTER_ACCESS_TOKEN,
                      settings.TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
