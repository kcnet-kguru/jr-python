import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from quiz.quiz1 import diffBig2

test_case = [
        [[10, 5, 2], 5],
        [[2, 3, 8, 5, 7, 10], 2]
            ]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for value1, answer in test_case:
            self.assertEqual(diffBig2(value1), answer)


if __name__ == '__main__':
    unittest.main()
