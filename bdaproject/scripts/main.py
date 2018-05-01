
#tweepy api
import sys, tweepy, time

#mongo library
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.elections_2018

#google translator to translate
from googletrans import Translator
translator = Translator()

from tweet_format import Tweet_Format
tweetFormater = Tweet_Format()

#indico library for sentiment analysis 
import indicoio
indicoio.config.api_key = 'a31b7a0762501bd8aacb747fec042df7'

#establish connection with API
consumerKey = "vSr0xlb5b0cUKre30sKmFIhO1"
consumerSecret = "l4G0CjnApxXjQD1T9MMxX1IUwsTAfBYo02WFs7mOMUwYkbRPev"
accessToken = "131291385-bF5hp8IXiqbpPFJYsm6j8F4bLx5VMM7mEiZ7SFT9"
accessTokenSecret = "79DqoAhROYvbT2p7OZNPrs1kiN7ByYjNEzjgZQauErX5Q"

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#query to find tweets
tweets = tweepy.Cursor(api.search, q='#YaSabesQuien', result_type="recent", lang="es", tweet_mode="extended").items(100)

candidate = '@lopezobrador_'

anaya = list(db.candidates.find({'username':candidate})) 
tweetFromDB = anaya[0]
old_positive_tweets = tweetFromDB['positive_tweets']
old_neutral_tweets = tweetFromDB['neutral_tweets']
old_negative_tweets = tweetFromDB['negative_tweets']

tweets_cuantity = len(tweetFromDB['tweets']) - 1
positive_tweets = 0
negative_tweets = 0
neutral_tweets = 0

for tweet in tweets:

    tweet_url = 'https://twitter.com/statuses/'+ tweet.id_str

    username = tweet.user.screen_name
    coordinates = tweet.place
    retweeted = 'retweeted_status' in dir(tweet)
    retweeted_times = tweet.retweet_count

    if(retweeted):
        tweet_text = tweet.retweeted_status.full_text
    else:
        tweet_text = tweet.full_text
        
    cleaned_tweet = tweetFormater.cleanText(tweet_text)
    translated_text = translator.translate(cleaned_tweet).text
    sentiment = indicoio.sentiment_hq(translated_text)
    if(sentiment > 0.8):
        positive_tweets = positive_tweets + 1
    elif(sentiment > 0.5 and sentiment < 0.8):
        neutral_tweets = neutral_tweets + 1
    elif(sentiment < 0.5):
        negative_tweets = negative_tweets + 1

    db.candidates.update(
    { 'username': candidate },
    {
    '$set':
        {
        "tweets."+str(tweets_cuantity+1): { 
            'username': username,
            'verified_account': tweet.user.verified,
            'favorite_count': tweet.favorite_count,
            'retweet_count': tweet.retweet_count,
            'text': tweet_text,
            'date': time.strftime("%d/%m/%Y"),
            'url': tweet_url
        }
        }
    })
    tweets_cuantity = tweets_cuantity + 1

new_positive_tweets = old_positive_tweets + positive_tweets
new_neutral_tweets = old_neutral_tweets + neutral_tweets
new_negative_tweets = old_negative_tweets + negative_tweets

db.candidates.update(
    { 'username': candidate },
    {
    '$set':
        {
        'positive_tweets': new_positive_tweets,
        'neutral_tweets': new_neutral_tweets,
        'negative_tweets': new_negative_tweets
        }
    })