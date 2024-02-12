import unittest
from base import Base

class testBase(unittest.TestCase):

    def test_id(self):
        # Test if ids are properly generated
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_inst_id(self):
        # Test custom id instantiation
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_set_id(self):
        # Test manually setting of id
        b = Base()
        b.set_id(5)
        self.assertEqual(b.id, 5)

if __name__ == '__main__':
    unittest.main()
