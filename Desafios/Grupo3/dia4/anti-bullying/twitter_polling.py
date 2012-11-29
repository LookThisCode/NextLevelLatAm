'''
Created on Nov 27, 2012

@author: mmoran
'''
from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
import tweepy
import urllib
import json
from google.appengine.ext import db
from models import *

consumer_key = "eYAdQJ5kxwjkkWSBmf2eQ"
consumer_secret = "IwaO986ppCHEZ0jnH6xVxg4qEeKv4Jwk1MfxmahZc"

access_token = "259374532-b8KQODTiq8yS9MhHfuDP10C0oj5UIkeJ8AKqnETN"
access_token_secret = "PgJYCrFmdpA75zLRMgzSKccF2cnlPh74uxFHwo2lr4"
BASE_URL = 'http://localhost:8080/'

class MyStreamListener(StreamListener):
    def __init__(self, api=None):
        StreamListener.__init__(self, api=api)
 
    def on_status(self, status):
        resp = urllib.urlopen(BASE_URL + 'backend/predict?%s'%urllib.urlencode({'text':status.text}))
        data = json.load(resp)
        if data['outputLabel'] != 'normal':
            print data['outputLabel']
            
    def on_error(self, status_code):
        print "ERROR: ",status_code
 
    def on_limit(self, track):
        print "LIMIT: ", track
 
    def on_timeout(self):
        print "TIMEOUT!"

def filter_track():
    q = Scrapers.all().filter('','')
    follow=[s.uid for s in q]
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, MyStreamListener())
    api = API(auth)
    #print 'start filter track ', ','.join(track)
    stream.filter(follow=follow)

if __name__ == "__main__":
    filter_track()
