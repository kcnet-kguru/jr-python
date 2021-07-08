import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from quiz.quiz2 import isFlush

# ["AS", "3S", "9S", "KS", "4S"]  ==> true
# ["AD", "4S", "7H", "KS", "10S"] ==> false

test_case = [
        [["AS", "3S", "9S", "KS", "4S"], True],
        [["AD", "4S", "7H", "KS", "10S"], False]
            ]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for value1, answer in test_case:
            self.assertEqual(isFlush(value1), answer)


if __name__ == '__main__':
    unittest.main()
