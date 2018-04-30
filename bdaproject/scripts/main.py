
#tweepy api
import sys, tweepy

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

# what tweets to find and how many
searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q=searchTerm, result_type="recent", lang="es", tweet_mode="extended").items(noOfSearchTerms)

username = ''
retweeted = False;
retweeted_times = 0
tweet_text= ''
cleaned_tweet = ''
positive_tweets = 0
negative_tweet = 0
neutral_tweets = 0

for tweet in tweets:
    username = tweet.user.screen_name
    retweeted = 'retweeted_status' in dir(tweet)
    retweeted_times = tweet.retweet_count
    if(retweeted):
        tweet_text = tweet.retweeted_status.full_text
    else:
        tweet_text = tweet.full_text
    
    cleaned_tweet = tweetFormater.cleanText(tweet_text)
    # print("tweet username: " + username)
    # print("Tweet Text: " + cleaned_tweet)
    # print("tweet retuits: " + str(retweeted_times))
    # print("SENTIMENT: " + str(indicoio.sentiment(cleaned_tweet, language="SPANISH")))
    translated_text = translator.translate(cleaned_tweet)
    sentiment = indicoio.sentiment_hq(translated_text.text)
    if(sentiment > 0.8):
        positive_tweets = positive_tweets + 1
        print("----------------------------")
        print("Tweet Text: " + tweet_text)
        print("----------POSITIVE----------")
    elif(sentiment > 0.5 and sentiment < 0.8):
        neutral_tweets = neutral_tweets + 1
        print("----------------------------")
        print("Tweet Text: " + tweet_text)
        print("----------NEUTRAL-----------")
    elif(sentiment < 0.5):
        negative_tweet = negative_tweet + 1
        print("----------------------------")
        print("Tweet Text: " + tweet_text)
        print("----------NEGATIVE----------")
    
print ("Positive tweets: " + str(positive_tweets))
print ("Neutral tweets: " + str(neutral_tweets))
print ("Negative tweets: " + str(negative_tweet))
