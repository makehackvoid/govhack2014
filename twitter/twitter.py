import re
import json
import os
from requests_oauthlib import OAuth1Session
import settings
import time


class Twitter(object):
    """
    Get latest tweet containing a suburb from the twitter account
    defined in settings.py

    ...

    Methods
    -------
    get_suburb
        return the most recent suburb in tweets or 'CITY' if no
        suburbs.
    parse_tweets
        parsing code to look for suburb in mentions_timeline json

    """

    def __init__(self):
        # self.suburbs = ['Belconnen', 'Civic', 'Gungahlin', 'Charnwood',
        #                'North Canberra', 'Parliamentary Triangle',
        #                'South Canberra', 'Tuggeranong', 'Woden']
        cwd = os.path.dirname(__file__)
        json_data = open(cwd + '/../govhack2014/static/artsact.json')
        data = json.load(json_data)
        suburbs = []
        for item in data:
            suburbs.append(item['suburb'])

        suburbs = set(suburbs)
        suburbs.remove('')
        suburbs.add('CIVIC')
        suburbs.add('CBD')
        suburbs.add('CONNOR')
        self.suburbs = suburbs

        self.url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
        self.last_tweet_id = 0
        self.last_tweet_time = 0
        self.last_suburb = 'CITY'
        self.last_from_user = 'mhvgovhacktest'

    def parse_tweets(self, response):
        for item in response:
            for word in re.findall(r"[\w']+", item['text']):
                word = word.upper()
                ts = time.strptime(item['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
                tsa = int(time.strftime('%s', ts))
                if word in self.suburbs:
                    if tsa >= self.last_tweet_time:
                        self.last_tweet_id = item['id']
                        self.last_tweet_time = tsa
                        self.last_from_user = item['user']['screen_name']
                        if word == 'CIVIC' or word == 'CBD':
                            word = 'CITY'
                        if word == 'CONNOR':
                            word = "O'CONNOR"
                        self.last_suburb = word
        last_tweet = {'timestamp': self.last_tweet_time,
                      'suburb': self.last_suburb,
                      'screen_name': self.last_from_user}
        return last_tweet

    def get_suburb(self):
        try:
            twitter_session = OAuth1Session(settings.TWITTER_CLIENT_KEY,
                                            client_secret=settings.TWITTER_CLIENT_SECRET,
                                            resource_owner_key=settings.TWITTER_RESOURCE_KEY,
                                            resource_owner_secret=settings.TWITTER_RESOURCE_SECRET)
            r = twitter_session.get(url=self.url)
            if r.ok:
                return self.parse_tweets(r.json())
        except:
                None
