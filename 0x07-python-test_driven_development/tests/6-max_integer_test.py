import unittest

from max_integer_6 import max_integer

class TestMaxInteger(unittest.TestCase):

    def max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([10, 2, 30, 4]), 30)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)
        

if __name__ == "__main__":
    unittest.main()
