from govhack2014 import app
import unittest


class test_app_startup(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200,
                         "Incorrect status code when retrieving page")

    def test_data_artsact(self):
        rv = self.app.get('/data/artsact.json')
        self.assertEqual(rv.status_code, 200,
                         "Incorrect status code when retrieving page")

    def test_data_ambient(self):
        rv = self.app.get('/ambient')
        self.assertEqual(rv.status_code, 200,
                         "Incorrect status code when retrieving page")

    def test_twitter_latest_request(self):
        rv = self.app.get('/twitter/latest_request')
        self.assertEqual(rv.status_code, 200,
                         "Incorrect status code when retrieving page")


if __name__ == '__main__':
    unittest.main()
