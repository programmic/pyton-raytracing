import unittest
from scripts.vec3 import Vec3
from scripts.material import Material
from scripts.sphere import Sphere

class TestSphere(unittest.TestCase):
    def test_init_and_eq(self):
        m = Material((1, 2, 3), 0.5)
        s1 = Sphere(Vec3(0, 0, 0), 1, m)
        s2 = Sphere(Vec3(0, 0, 0), 1, m)
        s3 = Sphere(Vec3(1, 0, 0), 1, m)
        self.assertEqual(s1, s2)
        self.assertNotEqual(s1, s3)
        self.assertEqual(s1.material, m)

if __name__ == "__main__":
    unittest.main()