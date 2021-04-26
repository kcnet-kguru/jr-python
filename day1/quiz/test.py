import unittest
import quiz1
import quiz2
import datetime

test_case = [
    [(22, 20),
    (25, 30),
    (37, 40)],
    [(1, 2, 2, 8),
     (2, 3, 3, 38)
     ]
]

class Test(unittest.TestCase):
    def test1(self):
        print("\nSolution #1 Unittest")
        for idx, case in enumerate(test_case[0]):
            start_time = datetime.datetime.now()
            self.assertEqual(quiz1.closest_multiple_10(case[0]), case[1])
            end_time = datetime.datetime.now()
            print(f"TestCase #{idx} : {end_time - start_time}")

    def test2(self):
        print("\nSolution #2 Unittest")
        for idx, case in enumerate(test_case[1]):
            start_time = datetime.datetime.now()
            self.assertEqual(quiz2.magical_well(case[0], case[1], case[2]), case[3])
            end_time = datetime.datetime.now()
            print(f"TestCase #{idx} : {end_time - start_time}")


if __name__ == '__main__':
    unittest.main()