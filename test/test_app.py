import unittest
from math import isclose, sqrt, pi

class TestGeometry(unittest.TestCase):
    def test_triangle_rectangle(self):
        base = 3
        hauteur = 4
        hypotenuse = sqrt(base**2 + hauteur**2)
        périmètre = base + hauteur + hypotenuse
        surface = (base * hauteur) / 2
        self.assertTrue(isclose(périmètre, 12.0))
        self.assertEqual(surface, 6.0)

    def test_cercle(self):
        rayon = 1
        périmètre = 2 * pi * rayon
        surface = pi * rayon ** 2
        self.assertTrue(isclose(périmètre, 2 * pi))
        self.assertTrue(isclose(surface, pi))

if __name__ == '__main__':
    unittest.main()
