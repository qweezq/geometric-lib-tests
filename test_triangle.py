import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(4, 5), 10.0)

    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0.0)

    def test_area_float(self):
        self.assertEqual(area(2.5, 4), 5.0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_float(self):
        self.assertEqual(perimeter(1.5, 2.5, 3.0), 7.0)

