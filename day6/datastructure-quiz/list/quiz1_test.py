import unittest
import quiz1


class TwoSumTest(unittest.TestCase):

    def test_two_sum1(self):
        answer = quiz1.twoSum(nums=[2, 7, 11, 15], target=9)
        self.assertEqual(answer, [0, 1])

    def test_two_sum2(self):
        answer = quiz1.twoSum2(nums=[2, 7, 11, 15], target=9)
        self.assertEqual(answer, [0, 1])

    def test_two_sum3(self):
        answer = quiz1.twoSum3(nums=[2, 7, 11, 15], target=9)
        self.assertEqual(answer, [0, 1])