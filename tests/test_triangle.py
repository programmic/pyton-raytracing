import unittest
from scripts.triangle import Triangle
from scripts.vec3 import Vec3

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.v0 = Vec3(0, 0, 0)
        self.v1 = Vec3(1, 0, 0)
        self.v2 = Vec3(0, 1, 0)
        self.tri = Triangle(self.v0, self.v1, self.v2)

    def test_eq(self):
        t2 = Triangle(Vec3(0, 0, 0), Vec3(1, 0, 0), Vec3(0, 1, 0))
        t3 = Triangle(Vec3(0, 0, 0), Vec3(1, 1, 0), Vec3(0, 1, 0))
        self.assertEqual(self.tri, t2)
        self.assertNotEqual(self.tri, t3)

    def test_get_set_item(self):
        self.assertEqual(self.tri[0], self.v0)
        self.assertEqual(self.tri[1], self.v1)
        self.assertEqual(self.tri[2], self.v2)
        vnew = Vec3(2, 2, 2)
        self.tri[1] = vnew
        self.assertEqual(self.tri[1], vnew)
        with self.assertRaises(IndexError):
            _ = self.tri[3]
        with self.assertRaises(IndexError):
            self.tri[3] = vnew
        with self.assertRaises(TypeError):
            self.tri[0] = (1, 2, 3)

    def test_str_repr(self):
        s = str(self.tri)
        r = repr(self.tri)
        self.assertIn("triangle", s)
        self.assertIn("triangle", r)

    def test_normal_and_area(self):
        n = self.tri.normal()
        self.assertIsInstance(n, Vec3)
        self.assertAlmostEqual(self.tri.area(), 0.5)

if __name__ == "__main__":
    unittest.main()