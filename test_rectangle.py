import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(5, 4), 20)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 4), 18)
        
    def test_perimeter_float(self):
        self.assertEqual(perimeter(2.5, 3.5), 12.0)
