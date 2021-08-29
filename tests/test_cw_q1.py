import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from teasers import cw_q1 as q1


class TestTeasers(unittest.TestCase):
    def test_countVowels(self):
        """
        check the count of vowels
        """
        self.assertEqual(q1.countVowels("a quick brown fox"), 5)


if __name__ == '__main__':
    unittest.main()
