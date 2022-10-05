#!/usr/bin/python3
"""Module Test Class Square"""


import unittest
from io import StringIO
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    """Testing Square"""
    def test_exists(self):
        rec = Square(1, 2, 3, 4, 5)
        self.assertEqual(rec.id, 5)

    def test_arearect_str_dic(self):
        self.r1 = Square(1, 2)
        self.assertEqual(self.r1.area(), 2)
        self.assertEqual(self.r1.__str__(), '[Square] (17) 0/0 - 1/2')
        self.assertEqual(self.r1.to_dictionary(), {'id': 17, 'width': 1, 'height': 2, 'x': 0, 'y': 0})

    def test_rect_err(self):
        with self.assertRaises(TypeError):
            Square("1", 2)
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1, 2)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(0, 2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_disp(self):
        r3 = Square(1, 1, 0, 0)
        with patch('sys.stdout', new=StringIO()) as outp:
            r3.display()
        self.assertEqual(outp.getvalue(), '#\n')
        r4 = Square(1, 2, 0, 1, 2)
        with patch('sys.stdout', new=StringIO()) as out4:
            r4.display()
        self.assertEqual(out4.getvalue(), '\n#\n#\n')

    def test_nice_update(self):
        r5 = Square(3, 6)
        r5.update(6, 9)
        self.assertEqual(r5.__str__(), '[Square] (6) 6/0 - 9')
        r6 = Square(1, 2, 0, 1, 2)
        r6.update(**{ 'id': 89, 'x': -1})
        self.assertEqual(r6.__str__(), '[Square] (89) -1/1 - 1/2')
        r7 = Square(3, 2, 1)
        r7.update("choripan", None, None)
        self.assertEqual(r7.__str__(), '[Square] (choripan) 1/0 - None/None')
        r8 = Square(6, 4, id="nice")
        r8.update(None)
        self.assertEqual(r8.__str__(), '[Square] (nice) 0/0 - 6/4')

    def test_creation(self):
        cre = Square.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(cre.__str__(), '[Square] (89) 3/4 - 1/2')

    def test_savetofilerec(self):
        Square.save_to_file(None)
        with open("Square.json") as fp:
            self.assertEqual('[]', fp.read())
        Square.save_to_file([Square(1, 2)])
        with open("Square.json") as fp3:
            self.assertEqual(fp3.read(), '[{"id": 30, "x": 2, "size": 1, "y": 0}]')

    def test_loadfromfilerec(self):
        Square.save_to_file([Square(1, 2)])
        lf = Square.load_from_file()
        self.assertTrue(isinstance(lf, list))

class TestChori(unittest.TestCase):
    def test_saveempty(self):
        emlii = []
        Square.save_to_file(emlii)
        with open("Square.json") as p:
            self.assertEqual('[]', p.read())

if __name__ == '__main__':
    unittest.main()
