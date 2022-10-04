#!/usr/bin/python3
"""Module Test Class Base"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Testing Base"""
    def setUp(self):
        self.b = Base()

    def test_ID_change_1(self):
        self.assertEqual(self.b.id, 1)

    def test_ID_change_2(self):
        self.assertEqual(self.b.id, 2)

    def test_ID_change_3(self):
        self.assertEqual(self.b.id, 3)

    def test_ID_change_4(self):
        self.b = Base(89)
        self.assertEqual(self.b.id, 89)

if __name__ == '__main__':
    unittest.main()
