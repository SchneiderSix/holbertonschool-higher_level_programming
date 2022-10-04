#!/usr/bin/python3
"""Module Test Base"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class"""
    def test_id(self):
        """Test id"""
        b = Base(None)
        self.assertEqual(base.id, 1)
        b = Base()
        self.assertEqual(base.id, 2)
        b = Base(6)
        self.assertEqual(base.id, 6)

