'''test suite for super_sum.'''

#import unittest
from unittest import TestCase
from super_sum import super_sum

class SuperSumTestCase(TestCase):
#or class testcase(unittest.testcase)
    '''Test Case for super sum.'''

    def test_empty_input(self):
    	'''test empty input.'''

    	self.assertEqual(super_sum(), "please enter numbers")

