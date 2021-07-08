import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from quiz.quiz2 import is_pangram

test_case = [
    ("The quick brown fox jumps over the lazy dog", True),
    ("abd", False)
]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for value1, answer in test_case:
            self.assertEqual(is_pangram(value1), answer)


if __name__ == '__main__':
    unittest.main()
