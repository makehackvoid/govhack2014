import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('./tests')
    unittest.TextTestRunner().run(all_tests)
