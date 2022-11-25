#!/usr/bin/python3

import unittest
from Prog1 import Addition
    #wrong test case
    def test_addition1(self):
        result = Addition(5,4)
        self.assertEqual(result,1)


class TestAddition(unittest.TestCase):
            
if __name__ == '__main__':
    unittest.main()
