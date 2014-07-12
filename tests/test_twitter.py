from twitter import Twitter
import unittest
 
 
class test_twitter(unittest.TestCase):
 
    def setUp(self):
    	pass
 
    def test_index(self):
        t =  Twitter()
        t.get_tweet()
 
if __name__ == '__main__':
    unittest.main()