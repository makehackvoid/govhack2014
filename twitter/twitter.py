import re
from requests_oauthlib import OAuth1Session
import settings


class Twitter(object):

    def __init__(self):
        self.suburbs = ['Belconnen', 'Civic', 'Gungahlin', 'Charnwood',
                        'North Canberra', 'Parliamentary Triangle',
                        'South Canberra', 'Tuggeranong', 'Woden']

        self.url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'

    def get_latest_suburb(self):
        return "Charnwood"  # todo, make this work

    def parse_tweets(self, response):
        for item in response:
            for word in re.findall(r"[\w']+", item['text']):
                if word in self.suburbs:
                    return word

    def get_tweet(self):
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
