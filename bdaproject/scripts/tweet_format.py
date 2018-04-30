#emoji library
import emoji

#punctuation library
from string import punctuation

#regex module
import re

class Tweet_Format:
    @staticmethod
    def get_hashtags(text):
        return re.findall(r'#(\w+)', text)
    @staticmethod
    def get_emojis(text):
        emojis_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
        r = re.compile('|'.join(re.escape(p) for p in emojis_list))
        return list(set(r.findall(text)))
    @staticmethod
    def remove_hashtags(text):
        for hashtag in Tweet_Format.get_hashtags(text):
            text = text.replace('#' + hashtag,'')
        return text
    @staticmethod
    def remove_emojis(text):
        for e in Tweet_Format.get_emojis(text):
            text = text.replace(e,'')
        return text
    @staticmethod
    def remove_urls(text):
        return re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
    @staticmethod
    def remove_usernames(text):
        text = re.sub(r'(\A|\s)@(\w+)','',text)
        return text.strip()
    @staticmethod
    def remove_punctuations(text):
        return ''.join(c for c in text if c not in punctuation)

    @staticmethod
    def cleanText(text):
        tweet_woEmoji = Tweet_Format.remove_emojis(text)
        tweet_woHashtags = Tweet_Format.remove_hashtags(tweet_woEmoji)
        tweet_woPunctuations = Tweet_Format.remove_punctuations(tweet_woHashtags)
        tweet_woURLS = Tweet_Format.remove_urls(tweet_woPunctuations)
        tweet_woUsernames = Tweet_Format.remove_usernames(tweet_woURLS)
        cleaned_tweet = tweet_woUsernames

        return cleaned_tweet