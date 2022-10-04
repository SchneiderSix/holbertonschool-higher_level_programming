#!/usr/bin/python3
"""Module Test Class Base"""


import unittest
from models.base import Base


class TestClassBase(unittest.TestCase):
    """Testing Base"""
    def setUp(self):
        self.base1 = Base()

    def test_id_change(self):
        _base = Base(None)
        self.assertEqual(self.base1.id, 1)
        _base = Base()
        self.assertEqual(self.base1.id, 2)
        _base = Base(6)
        self.assertEqual(self.base1.id, 6)

if __name__ == '__main__':
    unittest.main()
