#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer_6 import max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([10, 2, 30, 4]), 30)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-5, -1, -2, -3, -4]), -1)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-5, -1, -2, -3, -4]), -1)

    def test_list_of_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
