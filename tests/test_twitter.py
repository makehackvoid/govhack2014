from twitter import Twitter
import unittest
import json
import time


class test_twitter(unittest.TestCase):

    def setUp(self):
        self.t = Twitter()

    def test_get_suburb(self):
        # need tests for oauth failure
        # t.get_tweet()
        # only works when you know what the most recent tweet on twitter is,
        # and it is a suburb with art in it (not Charnwood!)
        # self.assertEqual(self.t.get_suburb()['suburb'], 'CHARNWOOD', "Tweet not found")
        # self.assertEqual(self.t.get_suburb(), None, "same tweet again")
        None

    def test_parse_tweets(self):
        # parse tweets returns  dict {'timestamp', 'suburb', 'screen_name'}
        test = '[{"created_at":"Sat Jul 12 01:22:32 +0000 2014",'
        test = test + '"id":487768939548536840,"id_str":"487768939548536840",'
        test = test + '"text":"@artifactsact Show me a Parkes sculpture",'
        test = test + '"user":{"screen_name":"cmrn"}}]'
        jsontest = json.loads(test)
        suburb = self.t.parse_tweets(jsontest)
        ts = time.strptime("Sat Jul 12 01:22:32 +0000 2014", '%a %b %d %H:%M:%S +0000 %Y')
        tse = int(time.strftime('%s', ts))

        self.assertEqual(suburb['suburb'], 'PARKES', "valid suburb")
        self.assertEqual(suburb['screen_name'], 'cmrn', "screen name")
        self.assertEqual(suburb['timestamp'], tse, "timestamp")
        test = '[{"created_at":"Sat Jul 12 01:22:32 +0000 2014",'
        test = test + '"id":487768939548536840,"id_str":"487768939548536840",'
        test = test + '"text":"@artifactsact Show me a Parkes sculpture",'
        test = test + '"user":{"screen_name":"cmrn"}}]'
        jsontest = json.loads(test)
        suburb = self.t.parse_tweets(jsontest)
        self.assertEqual(suburb['suburb'], 'PARKES', "previous suburb")

        test = '[{"created_at":"Sat Jul 12 01:22:32 +0000 2014",'
        test = test + '"id":487768939548539999,"id_str":"487768939548536840",'
        test = test + '"text":"@mhvgovhacktest Show me a Civic sculpture",'
        test = test + '"user":{"screen_name":"cmrn"}}]'
        jsontest = json.loads(test)
        suburb = self.t.parse_tweets(jsontest)
        ts = time.strptime("Sat Jul 12 01:22:32 +0000 2014", '%a %b %d %H:%M:%S +0000 %Y')
        tse = int(time.strftime('%s', ts))
        self.assertEqual(suburb['suburb'], 'CITY', "valid suburb")
        self.assertEqual(suburb['screen_name'], 'cmrn', "screen name")
        self.assertEqual(suburb['timestamp'], tse, "timestamp")

    def tearDown(self):
        del self.t

if __name__ == '__main__':
    unittest.main()
