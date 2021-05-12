import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from copy import deepcopy
from quiz.quiz3 import max_gap

# 주어진 배열을 정렬하여 이웃한 숫자와의 갭 차이가 제일 큰 수를 리턴하시오
# ex)
# max_gap ([13,10,5,2,9]) ==> return (4)
# 9 - 5 = 4
#
# max_gap ([-3,-27,-4,-2]) ==> return (23)
# |-4- (-27) | = 23
#
# max_gap ([-7,-42,-809,-14,-12]) ==> return (767)
# | -809- (-42) | = 767
#
# max_gap ([-54,37,0,64,640,0,-15]) ==> return (576)
# | 64 - 640 | = 576

test_case = [
        [[13, 10, 5, 2, 9], 4],
        [[-3, -27, -4, -2], 23],
        [[-7, -42, -809, -14, -12], 767],
        [[-54, 37, 0, 64, 640, 0, -15], 576]
            ]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        copy = deepcopy(test_case)
        for value1, answer in copy:
            self.assertEqual(max_gap(value1), answer)


if __name__ == '__main__':
    unittest.main()
