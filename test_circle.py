import math
import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertAlmostEqual(area(5), math.pi * 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)

    def test_perimeter_normal(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5)
        