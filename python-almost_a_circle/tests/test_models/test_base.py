#!/usr/bin/python3
"""Module Test Class Base"""


import unittest
from models.base import Base


class TestClassBase(unittest.TestCase):
    """Test ID"""
    def setUp(self):
        self.base1 = Base()

    def test_0(self):
        self.assertEqual(self.base1.id, 1)

    def test_1(self):
        self.assertEqual(self.base1.id, 2)

    def test_2(self):
        self.assertEqual(self.base1.id, 3)

    def test_3(self):
        self.assertEqual(self.base1.id, 4)

    def test_4(self):
        self.assertEqual(self.base1.id, 5)

    def test_5(self):
        self.assertEqual(self.base1.id, 6)

if __name__ == '__main__':
    unittest.main()
