from twitter import Twitter
import unittest
import json


class test_twitter(unittest.TestCase):

    def setUp(self):
        self.t = Twitter()

    def test_get_suburb(self):
        # need tests for oauth failure
        # t.get_tweet()
        # only works when you know what the most recent tweet on twitter is,
        # and it is a suburb with art in it (not Charnwood!)
        # self.assertEqual(self.t.get_suburb(), 'Charnwood', "Tweet not found")
        # self.assertEqual(self.t.get_suburb(), None, "same tweet again")
        None

    def test_parse_tweets(self):
        test = '[{"created_at":"Sat Jul 12 01:22:32 +0000 2014",'
        test = test + '"id":487768939548536840,"id_str":"487768939548536840",'
        test = test + '"text":"@mhvgovhacktest Show me a Parkes sculpture"}]'
        jsontest = json.loads(test)
        self.assertEqual(self.t.parse_tweets(jsontest), 'PARKES', "valid suburb")
        self.assertEqual(self.t.parse_tweets(jsontest), None, "same tweet again")
        test = '[{"created_at":"Sat Jul 12 01:22:32 +0000 2014",'
        test = test + '"id":487768939548536840,"id_str":"487768939548536840",'
        test = test + '"text":"@mhvgovhacktest Show me a Charnwood sculpture"}]'
        jsontest = json.loads(test)
        self.assertEqual(self.t.parse_tweets(jsontest), None, "invalid suburb")

    def tearDown(self):
        del self.t

if __name__ == '__main__':
    unittest.main()
