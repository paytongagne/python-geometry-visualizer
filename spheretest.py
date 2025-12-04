import math
import unittest
from sphere import volume

class TestSphereVolume(unittest.TestCase):

    def test_radius_1(self):
        expected = (4.0 / 3.0) * math.pi * (1 ** 3)
        self.assertAlmostEqual(volume(1), expected)

    def test_radius_2(self):
        expected = (4.0 / 3.0) * math.pi * (2 ** 3)
        self.assertAlmostEqual(volume(2), expected)

    def test_radius_3(self):
        expected = (4.0 / 3.0) * math.pi * (3 ** 3)
        self.assertAlmostEqual(volume(3), expected)

if __name__ == "__main__":
    unittest.main()
