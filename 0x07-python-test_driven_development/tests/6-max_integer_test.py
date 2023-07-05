#!/usr/bin/python3

"""
    Unittest for function max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_max_integer(unittest.TestCase):
    """
        test class for function max_integer.
    """

    def test_empty_list(self):
        """
            Test for empty list.
        """
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """
            Test for one element.
        """
        self.assertEqual(max_integer([1]), 1)

    def test_list(self):
        """
            Test list.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative(self):
        """
            Test for negative numbers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all(self):
        """
            Test all numbers.
        """
        self.assertEqual(max_integer([1, -2, 3, 4.5, 5]), 5)
