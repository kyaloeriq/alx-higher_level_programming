import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_str(self):
        r = Rectangle(4, 6, 2, 2, 7)
        self.assertEqual(str(r), "[Rectangle](7) 2/2 - 4/6")

    def test_update_args(self):
        r = Rectangle(1, 1)
        r.update(3, 5, 7, 9, 11)
        self.assertEqual(str(r), "[Rectangle](3) 9/11 - 5/7")

    def test_update_kwargs(self):
        r = Rectangle(1, 1)
        r.update(id=4, width=8, height=6, x=2, y=4)
        self.assertEqual(str(r), "[Rectangle](4) 2/4 - 8/6")

if __name__ == '__main__':
    unittest.main()
