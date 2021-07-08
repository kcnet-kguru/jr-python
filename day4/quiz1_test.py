import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from quiz.quiz1 import count_languages

list1 = [[
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
    { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
    ], { 'C': 2, 'JavaScript': 1, 'Ruby': 1 }]



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(count_languages(list1[0]), list1[1])


if __name__ == '__main__':
    unittest.main()
