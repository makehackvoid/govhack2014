from twitter import Twitter
import unittest
import json


class test_twitter(unittest.TestCase):

    def setUp(self):
        pass

    def test_index(self):
        # need tests for oauth failure
        t = Twitter()
        t.get_tweet()
        # only works when you know what the most recent tweet on twitter is
        # self.assertEqual(t.get_tweet(), 'Charnwood', "Tweet found")
        test = '[{"created_at":"Sat Jul 12 01:22:32 +0000 2014",'
        test = test + '"id":487768939548536833,"id_str":"487768939548536833",'
        test = test + '"text":"@mhvgovhacktest Show me a Charnwood sculpture"}]'
        jsontest = json.loads(test)
        self.assertEqual(t.parse_tweets(jsontest), 'Charnwood', "Tweet found")

if __name__ == '__main__':
    unittest.main()
