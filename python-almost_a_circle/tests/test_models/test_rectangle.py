#!/usr/bin/python3
"""Module Test Class Rectangle"""


import unittest
from models.base import Rectangle


class TestRectangle(unittest.TestCase):
    """Testing Rectangle"""
    def test_initRect(self):
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(1, 2, 3, 4)
        self.r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r4.id, 5)

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

    def test_aarea(self):
        self.assertEqual(self.r4.area(), 2)

    def test_stri_form(self):
        self.assertEqual(self.r4.__str__(), '[Rectangle] (5) 3/4 - 1/2')

    def test_disp(self):
        self.r5 = Rectangle(2, 4, 0, 0)
        self.r6 = Rectangle(2, 4, 1, 0)
        self.r7 = Rectangle(2, 4, 0, 1)
        self.assertEqual(self.r5.display(), None)

    def test_dic(self):
        self.assertEqual(self.r4.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

if __name__ == '__main__':
    unittest.main()
