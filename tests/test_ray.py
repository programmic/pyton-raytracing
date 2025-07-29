import unittest
from scripts.vec3 import Vec3
from scripts.ray import Ray

class TestRay(unittest.TestCase):
    def setUp(self):
        self.origin = Vec3(1, 2, 3)
        self.direction = Vec3(0, 1, 0)
        self.r = Ray(self.origin, self.direction)

    def test_init_and_eq(self):
        r2 = Ray(Vec3(1, 2, 3), Vec3(0, 1, 0))
        r3 = Ray(Vec3(0, 0, 0), Vec3(1, 0, 0))
        self.assertEqual(self.r, r2)
        self.assertNotEqual(self.r, r3)

    def test_invalid_init(self):
        with self.assertRaises(TypeError):
            Ray((1, 2, 3), Vec3(0, 1, 0))
        with self.assertRaises(TypeError):
            Ray(Vec3(1, 2, 3), (0, 1, 0))

    def test_at(self):
        # at(0) should return origin
        self.assertEqual(self.r.at(0), self.origin)
        # at(2) should return origin + 2*direction
        expected = self.origin + self.direction * 2
        self.assertEqual(self.r.at(2), expected)
        # at(-1) should return origin - direction
        expected = self.origin + self.direction * -1
        self.assertEqual(self.r.at(-1), expected)

    def test_str_and_repr(self):
        s = str(self.r)
        self.assertIn("origin", s)
        self.assertIn("direction", s)
        r = repr(self.r)
        self.assertIn("ray(origin=", r)
        self.assertIn("vec3(", r)

if __name__ == "__main__":
    unittest.main()