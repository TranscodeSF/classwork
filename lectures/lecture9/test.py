import unittest
import binarysearch

class TestSearch(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1, binarysearch.search([0,1,2], 1))

if __name__ == '__main__':
    unittest.main()
