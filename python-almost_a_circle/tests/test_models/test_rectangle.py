#!/usr/bin/python3
"""Module Test Class Rectangle"""


import unittest
from models.rectangle import Rectangle


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

    def test_aarea_strformat_dict(self):
        self.r5 = Rectangle(2, 2)
        self.assertEqual(self.r5.area(), 4)
        self.assertEqual(self.r5.__str__(), '[Rectangle] (1) 0/0 - 2/2')
        self.assertEqual(self.r5.to_dictionary(), {'id': 1, 'width': 2, 'height': 2, 'x': 0, 'y': 0})

if __name__ == '__main__':
    unittest.main()
