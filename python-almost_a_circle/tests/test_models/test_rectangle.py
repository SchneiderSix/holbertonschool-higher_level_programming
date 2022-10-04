#!/usr/bin/python3
"""Module Test Class Rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testing Rectangle"""
    def test_arearect_str_dic(self):
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r1.area(), 2)
        self.assertEqual(self.r1.__str__(), '[Rectangle] (17) 0/0 - 1/2')
        self.assertEqual(self.r1.to_dictionary(), {'id': 17, 'width': 1, 'height': 2, 'x': 0, 'y': 0})

    def test_rect_err(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_disp(self):
        r3 = Rectangle(1, 1, 0, 0)
        self.assertEqual(r3.display(), 'None')
        r4 = Rectangle(1, 1, 1, 0)
        self.assertEqual(r4.display(), ' #\n')

if __name__ == '__main__':
    unittest.main()
