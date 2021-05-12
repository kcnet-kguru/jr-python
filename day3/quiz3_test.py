import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from quiz.quiz3 import productArray

# 정수의 배열 Arr[] 이 주어졌을 때 prod[i]는 Arr[i]를 제외한 나머지 요소들의 곱을 가지고 있는 같은 크기의 배열을 반환합니다.
# Example
# productArray ([12,20]) ==>  return {20,12}
# productArray ([1,5,2]) ==> return {10,2,5}
# productArray ([10,3,5,6,2]) return ==> {180,600,360,300,900}

test_case = [
        [[12, 20], [20, 12]],
        [[1, 5, 2], [10, 2, 5]],
        [[10, 3, 5, 6, 2], [180, 600, 360, 300, 900]]
            ]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for value1, answer in test_case:
            self.assertEqual(productArray(value1), answer)


if __name__ == '__main__':
    unittest.main()
