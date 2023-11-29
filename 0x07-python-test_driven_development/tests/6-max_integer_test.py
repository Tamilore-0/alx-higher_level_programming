#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test case class for the max_integer function.

    This class contains multiple test scenarios to ensure the max_integer
    function behaves correctly under various conditions.
    """
    def setUp(self):
        """
        Set up initial data for each test case.
        """
        self.test_empty = max_integer([])
        self.test_zero = max_integer([0, 0, 0, 0])
        self.test_positive = max_integer([1, 2, 3, 4, 5])
        self.test_bool = max_integer([1, True, False, 4])
        self.test_single_element = max_integer([1])
        self.test_negative = max_integer([-5, -3, -8, -1])
        self.test_duplicate = max_integer([10, 20, 30, 40, 40, 30])
        self.test_large_num = max_integer([999999999, 1000000000, 500000000])

    def tearDown(self):
        """
        Clean up after each test case (optional).
        """
        pass

    def test_max(self):
        """
        Test the max_integer function with various scenarios.
        """
        self.assertEqual(self.test_empty, None)
        self.assertEqual(self.test_positive, 5)
        self.assertEqual(self.test_bool, 4)
        self.assertEqual(self.test_negative, -1)
        self.assertEqual(self.test_single_element, 1)
        self.assertEqual(self.test_duplicate, 40)
        self.assertEqual(self.test_large_num, 1000000000)
        self.assertEqual(self.test_zero, 0)
