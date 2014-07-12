import re
from requests_oauthlib import OAuth1Session
import settings


class Twitter(object):
    """
    Get latest tweet containing a suburb from the twitter account
    defined in settings.py

    ...

    Methods
    -------
    get_suburb
        return the most recent suburb in tweets or None if no
        suburbs or same tweet is still most recent.
    parse_tweets
        parsing code to look for suburb in mentions_timeline json

    """

    def __init__(self):
        self.suburbs = ['Belconnen', 'Civic', 'Gungahlin', 'Charnwood',
                        'North Canberra', 'Parliamentary Triangle',
                        'South Canberra', 'Tuggeranong', 'Woden']

        self.url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
        self.last_tweet_id = 0

    def parse_tweets(self, response):
        for item in response:
            for word in re.findall(r"[\w']+", item['text']):
                if word in self.suburbs:
                    if item['id'] != self.last_tweet_id:
                        self.last_tweet_id = item['id']
                        return word

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
