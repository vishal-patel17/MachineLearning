import tweepy
from textblob import TextBlob

consumer_key = '0dCIXfzikokHif4arhI8E3Bc2'
consumer_secret = 'rnX1GhOe56f4ku4kPLdDaF669Hpf5DM2iRNCm2cX6a545m8psP'

access_tokken = '703088268-86SghwB5cbWVjD14yCOtum0RnUccn1tqF8dBqV9c'
access_tokken_secret = 'SIUIVkKb0CYATYvz05fwvUJT3eTx4u2cMZMK2MXAIR6lP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_tokken, access_tokken_secret)

api = tweepy.API(auth)

public_tweets = api.search('ronaldo')

for tweet in public_tweets:
    print(tweet.text.encode("utf-8"))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
