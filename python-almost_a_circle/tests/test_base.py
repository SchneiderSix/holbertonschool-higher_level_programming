#!/usr/bin/python3
"""Module Test Base"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest, TestCase):
    """Test class"""
    def test_none(self):
        b = Base(None)
        self.assertEqual(base.id, 1)
        b = Base()
        self.assertEqual(base.id, 2)
        b = Base(6)
        self.assertEqual(base.id, 6)

if __name__ == '__main__':
    unittest.main()
