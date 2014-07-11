from govhack2014 import app
import unittest


class test_app_startup(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200,
                         "Incorrect status code when retrieving page")


if __name__ == '__main__':
    unittest.main()
