import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from copy import deepcopy
from quiz.quiz2 import magical_well

test_case = [
        [(1, 2, 2), 8]
            ]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        copy = deepcopy(test_case)
        for case, answer in copy:
            self.assertEqual(magical_well(case[0], case[1], case[2]), answer)

if __name__ == '__main__':
    unittest.main()
