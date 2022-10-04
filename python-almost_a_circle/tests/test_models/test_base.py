#!/usr/bin/python3
"""Module Test Class Base"""


import unittest
from models.base import Base


class TestClassBase(unittest.TestCase):
    """Testing Base"""
    def setUp(self):
        self.base1 = Base()

    def test_id_change(self):
        xbase = Base(None)
        self.assertEqual(self.xbase.id, 1)
        xbase = Base()
        self.assertEqual(self.xbase.id, 2)
        xbase = Base(6)
        self.assertEqual(self.xbase.id, 6)

if __name__ == '__main__':
    unittest.main()
