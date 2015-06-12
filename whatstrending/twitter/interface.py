from . import api as twitter

def get_user_tweets(screen_name):
    tweets = []

    # The max number of tweets we can grab per request = 200
    new_tweets = twitter.user_timeline(screen_name=screen_name, count=200)
    tweets.extend(new_tweets)

    # save the id of the oldest tweet offsetted by one
    oldest = tweets[-1].id - 1

    while len(new_tweets) > 0:
        new_tweets = twitter.user_timeline(screen_name=screen_name,
                                       count=200, max_id=oldest)

        #save most recent tweets
        tweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = tweets[-1].id - 1

    return [ { "id": tweet.id_str
             , "created_at": tweet.created_at
             , "text": tweet.text.encode("utf-8")
             }
             for tweet in tweets]
