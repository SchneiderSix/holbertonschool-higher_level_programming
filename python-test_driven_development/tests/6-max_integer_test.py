#!/usr/bin/python3
"""
Unittest for max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_Max_Integer(unittest.TestCase):
    "Unittests for max_integer"


    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_classic_list(self):
        """Test classic list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_unor_list(self):
        """Test unor list"""
        self.assertEqual(max_integer([1, 6, 7, 2, 6]), 7)

    def test_negative(self):
        """Test negative"""
        self.assertEqual(max_integer([-1, -6, -10, -100]), -1)

    def test_float(self):
        """Test float"""
        self.assertEqual(max_integer([9, 9.8, 9.9]), 9.9)

    def test_none(self):
        """Test none"""
        self.assertEqual(TypeError, max_integer, None)

    def test_strings(self):
        """Test strings"""
        self.assertEqual(max_integer(["low", "iq"]), "low")

if __name__ == '__main__':
    unittest.main()
