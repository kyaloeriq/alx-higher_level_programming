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


if __name__ == "__main__":
    unittest.main()
