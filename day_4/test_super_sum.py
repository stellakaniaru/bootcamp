'''test suite for super_sum.'''

#import unittest
from unittest import TestCase
from super_sum import super_sum

class SuperSumTestCase(TestCase):
#or class testcase(unittest.testcase)
    '''Test Case for super sum.'''

    def test_empty_input(self):
    	'''test empty input.'''

    	self.assertEqual(super_sum(), 0)


    def test_sum_of_integers(self):
    	'''test sum of integers'''

    	self.assertEqual(super_sum(1, 2, 3), 6)
    	self.assertEqual(super_sum(-1, 1), 0)
    	self.assertNotEqual(super_sum(10, 20, 30), 100)

    def test_string_input_returns(self):
    	'''test string inputs returns'''

    	self.assertEqual(super_sum('string', 1, 4), 0)

    def test_sum_of_items_in_one_list(self):
    	'''test sum of items in a single string'''

     	self.assertEqual(super_sum([1, 2, 3]), 6)
    	


