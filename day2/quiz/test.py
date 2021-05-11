import unittest
import quiz1
import quiz2
import quiz3
import datetime

test_case = [
    [([4, 3, 5], 2, 20),
    ([8, 10, 9, 7], 3, 720),
    ([10, 8, 3, 2, 1, 4, 10], 5, 9600),
     ([10, 3, -1, -27], 3, -30)
     ],
    [([5, 4, 2, 3], 22),
     ([12, 6, 10, 26, 3, 24], 342),
     ([9, 2, 8, 7, 5, 4, 0, 6], 74)
     ],
    [([13,10,5,2,9], 4),
     ([-3,-27,-4,-2], 23),
     ([-7,-42,-809,-14,-12], 767),
    ([-54,37,0,64,640,0,-15], 576)
     ]
]

class Test(unittest.TestCase):
    def test1(self):
        print("\nSolution #1 Unittest")
        for idx, case in enumerate(test_case[0]):
            start_time = datetime.datetime.now()
            self.assertEqual(quiz1.max_product(case[0], case[1]), case[2])
            end_time = datetime.datetime.now()
            print(f"TestCase #{idx} : {end_time - start_time}")

    def test2(self):
        print("\nSolution #1 Unittest")
        for idx, case in enumerate(test_case[1]):
            start_time = datetime.datetime.now()
            self.assertEqual(quiz2.min_sum(case[0]), case[1])
            end_time = datetime.datetime.now()
            print(f"TestCase #{idx} : {end_time - start_time}")

    def test3(self):
        print("\nSolution #1 Unittest")
        for idx, case in enumerate(test_case[2]):
            start_time = datetime.datetime.now()
            self.assertEqual(quiz3.max_gap(case[0]), case[1])
            end_time = datetime.datetime.now()
            print(f"TestCase #{idx} : {end_time - start_time}")

if __name__ == '__main__':
    unittest.main()