#!/usr/bin/python3
"""Module Test Base"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest, TestCase):
    """Test class"""
    def setUp(self):
        """Correct nb_objects = 0"""
        Base._Base__nb_objects = 0

    def test_style_b(self):
        """Pep9"""
        ck = pep8.StyleGuide(["models/base.py"])
        self.assertEqual(ck.total_errors, 0, "fix pep8")
