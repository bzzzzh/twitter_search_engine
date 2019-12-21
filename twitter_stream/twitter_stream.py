import tweepy
import json
import re
import requests
import lxml.html

CONSUMER_KEY = 'CEop2v3S3TGwYvi1OZeAkBJec'
CONSUMER_SECRET = 'pWkBa0k7YlPcaWFAuMFJKtfX8YwiZtBq84WYX8In9r5yNM1i4J'
ACCESS_TOKEN = '127900998-oj5lSpmfykGKqivkwchT7egHtrNYJJNEqdOrDJUu'
ACCESS_TOKEN_SECRET = 'Hemu3bZO00mKtGtaAXxcepYDg6Qt0GXNVAKBwZrptNN8k'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
output_file = open('data.json', 'a+')


def get_title(tweet_data):
    urls = tweet_data['entities']['urls']
    titles = []
    if len(urls) > 0:
        for url in urls:
            html = requests.get(url['expanded_url'])
            doc = lxml.html.fromstring(html.content)
            if doc.find(".//title"):
                title = doc.find(".//title").text
                if title:
                    titles.append(title.strip())

    tweet_data['url_titles'] = titles


class MyStreamListener(tweepy.StreamListener):

    def on_error(self, status_code):
        print(status_code)

    def on_data(self, raw_data):
        global output_file

        tweet = json.loads(raw_data)
        if not tweet['truncated']:
            print(tweet['text'])
            get_title(tweet)
        else:
            print(tweet['extended_tweet']['full_text'])
            get_title(tweet)

        json.dump(tweet, output_file)
        output_file.write("\n")


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode='extended')

try:
    print('Start streaming.')
    myStream.filter(languages=['en'], locations=[-118.436712, 33.455255, -117.138147, 34.400996])
except KeyboardInterrupt:
    print("Stopped.")
finally:
    print('Done.')
    myStream.disconnect()
    output_file.close()

