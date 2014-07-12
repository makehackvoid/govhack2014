# import requests
from requests_oauthlib import OAuth1Session
import settings


class Twitter(object):
#Reads the Twitter
    list_of_burbs = ['Belconnen', 'Civic', 'Gungahlin',
                     'North Canberra', 'Parliamentary Triangle',
                     'South Canberra', 'Tuggeranong', 'Woden']

    def __init__(self):
        self.api = 'https://api.twitter.com/1.1/statuses/mentions.json?include_entities=true'
        self.access_token_url = 'https://api.twitter.com/oauth/access_token'
        self.request_token_url = 'https://api.twitter.com/oauth/request_token'

    def get_latest_suburb(self):
        return "Charnwood"  # todo, make this work

    def get_tweet(self):
        twitter_session = OAuth1Session(settings.TWITTER_CLIENT_KEY,
                                        client_secret=settings.TWITTER_CLIENT_SECRET,
                                        resource_owner_key=settings.TWITTER_RESOURCE_KEY,
                                        resource_owner_secret=settings.TWITTER_RESOURCE_SECRET)
        print(twitter_session.fetch_request_token(self.request_token_url))
        print(twitter_session.fetch_access_token(self.access_token_url))
        pass
