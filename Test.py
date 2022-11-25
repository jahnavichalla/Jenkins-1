#!/usr/bin/python3

import unittest
from prog1 import Addition


class TestAddition(unittest.TestCase):
    #correct test case
    def test_addition1(self):
        result = Addition(2,3)
        self.assertEqual(result,5)

              
            
if __name__ == '__main__':
    unittest.main()
