import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from quiz.quiz3 import beggars


test_case = [
    ([1, 2, 3, 4, 5], 2, [9, 6]),
    ([1, 2, 3, 4, 5], 3, [7, 5, 3])
            ]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for value1, value2, answer in test_case:
            self.assertEqual(beggars(value1, value2), answer)


if __name__ == '__main__':
    unittest.main()
