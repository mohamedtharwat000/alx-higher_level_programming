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



    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)
