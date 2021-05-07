import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from copy import deepcopy
from quiz.quiz1 import closest_multiple_10

test_case = [
        [22, 20],
        [35, 30],
        [37, 40]
            ]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        copy = deepcopy(test_case)
        for case, answer in copy:
            self.assertEqual(closest_multiple_10(case), answer)


if __name__ == '__main__':
    unittest.main()
