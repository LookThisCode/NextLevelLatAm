'''
Created on Nov 27, 2012

@author: mmoran
'''
from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
import tweepy
import urllib2
import urllib
import json
import uuid


consumer_key1 = "eYAdQJ5kxwjkkWSBmf2eQ"
consumer_secret1 = "IwaO986ppCHEZ0jnH6xVxg4qEeKv4Jwk1MfxmahZc"

access_token1 = "259374532-b8KQODTiq8yS9MhHfuDP10C0oj5UIkeJ8AKqnETN"
access_token_secret1 = "PgJYCrFmdpA75zLRMgzSKccF2cnlPh74uxFHwo2lr4"

consumer_key2 = "SHEqbv5UJjEwrc4E5e3jA"
consumer_secret2 = "S2vILJ6l3kqdxoID1z38pE6VxOdOAIyxEUeraAkXkQ"

access_token2 = "259374532-II6RNvM8BeCwLmzeMKxZeBcIFL8Rq1T2mBtXgiYY"
access_token_secret2 = "UQaSTQo9ePovxZNVNl1w4A0eNup67RleZBxEgW8IU4"

BASE_URL = 'http://localhost:8080/'


class MyStreamListener(StreamListener):
    def __init__(self, api=None):
        StreamListener.__init__(self, api=api)
 
    def on_status(self, status):
        resp = urllib.urlopen(BASE_URL + 'backend/predict?%s'%urllib.urlencode({'text':status.text}))
        data = json.load(resp)
        if data['outputLabel'] != 'normal':
            code = uuid.uuid4()
            print status.entities['user_mentions'][0]['id']
            bdata = dict(code=code,
                         victims=status.entities['user_mentions'][0]['id'],
                         content=status.text, 
                         scrapper=status.author.id,
                         level=data['outputLabel'],
                         insert=True)
            params = urllib.urlencode(bdata)
            r = urllib2.Request(BASE_URL + 'bullying/')
            r.add_header('User-Agent', 'awesome fetcher')
            r.add_data(params)
            resp = urllib2.urlopen(r)

            args = {"text":status.text,
                    "code":code,
                    "level":data['outputLabel'],
                    "victims":[x['name'] for x in status.entities['user_mentions']],
                    "scrapper":status.author.screen_name}
            resp = urllib.urlopen(BASE_URL + 'notifier/broadcast', urllib.urlencode(args))
            r = json.load(resp)

            
            
    def on_error(self, status_code):
        print "ERROR: ",status_code
 
    def on_limit(self, track):
        print "LIMIT: ", track
 
    def on_timeout(self):
        print "TIMEOUT!"

def filter_follow(follow):
    auth = OAuthHandler(consumer_key1, consumer_secret1)
    auth.set_access_token(access_token1, access_token_secret1)
    stream = Stream(auth, MyStreamListener())
    api = API(auth)
    #print 'start filter track ', ','.join(track)
    stream.filter(follow=follow)

def filter_track(follow):
    auth = OAuthHandler(consumer_key2, consumer_secret2)
    auth.set_access_token(access_token2, access_token_secret2)
    stream = Stream(auth, MyStreamListener())
    api = API(auth)
    #print 'start filter track ', ','.join(track)
    stream.filter(track=follow)


if __name__ == '__main__':
    resp = urllib.urlopen(BASE_URL + 'supervisados/')
    follow = [s for s in json.load(resp)['results']]
    filter_follow(follow)

