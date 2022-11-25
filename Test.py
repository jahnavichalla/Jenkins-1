#!/usr/bin/python3

import unittest
from Prog1 import Addition


class TestAddition(unittest.TestCase):
    #correct test case
    def test_addition1(self):
        result = Addition(1,0)
        self.assertEqual(result,1)
              
            
if __name__ == '__main__':
    unittest.main()
