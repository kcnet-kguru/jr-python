import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from copy import deepcopy
from quiz.quiz1 import max_product

# max_product ([4, 3, 5], 2) ==>  return (20)
# 5 * 4 = 20
#
# max_product ([8, 10 , 9, 7], 3) ==>  return (720)
# 8 * 9 * 10 = 720
#
# max_product([10, 8, 3, 2, 1, 4, 10], 5) ==> return (9600)
# 10 * 10 * 8 * 4 * 3 = 9600
#
# max_product ([10, 3, -1, -27] , 3)  return (-30)
# 10 * 3 * -1 = -30

test_case = [
        [[4, 3, 5], 2, 20],
        [[8, 10, 9, 7], 3, 720],
        [[10, 8, 3, 2, 1, 4, 10], 5, 9600],
        [[10, 3, -1, -27], 3, -30]
            ]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        copy = deepcopy(test_case)
        for value1, value2, answer in copy:
            self.assertEqual(max_product(value1, value2), answer)


if __name__ == '__main__':
    unittest.main()
