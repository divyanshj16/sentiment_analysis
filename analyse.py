from textblob import TextBlob
import tweepy
import csv
import re

def polarity(polarity):
    if polarity > 0: return 'positive'
    else : return 'negative'

# --------------------YOUR CREDENTIALS--------------------------

consumer_key = ''
consumer_secret = ''

access_token = 	''
access_token_secret = ''

#------------------------------------------------------------------

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

with open('sentiments.csv','w') as csvfile:
    csvfile = csv.writer(csvfile, delimiter=',', quotechar='|')
    for tweet in public_tweets:
        lst = []
        blob = TextBlob(tweet.text)
        print(tweet.text,blob.sentiment.polarity)
        polarity_ = polarity(blob.sentiment.polarity)
        lst.append(tweet.text)
        lst.append(polarity_)
        csvfile.writerow(lst)
