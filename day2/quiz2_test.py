import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from copy import deepcopy
from quiz.quiz2 import min_sum

# 각 두 정수 곱의 합에서 얻은 최소 합계를 구합니다.
# ex)
# minSum([5,4,2,3]) ==> return (22)
# 5*2 + 3*4 = 22
#
# minSum([12,6,10,26,3,24]) ==> return (342)
# 26*3 + 24*6 + 12*10 = 342
#
# minSum([9,2,8,7,5,4,0,6]) ==> return (74)
# 9*0 + 8*2 +7*4 +6*5 = 74

test_case = [
        [[5, 4, 2, 3], 22],
        [[12, 6, 10, 26, 3, 24], 342],
        [[9, 2, 8, 7, 5, 4, 0, 6], 74]
            ]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        copy = deepcopy(test_case)
        for value1, answer in copy:
            self.assertEqual(min_sum(value1), answer)


if __name__ == '__main__':
    unittest.main()
