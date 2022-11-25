#!/usr/bin/python3

import unittest
from Prog1 import Addition



class TestAddition(unittest.TestCase):
    #correct test case
    def test_addition1(self):
        result = Addition(2,3)
        self.assertEqual(result,5)


    #correct test case
    def test_addition1(self):
        result = Addition(54,9)
        self.assertEqual(result,63)

    #correct test case
    def test_addition1(self):
        result = Addition(1,0)
        self.assertEqual(result,1)

    #wrong test case
    def test_addition1(self):
        result = Addition(5,4)
        self.assertEqual(result,1)

    #wrong test case
    def test_addition1(self):
        result = Addition(1,8)
        self.assertEqual(result,8)                

            
if __name__ == '__main__':
    unittest.main()
