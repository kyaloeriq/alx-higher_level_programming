import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNone(s.id)

    def test_str(self):
        s = Square(4, 2, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 2/3 - 4")

    def test_update(self):
        s = Square(1)
        s.update(3, 5, 7, 9, 11)
        self.assertEqual(str(s), "[Square] (3) 9/11 - 5")
        s.update(id=4, size=8, x=2, y=4)
        self.assertEqual(str(s), "[Square] (4) 2/4 - 8")

if __name__ == '__main__':
    unittest.main()
